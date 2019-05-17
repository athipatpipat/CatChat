from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth import get_user_model
from .exceptions import ClientError
from .utils import get_room_or_error
from .models import Message
from faker import Faker

User = get_user_model()

class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    This chat consumer handles websocket connections for chat clients.

    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    ##### WebSocket event handlers

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        

        # Are they logged in?
        if self.scope["user"].is_anonymous:
            # Reject the connection
            await self.close()
        else:
            # Accept the connection
            await self.accept()
        # Store which rooms the user has joined on this connection
        self.rooms = set()

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on
        command = content.get("command", None)
        print("from receive_json", content)
        try:
            if command == "join":
                # Make them join the room
                await self.join_room(content["room"],content["randomName"])
            elif command == "leave":
                # Leave the room
                await self.leave_room(content["room"],content["randomName"])
            elif command == "send":
                await self.send_room(content["room"], content["message"], content["from"], content["randomName"])
            elif command == "fetch":
                print("fetch from consumers.py")
                await self.fetch_msg(content["room"])
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({"error": e.code})


    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        # Leave all the rooms we are still in
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except ClientError:
                pass

    ##### Command helper methods called by receive_json



    ##helper to receive_json
    async def join_room(self, room_id,randomName):
        """
        Called by receive_json when someone sent a join command.
        """
        # The logged-in user is in our scope thanks to the authentication ASGI middleware
        room = await get_room_or_error(room_id, self.scope["user"])
        # Send a join message if it's turned on
        if settings.NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
            await self.channel_layer.group_send(
                room.group_name,
                {
                    "type": "chat.join",
                    "room_id": room_id,
                    "username": self.scope["user"].username,
                    "randomName": randomName,
                }
            )
        # Store that we're in the room
        self.rooms.add(room_id)
        # Add them to the group so they get room messages
        await self.channel_layer.group_add(
            room.group_name,
            self.channel_name,
        )
        # Instruct their client to finish opening the room
        await self.send_json({
            "join": str(room.id),
            "title": room.title,
        })

    ##helper to receive_json
    async def leave_room(self, room_id,randomName):
        """
        Called by receive_json when someone sent a leave command.
        """
        # The logged-in user is in our scope thanks to the authentication ASGI middleware
        room = await get_room_or_error(room_id, self.scope["user"])
        # Send a leave message if it's turned on
        if settings.NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
            await self.channel_layer.group_send(
                room.group_name,
                {
                    "type": "chat.leave",
                    "room_id": room_id,
                    "username": self.scope["user"].username,
                    "randomName": randomName,
                }
            )
        # Remove that we're in the room
        self.rooms.discard(room_id)
        # Remove them from the group so they no longer get room messages
        await self.channel_layer.group_discard(
            room.group_name,
            self.channel_name,
        )
        # Instruct their client to finish closing the room
        await self.send_json({
            "leave": str(room.id),
        })

    ##helper to receive_json
    async def send_room(self, room_id, message, author,randomName):
        """
        Called by receive_json when someone sends a message to a room.
        """
        author_user = User.objects.filter(username=author)[0]

        Message.objects.create(
            author= author_user,
            content = message,
            room_number = room_id,
            random_user = randomName,
        )


        # Check they are in this room
        if room_id not in self.rooms:
            raise ClientError("ROOM_ACCESS_DENIED")
        # Get the room and send to the group about it
        room = await get_room_or_error(room_id, self.scope["user"])
        await self.channel_layer.group_send(
            room.group_name,
            {
                "type": "chat.message",
                "room_id": room_id,
                "username": self.scope["user"].username,
                "message": message,
                "randomName": randomName,
            }
        )


    async def fetch_msg(self,room_id):
         ##fetch message from database
        load_message = Message.last_10_messages()
        formatted_message = self.messages_to_json(load_message)
        

        room = await get_room_or_error(room_id, self.scope["user"])
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_OLD_MSG,
                "room": room_id,
                "past_messages": formatted_message,
            }
            
        )




    ##helper to get_msg
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'room_number': message.room_number,
            'timestamp': str(message.timestamp),
            'randomName': message.random_user,
        }   


    ##### Handlers for messages sent over the channel layer

    # These helper methods are named by the types we send - so chat.join becomes chat_join
    async def chat_join(self, event):
        """
        Called when someone has joined our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_ENTER,
                "room": event["room_id"],
                "username": event["username"],
                "randomName": event["randomName"],
            },
        )

    async def chat_leave(self, event):
        """
        Called when someone has left our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_LEAVE,
                "room": event["room_id"],
                "username": event["username"],
                "randomName": event["randomName"],
            },
        )

    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        #edit here to add current author
        

        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": event["room_id"],
                "username": event["username"],
                "randomName": event["randomName"],
                "message": event["message"],
               
            },
        )
       

    async def chat_fetch(self, event):
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_OLD_MSG,
                "room": event["room_id"],
                "past_messages": event["past_messages"],
            }
            
        )

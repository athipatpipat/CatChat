from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Room

# Create your views here.

""" def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/index.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }) """


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "chat/index.html", {
        "rooms": rooms,
        'username': mark_safe(json.dumps(request.user.username)),
    }) 
from django.contrib import admin
from .models import Message, Room

# Register your models here.

admin.site.register(Message)

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)


from django.contrib import admin

from .models import Channel, Video
from django.contrib import admin
from .models import Stream, ChatMessage

admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Stream)
admin.site.register(ChatMessage)
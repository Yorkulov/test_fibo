from django.contrib import admin

from .models import CustomUser, MessageModel

admin.site.register(CustomUser)
admin.site.register(MessageModel)


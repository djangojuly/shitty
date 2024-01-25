from django.contrib import admin
from app.models import Post,Stories,Message,Profile,DirectMessage

# Register your models here.

admin.site.register(Post)
admin.site.register(Stories)
admin.site.register(Message)
admin.site.register(DirectMessage)
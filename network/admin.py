from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(User)
admin.site.register(Like)
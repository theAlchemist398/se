from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, Flight

admin.site.register(User)
admin.site.register(Flight)
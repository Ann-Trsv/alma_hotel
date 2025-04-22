from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Guest)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(GuestService)
admin.site.register(Payment)
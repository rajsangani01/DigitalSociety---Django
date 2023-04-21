from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Societymember)
admin.site.register(Notice)
admin.site.register(Complaint)
admin.site.register(Event)
admin.site.register(Maintenance)
admin.site.register(Transaction)
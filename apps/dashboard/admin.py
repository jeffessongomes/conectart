from django.contrib import admin
from .models import Events, Subscribe_User, Admin, TecDashImages, Our

admin.site.register(Our)
admin.site.register(TecDashImages)
admin.site.register(Events)
admin.site.register(Subscribe_User)
admin.site.register(Admin)
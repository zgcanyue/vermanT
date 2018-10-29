from django.contrib import admin
from .models import AppDate
# Register your models here.


class AppAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'adnroid', 'ios', 'address', 'test_account',)
    def save_model(self, request, obj, form, change):
        obj.test_account = request.user
        obj.save()
    readonly_fields = ('test_account',)
admin.site.register(AppDate,AppAdmin)
#!coding:utf-8
from django.contrib import admin

DATE_INPUT_FORMATS = "Y/m/d"


class BaseAdmin(admin.ModelAdmin):
    exclude = ['created', 'updated']


class ReadOnlyAdmin(BaseAdmin):
    list_display = ['__str__']

    def get_readonly_fields(self, *args, **kwargs):
        return [f.name for f in self.model._meta.fields]

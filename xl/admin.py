from django.contrib import admin
from .models import Grade_Nine, Grade_Ten, Grade_Eleven, Grade_Twelve
from import_export.admin import ImportExportModelAdmin

@admin.register(Grade_Nine)
@admin.register(Grade_Ten)
@admin.register(Grade_Eleven)
@admin.register(Grade_Twelve)
class userdata(ImportExportModelAdmin):
    pass

from django.contrib import admin

from shared.models import Contact
from modeltranslation.admin import TranslationAdmin





# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ['id', 'full_name', 'profession']
#     search_fields = ['full_name', 'profession', 'info']
#     list_filter = ['created_at', 'updated_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'subject', 'message']
    search_fields = ['full_name', 'email', 'subject']
    list_filter = ['is_read']


class MyTranslationOption(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



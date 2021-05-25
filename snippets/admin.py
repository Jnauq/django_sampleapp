from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['title', 'created']

admin.site.register(Snippet, SnippetAdmin)

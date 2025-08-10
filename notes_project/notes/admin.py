from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_title', 'user', 'created_on', 'last_update')
    list_filter = ('created_on', 'last_update')
    search_fields = ('note_title', 'note_content', 'user__user_email')
    readonly_fields = ('note_id', 'created_on', 'last_update')

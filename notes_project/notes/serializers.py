from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('note_id', 'note_title', 'note_content', 'created_on', 'last_update')
        read_only_fields = ('note_id', 'created_on', 'last_update')
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

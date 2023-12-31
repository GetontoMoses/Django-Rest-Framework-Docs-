from rest_framework import serializers
from quickstart.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    quickstart = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'quickstart']

class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
       
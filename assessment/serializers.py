"""
    Decides:
        1. What fields are accepted from request
        2. What fields are returned in response
"""
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
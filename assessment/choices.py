from django.db import models

class QuestionTypeChoices(models.TextChoices):
    GRAMMAR = 'GRAMMAR', 'Grammar'
    LISTENING = 'LISTENING', 'Listening'
    SPEAKING = 'SPEAKING', 'Speaking'
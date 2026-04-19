from django.db import models

class DifficultyChoices(models.TextChoices):
    EASY = 'EASY', 'Easy'
    MEDIUM = 'MEDIUM', 'Medium'
    HARD = 'HARD', 'Hard'

class QuestionTypeChoices(models.TextChoices):
    GRAMMAR = 'GRAMMAR', 'Grammar'
    LISTENING = 'LISTENING', 'Listening'
    SPEAKING = 'SPEAKING', 'Speaking'
    VOCABULARY = 'VOCABULARY', 'Vocabulary'
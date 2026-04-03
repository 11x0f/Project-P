from django.db import models

class DifficultyChoices(models.TextChoices):
    EASY = 'easy', 'Easy'
    MEDIUM = 'medium', 'Medium'
    HARD = 'hard', 'Hard'

class QuestionTypeChoices(models.TextChoices):
    GRAMMAR = 'GRAMMAR', 'Grammar'
    LISTENING = 'LISTENING', 'Listening'
    SPEAKING = 'SPEAKING', 'Speaking'
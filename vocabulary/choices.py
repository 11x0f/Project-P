from django.db import models

class DifficultyLevel(models.TextChoices):
    BEGINNER = 'BEGINNER', 'Beginner'
    INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
    ADVANCED = 'ADVANCED', 'Advanced'

class PartOfSpeech(models.TextChoices):
    NOUN = 'NOUN', 'Noun'
    VERB = 'VERB', 'Verb'
    ADJECTIVE = 'ADJECTIVE', 'Adjective'
    ADVERB = 'ADVERB', 'Adverb'
    PRONOUN = 'PRONOUN', 'Pronoun'
    PREPOSITION = 'PREPOSITION', 'Preposition'
    CONJUNCTION = 'CONJUNCTION', 'Conjunction'
    INTERJECTION = 'INTERJECTION', 'Interjection'

class VocabularyCategory(models.TextChoices):
    BUSINESS = 'BUSINESS', 'Business'
    DAILY_LIFE = 'DAILY_LIFE', 'Daily Life'
    TRAVEL = 'TRAVEL', 'Travel'
    TECHNOLOGY = 'TECHNOLOGY', 'Technology'
    ACADEMIC = 'ACADEMIC', 'Academic'
    GENERAL = 'GENERAL', 'General'

class PhraseCategory(models.TextChoices):
    MOTIVATION = 'MOTIVATION', 'Motivation'
    REALITY = 'REALITY', 'Reality'
    BUSINESS = 'BUSINESS', 'Business'
    HUMOR = 'HUMOR', 'Humor'
    DAILY_LIFE = 'DAILY_LIFE', 'Daily Life'

class GenzTone(models.TextChoices):
    FUNNY = 'FUNNY', 'Funny'
    CASUAL = 'CASUAL', 'Casual'
    SARCASTIC = 'SARCASTIC', 'Sarcastic'
    POSITIVE = 'POSITIVE', 'Positive'

class PopularityLevel(models.TextChoices):
    TRENDING = 'TRENDING', 'Trending'
    COMMON = 'COMMON', 'Common'
    RARE = 'RARE', 'Rare'
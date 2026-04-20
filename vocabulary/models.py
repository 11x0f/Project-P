from django.db import models
from django.conf import settings

from .choices import DifficultyLevel, PartOfSpeech, VocabularyCategory, PhraseCategory, GenzTone, PopularityLevel

class VocabularyWord(models.Model):
    word = models.TextField(unique=True)
    pronunciation = models.TextField(blank=True, null=True)
    meaning = models.TextField()
    part_of_speech = models.CharField(
        max_length = 50, 
        choices=PartOfSpeech.choices,
        blank=True, 
        null=True,
    )
    example_sentence = models.TextField(blank=True, null=True)
    synonyms = models.JSONField(default=list, blank=True)
    antonyms = models.JSONField(default=list, blank=True)
    difficulty_level = models.TextField(
        choices=DifficultyLevel.choices, 
        default= DifficultyLevel.BEGINNER
    )
    category = models.TextField(
        choices = VocabularyCategory.choices, 
        default = VocabularyCategory.GENERAL
    )
    source_type = models.TextField(default='manual')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta: 
        db_table = 'vocabulary_words'
        ordering = ['word']

    def __str__(self):
        return self.word
    
class Phrase(models.Model):
    phrase = models.TextField( unique=True)
    meaning = models.TextField()
    literal_meaning = models.TextField(blank=True, null=True)
    usage_context = models.TextField(blank=True, null=True)
    example_sentence = models.TextField(blank=True, null=True)
    category = models.TextField(
        choices=PhraseCategory.choices,
        default=PhraseCategory.DAILY_LIFE
    )
    difficulty_level = models.TextField(
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.BEGINNER
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'phrases'
        ordering = ['phrase']

    def __str__(self):
        return self.phrase
    

class GenzLingo(models.Model):
    term = models.TextField(max_length=255, unique=True)
    meaning = models.TextField()
    example_sentence = models.TextField(blank=True, null=True)
    tone = models.TextField(
        choices=GenzTone.choices,
        default=GenzTone.CASUAL
    )
    popularity_level = models.TextField(
        choices=PopularityLevel.choices,
        default=PopularityLevel.COMMON
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'genz_lingo'
        ordering = ['term']

    def __str__(self):
        return self.term


class DailyVocabularyContent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='daily_vocab_contents'
    )
    vocabulary_word = models.ForeignKey(
        VocabularyWord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    phrase = models.ForeignKey(
        Phrase,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    genz_term = models.ForeignKey(
        GenzLingo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    delivered_date = models.DateField()
    completed = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'daily_vocabulary_content'
        unique_together = ('user', 'delivered_date')
        ordering = ['-delivered_date']

    def __str__(self):
        return f'{self.user} - {self.delivered_date}'


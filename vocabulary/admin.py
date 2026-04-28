from django.contrib import admin

from .models import VocabularyWord, Phrase, GenzLingo, DailyVocabularyContent

@admin.register(VocabularyWord)
class VocabularyWordModel(admin.ModelAdmin):
    list_display = [field.name for field in VocabularyWord._meta.fields]

    list_filter = ('difficulty_level', 'category')
    search_filter = ('word')

@admin.register(Phrase)
class PhraseModel(admin.ModelAdmin):
    list_display = [field.name for field in Phrase._meta.fields]

    list_filter = ('category', 'difficulty_level')
    search_filter = ('phrase')

@admin.register(GenzLingo)
class GenzLingoModel(admin.ModelAdmin):
    list_display = [field.name for field in GenzLingo._meta.fields]

    list_filter = ('popularity_level', 'tone')
    search_filter = ('term')

@admin.register(DailyVocabularyContent)
class DailyVocabularyContentModel(admin.ModelAdmin):
    list_display = [ field.name for field in DailyVocabularyContent._meta.fields]
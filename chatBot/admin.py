from django.contrib import admin
from .models import Reply, WordsRegex
# Register your models here.

class WordsAdmin(admin.ModelAdmin):
    list_filter = ('wordsType',)

admin.site.register(Reply)
admin.site.register(WordsRegex, WordsAdmin)
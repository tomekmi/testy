from django.contrib import admin
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline

from apptesty.models import Tests, Questions, Answers

class AnswersInline(NestedStackedInline):
    model = Answers
    extra = 0

class QuestionsInline(NestedStackedInline):
    model = Questions
    extra = 1
    inlines = [AnswersInline,]

class TestsAdmin(NestedModelAdmin):
    inlines = [QuestionsInline,]
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']

admin.site.register(Tests, TestsAdmin)


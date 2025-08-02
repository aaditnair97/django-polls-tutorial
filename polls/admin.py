from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # or use StackedInline
    model = Choice
    extra = 3  # how many blank choices to show


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date info", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # ✅ embed choices
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)


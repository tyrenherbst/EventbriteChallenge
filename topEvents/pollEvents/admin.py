from django.contrib import admin

# Register your models here.
from .models import Question, Category

class ChoiceInLine(admin.TabularInline):
    model = Category
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    list_per_page = 5
    search_fields = ['question_text']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_text','pub_date','was_published_recently','votes','cID')
    list_per_page = 5
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question,QuestionAdmin)

admin.site.register(Category,CategoryAdmin)

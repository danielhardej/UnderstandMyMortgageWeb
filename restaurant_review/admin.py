from django.contrib import admin

from .models import Restaurant, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'rating', 'review_date', 'review_text')
    list_filter = ('restaurant', 'rating', 'review_date')
    search_fields = ('restaurant', 'rating', 'review_date', 'review_text')

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Review, ReviewAdmin)

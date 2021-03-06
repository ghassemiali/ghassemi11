from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'login_require', 'status', 'published_date')
    list_filter = ('status',)
    ordering = ('-created_date',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

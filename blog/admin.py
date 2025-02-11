from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'publications_flag')
    list_filter = ('publications_flag',)
    search_fields = ('title', 'publications_flag')

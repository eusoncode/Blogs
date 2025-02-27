from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Display and filter
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('email',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('title', 'author', 'date')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
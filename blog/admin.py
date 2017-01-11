from django.contrib import admin
from .models import Post
from .models import Category

class CategoryAdmin( admin.ModelAdmin ):
    list_display = [ 'name', ]
    prepopulated_fields = { 'slug': ( 'name', ) }

class PostAdmin( admin.ModelAdmin ):
    list_display = [ 'title', 'author', 'created_date' ]
    list_filter = [ 'created_date', 'categories' ]
    search_fields = [ 'title', 'text' ]
    date_hierarchy = 'created_date'
    filter_horizontal = ( 'categories', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

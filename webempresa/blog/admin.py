from django.contrib import admin

from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')



# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author','-published')
    search_fields = ('title','content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')


    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.post_categories.all().order_by('name') ])
    post_categories.short_description = 'Categorias'







admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
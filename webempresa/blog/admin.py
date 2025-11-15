from django.contrib import admin
from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')


class PostAdmin(admin.ModelAdmin):
    # aquí tenías ('updated', 'updated') -> lo normal es created + updated
    readonly_fields = ('created', 'updated')

    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', '-published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        # Usamos el campo real del modelo: "categories"
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    post_categories.short_description = 'Categorías'


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

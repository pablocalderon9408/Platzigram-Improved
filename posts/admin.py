from django.contrib import admin

from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'created')
    list_display_links = ('pk',)
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
         )

    list_filter = (
        'created',
        'modified',
        )

    fieldsets = (

        ('Metadata', {
            'fields': ('created', 'modified'),
        }),
        )

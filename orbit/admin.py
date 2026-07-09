from django.contrib import admin
from .models import About, About_skill, Category, Portfolio, Workex, Education, Awards, Hapclients, Services, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'created_date', 'is_published')
    list_filter = ('is_published', 'created_date')
    search_fields = ('first_name', 'email')

admin.site.register(About)
admin.site.register(About_skill)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Workex)
admin.site.register(Education)
admin.site.register(Awards)
admin.site.register(Hapclients)
admin.site.register(Services)
# admin.site.register(Contact, ContactAdmin)

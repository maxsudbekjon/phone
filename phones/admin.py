from django.contrib import admin

from .models import Phone, Category, Color, Image, PhoneVariant


class PhoneVariantInline(admin.TabularInline):
    model = PhoneVariant
    extra = 1


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'model',
        'year',
        'category',
        'verified',
        'hot',
    )
    search_fields = ('brand', 'model', 'year')
    list_filter = ('brand', 'category', 'verified', 'hot')
    ordering = ('id',)
    inlines = [PhoneVariantInline]


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Image)

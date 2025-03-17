from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image_preview', 'image_url_preview')
    fields = ('name', 'price', 'description', 'image', 'image_url', 'category', 'created_at')
    readonly_fields = ('created_at',)

    # আপলোড করা ইমেজ প্রিভিউ
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px;">'
        return "No Uploaded Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Uploaded Image'

    # URL ইমেজ প্রিভিউ
    def image_url_preview(self, obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" style="max-height: 50px;">'
        return "No URL Image"
    image_url_preview.allow_tags = True
    image_url_preview.short_description = 'URL Image'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
from rest_framework import serializers

from .models import Phone, PhoneVariant


class PhoneVariantSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = PhoneVariant
        fields = ['id', 'ram', 'storage', 'color', 'price']

    def get_color(self, obj):
        return obj.color.name if obj.color else None


class PhoneSerializer(serializers.ModelSerializer):
    variants = PhoneVariantSerializer(many=True, read_only=True)
    category = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = [
            'id',
            'brand',
            'model',
            'year',
            'category',
            'battery',
            'cycles',
            'issues',
            'verified',
            'hot',
            'image_url',
            'variants',
        ]

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    def get_image_url(self, obj):
        image = obj.image_set.first()
        if not image:
            return ''
        request = self.context.get('request')
        url = image.image.url
        return request.build_absolute_uri(url) if request else url

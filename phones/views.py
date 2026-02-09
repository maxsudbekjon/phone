from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Phone
from .serializers import PhoneSerializer


class PhoneListView(APIView):
    def get(self, request):
        phones = Phone.objects.prefetch_related('variants', 'image_set').order_by('id')
        serializer = PhoneSerializer(phones, many=True, context={'request': request})
        return Response(serializer.data)

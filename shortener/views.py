import string
import random
from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from .serializers import ShortenSerializer


class URLListCreateAPIView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = ShortenSerializer

    def generate_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def perform_create(self, serializer):
        code = self.generate_code()
        while URL.objects.filter(shorturl=code).exists():
            code = self.generate_code()
        serializer.save(shorturl=code)


class URLDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShortenSerializer

    def get_object(self):
        code = self.kwargs['shortCode']
        return get_object_or_404(URL, shorturl=code)


class URLStatsAPIView(generics.RetrieveAPIView):
    serializer_class = ShortenSerializer

    def get_object(self):
        code = self.kwargs['shortCode']
        return get_object_or_404(URL, shorturl=code)


def redirect_url(request, code):
    url = get_object_or_404(URL, shorturl=code)
    url.access_count += 1
    url.save()
    return redirect(url.longurl)
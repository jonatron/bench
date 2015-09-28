from mark.models import Foo
from mark.serializers import FooSerializer
from rest_framework import mixins
from rest_framework import generics


class FooList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

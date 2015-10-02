from mark.serializers import FooSerializer
from rest_framework import mixins
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response

from mark.models import Foo
foo1 = Foo(num=1, txt='hello')
foo2 = Foo(num=2, txt='hi')
foos = [foo1, foo2]

class FooList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = foos
    serializer_class = FooSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


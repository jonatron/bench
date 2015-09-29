from mark.models import Foo
from mark.serializers import FooSerializer
from rest_framework import mixins
from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response


class FooList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Want to test writes using ab...
class FooGetCreate(mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
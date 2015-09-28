from mark.models import Foo
from rest_framework import serializers


class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
        fields = ('id', 'num', 'txt')

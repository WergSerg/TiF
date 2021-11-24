from rest_framework import viewsets, pagination

from .models import Message, Text, Comment, Category, Foundation
from .serializers import TextNestedSerilizer, \
    CategoryReverseSerialize, \
    CreateTextSerializer, \
    CategorySerialize


class TextModeViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextNestedSerilizer


class CategoryTree(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryReverseSerialize


class CreateText(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = CreateTextSerializer


class FoundationTree(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialize

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'James'
from rest_framework import serializers
from bookLib.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name','title','author', 'time')
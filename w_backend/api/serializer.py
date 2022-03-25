from rest_framework import serializers
from .models import woman, path

class pathSerializer(serializers.ModelSerializer):
  class Meta:
    model = path
    fields = '__all__'

class womanSerializer(serializers.ModelSerializer):
  class Meta:
    model = woman
    fields = '__all__'
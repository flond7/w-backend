from rest_framework import serializers
from .models import woman, path

class womanSerializer(serializers.ModelSerializer):
  class Meta:
    model = woman
    fields = '__all__'
    depth = 1
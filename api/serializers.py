from rest_framework import serializers
from .models import calculate


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = calculate
        fields = '__all__'


class DetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = calculate
        fields = ['dob']

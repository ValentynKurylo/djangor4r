from rest_framework.serializers import ModelSerializer
from .models import ComputerModel
from rest_framework import serializers
from django.core.validators import RegexValidator

class ComputerSerializer(ModelSerializer):
    brand = serializers.CharField(validators=[
        RegexValidator('^[a-z A-Z]{1,30}$', 'only letter')
    ])
    memory = serializers.IntegerField(min_value=4)
    class Meta:
        model = ComputerModel
        fields = '__all__'

    def validate_procesor(self, procesor):
        if procesor % 2 != 0:
            raise serializers.ValidationError()
        return procesor
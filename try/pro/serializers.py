from rest_framework import serializers
from.models import emp

class empserializers(serializers.ModelSerializer):
    class Meta:
        model = emp
        fields = '__all__'
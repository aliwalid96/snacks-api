from rest_framework import serializers
from snacks.models import Snack



class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','purchaser','description')
        model = Snack
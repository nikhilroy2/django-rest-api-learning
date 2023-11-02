from app1.models import PersonalInfo
from rest_framework import serializers

class PersonalInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"
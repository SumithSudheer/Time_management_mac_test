from rest_framework import serializers

class User_serializer(serializers.Serializer):
    _id=serializers.CharField()
    username=serializers.CharField()
    password=serializers.CharField()

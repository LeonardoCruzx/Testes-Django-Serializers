from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data["email"],
            password = validated_data['password'],
        )
        user.save()
        return user

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        try:
            representation['profile_picture'] = instance.profile_picture.url
        except:
            representation['profile_picture'] = None
        return representation
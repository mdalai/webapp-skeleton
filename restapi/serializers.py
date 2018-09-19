from rest_framework import serializers
from home.models import Applications
from users.models import CustomUser


class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = ("id", "name", "description", "color", "defaultstatus", "link")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'id', 'username', 'password', 'email', 'groups')
from rest_framework import serializers
from .models import User, List

class UserSerializer(serializers.HyperlinkedModelSerializer):
    lists = serializers.HyperlinkedRelatedField(
        view_name='list_detail',
        many=True,
        read_only=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    def create(self, validated_data):
        lists_data = validated_data.pop('lists')
        user = User.objects.create(**validated_data)
        for list_data in lists_data:
            List.objects.create(user=user, **list_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'user_url', 'user_id', 'first_name', 'last_name', 'email_address', 'photo_url', 'create_ts', 'update_ts', 'lists',)

class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    list_url = serializers.ModelSerializer.serializer_url_field(
        view_name='list_detail'
    )

    class Meta:
        model = List
        fields = ('id', 'list_url', 'title', 'list_type', 'status', 'image_url', 'create_ts', 'update_ts', 'user', )




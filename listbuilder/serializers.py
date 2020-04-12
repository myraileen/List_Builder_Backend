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
        fields = ('id', 'list_url', 'title', 'list_type', 'status', 'image_url', 'user', 'create_ts', 'update_ts')



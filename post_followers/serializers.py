from django.db import IntegrityError
from rest_framework import serializers
from .models import PostFollower, Post, User

class PostFollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the PostFollower model.
    'owner' represents the user who is following the post.
    'followed_post' represents the ID of the followed post.
    """
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source="owner.username",
        default=serializers.CurrentUserDefault())
    followed_post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    followed_post_title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PostFollower
        fields = ['id', 'owner', 'created_at', 'followed_post', 'followed_post_title']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'Post already followed by user. possible duplicate'})

    def get_followed_post_title(self, obj):
        """
        Retrieve the title of the followed post.
        """
        return obj.followed_post.title

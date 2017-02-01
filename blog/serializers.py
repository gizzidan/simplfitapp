from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        title = validated_data.get('title', None)
        user = self.context.get("user")
        text = validated_data.get('text', None)
        categories = validated_data.get('categories', None)
        created_date = validated_data.get('created_date', None)
        published_date = validated_data.get('published_date', None)
        modified_at = validated_data.get('modified_at', None)
        slug = validated_data.get('slug', None)
        return Post.objects.create(title=title, author=user, text=text, categories=categories,
                                    created_date=created_date, published_date=published_date,
                                    modified_at=modified_at, slug=slug)

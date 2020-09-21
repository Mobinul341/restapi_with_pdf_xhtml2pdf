from rest_framework import serializers
from .models import PostModel
'''
#3. HyperlinkedModelSerializer
class PostModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id','url', 'title', 'blog']
'''



#2.ModelSerializer
class PostModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', 'title', 'blog']
        #fields = '__all__'

'''
#1. Only Serializer
class PostModelSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    blog = serializers.CharField(max_length=400)
    

    def create(self, validated_data):
        return PostModel.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.blog = validated_data.get('blog', instance.blog)

        instance.save()
        return instance

'''
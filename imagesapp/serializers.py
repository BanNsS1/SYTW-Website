from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Image, Rate, Comment

class ImageSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imagesapp:image_detail')
    rates = HyperlinkedRelatedField(many=True, read_only=True,view_name='imagesapp:rate_detail')
    comments = HyperlinkedRelatedField(many=True, read_only=True,view_name='imagesapp:comment_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Image
        fields = ('uri','title','url','user','date','description', 'rates', 'comments')

class RateSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imagesapp:rate_detail')
    image = HyperlinkedRelatedField(read_only=True, view_name='imagesapp:image_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Rate
        fields = ('uri','rating','user','image','date')

class CommentSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imagesapp:comment_detail')
    image = HyperlinkedIdentityField(read_only=True, view_name='imagesapp:image_detail')
    user = CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ('uri','image','text','date')

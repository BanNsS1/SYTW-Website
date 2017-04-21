from django.forms import ModelForm
from models import Image, Rate, Comment

class ImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ('date', 'user')

class RateForm(ModelForm):
    class Meta:
        model = Rate
        exclude = ('user', 'image', 'date')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'image', 'date')

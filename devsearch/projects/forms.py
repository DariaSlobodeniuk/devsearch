from cProfile import label

from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'description', 'source_link', 'demo_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwards):
        super(ProjectForm, self).__init__(*args, **kwards)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

       #  self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add title'})
       #  self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add description'})
       #


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment here'
        }

    def __init__(self, *args, **kwards):
        super(ReviewForm, self).__init__(*args, **kwards)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
from django import forms
from .models import Article, Category

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= '__all__'
        exclude= ('author', 'created_at', 'updated_at', 'slug',)


class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= '__all__'
        exclude= ('author', 'category', 'created_at', 'updated_at', 'slug',)

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= ('name',)

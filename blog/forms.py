
from secrets import choice
from unicodedata import category
from django import forms
from .models import Category


class PostForm(forms.Form):
    category_data=Category.objects.all()
    category_choice={}
    for category in category_data:
        category_choice[category]=category
    title=forms.CharField(max_length=30,label='タイトル',widget=forms.Textarea(attrs={'cols': '180', 'rows': '1'}))
    image=forms.ImageField(label='イメージ画像',required=False)
    content=forms.CharField(label='内容',widget=forms.Textarea(attrs={'cols': '180', 'rows': '10'}))
    category=forms.ChoiceField(label='カテゴリ',widget=forms.Select,choices=list(category_choice.items()))
from django import forms

from .models import Review, Comment
from movies.models import Movies

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'      : 'comment-control',
        'placeholder': '글 제목 항목 입니다!',  
        })
    )
    rank = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'      : 'review-rank',
        'placeholder': '평가 점수',  
        })
    )
    movie_title = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'      : 'comment-control',
        'placeholder': '리뷰를 남기실 영화 제목을 써주세요',  
        })
    )
    content = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'      : 'review-content',
        'placeholder': '글 본문을 쓰시면 됩니다!',  
        })
    )
    class Meta:
        model  = Review
        fields = ['title', 'movie_title', 'rank', 'content',]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
    label  = '',
    widget = forms.TextInput(attrs={
        'class'      : 'comment-control',
        'placeholder': '게시글에 대해 의견을 입력해주세요!',  
        })
    )
    class Meta:
        model  = Comment
        fields = ['content',]

'''
why Form?
1. Data validation
2. HTML easy
'''

from django import forms
from .models import Article
# forms.Form => 특정 모델과 연동 x 단순히 데이터 검증/HTML 생성용
class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=5)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField(widget=forms.Textarea) # 위젯은 html 생성시 주는 옵션

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        

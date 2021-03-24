from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ContactForm, ArticleForm
"""
1. 사용자가 /crud/contact/로 접속 => GET /crud/contact/
2. 사용자가 HTML > form 에서 데이터 제출 누르면 => POST /crud/contact/
3. view 함수에서 contact 로 redirect 시킴 => GET /crud/contact/
"""
def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form,
        }
        return render(request, 'articles/contact.html', context)
    elif request.method == 'POST':        
        contact_form = ContactForm(request.POST)
        # if contact_form.is_valid():

        # print(contact_form)
        print(contact_form.is_valid())
        return redirect('articles:contact')
    
@login_required # not logged_in 일 경우 무조건 '/accounts/login/'으로 redirect 한다.
@require_http_methods(['GET', 'POST'])
def new(request):
    # 사용자 요청이 GET일 경우
    if request.method == 'GET':
        # 비어있는 새로운 form 생성
        form = ArticleForm()
        context = {'form': form}
        # html에 form 실어서 전송
        return render(request, 'articles/new.html', context)

    # 사용자 요청이 POST 일 경우
    elif request.method == 'POST':
        # form 에 요청 DATA 입력
        form = ArticleForm(request.POST)
        # form 통해 DATA 유효성 검사(validation)
        if form.is_valid():
            # 유효하다면 저장
            article = form.save()      
            # 저장한 article 의 상세보기 페이지로 redirect
            return redirect('articles:detail', article_pk = article.pk)
        else: # 유효하지 않다면 기존의 잘못된 data 를 담은 form (38 번째 줄)을 담고
            context = {'form': form}
            # html 에 담아서 전송
            return render(request, 'articles/new.html', context)



def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        # new와 다르게 특정 아티클에 대한 내용을 request.POST로 덮어쓰기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        # 기존 게시를 내용을 포함한 html 을 만들기 위해 instance 추가
        form = ArticleForm(instance=article)
    context = {'form':form}
    return render(request, 'articles/edit.html', context)








    # if request.method == 'GET':
    #     # 기존 게시글 내용을 포함한 html 만들기 위해 instance 추가
    #     form = ArticleForm(instance=article)
    #     context = {'form': form}
    #     return render(request, 'articles/edit.html', context)

    # elif request.method == 'POST':
    #     # new 와 다르게 특정 article 에 대한 내용을 request.POST로 덮어쓰기
    #     form = ArticleForm(request.POST, instance=article) # 기존의 정보를 edit 하겠다는 거니까 instance 넣어줘야함
    #     if form.is_valid():
    #         article = form.save()      
    #         return redirect('detail', article_pk = article.pk)
   

# def update(request, article_pk):
#     return redirect()

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
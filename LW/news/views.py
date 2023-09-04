from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news(request):
    news = Articles.objects.all()
    return render(request, 'news/index.html', {'news': news})


def create_post(request):
    err = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('News')
        else:
            err = "Ошибка заполнения формы"
    form = ArticlesForm()
    post = {
        'form': form,
        'err': err
    }
    return render(request, 'news/create_post.html', post)

def post(request,number):
    return render(request,f'news/publication_{number}.html')

from django.shortcuts import render
from foodApp.models import Article, Comment
from django.http import Http404

def detail(request,article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Restaurant does not exist")
    
    if request.method == 'post':
        comment = Comment(article=article, text=request.POST['text'])
        comment.save()

    context = {
        'article':article,
        'comment':article.comment.order_by('-posted_at')
    }
    return render(request,'foodApp/helspo_comment.html',context)

def index(request):
    return render(request,'foodApp/index.html')

def kyosuke(request):
    return render(request,'foodApp/kyosuke.html')


def kyosuke_Photo(request):
    return render(request, 'foodApp/kyosuke_Photo.html')

def kyosuke_Comment(request):
    return render(request, 'foodApp/kyosuke_Comment.html')

def helspo(request):
    return render(request,'foodApp/helspo.html')

def template(request):
    return render(request,'foodApp/template.html')

def wellb(request):
    return render(request,'foodApp/wellb.html')

def tonnya(request):
    return render(request,'foodApp/tonnya.html')

def manngetu(request):
    return render(request,'foodApp/manngetu.html')
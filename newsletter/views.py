from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# DjangoGirls post_list view
def IndexView(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'newsletter/index.html', {'articles': articles})

# DjangoGirls post_detail view
def DetailView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'newsletter/detail.html', {'article': article})

# DjangoGirls post_new view
@permission_required('newsletter.add_article', raise_exception=True)
def CreateView(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'newsletter/create.html', {'form': form})

# DjangoGirls post_edit view
@permission_required('newsletter.change_article', raise_exception=True)
def EditView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'newsletter/edit.html', {'form': form})

# DjangoGirls post_draft_list view
@permission_required('newsletter.change_article', raise_exception=True)
def DraftsList(request):
    articles = Article.objects.filter(pub_date__isnull=True,).order_by('init_date')
    return render(request, 'newsletter/drafts.html', {'articles': articles})

# DjangoGirls post_publish view
@permission_required('newsletter.delete_article', raise_exception=True)
def PubView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('detail', pk=pk)

# DjangoGirls post_remove view
@permission_required('newsletter.delete_article', raise_exception=True)
def DelView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# DjangoGirls add_comment_to_post view
@permission_required('newsletter.add_comment', raise_exception=True)
def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'newsletter/comment.html', {'form': form})

# DjangoGirls comment_approve view
@permission_required('newsletter.delete_comment', raise_exception=True)
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', pk=comment.article.pk)

# DjangoGirls comment_remove view
@permission_required('newsletter.delete_comment', raise_exception=True)
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.article.pk)
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def welcome(request):
    new = project.objects.all()
    
    return render(request, 'welcome.html',locals())

# def search_results(request):
#
#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_title(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'all-templates/search.html',{"message":message,"articles": searched_articles})
#
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-templates/search.html',{"message":message})

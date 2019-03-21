from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# from .forms import NewProjectForm, NewsLetterForm

@login_required(login_url='/accounts/login/')

# Create your views here.
def welcome(request):
    new = project.objects.all()
    return render(request, 'welcome.html',locals())

def signup(request):
    return redirect('/accounts/login/')
    return render(request, 'registration_form.html')

# search form
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-templates/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-templates/search.html',{"message":message})

# the profile
def profile(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

        profile = Profile.objects.all()
        all_profile = Profile.objects.all()
    return render(request,'profile.html', locals())

#
# def update_index(request):
#     # all_profile = Profile.objects.all()
#     profile = Profile.objects.get(user_id = request.user)
#     if request.method == 'POST':
#         form = UploadForm(request.POST,request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form  = ProfileForm()
#
#     return render(request,'update.html', locals())

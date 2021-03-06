from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('home',views.welcome,name = 'welcome'),
    # url(r'^search/', views.search_results, name='search_results')
    url(r'^$',views.signup, name='sign'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^search/$',views.search_results, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

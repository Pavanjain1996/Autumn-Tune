from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from AutumnTune.models import File
from django.db.models import Q
from .views import searchtext

urlpatterns = [
    url(r'^Home/$',views.index,name='home'),
    url(r'^songs/$',ListView.as_view(queryset = File.objects.all().order_by("-date"),template_name='TuneIn/Songs.html')),
    url(r'^Arijit/$',ListView.as_view(queryset = File.objects.all().filter(singer__contains='Arijit Singh').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Atif/$',ListView.as_view(queryset = File.objects.all().filter(singer__contains='Atif Aslam').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Ankit/$',ListView.as_view(queryset = File.objects.all().filter(singer__contains='Ankit Tiwari').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Shreya/$',ListView.as_view(queryset = File.objects.all().filter(singer__contains='Shreya Ghoshal').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Hindi/$',ListView.as_view(queryset = File.objects.all().filter(language='Hindi').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^English/$',ListView.as_view(queryset = File.objects.all().filter(language='English').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Punjabi/$',ListView.as_view(queryset = File.objects.all().filter(language='Punjabi').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Romantic/$',ListView.as_view(queryset = File.objects.all().filter(category='Romantic').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Sad/$',ListView.as_view(queryset = File.objects.all().filter(category='Sad').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Mood/$',ListView.as_view(queryset = File.objects.all().filter(category='Mood').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Party/$',ListView.as_view(queryset = File.objects.all().filter(category='Party').order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^MostPopular/$',ListView.as_view(queryset = File.objects.all().filter(Q(language='Punjabi') | Q(singer='Arijit Singh') | Q(category='Mood')).order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^Top/$',ListView.as_view(queryset = File.objects.all().filter(Q(language='Punjabi') | Q(singer='Arijit Singh') | Q(category='Party')).order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^NewlyReleased/$',ListView.as_view(queryset = File.objects.all().order_by("-date")[:50],template_name='TuneIn/Songs.html')),
    url(r'^songs/(?P<pk>\d+)$',DetailView.as_view(model=File,template_name='TuneIn/Play.html')),
    url(r'^Register/$',views.register,name='Register'),
    url(r'^RegisterSubmit/$',views.registration,name='registration'),
    url(r'^$',views.login,name='login'),
    url(r'^LoginSubmit/$',views.verifylogin,name='verifylogin'),
    url(r'^Profile/$',views.profile,name='profile'),
    url(r'^Logout/$',views.logout,name='logout'),
    url(r'^Search/$',views.search,name='search'),
    url(r'^Answer/$',ListView.as_view(queryset = File.objects.all().filter(singer__contains=searchtext).order_by("-date")[:50],template_name='TuneIn/Songs.html')),
]

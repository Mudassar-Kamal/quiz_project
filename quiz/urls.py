
from django.contrib import admin
from django.urls import path , include
from .views import AboutUsView, ContactView, DownloadView, HomeView, IndexView, ProfileView,QuizView,CategoryDetailView,PerformanceView, ResultsView

urlpatterns = [

    path('' , HomeView.as_view() , name='index_view'),
    path('about/' , AboutUsView.as_view() , name='about'),
    path('download/' , DownloadView.as_view() , name='download'),
    path('result/' , ResultsView.as_view() , name='result'),
    path('contact/' , ContactView.as_view() , name='contact'),
    path('profile/' , ProfileView.as_view() , name='profile'),
    
    path('quiz/' , IndexView.as_view() , name='quiz'),
    path('category/detail/<uuid:id>/' , CategoryDetailView.as_view() , name='category_detail'),
    path('quiz/<uuid:id>/' , QuizView.as_view() , name='quiz_view'),
    path('performance/<uuid:id>/' , PerformanceView.as_view() , name='performace'),


]


from django.contrib import admin
from django.urls import path , include
from .views import IndexView,QuizView,CategoryDetailView,PerformanceView



urlpatterns = [

 
    path('' , IndexView.as_view() , name='index_view'),
    path('category/detail/<uuid:id>/' , CategoryDetailView.as_view() , name='category_detail'),
    path('quiz/<uuid:id>/' , QuizView.as_view() , name='quiz_view'),
    path('performance/<uuid:id>/' , PerformanceView.as_view() , name='performace'),


]

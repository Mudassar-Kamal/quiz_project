from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from quiz.utils import create_questions, send_contact_email
from .models import AskedQuestion, Category,Question,Option,ScoreCard, Student
import json
from django.http import JsonResponse
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

class HomeView(View):
    def get(self , request , *args , **kwargs):
    
        return render( request,'home.html')
class AboutUsView(View):
    def get(self , request , *args , **kwargs):
    
        return render( request,'about.html')
class DownloadView(View):
    def get(self , request , *args , **kwargs):
    
        return render( request,'download.html')
class ResultsView(View):
    def get(self , request , *args , **kwargs):
        
        return render( request,'result.html')

from django.conf import settings
from django.core.mail import send_mail
class ContactView(View):
    def get(self , request , *args , **kwargs):
        
        return render( request,'contact_us.html')

    def post(self , request , *args , **kwargs):
        send_mail = send_contact_email(request.POST.get('subject'),request.POST.get('message'),request.POST.get('email'))
        if send_mail:
            return redirect("index")
        return redirect('contact')

    
class ProfileView(LoginRequiredMixin, View):
    def get(self , request , *args , **kwargs):
        
        return render( request,'profile.html')
class IndexView(LoginRequiredMixin,View):
    def get(self , request , *args , **kwargs):
        categories = Category.objects.all() 
        context={
               "categories":categories
        }
        return render( request,'quiz_new.html',context=context)
class CategoryDetailView(LoginRequiredMixin,View):
    def get(self , request , *args , **kwargs):
        # Initialising the sessions
        request.session['passed_qs']=[]
        print("qss:::",request.session['passed_qs'])
        request.session['total']=0
        request.session['score']=0
        id        = self.kwargs.get("id")
        category  = Category.objects.get(id=id) 
# Querying if questions are added to enable or disable the button respectively
        questions = Question.objects.filter(category=id)
        context={
               "category":category,
               "questions":questions
        }
        return render( request,'test_templates/category_detail.html',context=context)
from dateutil.relativedelta import relativedelta
class QuizView(LoginRequiredMixin,View):
    def get(self , request , *args , **kwargs):
        id    = self.kwargs.get("id")
        # Excluding the questions stored in sessions (questions asked before)
        current_time = datetime.now()

        print("current time:",current_time)
        end_time =current_time + relativedelta(seconds=1800)
        print("end time:",end_time.time())



        items = list(Question.objects.filter( category = id).exclude(pk__in = request.session['passed_qs']))
        if items:
            random_item = random.choice(items)
            context={
                "questions":random_item,
                "end_time":end_time,
            }
            return render( request,'test_templates/quiz.html',context=context)
        else:
            cat = get_object_or_404(Category,id=id)
            correct_questions = 0
            questions = Question.objects.filter(category__id=id)
            for each_question in questions:
                correct_ans = Option.objects.filter(question=each_question)
                correct_questions += correct_ans.count()
            ScoreCard.objects.create(category=cat,User=request.user,score=request.session['score'])
            # resetting the sessions
            request.session['passed_qs']=[]
            request.session['total']=0
            request.session['score']=0
            return redirect("performace",id=id)
    #   Post request for Ajax-call
    def post(self , request , *args , **kwargs): 
        data    = json.loads(request.body)
        answer  = data.get("option")
        qid     = data.get("q_id")
        question   = get_object_or_404(Question,pk=qid)
        create_questions(request.user,question)
        correct = question.correct_answer.option_txt == answer
        if correct:  
            request.session['score']= request.session['score']+1
            request.session['total']= request.session['total']+1
            request.session['passed_qs'].append(qid)
            data={
                'class':'alert-success',
                'msg':'Correct Answer, Keep it up '
            }
            return JsonResponse(safe= False , data = data)    
        # Storing the asked question in list to exclude them 
        request.session['passed_qs'].append(qid)
        request.session['total']= request.session['total']+1
        data={
            'class':'alert-danger',
            'msg':f'Wrong Answer, the correct answer is "{question.correct_answer.option_txt}"'
            }
        return JsonResponse(safe= False , data =data)  
class PerformanceView(LoginRequiredMixin,View):

    def get(self,request,*args,**kwargs):
        id=self.kwargs.get("id")
        total_questions = Question.objects.filter( category__id= id)
        score = ScoreCard.objects.filter(category=id,User=request.user) 
        user_obj = Student.objects.get(user=request.user)
        print("user:::",user_obj.user.active_user)
        user_obj.user.active_user = False
        user_obj.user.save()
        
        context={
            "score_card":score,
            "total_questions":total_questions,
            "id":id
        }
        return render( request,'test_templates/performance.html',context=context)
from .models import AskedQuestion,Student
from django.conf import settings
from django.core.mail import send_mail

def create_questions(user,question_obj):
    user_obj = Student.objects.get(user=user)
    stude_obj = AskedQuestion.objects.create(student=user_obj,question = question_obj)
    ans_counter = 0
    for option in question_obj.option_set.all():
        ans_counter +=1
        if ans_counter == 1:
            stude_obj.option_txt_1 = option.option_txt
        if ans_counter == 2:
            stude_obj.option_txt_2 = option.option_txt
        if ans_counter == 3:
            stude_obj.option_txt_3 = option.option_txt
        if ans_counter == 4:
            stude_obj.option_txt_4 = option.option_txt
    stude_obj.save()


def send_contact_email(contact_subject, contact_message,contact_email):
    subject = contact_subject
    message =contact_message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [contact_email, ]
    send_mail( subject, message, email_from, recipient_list )
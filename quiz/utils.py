from .models import AskedQuestion,Student


def create_questions(user,question_obj):
    user_obj = Student.objects.get(user=user)
    stude_obj = AskedQuestion.objects.create(student=user_obj,question = question_obj)
    print("student:::",stude_obj)
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
import pandas as pd
from quiz.models import Student
from accounts.models import User

users = pd.read_csv('users.csv')
all_users = users.to_dict(orient='records')

for query_obj in all_users:
	username = query_obj.get('username')
	roll_number = query_obj.get('roll_number')
	school_name = query_obj.get('school_name')
	campus_name = query_obj.get('campus_name')
	user = User.objects.create(username=username, roll_number=roll_number, school_name=school_name, campus_name=campus_name)
	password = User.objects.make_random_password()
	user.readable_password = password
	user.set_password(password)
	user.save()
	student = Student.objects.create(user=user)

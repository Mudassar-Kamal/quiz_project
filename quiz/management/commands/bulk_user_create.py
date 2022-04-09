import pandas as pd
from quiz.models import Student
from accounts.models import User
from django.core.management import BaseCommand
class Command(BaseCommand):

	help = "Loads users data from .csv"
	def handle(self, *args, **options):
		users = pd.read_csv('users.csv')
		all_users = users.to_dict(orient='records')
		# print("ALLL USERS:::::",all_users)

		for query_obj in all_users:
			# print("iterators::::",query_obj)
			roll_no = query_obj.get('ROLL NO')
			student_name = query_obj.get('STUDENT NAME')
			grade = query_obj.get('CLASS / GRADE')
			group_name = query_obj.get('GROUP NAME')
			category = query_obj.get('CATEGORY')
			school_name = query_obj.get('SCHOOL NAME')
			campus_name = query_obj.get('CAMPUS NAME')
			address = query_obj.get('ADDRESS')
			school_code = query_obj.get('School Code')
			full_address = query_obj.get('SCHOOL NAME-CAMPUS NAME-ADDRESS')
			code = query_obj.get('School Code')

			user = User.objects.create(
				roll_number = roll_no,
				username = student_name,
				grade = grade,
				group_name = group_name,
				category = category,
				school_name = school_name,
				campus_name = campus_name,
				address = address,
				school_code = school_code,
				full_address = full_address,
				code = code,
				user_type = "Student"
				   )
			password = User.objects.make_random_password()
			user.readable_password = password
			user.set_password(password)
			user.save()
			student = Student.objects.create(user=user)

from csv import DictReader
from django.core.management import BaseCommand
from quiz.models import QuizQuestion,Choice
# from pytz import UTC

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the quiz data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from quiz.csv"

    def handle(self, *args, **options):
        # Show this when the data already exist in the database
        if QuizQuestion.objects.exists():
            print('quiz data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return False
        # Show this before loading the data into the database
        print("Loading Question data")

        # Code to load the data into database
        for row in DictReader(open('./test.csv')):
            ans=row['CORRECT_ANSWER']
            question_obj = QuizQuestion.objects.create(question=row['FULL_QUESTION'])
            count = 0
            for option in [Choice.objects.create(question=question_obj,choice=row['OPTION1']),
            Choice.objects.create(question=question_obj,choice=row['OPTION2']),
            Choice.objects.create(question=question_obj, choice=row['OPTION3']),
            Choice.objects.create(question=question_obj, choice=row['OPTION4'])]:


                if option.choice == ans:
                    count += 1
                    question_obj.correct_ans = ans
                    question_obj.save()
            print(count, '6th question')



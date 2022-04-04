from csv import DictReader
from django.core.management import BaseCommand
from quiz.models import Question,Option,Category
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
        if Question.objects.exists():
            print('quiz data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return False
        # Show this before loading the data into the database
        print("Loading Question data")

        # Code to load the data into database
        for row in DictReader(open('./test.csv')):
            ans=row['CORRECT_ANSWER']
            created_cat ,  created = Category.objects.get_or_create(
                 name = row['CATEGORY']
                )
            q_obj=Question.objects.create(full_question=row['FULL_QUESTION'],category=created_cat)

            for option in [Option.objects.create(option_txt=row['OPTION1'],question=q_obj), 
            Option.objects.create(option_txt=row['OPTION2'],question=q_obj), 
            Option.objects.create(option_txt=row['OPTION3'],question=q_obj), 
            Option.objects.create(option_txt=row['OPTION4'],question=q_obj)]:
                if option.option_txt == ans:
                    q_obj.correct_answer = option
                    q_obj.save()



from django.utils import timezone

from expenses.models import Expenses

HOUSE_NAME = 'House 1'
HOUSE_PUBLIC = True
HOUSE_PARENT_PROFESSION_1 = 'Teacher'
HOUSE_PARENT_PROFESSION_2 = 'Student'
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1
HOUSE_DESCRIPTION = 'description'

EXPENSE_AMOUNT = 100
EXPENSE_DATE = timezone.now()
EXPENSE_CATEGORY = Expenses.Category.CLOTHING

BAD_FORM_DATA = {'house_id': '1234'}

USERNAME = 'testuser'
FIRSTNAME = 'Test'
LASTNAME = 'User'
PASSWORD = 'TestPassword123!@#'
PASSWORD_NOT_MATCH = 'NOT_MATCH'
EMAIL = 'testuser@gmail.com'

AMOUNT = '100'
DATE = timezone.now()
CATEGORY = 'Clothing'

HOUSE_NAME_1 = 'House one'
HOUSE_NAME_2 = 'House two'
COUNTRY = 'Colorado'
CITY = 'South Park'

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
EXPENSE_DESCRIPTION = 'description'

EXPENSE_DESCRIPTION_BEFORE = 'before'
EXPENSE_DESCRIPTION_AFTER = 'after'

BAD_FORM_DATA = {'house_id': '1234'}
EXPENSE_BAD_AMOUNT = -100
EXPENSE_BAD_DESCRIPTION = ''

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

EXPENSE_FORM_DATA = {
    'date': EXPENSE_DATE,
    'amount': EXPENSE_AMOUNT,
    'category': EXPENSE_CATEGORY,
    'description': EXPENSE_DESCRIPTION,
}
EXPENSE_BAD_FORM_DATA_DESCRIPTION = {
    'date': EXPENSE_DATE,
    'amount': EXPENSE_AMOUNT,
    'category': EXPENSE_CATEGORY,
    'description': EXPENSE_BAD_DESCRIPTION,
}
EXPENSE_BAD_FORM_DATA_AMOUNT = {
    'date': EXPENSE_DATE,
    'amount': EXPENSE_BAD_AMOUNT,
    'category': EXPENSE_CATEGORY,
    'description': EXPENSE_DESCRIPTION,
}

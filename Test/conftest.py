import pytest
from datetime import date
import bcrypt
from Air_quality.user import User

@pytest.fixture(scope='function')
def common_user():
    user_detail = User(first_name='Jiaying', last_name='Pan', email='jypan@email.com',
                       username='jiayingpan', password='123456', dob= date(year=2001, month=6, day=25))
    yield user_detail


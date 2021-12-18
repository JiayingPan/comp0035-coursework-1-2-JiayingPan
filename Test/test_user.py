def test_correct_user_full_name(common_user):
   user_full_name = common_user.create_full_name
   assert user_full_name == 'Jiaying Pan'   #successful

def test_incorrect_user_full_name(common_user):
   user_full_name = common_user.create_full_name
   assert user_full_name == 'Harry Potter'   #failed


def test_correct_user_age(common_user):
   user_age = common_user.calculate_age
   assert user_age == 20     #successful

def test_incorrect_user_age(common_user):
   user_age = common_user.calculate_age
   assert user_age == 60     #failed

#def test_unknown_user_age(common_user):      #delete dob in conftest common user fixture
#   user_age = common_user.calculate_age
#   assert user_age == "Age not calculated, date of birth unknown"    #successful


#def test_correct_current_hashed_password(common_user):
#   current_hashed_password = common_user.hash_password
#   assert current_hashed_password == None      #successful

#def test_incorrect_current_hashed_password(common_user):
#   current_hashed_password = common_user.hash_password
#   assert current_hashed_password == '123456'  #failed


def test_the_string_password_matches_the_hashed_password_is_true(common_user):
   user_hashed_password = common_user.hash_password(common_user.hashed_password)
   assert common_user.is_correct_password(user_hashed_password) is True    #successful

def test_the_string_password_matches_the_hashed_password_is_false(common_user):
   user_hashed_password = common_user.hash_password(common_user.hashed_password)
   assert common_user.is_correct_password(user_hashed_password) is False    #failed


def test_login_status_is_false_when_user_created(common_user):
   login_status = common_user.is_logged_in
   assert login_status is False       #successful

def test_login_status_is_true_when_user_created(common_user):
   login_status = common_user.is_logged_in
   assert login_status is True        #failed


def test_login_status_is_false_when_user_logs_out(common_user):
   """
   GIVEN a user is logged in
   WHEN the logout function is called
   THEN the logged in status should be False
   """
   common_user.login(common_user.username, common_user.hashed_password)
   assert common_user.is_logged_in is True
   common_user.logout()
   assert common_user.is_logged_in is False       #successful

def test_login_status_is_true_when_user_logs_out(common_user):
   common_user.login(common_user.username, common_user.hashed_password)
   assert common_user.is_logged_in is True
   common_user.logout()
   assert common_user.is_logged_in is True        #failed

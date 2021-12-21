def test_correct_user_full_name(common_user): #successful
   """
   GIVEN the first name and last name of a user
   WHEN the create full name function is called
   THEN the full name should be returned
   """
   user_full_name = common_user.create_full_name
   assert user_full_name == 'Jiaying Pan'

def test_incorrect_user_age(common_user): #failed
   """
   GIVEN the date of birth of a user
   WHEN the calculate age function is called
   THEN the user age should be returned
   """
   user_age = common_user.calculate_age
   assert user_age == 60

#delete dob in conftest common user fixture
# def test_unknown_user_age(common_user): #successful
#   """
#   GIVEN the date of birth of a user is unknown
#   WHEN the calculate age function is called
#   THEN the the sentence "Age not calculated, date of birth unknown" should be returned
#   """
# user_age = common_user.calculate_age
# assert user_age == "Age not calculated, date of birth unknown"

def test_the_password_is_hashed(common_user): #successful
   """
   GIVEN the password of a user
   WHEN the hash password function is called
   THEN none should be returned
   """
   assert common_user.hashed_password == None

def test_the_password_string_matches_hashed_password(common_user): #successful
   """
   GIVEN the password of a user
   WHEN the password string is compared to the hashed password
   THEN the correctness of the password should be True
   """
   common_user.hash_password(common_user.password)
   assert common_user.is_correct_password(common_user.password) is True

def test_login_status_is_true_when_user_created(common_user):  #failed
   """
   GIVEN a new user(created as a fixture)
   WHEN it the user has just been created
   THEN the logged in status should be False
   """
   login_status = common_user.is_logged_in
   assert login_status is True

def test_login_status_is_false_when_user_logs_out(common_user): #successful
   """
   GIVEN a user is logged in
   WHEN the logout function is called
   THEN the logged in status should be False
   """
   common_user.login(common_user.username, common_user.hashed_password)
   assert common_user.is_logged_in is True
   common_user.logout()
   assert common_user.is_logged_in is False

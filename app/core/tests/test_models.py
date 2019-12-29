from django.test import TestCase
# django convention
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # test creating a new user with an email is successful
        testemail = "test@mail.com"
        testpassword = "test123"  # just for testing, doesnt have to be secure
        user = get_user_model().objects.create_user(
            email=testemail,
            password=testpassword
        )

        self.assertEqual(user.email, testemail)
        self.assertTrue(user.check_password(testpassword))
        """ we cant check password by direct equality = checkpassword is a helper function that coes with django"""

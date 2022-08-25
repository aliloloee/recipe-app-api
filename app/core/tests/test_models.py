from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase) :

    def test_create_user_with_email_successful(self) :
        """Test if creating a new user with email is successful"""

        email = 'test@testrecipe.com'
        password = 'test159487'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
    
    def test_new_user_email_normalized(self) :

        email = 'test2@tEsTRecIpE.cOm'
        password = 'test159487'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_have_email(self) :

        with self.assertRaises(ValueError) :
            get_user_model().objects.create_user(None, 'test159487')

    def test_new_superuser(self) :

        email = 'testadmin@testrecipe.com'
        password = 'test159487'

        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
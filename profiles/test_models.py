# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase
from django.contrib.auth.models import User

# Internal
from .models import UserProfile

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProfileModels(TestCase):
    """
    Tests the profile model
    """
    def setUp(self):
        """
        Sets up test user
        """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        test_user.save()

    def tearDown(self):
        """
        Delete test user
        """
        User.objects.all().delete()

    def test_profile_str_method(self):
        """
        Tests user's profile
        """
        test_user = User.objects.get(username='test_user')
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(str(profile), profile.user.username)

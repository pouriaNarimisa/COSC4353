import unittest
from django.http import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  PasswordChangeForm, SetPasswordForm, UserChangeForm, PasswordResetForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from fuel_app.forms import *   # import all forms
from django.db import models
import datetime
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import check_password


# Create your tests here.

class indexTests(TestCase):

    """ test homepage returns 200 status """
    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class LoginTests(TestCase):
    
    """ test login page returns 200 status for GET """
    def test_status(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)


    def test_home_view(self):
        user = User.objects.create(username="texasjordan", password="Texas44!")
        user.set_password('Texas44!!!')
        user.save()
        self.assertTrue(user)    

    def test_login_required(self, view_url='/login_required/', login_url='/login'):
        """
        login_required works on a simple view wrapped in a login_required
        decorator.
        """
        response = self.client.get(view_url)
        self.assertEqual(response.status_code, 404)


# https://django.readthedocs.io/en/stable/topics/auth/default.html


class UserCreationFormTest(TestCase):

    def test_user_already_exists(self):
        data = {
            'username': 'testclient',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_invalid_data(self):
        data = {
            'username': 'jsmith!',
            'password1': 'test123',
            'password2': 'test123',
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        validator = next(v for v in User._meta.get_field('username').validators if v.code == 'invalid')
        self.assertEqual(form["username"].errors, [str(validator.message)])

    def test_form_validation_for_blank_items(self):
        form = UserCreationForm(data={'text': ''})
        self.assertFalse(form.is_valid())

    def test_both_passwords(self):
            # One (or both) passwords weren't given
        data = {'username': 'jsmith'}
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors,
                         [u'This field is required.'])
        self.assertEqual(form['password2'].errors,
                         [u'This field is required.'])



class RegistrationTests(TestCase):
    
    """ test registration page returns 200 status for GET """
    def test_status(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post(
            "/register", data={'username': 'pouria123', 'password': 'UH123456',
            'confirm_password': 'UH123456'}
        ) 
        # verify that response is a 200 (successful POST)
        self.assertEqual(response.status_code, 200)

    def test_registration_form(self):
        # test invalid data
        invalid_data = {"username": "user@test.com", "password": "secret", "confirm_password": "not secret"}
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertFalse(form.errors)

    def test_registration_form2(self):
        # test invalid data
        valid_data = {"username": "user@test.com", "password": "secret", "confirm_password": "secret"}
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)         

    """ Testing submission of a registration that fits the form requirements """
    def test_good_registration(self):
        response = self.client.post(
            "/register", data={'username': 'ali456', 'password': 'Texas44!',
            'confirm_password': 'Texas44!'}
        ) 
        # verify that response is a 200 (successful POST)
        self.assertEqual(response.status_code, 200)


class QuoteFormTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'liz', password ='temporary123456')

    """ test QuoteForm page returns 200 status for GET """
    def test_status(self):
        User = get_user_model()
        self.client.login(username='liz', password='temporary123456')
        user = User.objects.get(username='liz')

        response = self.client.get("/quote")
        self.assertEqual(response.status_code, 200)
    
    
    def test_add_user_invalidform_view(self):
        User = get_user_model()
        self.client.login(username='liz', password='temporary123456')
        user = User.objects.get(username='liz')

        response = self.client.post("/quote", {'gallons': "zerosssormore", 'address': "dds", 'date': "random", 'dsjf': "dfdfsdf"})
        self.assertEqual(response.status_code, 200)


    # Valid Data
    def test_add_admin_form_view(self):
        User = get_user_model()
        self.client.login(username='liz', password='temporary123456')
        user = User.objects.get(username='liz')

        user_count = User.objects.count()
        response = self.client.post("/quote", {'gallons': "zerosssormore", 'address': "123 hello", 'date': "01/10/2000"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count)
    #    self.assertTrue('"error": false' in response.content)


class HistoryTests(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'liz', password ='temporary123456')

    """ test history page returns 200 status for GET """
    def test_status(self):
        User = get_user_model()
        self.client.login(username='liz', password='temporary123456')
        user = User.objects.get(username='liz')
        
        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)


class ProfileTests(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username = 'temp', password ='temporary123456')

    """ test profile page returns 200 status for GET """
    def test_status(self):
        User = get_user_model()
        self.client.login(username='temp', password='temporary123456')
        user = User.objects.get(username='temp')

        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    """ validating a profile form that fits the form requirements """
    def test_profile_form_is_valid(self):
        User = get_user_model()
        self.client.login(username='temp', password='temporary123456')
        user = User.objects.get(username='temp')

        response = self.client.post(
             "/profile", data={'full_name': 'first middle last',
             'address_1': '123 address dr.',
             'address_2': '123 adds dr.',
             'city': 'my city',
             'state': 'tx',
             'zip_code': 77777}
         )
        # verify that response is a redirect (successful POST)
        self.assertEqual(response.status_code, 200)

'''class RegistrationTests(TestCase):
    
    """ test registration page returns 200 status for GET """
    def test_status(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post(
            "/register", data={'username': 'pouria123', 'password': 'UH123456',
            'confirm_password': 'UH123456'}
        ) 
        # verify that response is a 200 (successful POST)
        self.assertEqual(response.status_code, 200)

    def test_registration_form(self):
        # test invalid data
        invalid_data = {"username": "user@test.com", "password": "secret", "confirm_password": "not secret"}
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertFalse(form.errors)

    def test_registration_form2(self):
        # test invalid data
        valid_data = {"username": "user@test.com", "password": "secret", "confirm_password": "secret"}
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)         

    """ Testing submission of a registration that fits the form requirements """
    def test_good_registration(self):
        response = self.client.post(
            "/register", data={'username': 'ali456', 'password': 'Texas44!',
            'confirm_password': 'Texas44!'}
        ) 
        # verify that response is a 200 (successful POST)
        self.assertEqual(response.status_code, 200)
'''
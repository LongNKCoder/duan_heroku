from django.test import TestCase
from django.urls import reverse, resolve
from .views import register_view, LoginViewCus

class ProfileTest(TestCase):
    def test_url(self):
        url = reverse('login_register:register')
        self.assertEquals(resolve(url).func, register_view)

    def test_url(self):
        url = reverse('login_register:login')
        self.assertEquals(resolve(url).func.view_class, LoginViewCus)

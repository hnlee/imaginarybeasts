from django.test import TestCase
from django.urls import resolve
from issues.views import home

class HomePageTest(TestCase):
  def test_root_path_renders_home_view(self):
    root = resolve('/')
    self.assertEqual(root.func, home)

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from issues.views import home

class HomePageTest(TestCase):
  def test_root_path_resolves_to_home_view(self):
    root = resolve('/')
    self.assertEqual(root.func, home)

  def test_home_view_renders_home_template(self):
    request = HttpRequest()
    response = home(request)
    self.assertTrue(response.content.startswith(b'<html>'))
    self.assertIn(b'<title>Imaginary Beasts</title>', response.content)
    self.assertTrue(response.content.endswith(b'</html>'))

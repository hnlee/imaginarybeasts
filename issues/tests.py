from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from issues.views import home

class HomePageTest(TestCase):
  def test_root_path_resolves_to_home_view(self):
    root = resolve('/')
    self.assertEqual(root.func, home)

  def test_home_view_renders_home_template(self):
    request = HttpRequest()
    response = home(request)
    expected_html = render_to_string('home.html')
    self.assertEqual(expected_html, response.content.decode())

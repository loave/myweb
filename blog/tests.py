# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from blog.models import import Author

# Create your tests here.
class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(first_name='zhang',last_name='san',email='zhangsan@gmail.com')
        Author.objects.create(first_name='li',last_name='si',email='lisi@gmail.com')

    def test_add_author_email(self):
        zhang=Author.objects.get(first_name='zhang')
        li=Author.objects.get(first_name='li')
        self.assertEqual(zhang.email,'zhangsan@gmail.com')
        self.assertEqual(li.email,'lisi@gmail.com')
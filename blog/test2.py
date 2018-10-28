from django.test import TestCase
from blog.models import Publisher

class PublisherTestCase(TestCase):
    def setUp(self):
        Publisher.objects.create(name='zhongxin',address='xinyuan south road,chaoyang district,beijing on the 6th',city='beijing',state_province='china',country='beijing',website='http://www.publish.citic.com')

    def test_add_publisher_city(self):
        zhongxin=Publisher.objects.get(name='zhongxin')
        self.assertEqual(zhongxin.city,'beijing')


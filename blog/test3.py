from django.test import TestCase

class MyTest(TestCase):
    def setUp(self):
        num=input('enter a number:')
        self.num=int(num)

    def test_case(self):
        self.assertEqual(self.num,10,msg='you are wrong')

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

class Test(TestCase):
    def setUp(self):
        n=input('enter a number again:')
        self.n=int(n)
        print 'test start'
    def test_case(self):
        print self.n
        self.assertTrue(is_prime(self.n),msg='is not a prime')
    def tearDown(self):
        print 'test end'

class TestIn(TestCase):
    def setUp(self):
        print 'start again'

    def test_case(self):
        a='hello'
        b='hello moto'
        self.assertIn(a,b,msg='a is not in b')

    def tearDown(self):
        print 'end again'
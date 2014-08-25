from django.test import TestCase
from apptesty.models import Tests, Questions, Answers
from apptesty.views import getAnswersDict

class SitesTestCase(TestCase):
    def test_home(self):
	response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def test_registration(self):
	response = self.client.get('/accounts/register/')
        self.failUnlessEqual(response.status_code, 200)

class FunctionsTestCase(TestCase):
    def test_getAnswersDict(self):
      params={ 'test1|1' : '1', 'abc' : '2', 'abcd2|2' : '3'}
      self.failUnlessEqual(getAnswersDict(params, 'test'), {1: [1]})
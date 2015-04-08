import datetime
from django.test import TestCase
from angular.serializers import Serializer


class SerializerTest(TestCase):
    def setUp(self):
        self.serializer = Serializer()

    def test_base_formats_to_simple(self):
        retval = self.serializer.to_simple(data=True)
        self.assertEqual(retval, True)
        retval = self.serializer.to_simple(data=u'test string')
        self.assertEqual(retval, u'test string')
        now = datetime.datetime.now()
        retval = self.serializer.to_simple(data=now)
        self.assertEqual(retval, now.isoformat())

    def test_queryset_to_simple(self):
        pass
from django.test import TestCase
from bangoo.navigation.models import Menu
from bangoo.content.models import Content


class NewMenuTestCase(TestCase):
    def test_add_menu(self):
        self.assertEquals(Content.objects.language('en').count(), 0)
        menu = Menu.handler.add_menu(titles={'en': 'First menu'}, plugin='bangoo.content')
        self.assertEquals(Content.objects.language('en').count(), 1)
        c = Content.objects.language('en').first()
        self.assertEquals(c.url, menu.path)
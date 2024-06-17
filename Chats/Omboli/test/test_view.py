# myapp/tests/test_models.py
from django.test import TestCase
from Omboli.models import MyModel
from Omboli.test.factory import MyModelFactory

class MyModelTestCase(TestCase):

    def test_model_creation(self):
        instance = MyModelFactory()
        self.assertEqual(MyModel.objects.count(), 1)
        self.assertEqual(instance.name, 'Test Name 1')  # Adjust based on your factory setup

    def test_model_attributes(self):
        instance = MyModelFactory(name='Custom Name', description='Custom Description')
        self.assertEqual(instance.name, 'Custom Name')
        self.assertEqual(instance.description, 'Custom Description')

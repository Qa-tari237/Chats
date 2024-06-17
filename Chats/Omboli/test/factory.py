# myapp/tests/factories.py
import factory
from Omboli.models import MyModel

class MyModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MyModel
    
    name = factory.Sequence(lambda n: f'Test Name {n}')
    description = factory.Faker('text')

from django.test import TestCase
from .models import Sentiment

# Create your tests here.
class SentimentModelTest(TestCase):
    def test_should_saved_sentiment(self):
       Sentiment.objects.create(
            text = 'Praew',
            value = True
       )

       actual = Sentiment.objects.last()

       self.assertEqual('Praew', actual.text)
       self.assertEqual(True, actual.value)


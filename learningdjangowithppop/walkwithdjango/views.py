from django.shortcuts import render, redirect
from django.views import View
from .models import Sentiment
from distutils.util import strtobool

def sentiment_list(request):
    if request.method == 'GET':
        good_sentiments = Sentiment.objects.filter(value=True)
        bad_sentiments = Sentiment.objects.filter(value=False)
        return render(request, 'sentiments_list.html', {'good' : good_sentiments, 'bad' : bad_sentiments})


    if request.method == 'POST':
        text = request.POST['text']
        sentiment = strtobool(request.POST['sentiment'])
        Sentiment.objects.create(text=text, value=sentiment)
        good_sentiments = Sentiment.objects.filter(value=True)
        bad_sentiments = Sentiment.objects.filter(value=False)
        return redirect('sentiment_list')


class SentimentView(View):
    def get(self, request):
        sentiments = Sentiment.object.all()
        return render(request, 'sentiments_list.html', {'good' : good_sentiments,     'bad' : bad_sentiments})


    def post(tself, request):
        sentiments = Sentiment.object.all()
        return render(request, 'sentiments_list.html', {'good' : good_sentiments,     'bad' : bad_sentiments})

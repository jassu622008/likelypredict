from django.shortcuts import render

from django.http import HttpResponse

import pickle

from sklearn.linear_model import LogisticRegression


def home(request):
    return render(request, 'index.html')

def pre(request):
    age = request.GET['age']
    with open('templates/main.pkl', 'rb') as f:
        model = pickle.load(f)
        res = model.predict([[age]])
        return render(request, 'index.html', {'res': res[0]})

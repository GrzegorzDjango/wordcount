from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #wie że home.html jest w folderze templates
    #to w settings.py ustawiliścy TEMPLATES = ['templates']
    return render(request, 'home.html')
    #return render(request, 'home.html', {'hi there': 'this is me'})
    #return HttpResponse('<h1>Hello, World!</h1>')

def count(request):
    #fulltext to nazwa pola gdzie człowiek wpisuje tekst
    #gdy wciśnie przycisk to do url będzie dodane ?fulltext=.....
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add
            worddict[word] = 1
    sortedWords = sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)[:10]
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist),
                                        'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')

def eggs(request):
    return HttpResponse('<h1>Get some eggs!</h1>')
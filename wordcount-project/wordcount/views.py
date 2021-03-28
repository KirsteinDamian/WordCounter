from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse('Hello')

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    occurence_count = {}
    for word in wordlist:
        if word not in occurence_count:
            occurence_count[word] = 1
        else:
            occurence_count[word] += 1
    popular_word, popular_count = word_and_count_that_appeared_the_most(occurence_count)
    return render(request, 'count.html', {
        'fulltext': fulltext, 'count': len(wordlist), 'popular_word': popular_word, 'popular_count': popular_count,
    })


def word_and_count_that_appeared_the_most(words: dict):
    popular_word = ""
    popular_count = 0
    for word, count in words.items():
        if popular_count < count:
            popular_count = count
            popular_word = word
    return popular_word, popular_count


def about(request):
    return render(request, 'about.html')

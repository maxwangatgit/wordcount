from django.http import HttpResponse
from django.shortcuts import render # 传达一个网页

def home(request):
    return  render(request,"home.html")

def count(request):
    text = request.GET['text']
    print(len(text))


    word_count = {}
    for word in text:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    sorted_word = sorted(word_count.items(),key=lambda w:w[1],reverse = True) #items 所有内容，按照字典的值进行排序


    context = {'total_count':str(len(text)),
                "text"      : text,
                "word_count":word_count,
                "sorted_word":sorted_word}    

    

    return  render(request,"count.html",context)
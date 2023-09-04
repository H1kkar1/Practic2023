from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

'''
url = 'https://habr.com/ru/search/?target_type=posts&order=relevance&q=%5Bнаучно-популярное%5D'
response = requests.get(url)
soup = BeautifulSoup(response.text)
'''

def index(request):
    return render(request,'main/index.html',)

def about(request):
    return render(request,'main/about.html')

def Error(request,err):
    return render(request,'main/Error_404')

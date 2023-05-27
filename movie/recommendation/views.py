
from recommendation.movie import recommends
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'first.html')


def recommend(request):
    movie_name = request.GET.get('movie_name')
    recommendations = recommends(movie_name)
    return JsonResponse({'recommendations': recommendations})
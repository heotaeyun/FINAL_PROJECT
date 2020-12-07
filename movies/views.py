from django.shortcuts               import render
from django.http                    import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators             import api_view
from rest_framework.response               import Response
from rest_framework                        import status
from .models                               import Movies
from .serializers                          import PopularSerializer

def start(request):
    return render(request, 'movies/start.html')

@login_required
def popular_movies(request):
    """
    이미지, 제목, 레이팅을 인기있는 순서대로 보내주는 API
    """
    movies  = Movies.objects.order_by('-people')
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/main.html', context)


@login_required
def recommend(request):
    """ 추천영화로 랜더링하는 함수"""
    return render(request, 'movies/recommend.html')


def recommendation(request, genre1, genre2):
    """
    추천영화 API
    """
    movies = Movies.objects.order_by('-rate')
    context = {}
    best_movie = []
    first_movie = []
    second_movie = []
    for movie in movies:
        movie_genres = movie.genre.split(' ')
        for movie_genre in movie_genres:
            if movie_genre == genre1:
                temp = {}
                temp['movieId']     = movie.id
                temp['movieTitle']  = movie.title
                temp['movieImgUrl'] = movie.img_url
                temp['movieRate']   = movie.rate
                temp['movieGenres'] = movie.genre
                temp['movieStory']  = movie.story
                first_movie.append(temp)
            if movie_genre == genre2:
                temp = {}
                temp['movieId']     = movie.id
                temp['movieTitle']  = movie.title
                temp['movieImgUrl'] = movie.img_url
                temp['movieRate']   = movie.rate
                temp['movieGenres'] = movie.genre
                temp['movieStory']  = movie.story
                second_movie.append(temp)
    if len(first_movie) > len(second_movie):
        long_length = len(first_movie)
        for i in first_movie:
            for j in second_movie:
                if i == j:
                    best_movie.append(i)
    elif len(first_movie) < len(second_movie):
        for i in second_movie:
            for j in first_movie:
                if i == j:
                    best_movie.append(i)
    context['bestMovie']   = best_movie
    context['firstMovie']  = first_movie
    context['secondMovie'] = second_movie
    return JsonResponse(context, status = 200)

@login_required
def show_movies(request, genre):
    """ context와 함께 genre별로 페이지 렌더링해주는 함수"""
    movies      = Movies.objects.all() 
    genre_movies=[]
    cnt         = 0
    for movie in movies:
        movie_genre = movie.genre.split(' ')
        for com in movie_genre:
            if com == genre:   
                genre_movies.append(movie)
    context = {
        'movies' : genre_movies 
    }
    return render(request, 'movies/moviesByGenre.html', context)


@api_view(['GET'])
def get_api(request, pk):
    movies     = Movies.objects.get(pk=pk)
    serializer = PopularSerializer(movies)
    return Response(serializer.data)


def about(request):
    return render(request, 'movies/about.html')
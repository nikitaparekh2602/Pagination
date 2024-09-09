from django.shortcuts import render
from .models import MovieData
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    movies = MovieData.objects.all()

    # search and filtering code
    movie_name = request.GET.get('movie_name') # get input field name
    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name) # filter by name and __icontains use bacause any alphabatic or space using name get find easyly and name is module field 


    # pagination code
    paginator = Paginator(movies,4)
    page = request.GET.get('page') #get page number
    movies = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', {'movies':movies})
from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

def movie_list(request):
    # Fetch all movies, ordered by name (or any field you prefer)
    movies_object = Movies.objects.all().order_by('name')  # You can use any field like 'name', 'rating', etc.

    # Get the search query from the request
    movie_name = request.GET.get('movie_name', '').strip()

    # If a movie name is provided, filter the movies
    if movie_name:
        movies_object = Movies.objects.filter(name__icontains=movie_name).order_by('name')  # Keep the ordering here too

    # Set up pagination
    paginator = Paginator(movies_object, 4)  # Show 4 movies per page
    page_number = request.GET.get('page')  # Get the page number from the request
    movies_object = paginator.get_page(page_number)  # Get the page object

    context = {
        'movie_list': movies_object
    }

    return render(request, "app/movies_list.html", context)

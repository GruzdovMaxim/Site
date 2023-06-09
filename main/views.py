from django.shortcuts import render
from movies.models import MovieGenre, TheMovie
from celebrities.models import Actor
from django.http import HttpResponse


# Create your views here.
def index(request):
    all_movies = TheMovie.objects.all()
    # for one_movie in all_movies:
    #     print(one_movie.genres.all())
    five_celebrities = Actor.objects.all()[:5]
    # print(five_actors)
    # current_user_username = request.session.get("current_user_username")
    # current_user_directory_name = request.session.get("current_user_username")
    errors = {}
    if request.session.get("login_error"):
        print(request.session.get("login_error"))
        errors["login_error"] = request.session["login_error"]
        del request.session["login_error"]
        # ensuring that everything is okey
        request.session.modified = True
        request.session.save()

    if request.session.get("signup_error"):
        print(request.session.get("signup_error"))
        errors["signup_error"] = request.session["signup_error"]
        del request.session["signup_error"]
        # ensuring that everything is okey
        request.session.modified = True
        request.session.save()
    return render(request, 'main/index.html',
                  {"all_movies": all_movies, "selected_celebrities": five_celebrities} | errors)

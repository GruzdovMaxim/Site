from django.shortcuts import render
from .models import Actor


def get_appropriate_movies(arg_request):
    all_celebrities = Actor.objects.all()
    print(arg_request.GET)

    defined_celebrities = []
    text_for_input = arg_request.GET.get("text_for_input")
    country = arg_request.GET.get("country")
    year_of_birth_from = arg_request.GET.get("year_of_birth_from")
    year_of_birth_to = arg_request.GET.get("year_of_birth_to")

    for one_celebrity in all_celebrities:
        appropriate_movie = True
        # print(text_for_input)
        # print(one_movie.title)
        # print(text_for_input in one_movie.title)
        if text_for_input is not None and text_for_input != "" and text_for_input.lower() not in one_celebrity.full_name.lower():
            appropriate_movie = False
        # if appropriate_movie and skills is not None:
        #     if type(skills) != list:
        #         skills = [skills]
        #     appropriate_movie = all(elem in list(map(lambda one_genre_name: one_genre_name.title(), list(
        #         one_celebrity.genres.all().values_list("whole_name", flat=True)))) for elem in skills)
        if country is not None and country != "" and country != one_celebrity.country:
            appropriate_movie = False

        if year_of_birth_from is not None and year_of_birth_from != "" and int(
                year_of_birth_from) > one_celebrity.date_of_birth.year:
            appropriate_movie = False

        if year_of_birth_to is not None and year_of_birth_to != "" and int(
                year_of_birth_to) < one_celebrity.date_of_birth.year:
            appropriate_movie = False
        if appropriate_movie:
            defined_celebrities.append(one_celebrity)
        # print(defined_movies)

    return defined_celebrities


# Create your views here.
def celebrities(request):
    defined_celebrities = get_appropriate_movies(request)
    defined_countries = set(Actor.objects.values_list("country", flat=True))
    # print(type(defined_countries))

    return render(request, 'celebrities/celebrities.html', {"defined_celebrities": defined_celebrities,
                                                            "defined_countries": defined_countries})


def celebrities_list(request):
    defined_celebrities = get_appropriate_movies(request)
    defined_countries = set(Actor.objects.values_list("country", flat=True))
    # print(type(defined_countries))

    return render(request, 'celebrities/celebrities_list.html', {"defined_celebrities": defined_celebrities,
                                                                 "defined_countries": defined_countries})


def celebrities_single(request, celebrities_id):
    selected_celebrity = Actor.objects.get(pk=celebrities_id)
    celebrity_short_description = selected_celebrity.short_description.split("\n")
    celebrity_biography = selected_celebrity.biography.split("\n")
    return render(request, 'celebrities/celebrities_single.html', {"selected_celebrity": selected_celebrity,
                                                                   "the_short_description": celebrity_short_description,
                                                                   "the_biography": celebrity_biography})

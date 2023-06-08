import os
import shutil
from datetime import datetime  # 'date' doesn't work!!!

from pymongo import MongoClient

genres_documents = [
    {"whole_name": "sci-fi", "background_color": "#1692bb",
     "wiki_link": "https://en.wikipedia.org/wiki/Science_fiction_film"},
    {"whole_name": "adventure", "background_color": "#ec5a1a",
     "wiki_link": "https://en.wikipedia.org/wiki/Adventure_film"},
    {"whole_name": "comedy", "background_color": "#a6bb16", "wiki_link": "https://en.wikipedia.org/wiki/Comedy_film"},
    {"whole_name": "action", "background_color": "#f5b50a", "wiki_link": "https://en.wikipedia.org/wiki/Action_film"},
    {"whole_name": "horror", "background_color": "#262626", "wiki_link": "https://en.wikipedia.org/wiki/Horror_film"},
    {"whole_name": "fantasy", "background_color": "#5e548e", "wiki_link": "https://en.wikipedia.org/wiki/Fantasy_film"}
]

movies_documents = [
    {
        "title": "Inception",
        "director": "Christopher Nolan",
        "writer": "Christopher Nolan",
        "release_date": datetime(2010, 7, 16),
        "duration": "2h 28min",
        "movie_score": 7.8,
        "MPAA_rating": "PG-13",
        "directory_name": "Inception_123456",
        "on_tv": True,
        "in_cinema": True
    },
    {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "writer": "Stephen King",
        "release_date": datetime(1994, 9, 23),
        "duration": "2h 22min",
        "movie_score": 9.3,
        "MPAA_rating": "R",
        "directory_name": "The_Shawshank_Redemption_654321",
        "on_tv": True,
        "in_cinema": False
    },
    {
        "title": "Jurassic Park",
        "director": "Steven Spielberg",
        "writer": "Michael Crichton",
        "release_date": datetime(1993, 6, 11),
        "duration": "2h 7min",
        "movie_score": 5.1,
        "MPAA_rating": "PG-13",
        "directory_name": "Jurassic_Park_789012",
        "on_tv": False,
        "in_cinema": True
    },
    {
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "writer": "Jonathan Nolan",
        "genres": ["adventure", "drama", "sci-fi"],
        "release_date": datetime(2014, 11, 7),
        "duration": "169",
        "movie_score": 8.6,
        "MPAA_rating": "PG-13",
        "directory_name": "Interstellar_789",
        "on_tv": False,
        "in_cinema": False
    },
    {
        "title": "The Green Mile",
        "director": "Frank Darabont",
        "writer": "Stephen King",
        "genres": ["crime", "drama", "fantasy"],
        "release_date": datetime(1999, 12, 10),
        "duration": "189",
        "movie_score": 8.6,
        "MPAA_rating": "R",
        "directory_name": "The_Green_Mile_654",
        "on_tv": False,
        "in_cinema": False
    },
    {
        "title": "Jaws",
        "director": "Steven Spielberg",
        "writer": "Peter Benchley",
        "genres": ["adventure", "thriller"],
        "release_date": datetime(1975, 6, 20),
        "duration": "124",
        "movie_score": 3.0,
        "MPAA_rating": "PG",
        "directory_name": "Jaws_321",
        "on_tv": False,
        "in_cinema": False
    },
    {
        "title": "The Matrix",
        "director": "Lana Wachowski, Lilly Wachowski",
        "writer": "Lana Wachowski, Lilly Wachowski",
        "genres": ["action", "sci-fi"],
        "release_date": datetime(1999, 3, 31),
        "duration": "136",
        "movie_score": 8.7,
        "MPAA_rating": "R",
        "directory_name": "The_Matrix_987",
        "on_tv": False,
        "in_cinema": False
    },
    {
        "title": "Fight Club",
        "director": "David Fincher",
        "writer": "Chuck Palahniuk",
        "genres": ["drama"],
        "release_date": datetime(1999, 10, 15),
        "duration": "139",
        "movie_score": 8.8,
        "MPAA_rating": "R",
        "directory_name": "Fight_Club_123",
        "on_tv": False,
        "in_cinema": False
    }

]

relationship_documents = [
    {"themovie_id": 1, "moviegenre_id": 1},  # Inception - sci-fi
    {"themovie_id": 1, "moviegenre_id": 4},  # Inception - action
    {"themovie_id": 2, "moviegenre_id": 3},  # The Shawshank Redemption - comedy
    {"themovie_id": 3, "moviegenre_id": 2},  # Jurassic Park - adventure
    {"themovie_id": 3, "moviegenre_id": 4}  # Jurassic Park - action
]

actors_documents = [
    {
        "full_name": "Leonardo DiCaprio",
        "date_of_birth": datetime(1974, 11, 11),
        "country": "United States",
        "height": 183,
        "directory_name": "Leonardo_DiCaprio_123",
        "short_description": "Is very cool\n",
        "biography": "Is very cool biography"
    },
    {
        "full_name": "Morgan Freeman",
        "date_of_birth": datetime(1937, 6, 1),
        "country": "United States",
        "height": 188,
        "directory_name": "Morgan_Freeman_456",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Tom Hanks",
        "date_of_birth": datetime(1956, 7, 9),
        "country": "United States",
        "height": 183,
        "directory_name": "Tom_Hanks_789",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Scarlett Johansson",
        "date_of_birth": datetime(1984, 11, 22),
        "country": "United States",
        "height": 160,
        "directory_name": "Scarlett_Johansson_987",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Robert Downey Jr.",
        "date_of_birth": datetime(1965, 4, 4),
        "country": "United States",
        "height": 174,
        "directory_name": "Robert_Downey_Jr_654",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Jennifer Lawrence",
        "date_of_birth": datetime(1990, 8, 15),
        "country": "United States",
        "height": 175,
        "directory_name": "Jennifer_Lawrence_321",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Denzel Washington",
        "date_of_birth": datetime(1954, 12, 28),
        "country": "United States",
        "height": 185,
        "directory_name": "Denzel_Washington_789",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Emma Stone",
        "date_of_birth": datetime(1988, 11, 6),
        "country": "United States",
        "height": 168,
        "directory_name": "Emma_Stone_654",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Brad Pitt",
        "date_of_birth": datetime(1963, 12, 18),
        "country": "United States",
        "height": 180,
        "directory_name": "Brad_Pitt_321",
        "short_description": "",
        "biography": ""
    },
    {
        "full_name": "Natalie Portman",
        "date_of_birth": datetime(1981, 6, 9),
        "country": "Israel",
        "height": 160,
        "directory_name": "Natalie_Portman_987",
        "short_description": "",
        "biography": ""
    },
]

all_filling_data = [genres_documents, movies_documents, relationship_documents, actors_documents]
amount_of_fillings = len(all_filling_data)
if __name__ == '__main__':
    # for creating directories for movies
    whole_path_directory_of_movies = "/tortillasite/main/static/main/images/movies\\"
    # print(os.makedirs(
    #     whole_path_directory_of_movies, exist_ok=True))
    # print(os.path.exists(
    #     whole_path_directory_of_movies
    # ))
    # shutil.rmtree("tortillasite/main/static/main/images/movies/prikol")

    # movie documents processing, about genres and creating directories for movies
    for one_document_index in range(len(movies_documents)):
        os.makedirs(whole_path_directory_of_movies + movies_documents[one_document_index]["directory_name"],
                    exist_ok=True)
        print(movies_documents[one_document_index]["title"])
        if "genres" in movies_documents[one_document_index]:
            # for one_defined_genre in movies_documents[one_document_index]["genres"]:
            for one_selected_genre_index in range(len(genres_documents)):
                if genres_documents[one_selected_genre_index]["whole_name"] \
                        in movies_documents[one_document_index]["genres"]:
                    relationship_documents.append({"themovie_id": one_document_index + 1,
                                                   "moviegenre_id": one_selected_genre_index + 1})
            del movies_documents[one_document_index]["genres"]

    client = MongoClient(
        'mongodb+srv://lexa_admin:G1ixqFQEpieq2LMz@cluster0.2vx4osp.mongodb.net/?retryWrites=true&w=majority')
    db = client.db_example11
    all_collections = [db.movies_moviegenre, db.movies_themovie, db.movies_themovie_genres, db.celebrities_actor]

    for one_filling_data_index in range(amount_of_fillings):
        all_collections[one_filling_data_index].delete_many({})

        the_length = all_collections[one_filling_data_index].count_documents({})
        for the_index, one_document in enumerate(all_filling_data[one_filling_data_index]):
            one_document["id"] = the_index + the_length + 1
        all_collections[one_filling_data_index].insert_many(all_filling_data[one_filling_data_index])

        client.close()

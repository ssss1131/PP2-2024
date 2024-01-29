movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def IMDB(movie):
    return movie["imdb"] >= 5.5


def good_one(movies):
    nice = []
    for i in movies:
        if IMDB(i):
            nice.append(i["name"])
    return nice


def category(cat):
    film_same_cat = []
    for i in movies:
        if i["category"] == cat:
            film_same_cat.append(i["name"])
    return film_same_cat


def average_IMDB(list):
    sum = 0
    for i in list:
        sum += i["imdb"]
    return sum / len(list)


def average_cat_IMDB(cat):
    sum = 0
    num_of_cat = 0
    for i in movies:
        if i["category"] == cat:
            sum += i["imdb"]
            num_of_cat += 1
    return sum / num_of_cat


#print(IMDB(movies[1]))
#print(IMDB(movies[7]))
#print(good_one(movies[6:11]))
#print(category("Romance"))
#print(average_IMDB(movies[0:3]))
#print(average_cat_IMDB("Romance"))

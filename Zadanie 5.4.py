import random

class Movies:
    def __init__(self, title, release_year, genre, nov):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.nov = nov
        self.vievs = 0
        
    def play(self, views=1):
        self.vievs += views

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    

class Series(Movies):
    def __init__(self, episode_nmb, sezon_nmb, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_nmb = episode_nmb
        self.sezon_nmb = sezon_nmb

    def __str__(self):
        return f'{self.title} S{self.sezon_nmb}E{self.episode_nmb}'
    
    
def get_movies():
    movies = [item for item in data if type(item) == Movies]
    return sorted(movies, key=lambda movie: movie.title)

def get_series():
    series = [item for item in data if type(item) == Series]
    return sorted(series, key=lambda serie: serie.title)

def search(title):
    for item in data:
        if item.title == title:
            return item
    return None

def generate_views():
    item = random.choice(data)
    views = random.randint(1, 100)
    item.play(views)
    #print(f'{item} - {views}')

def generate_views_10():
    for i in range(10):
        generate_views()

def top_titles(amount):
    return sorted(data, key=lambda item: item.vievs, reverse=True)[:amount]



movie1 = Movies('Forrest Gump', '1994', 'Drama', 10)
movie2 = Movies('Predator', '1987', 'Action', 15)
movie3 = Movies('Conan The Barbarian', '1982', 'Fantasy', 100)

series1 = Series(10, 11, 'X Files', '1992', 'Sci-Fi', 94)
series2 = Series(8, 2, 'Fallout', '2024', 'Sci-Fi', 27)
series3 = Series(10, 9, 'Game of Thrones', '2007', 'Fantasy', 500,)

data = [movie1, movie2, movie3, series1, series2, series3]


#for movie in get_movies():
    #print(movie)

#for serie in get_series():
    #print(serie)

#print(search('Forrest Gump'))

#generate_views()

generate_views_10()

for item in top_titles(3):
    print(item, item.vievs)

#print(movie1)
#print(series1)
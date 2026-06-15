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
        self.vievs = 0
    
    def play(self, views=1):
        self.vievs += views

    def __str__(self):
        return f'{self.title} S{self.sezon_nmb}E{self.episode_nmb}'
    
    
def get_movies():
    for item in movies_sorted:
     print(item.title)

def get_series():
    for item in series_sorted:
        print(item.title)

movie1 = Movies('Forrest Gump', '1994', 'Drama', 10)
movie2 = Movies('Predator', '1987', 'Action', 15)
movie3 = Movies('Conan The Barbarian', '1982', 'Fantasy', 100)

series1 = Series(10, 11, 'X Files', '1992', 'Sci-Fi', 94)
series2 = Series(8, 2, 'Fallout', '2024', 'Sci-Fi', 27)
series3 = Series(10, 9, 'Game of Thrones', '2007', 'Fantasy', 500,)

data = [movie1, movie2, movie3, series1, series2, series3]

movies_o = [item for item in data if type(item) == Movies]
movies_sorted = sorted(movies_o, key=lambda movie: movie.title)

series_o = [item for item in data if type(item) == Series]
series_sorted = sorted(series_o, key=lambda serie: serie.title)



#get_movies()
#get_series()

print(movie1)
print(series1)



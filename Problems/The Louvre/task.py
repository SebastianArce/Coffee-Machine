class Painting:
    museum = 'Louvre'

    def __init__(self, title_, painter_, year_):
        self.title_ = title_
        self.painter_ = painter_
        self.year_ = year_


title = input()
artist = input()
year = input()

art = Painting(title, artist, year)
print(f'"{art.title_}" by {art.painter_} ({art.year_}) hangs in the {Painting.museum}.')
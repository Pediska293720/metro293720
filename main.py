class User:
    def __init__(self, login: str):
        self.login = login

class Line:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

class Station:
    def __init__(self, name: str):
        self.name = name

class Line_Station:
    def __init__(self, line, station):
        self.line = line
        self.station = station

class Image:
    def __init__(self, url: str):
        self.url = url

class User_Station:
    def __init__(self, user: User, station: Station, date: str, image: Image):
        self.user = user
        self.station = station
        self.date = date
        self.image = image

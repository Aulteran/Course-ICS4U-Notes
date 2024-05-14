class Catalogue():
    def __init__(self):
        self.catalogue = []
    
    def checkOut(self):
        raise NotImplementedError
    
    def checkIn(self):
        raise NotImplementedError
    
    def bookSearch(self):
        raise NotImplementedError
    
    def genreSearch(self):
        raise NotImplementedError
    
class Book():
    def __init__(self,iden,title,desc,genre,status):
        self.iden = iden
        self.title = title
        self.desc = desc
        self.genre = genre
        self.status = status

    def addTo_catalogue(self):
        raise NotImplementedError
    
    def updateInfo(self):
        raise NotImplementedError

class Student():
    def __init__(self, iden,name,username,password):
        self.iden = iden
        self.name = name
        self.username = username
        self.password = password

    def changePass(self):
        raise NotImplementedError
    
    def borrowBook(self):
        raise NotImplementedError
    

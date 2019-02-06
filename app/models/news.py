class Source:
    '''
    Source class to define news objects (sources)
    '''
    def __init__ (self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    '''
    Articles class to define Articles objects
    '''
    def __init__(self,id,author,title,description,url,publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = descrption
        self.url = url
        self.publishedAt = publishedAt

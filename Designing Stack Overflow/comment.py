class Comment():
    def __init__(self,author:str,detail:str):
        self.id = id(self)
        self.author = author
        self.detail = detail
        
class Recipe:

    def __init__(self, id, name, cooking_time, rating):
        self.id = id
        self.name = name
        self.cooking_time = cooking_time
        self.rating = rating
    
    def __eq__(self, other):
        print(self.__dict__)
        print(other.__dict__)
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.name}, {self.cooking_time}, {self.rating})"
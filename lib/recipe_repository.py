from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["name"], row["cooking_time"], row["rating"])
            recipes.append(item)

        return recipes
    
    def find(self,name):
        rows = self._connection.execute('SELECT * from recipes where name = %s', [name])
        row = rows[0]
        return Recipe(row["id"], row["name"], row["cooking_time"], row["rating"])
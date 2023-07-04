from lib.recipe_repository import RecipeRepository
from lib.recipe import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()
    assert recipes == [
        Recipe(1, "Chicken Curry", 90, 6.0),
        Recipe(2, "Roast chicken", 125, 8),
        Recipe(3, "Chips", 15, 7),
    ]

def test_find_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find('Roast chicken')

    assert recipe == Recipe(2, "Roast chicken", 125, 8)
    


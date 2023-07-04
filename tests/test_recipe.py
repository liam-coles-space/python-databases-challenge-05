from lib.recipe import Recipe

def test_recipe_construct():
    recipe = Recipe(1, 'Curry', 45, 8.6)
    assert recipe.id == 1
    assert recipe.name == 'Curry'
    assert recipe.cooking_time == 45
    assert recipe.rating == 8.6

def test_recipes_format_nicely():
    recipe = Recipe(1, "Chicken Curry", 15, 8)
    assert str(recipe) == "Recipe(1, Chicken Curry, 15, 8)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.


def test_recipes_are_equal():
    recipe1 = Recipe(1, "Chicken Curry", 15, 8)
    recipe2 = Recipe(1, "Chicken Curry", 15, 8)
    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).


Table design:

Nouns:
recipes, name, cooking time, rating

Record  |   Properties
Recipe      name, cooking_time, rating

Name: text
cooking_time: int
rating: numeric(2,1)

SQL:

file: recipes.sql
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating numeric(2,1)
)

Classes:

Model:
class recipe:
    #name: string
    #cooking_time: int
    #rating: float(1)

Repository:
class recipe_repository:
    #No properties

    def all(self):
        #Gets all records as a list of recipe objects

    def find(self, name):
        #Finds single recipe based on name from recipes table and returns it as recipe object


Tests:

recipe:
#When I create a recipe object it has the correct properties



recipe_repository: 
#When i call the all method i get a list of recipe objects back that represents all the records in the recipes table

#When I call the find method with a name i get a single recipe object that represents the record in the recipes table that has the matching name 












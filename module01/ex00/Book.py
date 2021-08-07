from typing import List
import datetime
import Recipe

class Book:   

    def __init__(self, name: str = "My recipe book") -> None:
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list: dict[Recipe.RecipeType, List[Recipe.Recipe]] = {
            Recipe.RecipeType.STARTER : [],
            Recipe.RecipeType.CORE : [],
            Recipe.RecipeType.DESSERT : [],
            Recipe.RecipeType.OTHER : []
        }

    def get_recipe_by_name(self, name) -> Recipe.Recipe:
        """Print a recipe with the name `name` and return the instance"""

        recipe = None
        
        for lst in self.recipes_list.values():
            recipe = next((recipe for recipe in lst if recipe.name == name), None)
            if recipe:
                break
        else:
            print(f"No recipe for the name \"{name}\"")
            return

        print(str(recipe))
        return recipe

    def get_recipes_by_types(self, recipe_type: Recipe.RecipeType):
        """Get all recipe names for a given recipe_type """
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe.Recipe):
        """Add a recipe to the book and update last_update"""
        
        if type(recipe) is not Recipe.Recipe:
            print(f"Type error: Expected Recipe but got {type(recipe)}")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
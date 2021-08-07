from typing import List
from enum import Enum
import sys


class RecipeType(Enum):
    STARTER = 1
    CORE = 2
    DESSERT = 3
    OTHER = 4
        


class Recipe:
    def __init__(self, name: str, cooking_lvl: int, ingredients: List[str], description: str, recipe_type: RecipeType) -> None:
        if not name:
            print("Error: Name is required", file=sys.stderr)
            return
        if cooking_lvl < 1 or cooking_lvl > 5:
            print(
                "Error: `cooking_lvl` should be in the range [1, 5]", file=sys.stderr)
            return
        if not ingredients:
            print("Error: `ingredients` must not be empty", file=sys.stderr)
            return
        if not recipe_type:
            print("Error: `recipe_type` is required", file=sys.stderr)
            return

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self) -> str:
        return f"""{self.name}:
Level: {self.cooking_lvl}
Ingredients: {", ".join(self.ingredients)}
Recipe type: {str(self.recipe_type)}
Description: {self.description}        
"""

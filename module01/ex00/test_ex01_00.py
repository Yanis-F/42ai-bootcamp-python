import Book
import Recipe
from time import sleep

def make_recipe_pizza() -> Recipe.Recipe:
    return Recipe.Recipe("pizza", 2, ["tomato", "chorizo", "cheeze", "ananas"], "An italian pizza", Recipe.RecipeType.CORE) 
def make_recipe_soup() -> Recipe.Recipe:
    return Recipe.Recipe("soup",1 , ["water"], "Yes, that's basically water", Recipe.RecipeType.CORE) 
def make_recipe_cake() -> Recipe.Recipe:
    return Recipe.Recipe("cake",1 , ["sugar", "chocolate", "banana"], "This is delicious", Recipe.RecipeType.DESSERT) 
def make_recipe_milk() -> Recipe.Recipe:
    return Recipe.Recipe("milk",1 , ["water", "white colorant"], "Pure milk", Recipe.RecipeType.STARTER) 
def make_recipe_wine() -> Recipe.Recipe:
    return Recipe.Recipe("wine",5 , ["water", "red colorant"], "Pure wine", Recipe.RecipeType.OTHER) 

def test_add(capsys):
    book = Book.Book()

    assert book.creation_date == book.last_update

    recipe = make_recipe_pizza()

    book.add_recipe(recipe)

    assert book.get_recipe_by_name(recipe.name) == recipe
    assert book.last_update >= book.creation_date 

    captured = capsys.readouterr()
    assert captured.out == str(recipe) + "\n"
    assert captured.err == ""
    

def test_get_by_type():
    book = Book.Book()

    assert book.creation_date == book.last_update

    recipe_pizza = make_recipe_pizza()
    recipe_soup = make_recipe_soup()
    recipe_cake = make_recipe_cake()
    recipe_milk = make_recipe_milk()
    recipe_wine = make_recipe_wine()

    book.add_recipe(recipe_pizza)

    starters = book.get_recipes_by_types(Recipe.RecipeType.STARTER)
    cores = book.get_recipes_by_types(Recipe.RecipeType.CORE)
    desserts = book.get_recipes_by_types(Recipe.RecipeType.DESSERT)
    others = book.get_recipes_by_types(Recipe.RecipeType.OTHER)

    assert len(starters) == 0
    assert len(cores) == 1
    assert len(desserts) == 0
    assert len(others) == 0

    assert recipe_pizza in cores


    book.add_recipe(recipe_soup)

    starters = book.get_recipes_by_types(Recipe.RecipeType.STARTER)
    cores = book.get_recipes_by_types(Recipe.RecipeType.CORE)
    desserts = book.get_recipes_by_types(Recipe.RecipeType.DESSERT)
    others = book.get_recipes_by_types(Recipe.RecipeType.OTHER)

    assert len(starters) == 0
    assert len(cores) == 2
    assert len(desserts) == 0
    assert len(others) == 0

    assert recipe_pizza in cores
    assert recipe_soup in cores


    book.add_recipe(recipe_cake)

    starters = book.get_recipes_by_types(Recipe.RecipeType.STARTER)
    cores = book.get_recipes_by_types(Recipe.RecipeType.CORE)
    desserts = book.get_recipes_by_types(Recipe.RecipeType.DESSERT)
    others = book.get_recipes_by_types(Recipe.RecipeType.OTHER)

    assert len(starters) == 0
    assert len(cores) == 2
    assert len(desserts) == 1
    assert len(others) == 0

    assert recipe_pizza in cores
    assert recipe_soup in cores
    assert recipe_cake in desserts


    book.add_recipe(recipe_milk)

    starters = book.get_recipes_by_types(Recipe.RecipeType.STARTER)
    cores = book.get_recipes_by_types(Recipe.RecipeType.CORE)
    desserts = book.get_recipes_by_types(Recipe.RecipeType.DESSERT)
    others = book.get_recipes_by_types(Recipe.RecipeType.OTHER)

    assert len(starters) == 1
    assert len(cores) == 2
    assert len(desserts) == 1
    assert len(others) == 0

    assert recipe_pizza in cores
    assert recipe_soup in cores
    assert recipe_cake in desserts
    assert recipe_milk in starters


    book.add_recipe(recipe_wine)

    starters = book.get_recipes_by_types(Recipe.RecipeType.STARTER)
    cores = book.get_recipes_by_types(Recipe.RecipeType.CORE)
    desserts = book.get_recipes_by_types(Recipe.RecipeType.DESSERT)
    others = book.get_recipes_by_types(Recipe.RecipeType.OTHER)

    assert len(starters) == 1
    assert len(cores) == 2
    assert len(desserts) == 1
    assert len(others) == 1

    assert recipe_pizza in cores
    assert recipe_soup in cores
    assert recipe_cake in desserts
    assert recipe_milk in starters
    assert recipe_wine in others


def test_modif_time(capsys):
    book = Book.Book()

    assert book.creation_date == book.last_update

    recipe = make_recipe_pizza()

    sleep(1)
    book.add_recipe(recipe)

    assert book.get_recipe_by_name(recipe.name) == recipe
    assert book.last_update > book.creation_date          # note: stricly greater because we slept 1 second

    captured = capsys.readouterr()
    assert captured.out == str(recipe) + "\n"
    assert captured.err == ""
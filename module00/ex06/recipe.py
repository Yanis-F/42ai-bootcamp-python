import sys

recipe_book = {
    "sandwich" : {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : "10 minutes"
    },
    "cake" : {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : "60 minutes"
    },
    "salad" : {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : "15 minutes"
    }
}


def pick_menu() -> str:
    print("Available meals: " + ", ".join(recipe_book.keys()))
    name = input("Meal name: ")
    while not name in recipe_book:
        name = input("Please input a valid meal\n")

    return name



def add_menu():
    name = input("Meal name: ")
    
    if name in recipe_book:
        yn = input("A meal of this name already exists, do you want to delete it ? (y/n)\n")

        if not (yn.lower() == "y" or yn.lower() == "yes"):
            add_menu()
            return


    ingredients = input("comma-separated list of ingredients: ").split(',')
    meal_type = input("meal type (breakfast/meal/lunch ....): ")
    prep_time = input("preparation time: ")

    recipe_book[name] = {
        "ingredients": ingredients,
        "meal" : meal_type,
        "prep_time" : prep_time
    }

def delete_menu():
    recipe_book.pop(pick_menu())

def print_recipe_menu(name: str = None):
    if name == None:
        name = pick_menu()

    menu = recipe_book[name]

    print(f"""Recipe for {name}:
Ingredients: {", ".join(menu["ingredients"])}
To be eaten for {menu["meal"]}
Takes {menu["prep_time"]} of cooking
""")

def print_cookbook():
    print("Cookbook :")
    for key in recipe_book:
        print_recipe_menu(key)

def quit():
    sys.exit()

def main_menu():
    while True:
        choice = input(
"""Please selet an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
""")

        try:
            options = {
                1: add_menu,
                2: delete_menu,
                3: print_recipe_menu,
                4: print_cookbook,
                5: quit,
            }

            fn = options[int(choice)]

            try:
                fn()
            except Exception:
                print("Command internal error. If the problem persists just give up")

        except Exception: 
            print("This option does not exists, please type the corresponding number.\nTo exit, enter 5.")



if __name__ == "__main__":
    main_menu()

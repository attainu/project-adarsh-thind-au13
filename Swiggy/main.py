import swiggy_app
import restaurants

if __name__ == "__main__":
    swiggy = swiggy_app.SwiggyApp()
    dominoes = restaurants.Restaurant('domino', [])
    swiggy.view_all_restaurants()
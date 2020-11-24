class SwiggyApp:
    def __init_(self):
        self.restros = list()
        self.clients = list()


    def view_all_restaurants(self):
        for restro in self.restros:
            print(restro.name)
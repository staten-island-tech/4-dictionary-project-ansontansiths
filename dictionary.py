def dictionary():
    print("welcome to the shop dictionary what would you like to search for?")
    
    def search():
        search = input("enter item name:")

        if search == "garlic bread":
            print("garlic bread is in the hot food area would you like to purchase this item?")
        elif search == "milk":
            print("milk is in the refrigeration area would you like to purchase this item?")
        elif search == "eggs":
            print("eggs are in the refrigeration area would you like to purchase this item?")
        elif search == NameError:
            print("sorry we do not have that item in stock would you like to search for something else?")
            search()
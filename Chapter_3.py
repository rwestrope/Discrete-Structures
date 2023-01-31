#cashiers algorithm

BeverageMenu = {
    "Water: $1.00": 1,
    "Dr. Pepper": "$2.00",
    "Coca-Cola": "$2.00",
    }
BurgerMenu = {
    "Classic Burger": "$7.00",
    "Organic Sirloin Burger": "$9.00",
    "Greek Burger": "$10.00",
    "Bacon Cheeseburger":"$8.00", 
    "Quinoa and Black Bean Burger":"$9.00"
    }
SideMenu = {
    "Onion Rings": "$3.50",
    "Fries": "$3.00", 
    "Sweet Potato Fries": "$4.00", 
    "Mozzarella Sticks": "$3.00"
    }
DessertMenu = {
    "Cookie": "$2.50", 
    "Brownie": "$2.50"
    }

def GetBeverages():
    global user_beverage
    print("Beverages:")
    for beverage, price in BeverageMenu.items():
        print(beverage, price)
    user_beverage = input("Choose a beverage")
    return user_beverage

def GetBurgers():
    global user_burger
    print("\nBurgers")
    for burger, price in BurgerMenu.items():
        print(burger, price)
    user_burger = input("Choose a beverage")
    return user_burger

def GetSides():
    global user_side
    print("\nSides")
    for side, price in SideMenu.items():
        print(side, price)
    user_side = input("Choose a beverage")
    return user_side

def GetDesserts():
    global user_dessert
    print("\nDesserts")
    for dessert, price in DessertMenu.items():
        print(dessert, price)
    user_dessert = input("Choose a beverage")
    return user_dessert

def GetUserTotal():
    if user_beverage in BeverageMenu():
        print("hi")
        #beverage_cost = 
    #user_total = 


if __name__ == "__main__":
    GetBeverages()
    GetBurgers()
    GetSides()
    GetDesserts()

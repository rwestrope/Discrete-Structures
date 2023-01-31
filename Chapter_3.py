#cashiers algorithm

BeverageMenu = {
    "Water: $": "1.00",
    "Dr. Pepper: $": "2.00",
    "Coca-Cola: $": "2.00",
    }
BurgerMenu = {
    "Classic Burger: $": "7.00",
    "Organic Sirloin Burger: $": "9.00",
    "Greek Burger: $": "10.00",
    "Bacon Cheeseburger: $":"8.00", 
    "Quinoa and Black Bean Burger: $":"9.00"
    }
SideMenu = {
    "Onion Rings: $": "3.50",
    "Fries: $": "3.00", 
    "Sweet Potato Fries: $": "4.00", 
    "Mozzarella Sticks: $": "3.00"
    }
DessertMenu = {
    "Cookie: $": "2.50", 
    "Brownie: $": "2.50"
    }

def GetBeverages():
    global user_beverage
    print("Beverages:")
    for beverage, price in BeverageMenu.items():
        print(beverage, price)
    user_beverage = input("Choose a beverage\n:")
    return user_beverage

def GetBurgers():
    global user_burger
    print("\nBurgers")
    for burger, price in BurgerMenu.items():
        print(burger, price)
    user_burger = input("Choose a beverage\n:")
    return user_burger

def GetSides():
    global user_side
    print("\nSides")
    for side, price in SideMenu.items():
        print(side, price)
    user_side = input("Choose a beverage\n:")
    return user_side

def GetDesserts():
    global user_dessert
    print("\nDesserts")
    for dessert, price in DessertMenu.items():
        print(dessert, price)
    user_dessert = input("Choose a beverage\n:")
    return user_dessert

def GetUserTotal():
    global user_dessert, user_beverage, user_burger, user_side, total_cost
    #global total_cost, beverage_cost, burger_cost, side_cost, dessert_cost
    beverage_cost = 0
    burger_cost = 0
    side_cost = 0
    dessert_cost = 0
    for beverage, cost in BeverageMenu.items():
        if beverage.replace(": $", "") == user_beverage:
            
            print(f"The cost of your beverage is ${cost}")
            beverage_cost += float(cost)
            
    for burger, cost in BurgerMenu.items():
        if burger.replace(": $", "") == user_burger:
            print(f"The cost of your burger is ${cost}")
            burger_cost += float(cost)
            
    for side, cost in SideMenu.items():
        if side.replace(": $", "") == user_side:
            print(f"The cost of your side is ${cost}")
            side_cost += float(cost)
            
    for dessert, cost in DessertMenu.items():
        if dessert.replace(": $", "") == user_dessert:
            print(f"The cost of your dessert is ${cost}")
            dessert_cost += float(cost)
            
    total_cost = beverage_cost + burger_cost + side_cost + dessert_cost
    print(f"Your total cost is ${total_cost}")
    



if __name__ == "__main__":
    GetBeverages()
    GetBurgers()
    GetSides()
    GetDesserts()
    GetUserTotal()
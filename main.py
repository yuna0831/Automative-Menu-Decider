import random

# Define lists for countries and foods
Asian_Country = ["Korean", "Chinese", "Japanese", "Vietnamese"]
Western_Country = ["Italy", "Mexico", "United States", "France"]

Korean_Foods = ["Bulgogi", "Bibimbap", "Tteokbokki", "Japchae", "Samgyeopsal", "Kimchi Jjigae", "Sundubu Jjigae", "Galbi", "Gimbap", "Naengmyeon", "Haemul Pajeon", "Jjajangmyeon", "Samgyetang", "Dakgalbi"]
Chinese_Foods = ["Peking Duck", "Sweet and Sour Pork", "Kung Pao Chicken", "Ma Po Tofu", "Chow Mein", "Spring Rolls", "Dumplings", "Wontons", "Hot Pot", "Fried Rice", "Char Siu", "Eggplant with Garlic Sauce", "Yangzhou Fried Rice", "Hot and Sour Soup", "Scallion Pancakes", "Sesame Chicken", "Mapo Eggplant", "Steamed Buns", "Tea Eggs", "Beef and Broccoli"]
Japanese_Foods = ["Sushi", "Ramen", "Tempura", "Sashimi", "Udon", "Soba", "Okonomiyaki", "Takoyaki", "Miso Soup", "Teriyaki", "Yakitori", "Tonkatsu", "Onigiri", "Katsu Curry", "Shabu-Shabu", "Gyudon", "Tamago Sushi", "Natto", "Mochi", "Chawanmushi"]
Vietnamese_Foods = ["Pho", "Banh Mi", "Spring Rolls", "Bun Cha", "Banh Xeo", "Com Tam", "Bun Bo Hue", "Cao Lau", "Cha Gio", "Mi Quang", "Banh Cuon", "Che", "Xoi", "Goi Ngo Sen", "Hu Tieu", "Ga Nuong", "Ca Kho To", "Canh Chua", "Banh Bao", "Bo La Lot"]
Italian_Foods = ["Pizza", "Pasta", "Risotto", "Tiramisu", "Gelato", "Prosciutto", "Parmigiano-Reggiano", "Bruschetta", "Cannoli", "Lasagna", "Fettuccine Alfredo", "Margherita Pizza", "Panzanella", "Caprese Salad", "Arancini", "Gnocchi", "Carbonara", "Osso Buco", "Ravioli", "Frittata"]
Mexican_Foods = ["Tacos", "Enchiladas", "Guacamole", "Mole", "Churros", "Tamales", "Quesadillas", "Salsa", "Ceviche", "Pozole", "Burritos", "Fajitas", "Elote", "Chilaquiles", "Carnitas", "Sopes", "Tostadas", "Huevos Rancheros", "Nachos", "Agua Fresca"]
US_Foods = ["Burger", "Hot Dog", "Barbecue Ribs", "Macaroni and Cheese", "Apple Pie", "Fried Chicken", "Buffalo Wings", "Clam Chowder", "Cornbread", "Philly Cheesesteak", "Pancakes", "S'mores", "Tacos", "Bagels", "Biscuits and Gravy", "Lobster Roll", "Key Lime Pie", "Chili", "Pulled Pork", "Cheesecake"]
French_Foods = ["Croissant", "Baguette", "Quiche", "Ratatouille", "Coq au Vin", "Bouillabaisse", "Escargots", "Crêpes", "Croque Monsieur", "Ratatouille", "Beef Bourguignon", "Soufflé", "Tarte Tatin", "Macarons", "Madeleines", "Boeuf Bourguignon", "French Onion Soup", "Pâté", "Gougères", "Cassoulet"]

# Function to randomly choose an item from a list
def choice(lst):
    return random.choice(lst)

# Main logic
users = {}

def get_user_profile():
    user_name = input("Enter your name: ")
    if user_name not in users:
        users[user_name] = {"favorites": [], "history": []}
    else:
        print("You are already registered!")
    return user_name

while True:
    user = get_user_profile()
    favorites = users[user]["favorites"]
    history = users[user]["history"]

    choice1 = input("Choose between Asian and Western: ")
    if choice1 == "Asian" or choice1 == "Western":
        choice2 = input("Do you want a randomly picked country? y/n: ")
        
        if choice2 == "y":
            if choice1 == "Asian":
                A_C = choice(Asian_Country)
                Asian_choice = input(A_C + " is the randomly picked country! Press * to continue: ")

                if Asian_choice == "*":
                    if A_C == "Japanese":
                        food = choice(Japanese_Foods)
                    elif A_C == "Vietnamese":
                        food = choice(Vietnamese_Foods)
                    elif A_C == "Korean":
                        food = choice(Korean_Foods)
                    elif A_C == "Chinese":
                        food = choice(Chinese_Foods)
                    
                    print("Your food for today is " + food)
                    history.append(food)

            elif choice1 == "Western":
                W_C = choice(Western_Country)
                Western_choice = input(W_C + " is the randomly picked country! Press * to continue: ")

                if Western_choice == "*":
                    if W_C == "Italy":
                        food = choice(Italian_Foods)
                    elif W_C == "Mexico":
                        food = choice(Mexican_Foods)
                    elif W_C == "United States":
                        food = choice(US_Foods)
                    elif W_C == "France":
                        food = choice(French_Foods)
                    
                    print("Your food for today is " + food)
                    history.append(food)
        
        elif choice2 == "n":
            choice3 = input("Then enter the country: ")

            if choice3 == "Japanese":
                food = choice(Japanese_Foods)
            elif choice3 == "Vietnamese":
                food = choice(Vietnamese_Foods)
            elif choice3 == "Korean":
                food = choice(Korean_Foods)
            elif choice3 == "Chinese":
                food = choice(Chinese_Foods)
            elif choice3 == "Italy":
                food = choice(Italian_Foods)
            elif choice3 == "Mexico":
                food = choice(Mexican_Foods)
            elif choice3 == "United States":
                food = choice(US_Foods)
            elif choice3 == "France":
                food = choice(French_Foods)
            
            print("Your food for today is " + food)
            history.append(food)

    next_step = input("Would you like to (1) save this food to favorites, (2) see history, (3) see favorites, or (4) start over? Enter number: ")
    if next_step == "1":
        favorites.append(food)
        print(food + " has been added to your favorites.")
    elif next_step == "2":
        print("History of foods picked: " + ", ".join(history))
    elif next_step == "3":
        print("Your favorite foods: " + ", ".join(favorites))
    elif next_step == "4":
        continue
    else:
        print("Invalid option. Starting over.")

from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

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

users = {}

def choice(lst):
    return random.choice(lst)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form["username"]
        if user_name not in users:
            users[user_name] = {"favorites": [], "history": []}
        return redirect(url_for("profile", username=user_name))
    return render_template("index.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = users[username]
    if request.method == "POST":
        choice1 = request.form["choice1"]
        choice2 = request.form.get("choice2")
        country = request.form.get("country")

        if choice2 == "y":
            if choice1 == "Asian":
                A_C = choice(Asian_Country)
                food = ""
                if A_C == "Japanese":
                    food = choice(Japanese_Foods)
                elif A_C == "Vietnamese":
                    food = choice(Vietnamese_Foods)
                elif A_C == "Korean":
                    food = choice(Korean_Foods)
                elif A_C == "Chinese":
                    food = choice(Chinese_Foods)
                user["history"].append(food)
                return render_template("profile.html", username=username, country=A_C, food=food, history=user["history"], favorites=user["favorites"])
            elif choice1 == "Western":
                W_C = choice(Western_Country)
                food = ""
                if W_C == "Italy":
                    food = choice(Italian_Foods)
                elif W_C == "Mexico":
                    food = choice(Mexican_Foods)
                elif W_C == "United States":
                    food = choice(US_Foods)
                elif W_C == "France":
                    food = choice(French_Foods)
                user["history"].append(food)
                return render_template("profile.html", username=username, country=W_C, food=food, history=user["history"], favorites=user["favorites"])
        elif choice2 == "n":
            food = ""
            if country == "Japanese":
                food = choice(Japanese_Foods)
            elif country == "Vietnamese":
                food = choice(Vietnamese_Foods)
            elif country == "Korean":
                food = choice(Korean_Foods)
            elif country == "Chinese":
                food = choice(Chinese_Foods)
            elif country == "Italy":
                food = choice(Italian_Foods)
            elif country == "Mexico":
                food = choice(Mexican_Foods)
            elif country == "United States":
                food = choice(US_Foods)
            elif country == "France":
                food = choice(French_Foods)
            user["history"].append(food)
            return render_template("profile.html", username=username, country=country, food=food, history=user["history"], favorites=user["favorites"])
    return render_template("profile.html", username=username, history=user["history"], favorites=user["favorites"])

@app.route("/add_favorite/<username>/<food>")
def add_favorite(username, food):
    user = users[username]
    user["favorites"].append(food)
    return redirect(url_for("profile", username=username))

@app.route("/clear_history/<username>")
def clear_history(username):
    user = users[username]
    user["history"].clear()
    return redirect(url_for("profile", username=username))


if __name__ == '__main__':  
   app.run('0.0.0.0',port=20000,debug=True)
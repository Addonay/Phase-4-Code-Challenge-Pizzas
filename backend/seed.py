from random import randint, choice as rc,sample
from faker import Faker
from app import app
from models import db, Pizza, RestaurantPizza, Restaurant
import random
fake = Faker()

# creates pizza list
pizza_names = [
    "Margherita Pizza",
    "Pepperoni Pizza",
    "Hawaiian Pizza",
    "BBQ Chicken Pizza",
    "Veggie Supreme Pizza",
    "Meat Lovers Pizza",
    "Mushroom and Olive Pizza",
    "Buffalo Chicken Pizza",
    "Four Cheese Pizza",
    "Pesto and Tomato Pizza","Supreme Deluxe Pizza",
    "BBQ Bacon Ranch Pizza",
    "Spinach and Feta Pizza",
    "White Pizza",
    "Mediterranean Pizza",
    "Buffalo Ranch Chicken Pizza",
    "Taco Pizza",
    "Shrimp Scampi Pizza",
    "Philly Cheesesteak Pizza",
    "Caprese Pizza",
    "Alfredo Chicken Pizza",
    "Pesto and Artichoke Pizza",
    "Sausage and Mushroom Pizza",
    "Peking Duck Pizza",
    "Bacon and Egg Breakfast Pizza",
    "Reuben Pizza",
    "Greek Gyro Pizza",
    "Tandoori Chicken Pizza",
    "Kimchi and Pork Belly Pizza",
    "Clam and Garlic Pizza",
    "Cajun Shrimp Pizza",
    "Thai Peanut Chicken Pizza",
    "Smoked Salmon Pizza",
    "Eggplant Parmesan Pizza",
    "Breakfast Burrito Pizza",
    "Chicken Tikka Masala Pizza",
    "Prosciutto and Arugula Pizza",
    "Roast Beef and Horseradish Pizza",
    "Fig and Prosciutto Pizza",
    "Buffalo Cauliflower Pizza",
    "Ratatouille Pizza",
    "Pear and Gorgonzola Pizza",
    "Teriyaki Beef Pizza",
    "Falafel Pizza",
    "Mexican Street Corn Pizza",
    "Chili Dog Pizza",
    "Paella Pizza",
    "Crab Rangoon Pizza",
    "Pulled Pork BBQ Pizza",
    "Lobster and Garlic Butter Pizza"
  ]
# list of pizza ingredients
pizza_ingredients = [
    "Dough",
    "Tomato sauce",
    "Mozzarella cheese",
    "Pepperoni",
    "Bell peppers",
    "Onions",
    "Mushrooms",
    "Olives",
    "Basil",
    "Oregano",
    "Spinach",
    "Feta cheese",
    "Ranch dressing",
    "Alfredo sauce",
    "Artichoke hearts",
    "Italian sausage",
    "Peking duck",
    "Eggs",
    "Swiss cheese",
    "Tandoori sauce",
    "Kimchi",
    "Pork belly",
    "Clams",
    "Cajun spices",
    "Peanut sauce",
    "Smoked salmon",
    "Eggplant",
    "Breakfast burrito ingredients",
    "Tandoori chicken",
    "Prosciutto",
    "Arugula",
    "Roast beef",
    "Horseradish sauce",
    "Figs",
    "Buffalo cauliflower",
    "Ratatouille vegetables",
    "Gorgonzola cheese",
    "Teriyaki sauce",
    "Falafel balls",
    "Mexican street corn toppings",
    "Chili",
    "Hot dogs",
    "Paella ingredients",
    "Cream cheese",
    "Crab meat",
    "Rangoon sauce",
    "Pulled pork",
    "BBQ sauce",
    "Lobster",
    "Garlic butter"
  
]

# delete any existing data
with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    
    db.session.commit()
      
    # Create and add fake restaurants
    restaurants = [
        Restaurant( 
            name = fake.company() ,

            address=fake.address()
        )
        for i in range(10)
    ]
    db.session.add_all(restaurants)  # Use db.session.add_all() to add the list
    db.session.commit()

    # Create and add fake pizzas
    pizzas = [
        Pizza(
            name=pizza_name,
            ingredients=', '.join(sample(pizza_ingredients, 3)) 
        )
        for pizza_name in pizza_names
    ]
    db.session.add_all(pizzas)  # Use db.session.add_all() to add the list
    db.session.commit()

    # Create restaurant-pizza relationships
    restaurant_pizzas = [
        RestaurantPizza(
            pizza_id=random.choice(pizzas).id,
            restaurant_id=random.choice(restaurants).id,
            price=random.randint(1, 30)
        )
        for i in range(10)
    ]
    db.session.add_all(restaurant_pizzas)  # Use db.session.add_all() to add the list
    db.session.commit()
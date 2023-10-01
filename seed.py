from app import db, Restaurant, Pizza

def seed_database():
    # Create some restaurants
    restaurant1 = Restaurant(name='Pizza Palace', address='123 Main St')
    restaurant2 = Restaurant(name='Italian Delight', address='456 Elm St')
    restaurant3 = Restaurant(name='Mamma Mia Pizzeria', address='789 Oak St')

    # Create some pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato, mozzarella, basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, mozzarella, pepperoni')
    pizza3 = Pizza(name='Vegetarian', ingredients='Tomato, mozzarella, veggies')
    pizza4 = Pizza(name='Hawaiian', ingredients='Tomato, mozzarella, ham, pineapple')

    # Add pizzas to restaurants
    restaurant1.pizzas.extend([pizza1, pizza2])
    restaurant2.pizzas.extend([pizza2, pizza3])
    restaurant3.pizzas.extend([pizza3, pizza4])

    # Add data to the database session and commit
    db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, pizza4])
    db.session.commit()

if __name__ == '__main__':
    seed_database()

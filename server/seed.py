from app import app, db
from models import Restaurant, Pizza

if __name__ == '__main__':
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Seed Restaurants
        restaurants_data = [
            {"name": "Dominion Pizza", "address": "Good Italian, Ngong Road, 5th Avenue"},
            {"name": "Pizza Hut", "address": "Westgate Mall, Mwanzi Road, Nrb 100"},
            # Add more restaurants as needed
        ]

        for restaurant_data in restaurants_data:
            restaurant = Restaurant(**restaurant_data)
            db.session.add(restaurant)

        db.session.commit()

        # Seed Pizzas
        pizzas_data = [
            {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
            {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
            # Add more pizzas as needed
        ]

        for pizza_data in pizzas_data:
            pizza = Pizza(**pizza_data)
            db.session.add(pizza)

        db.session.commit()

    print("Data seeding completed.")

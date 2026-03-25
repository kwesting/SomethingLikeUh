favorite_cars = [
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2022,
        "price": 79999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": True,
        "owner": None
    },
    {
        "make": "Porsche",
        "model": "911 Carrera",
        "year": 2023,
        "price": 106500.00,
        "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2022,
        "price": 27995.00,
        "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Chevrolet",
        "model": "Corvette",
        "year": 2023,
        "price": 62995.00,
        "features": ["Supercharged", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "R8",
        "year": 2023,
        "price": 144195.00,
        "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
        "is_electric": False,
        "owner": None
    }
]

def price_finder(cars):

    for car in favorite_cars:
        
        if car["price"] > 100000:
            print(car["make"])
    

price_finder(favorite_cars)
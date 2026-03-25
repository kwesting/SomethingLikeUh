favorite_cars =[

    {
        "make": "BMW",
        "model": "Mini Cooper",
        "year": 2012, #int
        "price": 999999.99, #float
        "features": ["Double sunroof", "fast", "cute", "noisy"], #list
        "is_electric": False,
        "previous_owner": None,
    },
    {
        "make": "Chevrolet",
        "model": None,
        "year": 1955,
        "price": 999.99, #float
        "features": ["big body", "fast", "cute", "noisy", "mauve"], #list
        "is_electric": False,
        "previous_owner": "Bob",

    }
]

if favorite_cars == []:
    print("This list is empty.")
    print("Please add something for me to play with.")
    print("Dumbass")
else:
    print("This is a full af list bro")
    print(favorite_cars[0]["make"] + " " + favorite_cars[0]["model"] )
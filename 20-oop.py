class Car:
    # property of class
    name = "car"

    # property of object
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self.engine = engine

    # method
    def stop(self, reason):
        return "{} is stopping to {}".format(self.brand, reason)

    def run(self):
        return "{} is running on the street".format(self.brand)

    def startEngine(self):
        return "{} is starting the engine".format(self.brand)


# instantiate the Car class
toyota = Car("Toyota", "red", "electric")
lamborghini = Car("Lamborghini", "yellow", "Deisel")
porsche = Car("Porsche", "green", "Gas")

# access the class attributes
print("Porsche is a {}.".format(porsche.__class__.name))
print("Toyota is a {}.".format(toyota.__class__.name))
print("Lamborghini is a {}.".format(lamborghini.__class__.name))

# access the instance attributes
print("{} has {} color, {} engine."
      .format(toyota.brand, toyota.color, toyota.engine))
print("{} has {} color, {} engine."
      .format(lamborghini.brand, lamborghini.color, lamborghini.engine))
print("{} has {} color, {} engine."
      .format(porsche.brand, porsche.color, porsche.engine))

# call our instance methods
print(toyota.stop("fill the gas"))
print(lamborghini.run())
print(porsche.startEngine())

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def call(self, contact):
        print(f"Calling {contact} from {self.model}...")

    def browse(self, website):
        print(f"Browsing {website} on {self.model}.")

    def get_storage(self):
        return f"{self.__storage}GB"

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Invalid storage value!")

# Subclass
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Launching {game} with {self.gpu} GPU on {self.model}!")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 256, "Adreno 730")

# Use methods
phone1.call("Alice")
phone1.browse("www.google.com")
print(phone1.get_storage())

gaming_phone.call("Bob")
gaming_phone.play_game("Call of Duty")

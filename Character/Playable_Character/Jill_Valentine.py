from Character.character import Character
from Items.Weapons.Jills_Samurai_Edge import Jills_Samurai_Edge  # Import the weapon class

class Jill_Valentine(Character):
    def __init__(self):
        # Instantiate the weapon correctly
        starting_weapon = Jills_Samurai_Edge()

        # Call the parent constructor with the correct values
        super().__init__("Jill Valentine", 100, "Fine", starting_weapon, None, None)

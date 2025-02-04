from Character import character
from Items.Weapons import Jills_Samurai_Edge

class Jill_Valentine(character):
    def __init__(self):
        # The arguments taking in the super function are name, health, starting weapon, Special item
        super().__init__("Jill Valentine", 100, Jills_Samurai_Edge, [Jills_Samurai_Edge], None)

    # Planning on adding skills in the future

    
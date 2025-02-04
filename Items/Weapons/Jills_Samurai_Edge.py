#Having a problem where I have to add __init__ to each entity so to the folders Character, Enemies, Items

from .weapon import weapon  # Assuming `Weapon` is a class in `weapon.py`

class Jills_Samurai_Edge:
    def __init__(self):
        super(weapon).__init__("Jill's Samurai Edge", 15, "Handgun Ammo")

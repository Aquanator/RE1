#Having a problem where I have to add __init__ to each entity so to the folders Character, Enemies, Items

from .eapon import Weapon  # Assuming `Weapon` is a class in `weapon.py`

class Jills_Samurai_Edge:
    super(weapon).__init__("Jill's Samurai Edge", 15, "Handgun Ammo")

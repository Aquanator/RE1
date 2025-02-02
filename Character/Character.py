class Character:
    def __init__(self, name, max_health, weapon, special_item):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.health_state = "Fine"
        self.weapon = weapon
        self.inventory = []
        self.special_item = special_item
    
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon}")

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.health_state = "Dead"
            print("YOU HAVE DIED")
        else:
            print(f"{self.name} has taken {damage}")
    
    def attack(self):
        if self.weapon != None:
            print(f"{self.name} fires {self.weapon}")
        else:
            print(f"{self.name} does not have a weapon equipped!")
    
    def heal(self, amount):
        self.current_health += amount

        if(self.current_health > 100):
            self.current_health = 100

        if self.current_health >= 60 and self.current_health <= 100:
            self.health_state = "Fine"

        elif self.current_health <= 59 and self.current_health >= 30:
            self.health_state = "Caution"
        
        elif self.current_health <= 29 and self.current_health >= 15:
            self.health_state = "Extreme Caution"
        
        elif self.current_health <= 14 and self.current_health >= 1:
            self.health_state = "Danger"
            
        print(f"{self.name}: {self.health_state}")
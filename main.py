from Character.Playable_Character import Jill_Valentine
import time

def game_intro():
    """Displays an intro message"""
    print("========================================")
    print("    Welcome to Resident Evil: Escape")
    print("========================================")
    time.sleep(1)
    print("\nYou are Jill Valentine, a former S.T.A.R.S. officer trying to survive a zombie outbreak.")
    time.sleep(1)
    print("\nFind weapons, fight enemies, and escape the city alive!\n")
    time.sleep(1)

def main_game_loop():
    """Main game loop where player interacts with the world"""
    player = Jill_Valentine()  # Initialize Jill
    
    while player.health_state != "Dead":
        print("\n------ What do you want to do? ------")
        print("1. Check Status")
        print("2. Equip Weapon")
        print("3. Take Damage")
        print("4. Heal")
        print("5. Attack")
        print("6. Exit Game")
        
        choice = input("> ").strip()
        
        if choice == "1":
            print(f"\n{player.name} - Health: {player.current_health}/{player.max_health} ({player.health_state})")
            print(f"Weapon: {player.weapon if player.weapon else 'None'}")
        
        elif choice == "2":
            weapon_name = input("Enter weapon name: ").strip()
            player.equip_weapon(weapon_name)
        
        elif choice == "3":
            damage = int(input("Enter damage amount: "))
            player.take_damage(damage)
        
        elif choice == "4":
            heal_amount = int(input("Enter heal amount: "))
            player.heal(heal_amount)
        
        elif choice == "5":
            player.attack()
        
        elif choice == "6":
            print("Exiting the game... Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

    print("\nGame Over.")

if __name__ == "__main__":
    game_intro()
    main_game_loop()

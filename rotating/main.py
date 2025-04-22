# main.py

from pet import Pet

def main():
    pet = Pet("Daisy")  # You named your pet Daisy! 🌼

    pet.get_status()  # Check initial status
    pet.eat()         # Feed Daisy
    pet.sleep()       # Let Daisy sleep
    pet.play()        # Play with Daisy
    pet.train("roll over")  # Teach Daisy a trick
    pet.train("shake paw")  # Teach Daisy another trick
    pet.get_status()  # Check updated status
    pet.show_tricks() # Show Daisy's tricks

if __name__ == "__main__":
    main()

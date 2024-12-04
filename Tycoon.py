import random
import copy

# Player stats
player = {
    "money": 0,
    "pickaxe_dmg": 1,
    "inventory": []
}

# Ores with hp and values:
ores = [ #list of ores
    {"name": "Coal", "hp": 2, "value": 5},
    {"name": "Iron", "hp": 5, "value": 10},
    {"name": "Gold", "hp": 10, "value": 20},
    {"name": "Diamond", "hp": 20, "value": 50}
]

upgrades = [
    {"name": "Increase Pickaxe Damage", "cost": 50, "effect": "dmg", "value": 1},
    {"name": "Increase  Ore Value", "cost": 100, "effect": "value", "value": 1.2},
    {"name": "Better Ore Spawns", "cost": 150, "effect": "spawn", "value": 1.1},
]

# Function to spawn an ore
def spawn_ore():
    ore = random.choice(ores) # Random ore type
    return copy.deepcopy(ore) # Creates a fresh copy of the ore

# Function to mine an ore
def mine_ore(ore):
    print(f"You found a {ore['name']}! HP: {ore['hp']}")
    while ore["hp"] > 0:
        action = input("Press 'm' to mine or 'q' to quit: ").lower()
        if action == "m":
            ore["hp"] -= player["pickaxe_dmg"]
            print(f"Hit! {ore['name']} HP left: {max(0, ore['hp'])}")
        elif action == "q":
            print("You stopped mining.")
            return
    print(f"You mined a {ore['name']} worth {ore['value']} coins!")
    player["inventory"].append(ore)

# Function to sell inventory
def sell_inventory():
    if not player["inventory"]:
        print("Your inventory is empty!")
        return
    total_value = sum(item["value"] for item in player["inventory"])
    player["money"] += total_value
    print(f"You sold your inventory for {total_value} coins!")
    player["inventory"] = []

    # Game Loop
while True:
    print(f"\nMoney: {player['money']}, Pickaxe Damage: {player['pickaxe_dmg']}")
    print("1. Mine Ore\n2. Sell Inventory\n3. Quit")
    choice = input("Choose an action: ").strip()
    
    if choice == "1":
        ore = spawn_ore()
        mine_ore(ore)
    elif choice == "2":
        sell_inventory()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

import random

# Player stats
player = {
    "money": 0,
    "pickaxe_dmg": 1,
    "inventory": []
}

# List of ores and their hp and values. Might have to change later to balance the game.
ores = [
    {"name": "Coal", "hp": 2, "value": 5},
    {"name": "Iron", "hp": 5, "value": 10},
    {"name": "Gold", "hp": 10, "value": 20},
    {"name": "Diamond", "hp": 20, "value": 50},
]

# Function to spawn a random ore from the ores list.
def spawn_ore():
    return random.choice(ores)

def mine_ore(ore):
    print(f"You have found {ore['name']}! HP: {ore['hp']}")
    while ore["hp"] > 0:
        action = input("Press 'm' to mine ore or 'q' to quit: ").lower()
        if action == "m":
            ore["hp"] -= player["pickaxe_dmg"]
            print(f"Hit! {ore['name']} HP left: {max(0, ore['hp'])}")
        elif action == "q":
            print("You stopped mining")
            return
    print(f"You mined a {ore['name']} wort {ore['value']} coins!")
    player["inventory"].append(ore)

# Function to sell inventory
def sell_inventory():
    if not player["inventory"]:
        print("Your inventory is empty!")
        return
    total_value = sum(item['value'] for item in player["inventory"])
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
    elif choice == "2":
        sell_inventory()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. please try again.")

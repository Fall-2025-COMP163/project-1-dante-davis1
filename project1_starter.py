"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Dante Davis
Date: 10/22/2025

AI Usage: AI helped with the structure of file I/O and stat calculation logic
"""

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 10 + (3 * level)
        magic = 2 + (1 * level)
        health = 120 + (10 * level)
    elif character_class == "Mage":
        strength = 3 + (1 * level)
        magic = 12 + (3 * level)
        health = 80 + (5 * level)
    elif character_class == "Rogue":
        strength = 7 + (2 * level)
        magic = 7 + (2 * level)
        health = 70 + (5 * level)
    elif character_class == "Cleric":
        strength = 6 + (2 * level)
        magic = 10 + (3 * level)
        health = 110 + (7 * level)
    else:
        # Default case
        strength = 5
        magic = 5
        health = 100

    return strength, magic, health


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    """
    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def save_character(character, filename):
    """
    Saves character to text file in specific format.
    """
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True


def load_character(filename):
    """
    Loads character from text file.
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
            value = int(value)
        character[key.split()[-1].lower()] = value

    return character


def display_character(character):
    """
    Prints formatted character sheet.
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")


def level_up(character):
    """
    Increases character level and recalculates stats.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50  # Bonus for leveling up


# Main program area (for testing)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    char = create_character("Dante", "Warrior")
    display_character(char)

    save_character(char, "my_character.txt")

    loaded_char = load_character("my_character.txt")
    print("\nLoaded character from file:")
    display_character(loaded_char)

    print("\nAfter Level Up:")
    level_up(loaded_char)
    display_character(loaded_char)


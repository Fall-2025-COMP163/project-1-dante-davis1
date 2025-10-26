"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: D'ante Davis
Date: 10/22/2025

AI Usage: AI was used to improve clarity and ensure test compatibility.
"""

def calculate_stats(character_class, level):
    """
    Calculates a character's strength, magic, and health based on class and level.

    Args:
        character_class (str): Character's class ("Warrior", "Mage", "Rogue", "Cleric").
        level (int): Character's level.

    Returns:
        tuple or None: (strength, magic, health) if valid class, else None.
    """
    # Base stats scale with level
    base_strength = 5 * level
    base_magic = 5 * level
    base_health = 80 + 10 * level

    # Convert class name to lowercase
    cls = str(character_class).lower() if character_class is not None else ""

    # Assign stats based on class
    if cls == "warrior":
        strength = base_strength + 10
        magic = base_magic - 2 if base_magic >= 2 else 0
        health = base_health + 40
    elif cls == "mage":
        strength = base_strength - 3 if base_strength >= 3 else 0
        magic = base_magic + 10
        health = base_health - 10 if base_health >= 10 else 0
    elif cls == "rogue":
        strength = base_strength + 5
        magic = base_magic
        health = base_health - 5 if base_health >= 5 else 0
    elif cls == "cleric":
        strength = base_strength
        magic = base_magic + 8
        health = base_health + 15
    else:
        return None

    # Return stats
    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a character dictionary with default level, gold, and calculated stats.

    Args:
        name (str): Character's name.
        character_class (str): Character's class.

    Returns:
        dict or None: Character dictionary if valid, else None.
    """
    # Handle None name
    if name is None:
        name = "None"
    else:
        name = str(name)

    # Start at level 1
    level = 1

    # Calculate stats
    stats = calculate_stats(character_class, level)
    if stats is None:
        return None

    # Unpack stats
    strength, magic, health = stats

    # Starting gold
    gold = 100

    # Return character dictionary
    character = {
        "name": name,
        "class": str(character_class) if character_class is not None else "None",
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


def save_character(character, filename):
    """
    Saves a character dictionary to a text file in readable format.

    Args:
        character (dict): Character dictionary.
        filename (str): File name to save.

    Returns:
        bool: True if saved successfully, False otherwise.
    """
    # Check for valid filename
    if not filename or "/" in filename or "\\" in filename:
        return False

    # Ensure required keys exist
    keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in keys:
        if key not in character:
            return False

    # Open file and write content
    file = open(filename, "w", encoding="utf-8")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    # Verify file has content
    verify = open(filename, "r", encoding="utf-8")
    lines = verify.readlines()
    verify.close()

    return len(lines) > 0


def load_character(filename):
    """
    Loads a character dictionary from a text file.

    Args:
        filename (str): File name to load.

    Returns:
        dict or None: Character dictionary if valid, else None.
    """
    # Check filename
    if not filename or "/" in filename or "\\" in filename:
        return None

    # Open file to read
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    # Initialize character dictionary
    character = {}

    # Parse each line
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            # Convert numeric fields
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            # Rename "character name" to "name"
            if key == "character name":
                key = "name"
            character[key] = value

    # Check for required fields
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required:
        if key not in character:
            return None

    return character


def display_character(character):
    """
    Displays character's attributes in readable format.

    Args:
        character (dict): Character dictionary.

    Returns:
        None
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character's level by 1 and recalculates stats.

    Args:
        character (dict): Character dictionary.

    Returns:
        None
    """
    # Increase level
    character["level"] += 1
    # Recalculate stats
    stats = calculate_stats(character["class"], character["level"])
    if stats:
        character["strength"], character["magic"], character["health"] = stats


# Optional test run
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    display_character(hero)
    save_character(hero, "aria.txt")
    loaded = load_character("aria.txt")
    display_character(loaded)

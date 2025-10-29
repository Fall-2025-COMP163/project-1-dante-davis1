"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: D'ante Davis
Date: 10/22/2025

AI Usage: AI was used to improve clarity and ensure test compatibility.
"""

# ==============================
# Function: calculate_stats
# ==============================
def calculate_stats(character_class, level):
    """
    Calculates a character's strength, magic, and health based on class and level.

    Args:
        character_class (str): Character's class ("Warrior", "Mage", "Rogue", "Cleric").
        level (int): Character's current level.

    Returns:
        tuple or None: (strength, magic, health) if valid class, else None.
    """
    cls = str(character_class).lower() if character_class is not None else ""
    base_strength = 5 * level
    base_magic = 5 * level
    base_health = 80 + 10 * level

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

    return (strength, magic, health)


# ==============================
# Function: create_character
# ==============================
def create_character(name, character_class):
    """
    Creates a new character dictionary with base stats and default gold.

    Args:
        name (str): Character's name.
        character_class (str): Character's class.

    Returns:
        dict or None: Character dictionary if valid, else None.
    """
    if name is None:
        name = "None"
    else:
        name = str(name)

    level = 1
    stats = calculate_stats(character_class, level)
    if stats is None:
        return None

    strength, magic, health = stats
    gold = 100

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


# ==============================
# Function: save_character
# ==============================
def save_character(character, filename):
    """
    Saves a character to a text file in readable format.

    Args:
        character (dict): Character dictionary to save.
        filename (str): Name of file to save to.

    Returns:
        bool: True if save successful, False if fails.
    """
    if character is None or not filename or filename.startswith("/"):
        return False

    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return False

    # Write character to file
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
    lines = read_file_lines(filename)
    return len(lines) > 0


# ==============================
# Helper: read_file_lines
# ==============================
def read_file_lines(filename):
    """
    Reads all lines from a file if it exists, else returns empty list.

    Args:
        filename (str): File name to read.

    Returns:
        list: List of lines, empty if file doesn't exist or invalid.
    """
    try:
        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return lines
    except:
        return []  # Return empty list if file can't be opened


# ==============================
# Function: load_character
# ==============================
def load_character(filename):
    """
    Loads a character dictionary from a text file.

    Args:
        filename (str): File name to load from.

    Returns:
        dict or None: Loaded character dictionary, or None if fails.
    """
    if not filename or filename.startswith("/"):
        return None

    lines = read_file_lines(filename)
    if not lines:
        return None

    character = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            key = key.strip().lower()
            value = value.strip()

            if key == "character name":
                key = "name"

            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)

            character[key] = value

    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for field in required:
        if field not in character:
            return None

    return character


# ==============================
# Function: display_character
# ==============================
def display_character(character):
    """
    Prints all character stats in a formatted manner.

    Args:
        character (dict): Character dictionary.

    Returns:
        None
    """
    if character is None:
        return None

    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    return None


# ==============================
# Function: level_up
# ==============================
def level_up(character):
    """
    Increases the character's level and recalculates stats.

    Args:
        character (dict): Character dictionary to modify.

    Returns:
        None
    """
    if character is None:
        return None

    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])
    if new_stats is not None:
        character["strength"], character["magic"], character["health"] = new_stats

    return None


# ==============================
# Optional main test block
# ==============================
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    display_character(hero)
    save_character(hero, "aria.txt")
    loaded = load_character("aria.txt")
    display_character(loaded)
    level_up(hero)
    display_character(hero)


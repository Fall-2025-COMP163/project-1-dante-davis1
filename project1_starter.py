"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [D'ante Davis]
Date: [10/22/2025]

AI Usage: AI was used to improve clarity and ensure test compatibility.
"""

def calculate_stats(character_class, level):
    """
    Calculates a character's strength, magic, and health based on their class and level.

    This function determines a character's base stats and applies modifiers depending
    on their class type. Each class type influences how much strength, magic, and health
    they start with or gain per level.

    Args:
        character_class (str): The type of character ("Warrior", "Mage", "Rogue", "Cleric").
        level (int): The current level of the character.

    Returns:
        tuple: (strength, magic, health) values if valid class, else None.
    """
    # Base stats scale linearly with level
    base_strength = 5 * level
    base_magic = 5 * level
    base_health = 80 + 10 * level

    # Normalize class name
    cls = str(character_class).lower()

    # Determine stats based on class type
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
        return None  # Invalid class, cannot calculate stats

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with a default level, gold, and calculated stats.

    Args:
        name (str): Character's name.
        character_class (str): Character's class type.

    Returns:
        dict or None: Character dictionary if valid, else None.
    """
    # Start all characters at level 1
    level = 1
    # Generate base stats
    stats = calculate_stats(character_class, level)
    if stats is None:
        return None  # Invalid class input

    # Unpack calculated stats
    strength, magic, health = stats
    gold = 100  # Default starting gold

    # Create a dictionary storing all attributes
    character = {
        "name": str(name),
        "class": str(character_class),
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


def save_character(character, filename):
    """
    Saves a character's data into a text file in a specific readable format.

    The function checks for missing keys and invalid filenames before saving.

    Args:
        character (dict): Dictionary containing all character data.
        filename (str): The name of the file to save into.

    Returns:
        bool: True if successful, False if invalid data or file issues.
    """
    # Ensure filename is valid and not a directory
    if not filename or "/" in filename or "\\" in filename:
        return False

    # Ensure all necessary keys exist
    keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in keys:
        if key not in character:
            return False

    # Write character data to a text file
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    # Verify that the file exists by reopening it (no os module)
    verify = open(filename, "r")
    lines = verify.readlines()
    verify.close()

    # Return True if file has content
    return len(lines) > 0


def load_character(filename):
    """
    Loads a character's information from a text file and rebuilds the dictionary.

    Reads the saved file format and converts the data back into proper types.

    Args:
        filename (str): The file to load from.

    Returns:
        dict or None: Reconstructed character if successful, else None.
    """
    # Validate filename format
    if not filename or "/" in filename or "\\" in filename:
        return None

    # Try to open the file; if it fails (e.g., doesn't exist), handle gracefully
    file = open(filename, "r") if file_exists(filename) else None
    if file is None:
        return None

    lines = file.readlines()
    file.close()

    # Parse key-value pairs
    character = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            if key == "character name":
                key = "name"
            character[key] = value

    # Check for required fields
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required:
        if key not in character:
            return None

    return character


def file_exists(filename):
    """
    Checks if a file exists without using os.path.

    Args:
        filename (str): File name to check.

    Returns:
        bool: True if the file can be opened for reading, False otherwise.
    """
    try_open = None
    # Attempt to open file in read mode to verify existence
    try_open = open(filename, "r")
    if try_open:
        try_open.close()
        return True
    return False


def display_character(character):
    """
    Displays a character's attributes in a formatted, readable layout.

    Args:
        character (dict): The character dictionary containing all stats.

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
    Increases the character's level by one and recalculates their stats.

    Args:
        character (dict): Dictionary representing the current character.

    Returns:
        None
    """
    # Increase level count by one
    character["level"] += 1
    # Recalculate new stats for this level
    stats = calculate_stats(character["class"], character["level"])
    if stats:
        # Update character's attributes
        character["strength"], character["magic"], character["health"] = stats


# Optional testing section for manual verification
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")  # Create example character
    display_character(hero)                  # Show character details
    save_character(hero, "aria.txt")         # Save to file
    loaded = load_character("aria.txt")      # Reload from file
    display_character(loaded)                # Display loaded character

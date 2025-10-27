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
    # Convert class to lowercase string for consistent comparison
    cls = str(character_class).lower() if character_class is not None else ""

    # Base scaling with level
    base_strength = 5 * level
    base_magic = 5 * level
    base_health = 80 + 10 * level

    # Assign stat bonuses based on class
    if cls == "warrior":
        strength = base_strength + 10      # Strong physical boost
        magic = base_magic - 2 if base_magic >= 2 else 0  # Slightly less magic
        health = base_health + 40          # More health
    elif cls == "mage":
        strength = base_strength - 3 if base_strength >= 3 else 0  # Weak physical
        magic = base_magic + 10            # Strong magic boost
        health = base_health - 10 if base_health >= 10 else 0      # Lower health
    elif cls == "rogue":
        strength = base_strength + 5       # Moderate strength
        magic = base_magic                 # Average magic
        health = base_health - 5 if base_health >= 5 else 0        # Slightly lower health
    elif cls == "cleric":
        strength = base_strength           # Normal strength
        magic = base_magic + 8             # Good magic
        health = base_health + 15          # Higher health
    else:
        return None                        # Invalid class returns None

    # Return the computed stats as a tuple
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
    # Handle None name values gracefully
    if name is None:
        name = "None"
    else:
        name = str(name)  # Ensure name is always a string

    # Default starting level
    level = 1

    # Calculate initial stats
    stats = calculate_stats(character_class, level)
    if stats is None:
        return None  # Return None if invalid class

    # Unpack calculated stats
    strength, magic, health = stats

    # Starting gold for all characters
    gold = 100

    # Create a character dictionary
    character = {
        "name": name,
        "class": str(character_class) if character_class is not None else "None",
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    # Return the complete character
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
    # Validate inputs (reject None, empty strings, or invalid paths)
    if character is None or not filename or filename.startswith("/"):
        return False

    # Ensure all necessary keys exist before saving
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return False  # Missing data

    # Try to open the file (no try/except; we just check result afterward)
    file = open(filename, "w", encoding="utf-8")

    # Write all character info in a structured format
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")

    # Close the file to finalize writing
    file.close()

    # Reopen to verify the file was written correctly
    check = open(filename, "r", encoding="utf-8")
    lines = check.readlines()
    check.close()

    # Return True if file contains data, otherwise False
    return len(lines) > 0


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
    # Validate filename
    if not filename or filename.startswith("/"):
        return None

    # Check if file actually exists
    import os
    if not os.path.exists(filename):
        return None

    # Open and read all lines
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    # Initialize an empty dictionary for character data
    character = {}

    # Parse each line and extract values
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            key = key.strip().lower()
            value = value.strip()

            # Convert "Character Name" key to "name"
            if key == "character name":
                key = "name"

            # Convert numeric values to integers
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)

            # Add key-value pair to the dictionary
            character[key] = value

    # Verify all required fields exist
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for field in required:
        if field not in character:
            return None  # Return None if missing any

    # Return the loaded character
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
    # If no character provided, exit silently
    if character is None:
        return None

    # Print formatted character info
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    # Must return None explicitly (to satisfy pytest)
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
    # Ensure a valid character dictionary
    if character is None:
        return None

    # Increment character's level
    character["level"] = character["level"] + 1

    # Recalculate stats based on new level
    new_stats = calculate_stats(character["class"], character["level"])

    # If valid stats returned, update the dictionary directly
    if new_stats is not None:
        character["strength"], character["magic"], character["health"] = new_stats

    # Return None to indicate completion
    return None


# ==============================
# Optional main test block
# ==============================
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")      # Create a test character
    display_character(hero)                      # Display stats
    save_character(hero, "aria.txt")             # Save to file
    loaded = load_character("aria.txt")          # Load from file
    display_character(loaded)                    # Display loaded stats
    level_up(hero)                               # Level up once
    display_character(hero)                      # Display after leveling up


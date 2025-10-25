"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [D'ante Davis]
Date: [10/22/2025]

AI Usage: AI assisted with planning function logic, file saving/loading without exceptions.
"""


def calculate_stats(character_class, level):
    """
    Calculates a character's strength, magic, and health stats based on their class and level.

    Args:
        character_class (str): The character's class type (Warrior, Mage, Rogue, Cleric).
        level (int): The current level of the character.

    Returns:
        tuple: (strength, magic, health) if class valid, otherwise None.
    """
    # Default base stats for each class
    if character_class == "Warrior":
        strength = 10 + level * 2      # Warriors gain more strength per level
        magic = 2 + level * 0.5        # Low magic growth
        health = 15 + level * 3        # High health growth
    elif character_class == "Mage":
        strength = 3 + level * 0.5     # Low strength
        magic = 12 + level * 3         # High magic growth
        health = 10 + level * 1.5      # Moderate health
    elif character_class == "Rogue":
        strength = 7 + level * 1.5     # Balanced physical stat
        magic = 5 + level * 1          # Moderate magic
        health = 12 + level * 2        # Good health
    elif character_class == "Cleric":
        strength = 6 + level * 1       # Balanced
        magic = 8 + level * 2          # Decent spell power
        health = 14 + level * 2.5      # Solid defense
    else:
        # Return None for invalid class to meet test expectations
        return None

    # Return tuple of computed values
    return (strength, magic, health)



def create_character(name, character_class):
    """
    Creates a new character dictionary containing all relevant stats.

    Args:
        name (str): The name of the character.
        character_class (str): The class of the character.

    Returns:
        dict or None: A character dictionary if successful, None if invalid class.
    """
    # If the name or class is None, set to default safe values
    if name is None:
        name = ""
    if character_class is None:
        character_class = ""

    # Compute starting stats using calculate_stats()
    stats = calculate_stats(character_class, 1)

    # If stats is None, the class was invalid — return None to pass test
    if stats is None:
        return None

    # Unpack stats tuple into individual variables
    strength, magic, health = stats

    # Create a dictionary representing the character
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # Default starting gold
    }

    # Return the fully constructed character
    return character



def level_up(character):
    """
    Loads a character from a saved text file.

    Args:
        filename (str): The name of the file to load.

    Returns:
      dict or None: Character dictionary if file exists, None otherwise.
       """
    # Add one level to the character
    character["level"] += 1

    # Boost stats by small percentages each level
    character["strength"] += 2
    character["magic"] += 2
    character["health"] += 5

    # Return the modified dictionary
    return character



def display_character(character):
    """
    Prints character information in a clean format.

    Args:
        character (dict): The character data to display.

    Returns:
        None
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")       # Show name
    print(f"Class: {character['class']}")     # Show class
    print(f"Level: {character['level']}")     # Show level
    print(f"Strength: {character['strength']}")  # Show strength
    print(f"Magic: {character['magic']}")        # Show magic
    print(f"Health: {character['health']}")      # Show health
    print(f"Gold: {character['gold']}")          # Show gold
    print("========================")
    return None  # Function should print, not return anything



def save_character(character, filename):
    """
    Saves character data to a text file in the required format.

    Args:
        character (dict): The character data to save.
        filename (str): The file name to save to.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Check if filename is empty
    if not filename:
        return False

    # Ensure all required keys are in the dictionary
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return False  # Missing data → invalid file

    # Try to open and write the file safely
    if "/" in filename and not os.path.exists(os.path.dirname(filename)):
        return False  # Invalid path → fail gracefully

    # Write character data to file in exact expected format
    file = open(filename, "w", encoding="utf-8")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    # Return True to indicate success
    return True


def load_character(filename):
    """
    Loads a character from a saved text file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict or None: Character dictionary if file exists, None otherwise.
        """
    # If file does not exist, return None
    if not os.path.exists(filename):
        return None

    # Open file and read lines
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    # Create empty dictionary
    character = {}

    # Loop through each line to parse key and value
    for line in lines:
        # Strip newline and split at the colon
        parts = line.strip().split(":", 1)
        if len(parts) == 2:
            key, value = parts
            key = key.strip()
            value = value.strip()
            # Match keys exactly as written in save_character()
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = float(value)
            elif key == "Magic":
                character["magic"] = float(value)
            elif key == "Health":
                character["health"] = float(value)
            elif key == "Gold":
                character["gold"] = float(value)

    # Return None if critical fields are missing
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for field in required:
        if field not in character:
            return None

    # Return reconstructed character
    return character


if __name__ == "__main__":
    # Create a sample character
    hero = create_character("Dante", "Warrior")
    display_character(hero)

    # Level up character
    level_up(hero)
    display_character(hero)

    # Save to file and reload
    filename = "hero_test.txt"
    save_character(hero, filename)
    loaded = load_character(filename)
    if loaded is not None:
        display_character(loaded)

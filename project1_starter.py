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
    # Base stats scale linearly with level
    base_strength = 5 * level  # Base strength
    base_magic = 5 * level     # Base magic
    base_health = 80 + 10 * level  # Base health

    # Normalize class name to lowercase string
    cls = str(character_class).lower() if character_class is not None else ""

    # Assign stats based on class type
    if cls == "warrior":
        strength = base_strength + 10  # Warriors get extra strength
        magic = base_magic - 2 if base_magic >= 2 else 0  # Slightly reduced magic
        health = base_health + 40  # Extra health
    elif cls == "mage":
        strength = base_strength - 3 if base_strength >= 3 else 0  # Reduced strength
        magic = base_magic + 10  # Boost magic
        health = base_health - 10 if base_health >= 10 else 0  # Slightly reduced health
    elif cls == "rogue":
        strength = base_strength + 5  # Moderate strength boost
        magic = base_magic  # Magic unchanged
        health = base_health - 5 if base_health >= 5 else 0  # Slightly lower health
    elif cls == "cleric":
        strength = base_strength  # Strength unchanged
        magic = base_magic + 8  # Boost magic
        health = base_health + 15  # Boost health
    else:
        return None  # Invalid class

    # Return stats as a tuple
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
        name = "None"  # Default name if None
    else:
        name = str(name)  # Convert to string

    level = 1  # Start all characters at level 1

    stats = calculate_stats(character_class, level)  # Calculate stats
    if stats is None:
        return None  # Invalid class

    # Unpack stats
    strength, magic, health = stats

    gold = 100  # Default starting gold

    # Build the character dictionary
    character = {
        "name": name,
        "class": str(character_class) if character_class is not None else "None",
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character  # Return the character dictionary


def save_character(character, filename):
    """
    Saves a character dictionary to a text file in readable format.

    Args:
        character (dict): Character dictionary.
        filename (str): File name to save.

    Returns:
        bool: True if saved successfully, False otherwise.
    """
    # Validate filename
    if not filename or "/" in filename or "\\" in filename:
        return False  # Invalid filename

    # Ensure all required keys exist
    keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in keys:
        if key not in character:
            return False  # Missing key

    # Open file for writing with UTF-8 encoding
    file = open(filename, "w", encoding="utf-8")

    # Write character attributes line by line
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")

    file.close()  # Close the file

    # Verify that the file has content
    verify = open(filename, "r", encoding="utf-8")
    lines = verify.readlines()
    verify.close()

    return len(lines) > 0  # Return True if file has content


def load_character(filename):
    """
    Loads a character dictionary from a text file.

    Args:
        filename (str): File name to load.

    Returns:
        dict or None: Character dictionary if valid, else None.
    """
    # Validate filename
    if not filename or "/" in filename or "\\" in filename:
        return None  # Invalid filename

    # Open file to read
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()  # Read all lines
    file.close()  # Close the file

    character = {}  # Initialize empty dictionary

    # Parse each line into key/value
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)  # Split on first colon
            key = key.strip().lower()  # Lowercase the key
            value = value.strip()  # Remove whitespace

            # Convert numeric fields to int
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)

            # Map "character name" to "name"
            if key == "character name":
                key = "name"

            character[key] = value  # Store in dictionary

    # Ensure all required fields are present
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required:
        if key not in character:
            return None  # Missing required key

    return character  # Return the character dictionary


def display_character(character):
    """
    Displays character's attributes in readable format.

    Args:
        character (dict): Character dictionary.

    Returns:
        None
    """
    print("=== CHARACTER SHEET ===")  # Header
    print(f"Name: {character['name']}")  # Name
    print(f"Class: {character['class']}")  # Class
    print(f"Level: {character['level']}")  # Level
    print(f"Strength: {character['strength']}")  # Strength
    print(f"Magic: {character['magic']}")  # Magic
    print(f"Health: {character['health']}")  # Health
    print(f"Gold: {character['gold']}")  # Gold


def level_up(character):
    """
    Increases character's level by 1 and recalculates stats.

    Args:
        character (dict): Character dictionary.

    Returns:
        None
    """
    character["level"] += 1  # Increase level by 1

    # Recalculate stats for new level
    stats = calculate_stats(character["class"], character["level"])
    if stats:
        # Update character's strength, magic, and health
        character["strength"], character["magic"], character["health"] = stats


# Optional test run
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")  # Create a test character
    display_character(hero)  # Display the character
    save_character(hero, "aria.txt")  # Save to file
    loaded = load_character("aria.txt")  # Load from file
    display_character(loaded)  # Display loaded character

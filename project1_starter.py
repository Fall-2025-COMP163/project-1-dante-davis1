"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [D'ante Davis]
Date: [10/22/2025]

AI Usage: AI assisted with planning function logic, file saving/loading without exceptions.
"""

# Function to calculate base stats based on class and level
def calculate_stats(character_class, level):
    """
    Calculate stats for a character based on their class and level.
    Returns a tuple of (strength, magic, health).

    Parameters:
    - character_class (str): Class of the character ("Warrior", "Mage", "Rogue", "Cleric")
    - level (int): Current level of the character

    Returns:
    - tuple: (strength, magic, health)
    - None if class is invalid
    """
    if character_class == "Warrior":
        strength = 10 + level * 2
        magic = 2 + level
        health = 15 + level * 5
    elif character_class == "Mage":
        strength = 3 + level
        magic = 12 + level * 3
        health = 10 + level * 3
    elif character_class == "Rogue":
        strength = 7 + level * 2
        magic = 5 + level
        health = 8 + level * 2
    elif character_class == "Cleric":
        strength = 6 + level * 2
        magic = 10 + level * 3
        health = 12 + level * 4
    else:
        return None  # Invalid class
    return (strength, magic, health)


# Function to create a new character
def create_character(name, character_class):
    """
    Create a new character dictionary with initial stats and gold.

    Parameters:
    - name (str): Name of the character
    - character_class (str): Class of the character

    Returns:
    - dict: Character dictionary with stats, level, and gold
    - None if class is invalid
    """
    stats = calculate_stats(character_class, 1)  # Calculate base stats for level 1
    if stats is None:  # Check for invalid class
        return None
    strength, magic, health = stats  # Unpack stats into variables
    # Create the character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character


# Function to save character to a text file
def save_character(character, filename):
    """
    Save the character to a text file in the required format.

    Parameters:
    - character (dict): Character dictionary to save
    - filename (str): Name of the file to save to

    Returns:
    - bool: True if successful, False otherwise
    """
    # Return False if character or filename is invalid
    if character is None or filename == "" or filename is None:
        return False
    # Open the file for writing
    f = open(filename, "w")
    # Write each field in the required format
    f.write(f"Character Name: {character['name']}\n")
    f.write(f"Class: {character['class']}\n")
    f.write(f"Level: {character['level']}\n")
    f.write(f"Strength: {character['strength']}\n")
    f.write(f"Magic: {character['magic']}\n")
    f.write(f"Health: {character['health']}\n")
    f.write(f"Gold: {character['gold']}\n")
    f.close()  # Close the file
    return True


# Function to load character from a text file
def load_character(filename):
    """
    Load a character from a text file saved in the required format.

    Parameters:
    - filename (str): Name of the file to load

    Returns:
    - dict: Character dictionary if successful
    - None if file not found or empty
    """
    # Check if file exists
    try:
        f = open(filename, "r")
    except:
        return None  # Return None if file does not exist

    character = {}  # Initialize empty dictionary
    # Read file line by line
    for line in f:
        line = line.strip()  # Remove whitespace
        if line.startswith("Character Name:"):
            character["name"] = line.split("Character Name:")[1].strip()
        elif line.startswith("Class:"):
            character["class"] = line.split("Class:")[1].strip()
        elif line.startswith("Level:"):
            character["level"] = int(line.split("Level:")[1].strip())
        elif line.startswith("Strength:"):
            character["strength"] = int(line.split("Strength:")[1].strip())
        elif line.startswith("Magic:"):
            character["magic"] = int(line.split("Magic:")[1].strip())
        elif line.startswith("Health:"):
            character["health"] = int(line.split("Health:")[1].strip())
        elif line.startswith("Gold:"):
            character["gold"] = int(line.split("Gold:")[1].strip())
    f.close()  # Close the file
    if len(character) == 0:
        return None
    return character


# Function to display character information
def display_character(character):
    """
    Display character stats in a formatted sheet.

    Parameters:
    - character (dict): Character dictionary to display

    Returns:
    - None
    """
    if character is None:
        return
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# Function to level up a character
def level_up(character):
    """
    Increase character level by 1 and recalculate stats.

    Parameters:
    - character (dict): Character dictionary to level up

    Returns:
    - None
    """
    if character is None:
        return
    character["level"] += 1  # Increase level
    stats = calculate_stats(character["class"], character["level"])  # Recalculate stats
    if stats is not None:
        character["strength"], character["magic"], character["health"] = stats


# Optional main program for testing
if __name__ == "__main__":
    char = create_character("TestHero", "Warrior")  # Create example character
    display_character(char)  # Display stats
    save_character(char, "my_character.txt")  # Save to file
    loaded = load_character("my_character.txt")  # Load from file
    display_character(loaded)  # Display loaded character

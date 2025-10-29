Game Concept:
This RPG world lets players create characters like Warriors, Mages, Rogues, and Clerics. Each class has unique stat scaling for strength, magic, and health. For example, Mages get extra magic but lower health:
elif cls == "mage":
    strength = base_strength - 3 if base_strength >= 3 else 0
    magic = base_magic + 10
    health = base_health - 10 if base_health >= 10 else 0

Design Choices:
Stat formulas scale with level and reflect each class’s role in combat. Warriors are tanky, Mages are fragile but powerful, and Rogues are balanced. This logic is handled in:
base_strength = 5 * level
base_magic = 5 * level
base_health = 80 + 10 * level

Bonus Creative Features:
The code handles missing names or invalid classes gracefully. It also verifies file saves by reopening and checking contents. For example:
check = open(filename, "r", encoding="utf-8")
lines = check.readlines()
return len(lines) > 0

AI Usage:
AI helped improve clarity for testing. It suggested edge case handling like checking for missing keys. This is reflected in:
for key in required_keys:
    if key not in character:
        return False
        
How to Run:
Save the code as character_creator.py and run it with Python. It creates a Mage named Aria, saves her to a file, loads her back, and levels her up. The test block shows this:
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    display_character(hero)
    save_character(hero, "aria.txt")
    loaded = load_character("aria.txt")
    display_character(loaded)
    level_up(hero)
    display_character(hero)



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21180936&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge

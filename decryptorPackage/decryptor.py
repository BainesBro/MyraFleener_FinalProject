# File Name: decryptor.py
# Student Name: Collin Baines, Cole Crooks, Vanshika Rana
# email: bainesct@mail.uc.edu, crookscl@mail.uc.edu, ranava@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/24/2025
# Course #/Section: IS4010-002
# Semester/Year: Spring/2025
# Brief Description of the assignment: This assignment requires us to decrypt files to retrieve a location and movie name, as well as make a sign and take a picture in said location.

# Brief Description of what this module does: This module decrypts UCEnglish.txt using the indexes provided in EncryptedGroupHints Spring 2025.json
# Citations: ChatGPT, Gemini, stackoverflow, *prayer*, https://www.imdb.com/title/tt0091217/quotes/?item=qt3195774

# Anything else that's relevant:

import json

def decrypt_location(hint_file_path: str, english_file_path: str, team_name: str) -> str:
    with open(english_file_path, 'r', encoding='utf-8') as f:
        english_words = [line.strip() for line in f.readlines()]

    with open(hint_file_path, 'r', encoding='utf-8') as f:
        encrypted_data = json.load(f)

    encrypted_indices = encrypted_data.get(team_name)
    if not encrypted_indices:
        raise ValueError(f"No encrypted data found for team: {team_name}")

    # Use exact index — no +1
    decrypted_words = [english_words[int(index)] for index in encrypted_indices]
    return ' '.join(decrypted_words)




# File Name: main.py
# Student Name: Collin Baines
# email: bainesct@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/24/2025
# Course #/Section: IS4010-002
# Semester/Year: Spring/2025
# Brief Description of the assignment: This assignment requires us to decrypt files to retrieve a location and movie name, as well as make a sign and take a picture in said location.

# Brief Description of what this module does: This module calls upon functions made in our additional .py files
# Citations: ChatGPT

# Anything else that's relevant:

from decryptorPackage.decryptor import decrypt_location

def main():
    team_name = "Myra Fleener"
    hint_file = "data/EncryptedGroupHints.json"
    english_file = "data/UCEnglish.txt"

    location = decrypt_location(hint_file, english_file, team_name)
    print(f"Decrypted location for '{team_name}':")
    print(location)

if __name__ == "__main__":
    main()

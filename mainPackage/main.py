# File Name: main.py
# Student Name: Collin Baines, Cole Crooks
# email: bainesct@mail.uc.edu, crookscl@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/24/2025
# Course #/Section: IS4010-002
# Semester/Year: Spring/2025
# Brief Description of the assignment: This assignment requires us to decrypt files to retrieve a location and movie name, as well as make a sign and take a picture in said location.

# Brief Description of what this module does: This module calls upon functions made in our additional .py files
# Citations: ChatGPT, Gemini, stackoverflow, *prayer*

# Anything else that's relevant:

from decryptorPackage.decryptor import decrypt_location
from MovieDecryptionPackage.MovieDecryption import MovieDecryptor
import os

def main():
    # Decrypt the location
    team_name = "Myra Fleener"
    hint_file = "data/EncryptedGroupHints.json"
    english_file = "data/UCEnglish.txt"

    location = decrypt_location(hint_file, english_file, team_name)
    print(f"Decrypted location for '{team_name}':")
    print(location)

    # Decrypt the movie title
    decryption_key_bytes = b"___325px9Qm4Sq1OrAgutpUHzAj49W0J9oHrRVhS2yg="
    decryptor = MovieDecryptor(decryption_key_bytes)

    movie_title = decryptor.decrypt_movie_title()

    if movie_title:
        print(f"The decrypted movie title is: {movie_title}")
    else:
        print("Failed to decrypt the movie title.")

if __name__ == "__main__":
    main()
# File Name: MovieDecryption.py
# Student Name: Cole Crooks
# email: crookscl@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/24/2025
# Course #/Section: IS4010-002
# Semester/Year: Spring/2025
# Brief Description of the assignment: This assignment requires us to decrypt files to retrieve a location and movie name, as well as make a sign and take a picture in said location.

# Brief Description of what this module does: This module decrypts UCEnglish.txt using the indexes provided in EncryptedGroupHints Spring 2025.json
# Citations: ChatGPT, Gemini, stackoverflow, *prayer*

# Anything else that's relevant:

import json
import os
from cryptography.fernet import Fernet

class MovieDecryptor:
    def __init__(self, decryption_key):
        self.key = decryption_key
        self.fernet = Fernet(self.key)
        self.teams_data = self.load_teams_data("TeamsAndEncryptedMessagesForDistribution.json")
        self.team_name = "Myra Fleener"  # Set the target team here

    def load_teams_data(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))  # path to MovieDecryption.py
        data_path = os.path.join(script_dir, "..", "Data", filename)
        full_path = os.path.abspath(data_path)
        print(f"Loading file from: {full_path}")  # optional debug line

        try:
            with open(full_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at '{full_path}'.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{full_path}'.")
            return {}

    def get_encrypted_message(self):
        encrypted_messages = self.teams_data.get(self.team_name)
        if encrypted_messages and len(encrypted_messages) > 0:
            return encrypted_messages[0].encode()  # Encode to bytes for Fernet
        else:
            print(f"Error: Encrypted message not found for team '{self.team_name}'.")
            return None

    def decrypt_movie_title(self):
        encrypted_message = self.get_encrypted_message()
        if encrypted_message:
            try:
                decrypted_message = self.fernet.decrypt(encrypted_message)
                return decrypted_message.decode()
            except Exception as e:
                print(f"Decryption error: {e}")
                return None
        return None

if __name__ == "__main__":
    # This block is for testing the MovieDecryptor class directly
    # It will only run if you execute MovieDecryption.py

    # Replace with your actual key
    test_key = b"___325px9Qm4Sq1OrAgutpUHzAj49W0J9oHrRVhS2yg="

    # When running MovieDecryption.py directly, it's in the MovieDecryptionPackage
    # The data folder is one level up, then in the data folder.
    test_file_path = os.path.join("..", "data", "TeamsAndEncryptedMessagesForDistribution.json")
    decryptor = MovieDecryptor(test_key) # The path is now handled inside __init__
    movie = decryptor.decrypt_movie_title()

    if movie:
        print(f"Decrypted movie title (from MovieDecryption.py): {movie}")
    else:
        print("Decryption failed (from MovieDecryption.py).")
import re
import os
import random
import string

class PasswordAnalyzer:
    def __init__(self, common_passwords_file="common_passwords.txt"):
        self.common_passwords_file = common_passwords_file
        self.common_passwords = self._load_common_passwords()

    def _load_common_passwords(self):
        """Loads common weak passwords from a file if it exists."""
        # Default fallback list if file is missing
        fallback = ["password", "123456", "qwerty", "admin", "welcome", "abc123"]
        
        if os.path.exists(self.common_passwords_file):
            try:
                with open(self.common_passwords_file, "r") as f:
                    # Read lines and strip whitespace
                    passwords = [line.strip().lower() for line in f if line.strip()]
                    return list(set(passwords + fallback))
            except Exception:
                return fallback
        return fallback

    def suggest_password(self, length=12):
        """Generates a strong random password."""
        if length < 8: length = 8
        
        # Ensure at least one of each required type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*(),.?\":{}|<>")
        ]
        
        # Fill the rest with random characters
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
        password += [random.choice(all_chars) for _ in range(length - 4)]
        
        # Shuffle to avoid predictable pattern
        random.shuffle(password)
        return "".join(password)

    def analyze(self, password):
        """
        Analyzes the password and returns a dictionary with:
        - score: 0-100
        - label: Very Weak, Weak, Medium, Strong
        - color: Hex color code
        - suggestions: List of improvement tips
        """
        score = 0
        suggestions = []
        
        # 1. Check if it's a common weak password
        if password.lower() in self.common_passwords:
            return {
                "score": 10,
                "label": "Very Weak",
                "color": "#f44336",  # Red
                "suggestions": ["This is a common, easily guessable password. Please choose something unique."]
            }

        # 2. Length Check (Max 25 points)
        length = len(password)
        if length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        else:
            suggestions.append("Increase password length (minimum 8 characters).")

        # 3. Uppercase Check (15 points)
        if re.search(r"[A-Z]", password):
            score += 15
        else:
            suggestions.append("Add uppercase letters.")

        # 4. Lowercase Check (15 points)
        if re.search(r"[a-z]", password):
            score += 15
        else:
            suggestions.append("Add lowercase letters.")

        # 5. Numbers Check (20 points)
        if re.search(r"\d", password):
            score += 20
        else:
            suggestions.append("Add numbers.")

        # 6. Special Characters Check (25 points)
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 25
        else:
            suggestions.append("Add special characters (e.g., !, @, #, $, %).")

        # Determine Label and Color based on score
        if score >= 80:
            label = "Strong"
            color = "#4CAF50"  # Green
        elif score >= 60:
            label = "Medium"
            color = "#FFEB3B"  # Yellow (using a slightly darker yellow for visibility)
        elif score >= 40:
            label = "Weak"
            color = "#FF9800"  # Orange
        else:
            label = "Very Weak"
            color = "#f44336"  # Red

        # Ensure yellow is readable on white background
        if color == "#FFEB3B":
            color = "#FBC02D" # Darker yellow/Gold

        return {
            "score": score,
            "label": label,
            "color": color,
            "suggestions": suggestions
        }

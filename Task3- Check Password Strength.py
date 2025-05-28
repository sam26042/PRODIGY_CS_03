import tkinter as tk
from tkinter import font

class PasswordStrengthCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.custom_font = font.Font(family="Segoe UI", size=12)
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Password Complexity Checker",
                               font=self.title_font, bg="#1e1e2f", fg="#00d8ff")
        title_label.pack(pady=(20, 15))

        self.password_var = tk.StringVar()
        self.password_var.trace_add("write", self.check_password_strength)

        password_frame = tk.Frame(self.root, bg="#2a2a3d")
        password_frame.pack(padx=40, fill=tk.X)

        password_label = tk.Label(password_frame, text="Enter Password:", font=self.custom_font,
                                  bg="#2a2a3d", fg="white")
        password_label.pack(anchor="w", pady=(0,5))

        self.pass_entry = tk.Entry(password_frame, textvariable=self.password_var, show='*',
                                   font=self.custom_font, bg="#45455a", fg="white", insertbackground="white",
                                   relief=tk.FLAT)
        self.pass_entry.pack(fill=tk.X, ipady=8, padx=5)
        self.pass_entry.focus_set()

        self.strength_label = tk.Label(self.root, text="", font=self.custom_font,
                                       bg="#1e1e2f", fg="white")
        self.strength_label.pack(pady=(15,5))

        criteria_frame = tk.Frame(self.root, bg="#1e1e2f")
        criteria_frame.pack(pady=10, fill=tk.X, padx=40)

        self.criteria = {
            "length": tk.Label(criteria_frame, text="✔ At least 8 characters", font=self.custom_font, bg="#1e1e2f", fg="#666"),
            "uppercase": tk.Label(criteria_frame, text="✔ Contains uppercase letter", font=self.custom_font, bg="#1e1e2f", fg="#666"),
            "lowercase": tk.Label(criteria_frame, text="✔ Contains lowercase letter", font=self.custom_font, bg="#1e1e2f", fg="#666"),
            "digit": tk.Label(criteria_frame, text="✔ Contains number", font=self.custom_font, bg="#1e1e2f", fg="#666"),
            "special": tk.Label(criteria_frame, text="✔ Contains special character", font=self.custom_font, bg="#1e1e2f", fg="#666"),
        }

        for label in self.criteria.values():
            label.pack(anchor="w", pady=3)

        # Show initial prompt
        self.update_strength_label('')

    def check_password_strength(self, *args):
        pwd = self.password_var.get()
        length = len(pwd)
        uppercase = any(c.isupper() for c in pwd)
        lowercase = any(c.islower() for c in pwd)
        digit = any(c.isdigit() for c in pwd)
        special = any(not c.isalnum() for c in pwd)

        # Update criteria labels colors
        self.update_criteria_label("length", length >= 8)
        self.update_criteria_label("uppercase", uppercase)
        self.update_criteria_label("lowercase", lowercase)
        self.update_criteria_label("digit", digit)
        self.update_criteria_label("special", special)

        # Compute strength score
        score = sum([length >= 8, uppercase, lowercase, digit, special])

        if score == 0:
            strength_text = ""
            color = "#666"
        elif score <= 2:
            strength_text = "Weak"
            color = "#ff4d4d"  # red
        elif score == 3:
            strength_text = "Medium"
            color = "#ffa500"  # orange
        elif score == 4:
            strength_text = "Strong"
            color = "#9acd32"  # yellowgreen
        else:
            strength_text = "Very Strong"
            color = "#00e676"  # green

        self.update_strength_label(strength_text, color)

    def update_criteria_label(self, key, passed):
        label = self.criteria[key]
        if passed:
            label.config(fg="#00e676", text = label.cget("text").replace("✔", "✔"))
        else:
            label.config(fg="#666", text = label.cget("text").replace("✔", "✘"))

    def update_strength_label(self, text, color="#666"):
        self.strength_label.config(text=f"Password Strength: {text}" if text else "", fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthCheckerApp(root)
    root.mainloop()

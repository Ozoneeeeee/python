import sys
import traceback

# Immediate error catching for startup
try:
    import tkinter as tk
    from tkinter import messagebox
    from analyzer import PasswordAnalyzer
except ImportError as e:
    print("\n" + "="*50)
    print("CRITICAL IMPORT ERROR:")
    print(f"Could not find a required module: {e}")
    print("="*50 + "\n")
    # If on Windows and tkinter is missing, it's usually a Python install issue
    if "tkinter" in str(e):
        print("TIP: Reinstall Python and check 'tcl/tk and IDLE' during setup.")
    sys.exit(1)
except Exception as e:
    print("\n" + "="*50)
    print("UNEXPECTED STARTUP ERROR:")
    traceback.print_exc()
    print("="*50 + "\n")
    sys.exit(1)

class PasswordAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Security Analyzer")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Initialize the analyzer logic
        try:
            self.analyzer = PasswordAnalyzer()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize analyzer: {e}")
            sys.exit(1)

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        """Sets up the GUI components."""
        # Title Label
        title_label = tk.Label(self.root, text="Password Security Analyzer", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

        # Password Entry Frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(entry_frame, text="Enter Password:", font=("Helvetica", 10)).pack(anchor="w")
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(entry_frame, textvariable=self.password_var, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5, fill="x")

        # Show/Hide Password Checkbox
        self.show_pass_var = tk.BooleanVar(value=False)
        self.show_pass_check = tk.Checkbutton(
            entry_frame, text="Show Password", variable=self.show_pass_var, command=self.toggle_password
        )
        self.show_pass_check.pack(anchor="w")

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.analyze_btn = tk.Button(
            btn_frame, text="Analyze Password", command=self.on_analyze, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=10
        )
        self.analyze_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = tk.Button(
            btn_frame, text="Clear", command=self.on_clear, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"), padx=10
        )
        self.clear_btn.grid(row=0, column=1, padx=10)

        self.suggest_btn = tk.Button(
            btn_frame, text="Suggest Password", command=self.on_suggest, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), padx=10
        )
        self.suggest_btn.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # Strength Indicator Frame
        self.result_frame = tk.LabelFrame(self.root, text="Analysis Results", font=("Helvetica", 10, "bold"), padx=10, pady=10)
        self.result_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Strength Label
        self.strength_label = tk.Label(self.result_frame, text="Strength: N/A", font=("Helvetica", 12, "bold"))
        self.strength_label.pack(pady=5)

        # Score Label
        self.score_label = tk.Label(self.result_frame, text="Score: 0/100", font=("Helvetica", 10))
        self.score_label.pack(pady=5)

        # Strength Color Bar (Canvas)
        self.canvas = tk.Canvas(self.result_frame, width=300, height=20, bg="#e0e0e0", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.progress_bar = self.canvas.create_rectangle(0, 0, 0, 20, fill="red")

        # Suggestions Label
        tk.Label(self.result_frame, text="Suggestions:", font=("Helvetica", 10, "underline")).pack(anchor="w")
        self.suggestions_text = tk.Label(self.result_frame, text="", justify="left", font=("Helvetica", 9), wraplength=400)
        self.suggestions_text.pack(pady=5, anchor="w")

    def toggle_password(self):
        """Toggles password visibility."""
        if self.show_pass_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def update_strength_bar(self, score, color):
        """Updates the visual strength indicator."""
        width = (score / 100) * 300
        self.canvas.coords(self.progress_bar, 0, 0, width, 20)
        self.canvas.itemconfig(self.progress_bar, fill=color)

    def on_analyze(self):
        """Handles the Analyze button click."""
        password = self.password_var.get()
        
        if not password:
            messagebox.showwarning("Empty Input", "Please enter a password to analyze.")
            return

        # Get analysis from the analyzer logic
        results = self.analyzer.analyze(password)

        # Update UI with results
        self.strength_label.config(text=f"Strength: {results['label']}", fg=results['color'])
        self.score_label.config(text=f"Score: {results['score']}/100")
        self.update_strength_bar(results['score'], results['color'])
        
        suggestions = "\n".join([f"• {s}" for s in results['suggestions']]) if results['suggestions'] else "None (Great job!)"
        self.suggestions_text.config(text=suggestions)

    def on_suggest(self):
        """Handles the Suggest Password button click."""
        new_password = self.analyzer.suggest_password()
        self.password_var.set(new_password)
        # Automatically analyze the suggested password
        self.on_analyze()
        messagebox.showinfo("Password Suggested", f"A strong password has been generated:\n\n{new_password}\n\nIt has been automatically entered and analyzed for you.")

    def on_clear(self):
        """Clears all fields and results."""
        self.password_var.set("")
        self.strength_label.config(text="Strength: N/A", fg="black")
        self.score_label.config(text="Score: 0/100")
        self.update_strength_bar(0, "#e0e0e0")
        self.suggestions_text.config(text="")
        if self.show_pass_var.get():
            self.show_pass_var.set(False)
            self.toggle_password()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PasswordAnalyzerGUI(root)
        root.mainloop()
    except Exception:
        traceback.print_exc()
        input("\nPress Enter to exit...")

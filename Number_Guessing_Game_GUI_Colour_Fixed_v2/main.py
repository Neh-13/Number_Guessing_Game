import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("620x570")
        self.root.minsize(520, 500)
        self.root.configure(bg="#101827")

        self.secret_number = None
        self.attempts = 0
        self.max_number = 100

        self.show_home()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, color="#5148D8"):
        # A Label styled as a button ensures background/text colours display
        # consistently on macOS, Windows, and Linux Tkinter.
        button = tk.Label(
            parent,
            text=text,
            font=("Arial", 12, "bold"),
            bg=color,
            fg="#FFFFFF",
            padx=18,
            pady=12,
            cursor="hand2",
            relief="flat",
            bd=0
        )
        button.bind("<Button-1>", lambda event: command())
        button.bind("<Enter>", lambda event: button.config(bg="#3930B8" if color == "#5148D8" else "#267E61" if color == "#2E9D78" else "#465A76"))
        button.bind("<Leave>", lambda event: button.config(bg=color))
        button.bind("<Return>", lambda event: command())
        button.bind("<space>", lambda event: command())
        button.config(takefocus=True)
        return button

    def show_home(self):
        self.clear_screen()

        container = tk.Frame(self.root, bg="#101827")
        container.pack(expand=True, fill="both", padx=30, pady=25)

        tk.Label(container, text="🎯", font=("Arial", 48), bg="#101827", fg="white").pack(pady=(10, 5))
        tk.Label(container, text="NUMBER GUESSING", font=("Arial", 25, "bold"),
                 bg="#101827", fg="white").pack()
        tk.Label(container, text="GAME", font=("Arial", 25, "bold"),
                 bg="#101827", fg="#8B85FF").pack(pady=(0, 12))
        tk.Label(container, text="Can you find the secret number?", font=("Arial", 12),
                 bg="#101827", fg="#B8C2D6").pack(pady=(0, 24))

        card = tk.Frame(container, bg="#1B2638", padx=22, pady=18)
        card.pack(fill="x", pady=(0, 22))
        tk.Label(card, text="HOW TO PLAY", font=("Arial", 12, "bold"),
                 bg="#1B2638", fg="#AFAAFF").pack(anchor="w", pady=(0, 8))
        for line in [
            "• The computer picks a number from 1 to 100.",
            "• Enter your guess and press Guess.",
            "• Follow the hints: Too low or Too high.",
            "• Find the number in as few tries as you can!"
        ]:
            tk.Label(card, text=line, font=("Arial", 10), bg="#1B2638",
                     fg="#E4E9F2", anchor="w", justify="left").pack(fill="x", pady=3)

        self.make_button(container, "▶   START GAME", self.start_game, "#5148D8").pack(fill="x", pady=(0, 10))
        exit_button = tk.Label(container, text="Exit", font=("Arial", 10, "bold"),
                               bg="#101827", fg="#D0D7E5", cursor="hand2")
        exit_button.pack()
        exit_button.bind("<Button-1>", lambda event: self.root.destroy())

    def start_game(self):
        self.secret_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.show_game()

    def show_game(self):
        self.clear_screen()

        top = tk.Frame(self.root, bg="#101827")
        top.pack(fill="x", padx=26, pady=(22, 8))
        home_top = tk.Label(top, text="← Home", font=("Arial", 10, "bold"),
                            bg="#344258", fg="#FFFFFF", activebackground="#465A76",
                            padx=12, pady=7, cursor="hand2")
        home_top.pack(side="left")
        home_top.bind("<Button-1>", lambda event: self.show_home())
        home_top.bind("<Enter>", lambda event: home_top.config(bg="#465A76"))
        home_top.bind("<Leave>", lambda event: home_top.config(bg="#344258"))

        tk.Label(top, text="NUMBER GUESSING GAME", font=("Arial", 15, "bold"),
                 bg="#101827", fg="white").pack(side="right")

        tk.Label(self.root, text="I'm thinking of a number between 1 and 100",
                 font=("Arial", 12), bg="#101827", fg="#B8C2D6").pack(pady=(20, 12))

        card = tk.Frame(self.root, bg="#1B2638", padx=25, pady=25)
        card.pack(fill="x", padx=30, pady=10)

        tk.Label(card, text="YOUR GUESS", font=("Arial", 10, "bold"),
                 bg="#1B2638", fg="#AFAAFF").pack()
        self.guess_entry = tk.Entry(card, font=("Arial", 22, "bold"), justify="center",
                                    bg="#F4F6FB", fg="#101827", relief="flat",
                                    width=12, insertbackground="#101827")
        self.guess_entry.pack(pady=12, ipady=8)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.make_button(card, "GUESS", self.check_guess, "#5148D8").pack(fill="x", pady=(0, 12))

        self.feedback = tk.Label(card, text="Make your first guess!", font=("Arial", 12, "bold"),
                                 bg="#1B2638", fg="#E4E9F2")
        self.feedback.pack(pady=5)
        self.attempts_label = tk.Label(card, text="Attempts: 0", font=("Arial", 10),
                                       bg="#1B2638", fg="#B8C2D6")
        self.attempts_label.pack(pady=(8, 0))

        bottom = tk.Frame(self.root, bg="#101827")
        bottom.pack(fill="x", padx=30, pady=12)
        self.make_button(bottom, "↻   NEW GAME", self.start_game, "#2E9D78").pack(side="left", expand=True, fill="x", padx=(0, 6))
        self.make_button(bottom, "HOME", self.show_home, "#344258").pack(side="left", expand=True, fill="x", padx=(6, 0))

        self.guess_entry.focus_set()

    def check_guess(self):
        raw = self.guess_entry.get().strip()
        try:
            guess = int(raw)
        except ValueError:
            self.feedback.config(text="Please enter a whole number.", fg="#FFB86B")
            self.guess_entry.focus_set()
            return

        if not 1 <= guess <= self.max_number:
            self.feedback.config(text="Enter a number from 1 to 100.", fg="#FFB86B")
            self.guess_entry.focus_set()
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.feedback.config(text="⬆ Too low! Try a bigger number.", fg="#FFB86B")
        elif guess > self.secret_number:
            self.feedback.config(text="⬇ Too high! Try a smaller number.", fg="#FFB86B")
        else:
            self.feedback.config(text=f"🎉 Correct! It was {self.secret_number}.", fg="#66E3A4")
            self.guess_entry.config(state="disabled")
            messagebox.showinfo("You won!", f"Great job!\nYou found the number in {self.attempts} attempts.")
            self.make_button(self.root, "PLAY AGAIN", self.start_game, "#2E9D78").pack(pady=6)

        self.guess_entry.delete(0, tk.END)
        if self.guess_entry["state"] != "disabled":
            self.guess_entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

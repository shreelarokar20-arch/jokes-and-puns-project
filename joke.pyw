import tkinter as tk
from tkinter import scrolledtext
import random
import time
import threading

# Lists of jokes and puns (feel free to add more!)
jokes = [
    ("Why don't skeletons fight each other?", "They don't have the guts."),
    ("What do you call fake spaghetti?", "An impasta."),
    ("Why couldn't the bicycle stand up by itself?", "It was two-tired."),
    ("What do you call cheese that isn't yours?", "Nacho cheese!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
    ("How does a penguin build its house?", "Igloos it together."),
    ("What do you call a bear with no teeth?", "A gummy bear."),
    ("Why don't eggs tell jokes?", "They'd crack each other up."),
    ("I'm afraid for the calendar.", "Its days are numbered."),
    ("What did one wall say to the other?", "I'll meet you at the corner!"),
]

puns = [
    "I’m reading a book on anti-gravity. It's impossible to put down!",
    "Time flies like an arrow. Fruit flies like a banana.",
    "I used to be a baker, but I couldn't make enough dough.",
    "Acupuncture is a jab well done.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm on a seafood diet. I see food and I eat it.",
    "Velcro... what a rip-off!",
    "I'm terrified of elevators, so I'm taking steps to avoid them.",
    "I know a lot of jokes about retired people, but none of them work.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
]

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("😂 Ultimate Joke & Pun Machine 😂")
        self.root.geometry("650x750")
        self.root.configure(bg="#e8f4f8")
        self.root.resizable(False, False)

        # Center the window on screen
        self.root.eval('tk::PlaceWindow . center')

        # Title
        title = tk.Label(root, text="🎤 Joke & Pun Machine 🎤", font=("Comic Sans MS", 28, "bold"),
                         bg="#e8f4f8", fg="#ff6b6b")
        title.pack(pady=30)

        # Joke display area
        self.display = scrolledtext.ScrolledText(root, width=65, height=22, font=("Helvetica", 13),
                                                bg="#ffffff", fg="#2c3e50", wrap=tk.WORD,
                                                relief=tk.SUNKEN, bd=8, padx=15, pady=15)
        self.display.pack(padx=30, pady=10)
        self.display.insert(tk.END, "👋 Hey there! Ready for some laughs?\n\nClick the button below to get a joke or pun!\n\n")
        self.display.config(state=tk.DISABLED)

        # Big funny button
        self.joke_btn = tk.Button(root, text="🤡 TELL ME A JOKE OR PUN! 🤡", font=("Helvetica", 18, "bold"),
                                  bg="#ff9f43", fg="white", activebackground="#ee5a24",
                                  activeforeground="white", relief=tk.RAISED, bd=10,
                                  command=self.tell_joke_or_pun, width=30, height=2,
                                  cursor="hand2")
        self.joke_btn.pack(pady=30)

        # Rating section
        rating_frame = tk.Frame(root, bg="#e8f4f8")
        rating_frame.pack(pady=10)

        tk.Label(rating_frame, text="How funny was that? Rate it:", font=("Helvetica", 14),
                 bg="#e8f4f8", fg="#34495e").pack()

        rate_btn_frame = tk.Frame(rating_frame, bg="#e8f4f8")
        rate_btn_frame.pack(pady=10)

        for i in range(1, 6):
            btn = tk.Button(rate_btn_frame, text=f"{i} ⭐", font=("Helvetica", 14), width=5, height=2,
                            bg="#f1c40f", fg="white", relief=tk.RAISED,
                            command=lambda x=i: self.react_to_rating(x))
            btn.grid(row=0, column=i-1, padx=8)

        # Footer
        footer = tk.Label(root, text="Made with ❤️ and terrible puns • Double-click to close",
                          font=("Helvetica", 10), bg="#e8f4f8", fg="#95a5a6")
        footer.pack(side=tk.BOTTOM, pady=20)

        # Configure text tags
        self.display.tag_configure("punchline", font=("Helvetica", 16, "bold"), foreground="#e74c3c", justify="center")
        self.display.tag_configure("pun", font=("Helvetica", 15, "italic"), foreground="#9b59b6", justify="center")
        self.display.tag_configure("setup", foreground="#2980b9", font=("Helvetica", 14))

    def add_to_display(self, text, tag=None):
        self.display.config(state=tk.NORMAL)
        self.display.insert(tk.END, text + "\n\n")
        if tag:
            start = self.display.index("end-2l linestart")
            end = self.display.index("end-1c")
            self.display.tag_add(tag, start, end)
        self.display.config(state=tk.DISABLED)
        self.display.see(tk.END)

    def tell_joke_or_pun(self):
        self.joke_btn.config(state=tk.DISABLED, text="🤔 Brewing a good one...")
        self.root.update()

        threading.Thread(target=self._deliver_content, daemon=True).start()

    def _deliver_content(self):
        time.sleep(1.8)

        if random.random() < 0.65:  # More chances for full jokes
            setup, punchline = random.choice(jokes)
            self.root.after(0, self.add_to_display, f"🤔 {setup}", "setup")
            time.sleep(2.8)
            self.root.after(0, self.add_to_display, f"🥁 {punchline.upper()} 🥁", "punchline")
        else:
            pun = random.choice(puns)
            self.root.after(0, self.add_to_display, f"💡 {pun}", "pun")

        self.root.after(0, lambda: self.joke_btn.config(state=tk.NORMAL,
                                                        text="🤡 TELL ME A JOKE OR PUN! 🤡"))

    def react_to_rating(self, rating):
        reactions = {
            5: "🎉 YES! I'm basically a stand-up comedian now! 🎉",
            4: "😄 Awesome! My ego thanks you!",
            3: "😐 Fair enough... I'll try harder next time.",
            2: "😢 That stings a little... but okay.",
            1: "💔 My heart is shattered. I need therapy. 😭"
        }
        reaction = reactions[rating]
        self.add_to_display(f"You gave it {rating} ⭐ → {reaction}")

# Run the app (only GUI window will appear!)
if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
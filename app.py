import tkinter as tk
from Quizgenerator import get_response, bot_name

BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = ("Helvetica", 14)
FONT_BOLD = ("Helvetica", 14, "bold")

class ChatApplication:
    def __init__(self):
        self.window = tk.Tk()
        self._setup_main_window()

    def run(self):
        print("Launching GUI...")
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title(f"{bot_name} Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=600, bg=BG_COLOR)

        self.text_widget = tk.Text(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                                   font=FONT, padx=10, pady=10, wrap=tk.WORD)
        self.text_widget.place(relheight=0.75, relwidth=1, rely=0)
        self.text_widget.configure(state=tk.DISABLED)

        self.msg_entry = tk.Entry(self.window, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, rely=0.85, relheight=0.06, relx=0.011)
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = tk.Button(self.window, text="Send", font=FONT_BOLD,
                                width=20, bg="#ABB2B9", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.85, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, tk.END)
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.insert(tk.END, f"{sender}: {msg}\n")

        response = get_response(msg)
        self.text_widget.insert(tk.END, f"{bot_name}: {response}\n\n")
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.see(tk.END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()

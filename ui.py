import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue") 

class CalculatorView:
    def __init__(self, action_callback):
        self.root = ctk.CTk()
        
        # root properties
        self.display_var = ctk.StringVar(value="")
        self.action_callback = action_callback

        self.root.bind('<Key>', self.handle_keyboard)
        self.setupUI()

    def setupUI(self):
        # Window
        self.root.title("Calculator")
        self.root.geometry("350x500")

        # Auto resize
        for i in range(6): self.root.grid_rowconfigure(i, weight=1)
        for i in range(4): self.root.grid_columnconfigure(i, weight=1)

        # Screen
        self.screen = ctk.CTkEntry(
            self.root, 
            textvariable=self.display_var,
            font=("Consolas", 30),
            justify="right",
            height=75,
            state="disabled",
        )
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Buttons
        buttons = [
            'C', '⌫', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '^', '0', '.', '='
        ]
        row_val, col_val = 1, 0

        for button in buttons:
            btn = ctk.CTkButton(
                self.root,
                text=button,
                font=("Consolas", 20),
                command=lambda b=button: self.action_callback(b),
                width=50, 
                height=50
            )
            btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def handle_keyboard(self, event):
        char, keysym = event.char, event.keysym

        if keysym == 'Return': self.action_callback('=')
        elif keysym == 'Escape': self.action_callback('C')
        elif keysym == 'BackSpace' or keysym == "KP_Enter": self.action_callback('⌫')
        elif char in [str(x) for x in range(10)] + ['+', '-', '*', '/', '%', '^', '.']: self.action_callback(char)

    def update_screen(self, text: str):
        self.display_var.set(text)

    def run(self):
        self.root.mainloop()
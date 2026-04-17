import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue") 

class View:
    def __init__(self, action_callback):
        self.root = ctk.CTk()
        
        # root properties
        self.display_var = ctk.StringVar(value="")
        self.action_callback = action_callback
        self.setupUI()

    def setupUI(self):
        # Window
        self.root.title("Calculator")
        self.root.geometry("300x400")

        # Auto resize
        for i in range(5): self.root.grid_rowconfigure(i, weight=1)
        for i in range(4): self.root.grid_columnconfigure(i, weight=1)

        # Screen
        self.screen = ctk.CTkEntry(
            self.root, 
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            height=50
        )
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        row_val, col_val = 1, 0

        for button in buttons:
            btn = ctk.CTkButton(
                self.root,
                text=button,
                command=lambda x=button: self.action_callback(x),
                width=50, 
                height=50)
            btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def update_screen(self, text: str):
        self.display_var.set(text)

    def run(self):
        self.root.mainloop()
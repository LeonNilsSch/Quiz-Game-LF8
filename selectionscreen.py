import tkinter as tk

# Function to handle button click (you can modify the actions as needed)
def choose_mode(mode):
    print(f"Selected Mode: {mode}")
    # Here, you can proceed with the next screen or action based on mode

# Function to open the selection screen after login
def open_selection_screen():
    selection_screen = tk.Tk()
    selection_screen.title("Choose Your Mode")
    selection_screen.geometry("800x600")
    selection_screen.configure(bg="#1e1e1e")

    # Styling
    label_font = ("Arial", 16, "bold")
    btn_font = ("Arial", 80, "bold")  # Emojis bleiben groß
    btn_bg = "#00BFFF"
    btn_fg = "black"
    description_font = ("Arial", 12, "normal")

    # Title Label
    title_label = tk.Label(selection_screen, text="Choose Your Mode", font=label_font, fg="white", bg="#1e1e1e")
    title_label.pack(pady=20)

    # Frame to hold both buttons and descriptions (center the content)
    frame = tk.Frame(selection_screen, bg="#1e1e1e")
    frame.pack(expand=True)  # Allow the frame to expand and center its content

    # Single Player Button and Description (smaller button size)
    single_player_btn = tk.Button(frame, text="🧑‍💻", font=btn_font, bg=btn_bg, fg=btn_fg, width=4, height=2, command=lambda: choose_mode("Single Player"), relief="solid", bd=2)
    single_player_btn.grid(row=0, column=0, padx=10, pady=10)

    single_player_desc = tk.Label(frame, text="Singleplayer", font=description_font, fg="white", bg="#1e1e1e")
    single_player_desc.grid(row=1, column=0)

    # Multiplayer Button and Description (smaller button size)
    multiplayer_btn = tk.Button(frame, text="👾", font=btn_font, bg=btn_bg, fg=btn_fg, width=4, height=2, command=lambda: choose_mode("Multiplayer"), relief="solid", bd=2)
    multiplayer_btn.grid(row=0, column=1, padx=10, pady=10)

    multiplayer_desc = tk.Label(frame, text="Multiplayer", font=description_font, fg="white", bg="#1e1e1e")
    multiplayer_desc.grid(row=1, column=1)

    selection_screen.mainloop()
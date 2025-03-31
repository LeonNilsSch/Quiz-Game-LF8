import tkinter as tk

def difficulty_screen():
    # Neues Fenster für die Schwierigkeitseinstellung
    root = tk.Tk()
    root.title("Wähle die Schwierigkeit")
    root.geometry("600x400")  # Fenstergröße angepasst für kompakteres Design
    root.configure(bg="#2e2e2e")  # Hintergrundfarbe angepasst

    # Styling
    label_font = ("Helvetica", 16, "bold")  # Moderne Schriftart
    btn_font = ("Helvetica", 14, "bold")  # Moderne Schriftart für die Buttons
    btn_bg = "#6e6e6e"  # Schöne grüne Buttonfarbe
    btn_fg = "#FFFFFF"  # Weißer Text
    btn_hover_bg = "#1e1e1e"  # Button Hover-Effekt für grün
    btn_border_width = 0  # Kein Rand um die Buttons

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Schwierigkeit-Auswahl Label
    tk.Label(frame, text="Wählen Sie die Schwierigkeit", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

    # Button-Style anpassen und Buttons für Schwierigkeit hinzufügen
    def on_enter(event, button):
        button.config(bg=btn_hover_bg)

    def on_leave(event, button):
        button.config(bg=btn_bg)

    btn_easy = tk.Button(frame, text="Leicht", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_easy.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_easy.bind("<Enter>", lambda event, button=btn_easy: on_enter(event, button))
    btn_easy.bind("<Leave>", lambda event, button=btn_easy: on_leave(event, button))

    btn_medium = tk.Button(frame, text="Mittel", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_medium.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_medium.bind("<Enter>", lambda event, button=btn_medium: on_enter(event, button))
    btn_medium.bind("<Leave>", lambda event, button=btn_medium: on_leave(event, button))

    btn_hard = tk.Button(frame, text="Schwer", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_hard.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_hard.bind("<Enter>", lambda event, button=btn_hard: on_enter(event, button))
    btn_hard.bind("<Leave>", lambda event, button=btn_hard: on_leave(event, button))

    root.mainloop()

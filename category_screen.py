import tkinter as tk

def category_screen():
    # Neues Fenster für die Schwierigkeitseinstellung
    root = tk.Tk()
    root.title("Wähle die Kategorie")
    root.geometry("1360x768")  # Fenstergröße angepasst für kompakteres Design
    root.configure(bg="#2e2e2e")  # Hintergrundfarbe angepasst

    # Styling
    # Styling
    label_font = ("Helvetica", 16, "bold")  # Moderne Schriftart
    entry_bg = "#3A3A3A"  # Mittelgrau für das Eingabefeld
    entry_fg = "#FFFFFF"  # Weißer Text für bessere Lesbarkeit
    btn_font = ("Helvetica", 14, "bold")  # Button-Schriftart
    btn_bg = "#444444"  # Dunkleres Grau für bessere Lesbarkeit
    btn_fg = "#DDDDDD"  # Hellgrau für bessere Lesbarkeit
    btn_hover_bg = "#555555"  # Leicht helleres Grau für Hover
    btn_border_width = 2  # Dünner Rahmen für moderne Optik
    btn_border_color = "#666666"  # Noch dunkler für Rahmen


    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Schwierigkeit-Auswahl Label
    tk.Label(frame, text="Wählen sie ihre Kategorie aus", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

    # Button-Style anpassen und Buttons für Schwierigkeit hinzufügen
    def on_enter(event, button):
        button.config(bg=btn_hover_bg)

    def on_leave(event, button):
        button.config(bg=btn_bg)

    btn_easy = tk.Button(frame, text="Politik", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_easy.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_easy.bind("<Enter>", lambda event, button=btn_easy: on_enter(event, button))
    btn_easy.bind("<Leave>", lambda event, button=btn_easy: on_leave(event, button))

    btn_medium = tk.Button(frame, text="Geographie", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_medium.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_medium.bind("<Enter>", lambda event, button=btn_medium: on_enter(event, button))
    btn_medium.bind("<Leave>", lambda event, button=btn_medium: on_leave(event, button))

    btn_hard = tk.Button(frame, text="General Knowledge", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_hard.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_hard.bind("<Enter>", lambda event, button=btn_hard: on_enter(event, button))
    btn_hard.bind("<Leave>", lambda event, button=btn_hard: on_leave(event, button))

    btn_hard = tk.Button(frame, text="Film/Kino", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_hard.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_hard.bind("<Enter>", lambda event, button=btn_hard: on_enter(event, button))
    btn_hard.bind("<Leave>", lambda event, button=btn_hard: on_leave(event, button))

    btn_hard = tk.Button(frame, text="Videospiele", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_hard.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_hard.bind("<Enter>", lambda event, button=btn_hard: on_enter(event, button))
    btn_hard.bind("<Leave>", lambda event, button=btn_hard: on_leave(event, button))

    btn_hard = tk.Button(frame, text="Anime/Manga", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width)
    btn_hard.pack(pady=15, ipadx=10, ipady=10, fill="x")
    btn_hard.bind("<Enter>", lambda event, button=btn_hard: on_enter(event, button))
    btn_hard.bind("<Leave>", lambda event, button=btn_hard: on_leave(event, button))


    root.mainloop()

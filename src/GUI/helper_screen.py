import tkinter as tk


def helper_screen():
    # Hauptfenster erstellen
    root = tk.Tk()
    root.title("Hilfestellungen")
    root.geometry("1200x800")
    root.configure(bg="#2e2e2e")  # Hintergrundfarbe

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")
    text_font = ("Helvetica", 14)
    btn_font = ("Helvetica", 14, "bold")
    btn_bg = "#444444"  # Dunkleres Grau für Buttons
    btn_fg = "#DDDDDD"  # Hellgrauer Text

    # Titel
    tk.Label(
        root,
        text="Hilfestellungen für das Quiz-Spiel",
        font=label_font,
        fg="white",
        bg="#2e2e2e",
    ).pack(pady=20)

    # Hilfetext
    help_text = """
    Willkommen zum Quiz-Spiel! Hier sind einige Tipps und Anweisungen, um dir zu helfen:

    1. Ziel des Spiels:
       - Beantworte so viele Fragen wie möglich korrekt, um Punkte zu sammeln.
       - Jede Frage hat eine bestimmte Schwierigkeit (leicht, mittel, schwer), die die Punkte beeinflusst.

    2. Steuerung:
       - Wähle die richtige Antwort aus den vier Optionen aus.
       - Du kannst die Enter-Taste drücken, um dich einzuloggen.
       - Du kannst den Key "h" drücken um die Hilfestellungen zu öffnen.

    3. Zeitlimit:
       - Jede Frage hat ein Zeitlimit von 60 Sekunden. Beantworte die Frage, bevor die Zeit abläuft.

    4. Kategorien:
       - Wähle eine Kategorie aus, um Fragen zu einem bestimmten Thema zu beantworten.
       - Beispiele für Kategorien: Geografie, Videospiele, Allgemeinwissen.

    5. Punkte:
       - Für jede richtige Antwort erhältst du Punkte basierend auf der Schwierigkeit der Frage.
       - Falsche Antworten geben keine Punkte.

    6. Spiel beenden:
       - Du kannst das Spiel jederzeit über den "Spiel beenden"-Button oben rechts beenden.

    Viel Erfolg und hab Spaß beim Spielen!
    """

    tk.Label(
        root,
        text=help_text,
        font=text_font,
        fg="white",
        bg="#2e2e2e",
        justify="left",
        wraplength=1000,
    ).pack(pady=20)

    # Zurück-Button
    tk.Button(
        root,
        text="Zurück zum Hauptmenü",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=root.destroy,  # Schließt den Hilfebildschirm
    ).pack(pady=20, ipadx=20, ipady=10)

    root.mainloop()


if __name__ == "__main__":
    helper_screen()
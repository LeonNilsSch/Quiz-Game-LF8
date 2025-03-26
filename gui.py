import tkinter as tk
from tkinter import ttk 

class QuizGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("schlechtes Quiz Game")
        self.geometry ("800x600")

        self.category_frame = ttk.Frame(self)
        self.question_frame = ttk.Frame(self)
        self.result_frame = ttk.Frame(self)

        self.steup_category_selection()

        def setup_category_selection(self):
            pass

    def show_question(self, question):
        pass

    def show_resuts(self,score): 
        pass 
# importiert nötige Bibliotheken
import tkinter as tk
from tkinter import messagebox
from random import sample
from typing import Optional
from hello import *
# Anleitung für das Spiel in der Konsole ausdrucken
hello()

# Erstellt ein Class für die ganzen Game definitions etc.
class Game:
  # Variablen festelgen/definieren
    def __init__(self: object):
        self.canvas = tk.Canvas(win, bg='black', width=310, height=500)
        self.canvas.grid(rowspan=8, columnspan=5)
        self.row = 1
        self.column = 1
        self.colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'grey']
        self.pattern = sample(self.colours, 5)
        self.guessCoordinates = [10, 440, 60, 490]
        self.incorrectCoordinates = [10, 440, 60, 490]
        self.check = -1
        self.guess = []
        self.guesses = []
        self.choice = None
        self.nmb = 0
        for i in range(len(self.colours)):
            self.button = tk.Button(frame, bg=self.colours[i], width=6, height=3, bd=4, command=lambda colour=self.colours[i]: self.AddGuess(colour, self.guessCoordinates))# Lambda funtion as callback function, gibt ausgewählt Farbe an AddGuess weiter => erstellt dann das Oval
            self.button.grid(row=1, column=i, padx=(0, 4), pady=(0, 4))
        return
# wird aufgerufen, wenn der Spieler eine Farbe auswählt. Diese Methode erstellt eine ovale Form auf dem Canvas an den angegebenen Koordinaten und fügt die Farbe, die der Spieler ausgewählt hat, hinzu
    def AddGuess(self: object, colour: str, coordinates: list):
        if coordinates[1] + 60 and coordinates[3] == 70:
          return
        #https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_oval.html
        self.choice = self.canvas.create_oval(coordinates, outline='black', fill=colour, tags=colour)
        self.guesses.append(self.canvas.gettags(self.choice)[0])
        self.UpdateCoordinates(coordinates)
# aktualisiert die Koordinaten der ovale Form, die der Spieler hinzufügt, um dafür zu sorgen, dass die nächste ovale Form in der richtigen Position platziert wird
    def UpdateCoordinates(self: object, Coordinates: list) -> Optional[list]:
        if Coordinates[0] + 60 and Coordinates[2] == 300:
            Coordinates[0] = 10
            Coordinates[2] = 60
            Coordinates[1] -= 60
            Coordinates[3] -= 60
            self.CheckGuess()
            return None
        else:
            Coordinates[0] = Coordinates[0] + 60
            Coordinates[2] = Coordinates[2] + 60
        return Coordinates

# überprüft, ob der Spieler das richtige Muster geraten hat.
    def CheckGuess(self: object):
        self.nmb += 1
        self.check += 1
        if self.guesses == self.pattern:
            tk.messagebox._show('WIN', 'You found the correct order')
            self.guess = []
            return
        elif self.nmb == 7:
          tk.messagebox._show("Lost", "You used all your guesses")
          print(self.pattern)
          return
          
        else:
            for i in range(len(self.guesses)):
                if self.guesses[i] != self.pattern[i]:
                    self.ShowCorrectGuesses(i, self.check)
            self.guesses = []
        print("Dein Versuch:")
        print(self.nmb)
# Wenn man die Folge nicht richtig hat, wird diese Funktion aufgerufen
    def ShowCorrectGuesses(self: object, position: int, row: int):
        coordinates = [10, 440, 60, 490]
        Position = position * 60
        Row = row * 60
        coordinates[0] = coordinates[0] + Position
        coordinates[1] = coordinates[1] - Row
        coordinates[2] = coordinates[2] + Position
        coordinates[3] = coordinates[3] - Row
        self.choice = self.canvas.create_oval(coordinates, outline='black', fill='white')

if __name__ == '__main__':
    win = tk.Tk()
    win.title('Mastermind Game')
    label = tk.Label(text='Mastermind Game', font=("Helvetica", 18))
    frame = tk.Frame(win)
    mastermind = Game()
    label.grid(row=1, columnspan=5)
    frame.grid(row=10, columnspan=5)
    win.mainloop()
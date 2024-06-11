import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter.messagebox import showinfo

Main = tk.Tk()
Main.title("My first programm") #Titel des Main Fensters
Main.geometry("1090x800+400+100") #Größe des Fensters und abstand zu Bildschirmrand
Main.resizable(False, False) #Fenstergröße nicht Anpassbar

#Text
App1 = tk.Label(Main, text='Calculator',bg='red',fg='white')
App2 = tk.Label(Main,text='Guess a number',bg='green', fg='white')
Exit = tk.Label(Main, text='Exit',bg='blue', fg='white')

App1.pack(side=tk.TOP, expand=True, ipadx=20, ipady=20, fill=tk.X)
App2.pack(side=tk.TOP, expand=True, ipadx=20, ipady=20, fill=tk.X)
Exit.pack(side=tk.TOP, expand=True, ipadx=20, ipady=20, fill=tk.X)

def calculator ():
    global first_Number
    global second_Number

    sub = tk.Toplevel(Main) #Neues Fenster
    sub.title("Calculator")
    sub.geometry("400x300+125+125")

    #Textbereiche für die Eingaben
    operator = tk.StringVar()
    first_Number = tk.StringVar()
    second_Number = tk.StringVar()

    text_operator = ttk.Label(sub, text="What basic operator do you want to use? (+, -, *, /)")
    text_operator.pack(side="top")
    textbox = ttk.Entry(sub, textvariable=operator)
    textbox.pack(side="top")

    text_first_number = ttk.Label(sub, text="What is the first number?")
    text_first_number.pack(side="top")
    textbox = ttk.Entry(sub, textvariable=first_Number)
    textbox.pack(side="top")

    text_second_number = ttk.Label(sub, text="What is the second number?")
    text_second_number.pack(side="top")
    textbox = ttk.Entry(sub, textvariable=second_Number)
    textbox.pack(side="top")

    
    def calculate_clicked():#Funktion des Knopfes
        global operator_string
        #stringVar -> string -> float integer
        first_Number_string = first_Number.get()
        first_Number_int = int(float(first_Number_string))

        second_Number_string = second_Number.get()
        second_Number_int = int(float(second_Number_string))

        operator_string = operator.get()

        #Pfad aufgrund der Entscheidung des Benutzers
        if operator_string == "+":
            Ergebnis = first_Number_int + second_Number_int
            msg = first_Number_int, operator_string, second_Number_int, "=", Ergebnis
            showinfo(title='Calculation', message=msg)
        
        elif operator_string == "-":
            Ergebnis = first_Number_int - second_Number_int
            msg = first_Number_int, operator_string, second_Number_int, "=", Ergebnis
            showinfo(title='Calculation', message=msg)
        
        elif operator_string == "*":
            Ergebnis = first_Number_int * second_Number_int
            msg = first_Number_int, operator_string, second_Number_int, "=", Ergebnis
            showinfo(title='Calculation', message=msg)

        elif operator_string == "/":
            if second_Number_int == 0:
                msg = "You cant divide with Zero"
                showinfo(title='Calculation', message=msg)

            else:
                Ergebnis = first_Number_int / second_Number_int
                msg = first_Number_int, operator_string, second_Number_int, "=", Ergebnis
                showinfo(title='Calculation', message=msg)

        else:
            msg = "Please give a valid operator (+, -, *, /)"
            showinfo(title='Calculation', message=msg)

    calculate_button = ttk.Button(sub, text="Calculate", command=calculate_clicked) #Knopf zum ausrechnen
    calculate_button.pack(expand=True, pady=10, padx=10)    

    def Exit_button_clicked():  #Knopf zum Schließen des Programmes
        Main.quit() 
    Exit_button = tk.Button(sub, text="Exit", command=Exit_button_clicked)
    Exit_button.pack(ipadx=15, ipady=15, after=calculate_button)


def guess_a_number():
    import random #Important. We can use random because of this

    def guess(x):
        random_number = random.randint(1, x) #Getting a random_number within a threshold
        guess = 0 #Set Border for random_number

        while guess != random_number: #loop
            guess = int(input (f"Guess a number between 1 and {x}\n")) #Getting the users guess
            if guess < random_number:
                print("Sorry, your guess is too low")
            elif guess > random_number:
                print('Sorry, your guess is too high')
        print(f'Your guess is right. The Number was {random_number}')

    guess(10) #Setting border for the highest number possible

#Knöpfe
def App1_button_clicked(): 
    calculator() 
App1_button = tk.Button(Main, text="Start", command=App1_button_clicked)
App1_button.pack(ipadx=15, ipady=15,  expand=True, after=App1)

def App2_button_clicked(): 
    guess_a_number()
App2_button = tk.Button(Main, text="Start", command=App2_button_clicked)
App2_button.pack(ipadx=15, ipady=15,  expand=True, after=App2)

def Exit_button_clicked():  #Knopf zum Schließen des Programmes
    Main.quit() 
Exit_button = tk.Button(Main, text="Exit", command=Exit_button_clicked)
Exit_button.pack(ipadx=15, ipady=15,  expand=True, after=Exit)

Main.mainloop() #keep window open

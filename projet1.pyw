#imports
from cgitb import text
from tkinter import *
from tkinter import ttk
import random
import string

######################################################################## 
#Window setup ici parce que je sais pas commment le mettre dans une fction
window = Tk()
window.title("Password Gen")
window.configure(background="#E6E8E6")
window.resizable(False, False)
window.geometry("420x250")

######################################################################## 

#Return mdp en fonction de la longuer et des checkbuttons activés
def Password():
    #variables remises à 0 pour chaque nouvel appel 
    password = 0
    a = 0
    b = 0
    c = 0
    d = 0
    lgth = 0
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    lgth = longueur.get()
    all=""
    a = cbMaj.get()
    b = cbMin.get()
    c = cbNb.get()
    d = cbSym.get()
    
    #on checke qu'on ait bien choisi au moins une checkbox
    if(a == 0 and b == 0 and c == 0 and d == 0):
        password = "Choix de caractères invalide, modifier la selection."
        return password
    #Si y'en a au moins de checké alors vamos
    if(a== 1):
        all = all + upper 
    if(b == 1):
        all = all + lower
    if(c == 1):
        all = all + num
    if(d == 1):
        all = all + symbols
    
    temp = random.sample(all, lgth)
    password = "".join(temp)
    return password
        
######################################################################## 
#Clicker: on appelle password et on met le password ans une entry en bas 
def clicker():
    pwd = Password()
    output = Entry(window, width=50)
    lblVideC= Label(window, text="", bg="#E6E8E6").grid(row=8, column=0)
    length = 16
    for i in range (length):
        output.delete(i)
    output.grid(row=9, column=0, columnspan=4)
    output.insert(0,pwd)
    
########################################################################
#Variables (les lblVide\[*] servent a gerer la grille d'affichage)
cbMaj = IntVar()
cbMin = IntVar()
cbNb = IntVar()
cbSym = IntVar()
longueur = IntVar()

#Titre
txtT = Label(window, text="PASSWORD GENERATOR V1", bg="#E6E8E6", fg="#3F403F", font=("Impact", 20, "bold"), anchor="center").grid(row = 0, column = 0, columnspan = 4)
lblVideTa =  Label(window, text="", bg="#E6E8E6").grid(row=1, column=0) #VIDE

#Checkbuttons   
cb1 = Checkbutton(window, variable=cbMaj ,text="Majuscules", bg="#E6E8E6", fg="#3F403F").grid(row=2,column=0, padx=10)
cb2 = Checkbutton(window, variable=cbMin ,text="Minuscules", bg="#E6E8E6", fg="#3F403F").grid(row=2,column=1)
cb3 = Checkbutton(window, variable=cbNb ,text="Chiffres", bg="#E6E8E6", fg="#3F403F").grid(row=2,column=2)
cb4 = Checkbutton(window, variable=cbSym ,text="Symboles", bg="#E6E8E6", fg="#3F403F").grid(row=2,column=3)

#Spinbox length
lblVideT = Label(window, text="", bg="#E6E8E6").grid(row=3, column=4)#VIDE
txtL = Label(window, text="    Longueur du mot de passe: ", width = 25, bg="#E6E8E6", fg="#3F403F").grid(row =5, column = 0, columnspan=2)
spin = Spinbox(window, textvariable = longueur, from_=1, to=16, bg="white", fg="#3F403F").grid(row=5, column = 2)

#Valider
lblVideB= Label(window, text="", bg="#E6E8E6").grid(row=6, column=0)#VIDE
btn1 = Button(window, text="VALIDER", bg="#E6E8E6", fg="#3F403F", command= clicker).grid(row=7, column=1, columnspan=2)


window.mainloop()


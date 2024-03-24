from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def bloquear():
    for i in range(0,9):
        listabotones[i].config(state="disabled")
def iniciarj():
    for i in range(0,9):
        listabotones[i].config(state="normal")
        listabotones[i].config(bg="lightgray")
        listabotones[i].config(text="")
        t[i] = "N"
    global nombrejugador1,nombrejugador2
    nombrejugador1=simpledialog.askstring("Jugador","Escribe el nombre del jugador 1: ")
    nombrejugador2=simpledialog.askstring("Jugador","Escribe el nombre del jugador 2: ")
    turnojugador.set("Turno : " +nombrejugador1)
    
  
def cambiar(num):
    global turno,nombrejugador1,nombrejugador2
    if t[num]=="N" and turno==0:
        listabotones[num].config(text="x")
        listabotones[num].config(bg="white")
        t[num] = "X"
        turno = 1
        turnojugador.set("Turno : " + nombrejugador2)
    elif t[num]=="N" and turno==1:
        listabotones[num].config(text="O")
        listabotones[num].config(bg="lightblue")
        t[num] = "O"
        turno = 0
        turnojugador.set("Turno : " + nombrejugador1)
    listabotones[num].config(state="disabled")  
    verificar()
    
def verificar():
    if (t[0] == "X" and t[1] == "X" and t[2] == "X") or \
       (t[3] == "X" and t[4] == "X" and t[5] == "X") or \
       (t[6] == "X" and t[7] == "X" and t[8] == "X") or \
       (t[0] == "X" and t[3] == "X" and t[6] == "X") or \
       (t[1] == "X" and t[4] == "X" and t[7] == "X") or \
       (t[2] == "X" and t[5] == "X" and t[8] == "X") or \
       (t[0] == "X" and t[4] == "X" and t[8] == "X") or \
       (t[2] == "X" and t[4] == "X" and t[6] == "X"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste Jugador " + nombrejugador1)
    elif (t[0] == "O" and t[1] == "O" and t[2] == "O") or \
         (t[3] == "O" and t[4] == "O" and t[5] == "O") or \
         (t[6] == "O" and t[7] == "O" and t[8] == "O") or \
         (t[0] == "O" and t[3] == "O" and t[6] == "O") or \
         (t[1] == "O" and t[4] == "O" and t[7] == "O") or \
         (t[2] == "O" and t[5] == "O" and t[8] == "O") or \
         (t[0] == "O" and t[4] == "O" and t[8] == "O") or \
         (t[2] == "O" and t[4] == "O" and t[6] == "O"):
        bloquear()
        messagebox.showinfo("Ganador", "Ganaste Jugador " + nombrejugador2)
    elif all(element != "N" for element in t):
        bloquear()
        messagebox.showinfo("Empate", "¡Ha habido un empate!")
ventana = Tk()
ventana.geometry("400x500")
ventana.title("Juego triki")
turno = 0
nombrejugador1 = ""
nombrejugador2 = ""
listabotones = []
t = [] # X O N
turnojugador = StringVar()  
for i in range(0,9):
    t.append("N")
#crear cada boton
boton0 = Button(ventana,width=9,height=3,command=lambda: cambiar(0))
listabotones.append(boton0)
boton0.place(x=50,y=50)
boton1 = Button(ventana,width=9,height=3,command=lambda: cambiar(1))
listabotones.append(boton1)
boton1.place(x=150,y=50)
boton2 = Button(ventana,width=9,height=3,command=lambda: cambiar(2))
listabotones.append(boton2)
boton2.place(x=250,y=50)
boton3 = Button(ventana,width=9,height=3,command=lambda: cambiar(3))
listabotones.append(boton3)
boton3.place(x=50,y=150)
boton4 = Button(ventana,width=9,height=3,command=lambda: cambiar(4))
listabotones.append(boton4)
boton4.place(x=150,y=150)
boton5 = Button(ventana,width=9,height=3,command=lambda: cambiar(5))
listabotones.append(boton5)
boton5.place(x=250,y=150)
boton6 = Button(ventana,width=9,height=3,command=lambda: cambiar(6))
listabotones.append(boton6)
boton6.place(x=50,y=250)
boton7 = Button(ventana,width=9,height=3,command=lambda: cambiar(7))
listabotones.append(boton7)
boton7.place(x=150,y=250)
boton8 = Button(ventana,width=9,height=3,command=lambda: cambiar(8))
listabotones.append(boton8)
boton8.place(x=250,y=250)
turnoE = Label(ventana,textvariable=turnojugador).place(x=120,y=20)
iniciar = Button(ventana,bg='blue',fg='green',text='Iniciar Juego',width=15,height=3, command=iniciarj).place(x=130,y=350)  
bloquear()
ventana.mainloop()
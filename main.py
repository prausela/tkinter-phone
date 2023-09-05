from tkinter import *

interface = Tk()
interface.config(width=690, height=265, bg="white")
interface.title("440: Un Softphone Diferente")

def dial(number):
    global current_number
    global number_label
    if current_number is None:
        current_number = ""
    current_number += str(number)
    number_label.config(text=current_number)


def save_contact():
    global current_number
    global agenda_values
    global agenda
    global name_entry
    if current_number is not None:
        contact_name = name_entry.get()
        contact_name = contact_name.strip()
        if contact_name not in agenda_values and contact_name != "":
            agenda_values[contact_name] = current_number
            agenda.insert(len(agenda_values), contact_name)

def on_select(evt):
    global agenda_values
    global number_label
    global current_number
    w = evt.widget
    curr_sel = w.curselection()
    if curr_sel is not None and len(curr_sel) >= 1:
        index = int(curr_sel[0])
        value = w.get(index)
        current_number = agenda_values[value]
        number_label.config(text=str(current_number))

def hang_up():
    global current_number
    global number_label
    current_number = None
    number_label.config(text="Ingrese número")
    enable()

def call():
    global current_number
    global number_label
    current_number = None
    number_label.config(text="Llamando")
    disable()

def disable():
    global asterisk_button
    global zero_button
    global hashtag_button
    global seven_button
    global eight_button
    global nine_button
    global four_button
    global five_button
    global six_button
    global one_button
    global two_button
    global three_button
    global call_button
    global save_button
    global agenda

    asterisk_button.config(command=lambda : ())
    zero_button.config(command=lambda : ())
    hashtag_button.config(command=lambda : ())

    seven_button.config(command=lambda : ())
    eight_button.config(command=lambda : ())
    nine_button.config(command=lambda : ())

    four_button.config(command=lambda : ())
    five_button.config(command=lambda : ())
    six_button.config(command=lambda : ())

    one_button.config(command=lambda : ())
    two_button.config(command=lambda : ())
    three_button.config(command=lambda : ())

    call_button.config(command=lambda : ())
    save_button.config(command=lambda : ())
    agenda.unbind('<<ListboxSelect>>')

def enable():
    global asterisk_button
    global zero_button
    global hashtag_button
    global seven_button
    global eight_button
    global nine_button
    global four_button
    global five_button
    global six_button
    global one_button
    global two_button
    global three_button
    global call_button
    global save_button
    global agenda

    asterisk_button.config(command=lambda : dial("*"))
    zero_button.config(command=lambda : dial("0"))
    hashtag_button.config(command=lambda : dial("#"))

    seven_button.config(command=lambda : dial("7"))
    eight_button.config(command=lambda : dial("8"))
    nine_button.config(command=lambda : dial("9"))

    four_button.config(command=lambda : dial("4"))
    five_button.config(command=lambda : dial("5"))
    six_button.config(command=lambda : dial("6"))

    one_button.config(command=lambda : dial("1"))
    two_button.config(command=lambda : dial("2"))
    three_button.config(command=lambda : dial("3"))

    call_button.config(command=call)
    save_button.config(command=save_contact)
    agenda.unbind('<<ListboxSelect>>')
    agenda.bind('<<ListboxSelect>>', on_select)


current_number = None
agenda_values  = dict()

number_label    = Label(text="Ingrese número", width=40, height=2, anchor="e")
number_label.place(x=7, y=5)

asterisk_button = Button(text="*", width=10, bg="white", command=lambda : dial("*"))
asterisk_button.place(x=5, y=225)
zero_button     = Button(text="0", width=10, bg="white", command=lambda : dial("0"))
zero_button.place(x=115, y=225)
hashtag_button  = Button(text="#", width=10, bg="white", command=lambda : dial("#"))
hashtag_button.place(x=225, y=225)

seven_button    = Button(text="7", width=10, bg="white", command=lambda : dial("7"))
seven_button.place(x=5, y=190)
eight_button    = Button(text="8", width=10, bg="white", command=lambda : dial("8"))
eight_button.place(x=115, y=190)
nine_button     = Button(text="9", width=10, bg="white", command=lambda : dial("9"))
nine_button.place(x=225, y=190)

four_button     = Button(text="4", width=10, bg="white", command=lambda : dial("4"))
four_button.place(x=5, y=155)
five_button     = Button(text="5", width=10, bg="white", command=lambda : dial("5"))
five_button.place(x=115, y=155)
six_button      = Button(text="6", width=10, bg="white", command=lambda : dial("6"))
six_button.place(x=225, y=155)

one_button      = Button(text="1", width=10, bg="white", command=lambda : dial("1"))
one_button.place(x=5, y=120)
two_button      = Button(text="2", width=10, bg="white", command=lambda : dial("2"))
two_button.place(x=115, y=120)
three_button    = Button(text="3", width=10, bg="white", command=lambda : dial("3"))
three_button.place(x=225, y=120)

call_button     = Button(text="Llamar", width=17, bg="green", fg="white", command=call)
call_button.place(x=5, y=85)
hangup_button   = Button(text="Colgar", width=17, bg="red", fg="white", command=hang_up)
hangup_button.place(x=170, y=85)
save_button     = Button(text="Agendar", width=37, bg="white", command=save_contact)
save_button.place(x=7, y=50)

name_label      = Label(text="Nombre:", bg="white")
name_label.place(x=350, y=6)
name_entry      = Entry(width=30)
name_entry.place(x=426, y=5)
agenda = Listbox(width=40, height=11, selectmode=BROWSE)
agenda.place(x=350, y=40)
agenda.bind('<<ListboxSelect>>', on_select)

interface.mainloop()
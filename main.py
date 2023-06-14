from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    kilometer = miles * 1.609
    km_result.config(text=f'{kilometer}')

window = Tk()
window.title('Converter')
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1,row=0)
#label

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=0,row=1)

km_result = Label(text='0')
km_result.grid(column=1,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1,row=2)



window.mainloop()

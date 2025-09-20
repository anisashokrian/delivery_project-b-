from tkinter import *
import tkinter.ttk as ttk
from datetime import  date
import tkinter.messagebox as msg
from tools.validation import *
from data_access.database_manager import *
#save_butten
def save_button():
    try:

             product_validator(product.get())
             oder_datetime_validator(oder_datetime.get())
             deliver_datetime_validator(deliver_datetime.get())

             save_delivery(product.get(), oder_datetime.get(), status.get(), deliver_datetime.get())

             msg.showinfo("Saved", " Information save")

             product.set("")
             oder_datetime.set(str(date.today()))
             deliver_datetime.set(str(date.today()))
    except Exception as e:
        msg.showerror("Error", f"{e}")

def send_butten():



#status_list
status_list = ["none", "send", "delivery", "rejected"]

window = Tk()

window.title("delivery")
window.geometry("500x300")
#product
product = StringVar()
product.get()
Label(window, text= "product", bg="dark green", fg="white", font=("LucidaConsole", 11)).place(x=20, y=20)
Entry(window, textvariable=product).place(x=145, y=22)
#oder_datetime
oder_datetime = StringVar(value=str(date.today()))
Label(window, text= "oder_datetime", bg="dark green", fg="white", font=("LucidaConsole", 11)).place(x=20, y=60)
Entry(window, textvariable=oder_datetime).place(x=145, y=62)
#status
status = StringVar(value="none")
Label(window, text= "status", bg="dark green", fg="white", font=("LucidaConsole", 12)).place(x=20, y=100)
ttk.Combobox(window, values=status_list,width = 17 , textvariable=status, state="readonly").place(x=145, y=100)
#deliver_datetime
deliver_datetime = StringVar(value=str(date.today()))
Label(window, text= "deliver_datetime", bg="dark green", fg="white", font=("LucidaConsole", 11)).place(x=20, y=140)
Entry(window, textvariable=deliver_datetime).place(x=145, y=140)
#save
Button(window, text="Save", width= 15, command=save_button).place(x=70, y=200)
#send_butten
Button(window, text="send_butten", width= 15, command=send_butten).place(x=70, y=200)

window.mainloop()
from customtkinter import *
import currency

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")

label = CTkLabel(master=app,text="Karrency Translator", font=("Century",25),text_color="#F8F8FF")

label.place(relx=0.5,rely=0.15,anchor="center")

btn = CTkButton(master=app,text="Translate",corner_radius=32,fg_color="transparent",hover_color="#4158D0",border_color="#FFCC70",border_width=2,font=("Century",25))

btn.place(relx=0.5, rely=0.7, anchor="center")

fromCurr = CTkComboBox(master=app, values=currency.CURRENCIES, fg_color="#0093E9",border_color="#FBAB7E",dropdown_fg_color="#0093E9")

fromCurr.place(relx=0.25,rely=0.4,anchor="center")

toCurr = CTkComboBox(master=app, values=currency.CURRENCIES, fg_color="#0093E9",border_color="#FBAB7E",dropdown_fg_color="#0093E9")
toCurr.place(relx=0.75,rely=0.4,anchor="center")

app.mainloop()
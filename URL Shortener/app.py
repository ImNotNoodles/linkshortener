from tkinter import *
import pyshorteners
app = Tk()
app.overrideredirect(0.5)
app.resizable(False, False)
app.geometry("500x600")
app.title("Noodle's URL Shortner")
app.iconbitmap('Untitled.ico')
bg = PhotoImage(file = "bg.png")

def shorten():
    if shorter.get():
        shorter.delete(0,END)
    if entry.get():
        url = pyshorteners.Shortener().tinyurl.short(entry.get())
        shorter.insert(END, url)
def closeapp():
    app.quit()


label1 = Label(app, image = bg)
label1.place(x = 0, y = 0)
label = Label(app, text="Enter URL", font=("Helvetica", 30), background='black', foreground='white')
label.pack(pady=20)

entry = Entry(app, font=("Helvetica", 31), background='black', foreground='white')
entry.pack(pady=20)

Thebutton = Button(app, text="Shorten URL", command=shorten, font=("Helvetica", 20), background='black', foreground='white')
Thebutton.pack(pady=20)

shortLabel=Label(app, text="Shortened Link:", font=("Helvetica", 15), background='black', foreground='white')
shortLabel.pack(pady=50)

shorter = Entry(app, font=("Helvetica", 25), justify=CENTER, background='black', foreground='white')
shorter.pack(pady=10)


exitBtn = Button(app, text="Exit App", command=closeapp, font=("Helvetica", 20), background='black', foreground='white')
exitBtn.pack(pady=50)


app.mainloop()
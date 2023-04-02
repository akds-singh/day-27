import tkinter

window = tkinter.Tk()
window.title("my GUI app")
window.minsize(width=500, height=300)

# Label
print(type(window))
my_label = tkinter.Label(text='hello world', font=('Arial', 24, 'bold'))
my_label.pack()


# my_label['text'] = 'my name  is akash'


# Button
def button_clicked():
    print(text.get())
    my_label['text'] = text.get()


my_button = tkinter.Button(text='click', command=button_clicked)
my_button.pack()

# Input text

text = tkinter.Entry(window, width=10)
text.pack()

my_input_text = text.get()

print(text.get())
window.mainloop()

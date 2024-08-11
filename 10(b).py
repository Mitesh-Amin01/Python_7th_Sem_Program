import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

result = tk.StringVar()
result.set("Result")

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, textvariable=result)

entry1.pack()
entry2.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()

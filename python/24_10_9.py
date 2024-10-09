import tkinter as tk

def convert():
    if unit.get() == "평으로 바꾸기":
        factor = 1/3.3
        result_units = "평"
    
    else:
        factor = 3.3
        result_units = "제곱미터"

    value - float(entry.get())
    result = round(value * factor, 1)

    result_label.config(test=f"{result} {result_units}")


window = tk.TK()
window.title("면적 변환기")

unit_options = ["평으로 바꾸기", "제곱미터로 바꾸기"]
unit = tk.StringVar(value=unit_options[0])
unit_dropdown = tk.OptionMenu(window,unit,*unit_options)
unit_dropdown.pack()

entry = tk.Button(window, text="변환", command=convert)
button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
import tkinter as tk

def calculate_grade():
    m1 = int(e1.get())
    m2 = int(e2.get())
    m3 = int(e3.get())

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 70:
        grade = "A"
        color = "green"
    elif avg >= 55:
        grade = "B"
        color = "blue"
    elif avg >= 40:
        grade = "C"
        color = "orange"
    else:
        grade = "Fail"
        color = "red"

    total_lbl.config(text=total)
    avg_lbl.config(text=round(avg, 2))
    grade_lbl.config(text=grade, fg=color)

# Window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("420x320")
root.configure(bg="#e8f0ff")

# Heading
tk.Label(
    root,
    text="Student Grade Calculator",
    font=("Arial", 16, "bold"),
    bg="#e8f0ff",
    fg="#2b547e"
).pack(pady=10)

# Frame
frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.pack(pady=10, padx=10)

# Inputs
tk.Label(frame, text="Subject 1 Marks", bg="white").grid(row=0, column=0, padx=10, pady=5)
e1 = tk.Entry(frame)
e1.grid(row=0, column=1)

tk.Label(frame, text="Subject 2 Marks", bg="white").grid(row=1, column=0, padx=10, pady=5)
e2 = tk.Entry(frame)
e2.grid(row=1, column=1)

tk.Label(frame, text="Subject 3 Marks", bg="white").grid(row=2, column=0, padx=10, pady=5)
e3 = tk.Entry(frame)
e3.grid(row=2, column=1)

# Button
tk.Button(
    frame,
    text="Calculate Result",
    bg="#2b547e",
    fg="white",
    command=calculate_grade
).grid(row=3, column=1, pady=10)

# Output
tk.Label(frame, text="Total Marks", bg="white", font=("Arial", 10, "bold")).grid(row=4, column=0)
total_lbl = tk.Label(frame, text="", bg="white")
total_lbl.grid(row=4, column=1)

tk.Label(frame, text="Average Marks", bg="white", font=("Arial", 10, "bold")).grid(row=5, column=0)
avg_lbl = tk.Label(frame, text="", bg="white")
avg_lbl.grid(row=5, column=1)

tk.Label(frame, text="Grade", bg="white", font=("Arial", 10, "bold")).grid(row=6, column=0)
grade_lbl = tk.Label(frame, text="", bg="white", font=("Arial", 12, "bold"))
grade_lbl.grid(row=6, column=1)

root.mainloop()

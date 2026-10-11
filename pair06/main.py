import student_utils
import tkinter as tk

students = input("Учні (через кому): ").split(",")
count = int(input("Кількість оцінок: "))

for name in students:
    name = name.strip()
    grades = student_utils.generate_grades(count)
    average = student_utils.average_grade(grades)
    level = student_utils.get_level(average)
    print(f"{name}: {grades} -> Середнє: {round(average, 2)}, Рівень: {level}")

def make_report():
    names = [name.strip() for name in entry_students.get().split(",") if name.strip()]
 
    lines = []
    for name in names:
        grades = student_utils.generate_grades(count)
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        lines.append(f"{name}: {grades} -> Середнє: {round(avg, 2)}, Рівень: {level}")
 
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "\n".join(lines))


window = tk.Tk()
window.title("Звіт про оцінки учнів")
window.geometry("600x400")
 
tk.Label(
    window,
    text="Програма генерує випадкові оцінки для учнів та\n"
         "рахує середній бал і визначає рівень учня",
    justify="center",
).pack(pady=10)
 
tk.Label(window, text="Учні (через кому):").pack()
entry_students = tk.Entry(window, width=50)
entry_students.pack(pady=(0, 10))
 
tk.Label(window, text="Кількість оцінок:").pack()
entry_count = tk.Entry(window, width=10)
entry_count.pack(pady=(0, 10))
 
button_report = tk.Button(window, text="Зформулювати звіт", command=make_report)
button_report.pack(pady=5)
 
text_result = tk.Text(window, height=10, width=70)
text_result.pack(padx=10, pady=10, fill="both", expand=True)
 
window.mainloop()

import tkinter as tk
import random

omikuji_list = ["大吉", "中吉", "小吉", "吉", "凶"]

def draw_omikuji():
    result = random.choice(omikuji_list)
    result_label.config(text=f"結果:{result}")
    if result == "大吉":
        result_label.config(fg="red")
    elif result == "凶":
        result_label.config(fg="blue")
    else:
        result_label.config(fg="black")

root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("300x200")

message_label = tk.Label(root, text="おみくじを引いてみよう！", font=("Helvetica", 14))
message_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"))
result_label.pack(pady=20)

draw_button = tk.Button(root, text="おみくじを引く",  command=draw_omikkuji)
draw_button.pack()

root.mainloop()

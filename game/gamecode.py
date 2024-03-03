import tkinter as tk

def play_game():
    global n, m, count
    while n != 0:
        k = int(entry.get()) 
        n -= k
        m += k
        if k == 5:
            result_label.config(text="Máy chọn 5. Bạn đã thua.")
            return
        else:
            for i in range(1, m + 1):
                if (i + k) % 2 == 0:
                    result_label.config(text=f"Máy chọn {i}. Máy thắng lượt {count}.")
                    break
            count += 1
            coin_label.config(text=f"Số đồng xu của máy hiện tại là: {m}")
            player_label.config(text=f"Số đồng xu của bạn hiện tại là: {n}")
            if n == 0:
                result_label.config(text="Bạn đã thua.")

n = 10  # Số đồng xu của bạn
m = 10  # Số đồng xu của máy
count = 1

root = tk.Tk()
root.title("Coin Game")

title_label = tk.Label(root, text="Trò chơi đồng xu", font=("Arial", 18))
title_label.pack(pady=10)

coin_label = tk.Label(root, text=f"Số đồng xu của máy hiện tại là: {m}", font=("Arial", 12))
coin_label.pack()

player_label = tk.Label(root, text=f"Số đồng xu của bạn hiện tại là: {n}", font=("Arial", 12))
player_label.pack()

entry_label = tk.Label(root, text="Nhập số đồng xu bạn muốn chọn (1-5):")
entry_label.pack()

entry = tk.Entry(root, width=10)
entry.pack()

play_button = tk.Button(root, text="Chơi", command=play_game)
play_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()

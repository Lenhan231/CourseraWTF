import random
import tkinter as tk
from tkinter import messagebox

YS = 20  # Initial number of player's coins
BS = 20  # Initial number of bot's coins

def botwin(YC, BC):
    global YS, BS
    YS -= YC
    BS += YC
    update_display()
    messagebox.showinfo("Result", f"Bot chose {BC}\nBot Win\nYour coin at present: {YS}\nBot coin at present: {BS}")

def botlose(BC):
    global YS, BS
    YS += BC
    BS -= BC
    update_display()
    messagebox.showinfo("Result", f"Bot chose {BC}\nBot lose\nYour coin at present: {YS}\nBot coin at present: {BS}")

def chan():
    global YS, BS
    YC = int(entry_coin.get())
    while YS != 0:
        if BS == 2:
            BC = 1 if YC % 2 != 0 else 2  
        else:
            BC = random.randint(1, min(2, BS))  # Adjusted to ensure BC doesn't exceed BS
            
        if (YC + BC) % 2 == 0:
            botlose(YC)
        else:
            botwin(YC, BC)
        
        if YS != 0:
            YC = int(entry_coin.get())
            while YC > YS:
                entry_coin.delete(0, tk.END)
                messagebox.showerror("Error", "Your coin is smaller than your input coin. Please reinput.")
                return
        if BS <= 0:
            messagebox.showinfo("Result", "Bot lose the game")
            exit_game()
            return
    messagebox.showinfo("Result", "You lose the game")
    exit_game()

def le():
    global YS, BS
    YC = int(entry_coin.get())
    while YS != 0:
        if BS == 2:
            BC = 2 if YC % 2 != 0 else 1
        else:
            BC = random.randint(1, min(2, BS))  # Adjusted to ensure BC doesn't exceed BS - 1
            
        if (YC + BC) % 2 != 0:
            botlose(YC)
        else:
            botwin(YC, BC)
        
        if YS != 0:
            YC = int(entry_coin.get())
            while YC > YS:
                entry_coin.delete(0, tk.END)
                messagebox.showerror("Error", "Your coin is smaller than your input coin. Please reinput.")
                return
        if BS <= 0:
            messagebox.showinfo("Result", "Bot lose the game")
            exit_game()
            return
    messagebox.showinfo("Result", "You lose the game")
    exit_game()

def update_display():
    label_your_coin.config(text=f"Your coin at present: {YS}")
    label_bot_coin.config(text=f"Bot coin at present: {BS}")

def exit_game():
    root.destroy()

def main():
    role = int(entry_role.get())
    global YS, BS
    YS = 20  # Số đồng xu của bạn
    BS = 20  # Số đồng xu của máy
    update_display()
    if role == 1:
        chan()
    else:
        le()

root = tk.Tk()
root.title("Coin Game")

label_instruction = tk.Label(root, text="Both Bot and Player start with 10 coins", pady=10)
label_instruction.pack()

label_your_coin = tk.Label(root, text=f"Your coin at present: {YS}")
label_your_coin.pack()

label_bot_coin = tk.Label(root, text=f"Bot coin at present: {BS}")
label_bot_coin.pack()

label_role = tk.Label(root, text="Press 1 to choose EVEN and 2 to choose ODD:")
label_role.pack()

entry_role = tk.Entry(root)
entry_role.pack()

label_coin = tk.Label(root, text="Input your coin:")
label_coin.pack()

entry_coin = tk.Entry(root)
entry_coin.pack()

button_start = tk.Button(root, text="Start", command=main)
button_start.pack()

root.mainloop()

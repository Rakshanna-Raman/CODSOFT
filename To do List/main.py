import tkinter as tk
from tkinter import messagebox

# Wednesday Title Card Theme Colors
BG_COLOR = "#230230"       
BOX_COLOR = "#886C94"      
TEXT_COLOR = "#F5F1FF"    
ACCENT_COLOR = "#FFD166"  
window = tk.Tk()
window.title("Nevermore Mission Log")
window.geometry("500x550")
window.configure(bg=BG_COLOR)

# Simple Functions (Easy to explain line-by-line!)
def set_greeting():
    name = name_entry.get()
    welcome_label.config(text=f"Welcome, Scholar: {name} 🪄")

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, f"• {task}")
        task_entry.delete(0, tk.END)

def update_task():
    selected = task_listbox.curselection()
    new_task = task_entry.get()
    if selected and new_task != "":
        task_listbox.delete(selected[0])
        task_listbox.insert(selected[0], f"• {new_task}")
        task_entry.delete(0, tk.END)

def complete_task():
    """Simple 4-line addition to mark a task as completed!"""
    selected = task_listbox.curselection()
    if selected:
        current_text = task_listbox.get(selected[0])
        # Remove the bullet point and add a checkmark
        clean_text = current_text.replace("• ", "")
        task_listbox.delete(selected[0])
        task_listbox.insert(selected[0], f"✓ [DONE] {clean_text}")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])

# --- USER INTERFACE ---
title_label = tk.Label(
    window, 
    text="🪶Nevermore Mission Log 🪶", 
    font=("Georgia", 20,"bold"), 
    bg=BG_COLOR, 
    fg=TEXT_COLOR
)
title_label.pack(pady=15)

# Profile Setup
tk.Label(window, text="Enter Scholar Name:", font=("Georgia", 12, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack()
name_entry = tk.Entry(window, width=25, bg=BOX_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief=tk.FLAT)
name_entry.pack(pady=5)

tk.Button(window, text="🏰Enter Academy", font=("Segoe UI", 10, "bold"), bg=BOX_COLOR, fg=TEXT_COLOR, command=set_greeting).pack(pady=5)

welcome_label = tk.Label(window, text="Welcome, Scholar: ______ ⭐", font=("Georgia", 12, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
welcome_label.pack(pady=10)

# Mission Input
tk.Label(window, text="Mission Entry:", font=("Georgia", 12, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack()
task_entry = tk.Entry(window, width=32, bg=BOX_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief=tk.FLAT)
task_entry.pack(pady=5)

# Control Center Buttons
tk.Button(window, text="Add Mission", font=("Segoe UI", 10, "bold"), width=18, bg=BOX_COLOR, fg=TEXT_COLOR, command=add_task).pack(pady=3)
tk.Button(window, text="Update Mission", font=("Segoe UI", 10, "bold"), width=18, bg=BOX_COLOR, fg=TEXT_COLOR, command=update_task).pack(pady=3)
tk.Button(window, text="Complete Mission", font=("Segoe UI", 10, "bold"), width=18, bg=BOX_COLOR, fg=TEXT_COLOR, command=complete_task).pack(pady=3)
tk.Button(window, text="🪶Banish Log", font=("Segoe UI", 10, "bold"), width=18, bg=BOX_COLOR, fg=TEXT_COLOR, command=delete_task).pack(pady=3)

# Log Display Box
task_listbox = tk.Listbox(
    window, 
    width=35, 
    height=9, 
    font=("Courier", 10), 
    bg=BOX_COLOR, 
    fg=TEXT_COLOR, 
    selectbackground=ACCENT_COLOR, 
    relief=tk.FLAT
)
task_listbox.pack(pady=15)

window.mainloop()
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
import importlib
import json
from tkinterdnd2 import TkinterDnD


sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))

# 創建主應用程序窗口
root = TkinterDnD.Tk()
root.title("QR Code 生成工具")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


def open_about():
    # 關於按鈕點擊事件
    messagebox.showinfo("關於", "qrcode 產生工具\n作者: Weitsunglin")


# 創建導航按鈕的 Frame
nav_frame = tk.Frame(root)
nav_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=5)

about_button = tk.Button(nav_frame, text="關於", command=open_about)
about_button.pack(side=tk.LEFT, padx=5)

notebook = ttk.Notebook(root)
notebook.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

# 加載配置
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 加載頁面
for page in config["pages"]:
    module_name = page["module"]
    page_name = page["name"]
    
    module = importlib.import_module(module_name)
    page_frame = ttk.Frame(notebook)
    notebook.add(page_frame, text=page_name)
    module.create_page(page_frame)


root.mainloop()
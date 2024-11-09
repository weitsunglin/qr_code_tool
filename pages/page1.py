import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def create_page(page1):
    label1 = tk.Label(page1, text="請輸入您的網址：")
    label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    entry1 = tk.Entry(page1)
    entry1.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

    qr_label = tk.Label(page1)
    qr_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def on_submit_click():
        url = entry1.get()
        if url:
            messagebox.showinfo("生成二维码", f"即将为网址 {url} 生成二维码!")
            qr_code = qrcode.make(url)
            qr_code = qr_code.resize((300, 300))
            qr_img_tk = ImageTk.PhotoImage(qr_code)
            qr_label.config(image=qr_img_tk)
            qr_label.image = qr_img_tk
        else:
            messagebox.showwarning("警告", "網址不能為空！")

    submit_button1 = tk.Button(page1, text="提交", command=on_submit_click)
    submit_button1.grid(row=1, column=0, padx=5, pady=5)
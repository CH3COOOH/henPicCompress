import tkinter as tk
from tkinter import filedialog, messagebox

import batch_handle

def choose_folder(entry_var):
	folder_path = filedialog.askdirectory()
	entry_var.set(folder_path)

def execute():
	img_folder = entry_folder.get()
	sav_folder = entry_sav.get()
	grayscale_checked = grayscale_var.get()
	scale_checked = scale_var.get()
	ratio = entry_ratio.get()
	quality = entry_q.get()

	params = []
	if grayscale_checked:
		params.append('-gray')
	if scale_checked:
		params.append('-sratio=' + ratio)
	params.append('-q=' + quality)
	param = ' '.join(params)
	print(param)
	for save_path in batch_handle.exec(img_folder, sav_folder, param):
		print('-> ' + save_path)
	messagebox.showinfo('Info', 'Finished!')

if __name__ == '__main__':
	window = tk.Tk()
	window.title("henPicCompress")

	# Folder部分
	label_folder = tk.Label(window, text="Folder:")
	label_folder.grid(row=0, column=0, padx=5, pady=5, sticky="e")

	entry_folder_var = tk.StringVar()
	entry_folder = tk.Entry(window, textvariable=entry_folder_var)
	entry_folder.grid(row=0, column=1, padx=5, pady=5)

	btn_img = tk.Button(window, text="...", command=lambda: choose_folder(entry_folder_var))
	btn_img.grid(row=0, column=2, padx=5, pady=5, sticky="w")

	label_sav = tk.Label(window, text="Saveto:")
	label_sav.grid(row=1, column=0, padx=5, pady=5, sticky="e")

	entry_sav_var = tk.StringVar()
	entry_sav = tk.Entry(window, textvariable=entry_sav_var)
	entry_sav.grid(row=1, column=1, padx=5, pady=5)

	btn_sav = tk.Button(window, text="...", command=lambda: choose_folder(entry_sav_var))
	btn_sav.grid(row=1, column=2, padx=5, pady=5, sticky="w")

	grayscale_var = tk.BooleanVar()
	check_grayscale = tk.Checkbutton(window, text="Grayscale", variable=grayscale_var)
	check_grayscale.grid(row=2, column=0, padx=5, pady=5, columnspan=3, sticky="w")

	scale_var = tk.BooleanVar()
	check_scale = tk.Checkbutton(window, text="Resize (0.0-1.0)", variable=scale_var)
	check_scale.grid(row=3, column=0, padx=5, pady=5, sticky="w")

	entry_ratio = tk.Entry(window)
	entry_ratio.grid(row=3, column=1, padx=5, pady=5, sticky="w")

	label_q = tk.Label(window, text="Quality (1-100)")
	label_q.grid(row=4, column=0, padx=5, pady=5, sticky="e")

	entry_q = tk.Entry(window)
	entry_q.grid(row=4, column=1, padx=5, pady=5)

	btn_execute = tk.Button(window, text="GO", command=execute)
	btn_execute.grid(row=5, column=0, columnspan=3, pady=10)

	window.mainloop()

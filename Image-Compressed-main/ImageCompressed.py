import tkinter.filedialog as filedialog
from PIL import ImageTk ,Image
from tkinter import messagebox
import tkinter as tk
import shutil, os
import sys

master = tk.Tk()

def compressImg(file):

    file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    image = Image.open(file_path)

	# Set quality= to the preferred quality.
	# 85 has no difference in low size (MB) files and 65 is the lowest reasonable number
    image.save("Compressed_"+file,"JPEG",optimize=True,quality=65, )
    messagebox.showinfo("Compressed Success",  
                        "Image Saved\n" )
    master.after(100, master.destroy) 
   # os.system("pause")
   # messagebox.showinfo("Compressed Success!\n") 
        
    #with open(filename + '.jpg', 'wb') as f:
        
     # shutil.move(image.save+'.JPEG','Downloads')
       #shutil.copyfileobj(data.raw, file)

def main():
    
    
	# Gets current working directory
	dir = os.getcwd()
	for file in os.listdir(dir):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			compressImg(file)
    
    #input_entry.delete(1, tk.END)  # Remove current text in entry
    #input_entry.insert(0, input_path)  # Insert the 'path'


#def output():
 #   path = tk.filedialog.askopenfilename()
 #   input_entry.delete(1, tk.END)  # Remove current text in entry
 #   input_entry.insert(0, path)  # Insert the 'path'


top_frame = tk.Frame(master)
master.resizable(False, False) 
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=300, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=main)

#output_path = tk.Label(bottom_frame, text="Output File Path:")
#output_entry = tk.Entry(bottom_frame, text="", width=40)
#browse2 = tk.Button(bottom_frame, text="Browse", command=output)

#begin_button = tk.Button(bottom_frame, text='Done!')

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

#output_path.pack(pady=5)
#output_entry.pack(pady=5)
#browse2.pack(pady=5)


master.mainloop()


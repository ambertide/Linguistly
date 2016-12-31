from commonExpressions import CommonExpressions, prepare, save
from docx import Document
import tkinter as tk
from tkinter import filedialog


class Latte:
    def __init__(self, master):
        self.master = master
        master.title("Lingua MultiCounter")
        self.word_count_entry = tk.Entry(master)
        self.files_to_count_entry = tk.Entry(master)
        self.files_to_count_entry.grid(row=0, column=0,
            columnspan= 3, sticky= tk.W + tk.S + tk.N + tk.E)
        self.word_count_entry.grid(row=1, column=0, columnspan=2,
                                    sticky= tk.W + tk.S + tk.N + tk.E)
        self.selectorVar = tk.StringVar()
        self.selectorVar.set("sqlite3")
        self.output_type_selector = tk.OptionMenu(master, self.selectorVar,
                                        "sqlite3", "txt", "xlsx")
        #Allright, something WILL go wrong!
        self.output_type_selector.grid(row=0, column=3,
                                        sticky= tk.W + tk.S + tk.N + tk.E)
        self.analyize_button = tk.Button(master, text= "Analyise",
                                            command= lambda: self.commence())
        self.analyize_button.grid(row=1, column=2,
            sticky= tk.W + tk.S + tk.N + tk.E)
        self.word_count_entry.insert(tk.END, "Word to count")
        self.files_to_count_entry.insert(tk.END,
                                        "Name of the files (comma-seperated)")

    def commence(self):
        #Oh common...
        files = self.files_to_count_entry.get().split(",")
        results = {}
        data = ""
        for i in range(len(files)):
            extension = files[i].split(".")
            print(extension)
            if extension[1] == "txt":
                file_ = open(files[i], "r")
                data = file_.read()
                file_.close()
            elif extension[1] == "docx":
                file = Document(self.file_directory)
                parags = file.paragraphs
                for i in range(len(parags)):
                    data += (parags[i].text + "\n")
            print(data)
            print(type(data))
            data = prepare(data)
            count = data.count(self.word_count_entry.get())
            results[files[i]] = count
        print(self.selectorVar.get())
        print(files)
        print(results)
        save(results, files, self.selectorVar.get())
        print(self.selectorVar.get())
        print(files)
        print(results)

root = tk.Tk()
cappucino = Latte(root)
root.mainloop()

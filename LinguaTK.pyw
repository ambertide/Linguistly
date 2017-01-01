import tkinter as tk
from tkinter import filedialog
from commonExpressions import CommonExpressions, prepare, save
from docx import Document


class Latte:
    def __init__(self, master):
        self.master = master
        master.title("LinguaTK")
        self.file_directory = ""
        self.file_directory_label = tk.Label(master,
            text = "Please select your file?")
        self.file_directory_button = tk.Button(master,
            text = "Browse", command = lambda: self.browse())
        self.selectorVar = tk.StringVar(master)
        self.selectorVar.set("csv")
        self.checkBoxVar = tk.IntVar(master)
        self.output_method_select = tk.OptionMenu(master, self.selectorVar,
            "txt", "sqlite3", "xlsx", "csv")
        self.is_turkish = tk.Checkbutton(master, text= "Turkish",
            variable = self.checkBoxVar)
        self.output_finalize_button = tk.Button(master, text="Analyize",
            state = tk.DISABLED, command= lambda: self.commence())
        self.file_directory_label.grid(row=0, column=0, columnspan=2,
            sticky=tk.W + tk.E + tk.S + tk.N)
        self.file_directory_button.grid(row=0, column=2,
            sticky=tk.W + tk.E + tk.S + tk.N)
        self.output_method_select.grid(row=1, column=0,
            sticky=tk.W + tk.E + tk.S + tk.N)
        self.is_turkish.grid(row=1, column=1)
        self.output_finalize_button.grid(row=1, column=2,
            sticky=tk.W + tk.E + tk.S + tk.N)
    def browse(self):
        options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [("Text Files", ".txt"),
                                ("Word Files", ".docx")]
        options['title'] = 'Select File'
        self.file_directory = filedialog.askopenfilename(**options)
        self.file_directory_label['text'] = self.file_directory
        self.output_finalize_button['state'] = 'normal'

    def commence(self):
        extension = self.file_directory.split(".")
        initdata = ""
        findata = []
        if extension[1] == "txt":
            file = open(self.file_directory, "r")
            initdata = file.read()
            file.close()
        elif extension[1] == "docx":
            initdata = ""
            file = Document(self.file_directory)
            parags = file.paragraphs
            for i in range(len(parags)):
                initdata += parags[i].text
        if self.checkBoxVar.get() == 1:
            findata = prepare(initdata)
        elif self.checkBoxVar.get() == 0:
            findata = prepare(initdata)
        indexed = {}
        indata = list(set(findata))
        for i in range(len(indata)):
            indexed[indata[i]] = findata.count(indata[i])
        keysindex = list(indexed)
        save(indexed, keysindex,
            outputtype = self.selectorVar.get())
root = tk.Tk()
cappucino = Latte(root)
root.mainloop()

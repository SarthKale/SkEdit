import tkinter as tk 
from tkinter import filedialog
import pyautogui as ag 

# Class to display and manage Menu Bar. 
class Menubar:
    def __init__(self, parent): 
        font_detail = ("Windows", 9) 
        menubar = tk.Menu(parent.master, font=font_detail) 
        parent.master.config(menu=menubar)

        # File Menu 
        file_dd = tk.Menu(menubar, font=font_detail, tearoff=0) 
        file_dd.add_command(label="New File", command=parent.new_file, accelerator="Ctrl+N") 
        file_dd.add_separator() 
        file_dd.add_command(label="Open File", command=parent.open_file, accelerator="Ctrl+O") 
        file_dd.add_separator() 
        file_dd.add_command(label="Save", command=parent.save, accelerator="Ctrl+S") 
        file_dd.add_command(label="Save As", command=parent.save_as, accelerator="Ctrl+Shift+S") 
        file_dd.add_separator() 
        file_dd.add_command(label="Close", command=parent.master.destroy) 

        # Edit Menu 
        edit_dd = tk.Menu(menubar, font=font_detail, tearoff=0) 
        edit_dd.add_command(label="Cut", command=parent.cut, accelerator="Ctrl+X") 
        edit_dd.add_command(label="Copy", command=parent.copy, accelerator="Ctrl+C") 
        edit_dd.add_command(label="Paste", command=parent.paste, accelerator="Ctrl+V") 
        
        menubar.add_cascade(label="File", menu=file_dd) 
        menubar.add_cascade(label="Edit", menu=edit_dd) 

# Class to display and manage the Status Bar below the text area. 
class Statusbar:
    def __init__(self, parent):
        font_detail = ("Windows", 10) 
        self.status = tk.StringVar() 
        self.status.set("SkText - 0.1 Text Editor") 
        label = tk.Label(parent.textarea, textvar=self.status, fg="black", bg="lightgrey", anchor="sw", font=font_detail) 
        label.pack(side=tk.BOTTOM, fill=tk.BOTH) 

    def update_status(self, *args):
        if isinstance(args[0], bool):
            st1 = "File Saved : " +args[1] 
            self.status.set(st1) 
        else:
            self.status.set("SkText - 0.1 Text Editor") 

# Class to control and manage the overall functionality of the program. 
class SkText:
    def __init__(self, master): 
        master.title("Untitled - SkText")
        master.geometry("1200x600") 
        font_detail = ("Windows", 14) 
        self.master = master 
        self.filename = None 
        self.textarea = tk.Text(master, font=font_detail) 
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview) 
        self.textarea.configure(yscrollcommand=self.scroll.set) 
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)  
        self.menubar = Menubar(self) 
        self.statusbar = Statusbar(self) 
        self.shortcuts() 

    # Manages the Title Bar of the Text Editor. 
    def set_title(self, name=None):
        if name:
            self.master.title(name + " - SkText") 
        else: 
            self.master.title("Untitled - SkText") 

    # Creates an empty new document. 
    def new_file(self, *args): 
        self.textarea.delete(1.0, tk.END) 
        self.filename = None 
        self.set_title() 

    # Opening of existing files in the system. 
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", 
            filetypes=[("All Files", "*.*"), 
                    ("Bash Script Files", "*.sh"), 
                    ("C Files", "*.c"), 
                    ("C++ Files", "*.cpp"), 
                    ("CSV Files", "*.csv"), 
                    ("CSS Files", "*.css"), 
                    ("C Sharp Files", "*.cs"), 
                    ("MSWord Files", "*.docx"), 
                    ("HTML Files", "*.htm"), 
                    ("Java Files", "*.java"),
                    ("Java Class Files", "*.class"), 
                    ("JavaScript Files", "*.js"),  
                    ("Kotlin Files", "*.kt"), 
                    ("Markdown Files", "*.md"), 
                    ("Pearl Files", "*.pl"), 
                    ("PHP Files", "*.php"), 
                    ("Swift Files", "*.swift"), 
                    ("Text Files", "*.txt")]) 
        if self.filename: 
            self.textarea.delete(1.0, tk.END) 
            with open(self.filename, "r") as f: 
                self.textarea.insert(1.0, f.read()) 
            self.set_title(self.filename) 

    # Executes the Saving of a document. 
    def save(self, *args):
        if self.filename: 
            try:
                content = self.textarea.get(1.0, tk.END) 
                with open(self.filename, "w") as f: 
                    f.write(content) 
                self.statusbar.update_status(True, self.filename) 
            except Exception as e: 
                print(e) 
        else: 
            self.save_as() 

    # Executes Saving of the new document. 
    def save_as(self, *args):
        try:
            newfile = filedialog.asksaveasfilename(initialfile="Untitled.txt", 
            defaultextension=".txt", 
            filetypes=[("All Files", "*.*"), 
                    ("Bash Script Files", "*.sh"), 
                    ("C Files", "*.c"), 
                    ("C++ Files", "*.cpp"), 
                    ("CSS Files", "*.css"), 
                    ("C Sharp Files", "*.cs"), 
                    ("MSWord Files", "*.docx"), 
                    ("HTML Files", "*.htm"), 
                    ("Java Files", "*.java"),
                    ("Java Class Files", "*.class"), 
                    ("JavaScript Files", "*.js"),  
                    ("Kotlin Files", "*.kt"), 
                    ("Markdown Files", "*.md"), 
                    ("Pearl Files", "*.pl"), 
                    ("PHP Files", "*.php"), 
                    ("Swift Files", "*.swift"), 
                    ("Text Files", "*.txt")]) 
            
            content = self.textarea.get(1.0, tk.END) 
            with open(newfile, "w") as f: 
                f.write(content) 
                self.filename = newfile 
                self.set_title(self.filename) 
                self.statusbar.update_status(True, self.filename) 
        except Exception as e: 
            print(e) 

    # Controls the Editing feature Cut. 
    def cut(self):
        ag.keyDown("ctrl") 
        ag.keyDown("x") 
        ag.keyUp("x") 
        ag.keyUp("ctrl") 

    # Controls the Editing feature Copy. 
    def copy(self):
        ag.keyDown("ctrl") 
        ag.keyDown("c") 
        ag.keyUp("c") 
        ag.keyUp("ctrl") 

    # Controls the Editing feature Paste. 
    def paste(self): 
        ag.keyDown("ctrl") 
        ag.keyDown("v") 
        ag.keyUp("v") 
        ag.keyUp("ctrl") 

    # Links keyboard shortcuts with the Edit Menu in Menu Bar. 
    def shortcuts(self): 
        self.textarea.bind('<Control-n>', self.new_file) 
        self.textarea.bind('<Control-o>', self.open_file) 
        self.textarea.bind('<Control-s>', self.save) 
        self.textarea.bind('<Control-S>', self.save_as) 
        self.textarea.bind('<Key>', self.statusbar.update_status) 

if __name__ == "__main__":
    master = tk.Tk() 
    pt = SkText(master) 
    master.mainloop() 

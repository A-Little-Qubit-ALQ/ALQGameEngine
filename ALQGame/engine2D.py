from tkinter import *
from math import sqrt
from multiprocessing import *
from threading import *
from UI import Button,Label,Frame
from FileSystem import Config,StyleSheet
class Settings(Config):
    def __init__(self):
        super().__init__()


class Project():
    def __init__(self):
        self.settings=Settings()
        self.window=Tk()
        if self.settings["screensize"]==None:
            self.window.geometry("800x600")
        else:
            self.window.geometry(self.settings["screensize"])
        self.tree=[]
    def get_window(self):
        return self.window
    def d_tree(self):
        return {i.name:i.d_tree() for i in self.tree}
    def save(self):
        self.file=Config(file_name="project",format=".alqproj")
        self.file["project"]=self.d_tree()
    def new_child(self,element):
        self.tree.append(element)
    def run(self):
        self.window.mainloop()
class View2D():
    def __init__(self,parent,name="Untitled"):
        self.parent=parent
        self.name=name
        self.parent.new_child(self)
        self.canvas=Canvas(self.get_window(),background="#FFFFFF",width=self.parent.get_window().winfo_screenwidth(),height=self.parent.get_window().winfo_screenheight())
        self.canvas.pack()
        self.tree=[]
    def get_window(self):
        return self.parent.get_window()
    def d_tree(self):
        return {i.name:i.d_tree() for i in self.tree}
    def new_child(self,element):
        self.tree.append(element)
    def get_canvas(self):
        return self.canvas
root=Project()
window=View2D(root)
a=StyleSheet("./style.alqss",root.get_window())
a.process()
print(a.style)
frame=Frame(window,style=a,name="frame")
frame.draw()
button_1=Button(frame,"test",style=a)
button_1.draw()
button_2=Button(frame,"test",style=a,name="button_2")
button_2.draw()

label_1=Label(frame,"test",style=a,name="label_1")

label_1.draw()
root.save()
root.run()



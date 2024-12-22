import tkinter
import FileSystem
from typing import Any
class Button():
    def __init__(self,parent,title="Label",name="button",style:FileSystem.StyleSheet=None):
        self.parent=parent# parent contains the canvas called by get_canvas
        self.title=title
        self.name=name
        self.style=style.style
        self.parent.new_child(self)
        if name in self.style:
            self.style=self.style[name]
        self.tree=[]

    def new_child(self,child):
        self.tree.append(child)
    def get_canvas(self):
        return self.parent.get_canvas()
    def get_window(self):
        return self.parent.get_window()
    def d_tree(self):
        return {i.name:i.d_tree() for i in self.tree}
    def draw(self):
        self.canvas=self.get_canvas()
        self.window=self.get_window()
        if "position-x" in self.style:
            position_x=self.style["position-x"].x
        else:
            position_x=0
        if "position-y" in self.style:
            position_y=self.style["position-y"].x
        else:
            position_y=0
        if "width" in self.style:
            width=self.style["width"].x
        else:
            width=100
        if "height" in self.style:
            height=self.style["height"].x
        else:
            height=100
        if "font-family" in self.style:
            font_family=self.style["font-family"].replace(";","").replace(" ","")
        else:
            font_family="Arial"
        if "font-size" in self.style:
            font_size=self.style["font-size"].x
        else:
            font_size=12
        font=f"{font_family} {font_size}"
        if "color" in self.style:
            color=self.style["color"].hex()
        else:
            color="#000000"
        if "border-width" in self.style:
            border_width=self.style["border-width"].x
        else:
            border_width=0
        if "border-color" in self.style:
            border_color=self.style["border-color"].hex()
        else:
            border_color="#000000"
        if "text-color" in self.style:
            text_color=self.style["text-color"].hex()
        else:
            text_color="#000000"
        if "anchor" in self.style:
            anchor=self.style["anchor"].replace(";","").replace(" ","")
        else:
            anchor="center"
        print(f"position: {position_x} {position_y} color: {color} border: {border_color} {border_width}")
        if anchor=="center":
            cc=(position_x-width/2,position_y-height/2,position_x+width/2,position_y+height/2)
            ct=(position_x,position_y)
        elif anchor=="nw":
            cc=(position_x,position_y,position_x+width,position_y+height)
            ct=(position_x+width/2,position_y+height/2)
        elif anchor=="ne":
            cc=(position_x-width,position_y,position_x,position_y+height)
            ct=(position_x-width/2,position_y+height/2)
        elif anchor=="sw":
            cc=(position_x-width,position_y-height,position_x,position_y)
            ct=(position_x-width/2,position_y-height/2)
        elif anchor=="se":
            cc=(position_x,position_y-height,position_x+width,position_y)
            ct=(position_x+width/2,position_y-height/2)
        
        self.button_background=self.canvas.create_rectangle(cc,width=border_width,outline=border_color,fill=color,tags=(self.name,))
        self.button_text=self.canvas.create_text(ct,text=self.title,font=font,fill=text_color,tags=(self.name,))
        self.canvas.tag_bind(self.name, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.name, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.name, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.name, "<ButtonRelease>", self.on_release)
    def on_click(self,event):
        
        print(f"Button {self.name} clicked!")
    def on_enter(self,event):
        print(f"Button {self.name} entered!")
    def on_leave(self,event):
        print(f"Button {self.name} left!")
    def on_release(self,event):
        print(f"Button {self.name} released!")
    def delete(self):
        self.canvas.delete(self.button_background)
        self.canvas.delete(self.button_text)
    def move(self,dx,dy):
        self.canvas.move(self.button_background, dx, dy)
        self.canvas.move(self.button_text, dx, dy)
    def change_style(self, new_style:FileSystem.StyleSheet):
        self.style=new_style.style
        if self.name in self.style:
            self.style=self.style[self.name]
        self.draw()
    def change_text(self, new_text):
        self.canvas.itemconfig(self.button_text, text=new_text)
    def change_color(self, new_color):
        self.canvas.itemconfig(self.button_background, fill=new_color)
        self.canvas.itemconfig(self.button_text, fill=new_color)
    def change_border_color(self, new_color):
        self.canvas.itemconfig(self.button_background, outline=new_color)
    def change_border_width(self, new_width):
        self.canvas.itemconfig(self.button_background, width=new_width)
    def change_font(self, new_font):
        self.canvas.itemconfig(self.button_text, font=new_font)
    def change_text_color(self, new_color):
        self.canvas.itemconfig(self.button_text, fill=new_color)
    def change_position(self, new_position_x, new_position_y):
        self.canvas.move(self.button_background, new_position_x-self.style["position-x"].x, new_position_y-self.style["position-y"].x)
        self.canvas.move(self.button_text, new_position_x, new_position_y)
        self.style["position-x"].x=new_position_x
        self.style["position-y"].x=new_position_y
    
class Label():
    def __init__(self,parent,text="Label",name="label",style:FileSystem.StyleSheet=None):
        self.parent=parent
        self.text=text
        self.name=name
        self.style=style.style
        self.parent.new_child(self)
        if name in self.style:
            self.style=self.style[name]
        self.tree=[]
    def new_child(self,child):
        self.tree.append(child)
    def get_canvas(self):
        return self.parent.get_canvas()
    def get_window(self):
        return self.parent.get_window()
    def d_tree(self):
        return {i.name:i.d_tree() for i in self.tree}
    def draw(self):
        self.canvas=self.get_canvas()
        self.window=self.get_window()
        if "position-x" in self.style:
            position_x=self.style["position-x"].x
        else:
            position_x=0
        if "position-y" in self.style:
            position_y=self.style["position-y"].x
        else:
            position_y=0
        if "width" in self.style:
            width=self.style["width"].x
        else:
            width=100
        if "height" in self.style:
            height=self.style["height"].x
        else:
            height=100
        if "font-family" in self.style:
            font_family=self.style["font-family"].replace(";","").replace(" ","")
        else:
            font_family="Arial"
        if "font-size" in self.style:
            font_size=self.style["font-size"].x
        else:
            font_size=12
        font=f"{font_family} {font_size}"
        if "color" in self.style:
            color=self.style["color"].hex()
        else:
            color="#000000"
        if "border-width" in self.style:
            border_width=self.style["border-width"].x
        else:
            border_width=0
        if "border-color" in self.style:
            border_color=self.style["border-color"].hex()
        else:
            border_color="#000000"
        if "text-color" in self.style:
            text_color=self.style["text-color"].hex()
        else:
            text_color="#000000"
        if "anchor" in self.style:
            anchor=self.style["anchor"].replace(";","").replace(" ","")
        else:
            anchor="center"
        print(f"position: {position_x} {position_y} color: {color} border: {border_color} {border_width}")
        if anchor=="center":
            cc=(position_x-width/2,position_y-height/2,position_x+width/2,position_y+height/2)
            ct=(position_x,position_y)
        elif anchor=="nw":
            cc=(position_x,position_y,position_x+width,position_y+height)
            ct=(position_x+width/2,position_y+height/2)
        elif anchor=="ne":
            cc=(position_x-width,position_y,position_x,position_y+height)
            ct=(position_x-width/2,position_y+height/2)
        elif anchor=="sw":
            cc=(position_x-width,position_y-height,position_x,position_y)
            ct=(position_x-width/2,position_y-height/2)
        elif anchor=="se":
            cc=(position_x,position_y-height,position_x+width,position_y)
            ct=(position_x+width/2,position_y-height/2)
        
        self.button_text=self.canvas.create_text(ct,text=self.text,font=font,fill=text_color,tags=(self.name,))
        self.canvas.tag_bind(self.name, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.name, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.name, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.name, "<ButtonRelease>", self.on_release)
    def on_click(self,event):
        
        print(f"Label {self.name} clicked!")
    def on_enter(self,event):
        print(f"Label {self.name} entered!")
    def on_leave(self,event):
        print(f"Label {self.name} left!")
    def on_release(self,event):
        print(f"Label {self.name} released!")
class Frame():
    def __init__(self,parent,name="frame",style:FileSystem.StyleSheet=None):
        self.parent=parent
        self.name=name
        self.parent.new_child(self)
        self.style=style.style
        if name in self.style:
            self.style=self.style[name]
        self.tree=[]
    def new_child(self,child):
        self.tree.append(child)
    def get_canvas(self):
        return self.parent.get_canvas()
    def get_window(self):
        return self.parent.get_window()
    def d_tree(self):
        return {i.name:i.d_tree() for i in self.tree}
    def draw(self):
        self.canvas=self.get_canvas()
        self.window=self.get_window()
        if "position-x" in self.style:
            position_x=self.style["position-x"].x
        else:
            position_x=0
        if "position-y" in self.style:
            position_y=self.style["position-y"].x
        else:
            position_y=0
        if "width" in self.style:
            width=self.style["width"].x
        else:
            width=100
        if "height" in self.style:
            height=self.style["height"].x
        else:
            height=100
        if "font-family" in self.style:
            font_family=self.style["font-family"].replace(";","").replace(" ","")
        else:
            font_family="Arial"
        if "font-size" in self.style:
            font_size=self.style["font-size"].x
        else:
            font_size=12
        font=f"{font_family} {font_size}"
        if "color" in self.style:
            color=self.style["color"].hex()
        else:
            color="#000000"
        if "border-width" in self.style:
            border_width=self.style["border-width"].x
        else:
            border_width=0
        if "border-color" in self.style:
            border_color=self.style["border-color"].hex()
        else:
            border_color="#000000"
        if "text-color" in self.style:
            text_color=self.style["text-color"].hex()
        else:
            text_color="#000000"
        if "anchor" in self.style:
            anchor=self.style["anchor"].replace(";","").replace(" ","")
        else:
            anchor="center"
        print(f"position: {position_x} {position_y} color: {color} border: {border_color} {border_width}")
        if anchor=="center":
            cc=(position_x-width/2,position_y-height/2,position_x+width/2,position_y+height/2)
            ct=(position_x,position_y)
        elif anchor=="nw":
            cc=(position_x,position_y,position_x+width,position_y+height)
            ct=(position_x+width/2,position_y+height/2)
        elif anchor=="ne":
            cc=(position_x-width,position_y,position_x,position_y+height)
            ct=(position_x-width/2,position_y+height/2)
        elif anchor=="sw":
            cc=(position_x-width,position_y-height,position_x,position_y)
            ct=(position_x-width/2,position_y-height/2)
        elif anchor=="se":
            cc=(position_x,position_y-height,position_x+width,position_y)
            ct=(position_x+width/2,position_y-height/2)
        
        self.button_background=self.canvas.create_rectangle(cc,width=border_width,outline=border_color,fill=color,tags=(self.name,))
        self.canvas.tag_bind(self.name, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.name, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.name, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.name, "<ButtonRelease>", self.on_release)
    def on_click(self,event):
        
        print(f"Label {self.name} clicked!")
    def on_enter(self,event):
        print(f"Label {self.name} entered!")
    def on_leave(self,event):
        print(f"Label {self.name} left!")
    def on_release(self,event):
        print(f"Label {self.name} released!")
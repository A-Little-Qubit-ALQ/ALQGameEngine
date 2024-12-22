import tkinter
from functools import singledispatchmethod
class RGB():
    r,g,b=0,0,0
    ...
class RGB():
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    @singledispatchmethod
    def __add__(self, other):
        raise f"You can`t sum RGB with any variable of type {type(other)}"
    @__add__.register
    def _(self, other:RGB):
        self.r+=other.r
        self.g+=other.g
        self.b+=other.b

    @__add__.register
    def _(self, other: int):
        self.r += other
        self.g += other
        self.b += other

    @singledispatchmethod
    def __mul__(self, other):
        raise f"You can`t sum multiply with any variable of type {type(other)}"

    @__mul__.register
    def _(self, other: RGB):
        self.r *= other.r
        self.g *= other.g
        self.b *= other.b

    @__mul__.register
    def _(self, other: int):
        self.r *= other
        self.g *= other
        self.b *= other
    def hex(self):
        return f"#{'0'*(2-len(hex(self.r)[2:]))+hex(self.r)[2:]}{'0'*(2-len(hex(self.g)[2:]))+hex(self.g)[2:]}{'0'*(2-len(hex(self.b)[2:]))+hex(self.b)[2:]}"
class Size():
    def __init__(self, x,window:tkinter.Tk):
        self.window=window
        self.xx=x.replace(";","").replace(" ","")
        if "w%" in self.xx:
            self.x=int(self.xx[:-2])*window.winfo_screenwidth()/100
        elif "h%" in self.xx:
            self.x=int(self.xx[:-2])*window.winfo_screenheight()/100    
        elif "vh" in self.xx or "vw" in self.xx:
            if "vw" in self.xx:
                self.x=int(self.xx[:-2])*window.winfo_screenwidth()
            elif "vh" in self.xx:
                self.x=int(self.xx[:-2])*window.winfo_screenheight()
        else:
            self.x=int(self.xx[:-2])
    def recount(self):
        if "w%" in self.xx:
            self.x=int(self.xx[:-1])*self.window.winfo_screenwidth()/100
        elif "h%" in self.xx:
            self.x=int(self.xx[:-1])*self.window.winfo_screenheight()/100     
        elif "vh" in self.xx or "vw" in self.xx:
            if "vw" in self.xx:
                self.x=int(self.xx[:-2])*self.window.winfo_screenwidth()
            elif "vh" in self.xx:
                self.x=int(self.xx[:-2])*self.window.winfo_screenheight()
        else:
            self.x=int(self.xx[:-2])
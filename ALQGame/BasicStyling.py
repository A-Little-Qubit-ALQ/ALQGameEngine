import tkinter
from functools import singledispatchmethod

class RGB():
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b

    @singledispatchmethod
    def __add__(self, other):
        if type(other) == RGB:
            self.r+=other.r
            self.g+=other.g
            self.b+=other.b
            self.r = round(self.r) % 256
            self.g = round(self.g) % 256
            self.b = round(self.b) % 256

        else:
            raise Exception(f"You can`t sum RGB with any variable of type {type(other)}")
    @__add__.register
    def _(self, other: int):
        self.r += other
        self.g += other
        self.b += other

    @singledispatchmethod
    def __mul__(self, other):
        if type(other)==RGB:
            self.r *= other.r
            self.g *= other.g
            self.b *= other.b

        else:
            raise Exception(f"You can`t multiply RGB with any variable of type {type(other)}")

    @__mul__.register
    def _(self, other: int):
        self.r *= other
        self.g *= other
        self.b *= other

    @__mul__.register
    def _(self, other: float):
        self.r *= other
        self.g *= other
        self.b *= other
        self.r=round(self.r)%256
        self.g = round(self.g)%256
        self.b = round(self.b)%256
    def hex(self):
        self.r=round(self.r)
        self.g = round(self.g)
        self.b = round(self.b)
        return f"#{'0'*(2-len(hex(self.r)[2:]))+hex(self.r)[2:]}{'0'*(2-len(hex(self.g)[2:]))+hex(self.g)[2:]}{'0'*(2-len(hex(self.b)[2:]))+hex(self.b)[2:]}"
    def copy(self):
        return RGB(self.r,self.g,self.b)
    def PIL(self):
        return [self.r,self.g,self.b]
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
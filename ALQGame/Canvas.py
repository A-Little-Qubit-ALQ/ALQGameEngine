from BasicStyling import RGB,Size
from math import *
from PIL import Image
import numpy as np
"""
TOP VIEW ELEMENTS
to distribute 2d games
Classes
1. TopViewProject
2. TopViewFloor
3. TopViewLight
"""
def dist(pixel,light):
    return sqrt((pixel.x-light.position[0])**2+(pixel.y-light.position[1])**2)
class PIXEL():
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
        self.colors=[]
        self.powers=[]
    def add_color(self,color:RGB,power):
        self.colors.append(color)
        self.powers.append(power)
    def RGBCOUNT(self):
        powerz=sum([self.powers[i] for i in range(len(self.powers))])
        r=sum([self.colors[i].r*self.powers[i] for i in range(len(self.powers))])/powerz
        g=sum([self.colors[i].g*self.powers[i] for i in range(len(self.powers))])/powerz
        b=sum([self.colors[i].b*self.powers[i] for i in range(len(self.powers))])/powerz
        self.tot_color=RGB(r,g,b)
def alqrange(start_index,end_index,step=1):
    while start_index<end_index:
        yield start_index
        start_index += step
class Matrix():
    def __init__(self,size):
        self.size=size
        self.data=[[[] for i in range(size[0])] for j in range(size[1])]
        self.image=Image.new('RGB', self.size,(0,0,0))
        self.image=np.array(self.image, dtype=np.uint8)
        self.image.setflags(write=1)
    def put_pixel(self,pixel:PIXEL):
        self.data[pixel.x][pixel.y]=pixel.tot_color.hex()
        print(type(pixel.tot_color.PIL()))
        self.image[pixel.x,pixel.y]=pixel.tot_color.PIL()
    def show(self):
        self.image_copy=Image.fromarray(self.image)
        self.image_copy.show()
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                print(self.data[i][j])
class ViewPort():
    def __init__(self,size=[100,100]):
        self.size=size
        self._Matrix=Matrix(size)
    def Pixels(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                yield PIXEL(x,y)
    def fill(self,color):
        pass
    def ray(self,power,color,position,angle):
        x,y=position
        xs,ys=x,y
        step=1
        xw,yh=self._Matrix.size
        distance_m=sqrt((xw-xs)**2+(yh-ys)**2)
        color2=color.copy()
        while x+xw//2 in range(xw) and y+yh//2 in range(yh):
            distance=sqrt((xs-x)**2+(ys-y)**2)
            if distance == 0:
                distance=1
            color2 * (power / (distance / distance_m))
            self._Matrix.data[round(x)][round(y)].append(color2)
            if sin(angle)!=0:
                y+=step/sin(angle)
            if cos(angle)!=0:
                x+=step/cos(angle)
    def Matrix(self):
        return self._Matrix
class TopViewProject():
    def __init__(self,parent, name,shader=None):
        self.name = name
        self.parent = parent
        self.elements = []
        self.parent.new_child(self)
        self.window=parent.get_window()
        self.canvas=parent.get_canvas()
        self.lights=[]
        self.floor=None
        self.shader=shader
        self._viewport=ViewPort()
        self.tree=[]
    def get_tree(self):
        return f"{self.name}:\n"
    def get_floor(self):
        for i in self.elements:
            if type(i)==TopViewFloor:
                return i
    def render(self):
        exec(self.shader.logic_blocks)
    def viewport(self):
        return self._viewport
    def d_tree(self):
        return self.tree
class TopViewFloor():
    def __init__(self,TopviewProject:TopViewProject,color,sharpness=1):
        self.topviewproject = TopviewProject
        self.color = color
        self.sharpness = sharpness
        self.topviewproject.floor=self
class TopViewOmni():
    def __init__(self,TopviewProject:TopViewProject, position, color, size,power=1,distance=10):
        self.color = color
        self.topviewproject = TopviewProject
        self.position = position
        self.size = size
        self.power=power
        self.distance=distance
        self.topviewproject.lights.append(self)

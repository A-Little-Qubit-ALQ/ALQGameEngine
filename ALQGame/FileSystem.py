import re
from json import *
from pathlib import *
from functools import singledispatchmethod
from BasicStyling import RGB,Size
from re import findall
class Config():
    def __init__(self,config_dir=".",file_name="settings",format=".alqconf"):
        self.dir=config_dir
        self.name=file_name
        self.format=format
        if not(Path(config_dir+"/"+file_name+self.format).exists()):
            with open(config_dir+"/"+file_name+self.format,"w+") as f:
                f.close()
        with open(config_dir+"/"+file_name+self.format,"r+") as f:
            #loads(f.read())

            try:
                self.a=load(f)
            except:
                self.a=dict()

    def __getitem__(self, item):
        if item in self.a.keys():
            return self.a[item]
        else:
            return None
    def __setitem__(self, key, value):
        self.a[key]=value
        with open(self.dir + "/" + self.name + self.format, "w") as f:
            dump(self.a,f)

class StyleSheet():
    def __init__(self,path,window):
        self.stylesheet_str=open(path,"r+").read()
        self.style=dict()
        self.window=window
    def process(self):
        current=None
        for i in self.stylesheet_str.split("\n"):
            if "{" in i:
                current=i.replace(" ","").replace("{","")
                self.style[current]=dict()
            elif current!=None:
                if ":" in i:
                    id,val=i.split(":")
                    if "RGB" in val:
                        val=RGB(*list(map(int,val.replace("RGB(","").replace(");","").split(","))))
                    elif "%" in val or "vh" in val or "vw" in val or "px" in val:
                        val=Size(val,window=self.window)
                    self.style[current][id.replace(" ","")]=val
                if "}" in i:
                    current=None
class Shader():
    def __init__(self, path, window):
            self.shader_code = open(path, "r+").read()
            self.logic_blocks = """"""
            self.window = window
            self.shader_Keywords={"foreach": "for"," from ":" in ","Omnilight":"TopViewOmni","System":"self"," is ":"==",":=":"="}
    def process(self):
            current = None
            for i in self.shader_code.split("\n"):
               if "#" in i:
                   ni=i.split("#")[0]
               else:
                  ni=i
               ni=ni.replace("->",".").replace("{",":").replace("}","").replace(";","")
               for key,val in self.shader_Keywords.items():
                   ni=re.sub(key,val,ni)
               for i in re.findall("\[.*\.\..*:.*\]",ni):
                   ni=ni.replace(i,i.replace("[","alqrange(").replace("..",",").replace(":",",").replace("]",")"))
               self.logic_blocks+=ni+"\n"


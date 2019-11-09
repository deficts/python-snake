import math
import random
import tkinter as tk
from tkinter import messagebox
import pygame

class cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    def move(self,dirnx,dirny):
        pass
    def draw(self,surface,eyes=False):
        pass

class snake(object):
    def __init__(self,color,pos):
        pass
    def move(self):
        pass
    def reset(self,pos):
        pass
    def addCube(self):
        pass
    def draw(self,surface):
        pass

def redrawWindow(surface):
    global width, rows
    surface.fill((0,0,0))
    pygame.display.update()

def randomSnack(rows,items):
    pass

def message_box(subject,content):
    pass

def main():
    global width, rows
    width=500
    rows=20
    win=pygame.display.set_mode((width,width))
    flag=True
    clock=pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

    redrawWindow(win)
    pass

main()

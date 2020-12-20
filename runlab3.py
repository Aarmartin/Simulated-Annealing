#!/usr/bin/env python3
## 
## chessboard display based on FunChess written by Andrew Lamoureux
##

from tkinter import *
import threading
import time
import random
import numpy as np
import math
import base64

from queens import *

DARK_SQUARE_COLOR = '#58ae8b'
LIGHT_SQUARE_COLOR = '#feffed'


#IMAGE = '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'


class ChessEnvironment(object):
    def __init__(self,tk_root,N):
        self.root = tk_root
        self.runEvent = threading.Event()
        self.runEvent.clear()
        
        ## Set up canvas for drawing board
        self.canvas = Canvas( self.root, width=500, height=500 )
        self.canvas.place(x=0,y=0)
        self.canvas.img=PhotoImage(file='blackq.gif')
        self.alive = True
        self.running = False
        
        ## Default parameters
        self.maxsteps = IntVar(value=1000)
        self.starttemp = IntVar(value=1000)
        self.coolmode = StringVar(value='none')
        
        squareWidth=500/N
        squareHeight=500/N
        for ridx, rname in enumerate(list('87654321')):
            for fidx, fname in enumerate(list('abcdefgh')):
                tag = fname + rname
                color = [LIGHT_SQUARE_COLOR, DARK_SQUARE_COLOR][(ridx-fidx)%2]
                shade = ['light', 'dark'][(ridx-fidx)%2]

                tags = [fname+rname, shade, 'square']

                self.canvas.create_rectangle(
                    fidx*squareWidth, ridx*squareHeight,
                    fidx*squareWidth+squareWidth, ridx*squareHeight+squareHeight,
outline=color, fill=color, tag=tags)
    
                
        self.control = Frame(self.root, width=200, height=300)
        self.control.place(x=510,y=10)
        Button(self.control, text="Exit", command=self.finish).pack(anchor=W,fill=X)
        bframe = Frame(self.control)
        bframe.pack(anchor=W,fill=X)

        ## Keep track of widgets
        self.inputWidgets = []
        self.SAWidgets = []
        self.HCWidgets = []
        
        self.runButton = Button(bframe, text="Run", command=self.go)
        self.runButton.grid(row=0,column=0)
        self.inputWidgets.append(self.runButton)

        self.stopButton = Button(bframe, text="Stop", command=self.stop)
        self.stopButton.grid(row=0,column=1)

        self.clearButton = Button(bframe, text="Clear", command=self.clear)
        self.clearButton.grid(row=0,column=2)
        self.inputWidgets.append(self.clearButton)


        self.coolModeButtons = [Radiobutton(self.control, text="No cooling", variable=self.coolmode, value='none'),
                                Radiobutton(self.control, text="Linear cooling", variable=self.coolmode, value='linear'),
                                Radiobutton(self.control, text="Logarithmic cooling", variable=self.coolmode, value='logarithmic')]


        for i in range(len(self.coolModeButtons)):
            self.inputWidgets.append(self.coolModeButtons[i])
            self.coolModeButtons[i].pack(anchor=W)
            

        self.control.params = Frame(self.control,width=200, height=100,bd=1,relief=SUNKEN)
        self.control.params.pack(anchor=W)


        tf ='Helvetica 10 bold italic'
        Label(self.control.params,text="Parameters",relief=FLAT,font=tf).grid(row=0,column=0,columnspan=2,sticky=W+E)        
        ### STEPS
        Label(self.control.params,text="max steps:").grid(row=1,column=0,sticky=E)
        self.control.params.maxsteps = Spinbox(self.control.params, from_= 1, to = 100000, width = 6,textvariable=self.maxsteps)
        self.inputWidgets.append(self.control.params.maxsteps)
        self.control.params.maxsteps.grid(row=1,column=1,sticky=W)
        

        Label(self.control.params,text="start temp:").grid(row=2,column=0,sticky=E)
        self.control.params.starttemp = Spinbox(self.control.params, from_= 1, to = 1000, width = 5,textvariable=self.starttemp)
        self.control.params.starttemp.grid(row=2,column=1,sticky=W)
        self.inputWidgets.append(self.control.params.starttemp)

        self.messageArea = Text(self.root,width=30,height=4,bd=1,relief=SUNKEN)
        self.messageArea.place(x=510,y=310)


    def go(self):
        self.runEvent.set()

    def stop(self):
        self.running=False
        
    def disableInputWidgets(self):
        for w in self.inputWidgets:
            w.config(state=DISABLED)

    def enableInputWidgets(self):
        for w in self.inputWidgets:
            w.config(state=NORMAL)
        
    def clear(self):
        self.canvas.delete('piece')
        self.message('Ready')
        
    def finish( self ):
        self.alive=False
        self.runEvent.set() ## signal waiting thread
        self.root.destroy()

    def message(self, msg):
        self.messageArea.config(state=NORMAL)
        self.messageArea.delete(1.0,END)
        self.messageArea.insert(END,msg)
        self.messageArea.config(state=DISABLED)


    def display(self,board):
        """Display the board."""
        if self.alive:
            self.canvas.delete('piece')
            for r in range(len(board.queens)):
                for c in range(len(board.queens)):
                    if board.queens[c] == r:
                        self.canvas.create_image(r*(500/len(board.queens)) + 250/len(board.queens),c*(500/len(board.queens))+250/len(board.queens),image=self.canvas.img,tag='piece')
            self.canvas.update_idletasks()
            self.canvas.update()

class App(threading.Thread):
    def __init__(self,environment):
        self.environment = environment
        threading.Thread.__init__(self)
        self.start()

    def run(self):                
        self.environment.clear()
        while True:
            ## Wait for run signal
            if not self.environment.runEvent.is_set(): self.environment.runEvent.wait()
            ## Was the environment destroyed while we were waiting?
            if not self.environment.alive: return
            ## Reset for next time
            self.environment.runEvent.clear()

            ## Disable input
            self.environment.disableInputWidgets()
            self.environment.running=True
            steps = simulated_annealing(self.environment)
            self.environment.running=False
            ## Was the environment destroyed while we were running?
            if not self.environment.alive:
                print('DEBUG: environment destroyed while running')
                return


            self.environment.enableInputWidgets()
                
                                                                   
            

if __name__ == '__main__':
    ## Initialize environemnt
    root = Tk()
    root.title( "N-Queens" )
    root.geometry( "800x500" )
    #root.attributes('-type', 'dialog')


    env = ChessEnvironment(root,8)
    app = App(env)    
    root.mainloop()
    app.join()



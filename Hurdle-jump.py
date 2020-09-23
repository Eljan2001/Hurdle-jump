from tkinter import*
import time
import random
root=Tk()
canvas=Canvas(root, width=500, height=500)
canvas.pack()
z=0
variable=0
L=[0]



canvas.create_text(245, 50, text='Score:', font=('Times', 30), fill='red')
class Ball:

    def __init__(self, canvas, variable, ground):
        self.canvas=canvas
        self.ground=ground
        self.id=canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, 100, 250)
        self.x=0
        self.y=0
        self.gravity=0.1
        self.canvas.bind_all('<KeyPress-space>', self.jump)
        
        self.variable=variable
        self.id3=canvas.create_text(320, 50, text=L[0], font=('Times', 30), fill='red')
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        
        pos=self.canvas.coords(self.id)
        obstacle_pos=self.canvas.coords(self.ground.id2)
        
        if pos[2]>=obstacle_pos[0] and pos[0]<=obstacle_pos[2]:
            if pos[3]>=obstacle_pos[1]:
                root.destroy()
                root1=Tk()
                canvas1=Canvas(root1, width=500, height=500)
                canvas1.pack()
                canvas1.create_text(245, 150, text='Game Over', font=('Times', 30), fill='red')
                canvas1.create_text(245, 200, text='Your score is:'+str(L[0]), font=('Times', 30), fill='red')
                root1.mainloop()
        elif pos[0]>obstacle_pos[2] and pos[2]<=obstacle_pos[2]+18:
            canvas.delete(self.id3)
            L[0]+=10
            self.id3=canvas.create_text(320, 50, text=L[0], font=('Times', 30), fill='red')
        if self.y!=0:
            
            self.y+=self.gravity
                
            if pos[3]>=275:
                self.y=0
                self.variable=0
        
    def jump(self, evt):
        
        if self.variable==0:
            self.y=-4
        self.variable+=1
    
        
class Ground:

    def __init__(self, canvas):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0, 275, 500, 500, fill='#522915')
        self.id2=canvas.create_rectangle(530, 220, 540, 275, fill='green')
        
        self.x=-2
    def draw(self):
        self.canvas.move(self.id2, self.x,0)
        pos=self.canvas.coords(self.id2)
        if pos[0]<=200:
            if pos[0]<=0:
                canvas.delete(self.id2)
                self.id2=canvas.create_rectangle(500, 220, 510, 275, fill='green')
    
        
ground=Ground(canvas)      
ball=Ball(canvas, variable, ground)

while 1:
    ground.draw()
    ball.draw()
    root.update()
    root.update_idletasks()
    time.sleep(0.01)
root.mainloop()

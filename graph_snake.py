'''
AsAdbEk_Sotiboldiyev
'''
from tkinter import *
from random import randint

root=Tk()
root.title("Snake Game")
root.config(bg="aqua")

cords=[[0,0],[0,1]]
cor=[0,1]
target=[8,5]
res=False
bal=0

lst=[
    ["[ ]","[ ]","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","( )","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
    ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "],
]
def main(event):
	global target,res,key,bal
	KEYS=["Up","Down","Left","Right"]
	if event.keysym in KEYS and not res:
		avval=cords[0].copy()
		key=event.keysym

		if key=="Up":
			cor[0]-=1
			if cor[0]<0:
				cor[0]=len(lst)-1
		elif key=="Down":
			cor[0]+=1
			if cor[0]>len(lst)-1:
				cor[0]=0
		elif key=="Left":
			cor[1]-=1
			if cor[1]<0:
				cor[1]=len(lst[cor[0]])-1
		elif key=="Right":
			cor[1]+=1
			if cor[1]>len(lst[cor[0]])-1:
				cor[1]=0
		if cor in cords:
			res=True
		cords.append(cor.copy())
		lst[avval[0]][avval[1]]="  "

		lst[cords[-1][0]][cords[-1][1]]="[ ]"

		if target==cords[-1]:
			while True:
				target=[randint(0,len(lst)-1),randint(0,len(lst[cor[0]])-1)]
				if not target in cords:
					break
			lst[target[0]][target[1]]="( )"
			bal+=1
			ball.config(text=f"Ball: {bal}")
		else:
			cords.remove(cords[0])
		
		if res:
		    print("game over")
		    lst[cords[-1][0]][cords[-1][1]]="{ }"
		    result.config(text="GAME OVER",font=("sans-serif",30),bg="red")    

		for i in range(len(lst)):
			for j in range(len(lst[i])):
				color="orange"
				if lst[i][j]=="{ }":
					color="red"
				elif lst[i][j]=="[ ]":
					color="green"
				elif lst[i][j]=="( )":
					color="red"
				px_list[i][j].config(bg=color,text=lst[i][j])


game_place=Frame(root,bd=10,width=200,height=200,relief=SOLID)
game_place.pack()
px_list=[]
for i in range(len(lst)):
	px_list_0=[]
	for j in range(len(lst[i])):
		color="orange"
		if lst[i][j]=="[ ]":
			color="green"
		elif lst[i][j]=="( )":
			color="red"
		px_list_0.append(Label(game_place,bg=color,width=2,text=lst[i][j],font=("sans-serif",20)))
	px_list.append(px_list_0)
for i in range(len(lst)):
	for j in range(len(lst[i])):

		px_list[i][j].grid(row=i+1,column=j+1)

frame=Frame(root,bg="aqua")
frame.pack()

result=Label(frame,bg="aqua")
result.pack(side=LEFT)

ball=Label(frame,bg="blue",fg="white",text=f"Ball: {bal}",font=("sans-serif",30))
ball.pack(side=RIGHT)

root.bind("<Key>",main)
root.mainloop()
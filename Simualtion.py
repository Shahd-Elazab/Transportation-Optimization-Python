#The turtle’s speed lies in the range from 0 to 10.
#If input is a number greater than 10 , speed is set to 0.
#If input is a number smaller than or equal 0.5 , speed is set to 0.
#Negative values make the speed very fast.
#turtle's speed is increasing gradually from 0.6 to 10.
#‘fastest’ :  0
#‘fastest’ :  10
#‘normal’  :  6
#‘slow’    :  3
#‘slowest’ :  1
from playsound import playsound
import turtle
shahd = turtle.Turtle()
shahd.color("red")
x = str(input("Vote here whether the main street is busy or not :"))
def speedofshahd(y):
    if y > 6 or y <= 0.5 :
        playsound('speedalarm.wav')
        print("You have exceeded the speed limit. You must reduce your speed.")
    else: 
        if x=="busy":
            print("You must take the other street because the main street is busy.")
            shahd.forward(100)
            shahd.right(90)
            shahd.forward(200)
            shahd.right(90)
            shahd.forward(70)
        else:
            print("You can take the main street because it isn't busy now.")
            shahd.right(180)
            shahd.forward(100)
            shahd.left(90)
            shahd.forward(200)
            shahd.left(90)
            shahd.forward(70)
    
z=float(input("Enter your speed here : "))
speedofshahd(z)   
turtle.mainloop()

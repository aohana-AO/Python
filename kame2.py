from turtle import *
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(1000):
    color(col[i])
    circle(120)
    circle(100)
    circle(60)
    circle(20)
    left(70)
    for i in range(5):
        color(col[1])
        forward(200)
        left(144)
    
done()


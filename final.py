from visual import *

initialx = 25

floor = box(pos=(0, 0, 0), length=100, height=0.5, width=50, color=color.green)

wall1 = box(pos=(0, 0, 25), length=100, height=1, width=1, color=color.red)
wall2 = box(pos=(0, 0, -25), length=100, height=1, width=1, color=color.red)
wall1short = box(pos=(50, 0, 0), length=1, height=1, width=50, color=color.red)
wall2short = box(pos=(-50, 0, 0), lenght=1, height=1, width=50, color=color.red)

ball1 = sphere( pos=(0, 1, 0), radius =1, color = color.yellow)
ball2 = sphere( pos=(1, 1, 1), radius =1, color = color.blue)
ball3 = sphere( pos=(1, 1, -1), radius =1, color = color.red)
ball4 = sphere( pos=(2, 1, -2), radius =1, color = color.cyan)
ball5 = sphere( pos=(2, 1, 0), radius =1, color = color.orange)
ball6 = sphere( pos=(2, 1, 2), radius =1, color = color.green)
ball7 = sphere( pos=(3, 1, -3), radius =1, color = color.magenta)
ball8 = sphere( pos=(3, 1, -1), radius =1, color = color.black)
ball9 = sphere( pos=(3, 1, 1), radius =1, color = color.yellow, opacity = 0.9)
ball10 = sphere( pos=(3, 1, 3), radius =1, color = color.blue, opacity = 0.9)
ball11 = sphere( pos=(4, 1, -4), radius =1, color = color.red, opacity = 0.9)
ball12 = sphere( pos=(4, 1, -2), radius =1, color = color.cyan, opacity = 0.9)
ball13 = sphere( pos=(4, 1, 0), radius =1, color = color.orange, opacity = 0.9)
ball14 = sphere( pos=(4, 1, 2), radius =1, color = color.green, opacity = 0.9)
ball15 = sphere( pos=(4, 1, 4), radius =1, color = color.magenta, opacity = 0.9)
cueBall = sphere( pos=(-initialx, 1, 0), radius =1, color = color.white, make_trail = true)

hole1 = sphere( pos=(0, 0, 23), radius =2, color = color.black)
hole2 = sphere( pos=(0, 0, -23), radius =2, color = color.black)
hole3 = sphere( pos=(48, 0, 23), radius =2, color = color.black)
hole4 = sphere( pos=(-48, 0, 23), radius =2, color = color.black)
hole5 = sphere( pos=(48, 0, -23), radius =2, color = color.black)
hole6 = sphere( pos=(-48, 0,- 23), radius =2, color = color.black)
###loop across all balls in a list to make their velocities equal to zero.

ballList = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12, ball13, ball14, ball15]

def cueBallout(n):
    """lets one know if a ball is in or out"""
    if hole1.pos.x + 1 >= n.pos.x and n.pos.x >= hole1.pos.x - 1 and \
       hole1.pos.z + 1 >= n.pos.z and n.pos.z >= hole1.pos.z - 1:
        return True
    if hole2.pos.x + 1 >= n.pos.x and n.pos.x >= hole2.pos.x - 1 and \
       hole2.pos.z + 1 >= n.pos.z and n.pos.z >= hole2.pos.z - 1:
        return True
    if hole3.pos.x + 1 >= n.pos.x and n.pos.x >= hole3.pos.x - 1 and \
       hole3.pos.z + 1 >= n.pos.z and n.pos.z >= hole3.pos.z - 1:
        return True
    if hole4.pos.x + 1 >= n.pos.x and n.pos.x >= hole4.pos.x - 1 and \
       hole4.pos.z + 1 >= n.pos.z and n.pos.z >= hole4.pos.z - 1:
        return True
    if hole5.pos.x + 1 >= n.pos.x and n.pos.x >= hole5.pos.x - 1 and \
       hole5.pos.z + 1 >= n.pos.z and n.pos.z >= hole5.pos.z - 1:
        return True
    if hole6.pos.x + 1 >= n.pos.x and n.pos.x >= hole6.pos.x - 1 and \
       hole6.pos.z + 1 >= n.pos.z and n.pos.z >= hole6.pos.z - 1:
        return True
    else:
        return False

def gameBallout(n):
    """lets one know if a regular game ball is in or out"""
    if hole1.pos.x + 1 >= n.pos.x and n.pos.x >= hole1.pos.x - 1 and \
       hole1.pos.z + 1 >= n.pos.z and n.pos.z >= hole1.pos.z - 1:
        return True
    if hole2.pos.x + 1 >= n.pos.x and n.pos.x >= hole2.pos.x - 1 and \
       hole2.pos.z + 1 >= n.pos.z and n.pos.z >= hole2.pos.z - 1:
        return True
    if hole3.pos.x + 1 >= n.pos.x and n.pos.x >= hole3.pos.x - 1 and \
       hole3.pos.z + 1 >= n.pos.z and n.pos.z >= hole3.pos.z - 1:
        return True
    if hole4.pos.x + 1 >= n.pos.x and n.pos.x >= hole4.pos.x - 1 and \
       hole4.pos.z + 1 >= n.pos.z and n.pos.z >= hole4.pos.z - 1:
        return True
    if hole5.pos.x + 1 >= n.pos.x and n.pos.x >= hole5.pos.x - 1 and \
       hole5.pos.z + 1 >= n.pos.z and n.pos.z >= hole5.pos.z - 1:
        return True
    if hole6.pos.x + 1 >= n.pos.x and n.pos.x >= hole6.pos.x - 1 and \
       hole6.pos.z + 1 >= n.pos.z and n.pos.z >= hole6.pos.z - 1:
        return True
    else:
        return False

def yeezys():
    """The yeezys function initiates the velocity of the cue ball."""
    m = scene.mouse.getclick()
    temp =  scene.mouse.project(normal = (0,1,0), point = (0,1,0))
    print(temp)
    gamma = temp - cueBall.pos
    print gamma
    cueBall.velocity = 0.1*gamma
    print(cueBall.velocity)
    return cueBall.velocity

def inTablex(ballposx):
    """This function makes sure the balls are outside
    of the frame of the pool table for the x coordinate
    """
    if ballposx < -49 or ballposx > 49:
        return True
    else:
        return False
    return False


def inTablez(ballposz):
    """This function makes sure the balls are outside of
    the frame of the pool table for the z coordinate
    """
    if ballposz < - 24 or ballposz > 24:
        return True
    else:
        return False
    return False

def ballContact( ballin, ballout):
    if ballin.pos.x -1 <= ballout.pos.x <= ballin.pos.x and ballin.pos.z -1 <= ballout.pos.z <= ballin.pos.z:
        ballout.velocity = ballin.velocity
        ballin.velocity = ballin.velocity *(-1)
        
def countBalls( j , i):
    if i.pos == (0,-5,0):
        j +=1
    return j
    
#These variables will initialize the game
GameOver = False
j = 0

while GameOver == False:
    t = 0.0
    dt = 0.5
    cueBall.velocity = yeezys()
    for ball in ballList:
        ball.velocity = vector(0,0,0)
    while dt > 0.1:
        sleep (0.01)
        t = t + dt
        dt = dt - dt/20
        if  inTablez(cueBall.pos.z) == True:
            cueBall.velocity.z = cueBall.velocity.z*(-1)
        if inTablex(cueBall.pos.x) == True:
            cueBall.velocity.x = cueBall.velocity.x*(-1)
        cueBall.pos += cueBall.velocity*dt #(cueBall.pos/cueBall.mass)*dt
        print(cueBall.pos)
        for ball in range(len(ballList)):
            highball = ball +1
            lowball = ball-1
            if cueBall.pos.x - 1 <= ballList[ball].pos.x <= cueBall.pos.x + 1 and cueBall.pos.z - 1 <= ballList[ball].pos.z <= cueBall.pos.z + 1:
                ballList[ball].velocity = cueBall.velocity
                cueBall.velocity = (-1)*cueBall.velocity
            if  inTablez(ballList[ball].pos.z) == True:
                ballList[ball].velocity.z = ballList[ball].velocity.z*(-1)
            if inTablex(ballList[ball].pos.x) == True:
                ballList[ball].velocity.x = ballList[ball].velocity.x*(-1)
            while lowball > 0:
                ballContact(ballList[ball], ballList[lowball])
                lowball = lowball - 1
            while highball < len(ballList):
                ballContact(ballList[ball], ballList[highball])
                highball = highball +1
            ballList[ball].pos += ballList[ball].velocity*dt
            if gameBallout(ballList[ball]) == True:
                ballList[ball].pos = (0,-5,0)
                ballList[ball].velocity = (0,0,0)
                ballList[ball].color = color.black
                del ballList[ball]
                break
        if cueBallout(cueBall) == True:          
            cueBall.pos = (-initialx, 1, 0)
            cueBall.velocity = (0,0,0)
            break #make sure this break is always here.
    if ball8.pos == (0,-5,0):
        GameOver = True
    for i in ballList:
        countBalls( j , i)
    if j == 14:
        GameOver = True


    
       
        

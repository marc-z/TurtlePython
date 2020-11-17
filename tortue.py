import ipyturtle

global current
current = None

def ouvre_tableau(largeur=500, longueur=500):
    global current
    current = ipyturtle.Turtle(largeur, longueur)
    return current

def avance(longueur):
    current.forward(longueur)

def recule(longueur):
    current.back(longueur)

def couleur(r,g,b):
    current.pencolor(r,g,b)

def rouge():
    couleur(255,0,0)

def vert():
    couleur(0,255,0)

def bleu():
    couleur(0,0,255)

def leve_crayon():
    current.penup()

def pose_crayon():
    current.pendown()

def tourne(angle):
    current.left(angle)

def efface():
    current.reset()

def va(x,y):
    leve_crayon()
    a,b = current.position()
    angle = current.heading()
    tourne(-angle)
    avance(x-a)
    tourne(90)
    avance(y-b)
    tourne(-90+angle)
    pose_crayon()

def angle(a):
    tourne(a-current.heading())

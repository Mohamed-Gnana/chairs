from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def MyInit():
    glMatrixMode(GL_PROJECTION)
    #glortho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)

def chair():
    glPushMatrix()
    glScale(2.5,.5,2)
    glutWireCube(1)
    glLoadIdentity()
    glPopMatrix()
    glPushMatrix()
    glColor(0,0,0)
    glTranslate(0,1.5,-1)
    glScale(2.5,3,.5)
    glutWireCube(1)
    glLoadIdentity()
    glPopMatrix()
    glPushMatrix()
    glTranslate(1.25,-.5,1)
    glScale(.5,2,.5)
    glutWireCube(1)
    glLoadIdentity()
    glPopMatrix()
    glPushMatrix()
    glTranslate(-1.25+.5,-.5,1)
    glScale(.5,2,.5)
    glutWireCube(1)
    glLoadIdentity()
    glPopMatrix()
    glPushMatrix()
    glTranslate(1.25,-.5,-1+.5)
    glScale(.5,2,.5)
    glutWireCube(1)
    glLoadIdentity()
    glPopMatrix()
    glPushMatrix()
    glTranslate(-1.25+.5,-.5,-1+.5)
    glScale(.5,2,.5)
    glutWireCube(1)
    glPopMatrix()



def draw():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,0,0)
    chair()
    glLoadIdentity()
    glTranslate(5,0,0)
    chair()
    glLoadIdentity()
    glTranslate(-5,0,0)
    chair()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Chairs")
glutDisplayFunc(draw)
MyInit()
glutMainLoop()

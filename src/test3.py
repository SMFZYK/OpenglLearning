# -*- coding utf-8 -*-
# 作者: SMF
# 时间: 2022.12.23


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xx = 0
yy = 0
zz = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)

    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 10.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.0, 0.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))

    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.0, 0.5, 0.0, 0.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.0, 0.5, 0.0, 0.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 0.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_EMISSION, (0.0, 0.0, 0.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 30.0)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glColor3f(1.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotatef(xx, 1.0, 0.0, 0.0)
    glRotatef(yy, 0.0, 1.0, 0.0)
    glRotatef(zz, 0.0, 0.0, 1.0)
    glutSolidTeapot(1.3)
    glPopMatrix()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w / h, 1.0, 20.0)



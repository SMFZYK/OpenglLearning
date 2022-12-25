# -*- coding utf-8 -*-
# 作者: SMF
# 时间: 2022.12.23

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x = 0
f = True
z = 0
angl = 0

x_camera = 10
y_camera = 10
z_camera = 10


def myInit():
    global x_camera
    global y_camera
    global z_camera
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(72, 1, 1, 200)  # Fovy值在0-180的范围内，值越大，感觉物体越远，值越小，感觉物体越近；
    gluLookAt(x_camera, y_camera, z_camera,
              0, 0, 0,
              0, 4, 0)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)


def draw():
    global x
    global f
    global z
    global angl
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.2, 0.2, 0.2, 0.2)

    glColor3f(0.8, 0.8, 0.5)
    glBegin(GL_POLYGON)
    glVertex(100, 0, 5)
    glVertex(100, 0, -5)
    glVertex(-100, 0, -5)
    glVertex(-100, 0, 5)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-2, 0, 0.5)
    glVertex(-2, 0, -0.5)
    glVertex(2, 0, -0.5)
    glVertex(2, 0, 0.5)
    glEnd()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Moving Car")
    myInit()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == '__main__':
    main()

# -*- coding utf-8 -*-
# 作者: SMF
# 时间: 2022.12.22


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display1():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(50.0)
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.5, 0.5)
    glEnd()
    glFlush()


def display2():
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(2, 0x0F0F)
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.5, 0.5)
    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("An Opengl Programming")
    glutDisplayFunc(display2)
    glutMainLoop()


if __name__ == '__main__':
    main()

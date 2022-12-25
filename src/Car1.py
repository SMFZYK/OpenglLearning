# -*- coding utf-8 -*-
# 作者: SMF
# 时间: 2022.12.23


from math import *
import pygame

import numpy as s
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(72, 1, 1, 200)
    gluLookAt(8, 8, 8,
              0, 0, 0,
              0, 5, 0)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)


def circle(r):
    glColor3f(1, 1, 1)

    for cita in s.arange(0, 2 * 3.14, 0.001):
        a = r * cos(cita)
        b = r * sin(cita)
        glVertex(a, b)


x = 0
f = True
z = 0
angl = 0


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
    #
    # glTranslate(5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-10, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glTranslate(-5, 0, 0)
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # glLoadIdentity()
    # glTranslate(10, 0, 0)
    #
    # glBegin(GL_POLYGON)
    # glVertex(-2, 0, 0.5)
    # glVertex(-2, 0, -0.5)
    # glVertex(2, 0, -0.5)
    # glVertex(2, 0, 0.5)
    # glEnd()
    #
    # # 绘制小车
    # glLoadIdentity()  # 恢复初始坐标系
    # glColor3f(1, 1, 1)
    # glTranslate(-2.5 + x, -0.5 * 5 * 0.25, -1.25)  # 平移矩阵
    # glRotate(z, 0, 0, 1)  # 旋转变换
    # glutSolidTorus(0.125, 0.5, 7, 10)
    #
    # glLoadIdentity()
    # glTranslate(2.5 + x, -0.5 * 5 * 0.25, -1.25)
    # glRotate(z, 0, 0, 1)
    # glutSolidTorus(0.125, 0.5, 7, 10)
    # glLoadIdentity()
    #
    # glLoadIdentity()
    # glColor3f(0, 1, 0)
    # glScale(1, 0.25, 0.5)  # 模型缩放
    # glTranslate(x, 0, 0)
    # glutSolidCube(5)
    #
    # glColor3f(0, 1, 0)
    # glTranslate(2.5, 0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    # glutSolidSphere(0.3, 100, 100)
    # glTranslate(-2.5, -0.5 * 0.25 * 5, -0.5 * 0.5 * 5)
    # glTranslate(2.5, 0.5 * 0.5 * 5, - 0.5 * 0.5 * 5)
    # glutSolidSphere(0.3, 100, 100)
    # glTranslate(-2.5, -0.5 * 0.5 * 5, 0.5 * 0.5 * 5)
    # glTranslate(3, 0.5 * 0.3 * 5, 0)
    #
    # # glBegin(GL_POLYGON)
    # # glVertex(0, 0, 2)
    # # glVertex(0, 0, -2)
    # # glVertex(2, 0, -6)
    # # glVertex(2, 0, 6)
    # # glEnd()
    #
    # glTranslate(-3, -0.5 * 0.3 * 5, 0)
    # glColor3f(1, 1, 1)
    # glTranslate(0, 5, 0)
    # glScale(0.5, 1, 1)
    # glutSolidCube(5)
    # glLoadIdentity()
    #
    # glColor3f(1, 1, 1)
    # glTranslate(2.5 + x, 0.5 * 5 * -0.25, 1.25)
    # glRotate(z, 0, 0, 1)
    # glutSolidTorus(0.125, 0.5, 7, 10)
    #
    # glLoadIdentity()
    # glTranslate(-2.5 + x, -0.5 * 5 * 0.25, 1.25)
    # glRotate(z, 0, 0, 1)
    # glutSolidTorus(0.125, 0.5, 7, 10)
    #
    # glLoadIdentity()
    # glTranslate(x, 2.7, 0)
    # glColor3f(1, 0, 0)
    # glutSolidCylinder(0.2, 0.2, 1000, 5)
    # glRotate(angl, 0, 1, 0)
    #
    # glBegin(GL_POLYGON)
    # glColor3f(1, 0, 0)
    # glVertex(0.7, 0, 0.7)
    # glVertex(-0.7, 0, 0.7)
    # glVertex(-1, 0, 3)
    # glVertex(1, 0, 3)
    # glEnd()
    #
    # glBegin(GL_POLYGON)
    # glColor3f(1, 0, 0)
    # glVertex(-0.7, 0, - 0.7)
    # glVertex(0.7, 0, -0.7)
    # glVertex(1, 0, - 3)
    # glVertex(-1, 0, -3)
    # glEnd()
    #
    # # glLoadIdentity()
    #
    # # DrawXYZ()
    #
    glutSwapBuffers()
    # if x > 7:
    #     f = False
    #
    # if x < -7:
    #     f = True
    #
    # if f:
    #     x += .04
    #     z -= .1
    # else:
    #     x -= .04
    #     z += .1
    # angl += .3


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    # glutInitWindowPosition(800, 400)
    glutCreateWindow(b"Moving Car")
    myInit()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == '__main__':
    main()

# -*- coding utf-8 -*-
# 作者: SMF
# 时间: 2022.12.22

"""
OpenGL在处理光照时采用这样一种近似：把光照系统分为三部分，分别是光源、材质和光照环境。
光源就是光的来源，可以是前面所说的太阳或者电灯等。材质是指接受光照的各种物体的表面，
由于物体如何反射光线只由物体表面决定（OpenGL中没有考虑光的折射），材质特点就决定了物体反射光线的特点。
光照环境是指一些额外的参数   ，它们将影响最终的光照画面，比如一些光线经过多次反射后，已经无法分清它究竟是由哪个光源发出，
这时，指定一个“环境亮度”参数，可以使最后形成的画面更接近于真实情况。
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xx = 0.0
yy = 0.0
zz = 0.0


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
    glColor3f(1.0, 1.0, 1.0)
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


def keyboard(key, x, y):
    global xx
    global yy
    global zz
    if key == 'x':
        xx = (xx + 5) % 360
        glutPostRedisplay()
    elif key == 'X':
        xx = (xx - 5) % 360
        glutPostRedisplay()
    elif key == 'y':
        yy = (yy + 5) % 360
        glutPostRedisplay()
    elif key == 'Y':
        yy = (yy - 5) % 360
        glutPostRedisplay()
    elif key == 'z':
        zz = (zz + 5) % 360
        glutPostRedisplay()
    elif key == 'Z':
        zz = (zz - 5) % 360
        glutPostRedisplay()
    else:
        pass


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("An Opengl Programming on Lighting")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == '__main__':
    main()

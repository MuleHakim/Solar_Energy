import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from math import *


def draw_circle1(posx, posy, radius):
    sides = 32
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


def init():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.6, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(10, -10)
    glVertex2f(10, 10)
    glVertex2f(-10, 10)
    glVertex2f(-10, -10)
    glEnd()

    glColor3f(0.5, 0.7, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(10, 0)
    glVertex2f(10, 10)
    glVertex2f(-10, 10)
    glVertex2f(-10, 0)
    glEnd()
    # hotel
    glColor3f(0.0, 0.71, 0.58)
    # glColor3f(0.50, 0.71, 0.98)
    glBegin(GL_POLYGON)

    glVertex2f(5.50, -4.00)
    glVertex2f(5.50, 3.30)
    glVertex2f(9.50, 3.30)
    glVertex2f(9.50, -4.00)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0, 0, 0)
    glVertex2f(9.50, 3.30)
    glVertex2f(5.50, 3.30)
    glVertex2f(5.70, 3.70)
    glVertex2f(9.80, 3.70)

    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(9.50, -4.00)
    glVertex2f(9.50, 3.30)
    glVertex2f(9.80, 3.70)
    glVertex2f(9.80, -3.70)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(6.50, 2.70)
    glVertex2f(6.50, 3.30)
    glVertex2f(8.50, 3.30)
    glVertex2f(8.50, 2.70)

    glEnd()

    # window

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.50, -2.00)
    glVertex2f(8.50, -1.1)
    glVertex2f(9.30, -1.1)
    glVertex2f(9.30, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(8.50, 0.5)
    glVertex2f(8.50, -0.4)
    glVertex2f(9.30, -0.4)
    glVertex2f(9.30, 0.5)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(5.70, 0.5)
    glVertex2f(5.70, -0.4)
    glVertex2f(6.50, -0.4)
    glVertex2f(6.50, 0.5)
    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(5.70, -2.00)
    glVertex2f(5.70, -1.1)
    glVertex2f(6.50, -1.1)
    glVertex2f(6.50, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(5.70, 2.00)
    glVertex2f(5.70, 1.1)
    glVertex2f(6.50, 1.1)
    glVertex2f(6.50, 2.00)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.50, 2.00)
    glVertex2f(8.50, 1.1)
    glVertex2f(9.30, 1.1)
    glVertex2f(9.30, 2.00)
    glEnd()

    # door
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.00, -4.00)
    glVertex2f(8.00, -3.20)
    glVertex2f(7.00, -3.20)
    glVertex2f(7.00, -4.00)

    glEnd()

    glColor3f(0.35, 0.0, 0.0)
    glBegin(GL_POLYGON)

    glVertex2f(7.40, -4.20)
    glVertex2f(7.40, -3.00)
    glVertex2f(6.90, -3.20)
    glVertex2f(6.90, -4.00)

    glEnd()

    # hotel2
    glColor3f(0.0, 0.71, 0.58)
    # glColor3f(0.50, 0.71, 0.98)
    glBegin(GL_POLYGON)

    glVertex2f(-9.50, -4.00)
    glVertex2f(-9.50, 3.30)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-5.50, -4.00)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0, 0, 0)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-9.50, 3.30)
    glVertex2f(-9.30, 3.70)
    glVertex2f(-5.30, 3.70)

    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(-5.50, -4.00)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-5.30, 3.70)
    glVertex2f(-5.30, -3.70)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-8.50, 2.70)
    glVertex2f(-8.50, 3.30)
    glVertex2f(-6.50, 3.30)
    glVertex2f(-6.50, 2.70)

    glEnd()

    # window

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-6.50, -2.00)
    glVertex2f(-6.50, -1.1)
    glVertex2f(-5.80, -1.1)
    glVertex2f(-5.80, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(-6.50, 0.5)
    glVertex2f(-6.50, -0.4)
    glVertex2f(-5.80, -0.4)
    glVertex2f(-5.80, 0.5)
    glEnd()
    glBegin(GL_POLYGON)
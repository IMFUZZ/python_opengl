import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


verticies = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1, -1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1, -1,  1),
    (-1,  1,  1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    camera_X = 0.0
    camera_Y = 0.0
    camera_Z = 0.0
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("CUBE")
    #icon_32x32 = pygame.image.load("C:\\Users\\Daniel-Junior\\testpourgit\\poule.jpg").convert_alpha()
    #pygame.display.set_icon(icon_32x32)

    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(camera_X,camera_Y, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    camera_Y = -0.1
                if event.key == pygame.K_UP:
                    camera_Y = 0.1
                if event.key == pygame.K_LEFT:
                    camera_X = -0.1
                if event.key == pygame.K_RIGHT:
                    camera_X = 0.1
            else:
                    camera_X = 0.0
                    camera_Y = 0.0

        glRotatef(0.2, 3, 1, 1)
        glTranslatef(camera_X,camera_Y, camera_Z)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

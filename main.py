import pygame
import random
import numpy as np
import math
pygame.init()

WIDTH, HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Simulation")
WHITE= (255,255,255)
SAND_COLOR=(194, 178, 250)
T=8 #Size of one sand piece

class Grid:
    def __init__(self):
        self.grid=np.zeros((WIDTH*2,HEIGHT+T))
        self.position=[]
    
    #Sand der Liste positions hinzufügen.
    def addSand(self,pointX, pointY):
        #Wenn sich der Mausezeiger innerhalb des Fensters befindet (und geklickt wird)
        if pointX>=0 and pointX<=WIDTH and pointY>=0 and pointY<=HEIGHT:
            if self.grid[pointX][pointY]==0:
                self.grid[pointX][pointY]=1
                self.position.append((pointX,pointY))
    
    def update_position(self):
        for points in self.position:
            listpoints = list(points)
            self.position.remove(points)

            # Überprüfen, ob die Zelle unterhalb der aktuellen Position leer ist
            if points[1] >= HEIGHT - T:
                self.position.append(points)
            
            # Fall: Die Zelle unterhalb der aktuellen Position ist leer
            elif self.grid[points[0]][points[1] + T] == 0:
                # Aktualisiere das Gitter und die Position des Sandpartikels
                self.grid[points[0]][points[1]] = 0
                self.grid[points[0]][points[1] + T] = 1
                listpoints[1] += T
                points = tuple(listpoints)
                self.position.append(points)
            
            # Fall: Die Zelle unterhalb der aktuellen Position ist bereits belegt
            elif self.grid[points[0]][points[1] + T] == 1:
                # Überprüfen der umliegenden Zellen
                if (self.grid[points[0] + T][points[1] + T] == 1) and (self.grid[points[0] - T][points[1] + T] == 1):
                    # Wenn beide umliegenden Zellen belegt sind, behalte die aktuelle Position bei
                    self.position.append(points)
                    
                elif (self.grid[points[0] + T][points[1] + T] == 1) and (self.grid[points[0] - T][points[1] + T] == 0):
                    # Wenn nur die rechte obere Zelle belegt ist, bewege das Sandpartikel nach links oben
                    self.grid[points[0]][points[1]] = 0
                    self.grid[points[0] - T][points[1] + T] = 1
                    listpoints[0] -= T
                    listpoints[1] += T
                    points = tuple(listpoints)
                    self.position.append(points)
                    
                elif (self.grid[points[0] + T][points[1] + T] == 0) and (self.grid[points[0] - T][points[1] + T] == 1):
                    # Wenn nur die linke obere Zelle belegt ist, bewege das Sandpartikel nach rechts oben
                    self.grid[points[0]][points[1]] = 0
                    self.grid[points[0] + T][points[1] + T] = 1
                    listpoints[0] += T
                    listpoints[1] += T
                    points = tuple(listpoints)
                    self.position.append(points)
                    
                else:
                    # Wenn beide umliegenden Zellen leer sind, bewege das Sandpartikel zufällig nach links oder rechts oben
                    self.grid[points[0]][points[1]] = 0
                    a = random.randint(0, 1)
                    if a == 0:
                        a = -1
                    self.grid[points[0] + a * T][points[1] + T] = 1
                    listpoints[0] += a * T
                    listpoints[1] += T
                    points = tuple(listpoints)
                    self.position.append(points)

    
    def draw(self, screen):
        for points in self.position:
            pygame.draw.rect(screen, SAND_COLOR, (points[0],points[1],T,T), 0)       
            #pygame.draw.circle(screen, SAND_COLOR, (points[0],points[1]) , T,3)
                    
                    
    
        


def main():
    run= True
    clock= pygame.time.Clock()
    
    sandbox= Grid()
    
    while run:
        clock.tick(30)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
            
            elif pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                btn=pygame.mouse
                sandbox.addSand(pos[0]-pos[0]%T,pos[1]-pos[1]%T)
        
        sandbox.update_position()
        sandbox.draw(screen)
        
                
               
        pygame.display.update()
    pygame.quit()
    
main()
            
        
                
        
        
    
    
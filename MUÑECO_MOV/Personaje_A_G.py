import pygame
import constantes
class Personaje():
    def __init__(self, x, y, animaciones): #Coordenadas
        self.flit = False
        self.animaciones = animaciones
        #Imagen de la animación que se está mostrando actualmente
        self.frame_index = 0
        
        #Aquí se almacena la hora actual (en milisegundos desde que se inició 'pygame')
        self.update_time = pygame.time.get_ticks()
        
        
        self.image = animaciones[self.frame_index]
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PERSONAJE,
                                 constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y)
    
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flit = True
        if delta_x > 0:
            self.flit = False
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    
    def update (self):
        cooldowm_animacion = 150
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldowm_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
            
    
    def dibujar (self, interfaz): # Es un método
        image_flip = pygame.transform.flip(self.image, self.flit, flip_y = False, )
        interfaz.blit(image_flip, self.forma)
        
        
        #pygame.draw.rect (interfaz, constantes.COLOR, self.forma, width = 1) 
        
        #Dibuja la interfaz o solicita la ventana,
        # se selecciona el color y 
        # se le indíca lo que se quiere dibujar.


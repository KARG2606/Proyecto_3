import pygame
import constantes
from Personaje_A_G import Personaje

pygame.init() 

ventana = pygame.display.set_mode(((1000,600)))

pygame.display.set_caption("Árbol genealógico")

def escalar_img(image, scale):
    W = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, size = (W*scale, h*scale))
    return nueva_imagen

animaciones = []
for img in range(7):
    img = pygame.image.load(f"Datos_características_pygame/imagenes/Player_{img}.png") 
    img = escalar_img (img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)
 

"""
player_image = pygame.image.load("Datos_características_pygame/imagenes/Player_0.png") 
Datos_características_pygame, Imagenes, carácteres, personaje
player_image = escalar_img(player_image,constantes.SCALA_PERSONAJE)
"""

jugador = Personaje(x= 20, y= 20, animaciones = animaciones) 
#Establecemos las coordenadas del personaje

#Definir las variables de movimiento de jugar
mover_izquierda = False #True al oprimir a

mover_derecha = False #True al oprimir d

mover_arriba = False #True al oprimir w

mover_abajo = False #True al oprimir s

#Controlar el frame
reloj = pygame.time.Clock()

run = True
while run == True:
    #velocidad del jugador
    reloj.tick(constantes.FPS)
     
    ventana.fill(constantes.COLOR_BG)
    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0
    
    if mover_izquierda == True:
        delta_x = -constantes.Velocidad

    if mover_derecha == True:
        delta_x = constantes.Velocidad

    if mover_arriba == True:
        delta_y = -constantes.Velocidad  

    if mover_abajo == True:
        delta_y = constantes.Velocidad 
      
    
    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)
    #print(delta_x,delta_y)
    
    jugador.update()
    
    jugador.dibujar(ventana) #Utilizamos el método de jugador
    
    for event in pygame.event.get(): #Salida
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN: #Inicializa las teclas
          if event.key == pygame.K_LEFT:
              mover_izquierda = True 
              
          if event.key == pygame.K_RIGHT:
              mover_derecha = True
              
          if event.key == pygame.K_UP:
              mover_arriba = True
              
          if event.key == pygame.K_DOWN:
              mover_abajo = True
        
        #Al soltarse la tecla
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              mover_izquierda = False 
              
          if event.key == pygame.K_RIGHT:
              mover_derecha = False
              
          if event.key == pygame.K_UP:
              mover_arriba = False
              
          if event.key == pygame.K_DOWN:
              mover_abajo = False        
        
              
    pygame.display.update()
pygame.quit()
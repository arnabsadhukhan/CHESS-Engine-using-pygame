#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import pandas as pd
import numpy as np
import CHESS_PIECES as cp


# In[2]:


pygame.init()

height,weidth = 700,700

#colors===========================================================
white = (255,255,255)
gray = (128,128,128)
black = (0,0,0)
#colors===========================================================


gameDisplay = pygame.display.set_mode((weidth,height))
pygame.display.set_caption('CHESS')
clock = pygame.time.Clock()
crashed = False
font = pygame.font.Font('freesansbold.ttf', 22) 
flag =0 


# information array-------------------------------------------------------------------------------------------
pieces = ['king','queen','bishop1','bishop2','knight1','knight2','rook1','rook2','pawn1','pawn2','pawn3','pawn4',
          'pawn5','pawn6','pawn7','pawn8']
black_pieces = {'king': (8, 'e'),'queen': (8, 'd'),'bishop1': (8, 'c'),'bishop2': (8, 'f'),'knight1': (8, 'b'),
 'knight2': (8, 'g'),'rook1': (8, 'a'),'rook2': (8, 'h'),'pawn1': (7, 'a'),'pawn2': (7, 'b'),'pawn3': (7, 'c'),
 'pawn4': (7, 'd'),'pawn5': (7, 'e'),'pawn6': (7, 'f'),'pawn7': (7, 'g'),'pawn8': (7, 'h')}
black_images = dict()
black_images_loc = ["Chess_kb.png","Chess_qb.png","Chess_bb.png","Chess_bb.png","Chess_knb.png","Chess_knb.png",
                    "Chess_rb.png","Chess_rb.png","Chess_pb.png","Chess_pb.png","Chess_pb.png","Chess_pb.png",
                    "Chess_pb.png","Chess_pb.png","Chess_pb.png","Chess_pb.png"]
j=0
for i in pieces:
    black_images[i] = pygame.image.load(black_images_loc[j])
    j+=1

white_pieces = {'king': (1, 'e'),'queen': (1, 'd'),'bishop1': (1, 'c'),'bishop2': (1, 'f'),'knight1': (1, 'b'),
                'knight2': (1, 'g'),'rook1': (1, 'a'), 'rook2': (1, 'h'),'pawn1': (2, 'a'),'pawn2': (2, 'b'),
                'pawn3': (2, 'c'),'pawn4': (2, 'd'), 'pawn5': (2, 'e'),'pawn6': (2, 'f'),'pawn7': (2, 'g'),'pawn8': (2, 'h')}

white_images = dict()
white_images_loc = ["Chess_kw.png","Chess_qw.png","Chess_bw.png","Chess_bw.png","Chess_knw.png","Chess_knw.png",
                    "Chess_rw.png","Chess_rw.png","Chess_pw.png","Chess_pw.png","Chess_pw.png","Chess_pw.png",
                    "Chess_pw.png","Chess_pw.png","Chess_pw.png","Chess_pw.png"]
j=0
for i in pieces:
    white_images[i] = pygame.image.load(white_images_loc[j])
    j+=1
    
    
black_agents={'king':cp.King(black_pieces['king']),
              'queen':cp.Queen(black_pieces['queen']),
              'bishop1':cp.Bishop(black_pieces['bishop1']),
              'bishop2':cp.Bishop(black_pieces['bishop2']),
              'knight1':cp.Knight(black_pieces['knight1']),
              'knight2':cp.Knight(black_pieces['knight2']),
              'rook1':cp.Rook(black_pieces['rook1']),
              'rook2':cp.Rook(black_pieces['rook2']),
              'pawn1':cp.Pawn(black_pieces['pawn1']),
              'pawn2':cp.Pawn(black_pieces['pawn2']),
              'pawn3':cp.Pawn(black_pieces['pawn3']),
              'pawn4':cp.Pawn(black_pieces['pawn4']),
              'pawn5':cp.Pawn(black_pieces['pawn5']),
              'pawn6':cp.Pawn(black_pieces['pawn6']),
              'pawn7':cp.Pawn(black_pieces['pawn7']),
              'pawn8':cp.Pawn(black_pieces['pawn8'])}

white_agents={'king':cp.King(white_pieces['king'],team='white'),
              'queen':cp.Queen(white_pieces['queen'],team='white'),
              'bishop1':cp.Bishop(white_pieces['bishop1'],team='white'),
              'bishop2':cp.Bishop(white_pieces['bishop2'],team='white'),
              'knight1':cp.Knight(white_pieces['knight1'],team='white'),
              'knight2':cp.Knight(white_pieces['knight2'],team='white'),
              'rook1':cp.Rook(white_pieces['rook1'],team='white'),
              'rook2':cp.Rook(white_pieces['rook2'],team='white'),
              'pawn1':cp.Pawn(white_pieces['pawn1'],team='white'),
              'pawn2':cp.Pawn(white_pieces['pawn2'],team='white'),
              'pawn3':cp.Pawn(white_pieces['pawn3'],team='white'),
              'pawn4':cp.Pawn(white_pieces['pawn4'],team='white'),
              'pawn5':cp.Pawn(white_pieces['pawn5'],team='white'),
              'pawn6':cp.Pawn(white_pieces['pawn6'],team='white'),
              'pawn7':cp.Pawn(white_pieces['pawn7'],team='white'),
              'pawn8':cp.Pawn(white_pieces['pawn8'],team='white')}
# information array-------------------------------------------------------------------------------------------

#define functions =================================================================================

def pixel_pos(data):
    x,y = data
    return (8-(y-50)//75, chr(97+(x-50)//75))
def pos_pixel(data):
    x,y = data
    x = int(8-x)
    y = int(ord(y)-97)
    return ((y*75+55),(x*75+55))
def where(array,data):
    k=0
    for i in array.keys():
        x,y = array[i]
        g,h  = data
        
        if x==g and y==h:
            return i
        k+=1
    return None
def isPresent(main_data,finding_data):
    g,h  = finding_data
    for x, y in main_data:        
        if x==g and y==h:
            return True
    return False
#define functions =================================================================================

#main loop ****************************************************************************************
w =None
lock_key = 0
turn = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #print(event)
    
    #mouse event =================================================
    if event.type == pygame.MOUSEBUTTONDOWN and flag == 0:
        flag = 1
        #print(pixel_pos(event.pos))
        x,y = pixel_pos(event.pos)
        #print("black",where(black_pieces,pixel_pos(event.pos)))
        b = where(black_pieces,pixel_pos(event.pos))
        
        if lock_key==0:
            ini_pos_b = pixel_pos(event.pos)
            lock_bp = list(black_pieces.values())
            lock_wp = list(white_pieces.values())
            lock_key=1
            w = where(white_pieces,pixel_pos(event.pos))
            ini_pos_w = pixel_pos(event.pos)
        #print("white",where(white_pieces,pixel_pos(event.pos)))
        
        
    if event.type == pygame.MOUSEBUTTONUP and flag==1:
        flag =0
        #print(pixel_pos(event.pos))
        if b!=None:
            if isPresent(black_agents[b].posible_moves(lock_wp,lock_bp),pixel_pos(event.pos)) and turn:
                black_pieces[b] = pixel_pos(event.pos)
                black_agents[b].positions = pixel_pos(event.pos)
                v = where(white_pieces,pixel_pos(event.pos))
                if  v != None:
                    white_agents[v].isAlive = False
                    white_agents[v].positions = (10,'c') 
                    white_pieces[v] = (10,'c')
                lock_key=0
                b=None
                turn = not turn
            else:
                black_pieces[b] = ini_pos_b
                black_agents[b].positions = ini_pos_b
                lock_key=0
                b=None
                
        if w!=None:
            if isPresent(white_agents[w].posible_moves(lock_wp,lock_bp),pixel_pos(event.pos)) and not turn:
                white_pieces[w] = pixel_pos(event.pos)
                white_agents[w].positions = pixel_pos(event.pos)
                v = where(black_pieces,pixel_pos(event.pos))
                if  v != None:
                    black_agents[v].isAlive = False
                    black_agents[v].positions = (10,'c') 
                    black_pieces[v] = (10,'c')
                lock_key=0
                w=None
                turn = not turn
            else:
                white_pieces[w] = ini_pos_w
                white_agents[w].positions = ini_pos_w
                lock_key=0
                w=None
    #mouse event =================================================
        
        
    try:    
        black_pieces[b] = pixel_pos(event.pos)
        white_pieces[w] = pixel_pos(event.pos)
    except:
        pass
    
    
    # board-------------------------------------------------------------------
    gameDisplay.fill(white)
    for j in range(8):
        if j%2==0:
            for i in range(8):
                if i%2==0:
                    rect = pygame.Rect(j*75+50, i*75+50, 75, 75)
                    pygame.draw.rect(gameDisplay, gray ,rect)
                else:
                    rect = pygame.Rect(j*75+50, i*75+50, 75, 75)
                    pygame.draw.rect(gameDisplay, white ,rect)
        else:
            for i in range(8):
                if i%2==0:
                    rect = pygame.Rect(j*75+50, i*75+50, 75, 75)
                    pygame.draw.rect(gameDisplay, white ,rect)
                else:
                    rect = pygame.Rect(j*75+50, i*75+50, 75, 75)
                    pygame.draw.rect(gameDisplay, gray ,rect)
    rect = pygame.Rect(50,50, 4, weidth-100)
    pygame.draw.rect(gameDisplay, gray ,rect)
    rect = pygame.Rect(50,height-50, weidth-100, 4)
    pygame.draw.rect(gameDisplay, gray ,rect)
    
    rect = pygame.Rect(weidth-50, 50, 4, weidth-96)
    pygame.draw.rect(gameDisplay, gray ,rect)
    rect = pygame.Rect(50,50, weidth-100, 4)
    pygame.draw.rect(gameDisplay, gray ,rect)
    
    # board positions -------------------------------------------------
    
    for i in range(97,105):
        text = font.render(chr(i), True, gray)
        gameDisplay.blit(text,((i-97)*75+75,10))
        text = font.render(chr(i), True, gray)
        gameDisplay.blit(text,((i-97)*75+75,height-40))
        text = font.render(f"{105-i}", True, gray)
        gameDisplay.blit(text,(20,(i-97)*75+75))
        text = font.render(f"{105-i}", True, gray)
        gameDisplay.blit(text,(weidth-30,(i-97)*75+75))
        
    # board positions -------------------------------------------------
    
    
    
    
    # board-------------------------------------------------------------------
    
    
    # pieces-------------------------------------------------------------------
    for i in pieces:
        if black_agents[i].isAlive == True:   
            gameDisplay.blit(black_images[i],pos_pixel(black_pieces[i]))
        if white_agents[i].isAlive == True:
            gameDisplay.blit(white_images[i],pos_pixel(white_pieces[i]))
    # pieces-------------------------------------------------------------------
    
    
    #show posibble moves-------------------------------------------------------
    if flag==1:
        bp = list(black_pieces.values())
        wp = list(white_pieces.values())
        if w!= None:
            temp=white_agents[w].posible_moves(wp,bp)
            #print('temp',temp)
            if temp!=None:
                for i in temp:
                    g,h = tuple(i)
                    g = int(g)
                    h = str(h)
                    g,h = pos_pixel((g,h))
                    rect = pygame.Rect(g+5,h+5, 50, 50)
                    pygame.draw.rect(gameDisplay, (135,206,235) ,rect)
        if b!= None:
            temp=black_agents[b].posible_moves(wp,bp)
            if temp!=None:
                for i in temp:
                    g,h = tuple(i)
                    g = int(g)
                    h = str(h)
                    g,h = pos_pixel((g,h))
                    rect = pygame.Rect(g+5,h+5, 50, 50)
                    pygame.draw.rect(gameDisplay, (135,206,235) ,rect)
    #show posibble moves-------------------------------------------------------
    
    
    
    
    
    
    
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()







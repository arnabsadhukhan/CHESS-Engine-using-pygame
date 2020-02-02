import pandas as pd
import numpy as np


def isPresent(blocked_positions,piece_moves):
    temp=[]
    for r,c in piece_moves:
        flag=0
        r = int(r)
        c = str(c)
        for i,j in blocked_positions:
            i = int(i)
            j = str(j)
            if i==r and j==c:
                flag=1
                return True
    return False


def moves_filter(blocked_positions,pieces_moves):
    temp=[]
    for r,c in pieces_moves:
        flag=0
        r = int(r)
        c = str(c)
        for i,j in blocked_positions:
            i = int(i)
            j = str(j)
            if i==r and j==c:
                flag=1
                break
        if flag!=1:
            temp.append((r,c))
    return temp




class King:
    def __init__(self,position,team='black'):
        self.positions = position
        self.isAlive = True
        self.team = team

    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos):
        (r,c) = self.positions
        c = ord(c)
        self.posible_move = []
        if self.team=='black':
            if not isPresent(black_pos,[(r+1,chr(c+1))]):
                    if not isPresent(white_pos,[(r+1,chr(c+1))]):
                        self.posible_move.append((r+1,chr(c+1)))
                    else:
                        self.posible_move.append((r+1,chr(c+1)))
                        
            if not isPresent(black_pos,[(r-1,chr(c-1))]):
                    if not isPresent(white_pos,[(r-1,chr(c-1))]):
                        self.posible_move.append((r-1,chr(c-1)))
                    else:
                        self.posible_move.append((r-1,chr(c-1)))
                      
            if not isPresent(black_pos,[(r+1,chr(c))]):
                    if not isPresent(white_pos,[(r+1,chr(c))]):
                        self.posible_move.append((r+1,chr(c)))
                    else:
                        self.posible_move.append((r+1,chr(c)))
                      
            if not isPresent(black_pos,[(r-1,chr(c))]):
                    if not isPresent(white_pos,[(r-1,chr(c))]):
                        self.posible_move.append((r-1,chr(c)))
                    else:
                        self.posible_move.append((r-1,chr(c)))
                        
            if not isPresent(black_pos,[(r,chr(c+1))]):
                    if not isPresent(white_pos,[(r,chr(c+1))]):
                        self.posible_move.append((r,chr(c+1)))
                    else:
                        self.posible_move.append((r,chr(c+1)))
                       
            if not isPresent(black_pos,[(r,chr(c-1))]):
                    if not isPresent(white_pos,[(r,chr(c-1))]):
                        self.posible_move.append((r,chr(c-1)))
                    else:
                        self.posible_move.append((r,chr(c-1)))
                       
            
            if not isPresent(black_pos,[(r+1,chr(c-1))]):
                    if not isPresent(white_pos,[(r+1,chr(c-1))]):
                        self.posible_move.append((r+1,chr(c-1)))
                    else:
                        self.posible_move.append((r+1,chr(c-1)))
                        
            if not isPresent(black_pos,[(r-1,chr(c+1))]):
                    if not isPresent(white_pos,[(r-1,chr(c+1))]):
                        self.posible_move.append((r-1,chr(c+1)))
                    else:
                        self.posible_move.append((r-1,chr(c+1)))
                       
        else:
            temp1 = white_pos
            white_pos = black_pos
            black_pos = temp1
            if not isPresent(black_pos,[(r+1,chr(c+1))]):
                    if not isPresent(white_pos,[(r+1,chr(c+1))]):
                        self.posible_move.append((r+1,chr(c+1)))
                    else:
                        self.posible_move.append((r+1,chr(c+1)))
                        
            if not isPresent(black_pos,[(r-1,chr(c-1))]):
                    if not isPresent(white_pos,[(r-1,chr(c-1))]):
                        self.posible_move.append((r-1,chr(c-1)))
                    else:
                        self.posible_move.append((r-1,chr(c-1)))
                        
            if not isPresent(black_pos,[(r+1,chr(c))]):
                    if not isPresent(white_pos,[(r+1,chr(c))]):
                        self.posible_move.append((r+1,chr(c)))
                    else:
                        self.posible_move.append((r+1,chr(c)))
                        
            if not isPresent(black_pos,[(r-1,chr(c))]):
                    if not isPresent(white_pos,[(r-1,chr(c))]):
                        self.posible_move.append((r-1,chr(c)))
                    else:
                        self.posible_move.append((r-1,chr(c)))
                        
            if not isPresent(black_pos,[(r,chr(c+1))]):
                    if not isPresent(white_pos,[(r,chr(c+1))]):
                        self.posible_move.append((r,chr(c+1)))
                    else:
                        self.posible_move.append((r,chr(c+1)))
                       
            if not isPresent(black_pos,[(r,chr(c-1))]):
                    if not isPresent(white_pos,[(r,chr(c-1))]):
                        self.posible_move.append((r,chr(c-1)))
                    else:
                        self.posible_move.append((r,chr(c-1)))
                       
            
            if not isPresent(black_pos,[(r+1,chr(c-1))]):
                    if not isPresent(white_pos,[(r+1,chr(c-1))]):
                        self.posible_move.append((r+1,chr(c-1)))
                    else:
                        self.posible_move.append((r+1,chr(c-1)))
                       
            if not isPresent(black_pos,[(r-1,chr(c+1))]):
                    if not isPresent(white_pos,[(r-1,chr(c+1))]):
                        self.posible_move.append((r-1,chr(c+1)))
                    else:
                        self.posible_move.append((r-1,chr(c+1)))
                        
            
        self.posible_move = np.unique(self.posible_move,axis=0)
        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp
class Rook:
    def __init__(self,position,team='black'):
        self.positions = position
        self.isAlive = True
        self.team=team

    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos):
        (r,c) = self.positions
        c = ord(c)
        self.posible_move = []
        if self.team=='black':
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c))]):
                    if not isPresent(white_pos,[(r+i,chr(c))]):
                        self.posible_move.append((r+i,chr(c)))
                    else:
                        self.posible_move.append((r+i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c+i))]):
                    if not isPresent(white_pos,[(r,chr(c+i))]):
                        self.posible_move.append((r,chr(c+i)))
                    else:
                        self.posible_move.append((r,chr(c+i)))
                        break
                else:
                    break
         
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c))]):
                    if not isPresent(white_pos,[(r-i,chr(c))]):
                        self.posible_move.append((r-i,chr(c)))
                    else:
                        self.posible_move.append((r-i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c-i))]):
                    if not isPresent(white_pos,[(r,chr(c-i))]):
                        self.posible_move.append((r,chr(c-i)))
                    else:
                        self.posible_move.append((r,chr(c-i)))
                        break
                else:
                    break
        else:
            temp1 = white_pos
            white_pos = black_pos
            black_pos = temp1
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c))]):
                    if not isPresent(white_pos,[(r+i,chr(c))]):
                        self.posible_move.append((r+i,chr(c)))
                    else:
                        self.posible_move.append((r+i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c+i))]):
                    if not isPresent(white_pos,[(r,chr(c+i))]):
                        self.posible_move.append((r,chr(c+i)))
                    else:
                        self.posible_move.append((r,chr(c+i)))
                        break
                else:
                    break
         
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c))]):
                    if not isPresent(white_pos,[(r-i,chr(c))]):
                        self.posible_move.append((r-i,chr(c)))
                    else:
                        self.posible_move.append((r-i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c-i))]):
                    if not isPresent(white_pos,[(r,chr(c-i))]):
                        self.posible_move.append((r,chr(c-i)))
                    else:
                        self.posible_move.append((r,chr(c-i)))
                        break
                else:
                    break
            

        self.posible_move = np.unique(self.posible_move,axis=0)
        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp
class Bishop:
    def __init__(self,position,team='black'):
        self.positions = position
        self.isAlive = True
        self.team=team

    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos):
        (r,c) = self.positions
        c = ord(c)
        self.posible_move = []
        if self.team=='black':
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c+i))]):
                    if not isPresent(white_pos,[(r+i,chr(c+i))]):
                        self.posible_move.append((r+i,chr(c+i)))
                    else:
                        self.posible_move.append((r+i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c-i))]):
                    if not isPresent(white_pos,[(r-i,chr(c-i))]):
                        self.posible_move.append((r-i,chr(c-i)))
                    else:
                        self.posible_move.append((r-i,chr(c-i)))
                        break
                else:
                    break

            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c-i))]):
                    if not isPresent(white_pos,[(r+i,chr(c-i))]):
                        self.posible_move.append((r+i,chr(c-i)))
                    else:
                        self.posible_move.append((r+i,chr(c-i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c+i))]):
                    if not isPresent(white_pos,[(r-i,chr(c+i))]):
                        self.posible_move.append((r-i,chr(c+i)))
                    else:
                        self.posible_move.append((r-i,chr(c+i)))
                        break
                else:
                    break
        else:
            temp1 = white_pos
            white_pos = black_pos
            black_pos = temp1
            
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c+i))]):
                    if not isPresent(white_pos,[(r+i,chr(c+i))]):
                        self.posible_move.append((r+i,chr(c+i)))
                    else:
                        self.posible_move.append((r+i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c-i))]):
                    if not isPresent(white_pos,[(r-i,chr(c-i))]):
                        self.posible_move.append((r-i,chr(c-i)))
                    else:
                        self.posible_move.append((r-i,chr(c-i)))
                        break
                else:
                    break

            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c-i))]):
                    if not isPresent(white_pos,[(r+i,chr(c-i))]):
                        self.posible_move.append((r+i,chr(c-i)))
                    else:
                        self.posible_move.append((r+i,chr(c-i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c+i))]):
                    if not isPresent(white_pos,[(r-i,chr(c+i))]):
                        self.posible_move.append((r-i,chr(c+i)))
                    else:
                        self.posible_move.append((r-i,chr(c+i)))
                        break
                else:
                    break
        self.posible_move = np.unique(self.posible_move,axis=0)
        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp

class Knight:
    def __init__(self,position,team='black'):
        self.positions = position
        self.isAlive = True
        self.team=team

    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos):
        (r,c) = self.positions
        c = ord(c)
        self.posible_move = []
        if self.team=='black':
            if not isPresent(black_pos,[(r+2,chr(c+1))]):
                if not isPresent(white_pos,[(r+2,chr(c+1))]):
                    self.posible_move.append((r+2,chr(c+1)))
                else:
                    self.posible_move.append((r+2,chr(c+1)))
                  
            if not isPresent(black_pos,[(r+2,chr(c-1))]):
                if not isPresent(white_pos,[(r+2,chr(c-1))]):
                    self.posible_move.append((r+2,chr(c-1)))
                else:
                    self.posible_move.append((r+2,chr(c-1)))
                  
            if not isPresent(black_pos,[(r-2,chr(c+1))]):
                if not isPresent(white_pos,[(r-2,chr(c+1))]):
                    self.posible_move.append((r-2,chr(c+1)))
                else:
                    self.posible_move.append((r-2,chr(c+1)))
                   
            if not isPresent(black_pos,[(r-2,chr(c-1))]):
                if not isPresent(white_pos,[(r-2,chr(c-1))]):
                    self.posible_move.append((r-2,chr(c-1)))
                else:
                    self.posible_move.append((r-2,chr(c-1)))
                   
            if not isPresent(black_pos,[(r+1,chr(c+2))]):
                if not isPresent(white_pos,[(r+1,chr(c+2))]):
                    self.posible_move.append((r+1,chr(c+2)))
                else:
                    self.posible_move.append((r+1,chr(c+2)))
                   
            if not isPresent(black_pos,[(r-1,chr(c+2))]):
                if not isPresent(white_pos,[(r-1,chr(c+2))]):
                    self.posible_move.append((r-1,chr(c+2)))
                else:
                    self.posible_move.append((r-1,chr(c+2)))
                   
            if not isPresent(black_pos,[(r+1,chr(c-2))]):
                if not isPresent(white_pos,[(r+1,chr(c-2))]):
                    self.posible_move.append((r+1,chr(c-2)))
                else:
                    self.posible_move.append((r+1,chr(c-2)))
                    
            if not isPresent(black_pos,[(r-1,chr(c-2))]):
                if not isPresent(white_pos,[(r-1,chr(c-2))]):
                    self.posible_move.append((r-1,chr(c-2)))
                else:
                    self.posible_move.append((r-1,chr(c-2)))
                   
        else:
            temp1 = white_pos
            white_pos = black_pos
            black_pos = temp1
            if not isPresent(black_pos,[(r+2,chr(c+1))]):
                if not isPresent(white_pos,[(r+2,chr(c+1))]):
                    self.posible_move.append((r+2,chr(c+1)))
                else:
                    self.posible_move.append((r+2,chr(c+1)))
                  
            if not isPresent(black_pos,[(r+2,chr(c-1))]):
                if not isPresent(white_pos,[(r+2,chr(c-1))]):
                    self.posible_move.append((r+2,chr(c-1)))
                else:
                    self.posible_move.append((r+2,chr(c-1)))
                   
            if not isPresent(black_pos,[(r-2,chr(c+1))]):
                if not isPresent(white_pos,[(r-2,chr(c+1))]):
                    self.posible_move.append((r-2,chr(c+1)))
                else:
                    self.posible_move.append((r-2,chr(c+1)))
                   
            if not isPresent(black_pos,[(r-2,chr(c-1))]):
                if not isPresent(white_pos,[(r-2,chr(c-1))]):
                    self.posible_move.append((r-2,chr(c-1)))
                else:
                    self.posible_move.append((r-2,chr(c-1)))
                   
            if not isPresent(black_pos,[(r+1,chr(c+2))]):
                if not isPresent(white_pos,[(r+1,chr(c+2))]):
                    self.posible_move.append((r+1,chr(c+2)))
                else:
                    self.posible_move.append((r+1,chr(c+2)))
                    
            if not isPresent(black_pos,[(r-1,chr(c+2))]):
                if not isPresent(white_pos,[(r-1,chr(c+2))]):
                    self.posible_move.append((r-1,chr(c+2)))
                else:
                    self.posible_move.append((r-1,chr(c+2)))
                    
            if not isPresent(black_pos,[(r+1,chr(c-2))]):
                if not isPresent(white_pos,[(r+1,chr(c-2))]):
                    self.posible_move.append((r+1,chr(c-2)))
                else:
                    self.posible_move.append((r+1,chr(c-2)))
                    
            if not isPresent(black_pos,[(r-1,chr(c-2))]):
                if not isPresent(white_pos,[(r-1,chr(c-2))]):
                    self.posible_move.append((r-1,chr(c-2)))
                else:
                    self.posible_move.append((r-1,chr(c-2)))
                    
            
        self.posible_move = np.unique(self.posible_move,axis=0)

        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp

class Queen:
    def __init__(self,position,team='black'):
        self.positions = position
        self.isAlive = True
        self.team =team

    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos):
        (r,c) = self.positions
        c = ord(c)
        data = np.append(white_pos,black_pos,axis=0)
        self.posible_move = []
        if self.team=='black':
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c+i))]):
                    if not isPresent(white_pos,[(r+i,chr(c+i))]):
                        self.posible_move.append((r+i,chr(c+i)))
                    else:
                        self.posible_move.append((r+i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c-i))]):
                    if not isPresent(white_pos,[(r-i,chr(c-i))]):
                        self.posible_move.append((r-i,chr(c-i)))
                    else:
                        self.posible_move.append((r-i,chr(c-i)))
                        break
                else:
                    break

            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c-i))]):
                    if not isPresent(white_pos,[(r+i,chr(c-i))]):
                        self.posible_move.append((r+i,chr(c-i)))
                    else:
                        self.posible_move.append((r+i,chr(c-i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c+i))]):
                    if not isPresent(white_pos,[(r-i,chr(c+i))]):
                        self.posible_move.append((r-i,chr(c+i)))
                    else:
                        self.posible_move.append((r-i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c))]):
                    if not isPresent(white_pos,[(r+i,chr(c))]):
                        self.posible_move.append((r+i,chr(c)))
                    else:
                        self.posible_move.append((r+i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c+i))]):
                    if not isPresent(white_pos,[(r,chr(c+i))]):
                        self.posible_move.append((r,chr(c+i)))
                    else:
                        self.posible_move.append((r,chr(c+i)))
                        break
                else:
                    break
         
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c))]):
                    if not isPresent(white_pos,[(r-i,chr(c))]):
                        self.posible_move.append((r-i,chr(c)))
                    else:
                        self.posible_move.append((r-i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c-i))]):
                    if not isPresent(white_pos,[(r,chr(c-i))]):
                        self.posible_move.append((r,chr(c-i)))
                    else:
                        self.posible_move.append((r,chr(c-i)))
                        break
                else:
                    break
        
        else:
            temp1 = white_pos
            white_pos = black_pos
            black_pos = temp1
            
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c+i))]):
                    if not isPresent(white_pos,[(r+i,chr(c+i))]):
                        self.posible_move.append((r+i,chr(c+i)))
                    else:
                        self.posible_move.append((r+i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c-i))]):
                    if not isPresent(white_pos,[(r-i,chr(c-i))]):
                        self.posible_move.append((r-i,chr(c-i)))
                    else:
                        self.posible_move.append((r-i,chr(c-i)))
                        break
                else:
                    break

            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c-i))]):
                    if not isPresent(white_pos,[(r+i,chr(c-i))]):
                        self.posible_move.append((r+i,chr(c-i)))
                    else:
                        self.posible_move.append((r+i,chr(c-i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c+i))]):
                    if not isPresent(white_pos,[(r-i,chr(c+i))]):
                        self.posible_move.append((r-i,chr(c+i)))
                    else:
                        self.posible_move.append((r-i,chr(c+i)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r+i,chr(c))]):
                    if not isPresent(white_pos,[(r+i,chr(c))]):
                        self.posible_move.append((r+i,chr(c)))
                    else:
                        self.posible_move.append((r+i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c+i))]):
                    if not isPresent(white_pos,[(r,chr(c+i))]):
                        self.posible_move.append((r,chr(c+i)))
                    else:
                        self.posible_move.append((r,chr(c+i)))
                        break
                else:
                    break
         
            for i in range(1,9):
                if not isPresent(black_pos,[(r-i,chr(c))]):
                    if not isPresent(white_pos,[(r-i,chr(c))]):
                        self.posible_move.append((r-i,chr(c)))
                    else:
                        self.posible_move.append((r-i,chr(c)))
                        break
                else:
                    break
            for i in range(1,9):
                if not isPresent(black_pos,[(r,chr(c-i))]):
                    if not isPresent(white_pos,[(r,chr(c-i))]):
                        self.posible_move.append((r,chr(c-i)))
                    else:
                        self.posible_move.append((r,chr(c-i)))
                        break
                else:
                    break
            
        
    

        self.posible_move = np.unique(self.posible_move,axis=0)

        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp


class Pawn:
    def __init__(self,position,team="black"):
        self.positions = position
        self.isAlive = True
        self.team = team


    def isAlive(self):
        return self.isAlive

    def posible_moves(self,white_pos,black_pos,first_move = False):
        self.frst_move = first_move
        (r,c) = self.positions
        c = ord(c)
        self.posible_move = []
        if self.frst_move:
            if self.team =="black":
                self.posible_move.append((r-2,chr(c)))
                self.posible_move.append((r-1,chr(c)))
            else:
                self.posible_move.append((r+2,chr(c)))
                self.posible_move.append((r+1,chr(c)))
        else:
            if self.team =="black":
                if not isPresent(black_pos,[(r-1,chr(c))]):
                    if not isPresent(white_pos,[(r-1,chr(c))]):
                        self.posible_move.append((r-1,chr(c)))
                        
                        
                if isPresent(white_pos,[(r-1,chr(c-1))]):
                    self.posible_move.append((r-1,chr(c-1)))
                if isPresent(white_pos,[(r-1,chr(c+1))]):
                    self.posible_move.append((r-1,chr(c+1)))
                    
                        
            else:
                if not isPresent(black_pos,[(r+1,chr(c))]):
                    if not isPresent(white_pos,[(r+1,chr(c))]):
                        self.posible_move.append((r+1,chr(c)))
                        
                        
                if isPresent(black_pos,[(r+1,chr(c-1))]):
                    self.posible_move.append((r+1,chr(c-1)))
                if isPresent(black_pos,[(r+1,chr(c+1))]):
                    self.posible_move.append((r+1,chr(c+1)))
                       
                
        self.temp = []
        i,j =self.positions
        j= int(ord(j))
        for r,c in self.posible_move:
            c= int(ord(c))
            r= int(r)
            if r==i and c==j:
                pass
            elif r<=8 and r>=1 and c>=97 and c<=104:
                self.temp.append((r,chr(c)))
        return self.temp

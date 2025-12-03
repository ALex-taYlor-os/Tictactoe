import os
import random
import re
import time

#grille de morpion sous forme de liste linéaire en variable globale 
tabTictactoe = ['V','V','V','V','V','V','V','V','V']


# Jouer contre l'ordinateur
def ordinateur(board, signe): 
    positionAlea=random.randint(0, 8)
    if board[positionAlea]=="V":        #on vérifiuesi la case est libre
        return positionAlea
    elif board[positionAlea]==signe:    #on vérifie si la case contient déjà le signe auquel cas , on rappelle la fonction pour choisir une autre case
        return ordinateur(board,signe)
    elif board.count("V")>1:            #on demande si il existe encore des cases vides pour jouer auquel cas, on rappelle encore la fonction
        return ordinateur(board,signe)
    else:                               # si il n'existe plus de case
        return False


#Fonction pour mettre un signe par un utilisateur humain
def putSign(signTest):
    indexUser=input("Veuillez rentrer un numéro compris entre 1 et 9:"+"\n")

    
    if re.fullmatch(r"[1-9]",indexUser):
        indexUserInt=int(indexUser)
        if tabTictactoe[indexUserInt-1]=="V": #Si la case est vide mettre le signe
            tabTictactoe[indexUserInt-1]=signTest
            return 
        else:                           # Sinon redemandait une autre valeur de case
             
            putSign(signTest)
    else:
              
        putSign(signTest)
         





#Fonction affichant le morpion
def screenBoard(board): #trouver un moyen pour que saffiche toutjours en haut
      clear_console()
      u=0      
      for i in range(0,3):
        print(i+1,end="")
        print("|",end="")
        for j in range(0,3):
            print(board[u],"|",end="")
            u+=1          
        print("") 

    
#fonction pour supprimer tout ce qui a été marqué dans le terminal
def clear_console():
    os.system("cls" )


#fonction qui vérifie si il y a un gagnant selon le signe
def victoryUser(board,sign):
   
    if board.count(sign)<3: #Si moins de trois fois le même signe, pas de possibilité de gagne
        return False
    
    else:                    # Toutes les combinaisons pour gagner, A revoir pour le programmer en fonction selon taille de la grille
        if board[0]==sign and board[3]==sign and board[6]==sign: #Combinaisons gagnantes en colonnes
            return True
        elif board[1]==sign and board[4]==sign and board[7]==sign:
            return True
        elif board[0]==sign and board[4]==sign and board[8]==sign:
            return True
        elif board[2]==sign and board[4]==sign and board[6]==sign:
            return True
        elif board[0]==sign and board[1]==sign and board[2]==sign:
            return True
        elif board[3]==sign and board[4]==sign and board[5]==sign:
            return True
        elif board[6]==sign and board[7]==sign and board[8]==sign:
            return True 
        elif board[2]==sign and board[5]==sign and board[7]==sign:
            return True 
        else:
            return False          
    

def screenWin(MessageVictory): #REVOIR LES FONCTIONS QUI DOIVENT FAIRE UNE SEULE
    screenBoard(tabTictactoe)
    print(MessageVictory)


#intialisation pour une partie contre l'ordinateur
def playgame(sign,sign2):
   
    userChoiceVersus=input("Voulez-vous jouer contre l'ordinateur (1) ou avec un deuxième joueur (2) ?")

    if re.fullmatch(r"[1-2]",userChoiceVersus):
        userChoiceVersus=int(userChoiceVersus)
        if userChoiceVersus==1:
            sign="X"
            sign2="O"
        else:                   #A voir pour rajouter l'option du choix quand tu es le joueur 1 et le joueur 2.
            sign = "O"
            sign2 = "X"
            print(f"Le joueur 1 a les {sign} et le joueur 2 a les {sign2}.")
            time.sleep(4)
    else:
        print("Veuillez rentrer un nombre valide")
        playgame(sign,sign2)
        return

    return sign,sign2,userChoiceVersus# retourner  plus de signes



play=True
sign=""
signAIorPlayer2=""
sign,signAIorPlayer2,userchoice=playgame(sign,signAIorPlayer2)


#boucle infini pour afficher en continu la grille du morpion
while play==True:
    
    if tabTictactoe.count("V")==0:
        print("Match nul !")
        break
    else:
        
        screenBoard(tabTictactoe)       
        print("C'est au tour du Joueur 1 de jouer.")
        putSign(sign)#fonction pour que l'utilisateur mette un signe dans la grille 
        if userchoice==1:
           tabTictactoe[ordinateur(tabTictactoe,signAIorPlayer2)]="O"
        else:
            screenBoard(tabTictactoe)
            print("C'est au tour du Joueur 2 de jouer.")
            putSign(signAIorPlayer2)
    

    if victoryUser(tabTictactoe,sign):
            screenWin("Vous avez gagné!!")
            print("")
            play=False
    elif victoryUser(tabTictactoe,signAIorPlayer2):
        if signAIorPlayer2=="O":
            print("L'ordinateur a gagné!!") 
        else: 
            print("Le deuxième joueur a gagné!!")
         
            print()
        play=False
    else:
        pass
        print("")

   

    
    
import os
import random
import re
import time

#grille de morpion sous forme de liste linéaire en variable globale 1
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

#fonction qui vérifie si il y a un gagnant selon le signe par un True et False= aucun gagnant
def checkVictory(board,sign,player="player1"):
   
    tupleContext=(sign,player)
    if board.count(sign)<3: #Si moins de trois fois le même signe, pas de possibilité de gagne
        return False
    elif board[0]==sign and board[3]==sign and board[6]==sign or\
        board[1]==sign and board[4]==sign and board[7]==sign \
        or board[0]==sign and board[4]==sign and board[8]==sign \
        or board[2]==sign and board[4]==sign and board[6]==sign \
        or board[0]==sign and board[1]==sign and board[2]==sign \
        or board[3]==sign and board[4]==sign and board[5]==sign \
        or board[6]==sign and board[7]==sign and board[8]==sign \
        or board[2]==sign and board[5]==sign and board[7]==sign:
            screenBoard(board)
            for i in range(len(tabTictactoe)):
                tabTictactoe[i]='V'

            match tupleContext:
                case ("X","humainOrdi"):
                    print("Vous avez gagné !")
                    return True
                case ("X","player1"):
                    print("Le joueur 1 a gagné")
                    return True
                case ("O","Computer"):
                    print("L'ordinateur a gagné")
                    return True
                case ("O","joueur2"):
                    print("Le joueur 2 a gagné !")
                    return True                
                case _:
                    return False
    elif board.count("V")==0:
        print("Match nul !")
        return True
    else:
        return False
               # Toutes les combinaisons pour gagner, A revoir pour le programmer en fonction selon taille de la grille
           
    

def screenWin(MessageVictory): #REVOIR LES FONCTIONS QUI DOIVENT FAIRE UNE SEULE
    screenBoard(tabTictactoe)
    print(MessageVictory)
    print("")


#intialisation pour une partie contre l'ordinateur
def playgame(sign,sign2):
   
    userChoiceVersus=input("Voulez-vous jouer contre l'ordinateur (1) ou avec un deuxième joueur (2) ? ")

    if re.fullmatch(r"[1-2]",userChoiceVersus):
        userChoiceVersus=int(userChoiceVersus)
        if userChoiceVersus==1:
            sign="X"
            sign2="O"
            player2="Computer"
        else:                   #A voir pour rajouter l'option du choix quand tu es le joueur 1 et le joueur 2.
            sign = "X"
            sign2 = "O"            
            player2="joueur2"
            input(f"Le joueur 1 a les {sign} et le joueur 2 a les {sign2}. Apuuyez sur Entrée pour commencer")
            
    else:
        print("Veuillez rentrer un nombre valide")
        playgame(sign,sign2)
        return

    return sign,sign2,player2,userChoiceVersus # retourner  plus de signes


def mainGame():
    play=True
    sign=""
    signAIorPlayer2=""
    sign,signAIorPlayer2,secondPlayer,modePlay=playgame(sign,signAIorPlayer2)

    firstPlayer="player1"



    #boucle infini pour afficher en continu la grille du morpion
    while play==True:
        
        screenBoard(tabTictactoe)       
        print("C'est au tour du Joueur 1 de jouer.")
        putSign(sign)#fonction pour que l'utilisateur mette un signe dans la grille 
        if checkVictory(tabTictactoe,sign,firstPlayer):
            break
        else:        
            match modePlay:
                case 1:
                    tabTictactoe[ordinateur(tabTictactoe,signAIorPlayer2)]="O" 
                    firstPlayer="humainOrdi"
                case 2:
                    screenBoard(tabTictactoe)
                    print("C'est au tour du Joueur 2 de jouer.")
                    putSign(signAIorPlayer2)

            if checkVictory(tabTictactoe,signAIorPlayer2,secondPlayer):
                    
                break

            else:
                pass
    choice=input("Voulez-vous recommencer une partie ? 1 = Oui et 2 = Non"+"\n")
    if re.fullmatch(r"[1-2]",choice):
        if int(choice) == 1:            
            mainGame()
        else:
            exit 
    else:
        exit

mainGame()
 

    
    
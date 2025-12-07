import os
import random
import re



# Jouer contre l'ordinateur
def ordinateur(board, AIsign): 
     
    if AIsign=='X':
        humanSign="O"
    else:
        humanSign="X"

    positionHumanSign = calculatedPosition(board,humanSign)

    if board.count(humanSign)==0 or (positionHumanSign is not None and board.count(humanSign)==1 and positionHumanSign!=4 ): 
        return 4
    
    elif board.count(humanSign)==1 and positionHumanSign==4 : 
        listForAItoPlay=[0,2,6,8]        
        return random.choice(listForAItoPlay)
    
    else:
        return blockingAI(board,AIsign,humanSign)               



#IA qui va essayer de bloquer les attaques du joueur mais aussi attaquer si elle le peut.
#Renvoie une position à jouer pour l'ordinateur
def blockingAI(board,AIsign,humanSign):
    combinaisonVictory=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(6,4,2)]
    

    for i in range(len(board)):
        if board[i]==humanSign:
            for u in range(len(board)):
                if u!=i and board[u]==humanSign:
                    tuplewinning=(i,u)
                    for lineCompared in combinaisonVictory:
                        if isSubTuple(tuplewinning,lineCompared):
                            number=indexNotInTuple(lineCompared,tuplewinning)
                            if number is not None and board[number]=="V":
                                return number


    for i in range(len(board)):
        if board[i]==AIsign:
            for u in range(len(board)):
                if u!=i and board[u]==AIsign:
                    tuplewinning=(i,u)
                    for lineCompared in combinaisonVictory:
                        if isSubTuple(tuplewinning,lineCompared):
                            number=indexNotInTuple(lineCompared,tuplewinning)
                            if number is not None and board[number]=="V":
                                return number 
    
    listForChoicePosition=[]
    for i in range(len(board)):
        if board[i]=="V":
            listForChoicePosition.append(i)
              
            
    return random.choice(listForChoicePosition)



#Fonction qui renvoie le chiffre qui n'est pas dans le triplet gagnant
def indexNotInTuple(combinaisonVictory,tuplewinning):
    for i in combinaisonVictory:
        if i not in tuplewinning:
            return i
       
#Fonction verifiant si un tuple fait parti d'un plus grand tuple.
def isSubTuple(subSequence,fullSequence):
    count=0
    for value in subSequence:
        if value in fullSequence:
            count+=1
    if count >=2:
        return True
    else:         
        return False


#Retourne l'indice auquel se trouve le signExample
def  calculatedPosition(board,signExample):
    for i in range(len(board)):
        if board[i]==signExample:
            return i
        else:
           pass
    return None

#Fonction qui ajoute un signe dans la grille. Renvoie le tableau mis à jour.
def putSign(board,signTest):
    
    indexUser=input("Veuillez rentrer un numéro compris entre 1 et 9:"+"\n")

    
    if re.fullmatch(r"[1-9]",indexUser):
        indexUserInt=int(indexUser)
       
        if 1 <= indexUserInt <= 3:
            indexUserInt+=6           
        elif 7 <= indexUserInt <= 9:  
            indexUserInt-=6   
        else:
            pass
       
        indexUserInt-=1
        if board[indexUserInt]=="V": #Si la case est vide mettre le signe
               board[indexUserInt]=signTest
               return board
        else:                           # Sinon redemandait une autre valeur de case
               
              return putSign(board,signTest)     
    else:
        
        return putSign(board,signTest)
         

#Fonction affichant la grille du tictactoe
def screenBoard(board): 
      os.system("cls" )
      u=0      
      for i in range(0,3):
        print(i+1,end="")
        print("|",end="")
        for j in range(0,3):
            print(board[u],"|",end="")
            u+=1          
        print("") 
   

#Fonction qui vérifie si il y a un gagnant. Renvoie True = Il existe, False= Il existe pas.
def checkVictory(board,sign,player):
   
    tupleContext=(sign,player)
    if board.count(sign)<3: 
        return False
    elif board[0]==sign and board[3]==sign and board[6]==sign or\
        board[1]==sign and board[4]==sign and board[7]==sign \
        or board[0]==sign and board[4]==sign and board[8]==sign \
        or board[2]==sign and board[4]==sign and board[6]==sign \
        or board[0]==sign and board[1]==sign and board[2]==sign \
        or board[3]==sign and board[4]==sign and board[5]==sign \
        or board[6]==sign and board[7]==sign and board[8]==sign \
        or board[2]==sign and board[5]==sign and board[8]==sign:
            screenBoard(board)
            for i in range(len(board)):
                board[i]='V'

            match tupleContext:
                case ("X","alone"):
                    print("Vous avez gagné !")
                    return True
                case ("X","withHuman"):
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


#Fonction pour commencer une partie. Elle renvoie les signes pour chaque joeur et le mode de jeu
def playgame(sign,sign2):
   
    userChoiceVersus=input("Voulez-vous jouer contre l'ordinateur (1) ou avec un deuxième joueur (2) ? \n ")
    if re.fullmatch(r"[1-2]",userChoiceVersus):
        userChoiceVersus=int(userChoiceVersus)
        
        if userChoiceVersus==1:
            sign="X"
            sign2="O"
            playerAIorHuman="Computer"
        else:                   
            sign = "X"
            sign2 = "O"            
            playerAIorHuman="joueur2"
            input(f"Le joueur 1 a les {sign} et le joueur 2 a les {sign2}. \nAppuyez sur Entrée pour commencer")
            
    else:
        print("Veuillez rentrer un nombre valide.")
        return playgame(sign,sign2)
        

    return sign,sign2,playerAIorHuman,userChoiceVersus 


#Fonction principale qui lance le jeu

def main():
    print("\n-------------------Bienvenue au jeu du morpion-------------------\n")
    tabTictactoe=["V","V","V","V","V","V","V","V","V"]
    play=True
    sign=""
    signAIorPlayer2=""
    sign,signAIorPlayer2,secondPlayer,modePlay=playgame(sign,signAIorPlayer2)
    mainPlayer="withHuman"

    while play==True:
        
        screenBoard(tabTictactoe)       
        print("C'est au tour du Joueur 1 de jouer.\n")
        tabTictactoe=putSign(tabTictactoe,sign)
        if checkVictory(tabTictactoe,sign,mainPlayer):
            break
        else:        
            match modePlay:
                case 1:
                    indexAI=ordinateur(tabTictactoe,signAIorPlayer2)
                    tabTictactoe[indexAI]="O" 
                    mainPlayer="alone"
                case 2:
                    screenBoard(tabTictactoe)
                    print("C'est au tour du Joueur 2 de jouer.")
                    tabTictactoe=putSign(tabTictactoe,signAIorPlayer2)

            if checkVictory(tabTictactoe,signAIorPlayer2,secondPlayer):                    
                break

          
    choice=input("Voulez-vous recommencer une partie ? (1) = Oui, (2) = Non"+"\n")
    if re.fullmatch(r"[1-2]",choice):
        if int(choice) == 1:            
            main()
        else:
            print("A bientôt !")
            exit 
    
#Lancement du jeu par l'appel de la fonction mainGame

main()
 

    
    
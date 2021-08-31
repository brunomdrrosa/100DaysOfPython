campo = {'Q': ' ' , 'W': ' ' , 'E': ' ' ,
        'A': ' ' , 'S': ' ' , 'D': ' ' ,
        'Z': ' ' , 'X': ' ' , 'C': ' ' }

board_keys = []

for key in campo:
    board_keys.append(key)

def printBoard(board):
    print(board['Q'] + '|' + board['W'] + '|' + board['E'])
    print('-+-+-')
    print(board['A'] + '|' + board['S'] + '|' + board['D'])
    print('-+-+-')
    print(board['Z'] + '|' + board['X'] + '|' + board['C'])


def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(campo)
        print(f"É o seu turno, {turn}. Você quer colocar um {turn} em qual campo?")

        move = input()        

        if campo[move] == ' ':
            campo[move] = turn
            count += 1
        else:
            print("Esse campo já está preenchido.\nMover para qual campo?")
            continue

        if count >= 5:
            if campo['Q'] == campo['W'] == campo['E'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")                
                break
            elif campo['A'] == campo['S'] == campo['D'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break
            elif campo['Z'] == campo['X'] == campo['C'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break
            elif campo['Q'] == campo['A'] == campo['Z'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break
            elif campo['W'] == campo['S'] == campo['X'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break
            elif campo['E'] == campo['D'] == campo['C'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break 
            elif campo['Q'] == campo['S'] == campo['C'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break
            elif campo['Z'] == campo['S'] == campo['E'] != ' ':
                printBoard(campo)
                print("\nGame Over.\n")                
                print(" **** " +turn + " ganhou! ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("Empatou!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Você quer jogar de novo? (S/N)\n")
    if restart == "s" or restart == "S":  
        for key in board_keys:
            campo[key] = " "

        game()

if __name__ == "__main__":
    game()
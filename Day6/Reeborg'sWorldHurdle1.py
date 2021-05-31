def turn_right():
    turn_left()
    turn_left()
    turn_left()    

def andar_cima():
    turn_left()
    move()
    
def andar_lado():
    turn_right()
    move()
    
def andar_baixo():
    turn_right()
    move()
    
def loop():
    move()
    andar_cima()
    andar_lado()
    andar_baixo()
    turn_left()
    
for pulo in range(6):
    loop()
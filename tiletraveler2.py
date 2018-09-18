# Forritið felst í því að notandinn byrjar á 1,1 og þarf að komast til 3,1 
# Forritið keyrist í while loopu alveg þangað til að notandinn kemst á endareitinn
# Það er skoðað hvaða áttir notandinn getur farið í og út frá því er prentað út hvert hann getur farið
# Notandinn stimplar inn hvaða átt hann vill fara í og ef hún það er ekki hægt að fara í hana prentast út villa
# Notandinn finnur leiðina sína til 3,1 og þegar hann kemst þangað vinnur hann
# https://github.com/joelsnaer/HR-Forritun-1

def direction_check(x,y,directions):
    if x == 1 and y == 1: directions = "(N)orth."
    if x == 1 and y == 2: directions = "(N)orth or (E)ast or (S)outh."
    if x == 1 and y == 3: directions = "(E)ast or (S)outh."
    if x == 2 and y == 1: directions = "(N)orth."
    if x == 2 and y == 2: directions = "(S)outh or (W)est."
    if x == 2 and y == 3: directions = "(E)ast or (W)est."
    if x == 3 and y == 2: directions = "(N)orth or (S)outh."
    if x == 3 and y == 3: directions = "(S)outh or (W)est."
    return directions
def victory_check(x,y):
    if x == 3 and y == 1:
        print("Victory!")
        return True
def player_input(directions, player_choice):
    player_choice = input("You can travel: " + directions + "\nDirection:")
    return "(" + player_choice.upper() + ")"

def movement(x,y,directions,player_choice):
    if player_choice in directions:
        if player_choice == "(N)":
            y += 1
            return x, y
        elif player_choice == "(E)":
            x += 1
            return x, y
        elif player_choice == "(S)":
            y -= 1
            return x, y
        elif player_choice == "(W)":
            x -= 1
            return x, y
    else:
        print("Not a valid direction!")
        return x, y

directions = ""
player_tile_x = 1
player_tile_y = 1
player_choice = ""
running = True

while running:
    if (victory_check(player_tile_x, player_tile_y) == True):
        running = False
    else:
        directions = direction_check(player_tile_x, player_tile_y, directions)
        player_choice = player_input(directions, player_choice)
        player_tile_x, player_tile_y = movement(player_tile_x,player_tile_y,directions,player_choice)
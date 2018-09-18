# Forritið felst í því að notandinn byrjar á 1,1 og þarf að komast til 3,1 
# Forritið keyrist í while loopu alveg þangað til að notandinn kemst á endareitinn
# Það er skoðað hvaða áttir notandinn getur farið í og út frá því er prentað út hvert hann getur farið
# Notandinn stimplar inn hvaða átt hann vill fara í og ef hún það er ekki hægt að fara í hana prentast út villa
# Notandinn finnur leiðina sína til 3,1 og þegar hann kemst þangað vinnur hann

def direction_check(x,y,directions):
    if x == 1 and y == 1: directions = "(N)orth"
    if x == 1 and y == 2: directions = "(N)orth or (E)ast or (S)outh"
    if x == 1 and y == 3: directions = "(E)ast or (S)outh"
    if x == 2 and y == 1: directions = "(N)orth"
    if x == 2 and y == 2: directions = "(S)outh or (W)est"
    if x == 2 and y == 3: directions = "(E)ast or (W)est"
    if x == 3 and y == 2: directions = "(N)orth or (S)outh"
    if x == 3 and y == 3: directions = "(S)outh or (W)est"
    return directions
def victory_check(x,y):
    if x == 3 and y == 1:
        return True

directions = ""
player_tile_x = 1
player_tile_y = 1
player_choice = ""
running = True

while running:
    
    if (victory_check(player_tile_x, player_tile_y) == True):
        print("Victory!")
        running = False
    else:
        directions = direction_check(player_tile_x, player_tile_y, directions)
        player_choice = input("You can travel: " + directions + "\nDirection:")
        player_choice = "(" + player_choice.upper() + ")"
        if player_choice in directions:
            if player_choice == "(N)":
                player_tile_y += 1
            elif player_choice == "(E)":
                player_tile_x += 1
            elif player_choice == "(S)":
                player_tile_y -= 1
            elif player_choice == "(W)":
                player_tile_x -= 1
        else:
            print("Not a valid direction!")
            
            
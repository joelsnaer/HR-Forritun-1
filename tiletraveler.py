# Forritið felst í því að notandinn byrjar á 1,1 og þarf að komast til 3,1 
# Forritið keyrist í while loopu alveg þangað til að notandinn kemst á endareitinn
# Það er skoðað hvaða áttir notandinn getur farið í og út frá því er prentað út hvert hann getur farið
# Notandinn stimplar inn hvaða átt hann vill fara í og ef hún það er ekki hægt að fara í hana prentast út villa
# Notandinn finnur leiðina sína til 3,1 og þegar hann kemst þangað vinnur hann
# https://github.com/joelsnaer/HR-Forritun-1

tile11 = "(N)orth."
tile12 = "(N)orth or (E)ast or (S)outh."
tile13 = "(E)ast or (S)outh."
tile21 = "(N)orth."
tile22 = "(S)outh or (W)est."
tile23 = "(E)ast or (W)est."
tile32 = "(N)orth or (S)outh."
tile33 = "(S)outh or (W)est."
directions = ""
player_tile_x = 1
player_tile_y = 1
player_choice = ""
running = True
validation = 1

while running:
    if player_tile_x == 1 and player_tile_y == 1: directions = tile11
    if player_tile_x == 1 and player_tile_y == 2: directions = tile12
    if player_tile_x == 1 and player_tile_y == 3: directions = tile13
    if player_tile_x == 2 and player_tile_y == 1: directions = tile21
    if player_tile_x == 2 and player_tile_y == 2: directions = tile22
    if player_tile_x == 2 and player_tile_y == 3: directions = tile23
    if player_tile_x == 3 and player_tile_y == 2: directions = tile32
    if player_tile_x == 3 and player_tile_y == 3: directions = tile33
    
    if player_tile_x == 3 and player_tile_y == 1:
        print("Victory!")
        running = False
    else:
        if validation == 1:
            player_choice = print("You can travel: " + directions)
        player_choice = input("Direction: ")
        
        
        player_choice = "(" + player_choice.upper() + ")"
        if player_choice in directions:
            if player_choice == "(N)":
                player_tile_y += 1
                validation = 1
            elif player_choice == "(E)":
                player_tile_x += 1
                validation = 1
            elif player_choice == "(S)":
                player_tile_y -= 1
                validation = 1
            elif player_choice == "(W)":
                player_tile_x -= 1
                
        else:
            print("Not a valid direction!")
            validation = 0
            
            
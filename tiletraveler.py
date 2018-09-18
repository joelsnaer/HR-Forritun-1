# Forritið felst í því að notandinn byrjar á 1,1 og þarf að komast til 3,1 
# Forritið keyrist í while loopu alveg þangað til að notandinn kemst á endareitinn
# Það er skoðað hvaða áttir notandinn getur farið í og út frá því er prentað út hvert hann getur farið
# Notandinn stimplar inn hvaða átt hann vill fara í og ef hún það er ekki hægt að fara í hana prentast út villa
# Notandinn finnur leiðina sína til 3,1 og þegar hann kemst þangað vinnur hann
# https://github.com/joelsnaer/HR-Forritun-1
#
# 1. Which implementation was easier and why?
#Seinni framkvæmdin var léttari, fyrri framkvæmdin var erfiðara að lesa útaf þetta var ekki skipt upp í functions,
#það var léttara að gera breytingar við öll output-in þegar það var einfaldara að sjá hvað gerði hvað.
#
#  2. Which implementation is more readable and why?
#Seinni framkvæmdin er lesanlegri, hún er skipt upp í functions þannig það er léttar að lesa kóða þegar hann 
#er skiptur upp í búta sem gera sína vinnu, ég get séð léttilega hvað þessi hlutur gerir og þannig tengt það 
# inn í stóru myndina af forritinu
#
#  3. Which problems in the first implementations were you able to solve with the latter implementation?
#Stærsta vandamálið með þennan kóða var hversu mikið erfiðara það er að lesa hann, 
#vandamálin koma líka í að validation-ið þegar þú ert að stimpla inn breytu tekur lengri tíma og er mjög illa sett upp. 
#að finna hvaða átt hver kassi getur farið í er bara ljótur kassi af breytum sem ég náði að taka út í seinni framkvæmdinni.
#Ég lenti ekki í neinum stórum hættilegum vandamálum í fyrstu framkvæmdinni, 
#þetta voru bara minor hlutir sem bætast upp í að láta kóðann vera verri.


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
            
            
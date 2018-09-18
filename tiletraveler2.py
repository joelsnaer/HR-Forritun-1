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
    print("You can travel: " + directions)
    while validation:
        player_choice = input("Direction: ")
        if player_choice.upper() in directions:
            return "(" + player_choice.upper() + ")"
        else:
            print("Not a valid direction!")

def movement(x,y,directions,player_choice):
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

directions = ""
player_tile_x = 1
player_tile_y = 1
player_choice = ""
running = True
validation = True

while running:
    if (victory_check(player_tile_x, player_tile_y) == True):
        running = False
    else:
        directions = direction_check(player_tile_x, player_tile_y, directions)
        player_choice = player_input(directions, player_choice)
        player_tile_x, player_tile_y = movement(player_tile_x,player_tile_y,directions,player_choice)
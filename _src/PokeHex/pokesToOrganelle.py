import os
from PIL import Image #pip install pillow

mypath =  os.getcwd()
im = Image.open(mypath + '/atlas.png')

pix = im.load()
w = 56 
h = 56
gfxbitty = ""

incommingLine = False

x_past = 0

names = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
color = [1, 1, 1, 4, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 3, 3, 3, 7, 7, 3, 3, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 4, 4, 7, 7, 6, 6, 1, 1, 1, 1, 1, 1, 1, 6, 6, 7, 7, 2, 2, 7, 7, 4, 4, 2, 2, 2, 5, 5, 5, 3, 3, 3, 1, 1, 1, 2, 2, 7, 7, 7, 4, 4, 6, 6, 5, 5, 3, 7, 7, 2, 2, 6, 6, 2, 2, 6, 6, 6, 7, 5, 5, 2, 2, 5, 5, 1, 1, 7, 7, 7, 7, 6, 6, 6, 7, 7, 7, 1, 7, 2, 2, 2, 2, 2, 2, 7, 1, 7, 5, 4, 1, 7, 2, 2, 2, 6, 7, 2, 5, 4, 6, 2, 2, 7, 7, 3, 7, 3, 5, 4, 3, 3, 3, 6, 6]
# 0 apagado
# 1 verde
# 2 azul
# 3 celeste
# 4 rojo
# 5 verde amarillento
# 6 magenta
# 7 blanco

for poke_number in range(0,151):
    

    print("Processing: #"+ str(poke_number + 1).zfill(3) +" "+names[poke_number])

    gfxbitty = str(poke_number + 1).zfill(3) + " " + names[poke_number] + ";" +"\n"
    gfxbitty = gfxbitty + str(color[poke_number]) + ";" +"\n"
    poke_x = poke_number % 10 * w
    poke_y = int(poke_number / 10) * h

    for y in range(poke_y, poke_y + h):

        incommingLine = False;

        for x in range(poke_x, poke_x + w):

            r,g,b,a = pix[x,y]				

            if(incommingLine == False):
                if(r == 0):
                    incommingLine = True
                    x_past = x
            elif(r == 255):
                incommingLine = False

                pix_x = x_past - (poke_number % 10 * w)
                pix_x_new = x - 1 - (poke_number % 10 * w)
                pix_y = y - (int(poke_number / 10) * h)

                if(x - x_past == 1):
                    gfxbitty = gfxbitty + str(pix_x) + " " + str(pix_y) + " " + "0" + ";" +"\n"
                else:
                    gfxbitty = gfxbitty + str(pix_x) + " " + str(pix_y) + " " + str(pix_x_new) + " " + str(pix_y) + " " + "0" + ";" +"\n"
    
    text_file = open(mypath + "/../sprites/"+ str(poke_number + 1) +".txt", "w")
    text_file.write(gfxbitty)
    text_file.close()






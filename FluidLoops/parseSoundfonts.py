import os
from sf2utils.sf2parse import Sf2File

listFile = ""

for file in os.listdir(os.getcwd() + "/sf2/"):
    if os.path.splitext(file)[-1].lower() == ".txt":        
        os.remove(os.getcwd() + "/sf2/" + file)

def takeFirst(elem):
    return elem[0]
def takeSecond(elem):
    return elem[1]

for file in os.listdir(os.getcwd() + "/sf2/"):

        soundfontFile = ""
        presetsList = []
        
        with open(os.getcwd() + "/sf2/" + str(file), 'rb') as sf2_file:
                sf2 = Sf2File(sf2_file)
        
        sf2Name = str(os.path.splitext(file)[0])
        if len(sf2Name) > 20:
                sf2Name = sf2Name[0:20]
        sf2Name = sf2Name.rstrip()
        sf2Name = sf2Name.replace(" ", "_")
        listFile = listFile +" "+sf2Name+" "+sf2Name+" "+str(len(sf2Name))  # sf2Name is repeated now, older versions used the embeded name of the sf2

        instNume = 0

        for preset in sf2.raw.pdta["Phdr"]:
                instNume += 1
                
                if str(preset[0])[2:5] != "EOP": # End of presets tags
                        instName = str(preset[0])[2:str(preset[0]).find('\\')];

                        if len(instName) > 14:
                                instName = instName[0:14]
                        instName = instName.rstrip()
                        instName = instName.replace(" ", "_")
                        presetsList.append([int(preset[2]), int(preset[1]), instName])

        presetsList.sort()
        for p in presetsList:
                soundfontFile = soundfontFile + p[2] +";"+"\n" 

        listFile = listFile+" "+str(instNume-1)+";"+"\n"
        
        text_file = open(os.getcwd() + "/sf2/"+ str(os.path.splitext(file)[0]) + ".txt", "w")
        text_file.write(soundfontFile)
        text_file.close()

text_file = open(os.getcwd() + "/sf2/"+ "list.txt", "w")
text_file.write(listFile)
text_file.close()

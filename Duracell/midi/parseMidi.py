import mido
import os

filelist = ""
partNumber = 0

isABass = False;

lastOneWasAChunkEnd = False;

oldMsgTime = 0;

for file in os.listdir(os.getcwd() + "/../mididata/"):
	os.remove(os.getcwd() + "/../mididata/" + file)

for file in os.listdir("midi/"):
		if file.endswith(".mid"):
			
			partNumber = 0
			song = ""
			lastOneWasAChunkEnd = False

			mid = mido.MidiFile("midi/" + file)			

			for msg in mid:	
				if not isinstance(msg, mido.MetaMessage):

					print(msg);
					
					# check end of chunks
					if(msg.channel == 0 and msg.type == "note_off" and msg.time != oldMsgTime and lastOneWasAChunkEnd == False):
						song = song + "0" + ";" +"\n"
						lastOneWasAChunkEnd = True
					else:
						lastOneWasAChunkEnd = False

					# check for start of new part
					if(msg.channel == 8):
						if(msg.type == "note_off"):
							partNumber += 1

							text_file = open(os.getcwd() + "/../mididata/"+ str(os.path.splitext(file)[0])+"_"+ str(partNumber) + ".txt", "w")
							text_file.write(song)
							text_file.close()

							song = ""
					# print everything except bass off
					elif(not (msg.channel == 4 and msg.type == "note_off")):
						song = song + str(msg.channel) + " " + str(msg.note) + " " + str(msg.velocity) + ";" +"\n"

					oldMsgTime = msg.time;

			filelist = filelist + str(os.path.splitext(file)[0])+" "+str(partNumber)+ ";" +"\n"


text_file = open(os.getcwd() + "/../mididata/"+ "list.txt", "w")
text_file.write(filelist)
text_file.close()

# input("PRESS ENTER TO CLOSE")


					

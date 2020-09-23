import mido
import os

filelist = ""

for file in os.listdir("midi/"):
		if file.endswith(".mid"):
			filelist = filelist + str(os.path.splitext(file)[0])+ ";" +"\n"

			song = ""
			notes = [None] * 124
			timer = 0
			mid = mido.MidiFile("midi/" + file)

			for msg in mid:	
				if not isinstance(msg, mido.MetaMessage):

					timer += msg.time

					if(msg.type is 'note_on'):
						notes[msg.note] = timer
					elif(msg.type is 'note_off'):
						song = song + str(msg.note) + " " + str(notes[msg.note]) + " " + str(timer) + ";" +"\n"

			song = song + str(timer) + ";" +"\n"

			print(file)
			print(song)

			text_file = open(os.getcwd() + "/../miditxt/"+ str(os.path.splitext(file)[0]) +".txt", "w")
			text_file.write(song)
			text_file.close()

print(filelist)
text_file = open(os.getcwd() + "/../miditxt/"+ "list.txt", "w")
text_file.write(filelist)
text_file.close()

input("PRESS ENTER TO CLOSE")


					

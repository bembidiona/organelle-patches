# Pianelle
Pianelle it’s a virtual pianola in the same vein of Synthesia.

## FEATURES/NOTES:
- It plays midi files, and show the notes in the display like a pianola
- You can change and reverse speed of playing, or totally control the position of the score.
- Zoom in and out of the score
- Ships with a couple of retro videogame songs but you can add your own.

## CONTROLS:
- Knob 1: Adjust the playback speed. in pause mode, it scroll through the song.
- Knob 2: Adjust the zoom of the score
- Knob 3: Adjust the volume of the organelle keys
- Knob 4: Adjust the volume of the pianola notes
- Aux Button: Toggle pause mode
- Encoder Knob: Select song
- Encoder Button: Exit patch

## HOW TO ADD MORE SONGS
- First of, I wanted to stay vanilla, so I went the route of reading text files instead of directly from midi files. This conversion processes is done on a PC/MAC/LINUX computer. (maybe python can be runed on the organelle, but idkh) 
- Add the midi files you want to src/midi/ folder
- Run src/parseMidi.py (you need to have installed Python and the [mido](https://pypi.org/project/mido/) module)
- The converted midi files will be automatically placed on the miditxt/ folder
- Copy the new .txt files (including list.txt) to the miditxt/ folder on the Organelle patch.

### Notes
- The /src folder it just to convert the midi files to the txt files that will be read by PureData. It's not used by the patch on the Organelle in any way, so you don't need to copy it.
- The recommended range of keys is from C4 to B5. Lower and higher notes will be automatically remapped tho.
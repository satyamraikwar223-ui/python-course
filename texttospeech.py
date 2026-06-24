# This code converts the given text to speech and saves it as an MP3 file, then plays it using the default media player on Windows.
import os
from gtts import gTTS

text_to_convert = "Maine sikke fekein the nadiyon me " \
"Tootte taaron se tujhe maanga tha" \
" Maine sapne dekhe the bas tere " \
"Pakke dil se tujhe pukara tha" \
" Kbhi kabhi sochta hun" \
" Waadon ka itna pakka" \
" Koi dekha hi nahi" \
" Kitne phool dekhe maine" \
" Tere jaisa koi " \
"Mehka hi nahi."

# Generate the audio stream
tts = gTTS(text=text_to_convert, lang='hi', slow=False)

# Save the file locally
tts.save("speech_output.mp3")

# Tell Windows to play the file using its default player
os.system("start speech_output.mp3")

#------------------------------------------------------------------------------------------------------

#this code only play text to speech in windows os.
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Optional: Customize the speech rate and volume
engine.setProperty('rate', 150)    # Speed of speech (default is ~200)
engine.setProperty('volume', 0.9)  # Volume level between 0.0 and 1.0

# Queue the text to be spoken
text = "Hello! This text is spoken instantly without being saved to any file."
engine.say(text)

# Process and run the speech loop
engine.runAndWait()


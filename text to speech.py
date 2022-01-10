
#  this line will import our model so that we can 
# play the converted audio
from gtts import gTTS
  import os
  
# the following text store in  variable will be converted in to audio
mytext = 'hello there! how are you?'
  
# we want to listen it in english	
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
#  this line tell the module to play
 #  sound loudly
myobj.save("audiofile.mp3")
os.system("mpg321 audiofile.mp3")
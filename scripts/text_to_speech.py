import tkinter as tk
from tkinter import *
import pyttsx3
import clipboard

#we use pyttsx3 just because it is compatible offline
#initialize the speech engine
engine = pyttsx3.init()





#fuction to get user input and convert to audio
def generatedAudio():
    text = textWideget.get('1.0','end-1c')
    if text.strip():
        voice = engine.getProperty('voices')
        engine.setProperty('voice',voice[1].id)
        engine.say(text)
        engine.runAndWait()


#function for getting the content from clipboard
def readClipBoard():
    text = clipboard.paste()
    
    # textWideget.delete('1.0', 'end') #delets exisiting content
    textWideget.insert('1.0', text) # Insert clipboard content

#function to save the generated audio
def saveAudioButton():
    text = textWideget.get('1.0','end-1c')
    if text.strip(): #checks if the textwidget is empty or not
        engine.save_to_file(text, 'output.mp4')
        engine.runAndWait()



#initialize the window using tkinter
root = tk.Tk()
root.title('Text to Audio converter')


#making a text widget for taking text from the user
textWideget = tk.Text(root, wrap='word', width=50, height=10,bg='#049acc', fg='black')
textWideget.pack(pady=30)

# Frame to hold the buttons in the same row
button_frame = tk.Frame(root)
button_frame.pack()


#convert button to call generate audion function
convertButton = tk.Button(button_frame, text='Convert to Speech',command=generatedAudio, bg='#007acc', fg='white')
convertButton.pack(side='left', padx=5)

#read the clipboardbutton
clipboardReadBtn = tk.Button(button_frame, text='copy from clipboard', command=readClipBoard, bg='#007acc', fg='white')
clipboardReadBtn.pack(side='left', padx=5)

#button to save the voice
saveButton = tk.Button(button_frame, text='save audio',command=saveAudioButton, bg='#007acc', fg='white')
saveButton.pack(side='left', padx=5)


root.mainloop()



#loooooooooookking forward to ->
### upload files like (.docx, .pdf, other formats) and convert them into audio
### make the user able to customise the speed and pitch of the speaker
### make it available in more than just 2 speakers
### a web based application of the same project using streamlit or flask
### ----------------------------------------------------------------------------
### audio to text using speech_recognition liabrary
### use lang-chaine if you dont have any text to convert it will generate some
### ----------------------------------------------------------------------------
### may work with the liabraries offered by google that offers more varieties
### may add some shortcut keys if they were possible
### thats all for the project




###sharpFeatures
#words count
#charractors count
#stopbotton
#settings tab to change bgcolor 
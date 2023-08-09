from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES
import speech_recognition as sr

history = []  # Initialize an empty list to store translation history


root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.title("Language Translator")
root.config(bg = 'ghost white')

#heading
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(root, font = 'arial 20 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')



#INPUT AND OUTPUT TEXT WIDGET
Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)


Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

##################
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')
########################################  Define function #######

def Translate():
    translator = Translator()
    text = Input_text.get(1.0, END)
    src = src_lang.get()
    dest = dest_lang.get()

    translated = translator.translate(text=text, src=src, dest=dest)
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

    history.append((text.strip(), src, dest, translated.text.strip()))  # Update history with the translation details

   

def SpeechToText():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            Input_text.delete(1.0, END)
            Input_text.insert(END, text)
            Translate()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
def DisplayHistory():
    history_window = Toplevel(root)
    history_window.geometry('800x400')
    history_window.title('Translation History')

    history_text = Text(history_window, font='arial 10', height=20, wrap=WORD, padx=5, pady=5)
    history_text.pack()

    for entry in history:
        history_text.insert(END, f"Input: {entry[0]}\n")
        history_text.insert(END, f"Source Language: {entry[1]}\n")
        history_text.insert(END, f"Target Language: {entry[2]}\n")
        history_text.insert(END, f"Translation: {entry[3]}\n\n")


##########  Translate Button ########
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 180)

speech_btn = Button(root, text='Speech to Text', font='arial 12 bold', pady=5, command=SpeechToText, bg='green', activebackground='lime green')
speech_btn.place(x=470, y=300)


history_btn = Button(root, text='View History', font='arial 12 bold', pady=5, command=DisplayHistory, bg='gray',
                     activebackground='light gray')
history_btn.place(x=200, y=300)




root.mainloop()


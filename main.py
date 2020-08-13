from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

gui = Tk()
gui.title("Languages Translator - Sudotech Code")
gui.geometry("530x330")

def translate_text():
    lang1 = text1.get("1.0", "end-1c")
    c_lang = choose_lang.get()

    if lang1 == "":
        messagebox.showerror("Languages Translator - Sudotech Code", "Please fill the box!")
    else:
        translator = Translator()
        out = translator.translate(lang1, dest=c_lang)
        text2.insert('end', out.text)

def clear_text():
    text1.delete(1.0, 'end')
    text2.delete(1.0, 'end')

a = StringVar()
auto_detect = ttk.Combobox(gui, width=20, textvariable=a, state='readonly', font=('Times', 10, 'bold'))
auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

lang = StringVar()
choose_lang = ttk.Combobox(gui, width=20, textvariable=lang, state='readonly', font=('Times', 10, 'bold'))
choose_lang['values'] = ('Afrikaans',
                        'Albanian',
                        'Arabic',
                        'Armenian',
                       	'Azerbaijani',
                        'Basque',
                        'Belarusian',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                       	'Catalan',
                        'Cebuano',
                        'Chichewa',
                        'Chinese',
                        'Corsican',
                        'Croatian',
                       	'Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Esperanto',
                        'Estonian',
                        'Filipino',
                        'Finnish',
                        'French',
                        'Frisian',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hawaiian',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Kinyarwanda',
                        'Korean',
                        'Kurdish',
                        'Kyrgyz',
                        'Lao',
                        'Latin',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Myanmar',
                        'Nepali',
                        'Norwegian'
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Scots Gaelic',
                        'Serbian',
                        'Sesotho',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Sundanese',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Tatar',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Turkmen',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa'
                        'Yiddish',
                        'Yoruba',
                        'Zulu',)
choose_lang.place(x=290, y=70)
choose_lang.current(0)

text1 = Text(gui, width=30, height=10, borderwidth=5, relief=RIDGE)
text1.place(x=10, y=100)

text2 = Text(gui, width=30, height=10, borderwidth=5, relief=RIDGE)
text2.place(x=260, y=100)

btn_translate = Button(
    gui,
    text="Translate",
    relief=RIDGE,
    borderwidth=3,
    font=('Times', 10, 'bold'),
    cursor='hand2',
    command=translate_text)
btn_translate.place(x=150, y=280)

btn_clear = Button(
    gui,
    text="Clear",
    relief=RIDGE,
    borderwidth=3,
    font=('Times', 10, 'bold'),
    cursor='hand2',
    command=clear_text)
btn_clear.place(x=280, y=280)

gui.mainloop()
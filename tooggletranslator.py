from tkinter import *
from tkinter.ttk import Combobox
from googletrans import Translator
from pyperclip import copy as clip_copy

languages_index = {'Portuguese': 'pt', 'English': 'en', 'Japanese': 'ja', 'Espanish': 'es', 'German': 'de',
                   'Latin': 'la', 'Chinese (simplified)': 'zh-cn', 'Chine (traditional)': 'zh-tw', 'Afrikaans': 'af',
                   'Dutch': 'nl', 'Italian': 'it', 'Polish': 'pl', 'Russian': 'ru', 'Korean': 'ko', 'French': 'fr'}

LANGUAGES = sorted([la for la in languages_index])

class Janela:
    def __init__(self, master):
        self.dimensions = ['600', '650']
        self.translator = Translator()
        self.master = master
        self.master.title('Tooggle Translator')
        self.master.geometry('x'.join(self.dimensions)+'+300+10')
        self.master.resizable(0, 0)
        self.container = Frame(self.master, bg='#f3f3f3', width=self.dimensions[0], height=self.dimensions[1])
        self.container.pack()
        self.container.pack_propagate(0)
        self.tudo = Frame(self.container, bg='#fff')
        self.tudo.pack()
        self.header = Frame(self.tudo, width=self.dimensions[0], height=50, bg='#5094ff')
        self.header.pack()
        self.header.pack_propagate(0)
        self.f_langs = Frame(self.tudo, bg='#fff')
        self.f_langs.pack(pady=10)
        self.div_1 = Frame(self.tudo, bg='#cbcccb', width=self.dimensions[0], height=2)
        self.div_1.pack()
        self.f_texto = Frame(self.tudo, bg='#fff')
        self.f_texto.pack(pady=20)
        self.div_2 = Frame(self.tudo, bg='#cbcccb', width=self.dimensions[0], height=2)
        self.div_2.pack()
        self.f_transl_text = Frame(self.container, bg='#5094ff', width=575, height=260, highlightthickness=1,
                                 highlightbackground='#2379ff')
        self.f_transl_text.pack(pady=12)
        self.f_transl_text.pack_propagate(0)
        self.f_transl_text_inner = Frame(self.f_transl_text, bg='#5094ff')
        self.f_transl_text_inner.pack(pady=12)

        # WIDGETS ----------------------------------------------------
        self.logo = Label(self.header, text='Tooggle Translator', fg='#fff', bg='#5094ff', font=('Lucida Sans Typewriter', '17'))
        self.logo.pack(anchor=W, pady=10, padx=40)
        self.langs_0 = Combobox(self.f_langs, values=LANGUAGES, font=('Calibri', '15'),
                                  foreground='#5597ff', width=10, justify=CENTER)
        self.langs_0.grid(row=0, column=0)
        self.langs_0.current(13)  # Portuguese
        self.langs_0.bind('<<ComboboxSelected>>', self.translate)
        self.langs_1 = Combobox(self.f_langs, values=LANGUAGES, font=('Calibri', '15'),
                                  foreground='#5597ff', width=10, justify=CENTER)
        self.langs_1.grid(row=0, column=2)
        self.langs_1.current(4)  # English
        self.langs_1.bind('<<ComboboxSelected>>', self.translate)
        self.inverter_langs = Label(self.f_langs, text='⇄', font='Helvetica 20 bold', fg='#5597ff', bg='#fff')
        self.inverter_langs.grid(row=0, column=1, padx=70)
        self.inverter_langs.bind('<ButtonRelease-1>', self.inverter)

        self.entry = Text(self.f_texto, width=43, height=6, font='Helvetica 17', relief=FLAT,
                               fg='#515150') #width=36
        self.entry.bind('<Escape>', self.translate)
        self.entry.insert('end', 'Olá, Rogério...\nTudo bom?')
        self.entry.pack()

        self.transl_text = Text(self.f_transl_text_inner, font='Helvetica 15', bg='#5094ff', fg='#fff', relief=FLAT,
                              width=50, height=8, state=DISABLED, cursor='right_ptr')
        self.transl_text.pack()
        self.copy_img = PhotoImage(file='copy_img.png')
        self.copy_button = Label(self.f_transl_text_inner, bg='#5094ff', image=self.copy_img, cursor='right_ptr')
        self.copy_button.pack(pady=2, anchor=E, padx=20)
        self.copy_button.bind('<ButtonRelease-1>', lambda x: clip_copy(self.transl_text.get('1.0', END)))

    def inverter(self, event):
        l_0 = self.entry.get('1.0', END)
        l_1 = self.transl_text.get('1.0', END)
        l_0_index = self.langs_0.current()
        l_1_index = self.langs_1.current()
        self.transl_text['state'] = NORMAL
        self.entry.delete('1.0', END)
        self.transl_text.delete('1.0', END)
        self.entry.insert('end', l_1)
        self.transl_text.insert('end', l_0)
        self.transl_text['state'] = DISABLED
        self.langs_0.current(l_1_index)
        self.langs_1.current(l_0_index)


    def translate(self, event):
        texto = self.entry.get('1.0', END)
        lingua_0 = languages_index.get(self.langs_0.get())
        lingua_1 = languages_index.get(self.langs_1.get())
        print(self.langs_1.current())
        traduzido = self.translator.translate(text=texto, src=lingua_0, dest=lingua_1).text
        self.transl_text['state'] = NORMAL
        self.transl_text.delete('1.0', END)
        self.transl_text.insert('end', traduzido)
        self.transl_text['state'] = DISABLED

root = Tk()
janela = Janela(root)
root.mainloop()
print('oi')
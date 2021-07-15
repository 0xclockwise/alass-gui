from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
import subprocess
from encoding_list import enc_list # TODO: tidy up that list
from terminals import term_list
import shutil

filetypes = [('Subtitle file', '*.srt *.ass *.ssa *.idx *.sub')]

def set_ref_file():
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path != '':
        ref_file.set(path)

def set_inc_file():
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path != '':
        inc_file.set(path)

def set_out_file():
    path = filedialog.asksaveasfilename(defaultextension='.srt')
    if path != '':
        out_file.set(path)

def choose_terminal():
    for t in term_list:
        if shutil.which(t):
            term.set(t)
            return


def run():
    # gnome-terminal
    if term.get() == 'gnome-terminal':
        p = subprocess.Popen([term.get(), '--', 'sh', '-c', f'alass {ref_file.get()} {inc_file.get()} {out_file.get()} ; echo Press \<Enter\> to close ; read'])
        return
    # urxvt, st, deepin-terminal, kitty, konsole, alacritty and xterm
    if term.get() in ('urxvt', 'st', 'xterm', 'io.elementary.terminal', 'deepin-terminal', 'kitty', 'konsole', 'alacritty'):
        p = subprocess.Popen([term.get(), '-e', 'sh', '-c', f'alass {ref_file.get()} {inc_file.get()} {out_file.get()} ; echo Press \<Enter\> to close ; read'])
        return
    # io.elementary.terminal
    # this terminal emulator does not close after the program in it finishes, so there is no need to call the read command
    if term.get() == 'io.elementary.terminal':
        p = subprocess.Popen([term.get(), '-e', f'sh -c alass {ref_file.get()} {inc_file.get()} {out_file.get()}'])
    # terminator and terminolofy
    if term.get() in ('terminator', 'terminology'):
        p = subprocess.Popen([term.get(), '-e', f'sh -c alass {ref_file.get()} {inc_file.get()} {out_file.get()} ; echo Press \<Enter\> to close ; read'])
        return
    # xfce4-terminal and lxterminal
    if term.get() in ('xfce4-terminal', 'lxterminal'):
        p = subprocess.Popen([term.get(), '-e', f'sh -c "alass {ref_file.get()} {inc_file.get()} {out_file.get()} ; echo Press \<Enter\> to close ; read"'])
        return

def _quit():
    win.quit()
    win.destroy()
    exit()

def _about():
    messagebox.showinfo('About', 'Original program by kaegi')

win = Tk()
win.title('ALASS - GUI')
win.resizable(False, False)

menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Exit', command=_quit)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=_about)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Help', menu=help_menu)


ref_file = StringVar()
inc_file = StringVar()
out_file = StringVar()
ant = BooleanVar(value=False)
dfg = BooleanVar(value=False)
no_split = BooleanVar(value=False)
audio_index = IntVar(value=0)
ref_enc = StringVar(value='auto')
inc_enc = StringVar(value='auto')
term = StringVar()
choose_terminal()


ref_lab = Label(win, text='Reference file: ')
ref_ent = Entry(win, textvariable=ref_file, width=40)
ref_btn = Button(win, text='...', command=set_ref_file, width=3)
inc_lab = Label(win, text='Incorrect subtitle: ')
inc_ent = Entry(win, textvariable=inc_file, width=40)
inc_btn = Button(win, text='...', command=set_inc_file, width=3)
out_lab = Label(win, text='Output file: ')
out_ent = Entry(win, textvariable=out_file, width=40)
out_btn = Button(win, text='...', command=set_out_file, width=3)

run_btn = Button(win, text='RUN!', command=run)

adv = LabelFrame(win, text='Advanced options')
ant_chk = Checkbutton(adv, text='Allow negative timestamps', variable=ant)
dfg_chk = Checkbutton(adv, text='Disable FPS guessing', variable=dfg)
no_split_chk = Checkbutton(adv, text='No split', variable=no_split)
ai_lab = Label(adv, text='Audio Index:')
audio_index_spn = Spinbox(adv, from_=0, to=20, increment=1, textvariable=audio_index)
ref_enc_lb = Label(adv, text='Reference encoding:')
ref_enc_cb = Combobox(adv, values=enc_list, state='readonly', textvariable=ref_enc)
inc_enc_lb = Label(adv, text='Incorrect encoding:')
inc_enc_cb = Combobox(adv, values=enc_list, state='readonly', textvariable=inc_enc)
term_lb = Label(adv, text='Terminal emulator:')
term_cb = Combobox(adv, values=term_list, state='readonly', textvariable=term)

ref_lab.grid(column=0, row=0, sticky='w')
ref_ent.grid(column=1, row=0)
ref_btn.grid(column=2, row=0)
inc_lab.grid(column=0, row=1, sticky='w')
inc_ent.grid(column=1, row=1)
inc_btn.grid(column=2, row=1)
out_lab.grid(column=0, row=2, sticky='w')
out_ent.grid(column=1, row=2)
out_btn.grid(column=2, row=2)

adv.grid(column=0, row=3, columnspan=3, padx=5)

ant_chk.grid(column=0, row=0, sticky='w')
dfg_chk.grid(column=0, row=1, sticky='w')
no_split_chk.grid(column=0, row=2, sticky='w')
ai_lab.grid(column=0, row=3, sticky='w')
audio_index_spn.grid(column=0, row=4, sticky='w')

ref_enc_lb.grid(column=0, row=5, sticky='w')
ref_enc_cb.grid(column=0, row=6, sticky='w')
inc_enc_lb.grid(column=0, row=7, sticky='w')
inc_enc_cb.grid(column=0, row=8, sticky='w')
term_lb.grid(column=0, row=9, sticky='w')
term_cb.grid(column=0, row=10, sticky='w')

run_btn.grid(column=0, row=4, columnspan=3, sticky='nesw')

win.mainloop()
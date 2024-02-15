import os
import webbrowser
from customtkinter import *
from ips import ips
import time


root = CTk()  # create CTk window like you do with the Tk window
root.title("ShutOn")
set_appearance_mode("dark")  # Modes: system (default), light, dark  # Themes: blue (default), dark-blue, green

set_widget_scaling(1.0)  # widget dimensions and text size
#set_window_scaling(1.25)  # window geometry dimensions
#deactivate_automatic_dpi_awareness()

root.geometry('980x380')

set_default_color_theme("green")
root.option_add("*tearOff", FALSE)
root.resizable(False, False)

moves = ['Выключить', 'Включение', 'Перезагрузка']
computers=['-']
for key, value in ips.items():
    computers.append(f'K{key}  - {value[0]}')


info_text = """ 
ⓘ Чтобы все функции работали нормально надо 
выполнить ряд действий над которыми выполняется 
данное действие подробнее в readme.md
"""

def build():
    if comment_entry.get() == '': comentStr='def'
    else: comentStr=comment_entry.get()

    if time_entry.get() == '': timeStr=0
    else: timeStr=int(time_entry.get())

    if time_entry_noshow.get() == '': timeStr_noshow=0
    else: timeStr_noshow=int(time_entry_noshow.get())

    if moves_combobox.get() == 'Выключить':
        time.sleep(timeStr_noshow)
        shutdown(mode='s', comment=comentStr, time=timeStr)
    if moves_combobox.get() == 'Включение':
        time.sleep(timeStr_noshow)
        on()
    if moves_combobox.get() == 'Перезагрузка':
        time.sleep(timeStr_noshow)
        reboot(mode='r', comment=comentStr, time=timeStr)

    #if moves_combobox.get() == 'Спящий режим':
    #    sleep()
def shutdown(mode, comment, time):
    if shutall_checkbox.get() == 1:
        for i in range(list(ips.items())[0][0], len(ips) + list(ips.items())[0][0]):
            os.system(r'shutdown /m \\' + ips[i][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

    elif single_power_off_combobox.get() != '-':
        os.system(r'shutdown /m \\' + ips[int(single_power_off_combobox.get()[1:4])][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

    else:
        for i in range(int(diapoz_entry_from.get()), int(diapoz_entry_to.get())+1):
            os.system(r'shutdown /m \\' + ips[i][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

def on():
    if shutall_checkbox.get() == 1:
        for i in range(list(ips.items())[0][0], len(ips) + list(ips.items())[0][0]):
            os.system(r'wakeup\WakeOnLanC.exe -w -mac ' + ips[i][1])

    elif single_power_off_combobox.get() != '-':
        os.system(r'wakeup\WakeOnLanC.exe -w -mac ' + ips[int(single_power_off_combobox.get()[1:4])][1])

    else:
        for i in range(int(diapoz_entry_from.get()), int(diapoz_entry_to.get())+1):
            os.system(r'wakeup\WakeOnLanC.exe -w -mac ' + ips[i][1])


def reboot(mode, comment, time):
    if shutall_checkbox.get() == 1:
        for i in range(list(ips.items())[0][0], len(ips) + list(ips.items())[0][0]):
            os.system(r'shutdown /m \\' + ips[i][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

    elif single_power_off_combobox.get() != '-':
        os.system(r'shutdown /m \\' + ips[int(single_power_off_combobox.get()[1:4])][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

    else:
        for i in range(int(diapoz_entry_from.get()), int(diapoz_entry_to.get())+1):
            print(r'shutdown /m \\' + ips[i][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')
            os.system(r'shutdown /m \\' + ips[i][0] + ' /' + mode + r' /t ' + str(time) + ' /c "' + comment + '"')

'''
def sleep():
    if shutall_checkbox.get() == 1:
        for i in range(ips.items()[0][0], len(ips) + ips.items()[0][0]):
            os.system(r'WakeOnLanC.exe -s1 -m ' + ips[i][0])

    elif single_power_off_combobox.get() != '-':
        os.system(r'WakeOnLanC.exe -s1 -m ' + ips[int(single_power_off_combobox.get()[1:4])][0])

    else:
        for i in range(int(diapoz_entry_from.get()), int(diapoz_entry_to.get())+1):
            os.system(r'WakeOnLanC.exe -s1 -m ' + ips[i][0])
'''

text_move = CTkLabel(root, text="Действие: ", font=('Arial', 32), justify="left")
text_move.grid(column=0, row=0, columnspan=3, pady=[10,10])

moves_combobox = CTkComboBox(root, values=moves, width=300)
moves_combobox.grid(column=3, row=0, columnspan=4, pady=[10,10])

single = CTkFrame(master=root)
single.grid(column=0, row=1, columnspan=3, rowspan=3, padx=[10, 0], ipady=30, ipadx=10)

single_power_off_text = CTkLabel(single, text="\nОтдельный компьютер:\n", justify="left")
single_power_off_text.grid(row=0, column=0, columnspan=1, padx=[10,0])

single_power_off_combobox = CTkComboBox(single, values=computers, width=200)
single_power_off_combobox.grid(column=0, row=1, columnspan=2, padx=[10,0])

or_label=CTkLabel(root, text="или")
or_label.grid(column=3, row=1, padx=15)

diapoz=single = CTkFrame(root)
diapoz.grid(row=1, column=4, rowspan=2, columnspan=3, ipady=10, ipadx=25)

diapoz_text=CTkLabel(diapoz, text="\nИз диапозона:\n")
diapoz_text.grid(column=0, row=0, columnspan=2, padx=[10,0])

diapoz_text_from=CTkLabel(diapoz, text=" От   ")
diapoz_text_from.grid(column=0, row=1, padx=[10,0], pady=[0,10])

diapoz_entry_from=CTkEntry(diapoz, placeholder_text="Номер компьютера")
diapoz_entry_from.grid(column=1, row=1, pady=[0,10])

diapoz_text_to=CTkLabel(diapoz, text=" До   ")
diapoz_text_to.grid(column=0, row=2, padx=[10,0])

diapoz_entry_to=CTkEntry(diapoz, placeholder_text="Номер компьютера")
diapoz_entry_to.grid(column=1, row=2)

or_label=CTkLabel(root, text=" или ")
or_label.grid(column=7, row=1, padx=15)

shutall = CTkFrame(root)
shutall.grid(column=8, row=1, rowspan=3, columnspan=5, padx=[0, 10], ipadx=25, ipady=8)

shutall_checkbox = CTkCheckBox(shutall, text="Применить для всех")
shutall_checkbox.grid(column=0, row=0, rowspan=1, padx=[10, 0], pady=[20,0])

shutall_infotext = CTkLabel(shutall, text=info_text, text_color="yellow", font=('Arial', 10))
shutall_infotext.grid(column=0, row=1, columnspan=5, rowspan=2, padx=[10, 0])



add_frame = CTkFrame(root)
add_frame.grid( column=0, row=5, columnspan=6, pady=[20, 38], padx=[10, 10])

text_add=CTkLabel(add_frame, text="Дополнительно:")
text_add.grid(column=0, row=0)

comment_text=CTkLabel(add_frame, text="Комментарий ", justify="left")
comment_text.grid(column=0, row=1, columnspan=1, pady=[5, 5], padx=[0, 20])

comment_entry=CTkEntry(add_frame, width=250)
comment_entry.grid(column=1, row=1, columnspan=1, pady=[5, 5])

time_shut_text=CTkLabel(add_frame, text="Время ожидания ")
time_shut_text.grid(column=0, row=2, padx=[0, 20])

time_entry = CTkEntry(add_frame, width=250)
time_entry.grid(column=1, row=2, columnspan=4)

time_shut_text_noshow=CTkLabel(add_frame, text="Время скрытого ожидания ")
time_shut_text_noshow.grid(column=0, row=3, pady=[5, 5], padx=[0, 20])

time_entry_noshow = CTkEntry(add_frame, width=250)
time_entry_noshow.grid(column=1, row=3, pady=[5, 5])

btn_author = CTkButton(add_frame, fg_color="black", width=450, text="By Bolgaro4ka", command=lambda: webbrowser.open('https://github.com/bolgaro4ka', new=True))
btn_author.grid(column=0, row=4, columnspan=2)

move_button=CTkButton(root, text='Выполнить', width=500, height=155, command=build)
move_button.grid(column=6, row=5, columnspan=7, padx=[0, 10], pady=[0, 12])

root.mainloop()

import os
from ips import ips, group_name

DEBUG = False
print("Выберите действие:")
print("1. Выключение")
print("2. Перезагрузка")
print("3. Включение")

mode = input("Выберите: ")

print("\nДля какого компьютера выполнять действие?")
print("Параметр: (-1)- действие для всех.")
print("Параметр: (2-15)- действие для отдельного компьютера.")

comp = int(input("Выберите цель <<< "))
time = int(input("\nЧерез сколько секунд выдполнить действие <<< "))
comment = input("\nКомментарий: ")

try:
    mode = int(mode)
    if mode == 1:
        mode = "s"
    elif mode == 2:
        mode = "r"
except:
    mode = "s"

if DEBUG == True:
    print(
        r"shutdown /m \\"
        + ips[comp][0]
        + " /"
        + mode
        + r" /t "
        + str(time)
        + ' /c "'
        + comment
        + '"'
    )
if mode == 3:
    if comp == -1:
        for i in range(2, len(ips) + 2):
            os.system(r"WakeOnLanC.exe -w -mac " + ips[i][1])
    else:
        os.system(r"WakeOnLanC.exe -w -mac " + ips[comp][1])
else:
    if comp == -1:
        for i in range(2, len(ips) + 2):
            os.system(
                r"shutdown /m \\"
                + ips[i][0]
                + " /"
                + mode
                + r" /t "
                + str(time)
                + ' /c "'
                + comment
                + '"'
            )

    else:
        os.system(
            r"shutdown /m \\"
            + ips[comp][0]
            + " /"
            + mode
            + r" /t "
            + str(time)
            + ' /c "'
            + comment
            + '"'
        )

print("Всё")

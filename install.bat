@echo off
set "source_folder=%~dp0data"
set "destination_folder=C:\Program Files\ShutOn"
set "shortcut_source=%~dp0data\ShutOn.lnk"
set "shortcut_destination=%userprofile%\Desktop\ShutOn.lnk"

REM Проверяем существование папки назначения
if not exist "%destination_folder%" mkdir "%destination_folder%"

REM Копируем файлы из папки data в папку назначения
xcopy /s /y "%source_folder%" "%destination_folder%"

REM Копируем ярлык на рабочий стол
copy "%shortcut_source%" "%shortcut_destination%"

echo The installation program has completed its work.
pause

pip install customtkinter
pip install packaging
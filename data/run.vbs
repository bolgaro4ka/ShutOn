Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Program Files\ShutOn\ShutOn Lanch.cmd" & Chr(34), 0
Set WshShell = Nothing
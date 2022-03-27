import os, winshell, win32com.client#, Pythoncom

desktop = winshell.desktop()
#desktop = r"path to where you wanna put your .lnk file"

current_folder = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(desktop, 'English App.lnk')
target = os.path.join(current_folder, 'run.bat')
icon = os.path.join(current_folder, 'graphics\\icons\\application.dll')

shell = win32com.client.Dispatch("WScript.Shell")

shortcut = shell.CreateShortCut(path)
shortcut.WorkingDirectory = current_folder
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()

import winreg
import os
program_path = os.path.abspath("browser.py")
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Microsoft\\Windows\\CurrentVersion\\Explorer\\StartupApproved\\Run", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "Browser Set prog", 0, winreg.REG_SZ, program_path)
winreg.CloseKey(key)

import winreg

with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "") as hklm_key:
    for idx in range(winreg.QueryInfoKey(hklm_key)[0]):
        if winreg.EnumKey(hklm_key, idx)[0] == ".":
            print(winreg.EnumKey(hklm_key, idx))

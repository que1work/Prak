import os

def Func(file, direc):  #Оголошення функції з параметрами file (назва файлу), direc (шлях до директорії)
    for root, dirs, files in os.walk(direc): #Викор. функції os.walk для поточної папки, директорій та файлів
        if file in files:   #Перевірка наявності шуканого файлу
            return os.path.join(root, file) #Об'єднання шляху та назви файлу і повернення значення
    return None;

direc = input("Введіть шлях до папки: ")
file = input("Введіть назву файлу: ")

result = Func(file, direc)
if result:
    print("Файл знайдено: " + result)
else:
    print("Файл не знайдено")

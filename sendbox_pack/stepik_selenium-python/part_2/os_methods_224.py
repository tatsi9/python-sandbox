import os

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла ??
print(file_path)

# В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
# если path изменится - код без правок все равно заработает

# file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']").click() - найти кнопку добавления файла
# file_button.send_keys(file_path) # отправить файл

print(os.path.abspath(__file__))  # возвращает путь к прям вот этому исполняемому файлу
print(os.path.abspath(os.path.dirname(__file__)))  # возвращает путь к каталогу, где данный исполняемый файл
# это будет работать только при запуске кода из файла, в интерпретаторе не сработает.



#os.path.exists("/sendbox_pack/stepik_selenium-python/part_2/file.txt")  # говорит, существует ли такой путь (к файлу)
#print(os.path.exists("/sendbox_pack/stepik_selenium-python/part_2/file.txt"))

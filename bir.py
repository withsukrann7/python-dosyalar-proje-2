"""
Örneğin, Python dosyalarının içeriği hakkında bilgi almak istediğinizde, 
belirli bir Python dosyasının içeriğini okumak ve görüntülemek için bir program yazabilirsiniz. 
"""
"""
import os 
def get_file_name():
    file_name = input("Lütfen dosya adını girin: ")
    return file_name

   
def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r',encoding="UTF-8") as f:
            content = f.read()
            return content
    else:
        print("Dosya bulunamadı!")



def see_file(file_name):
    with open(file_name, 'r',encoding="UTF-8") as f1:
        icerik = f1.read()
        print(icerik)

# program
file_name = get_file_name()
content = read_file(file_name)
if content:
    see_file(file_name)
"""
import os 

def get_file_name():
    file_name = input("dosya adını giriniz..:")
    return file_name

def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r",encoding="UTF-8") as f:
            contenct = f.read()
            return contenct
    else:
        print("dosya bulunamamaktadır..")

def see_file(file_name):
    with open(file_name,"r",encoding="UTF-8") as f1:
        içerik = f1.read()
        print(içerik)
    
file_name = get_file_name()
contenct = read_file(file_name)
if contenct:
    see_file(file_name)

        



    








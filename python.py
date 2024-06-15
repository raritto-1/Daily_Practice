import os 
folder = 'data'#path
data = os.listdir(folder)
print(data )
for i in data:
    print(i)
    if i.endswith((".exe", ".jpg", ".png" , ".txt")):#type of file
        file = i.split('.')[-1]
        
        #i got the type of file so writ now create the folders and transfer the data into foldes
        
        comp = os.path.join(folder ,  i)

        os.makedirs(comp , exist_ok=True)
        source = os .path.join(folder  , i )       
        destination_path = os.path.join(comp, i)
        os.rename(source, destination_path)

print('your files are transfer successfully ')

                 
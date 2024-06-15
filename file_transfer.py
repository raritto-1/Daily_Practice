import os 
folder = 'data'
data = os.listdir(folder)
print(data )
for i in data:
    print(i)
    if i.endswith((".exe", ".jpg", ".png" , ".txt")):
        file = i.split('.')[-1]
        
               
        comp = os.path.join(folder ,  i)

        os.makedirs(comp , exist_ok=True)
        source = os .path.join(folder  , i )       
        
        destination_path = os.path.join(comp, i)
        os.rename(source, destination_path)

print('your files are transfer successfully ')

                 
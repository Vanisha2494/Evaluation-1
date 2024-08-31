#dictionary = {ID:[name,task]}

def add_task(name, ID, status, d):
    d[ID]=[name, status]
    return

def update_task(opt, change, ID, d):
    if(opt not in [1,2,3]):
        print("Invalid modification")
        return
    if(opt==1):      #change name
        d[ID][0]=change
    elif(opt==2):    #change task status
        d[ID][1]=change
    elif(opt==3):    #change both
        d[ID]=change
        
def delete_task(name, d):
    for key,value in d.items():
        if(d[key][0]==name):
            del d[key]
            return
    print("The name not present.")
    
def display(d):
    print(" ID   Name \t Status ")
    for key, value in d.items():
        print(f" {key}   {value[0]} \t {value[1]}")
        
def search(opt, key, d):
    if(opt not in [1,2]):
        print("Invalid Option. \n")
        return
    print(" ID   Name   Status ")
    if(opt==1):       #search using ID
        if(key in d):
            print(f" {key}   {d[key][0]} \t {d[key][1]}\n")
        else:
            print("ID not found. \n")
    elif(opt==2):     #search using name
        for k in d.keys():
            if(d[k][0]==key):
                print(f" {k}    {d[k][0]} \t {d[k][1]}\n")
                return
        print("Name not found. \n")
        
def list_task(ch, d):
    print(" ID   Name   Status ")
    for k in d.keys():
            if(d[k][0][-1]==ch):
                print(f" {k}    {d[k][0]} \t {d[k][1]}")
            
dic= {1:["Laundry", "Y"], 2:["Meals", "Y"], 3:["Groceries", "N"], 4:["Study", "N"], 5:["Cleaning", "Y"]}

add_task("Travel", 6, "N", dic)
display(dic)

delete_task("Study", dic)
display(dic)

update_task(1, "Clean", 5, dic)
update_task(2, "N", 1, dic)
update_task(3, ["Tours","Y"], 6, dic)
display(dic)

search(1, 5, dic)
search(2, "Laundry", dic)
search(3, 3, dic)

list_task("s", dic)

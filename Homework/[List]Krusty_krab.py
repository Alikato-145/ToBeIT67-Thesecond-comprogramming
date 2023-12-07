menu_data = []
menu_N = []
N = 0
y=0
while True:
    menu = input()
    if menu.upper() == "DONE":
        break
    position = menu.find('#')
    menu_name = menu[:position].strip()
    menu_number = menu[position + 1:].strip()
    if not menu_number.isnumeric():
        if len(menu_data) == 0:
            menu_number = 1
            menu_data.append(menu_name)
        else:
            if "N" in menu_number:
                menu_data.append(menu_name)
    else:
        menu_number = int(menu_number)     
        if len(menu_data) == 0:
            menu_data.append(menu_name)
        else:
            for i in range(len(menu_data)):
                if i+1 == menu_number:
                    menu_data.insert(i,menu_name)
                    y=1
                    break
            if y==0:
                menu_data.insert(i+1,menu_name)
                if menu_number >len(menu_data):
                    menu_data.append(menu_name)
            y=0
k = 0
while k < len(menu_data):
    count = menu_data.count(menu_data[k])
    if count >= 2:
        menu_data.remove(menu_data[k])
    else:
        k += 1
print("Menu:",menu_data)
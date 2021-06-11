# Challenge 5 using Easygui
import easygui as gui

d = {}
while True:
    res = gui.multenterbox(title='Enter information', fields=['Name', 'Age'])
    print(res)
    if res:
        if res[0] and res[1]:
            d[res[0]] = res[1]
    ans = gui.ynbox(title="Continue")
    if not ans:
        break

while True:
    name = gui.enterbox(msg='Enter name to search', title='Search')
    if name:
        age = d.get(name, 'unknown')
        ans = gui.msgbox(msg=f"{name}'s age is {age}", title='Information')
    ans = gui.ynbox(title="Continue")
    if not ans:
        break        

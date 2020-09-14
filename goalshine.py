import time
def goalshineinput():
    global gfxName
    gfxName = input("Enter GFX name exluding .dds or other file format. Type quit to quit.")
    if gfxName in {'quit', 'Quit', 'QUIT'}:
        exit('Goodbye')
    else:
        global gfxNameFile
        gfxNameFile = input("Enter GFX name including .dds or other file format. Type quit to quit.")
        confirmation()
def confirmation():
    if gfxNameFile in {'Quit', 'quit', 'QUIT'}: 
        exit()
    else:
        print(gfxName)
        print(gfxNameFile)
        sure = input('Are you sure?')
        if sure in {'y', 'Y'}:
            print('Confirmation Code Works!')
            time.sleep(3)
        elif sure in {'n', 'N'}:
            exit('Exit Code Works!')
        else:
            print("Please Enter Y or N")
            time.sleep(3)
            confirmation()
goalshineinput()
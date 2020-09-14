import time
def goalshineinput(): #gets gfx names for print
    global gfxName
    gfxName = input("Enter GFX name exluding .dds or other file format. Type quit to quit.")
    if gfxName in {'quit', 'Quit', 'QUIT'}:
        exit('Goodbye')
    else:
        global gfxNameFile
        gfxNameFile = input("Enter GFX name including .dds or other file format. Type quit to quit.")
        confirmation()
def confirmation(): #confirms the user wants those, if not, quits program (make it rerun goalshineinput at some point)
    if gfxNameFile in {'Quit', 'quit', 'QUIT'}: 
        exit()
    else:
        print(gfxName)
        print(gfxNameFile)
        sure = input('Are you sure? Y|N')
        if sure in {'y', 'Y'}:
            print('Confirmation Code Works!')
            time.sleep(3)
        elif sure in {'n', 'N'}:
            goalshineinput()
        else:
            print("Please Enter Y or N")
            time.sleep(3)
            confirmation()
goalshineinput()

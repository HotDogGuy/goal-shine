import time
import sys
def goalshineinput(): #gets gfx names for print
    global gfxName #name of file without .dds
    gfxName = input("Enter GFX name exluding .dds or other file format. Type quit to quit.")
    if gfxName in {'quit', 'Quit', 'QUIT'}: #used to exit if quit is typed in
        sys.exit('Goodbye')
    else:
        global gfxNameFile #name of file with .dds
        gfxNameFile = input("Enter GFX name including .dds or other file format. Type quit to quit.")
        confirmation()
def confirmation(): #confirms the user wants those, if not, restarts goalshineinput
    if gfxNameFile in {'Quit', 'quit', 'QUIT'}: #used to exit if quit is typed in
        sys.exit('Goodbye')
    else:
        print(gfxName) #for testing, combine into complete sentence
        print(gfxNameFile) #for testing, combine into complete sentence
        sure = input('Are you sure? Y|N')
        if sure in {'y', 'Y'}:
            print('Confirmation Code Works!')
            goalshinework()
        elif sure in {'n', 'N'}:
            goalshineinput()
        else:
            print("Please Enter Y or N")
            time.sleep(2)
            confirmation()
def goalshinework(): #creates the thing to be printed
    print('SpriteType = {')
    print('\t''name = ''\"' + gfxName + '\"')
    print('\t''texturefile = ''\"''gfx/interface/goals/' + gfxNameFile + '\"')
    time.sleep(3)
goalshineinput()

import time
import sys
sys.stdout = open("output.txt", "w") #save output
sys.stdin = open("input.txt", "w") #save input
def goalshineinput(): #gets gfx names for print
    global gfxName
    gfxName = input("Enter GFX name exluding .dds or other file format. Type quit to quit.")
    if gfxName in {'quit', 'Quit', 'QUIT'}:
        exit('Goodbye')
    else:
        global gfxNameFile
        gfxNameFile = input("Enter GFX name including .dds or other file format. Type quit to quit.")
        confirmation()
def confirmation(): #confirms the user wants those, if not, quits program
    if gfxNameFile in {'Quit', 'quit', 'QUIT'}: 
        exit()
    else:
        print(gfxName)
        print(gfxNameFile)
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
    sys.stdin.close()
    sys.stdout.close()
goalshineinput()

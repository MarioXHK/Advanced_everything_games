import pygame
from foreverglobals import illegals

def keyboard(onlyNums = False):
    if not pygame.scrap.get_init():
        pygame.scrap.init()
    shiftKey = False
    ctrlKey = False
    returnKey = ""
    for event in pygame.event.get(): #Keyboard logging!!
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            returnKey = "escape"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                returnKey = "end"
            elif event.key == pygame.K_BACKSPACE:
                returnKey = "back"
            elif (not onlyNums) and event.key == pygame.K_SPACE:
                returnKey = " "
            elif event.key == pygame.K_1:
                returnKey = "1"
            elif event.key == pygame.K_2:
                returnKey = "2"
            elif event.key == pygame.K_3:
                returnKey = "3"
            elif event.key == pygame.K_4:
                returnKey = "4"
            elif event.key == pygame.K_5:
                returnKey = "5"
            elif event.key == pygame.K_6:
                returnKey = "6"
            elif event.key == pygame.K_7:
                returnKey = "7"
            elif event.key == pygame.K_8:
                returnKey = "8"
            elif event.key == pygame.K_9:
                returnKey = "9"
            elif event.key == pygame.K_0:
                returnKey = "0"
            elif not onlyNums:
                if event.key == pygame.K_MINUS:
                    returnKey = "-"
                elif event.key == pygame.K_EQUALS:
                    returnKey = "2"
                elif event.key == pygame.K_EXCLAIM:
                    returnKey = "!"
                elif event.key == pygame.K_AT:
                    returnKey = "@"
                elif event.key == pygame.K_DOLLAR:
                    returnKey = "$"
                elif event.key == pygame.K_PERCENT:
                    returnKey = "%"
                elif event.key == pygame.K_CARET:
                    returnKey = "^"
                elif event.key == pygame.K_AMPERSAND:
                    returnKey = "&"
                elif event.key == pygame.K_LEFTPAREN:
                    returnKey = "("
                elif event.key == pygame.K_RIGHTPAREN:
                    returnKey = ")"
                elif event.key == pygame.K_UNDERSCORE:
                    returnKey = "_"
                elif event.key == pygame.K_PLUS:
                    returnKey = "+"
                elif event.key == pygame.K_q:
                    returnKey = "q"
                elif event.key == pygame.K_w:
                    returnKey = "w"
                elif event.key == pygame.K_e:
                    returnKey = "e"
                elif event.key == pygame.K_r:
                    returnKey = "r"
                elif event.key == pygame.K_t:
                    returnKey = "t"
                elif event.key == pygame.K_y:
                    returnKey = "y"
                elif event.key == pygame.K_u:
                    returnKey = "u"
                elif event.key == pygame.K_i:
                    returnKey = "i"
                elif event.key == pygame.K_o:
                    returnKey = "o"
                elif event.key == pygame.K_p:
                    returnKey = "p"
                elif event.key == pygame.K_LEFTBRACKET:
                    returnKey = "["
                elif event.key == pygame.K_RIGHTBRACKET:
                    returnKey = "]"
                elif event.key == pygame.K_a:
                    returnKey = "a"
                elif event.key == pygame.K_s:
                    returnKey = "s"
                elif event.key == pygame.K_d:
                    returnKey = "d"
                elif event.key == pygame.K_f:
                    returnKey = "f"
                elif event.key == pygame.K_g:
                    returnKey = "g"
                elif event.key == pygame.K_h:
                    returnKey = "h"
                elif event.key == pygame.K_j:
                    returnKey = "j"
                elif event.key == pygame.K_k:
                    returnKey = "k"
                elif event.key == pygame.K_l:
                    returnKey = "l"
                elif event.key == pygame.K_SEMICOLON:
                    returnKey = ";"
                elif event.key == pygame.K_QUOTE:
                    returnKey = "'"
                elif event.key == pygame.K_z:
                    returnKey = "z"
                elif event.key == pygame.K_x:
                    returnKey = "x"
                elif event.key == pygame.K_c:
                    returnKey = "c"
                elif event.key == pygame.K_v:
                    returnKey = "v"
                elif event.key == pygame.K_b:
                    returnKey = "b"
                elif event.key == pygame.K_n:
                    returnKey = "n"
                elif event.key == pygame.K_m:
                    returnKey = "m"
                elif event.key == pygame.K_COMMA:
                    returnKey = ","
                elif event.key == pygame.K_PERIOD:
                    returnKey = "."
                elif event.key == pygame.K_SLASH:
                    returnKey = "/"
    
    if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
        shiftKey = True
    if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
        ctrlKey = True

    unShiftable = ("end"," ","escape")
    if not onlyNums:
        if shiftKey:
            #Numbers being shifted
            if returnKey == "1":
                returnKey = "!"
            elif returnKey == "2":
                returnKey = "@"
            elif returnKey == "3":
                returnKey = "#"
            elif returnKey == "4":
                returnKey = "$"
            elif returnKey == "5":
                returnKey = "%"
            elif returnKey == "6":
                returnKey = "^"
            elif returnKey == "7":
                returnKey = "&"
            elif returnKey == "9":
                returnKey = "("
            elif returnKey == "0":
                returnKey = ")"
            #Symbols
            elif returnKey == "'":
                returnKey = "\""
            elif returnKey == "back":
                returnKey = "fullback"
            elif returnKey == "[":
                returnKey = "{"
            elif returnKey == "]":
                returnKey = "}"
            elif returnKey == "/":
                returnKey = ""
            elif not returnKey in unShiftable:
                returnKey = returnKey.upper()
        if ctrlKey:
            if returnKey.lower() == "v":
                legal = True
                text = pygame.scrap.get(pygame.SCRAP_TEXT)
                text = str(text)[2:-5]
                if "//" in text or text[0] == "/":
                    print("Cannot paste text with blank path!")
                    legal = False
                else:
                    for l in text:
                        if l in illegals:
                            print("Cannot paste text with illegal characters!")
                            legal = False
                            break
                if legal:
                    returnKey = str(text)
                else:
                    returnKey = ""
    return returnKey

print("You'll need your keyboard for this~")
import pygame

def keyboard():
    shiftKey = False
    returnKey = ""
    for event in pygame.event.get(): #Keyboard logging!!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                returnKey = "end"
            elif event.key == pygame.K_SPACE:
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
            elif event.key == pygame.K_MINUS:
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
                returnKey = "quotationmarks"
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
            elif event.key == pygame.K_BACKSPACE:
                returnKey = "back"
    
    if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        shiftKey = True

    unShiftable = ("end"," ")
    
    if shiftKey:
        if returnKey == "quotationmarks":
            returnKey = "'"
        elif returnKey == "back":
            returnKey = "fullback"
        elif returnKey == "[":
            returnKey = "{"
        elif returnKey == "]":
            returnKey = "}"
        elif not returnKey in unShiftable:
            returnKey = returnKey.upper()
    return returnKey
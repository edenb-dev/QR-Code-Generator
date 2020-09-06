
# ------------------------ Useful ------------------------- #

# Help's Converting Hex To RGB/RGBA Values.


def Hex_To_RGB(Hex):

    # Input: #ff00ff -> Output: (255,0,255)

    Hex = Hex.lstrip('#')  # Striping From The Start The '#' Character(s).
    Parsing_Base = 16

    return str(tuple(int(Hex[Range:Range+2], Parsing_Base) for Range in (0, 2, 4)))


def Insert_To_String(Source_String, Insert_String, Position):

    return Source_String[:Position] + Insert_String + Source_String[Position:]


def Hex_To_RGBA(Hex_Color, Alpha):

    RGB_Color = Hex_To_RGB(Hex_Color)  # Parsing The Hex Color To RGB.

    return Insert_To_String(RGB_Color, ', ' + str(Alpha), len(RGB_Color)-1)

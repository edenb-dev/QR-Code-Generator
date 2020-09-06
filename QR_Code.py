from io import BytesIO
import qrcode


def Generate_QR_Image(Text, Fill_Color="#000000", Background_Color="#ffffff", File_Format="JPEG"):

    QR_Manager = qrcode.QRCode(  # Settings Of The QR_Manager.
        version=None,  # When Set To None, Auto Assigned. ( Possible Version 1 - 40 )
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # ERROR_CORRECT_'L/M/Q/H' -> 7%/15%/25%/30% Error Correction.
        box_size=10,  # Pixel Rendering.
        border=2)     # Setting The Border.

    QR_Manager.add_data(Text)   # Adding The Text.
    QR_Manager.make(fit=True)   # Detecting The Best Version To Use.

    QR_Image = QR_Manager.make_image(fill_color=Fill_Color, back_color=Background_Color)  # Generating The Image.

    Buffered = BytesIO()  # Creating The Buffer.
    QR_Image.save(Buffered, format=File_Format)  # Saving The Image To The Buffer.

    return Buffered.getvalue()  # Returning The Bytes Of The Image.


# ------------------------ Imports ------------------------ #

import sys

from QR_Code import Generate_QR_Image
from GUI_Helper_Functions import Hex_To_RGB, Hex_To_RGBA

# ---- PyQt5 - GUI ---- #

from PyQt5.QtWidgets import QGraphicsDropShadowEffect  # Effects.
from PyQt5.QtWidgets import QApplication, QDesktopWidget  # Must Elements.
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFileDialog  # Elements.

from PyQt5.QtGui import QIcon, QPixmap  # Image.
from PyQt5.QtGui import QPainter, QBrush, QColor  # Painter.
from PyQt5.QtGui import QFontDatabase  # Font Loader.

from PyQt5.QtCore import Qt  # Enums.
from PyQt5.QtCore import QRect, QSize  # Frame.

# ---------------------- Imports End ---------------------- #


def Main():  # Starting The GUI App.

    # Setting The App.

    App = QApplication(sys.argv)    # Initializing The App.
    Main_Window = Window()          # Loading The Window. ( GUI )
    sys.exit(App.exec())            # Closing The App.


# --------------------- GUI Elements ---------------------- #

class Window(QWidget):

    # --------------------- Initializing ---------------------- #

    def __init__(self):

        super().__init__()

        # Getting The User's Screen Resolution.
        ScreenGeometry = QDesktopWidget().screenGeometry()
        Window_Resolution = 9/16

        self.Title = "QR Code Generator"

        self.Width = ScreenGeometry.width() / 1.5
        self.Height = self.Width * Window_Resolution

        self.Left = (ScreenGeometry.width() - self.Width) / 2
        self.Top = (ScreenGeometry.height() - self.Height) / 2

        self.InitWindow()

    def InitWindow(self):

        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.Title)
        self.setGeometry(self.Left, self.Top, self.Width, self.Height)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('''
                                    Window {
                                                background: QLinearGradient(x1:0,y1:0,x2:1,y2:1,stop:0 #6600cc ,stop: .9 #cc00cc, stop: 1 #ff00ff);
                                        }                     
                            ''')

        # Setting The Focus.
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus(True)

        self.setFixedSize(self.Width, self.Height)

        self.show()

        self.On_Window_Loaded()  # Loading All The GUI Elements

    # ------------ Creating & Loading GUI Elements ------------ #

    def On_Window_Loaded(self):

        if (True):  # Loading Assets.

            # Loading The Font, From A File.
            QFontDatabase().addApplicationFont("./Assets/Fonts/Cabin-Bold.ttf")

        if (True):  # Creating And Loading The GUI.

            self.GUI_Labels()

            self.GUI_LineEdits()

            self.GUI_Buttons()

            self.GUI_Images()

            self.GUI_Banner()

        if (True):  # Loading Credits.

            self.Show_QR_Image('Created by Eden Boaron.\nGit : github.com/edenb-dev\nSite : edenb-dev.com\nEmail : edenb.dev@gmail.com')

    def GUI_Labels(self):

        if (True):  # Initializing.

            # Setting The Labels Data.
            Labels = [
                {'Text': 'QR',
                    'Left': self.Width * 0.05, 'Top': self.Height * -0.02,
                 'Font_Size': int(self.Height * 0.54),
                    'Text_Color': Hex_To_RGBA("#ffffff", 0.4)},
                {'Text': 'Code Generator',
                    'Left': self.Width * 0.07, 'Top': self.Height * 0.18,
                 'Font_Size': int(self.Height * 0.14),
                 'Text_Color': Hex_To_RGBA("#ffffff", 1)},
                {'Text': 'Turn any piece of text into a QR code.',
                 'Left': self.Width * 0.08, 'Top': self.Height * 0.35,
                 'Font_Size': int(self.Height * 0.03),
                 'Text_Color': Hex_To_RGBA("#ffffff", 1)}]

        if (True):  # Creating The Labels.

            for Label_Data in Labels:

                StyleSheet = ('''
                                    QLabel{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                    }}
                                    ''').format(**Label_Data)

                Label = QLabel(Label_Data.get('Text'), self)  # Creating A Label, With The Given Text.
                Label.setStyleSheet(StyleSheet)  # Setting The StyleSheets.
                Label.move(Label_Data.get('Left'), Label_Data.get('Top'))  # Moving The Label.
                Label.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3))  # Adding Shadow Effect.

                Label.show()  # Showing The Label.

    def GUI_LineEdits(self):

        if (True):  # Initializing.

            # Setting The LineEdits Data.
            LineEdits = [
                {'PlaceHolder_Text': 'Enter Text',
                 'Left': self.Width*0.07, 'Top': self.Height*0.56,
                 'Width': self.Width*0.25, 'Height': self.Height*0.10,
                 'Font_Size': int(self.Height*0.03),
                 'Padding_Left': self.Height*0.03, 'Padding_Right': self.Height*0.03,
                 'Text_Color': Hex_To_RGBA("#000000", 0.8),
                 'Background_Color': Hex_To_RGBA("#ffffff", 0.4),
                 'Round': self.Height*0.05}]

        if (True):  # Creating The LineEdits.

            for LineEdit_Data in LineEdits:

                StyleSheet = ('''
                                    QLineEdit{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                        padding-left: {Padding_Left}px;
                                        padding-right: {Padding_Right}px;
                                        background-color: rgba{Background_Color};
                                        border-radius: {Round}px;

                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}
                                    ''').format(**LineEdit_Data)

                self.LineEdit = QLineEdit(self)
                self.LineEdit.setPlaceholderText(LineEdit_Data.get('PlaceHolder_Text'))
                self.LineEdit.setStyleSheet(StyleSheet)  # Setting The StyleSheets.
                self.LineEdit.move(LineEdit_Data.get('Left'), LineEdit_Data.get('Top'))  # Moving The LineEdit.
                self.LineEdit.show()

    def GUI_Buttons(self):

        if (True):  # Initializing.

            # Setting The Buttons Data.
            Buttons = [
                {'Text': 'Generate QR',
                 'Left': self.Width*0.39, 'Top': self.Height*0.56,
                 'Width': self.Width*0.25, 'Height': self.Height*0.10,
                         'Font_Size': int(self.Height*0.03),
                 'Text_Color': Hex_To_RGBA("#ffffff", 0.9),
                 'Background_Color': Hex_To_RGBA("#e30053", 0.9),
                 'Hover_Background_Color': Hex_To_RGBA("#fa0a62", 0.9),
                 'Pressed_Background_Color': Hex_To_RGBA("#d7004f", 0.9),
                 'Round_Top_Left': self.Height*0.05, 'Round_Top_Right': self.Height*0.05,
                 'Round_Bottom_Left': 0, 'Round_Bottom_Right': self.Height*0.05,
                         'Object_Name': 'Generate QR'},
                {'Text': '',
                 'Left': self.Width*0.7, 'Top': self.Height*0.61,
                 'Width': self.Height*0.38, 'Height': self.Height*0.05,
                         'Font_Size': int(self.Height*0.03),
                         'Text_Color': Hex_To_RGBA("#ffffff", 1),
                         'Background_Color': Hex_To_RGBA("#ffffff", 0.25),
                         'Hover_Background_Color': Hex_To_RGBA("#ffffff", 0.15),
                         'Pressed_Background_Color': Hex_To_RGBA("#ffffff", 0.4),
                 'Round_Top_Left': 0, 'Round_Top_Right': 0,
                 'Round_Bottom_Left': self.Height*0.05, 'Round_Bottom_Right': self.Height*0.05,
                         'Image': 'Assets/Images/download-white-64x64.png',
                 'Image_Width': self.Height*0.025, 'Image_Height': self.Height*0.025,
                         'Object_Name': 'Download'}]

        if (True):  # Creating The Buttons.

            for Button_Data in Buttons:

                StyleSheet = ('''
                                    QPushButton{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                        background-color: rgba{Background_Color};
                                        
                                        border-top-left-radius: {Round_Top_Left}px;
                                        border-top-right-radius: {Round_Top_Right}px;
                                        border-bottom-left-radius: {Round_Bottom_Left}px;
                                        border-bottom-right-radius: {Round_Bottom_Right}px;

                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}

                                    QPushButton:hover{{
                                        background-color: rgba{Hover_Background_Color};
                                    }}

                                    QPushButton:pressed{{
                                        background-color: rgba{Pressed_Background_Color};
                                    }}
                                    ''').format(**Button_Data)

                Button = QPushButton(Button_Data.get('Text'), self)
                Button.setStyleSheet(StyleSheet)  # Setting The StyleSheets.
                Button.move(Button_Data.get('Left'), Button_Data.get('Top'))  # Moving The Button.
                Button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3))  # Adding Shadow Effect.
                Button.clicked.connect(self.on_Click)
                Button.setObjectName(Button_Data.get('Object_Name'))

                if ('Image' in Button_Data):  # Adding Image.

                    Button.setIcon(QIcon(Button_Data.get('Image')))
                    Button.setIconSize(QSize(Button_Data.get('Image_Width'), Button_Data.get('Image_Height')))

                Button.show()

    def GUI_Images(self):

        if (True):  # Initializing.

            # Setting The Images Data.
            Images = [
                {'Left': self.Width*0.7, 'Top': self.Height*0.23,
                 'Width': self.Height*0.38, 'Height': self.Height*0.38}]

        if (True):  # Creating The Buttons.

            for Image_Data in Images:

                StyleSheet = ('''
                                    QLabel{{
                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}
                                    ''').format(**Image_Data)

                self.Image = QLabel(self)
                self.Image.setStyleSheet(StyleSheet)  # Setting The StyleSheets.
                self.Image.move(Image_Data.get('Left'), Image_Data.get('Top'))  # Moving The Label.
                self.Image.setScaledContents(True)
                self.Image.setFixedSize(Image_Data.get('Width'), Image_Data.get('Height'))

                self.Image.show()

    def GUI_Banner(self):

        if (True):  # Initializing.

            # Setting The Banner Location.
            Banner_Left, Banner_Top = 0, self.Height*0.75

            # Setting The Block Sizes.
            Block_Width, Block_Height = self.Width, self.Height * 0.15

            # Setting The Blocks Data.
            Banner_Blocks = [
                {'Left': 0, 'Top': self.Height * 0.18, 'Opacity': 0.4, 'Rotation': -5},
                {'Left': 0, 'Top': self.Height * 0.2, 'Opacity': 0.4, 'Rotation': -5},
                {'Left': 0, 'Top': self.Height * 0.05, 'Opacity': 1, 'Rotation': 7},
                {'Left': 0, 'Top': self.Height * 0.15, 'Opacity': 1, 'Rotation': 0}]

        if (True):  # Creating The Blocks.

            for Block in Banner_Blocks:

                Banner_Block(Parent=self,
                             Banner_Left=Banner_Left, Banner_Top=Banner_Top,
                             Left=Block.get('Left'), Top=Block.get('Top'),
                             Width=Block_Width, Height=Block_Height,
                             Opacity=Block.get('Opacity'), Rotation=Block.get('Rotation'))

    # ------------------ QR & GUI Functions ------------------- #

    def Show_QR_Image(self, Text):
        '''
            Generating And Showing The QR Code, Based On The Given Text.
        '''

        self.QR_Manager = Generate_QR_Image(Text, File_Format="PNG")  # Generating The Bytes Of The QR Code.

        Pixmap = QPixmap()
        Pixmap.loadFromData(self.QR_Manager)  # Loading The Bytes Of The QR Code Into A Image.

        self.Image.setPixmap(Pixmap)  # Setting The New Image.

    def Save_QR_Image(self):
        '''
            Opening The File Dialog. 
            After The User Clicks "Save", The QR Image Will Be Saved.
        '''

        # Opening File Dialog.
        File_Path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "QR Image", "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpeg)")

        if File_Path:  # Checking If The User Chosen Save In The FileDialog.

            with open(File_Path, 'wb') as File:  # Saving The QR Image.
                File.write(self.QR_Manager)

    # ------------------------ Events ------------------------- #

    # ----- Button Click Event ------ #

    def on_Click(self):

        # Checking Button Clicks.
        if (self.sender().objectName() == 'Generate QR'):  # Generating The QR Image.

            self.Show_QR_Image(self.LineEdit.text())  # Generating And Displaying The QR Image, Based On The User Input.

        elif (self.sender().objectName() == 'Download'):  # Saving The Image.

            self.Save_QR_Image()  # Loading The File Dialog, And Saving The QR Image.


class Banner_Block(QWidget):

    # --------------------- Initializing ---------------------- #

    def __init__(self, Parent, Banner_Left, Banner_Top, Left, Top, Width, Height, Opacity, Rotation):

        super().__init__(Parent)

        self.Parent = Parent

        self.Left = Left
        self.Top = Top
        self.Width = Width
        self.Height = Height
        self.Opacity = Opacity
        self.Rotation = Rotation
        self.Banner_Left = Banner_Left
        self.Banner_Top = Banner_Top

        self.InitWindow()

    def InitWindow(self):

        self.setGeometry(self.Banner_Left, self.Banner_Top, self.Parent.frameGeometry().width()-self.Banner_Left, self.Parent.frameGeometry().height()-self.Banner_Top)
        self.show()

    # --------------------- Paint Event ----------------------- #

    def paintEvent(self, Event):
        '''
            Drawing The Banner Based On The Initialization Data.
        '''

        Painter = QPainter(self)

        Brush = QBrush(QColor('#ffffff'), Qt.SolidPattern)  # Setting The Brush.
        Rect = QRect(self.Left, self.Top, self.Width, self.Height)  # Setting The Rectangle.

        Painter.setRenderHint(QPainter.HighQualityAntialiasing)  # Adding AA.
        Painter.setOpacity(self.Opacity)  # Setting The Opacity.
        Painter.rotate(self.Rotation)  # Rotating The Frame.
        Painter.fillRect(Rect, Brush)  # Drawing The Frame.

        Painter.end()


if __name__ == "__main__":

    Main()

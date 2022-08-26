# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timelapse_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog, QApplication, QSlider
import os, sys
from time import sleep
from datetime import datetime
from numpy import uint8, fromfile
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 669)
        
        ################################################
        ########### STATIC SETUP #######################
        ################################################
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        #MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_ipnut_folder = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_ipnut_folder.setGeometry(QtCore.QRect(480, 170, 27, 22))
        self.toolButton_ipnut_folder.setObjectName("toolButton_ipnut_folder")
        self.label_input_folder = QtWidgets.QLabel(self.centralwidget)
        self.label_input_folder.setGeometry(QtCore.QRect(70, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input_folder.setFont(font)
        self.label_input_folder.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_input_folder.setObjectName("label_input_folder")
        self.toolButton_output_folder = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_output_folder.setGeometry(QtCore.QRect(480, 220, 27, 22))
        self.toolButton_output_folder.setObjectName("toolButton_output_folder")
        self.label_output_folder = QtWidgets.QLabel(self.centralwidget)
        self.label_output_folder.setGeometry(QtCore.QRect(70, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_output_folder.setFont(font)
        self.label_output_folder.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_output_folder.setObjectName("label_output_folder")
        self.comboBox_video_format = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_video_format.setGeometry(QtCore.QRect(240, 270, 231, 22))
        self.comboBox_video_format.setObjectName("comboBox_video_format")
        self.comboBox_video_format.addItem('')
        
        self.label_video_format = QtWidgets.QLabel(self.centralwidget)
        self.label_video_format.setGeometry(QtCore.QRect(50, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_video_format.setFont(font)
        self.label_video_format.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_video_format.setObjectName("label_video_format")
        self.label_fps = QtWidgets.QLabel(self.centralwidget)
        self.label_fps.setGeometry(QtCore.QRect(50, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_fps.setFont(font)
        self.label_fps.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_fps.setObjectName("label_fps")
        self.fps_slider = QtWidgets.QSlider(self.centralwidget)
        self.fps_slider.setGeometry(QtCore.QRect(240, 320, 231, 22))
        self.fps_slider.setAutoFillBackground(False)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(120)
        self.fps_slider.setSliderPosition(25)
        self.fps_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fps_slider.setObjectName("fps_slider")
        self.pushButton_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_convert.setEnabled(True)
        self.pushButton_convert.setGeometry(QtCore.QRect(240, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_convert.setFont(font)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 160, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(240, 430, 291, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.lineEdit_input_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input_folder.setGeometry(QtCore.QRect(240, 170, 231, 22))
        self.lineEdit_input_folder.setObjectName("lineEdit_input_folder")
        self.lineEdit_output_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output_folder.setGeometry(QtCore.QRect(240, 220, 231, 22))
        self.lineEdit_output_folder.setObjectName("lineEdit_output_folder")
        self.label_app_name = QtWidgets.QLabel(self.centralwidget)
        self.label_app_name.setGeometry(QtCore.QRect(70, 40, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_app_name.setFont(font)
        self.label_app_name.setObjectName("label_app_name")
        self.label_fps_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_fps_2.setGeometry(QtCore.QRect(490, 320, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_fps_2.setFont(font)
        self.label_fps_2.setObjectName("label_fps_2")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setEnabled(True)
        self.pushButton_quit.setGeometry(QtCore.QRect(890, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_quit.setFont(font)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.label_image_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_image_preview.setGeometry(QtCore.QRect(570, 160, 461, 291))
        self.label_image_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_preview.setObjectName("label_image_preview")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(570, 160, 461, 291))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        
        self.label_image_preview.setGeometry(QtCore.QRect(570, 160, 461, 291))
        self.label_image_preview.setAlignment(QtCore.Qt.AlignCenter)

        self.label_image_preview.setObjectName("label_image_preview")

        self.pushButton_about = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_about.setEnabled(True)
        self.pushButton_about.setGeometry(QtCore.QRect(730, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_about.setFont(font)
        self.pushButton_about.setObjectName("pushButton_about")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 490, 471, 101))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        #####################################################################
        # fill for testing purposes
        #####################################################################
        
        # self.lineEdit_input_folder.setText("C:\\Users\\jirka\\OneDrive\\Dokumenty\\PythonScripts\\Open CV\\timelapseTool\\stock\\")
        # self.lineEdit_output_folder.setText("C:\\Users\\jirka\\OneDrive\\Dokumenty\\PythonScripts\\Open CV\\timelapseTool\\")
        

        #####################################################################
        # END OF fill for testing purposes
        #####################################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JJ - Timelapse tool"))
        self.toolButton_ipnut_folder.setText(_translate("MainWindow", "..."))
        self.label_input_folder.setText(_translate("MainWindow", "Input folder:"))
        self.toolButton_output_folder.setText(_translate("MainWindow", "..."))
        self.label_output_folder.setText(_translate("MainWindow", "Output folder:"))
        self.label_video_format.setText(_translate("MainWindow", "Video format:"))
        self.label_fps.setText(_translate("MainWindow", "FPS:"))
        self.pushButton_convert.setText(_translate("MainWindow", "Check files"))
        self.label_app_name.setText(_translate("MainWindow", "JJ - Timelapse tool"))
        self.label_fps_2.setText(_translate("MainWindow", "25"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_about.setText(_translate("MainWindow", "About"))
        self.label_image_preview.setText(_translate("MainWindow", "Preview"))

        



        
        ################################################
        ########### VARIABLES ##########################
        ################################################
        # check if all the input pictures are fine and ready to use
        self.files_checked = False
        # variable is true while process of control of video writing is in progress. During this time the button is a "cancel button"
        self.in_process = False
        # flag which orders to abort current process (checking files or creating video)
        self.abort_process = False
        # video formats available
        self.format_dict = {'mp4':'XVID','avi':'MJPG'}
        # fast check if the input folder content has been somehow changed since last checked
        self.files_list_check = None
        # characters allowed for output file path (cv2.videoWriter will not create the video with special characters in the path) 
        self.allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .,:;+-/_&()[]{}"


        

        ################################################
        ########### ACTIONS ############################
        ################################################
        self.toolButton_ipnut_folder.clicked.connect(self.select_input_folder) 
        self.toolButton_output_folder.clicked.connect(self.select_output_folder) 
        self.pushButton_quit.clicked.connect(self.quit_timelapse_app)
        self.fps_slider.valueChanged.connect(self.update_slider)
        self.pushButton_convert.clicked.connect(self.convert_button)
        self.lineEdit_input_folder.textChanged.connect(self.input_folder_changed)

        self.pushButton_about.clicked.connect(self.about_function)

        # initialize comboBox_video_format
        self.fill_comboBox_video_format()






    def about_function(self):
        about_msg = QtWidgets.QMessageBox()
        about_msg.setText("\nAuthor: \t\t Jiri Jiruska\n" + \
        "Version: \t\t 1.0\n" + \
        "Contact:\t\t dzejdzejemail@seznam.cz\t\t\n\n")
        about_msg.setWindowTitle("About application")
        about_msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        ex = about_msg.exec_()
        
        


    
    def fill_comboBox_video_format(self):
        for f in list(self.format_dict.keys()):
            self.comboBox_video_format.addItem(f.upper())
        self.comboBox_video_format.setCurrentIndex(0)


    
    def select_input_folder(self):
        filename = str(QFileDialog.getExistingDirectory()) + "/"
        self.lineEdit_input_folder.setText(filename)
        print(filename)
    
    def select_output_folder(self):
        filename = str(QFileDialog.getExistingDirectory()) + "/"
        self.lineEdit_output_folder.setText(filename)

    def quit_timelapse_app(self):
        QApplication.quit()

    def update_slider(self):
        self.label_fps_2.setText(str(self.fps_slider.value()))

    def set_files_checked(self, val):
        self.files_checked = val

    def is_checked(self):
        return self.files_checked

    # if one of input parameters changes, forbid to convert files. Another check/load is needed
    def input_folder_changed(self):
        self.pushButton_convert.setText("Check files")
        self.set_files_checked(False)

        
        
    # path have to be in a right format with forward slash. Every back slahes change to forward slashes
    def check_path(self, path: str):
        if len(path) > 0:
            path = list(path)
            for index in range(len(path)):
                if path[index] == '\\':
                    path[index] = '/'
            if path[-1] != '/':
                path.append('/')
            path = ''.join(path)
            return path


    def check_special_characters(self, path: str, allowed_characters: str):
        if len(path) > 0:
            for char in path:
                if not char in allowed_characters:
                    return char
            return False    
            # self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Please don't use any special characters in output file, such as '{a}.".format(a=char))


    def convert_button(self):

        # if in process (checking or converting), do nothing from here, but cancle the process by if statement in the particular function
        if self.in_process:
            self.abort_process = True
            return

        if self.is_checked():
            self.create_video()

        else:
            self.load_files()




    def load_files(self):
        # check the path format by check_path function
        self.lineEdit_input_folder.setText(self.check_path(self.lineEdit_input_folder.text())) 
        home_dir = self.lineEdit_input_folder.text()
        #################### Check if folder contains images ###########################
        if not os.path.exists(home_dir):
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "The input folder path doesn't exist.")
            return
        if len(os.listdir(home_dir)) == 0:
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Selected input folder is empty") 
            return
        last_name, last_extention = os.path.splitext(os.listdir(home_dir)[0])
        for filename in os.listdir(home_dir):
            name, extention = os.path.splitext(filename)
            if extention.lower() != ".jpg" and \
                extention.lower() != ".png":
                self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + \
                    "File \"{a}\" has unknown format. Only .jpg and .png is supported.".format(a=name + extention))
                return
            if last_extention != extention:
                self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + \
                    "File {a} and {b} have different format. All the files in the folder must have the same format.".format(a=last_name + last_extention, b=name + extention)) 
                return
            last_extention = extention
            last_name = name

        #################### Check if all images have the same size ###########################   
        # previous_img = cv2.imread(home_dir + os.listdir(home_dir)[0])
        previous_img = cv2.imdecode(fromfile(home_dir + os.listdir(home_dir)[0], dtype=uint8), cv2.IMREAD_UNCHANGED)
        prev_size = previous_img.shape
        print(prev_size)
        progress = 1
        self.progressBar.setVisible(True)
        self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Checking...")
        for filename in os.listdir(home_dir):
            
            # img = cv2.imread(home_dir + filename)
            img = cv2.imdecode(fromfile(home_dir + filename, dtype=uint8), cv2.IMREAD_UNCHANGED)
            size = img.shape
            if prev_size != size:
                self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Pictures doesn't have the same resolution. Check the file {a}.".format(a=filename))   
                self.progressBar.setVisible(False)
                self.pushButton_convert.setText("Convert")
                self.in_process = False
                return

            prev_size = size

            self.progressBar.setValue(int(progress / len(os.listdir(home_dir)) * 100))    
            cv2.waitKey(1)               
            progress += 1
            print(filename)
            self.in_process = True
            self.pushButton_convert.setText("Cancel")
            if self.abort_process:
                self.abort_process = False
                self.in_process = False
                
                self.progressBar.setValue(0)
                self.progressBar.setVisible(False)
                self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Files checking canceled.")
                self.pushButton_convert.setText("Check files")
                return


        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)
        self.in_process = False

        self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Files checked successfully!")
        self.textBrowser.append("\n{a} files".format(a=len(os.listdir(home_dir))))
        self.textBrowser.append("{a} fps".format(a=self.fps_slider.value()))
        self.textBrowser.append("Final time: {a} sec\n".format(a=len(os.listdir(home_dir)) / int(self.fps_slider.value())))
         
        self.pushButton_convert.setText("Convert")
        self.set_files_checked(True)
        # saved for later fast check is the directory content changed somehow
        self.files_list_check = os.listdir(home_dir)


        #################### Load the preview of the first picture ###########################   
        print(self.label_image_preview.width())
        print(self.label_image_preview.height())
        pixmap = QtGui.QPixmap(home_dir + os.listdir(home_dir)[0]).scaled(self.label_image_preview.width(),self.label_image_preview.height(), QtCore.Qt.KeepAspectRatio)
        #self.label_image_preview.setStyleSheet('background-color:black')
        self.label_image_preview.setPixmap(pixmap)
        self.groupBox.setVisible(False)


        
    def create_video(self):

        # check the path format by check_path function (change "\" na "/" and add "/" to the end, if not)
        self.lineEdit_output_folder.setText(self.check_path(self.lineEdit_output_folder.text())) 
        output_dir = self.lineEdit_output_folder.text()
        
        home_dir = self.lineEdit_input_folder.text()
        img_names_list = [home_dir + f for f in os.listdir(home_dir)]

        if not os.path.exists(output_dir) or len(output_dir) < 2:
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "The output folder doesn't exist.")
            return


        if self.comboBox_video_format.currentText() == '':
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Please select the video format.")
            return
        if self.files_list_check != os.listdir(home_dir):
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "The content of the input folder has changed. Files need to be reloaded and checked again.")
            self.set_files_checked(False)
            self.pushButton_convert.setText("Check files")
            return

        # check duplicity of output file name
        
        name = "video." + self.comboBox_video_format.currentText().lower()
        duplicity = True
        num = 1
        while duplicity == True:
            duplicity = False
            if name in os.listdir(output_dir):
                name = "video(" + str(num) + ")." + self.comboBox_video_format.currentText().lower()
                duplicity = True
                num += 1

        
        # check if there are only allowed characters in the path, otherwise cv2.VideoWriter will not create a video file (known python3 issue)
        path = output_dir + name
        print(path)
        char = self.check_special_characters(path, self.allowed_characters)
        if char:
            self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Please don't use any special characters in output file, such as '{a}'.".format(a=char))
            return        
        # fourcc is variable defining the compression format. Format is selected from "format_dict" based on selected option in "comboBox_video_format"
        fourcc = cv2.VideoWriter_fourcc(*self.format_dict[self.comboBox_video_format.currentText().lower()])

        # frame per second selected by "fps_slider" 
        fps = self.fps_slider.value()
        # resolution is excracted from first picture in input folder. "shape" comtains (width, height, depth), but we only use (width, height)
        # img = cv2.imread(self.lineEdit_input_folder.text() + os.listdir(self.lineEdit_input_folder.text())[0])
        img = cv2.imdecode(fromfile(self.lineEdit_input_folder.text() + os.listdir(self.lineEdit_input_folder.text())[0], dtype=uint8), cv2.IMREAD_UNCHANGED)
        resolution = tuple(list(img.shape)[1::-1])
        
        # >>>>>>>>>   creates the empty video instance which will be filled by pictures later on  <<<<<<<<<<
        videowriter = cv2.VideoWriter(path , fourcc, fps, resolution)
        counter = 1
        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)
        self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Creating video...")


        for image_name in img_names_list:
            
            # img = cv2.imread(image_name)
            img = cv2.imdecode(fromfile(image_name, dtype=uint8), cv2.IMREAD_UNCHANGED)
            videowriter.write(img)

            self.progressBar.setValue(int(counter / len(os.listdir(home_dir)) * 100))
            cv2.waitKey(1)                          
            #print(int(counter / len(os.listdir(home_dir)) * 100))
            counter += 1
            self.in_process = True
            self.pushButton_convert.setText("Cancel")
            if self.abort_process:
                self.abort_process = False
                self.in_process = False
                self.pushButton_convert.setText("Convert")
                self.progressBar.setVisible(False)
                self.progressBar.setValue(0)
                self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Video processing has been canceled.")
                videowriter.release()
                os.remove(path)
                return
                

        videowriter.release()

        self.in_process = False
        self.pushButton_convert.setText("Convert")
        self.progressBar.setVisible(False)
        self.progressBar.setValue(0)
        self.textBrowser.append(datetime.now().strftime("%H:%M:%S: ") + "Video is completed!")
        


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import cm
import matplotlib.ticker as ticker
import matplotlib.dates as dates
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import math
import psychrolib
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class loading_screen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QtWidgets.QLabel(self)
        self.gif_path = self.resource_path("loading.gif")
        self.movie = QMovie(self.gif_path)
        self.label_animation.setMovie(self.movie)
        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(3000, self.stopAnimation)
        self.show()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = None
        if base_path != None:
            relative_path = os.path.join(base_path, relative_path)
        return relative_path

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.loading_screen = loading_screen()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(701, 398)
        self.ico_path = self.resource_path("PDC_logo.png")
        icon = QtGui.QIcon(self.ico_path)
        MainWindow.setWindowIcon(icon)
        MainWindow.setGeometry(100,100,701,398)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow::separator {\n"
        "    background: yellow;\n"
        "    width: 10px; /* when vertical */\n"
        "    height: 10px; /* when horizontal */\n"
        "}\n"
        "QMainWindow{\n"
        "    background: #E0E0E0;\n"
        "}\n"
        "QMenuBar::item {\n"
        "    padding: 1px 4px;\n"
        "    background: transparent;\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
        "    background: #CCFFCC;\n"
        "}\n"
        "\n"
        "QMenuBar::item:pressed {\n"
        "    background: #CCFFCC;\n"
        "}")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)

        self.file_input_widget()
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setShortcut("Ctrl+i")
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionChange_weather_data = QtWidgets.QAction(MainWindow)
        self.actionChange_weather_data.setShortcut("Ctrl+h")
        self.actionChange_weather_data.setObjectName("actionChange_weather_data")
        self.actionTerms_of_use = QtWidgets.QAction(MainWindow)
        self.actionTerms_of_use.setObjectName("actionTerms_of_use")
        self.actionUser_help = QtWidgets.QAction(MainWindow)
        self.actionUser_help.setObjectName("actionUser_help")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionInstructions)
        self.menuFile.addAction(self.actionChange_weather_data)
        self.menuFile.addAction(self.actionTerms_of_use)
        self.menuHelp.addAction(self.actionUser_help)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionInstructions.triggered.connect(lambda: self.instruction_window())
        self.actionTerms_of_use.triggered.connect(lambda: self.terms_of_use_window())
        self.actionAbout.triggered.connect(lambda: self.about_window())
        self.actionUser_help.triggered.connect(lambda: self.user_help_window())
        self.actionChange_weather_data.triggered.connect(lambda: self.back_page())

    def user_help_window(self):
        Dialog_user_help = QtWidgets.QDialog()
        Dialog_user_help.setObjectName("Dialog_user_help")
        Dialog_user_help.resize(737, 432)
        icon = QtGui.QIcon(self.ico_path)
        Dialog_user_help.setWindowIcon(icon)
        self.gridLayout_user_help = QtWidgets.QGridLayout(Dialog_user_help)
        self.gridLayout_user_help.setObjectName("gridLayout_user_help")
        self.horizontalLayout_user_help = QtWidgets.QHBoxLayout()
        self.horizontalLayout_user_help.setObjectName("horizontalLayout_user_help")
        self.treeWidget_user_help = QtWidgets.QTreeWidget(Dialog_user_help)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_user_help.sizePolicy().hasHeightForWidth())
        self.treeWidget_user_help.setSizePolicy(sizePolicy)
        self.treeWidget_user_help.setObjectName("treeWidget_user_help")
        self.treeWidget_user_help.setStyleSheet("QTreeView {\n"
                                                "    show-decoration-selected: 1;\n"
                                                "}\n"
                                                "QTreeView::item {\n"
                                                "     border: 1px solid #d9d9d9;\n"
                                                "    border-top-color: transparent;\n"
                                                "    border-bottom-color: transparent;\n"
                                                "}\n"
                                                "QTreeView::item:hover {\n"
                                                "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4169E1, stop: 1 #4169E1);\n"
                                                "    border: 1px solid #bfcde4;\n"
                                                "}\n"
                                                "QTreeView::item:selected {\n"
                                                "    border: 1px solid #567dbc;\n"
                                                "}\n"
                                                "QTreeView::item:selected:active{\n"
                                                "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
                                                "}\n"
                                                "QTreeView::item:selected:!active {\n"
                                                "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
                                                "}\n"
                                                "QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
                                                "    border-image: url(branch-end.png) 0;\n"
                                                "}")

        Dialog_user_help.setWindowTitle("Passive design consultant")
        self.treeWidget_user_help.headerItem().setText(0, "Tool Help", )
        __sortingEnabled = self.treeWidget_user_help.isSortingEnabled()
        self.treeWidget_user_help.setSortingEnabled(False)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_user_help)
        self.horizontalLayout_user_help.addWidget(self.treeWidget_user_help)
        self.textEdit_user_help = QtWidgets.QTextEdit(Dialog_user_help)
        self.textEdit_user_help.setAutoFillBackground(True)
        self.textEdit_user_help.setReadOnly(True)
        self.textEdit_user_help.setObjectName("textEdit_user_help")
        self.horizontalLayout_user_help.addWidget(self.textEdit_user_help)
        self.textEdit_user_help.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Select a topic from the tree list present on the left side panel</span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\"> </span></p>\n"
            "</body></html>")
        self.gridLayout_user_help.addLayout(self.horizontalLayout_user_help, 0, 0, 1, 1)
        self.treeWidget_user_help.topLevelItem(0).setText(0, "Instructions")
        self.treeWidget_user_help.topLevelItem(1).setText(0, "Change weather data")
        self.treeWidget_user_help.topLevelItem(2).setText(0, "Weather Data Summary")
        self.treeWidget_user_help.topLevelItem(2).child(0).setText(0, "Global Horizontal Radiation")
        self.treeWidget_user_help.topLevelItem(2).child(1).setText(0, "Direct  Normal  Radiation")
        self.treeWidget_user_help.topLevelItem(2).child(2).setText(0, "Diffuse Radiation")
        self.treeWidget_user_help.topLevelItem(2).child(3).setText(0, "Global Horizontal Illumination")
        self.treeWidget_user_help.topLevelItem(2).child(4).setText(0, "Direct  Normal  Illumination")
        self.treeWidget_user_help.topLevelItem(2).child(5).setText(0, "Dry Bulb Temperature")
        self.treeWidget_user_help.topLevelItem(2).child(6).setText(0, "Dew Point Temperature")
        self.treeWidget_user_help.topLevelItem(2).child(7).setText(0, "Relative Humidity")
        self.treeWidget_user_help.topLevelItem(2).child(8).setText(0, "Wet Bulb Temperature")
        self.treeWidget_user_help.topLevelItem(3).setText(0, "Temperature Range")
        self.treeWidget_user_help.topLevelItem(3).child(0).setText(0, "Recorded High or Low Temperature")
        self.treeWidget_user_help.topLevelItem(3).child(1).setText(0, "Mean or Average Temperature")
        self.treeWidget_user_help.topLevelItem(4).setText(0, "Radiation   Range")
        self.treeWidget_user_help.topLevelItem(4).child(0).setText(0, "Direct Normal Radiation Range")
        self.treeWidget_user_help.topLevelItem(4).child(1).setText(0, "Global Horizontal Radiation Range")
        self.treeWidget_user_help.topLevelItem(4).child(2).setText(0, "Diffused Horizontal Radiation Range")
        self.treeWidget_user_help.topLevelItem(5).setText(0, "Illumination Range")
        self.treeWidget_user_help.topLevelItem(5).child(0).setText(0, "Direct  Normal Illumination Range")
        self.treeWidget_user_help.topLevelItem(5).child(1).setText(0, "Global Horizontal Illumination Range")
        self.treeWidget_user_help.topLevelItem(6).setText(0, "Wind Velocity")
        self.treeWidget_user_help.topLevelItem(7).setText(0, "Ground Temperature")
        self.treeWidget_user_help.topLevelItem(8).setText(0, "Hourly Color Map")
        self.treeWidget_user_help.topLevelItem(9).setText(0, "Bioclimatic Design Chart")
        self.treeWidget_user_help.topLevelItem(9).child(0).setText(0, "Comfort Zone")
        self.treeWidget_user_help.topLevelItem(9).child(1).setText(0, "Evaporative Cooling")
        self.treeWidget_user_help.topLevelItem(9).child(2).setText(0, "Thermal Mass")
        self.treeWidget_user_help.topLevelItem(9).child(3).setText(0, "Sun Shading")
        self.treeWidget_user_help.topLevelItem(10).setText(0, "Design Guidelines")
        self.treeWidget_user_help.topLevelItem(11).setText(0, "Bibliography")
        self.treeWidget_user_help.setSortingEnabled(__sortingEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog_user_help)
        self.treeWidget_user_help.clicked.connect(
            lambda: self.tree_button_clicked(self.treeWidget_user_help.currentIndex()))
        Dialog_user_help.exec()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = None
        if base_path != None:
            relative_path = os.path.join(base_path, relative_path)
        return relative_path

    def tree_button_clicked(self, a):
        if a.data() == "Instructions":
            self.textEdit_user_help.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Instructions</span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">To make the building climate responsive first we have to properly understand the local climate. The passive design consultant reads the local climate data from EPW (EnergyPlus Weather) format files and represent it using different graphical and tabular format of various weather parameters. </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The main aim of the tool is to make it easier for the user to understand the local climatic conditions and get more and accurate information from it to get a better built form.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">For demo of the tool just go through all the tabs on the top of the tool. On any tab if you want to understand a term click on help on the menu bar. For many charts there are buttons on the left-hand side of the window panel which can also be checked.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">In user help there are subtopics in some topics, just double click on it to get the subtopics.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Change weather data":
            self.textEdit_user_help.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Change weather data </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">If you want to change the weather data just click on the back button given on the summary tab or go to the file menu and click on the change weather data option, it will take you back to the main page to select new weather data file.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">You have two options to select an EPW format weather data “Select Indian Composite Climate Weather file” button. A dialog box will open which contains some Indian composite climate weather files by city names. Second “Browse existing EPW weather file” button which is one you already have downloaded.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">If you wish to download a new EPW format weather data file then you can browse the ISHRAE website or go to the link </span><a href=\"https://energyplus.net/weatherregion/asia_wmo_region_2/IND%20%20\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">ISHRAE EPW file</span></a><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">. </span></p></body></html>")

        if a.data() == "Weather Data Summary":
            self.textEdit_user_help.setHtml(
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Weather Data Summary </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This summary table is made from the weather data. It shows the monthly average values of various weather parameters calculated from 8760 hours of data.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">If the data displayed on the summary table is defective or error detected or showing zero values that means the there was some problem while reading the EPW data file. If no data has been recorded for a particular variable at a site, zero will be shown in the chart.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Global Horizontal Radiation":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Global Horizontal Radiation</span></p>\n"
                                             "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Global Horizontal Radiation is defined as the amount of direct and diffuse solar radiation received on a horizontal surface. The units are in Wh/sq.m or Btu/sq.ft. </span></p></body></html>")

        if a.data() == "Direct  Normal  Radiation":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Direct Normal Radiation </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Direct Normal Radiation is defined as the amount of solar radiation received normal to the horizontal surface. The units are in Wh/sq.m or Btu/sq.ft. </span></p></body></html>")

        if a.data() == "Diffuse Radiation":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Diffuse Radiation </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Diffuse Radiation is defined as the incoming solar radiation onto a horizontal surface from the entire sky except for the Direct Normal Radiation that is incoming from the sun. The units are in Btu/sq.ft or Wh/sq.m. </span></p></body></html>")

        if a.data() == "Global Horizontal Illumination":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Global Horizontal Illumination </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Global Horizontal Illumination is defined as the total visible light that falls on a horizontal surface from the entire sky plus Direct Normal Illumination from the sun. The units are in lumens per square foot or lux.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Direct  Normal  Illumination":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Direct Normal Illumination </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Direct Normal Illumination is defined as the visible light from the sun that is measured by a narrow angle meter pointed directly at the sun and that excludes the surrounding sky.  The units are in lumens per square foot or lux. </span></p></body></html>")

        if a.data() == "Dry Bulb Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Dry Bulb Temperature </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Dry Bulb Temperature is the sensible temperature typically measured by a thermometer with a dry bulb. The units are either in degrees C or F. </span></p></body></html>")

        if a.data() == "Dew Point Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Dew Point Temperature </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#000000;\">The temperature at which water vapor has reached the saturation point (100% relative humidity). The temperature of the air at which it must be cooled at constant barometric pressure for water vapor to condense.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Relative Humidity":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Relative Humidity</span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Relative Humidity is the ratio of the amount of moisture in the air compared to the total amount it could hold at the same dry bulb temperature. Relative Humidity is measured as a percent.</span></p></body></html>")

        if a.data() == "Wet Bulb Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Wet Bulb Temperature</span><span style=\" font-size:8pt; text-decoration: underline;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#000000;\">the temperature indicated when a thermometer bulb is covered with water wick over which air is caused to flow at approximately 4.5 m/s (900 ft/min) to reach the equilibrium temperature of water evaporating into the air when the heat of vaporization is supplied by the sensible heat of the air.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Temperature Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Temperature Range </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This tab shows all the temperatures (dry bulb, dew point and wet bulb) range throughout the year. The chart represents the maximum, minimum and mean values on monthly basis using the violin graphs. You can switch between the temperatures using the buttons provided on the left side panel of that tab.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Recorded High or Low Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Recorded High or Low Temperature </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">These are the highest and lowest dry bulb temperatures that were recorded in each month or over the full year in this particular data file.  Note that this is probably not the all-time Record High or Low for this particular site because EPW files are composed of actual months from different years chosen in the interest of producing a typical or representative year. </span></p></body></html>")

        if a.data() == "Mean or Average Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Mean or Average Temperature </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This is the average of all dry bulb temperatures in that particular month or annually. </span></p></body></html>")

        if a.data() == "Radiation   Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Radiation Range </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The Hourly Averages Chart shows for each month and the full year, the Direct Normal Solar Radiation, Global (Total) Horizontal Solar Radiation and Diffused Surface Radiation for all daylight hours. The mean or average of all daylight hours is shown by a small horizontal line. The units are in Btu/sq.ft. or Wh/sq.m.</span></p></body></html>")

        if a.data() == "Direct Normal Radiation Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Direct Normal </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The graph shows the amount of solar radiation measured as if the sensor was pointed directly toward (or normal to) the sun.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Global Horizontal Radiation Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Global Horizontal </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The graph shows the amount of solar radiation that is recorded falling on a horizontal surface. In theory, it is composed of all the diffuse radiation from</span><span style=\" font-size:8pt;\"> </span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">the total sky vault plus the direct radiation from the sun times the cosine of the angle of incidence.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Diffused Horizontal Radiation Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Diffused Radiation </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Diffuse Radiation is defined as the incoming solar radiation onto a horizontal surface from the entire sky except for the Direct Normal Radiation that is incoming from the sun. The units are in Btu/sq.ft or Wh/sq.m. </span></p></body></html>")

        if a.data() == "Illumination Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Illumination Range </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The Visible Direct Normal Illumination shows for each month. The Recorded High and Low Daily value (green dot) and the Daily Mean Illumination. The units are in lumens per square foot or lux.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Direct  Normal Illumination Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Direct Normal Illumination </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Direct Normal Illumination is defined as the visible light from the sun that is measured by a narrow angle meter pointed directly at the sun and that excludes the surrounding sky.  The units are in lumens per square foot or lux. </span></p></body></html>")

        if a.data() == "Global Horizontal Illumination Range":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Global Horizontal Illumination </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Global Horizontal Illumination is defined as the total visible light that falls on a horizontal surface from the entire sky plus Direct Normal Illumination from the sun.   The units are in lumens per square foot or lux.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Wind Velocity":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Wind Velocity </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This chart shows each month. Wind Velocity meters per second (m/s). The Recorded High value in the EPW file is shown as a small horizontal line. The Mean or average of all hours during the month is shown as the break in the plot with a small horizontal line. The Recorded Low value is shown as the small horizontal line.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Ground Temperature":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Ground Temperature (Monthly Average) </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The Average Monthly Temperature of the soil at various depths is shown on the Ground Temperature chart. Depth is given in meters and the temperatures are in degrees C.  Notice that as the depth increases the thermal mass of the soil causes a greater time lag and more damping.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Hourly Color Map":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Hourly Plot </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This plot shows along the bottom the months of the year and along the side the hours of the day. Dry bulb temperature is shown in this colour plot.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The units for each variable are indicated in the upper left, divided into four different ranges in colours from blue to red, and the temperature that falls in each range are also shown. </span></p></body></html>")

        if a.data() == "Bioclimatic Design Chart":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Psychrometric Chart </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This is the most important and main function of the passive design consultant. It shows dry bulb temperature across the bottom and moisture content of the air up the side. This vertical scale is also called absolute humidity and can be shown as the humidity ratio in grams of water per kilogram of dry air, or as the vapor pressure. The curved line on the far left is the saturation line (100% Relative Humidity line) which represents the fact that at lower temperatures air can hold less moisture than at higher temperatures. Every hour in the EPW climate data file is shown as a dot on this chart.  Notice that some dots may represent more than one hour, for example when a given temperature and humidity occurs more than once in any month.   Notice also that a given hour\'s dot might meet the criteria for more than one strategy zone, in which case it is counted in the Percentage of Hours for both zones, which is why the percentages add up to more than 100%.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The colour of each dot can represent whether or not the hour is Comfortable (light green) or Uncomfortable (red), according to the inputs defining Comfort on the Criteria screen. </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Variation of air speed is also provided in the left side panel by which the effect of indoor air velocity can be easily studied.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Comfort Zone":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Comfort zone</span><span style=\" font-size:8pt; text-decoration: underline;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Comfort zone defines on the screen and can be easily seen on the psychrometric chart. It is made on the conditions of DBT, humidity ratio and RH for which occupant will feel comfortable. The zone is defined by the lines in the psychrometric chart with the dark blue colour. It is assumed to enclose the number of hours when the occupants of a space are thermally comfortable whether in indoor or outdoor conditions. Zone varies with change in indoor air speed.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Evaporative Cooling":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Evaporative Cooling Polygon</span><span style=\" font-size:8pt; text-decoration: underline;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This zone is defined on the Criteria screen and is displayed on the Psychrometric Chart down and to the right of the Comfort Zone using the dark green colour. Evaporative cooling takes place when water is changed from liquid water to gas (taking on the latent heat of fusion), thus the air becomes cooler but more humid. Evaporation follows the Wet Bulb Temperature line on the Psychrometric Chart. This makes an evaporative cooler a good cooling strategy for hot dry climates. This polygon is defined automatically by the highest and lowest Wet Bulb</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt;\"> </span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Temperatures that fall within the comfort zone. Passive Design Consultant automatically calculates these two values and shows them.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Thermal Mass":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">High Thermal Mass Polygon</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This extended polygon is shown by yellow colour on the psychrometric chart. When an hour point lies in this polygon it means that the temperature of that point can be reduced to the comfortable condition if thermal mass is used in the building.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">In summer, in hot dry climates using high thermal mass on the interior is a good cooling design strategy.  This counts on the thermal storage and time lag and damping effects of the mass. Thus, high daily outdoor temperature swings will become low daily indoor temperature swings, thus the building will be closed up and \'coast\' through high daytime temperatures.  This is why high mass construction is a good natural cooling strategy in hot arid climates, on days when outdoor temperatures were below the Comfort High during the preceding evening.  In winter there is also some positive warming effect of high mass buildings provided that daytime outdoor temperatures get into the comfort zone.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Sun Shading":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Sun Shading Polygon </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This zone is defined on the Criteria screen and is displayed on the Psychrometric Chart, at the right of the comfort zone using the orange colour. By using sun shading devices on the windows, you can reduce the solar heat gain through the windows which is the main cause of the temperature rise inside the room. Sun Shading is particularly effective in outdoor spaces to control radiant temperatures, and on windows to help prevent indoor dry bulb temperatures from climbing above ambient temperature. Note that the extended polygon for sun shading is made while using the maximum shading of the windows but with fulfilling the criteria of the minimum VLT (Visible Light Transmission) and minimum Lux level inside the room.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        if a.data() == "Design Guidelines":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Design Guidelines </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The Design Guidelines screen shows a list of suggestions, specific to this particular climate and selected set of Design Strategies, to guide the design of buildings such as homes, shops, classrooms, and small offices. </span></p></body></html>")

        if a.data() == "Bibliography":
            self.textEdit_user_help.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Bibliography </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">ASHRAE. “Handbook HVAC Fundamentals.” </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Ashrae</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, vol. 30329, no. 404, 2009.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Bhatnagar, Mayank, et al. “Development of Reference Building Models for India.” </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Journal of Building Engineering</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, vol. 21, no. October 2018, Elsevier Ltd, 2019, pp. 267–77, doi:10.1016/j.jobe.2018.10.027.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Eddy, Josh, et al. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Thermal Environmental Conditions for Human Occupancy</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">. 2017.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Givoni, Baruch. “Comfort, Climate Analysis and Building Design Guidelines.” </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Energy and Buildings</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, vol. 18, no. 1, 1992, pp. 11–23, doi:10.1016/0378-7788(92)90047-K.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Kumar, Sanjay, Jyotirmay Mathur, et al. “An Adaptive Approach to Define Thermal Comfort Zones on Psychrometric Chart for Naturally Ventilated Buildings in Composite Climate of India.” </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Building and Environment</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, vol. 109, Elsevier Ltd, 2016, pp. 135–53, doi:10.1016/j.buildenv.2016.09.023.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">6.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Kumar, Sanjay, Priyam Tewari, et al. “Development of Mathematical Correlations for Indoor Temperature from Field Observations of the Performance of High Thermal Mass Buildings in India.” </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Building and Environment</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, vol. 122, Elsevier Ltd, 2017, pp. 324–42, doi:10.1016/j.buildenv.2017.06.030.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">7.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Energy conservation building code (ECBC) 2017</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">8.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">P. Tewari, S. Mathur, J. Mathur, V. Loftness, and A. Abdul-Aziz, “Advancing building bioclimatic design charts for the use of evaporative cooling in the composite climate of India,” Energy Build., vol. 184, pp. 177–192, 2019.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">9.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">        </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">N. K. Khambadkone and R. Jain, “A bioclimatic analysis tool for investigation of the potential of passive cooling and heating strategies in a composite Indian climate,” Build. Environ., vol. 123, pp. 469–493, 2017.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">10.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">E. A. Arens et al., “Thermal Environmental Conditions for Human Occupancy,” vol. 2013, 2013.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">11.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Kirankumar, G., Saboor, S., &amp; Ashok Babu, T. P. (2017). Thermal Analysis of Wall and Window Glass Materials for Cooling Load Reduction in Green Energy Building Design. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Materials Today: Proceedings</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">4</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">(9), 9514–9518</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">12.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Kirankumar, G., Saboor, S., &amp; Ashok Babu, T. P. (2017). Investigation of Various Low Emissivity Glass Materials for Green Energy Building Construction in Indian Climatic Zones. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">MaterialsToday: Proceedings</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">4</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">(8), 80528058. </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">13.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">PsychroLib (version 2.2.0) (https://github.com/psychrometrics/psychrolib)</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">14.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Yi, Y. K., Yin, J., &amp; Tang, Y. (2018). Developing an advanced daylight model for building energy tool to simulate dynamic shading device. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Solar Energy</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">163</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">(January), 140–149. </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">15.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Mainini, A. G., Poli, T., Zinzi, M., &amp; Speroni, A. (2015). Metal mesh as shading devices and thermal response of an office building: Parametric analysis. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Energy Procedia</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">78</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, 103–109. </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">16.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Ghosh, A., &amp; Neogi, S. (2018). Effect of fenestration geometrical factors on building energy consumption and performance evaluation of a new external solar shading device in warm and humid climatic condition. </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-style:italic;\">Solar Energy</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">, Vol. 169, pp. 94–104. </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">17.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">F Nicol and M A Humphreys, &quot;Thermal comfort as part of a self-regulating system. Building Research and Practice 1(3); pp. 174-179.,&quot; vol. 1, no. 3, pp. 174-179, 1973.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                                       "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:200%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">18.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">ASHRAE, ASHRAE Standard 55. Thermal environmental conditions for human occupancy. Atlanta, USA, 2013.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

    def about_window(self):
        Dialog_about = QtWidgets.QDialog()
        Dialog_about.setObjectName("Dialog_about")
        Dialog_about.resize(735, 409)
        icon = QtGui.QIcon(self.ico_path)
        Dialog_about.setWindowIcon(icon)
        self.gridLayout_about = QtWidgets.QGridLayout(Dialog_about)
        self.gridLayout_about.setObjectName("gridLayout_about")
        self.verticalLayout_about = QtWidgets.QVBoxLayout()
        self.verticalLayout_about.setObjectName("verticalLayout_about")
        self.line_2_about = QtWidgets.QFrame(Dialog_about)
        self.line_2_about.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2_about.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_about.setObjectName("line_2_about")
        self.verticalLayout_about.addWidget(self.line_2_about)
        self.textEdit_about = QtWidgets.QTextEdit(Dialog_about)
        self.textEdit_about.setAutoFillBackground(True)
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setObjectName("textEdit_about")
        self.verticalLayout_about.addWidget(self.textEdit_about)
        self.line_about = QtWidgets.QFrame(Dialog_about)
        self.line_about.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_about.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_about.setObjectName("line_about")
        self.verticalLayout_about.addWidget(self.line_about)
        self.gridLayout_about.addLayout(self.verticalLayout_about, 0, 0, 1, 1)
        Dialog_about.setWindowTitle("Passive design conslutant")
        self.textEdit_about.setDocumentTitle("About")
        self.textEdit_about.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>About</title><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">ABOUT</span><span style=\" font-size:8pt; text-decoration: underline;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Passive design consultant tool is developed by Raj Gupta under the supervision of professor Jyotirmay Mathur, Centre for Energy and Environment (MNIT, Jaipur) with the technical support by Malviya National Institute of technology, Jaipur and financial support by ISHRAE. The basic idea of the tool was taken from the climate consultant software.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Acknowledgment </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">I would like to express my sincere gratitude to Prof. Jyotirmay Mathur, Department of Centre for Energy and Environment, who provide me with generous guidance, valuable help, and endless encouragement by taking personal interest and attention. He has been the principal motivation behind this work and provided all kinds of possible support.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">I am very fortunate that the project was selected for ISHRAE grant and to have an opportunity to work on this topic with the help of ISHRAE by providing the funding. I also appreciate and heartily thank to all the co-workers at ISHRAE for giving us time and support. </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">It is also a pleasure to mention my sincere and profound gratitude to Mrs. Priyam Tewari (Associate Fellow), The Energy and Resources Institute and Mr. Ranaveer Pratap Singh (Research Scholar), Malaviya National Institute of Technology, Jaipur, for their love, care, support and creating a pleasant atmosphere for me here, who also abundantly helpful and offered invaluable assistance, support and guidance with their experience and knowledge, throughout my project work.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Passive design consultant is based on the theoretical work by Baruch Givoni and Murray Milne with addition of practical work done by Indian researchers on Psychrometric chart for composite climate of India.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">FEEDBACK AND QUESTIONS</span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Please give your valuable feedback and let us know what you think about this tool.</span><span style=\" font-size:12pt;\"> </span></p>\n"
                                               "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">And if you have any quarries reach us at </span><a href=\"mailto:%20guptaa.raj07@gmail.com\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; text-decoration: underline; color:#0000ff;\">guptaa.raj07@gmail.com</span></a><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">.</span><span style=\" font-size:12pt;\"> </span></p></body></html>")

        QtCore.QMetaObject.connectSlotsByName(Dialog_about)
        Dialog_about.exec()

    def terms_of_use_window(self):
        Dialog_terms = QtWidgets.QDialog()
        Dialog_terms.setObjectName("Dialog_terms")
        Dialog_terms.resize(738, 412)
        icon = QtGui.QIcon(self.ico_path)
        Dialog_terms.setWindowIcon(icon)
        self.gridLayout_terms = QtWidgets.QGridLayout(Dialog_terms)
        self.gridLayout_terms.setObjectName("gridLayout_terms")
        self.verticalLayout_terms = QtWidgets.QVBoxLayout()
        self.verticalLayout_terms.setObjectName("verticalLayout_terms")
        self.line_2_terms = QtWidgets.QFrame(Dialog_terms)
        self.line_2_terms.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2_terms.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_terms.setObjectName("line_2_terms")
        self.verticalLayout_terms.addWidget(self.line_2_terms)
        self.textEdit_terms = QtWidgets.QTextEdit(Dialog_terms)
        self.textEdit_terms.setAutoFillBackground(True)
        self.textEdit_terms.setReadOnly(True)
        self.textEdit_terms.setObjectName("textEdit_terms")
        self.verticalLayout_terms.addWidget(self.textEdit_terms)
        self.line_terms = QtWidgets.QFrame(Dialog_terms)
        self.line_terms.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_terms.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_terms.setObjectName("line_terms")
        self.verticalLayout_terms.addWidget(self.line_terms)
        self.gridLayout_terms.addLayout(self.verticalLayout_terms, 0, 0, 1, 1)
        Dialog_terms.setWindowTitle("Passive design consultant")
        self.textEdit_terms.setDocumentTitle("Terms of use")
        self.textEdit_terms.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline;\">Terms of Use</span><span style=\" font-size:8pt; text-decoration: underline;\"> </span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This tool is free of cost and we welcome you to use it. You can share it with others provided not distributed for commercial advantage. And that these terms of use are unaltered since release date.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">Users shall have no rights to modify, change, alter, edit or create derivative works.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">You may publish the output of passive design consultant provided that acknowledgementis made that it was developed by raj gupta for his master’s degree in renewable energy from MNIT, Jaipur and with collaboration and funding by ISHRAE. </span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Disclaimer</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">The information provided by the tool is believed to be accurate and reliable. However, we are not liable for any damage due to accuracy of this tool or climate data it uses or for any error in this software or its documentation. The operation of this design guide tool is the responsibility of the user.</span><span style=\" font-size:8pt;\"> </span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\">This software is made as a result of final year project of master’s degree from Malviya National Institute of Technology, Jaipur with collaboration and funding by ISHRAE. ISHRAE, its employees, MNIT, its staff, employees or student are not liable, make no warranty for the information in this report. </span></p></body></html>")

        QtCore.QMetaObject.connectSlotsByName(Dialog_terms)
        Dialog_terms.exec()

    def instruction_window(self):
        Dialog_instruction = QtWidgets.QDialog()
        Dialog_instruction.setObjectName("Dialog_instruction")
        Dialog_instruction.resize(736, 508)
        Dialog_instruction.setAutoFillBackground(True)
        self.gridLayout_inst = QtWidgets.QGridLayout(Dialog_instruction)
        self.gridLayout_inst.setObjectName("gridLayout_inst")
        self.textEdit_inst = QtWidgets.QTextEdit(Dialog_instruction)
        self.textEdit_inst.setReadOnly(True)
        self.textEdit_inst.setObjectName("textEdit_inst")
        self.gridLayout_inst.addWidget(self.textEdit_inst, 0, 0, 1, 1)
        Dialog_instruction.setWindowTitle("Passive design consultant")
        icon = QtGui.QIcon(self.ico_path)
        Dialog_instruction.setWindowIcon(icon)
        Dialog_instruction.setStatusTip("INSTRUCTIONS")
        self.textEdit_inst.setDocumentTitle("Instructions")
        self.textEdit_inst.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Instructions</title><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline; color:#434343;\">INSTRUCTIONS TO USE THE TOOL</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; color:#434343;\">WEATHER DATA</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">Some .EPW format files for composite climate of India are pre available in the tool by clicking on the button Select Indian Composite Climate Zone Weather File. Select desired city and click ok to load it for the study. For downloading an .EPW file you can access through </span><a href=\"https://energyplus.net/weatherregion/asia_wmo_region_2/IND%20%20\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://energyplus.net/weatherregion/asia_wmo_region_2/IND%20%20</span></a><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">. Once a file is installed successfully you can choose that file by the browse existing EPW Weather file button.</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; color:#434343;\">TABS</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">For keeping the use of tool easier tabs are used to navigate all screens as present on top of the window A back button is also available on the summary page so as to go back and select other .EPW file. At any point you can select any screen you wish by clicking on that tab.</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; color:#434343;\">DEMO</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">For a demonstration of all the things that the tool can do, just go through all the tabs.</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; color:#434343;\">HELP</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">For definitions of terms and use of all screens click on help on the main menu.</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; color:#434343;\">FEEDBACK AND QUESTIONS</span></p>\n"
                                         "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; color:#434343;\">Please give your valuable feedback and let us know what you think about this tool.And if you have any quarries reach us at </span><a href=\"guptaa.raj07@gmail.com\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">guptaa.raj07@gmail.com</span></a><span style=\" font-family:\'Cambria,serif\'; font-size:14pt; color:#434343;\">.</span></p></body></html>")
        QtCore.QMetaObject.connectSlotsByName(Dialog_instruction)
        Dialog_instruction.exec()

    def exit_window(self):
        QtWidgets.QMainWindow.close()

    def browse_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()
        fpath = fname[0]
        if fpath != "":
            self.Next_wid(fpath)

    def select_file(self):
        select_city = QtWidgets.QDialog()
        select_city.setObjectName("select_city")
        select_city.resize(299, 394)
        icon = QtGui.QIcon(self.ico_path)
        select_city.setWindowIcon(icon)
        select_city.setWindowTitle("City List")
        self.gridLayout = QtWidgets.QGridLayout(select_city)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(select_city)
        self.label.setText("Select composite climate city")
        font = QtGui.QFont()
        font.setPointSize(10)   
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list = QtWidgets.QListWidget(select_city)
        self.list.setStyleSheet("")
        self.list.setObjectName("list")
        self.list.insertItem(0, "Allahabad")
        self.list.insertItem(1, "Amritsar")
        self.list.insertItem(2, "Bhopal")
        self.list.insertItem(3, "Dehradun")
        self.list.insertItem(4, "Gorakhpur")
        self.list.insertItem(5, "Gwalior")
        self.list.insertItem(6, "Hissar")
        self.list.insertItem(7, "Hyderabad")
        self.list.insertItem(8, "Indore")
        self.list.insertItem(9, "Jabalpur")
        self.list.insertItem(10, "Jaipur")
        self.list.insertItem(11, "Lucknow")
        self.list.insertItem(12, "Nagpur")
        self.list.insertItem(13, "New_Delhi")
        self.list.insertItem(14, "Patna")
        self.list.insertItem(15, "Raipur")
        self.list.insertItem(16, "Rajkot")
        self.list.insertItem(17, "Ranchi")
        self.verticalLayout.addWidget(self.list)
        self.buttonBox = QtWidgets.QDialogButtonBox(select_city)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.buttonBox.accepted.connect(select_city.accept)
        self.buttonBox.rejected.connect(select_city.reject)
        self.buttonBox.accepted.connect(self.city_value)
        QtCore.QMetaObject.connectSlotsByName(select_city)
        select_city.exec()

    def city_value(self):
        item = self.list.currentItem()
        print(item.text())
        fname = item.text() + ".epw"
        fpath = "Composite Climate EPW Files/"+ fname
        epw_file_path = self.resource_path(fpath)
        if epw_file_path != "":
        	self.Next_wid(epw_file_path)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = None
        if base_path != None:
            relative_path = os.path.join(base_path, relative_path)
        return relative_path

    def back_page(self):
        self.file_input_widget()

    def rel_data(self, data, altitude):
        psychrolib.SetUnitSystem(psychrolib.SI)
        dbt = []
        dpt = []
        wbt = []
        rh = []
        dnr = []
        ghr = []
        dhr = []
        ghi = []
        dni = []
        wv = []
        m = []
        d = []
        h = []
        p = []
        press = psychrolib.GetStandardAtmPressure(float(altitude))
        for row in data:
            dbt.append(round(float(row[6]), 1))
            dpt.append(round(float(row[7]), 1))
            rh.append(round(float(row[8]), 1))
            ghr.append(round(float(row[13]), 1))
            dnr.append(round(float(row[14]), 1))
            dhr.append(round(float(row[15]), 1))
            ghi.append(round(float(row[16]), 1))
            dni.append(round(float(row[17]), 1))
            wv.append(round(float(row[21]), 1))
            wbt.append(round(float(psychrolib.GetTWetBulbFromRelHum(float(row[6]), float(row[8])/100, press)), 1))
            m.append(row[1])
            d.append(row[2])
            h.append(row[3])
            p.append(press)
        #print('calc complete')
        return {'dbt': dbt, 'dpt': dpt, 'wbt': wbt, 'rh': rh, 'dnr': dnr, 'ghr': ghr, 'dhr': dhr, 'ghi': ghi, 'dni': dni, 'wv': wv, 'm': m, 'd': d, 'h': h, 'p': p}

    def collect_epw(self,fpath):
        import psychrolib
        import csv
        psychrolib.SetUnitSystem(psychrolib.SI)
        data = []
        with open(fpath) as epw_file:
            #print(epw_file)
            csv_reader = csv.reader(epw_file)
            count = 0
            for row in csv_reader:
                #print(row)
                data.append(row)
        self.elevation = float(data[0][9])
        lat = float(data[0][6])
        lon = float(data[0][7])
        city = data[0][1]
        state = data[0][2]
        country = data[0][3]
        tz = data[0][8]
        self.relv_data = self.rel_data(data[8:], self.elevation)
        source = "ISHRAE"

        self.dbt = self.relv_data['dbt']
        self.dpt = self.relv_data['dpt']
        self.rh = self.relv_data['rh']
        self.wbt = self.relv_data['wbt']
        self.ghr = self.relv_data['ghr']
        self.dnr = self.relv_data['dnr']
        self.dhr = self.relv_data['dhr']
        self.ghi = self.relv_data['ghi']
        self.dni = self.relv_data['dni']
        self.wvr = self.relv_data['wv']
        self.m = self.relv_data['m']
        self.d = self.relv_data['d']
        self.h = self.relv_data['h']
        p = self.relv_data['p']

        self.grd_0 = [round(float(data[3][i]), 1) for i in range(6, 18)]
        self.grd_1 = [round(float(data[3][i]), 1) for i in range(22, 34)]
        self.grd_2 = [round(float(data[3][i]), 1) for i in range(38, 50)]


        ###########
        self.lat_lon.setText(str(lat) + " / " + str(lon))
        self.lat_lon_2.setText(str(lat) + " / " + str(lon))
        self.lat_lon_3.setText(str(lat) + " / " + str(lon))
        self.lat_lon_4.setText(str(lat) + " / " + str(lon))
        self.lat_lon_5.setText(str(lat) + " / " + str(lon))
        self.lat_lon_6.setText(str(lat) + " / " + str(lon))
        self.lat_lon_7.setText(str(lat) + " / " + str(lon))
        self.lat_lon_9.setText(str(lat) + " / " + str(lon))

        ##
        self.location.setText(city + ", " + state + ", " + country)
        self.location_2.setText(city + ", " + state + ", " + country)
        self.location_3.setText(city + ", " + state + ", " + country)
        self.location_4.setText(city + ", " + state + ", " + country)
        self.location_5.setText(city + ", " + state + ", " + country)
        self.location_6.setText(city + ", " + state + ", " + country)
        self.location_7.setText(city + ", " + state + ", " + country)
        self.location_9.setText(city + ", " + state + ", " + country)

        ##
        self.ele_tz.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_2.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_3.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_4.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_5.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_6.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_7.setText(str(self.elevation) + " / " + str(tz))
        self.ele_tz_9.setText(str(self.elevation) + " / " + str(tz))

        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "december"]


        #######
        self.summary_values(self.dbt,self.rh,self.dpt,self.wbt,self.ghr,self.dnr,self.dhr,self.ghi,self.dni,self.m,self.d,self.h)
        self.temp_graph()
        self.radia_graph()
        self.illumi_graph()
        self.windv_graph()
        self.grd_graph()
        self.hour_graph()
        self.psychrometric_graph()

    def summary_values(self,dbt,rh,dpt,wbt,ghr,dnr,dhr,ghi,dni,m,d,h):
        #### DBT(avg) ####
        self.jan_7.setText(str(round(sum(dbt[:744]) / 744,2)))
        self.feb_7.setText(str(round(sum(dbt[744:1416]) / 672,2)))
        self.mar_7.setText(str(round(sum(dbt[1416:2160]) / 744,2)))
        self.apr_7.setText(str(round(sum(dbt[2160:2880]) / 720,2)))
        self.may_7.setText(str(round(sum(dbt[2880:3624]) / 744,2)))
        self.jun_7.setText(str(round(sum(dbt[3624:4344]) / 720,2)))
        self.jul_7.setText(str(round(sum(dbt[4344:5088]) / 744,2)))
        self.aug_7.setText(str(round(sum(dbt[5088:5832]) / 744,2)))
        self.sep_7.setText(str(round(sum(dbt[5832:6552]) / 720,2)))
        self.oct_7.setText(str(round(sum(dbt[6552:7296]) / 744,2)))
        self.nov_7.setText(str(round(sum(dbt[7296:8016]) / 720,2)))
        self.dec_7.setText(str(round(sum(dbt[8016:8760]) / 744,2)))
        #### DBT(max) ####
        self.jan_8.setText(str(round(max(dbt[:744]),2)))
        self.feb_8.setText(str(round(max(dbt[744:1416]),2)))
        self.mar_8.setText(str(round(max(dbt[1416:2160]),2)))
        self.apr_8.setText(str(round(max(dbt[2160:2880]),2)))
        self.may_8.setText(str(round(max(dbt[2880:3624]),2)))
        self.jun_8.setText(str(round(max(dbt[3624:4344]),2)))
        self.jul_8.setText(str(round(max(dbt[4344:5088]),2)))
        self.aug_8.setText(str(round(max(dbt[5088:5832]),2)))
        self.sep_8.setText(str(round(max(dbt[5832:6552]),2)))
        self.oct_8.setText(str(round(max(dbt[6552:7296]),2)))
        self.nov_8.setText(str(round(max(dbt[7296:8018]),2)))
        self.dec_8.setText(str(round(max(dbt[8016:8760]),2)))
        #### DPT ####
        self.jan_11.setText(str(round(sum(dpt[:744]) / 744)))
        self.feb_11.setText(str(round(sum(dpt[744:1416]) / 672)))
        self.mar_11.setText(str(round(sum(dpt[1416:2160]) / 744)))
        self.apr_11.setText(str(round(sum(dpt[2160:2880]) / 720)))
        self.may_11.setText(str(round(sum(dpt[2880:3624]) / 744)))
        self.jun_11.setText(str(round(sum(dpt[3624:4344]) / 720)))
        self.jul_11.setText(str(round(sum(dpt[4344:5088]) / 744)))
        self.aug_11.setText(str(round(sum(dpt[5088:5832]) / 744)))
        self.sep_11.setText(str(round(sum(dpt[5832:6552]) / 720)))
        self.oct_11.setText(str(round(sum(dpt[6552:7296]) / 744)))
        self.nov_11.setText(str(round(sum(dpt[7296:8016]) / 720)))
        self.dec_11.setText(str(round(sum(dpt[8016:8760]) / 744)))
        #### RH ####
        self.jan_9.setText(str(round(sum(rh[:744]) / 744)))
        self.feb_9.setText(str(round(sum(rh[744:1416]) / 672)))
        self.mar_9.setText(str(round(sum(rh[1416:2160]) / 744)))
        self.apr_9.setText(str(round(sum(rh[2160:2880]) / 720)))
        self.may_9.setText(str(round(sum(rh[2880:3624]) / 744)))
        self.jun_9.setText(str(round(sum(rh[3624:4344]) / 720)))
        self.jul_9.setText(str(round(sum(rh[4344:5088]) / 744)))
        self.aug_9.setText(str(round(sum(rh[5088:5832]) / 744)))
        self.sep_9.setText(str(round(sum(rh[5832:6552]) / 720)))
        self.oct_9.setText(str(round(sum(rh[6552:7296]) / 744)))
        self.nov_9.setText(str(round(sum(rh[7296:8016]) / 720)))
        self.dec_9.setText(str(round(sum(rh[8016:8760]) / 744)))
        #### WBT ####
        self.jan_10.setText(str(round(sum(wbt[:744]) / 744)))
        self.feb_10.setText(str(round(sum(wbt[744:1416]) / 672)))
        self.mar_10.setText(str(round(sum(wbt[1416:2160]) / 744)))
        self.apr_10.setText(str(round(sum(wbt[2160:2880]) / 720)))
        self.may_10.setText(str(round(sum(wbt[2880:3624]) / 744)))
        self.jun_10.setText(str(round(sum(wbt[3624:4344]) / 720)))
        self.jul_10.setText(str(round(sum(wbt[4344:5088]) / 744)))
        self.aug_10.setText(str(round(sum(wbt[5088:5832]) / 744)))
        self.sep_10.setText(str(round(sum(wbt[5832:6552]) / 720)))
        self.oct_10.setText(str(round(sum(wbt[6552:7296]) / 744)))
        self.nov_10.setText(str(round(sum(wbt[7296:8016]) / 720)))
        self.dec_10.setText(str(round(sum(wbt[8016:8760]) / 744)))
        #### DNI ####
        self.jan_12.setText(str(round(sum(dni[:744]) / 248)))
        self.feb_12.setText(str(round(sum(dni[744:1416]) / 672)))
        self.mar_12.setText(str(round(sum(dni[1416:2160]) / 248)))
        self.apr_12.setText(str(round(sum(dni[2160:2880]) / 720)))
        self.may_12.setText(str(round(sum(dni[2880:3624]) / 248)))
        self.jun_12.setText(str(round(sum(dni[3624:4344]) / 720)))
        self.jul_12.setText(str(round(sum(dni[4344:5088]) / 248)))
        self.aug_12.setText(str(round(sum(dni[5088:5832]) / 248)))
        self.sep_12.setText(str(round(sum(dni[5832:6552]) / 720)))
        self.oct_12.setText(str(round(sum(dni[6552:7296]) / 248)))
        self.nov_12.setText(str(round(sum(dni[7296:8016]) / 720)))
        self.dec_12.setText(str(round(sum(dni[8016:8760]) / 248)))
        #### GHI ####
        self.jan_13.setText(str(round(sum(ghi[:744]) / 248)))
        self.feb_13.setText(str(round(sum(ghi[744:1416]) / 672)))
        self.mar_13.setText(str(round(sum(ghi[1416:2160]) / 248)))
        self.apr_13.setText(str(round(sum(ghi[2160:2880]) / 720)))
        self.may_13.setText(str(round(sum(ghi[2880:3624]) / 248)))
        self.jun_13.setText(str(round(sum(ghi[3624:4344]) / 720)))
        self.jul_13.setText(str(round(sum(ghi[4344:5088]) / 248)))
        self.aug_13.setText(str(round(sum(ghi[5088:5832]) / 248)))
        self.sep_13.setText(str(round(sum(ghi[5832:6552]) / 720)))
        self.oct_13.setText(str(round(sum(ghi[6552:7296]) / 248)))
        self.nov_13.setText(str(round(sum(ghi[7296:8016]) / 720)))
        self.dec_13.setText(str(round(sum(ghi[8016:8760]) / 248)))
        #### GHR ####
        self.jan_1.setText(str(round(sum(ghr[:744]) / (744 - (ghr[:744].count(0))))))
        self.feb_1.setText(str(round(sum(ghr[744:1416]) / (672 - (ghr[744:1416].count(0))))))
        self.mar_1.setText(str(round(sum(ghr[1416:2160]) / (744 - (ghr[1416:2160].count(0))))))
        self.apr_1.setText(str(round(sum(ghr[2160:2880]) / (720 - (ghr[2160:2880].count(0))))))
        self.may_1.setText(str(round(sum(ghr[2880:3624]) / (744 - (ghr[2880:3624].count(0))))))
        self.jun_1.setText(str(round(sum(ghr[3624:4344]) / (720 - (ghr[3624:4344].count(0))))))
        self.jul_1.setText(str(round(sum(ghr[4344:5088]) / (744 - (ghr[4344:5088].count(0))))))
        self.aug_1.setText(str(round(sum(ghr[5088:5832]) / (744 - (ghr[5088:5832].count(0))))))
        self.sep_1.setText(str(round(sum(ghr[5832:6552]) / (720 - (ghr[5832:6552].count(0))))))
        self.oct_1.setText(str(round(sum(ghr[6552:7296]) / (744 - (ghr[6552:7296].count(0))))))
        self.nov_1.setText(str(round(sum(ghr[7296:8016]) / (720 - (ghr[7296:8016].count(0))))))
        self.dec_1.setText(str(round(sum(ghr[8016:8760]) / (744 - (ghr[8016:8760].count(0))))))
        #### DNR ####
        self.jan_2.setText(str(round(sum(dnr[:744]) / (744 - (dnr[:744].count(0))))))
        self.feb_2.setText(str(round(sum(dnr[744:1416]) / (672 - (dnr[744:1416].count(0))))))
        self.mar_2.setText(str(round(sum(dnr[1416:2160]) / (744 - (dnr[1416:2160].count(0))))))
        self.apr_2.setText(str(round(sum(dnr[2160:2880]) / (720 - (dnr[2160:2880].count(0))))))
        self.may_2.setText(str(round(sum(dnr[2880:3624]) / (744 - (dnr[2880:3624].count(0))))))
        self.jun_2.setText(str(round(sum(dnr[3624:4344]) / (720 - (dnr[3624:4344].count(0))))))
        self.jul_2.setText(str(round(sum(dnr[4344:5088]) / (744 - (dnr[4344:5088].count(0))))))
        self.aug_2.setText(str(round(sum(dnr[5088:5832]) / (744 - (dnr[5088:5832].count(0))))))
        self.sep_2.setText(str(round(sum(dnr[5832:6552]) / (720 - (dnr[5832:6552].count(0))))))
        self.oct_2.setText(str(round(sum(dnr[6552:7296]) / (744 - (dnr[6552:7296].count(0))))))
        self.nov_2.setText(str(round(sum(dnr[7296:8016]) / (720 - (dnr[7296:8016].count(0))))))
        self.dec_2.setText(str(round(sum(dnr[8016:8760]) / (744 - (dnr[8016:8760].count(0))))))
        #### DR ####
        self.jan_3.setText(str(round(sum(dhr[:744]) / (744 - (dhr[:744].count(0))))))
        self.feb_3.setText(str(round(sum(dhr[744:1416]) / (672 - (dhr[744:1416].count(0))))))
        self.mar_3.setText(str(round(sum(dhr[1416:2160]) / (744 - (dhr[1416:2160].count(0))))))
        self.apr_3.setText(str(round(sum(dhr[2160:2880]) / (720 - (dhr[2160:2880].count(0))))))
        self.may_3.setText(str(round(sum(dhr[2880:3624]) / (744 - (dhr[2880:3624].count(0))))))
        self.jun_3.setText(str(round(sum(dhr[3624:4344]) / (720 - (dhr[3624:4344].count(0))))))
        self.jul_3.setText(str(round(sum(dhr[4344:5088]) / (744 - (dhr[4344:5088].count(0))))))
        self.aug_3.setText(str(round(sum(dhr[5088:5832]) / (744 - (dhr[5088:5832].count(0))))))
        self.sep_3.setText(str(round(sum(dhr[5832:6552]) / (720 - (dhr[5832:6552].count(0))))))
        self.oct_3.setText(str(round(sum(dhr[6552:7296]) / (744 - (dhr[6552:7296].count(0))))))
        self.nov_3.setText(str(round(sum(dhr[7296:8016]) / (720 - (dhr[7296:8016].count(0))))))
        self.dec_3.setText(str(round(sum(dhr[8016:8760]) / (744 - (dhr[8016:8760].count(0))))))
        #### GHR(max) ####
        self.jan_4.setText(str(round(max(ghr[:744]))))
        self.feb_4.setText(str(round(max(ghr[744:1416]))))
        self.mar_4.setText(str(round(max(ghr[1416:2160]))))
        self.apr_4.setText(str(round(max(ghr[2160:2880]))))
        self.may_4.setText(str(round(max(ghr[2880:3624]))))
        self.jun_4.setText(str(round(max(ghr[3624:4344]))))
        self.jul_4.setText(str(round(max(ghr[4344:5088]))))
        self.aug_4.setText(str(round(max(ghr[5088:5832]))))
        self.sep_4.setText(str(round(max(ghr[5832:6552]))))
        self.oct_4.setText(str(round(max(ghr[6552:7296]))))
        self.nov_4.setText(str(round(max(ghr[7296:8018]))))
        self.dec_4.setText(str(round(max(ghr[8016:8760]))))
        #### DNR(max) ####
        self.jan_5.setText(str(round(max(dnr[:744]))))
        self.feb_5.setText(str(round(max(dnr[744:1416]))))
        self.mar_5.setText(str(round(max(dnr[1416:2160]))))
        self.apr_5.setText(str(round(max(dnr[2160:2880]))))
        self.may_5.setText(str(round(max(dnr[2880:3624]))))
        self.jun_5.setText(str(round(max(dnr[3624:4344]))))
        self.jul_5.setText(str(round(max(dnr[4344:5088]))))
        self.aug_5.setText(str(round(max(dnr[5088:5832]))))
        self.sep_5.setText(str(round(max(dnr[5832:6552]))))
        self.oct_5.setText(str(round(max(dnr[6552:7296]))))
        self.nov_5.setText(str(round(max(dnr[7296:8018]))))
        self.dec_5.setText(str(round(max(dnr[8016:8760]))))
        #### DR(max) ####
        self.jan_6.setText(str(round(max(dhr[:744]))))
        self.feb_6.setText(str(round(max(dhr[744:1416]))))
        self.mar_6.setText(str(round(max(dhr[1416:2160]))))
        self.apr_6.setText(str(round(max(dhr[2160:2880]))))
        self.may_6.setText(str(round(max(dhr[2880:3624]))))
        self.jun_6.setText(str(round(max(dhr[3624:4344]))))
        self.jul_6.setText(str(round(max(dhr[4344:5088]))))
        self.aug_6.setText(str(round(max(dhr[5088:5832]))))
        self.sep_6.setText(str(round(max(dhr[5832:6552]))))
        self.oct_6.setText(str(round(max(dhr[6552:7296]))))
        self.nov_6.setText(str(round(max(dhr[7296:8018]))))
        self.dec_6.setText(str(round(max(dhr[8016:8760]))))

        ##################################

    def temp_graph(self, text = "DBT"):
        dbt = self.dbt.copy()
        dpt = self.dpt.copy()
        wbt = self.wbt.copy()
        dbt.sort(reverse = True)
        dpt.sort(reverse=True)
        wbt.sort(reverse=True)
        if text == "DBT":
            self.label_design_cond_temp.setText("Design Conditions\n(cooling DBT)")
            self.label_design_cond_val_temp_1.setText("0.4% = " + str(dbt[35]) + "°C")
            self.label_design_cond_val_temp_2.setText("1%   = " + str(dbt[87]) + "°C")
            self.label_design_cond_val_temp_3.setText("2%   = " + str(dbt[175]) + "°C")
            self.canvas_1.temp_plot(text, self.dbt)
        if text == "WBT":
            self.label_design_cond_temp.setText("Design Conditions\n(cooling WBT)")
            self.label_design_cond_val_temp_1.setText("0.4% = " + str(wbt[35]) + "°C")
            self.label_design_cond_val_temp_2.setText("1%   = " + str(wbt[87]) + "°C")
            self.label_design_cond_val_temp_3.setText("2%   = " + str(wbt[175]) + "°C")
            self.canvas_1.temp_plot(text, self.wbt)
        if text == "DPT":
            self.label_design_cond_temp.setText("Design Conditions\n(cooling DPT)")
            self.label_design_cond_val_temp_1.setText("0.4% = " + str(dpt[35]) + "°C")
            self.label_design_cond_val_temp_2.setText("1%   = " + str(dpt[87]) + "°C")
            self.label_design_cond_val_temp_3.setText("2%   = " + str(dpt[175]) + "°C")
            self.canvas_1.temp_plot(text, self.dpt)

    def radia_graph(self, text = "GHR"):
        ghr = self.ghr
        dnr = self.dnr
        dhr = self.dhr
        # for radiation data plot removing 0 #
        self.data_1 = []
        self.data_2 = []
        self.data_3 = []
        self.r = []
        self.s = []
        self.t = []
        c = 0
        days_0 = [0, 744, 1416, 2160, 2880, 3624, 4344, 5088, 5832, 6552, 7296, 8016]
        days_1 = [744, 1416, 2160, 2880, 3624, 4344, 5088, 5832, 6552, 7296, 8016, 8760]
        for i, j in zip(days_0, days_1):
            for z in ghr[i:j]:
                if z != 0:
                    self.data_1.append(z)
                    c = c + 1
            self.r.append(c)
        c = 0
        for i, j in zip(days_0, days_1):
            for z in dnr[i:j]:
                if z != 0:
                    self.data_2.append(z)
                    c = c + 1
            self.s.append(c)
        c = 0
        for i, j in zip(days_0, days_1):
            for z in dhr[i:j]:
                if z != 0:
                    self.data_3.append(z)
                    c = c + 1
            self.t.append(c)
        ghr_wt0 = [self.data_1[:self.r[0]], self.data_1[self.r[0]:self.r[1]], self.data_1[self.r[1]:self.r[2]],
                   self.data_1[self.r[2]:self.r[3]], self.data_1[self.r[3]:self.r[4]], self.data_1[self.r[4]:self.r[5]],
                   self.data_1[self.r[5]:self.r[6]], self.data_1[self.r[6]:self.r[7]], self.data_1[self.r[7]:self.r[8]],
                   self.data_1[self.r[8]:self.r[9]], self.data_1[self.r[9]:self.r[10]],
                   self.data_1[self.r[10]:self.r[11]]]
        dnr_wt0 = [self.data_2[:self.s[0]], self.data_2[self.s[0]:self.s[1]], self.data_2[self.s[1]:self.s[2]],
                   self.data_2[self.s[2]:self.s[3]], self.data_2[self.s[3]:self.s[4]], self.data_2[self.s[4]:self.s[5]],
                   self.data_2[self.s[5]:self.s[6]], self.data_2[self.s[6]:self.s[7]], self.data_2[self.s[7]:self.s[8]],
                   self.data_2[self.s[8]:self.s[9]], self.data_2[self.s[9]:self.s[10]],
                   self.data_2[self.s[10]:self.s[11]]]
        dhr_wt0 = [self.data_3[:self.t[0]], self.data_3[self.t[0]:self.t[1]], self.data_3[self.t[1]:self.t[2]],
                   self.data_3[self.t[2]:self.t[3]], self.data_3[self.t[3]:self.t[4]], self.data_3[self.t[4]:self.t[5]],
                   self.data_3[self.t[5]:self.t[6]], self.data_3[self.t[6]:self.t[7]], self.data_3[self.t[7]:self.t[8]],
                   self.data_3[self.t[8]:self.t[9]], self.data_3[self.t[9]:self.t[10]],
                   self.data_3[self.t[10]:self.t[11]]]

        self.label_annual_avg_radia_val_1.setText("GHR = " + str(round(sum(self.data_1)/len(self.data_1))) + ' Wh/sq.m')
        self.label_annual_avg_radia_val_2.setText("DNR = " + str(round(sum(self.data_2) / len(self.data_2))) + ' Wh/sq.m')
        self.label_annual_avg_radia_val_3.setText("DR  = " + str(round(sum(self.data_3) / len(self.data_3))) + ' Wh/sq.m')
        if text == "GHR":
            self.canvas_2.radia_plot(text,ghr_wt0)
        if text == "DNR":
            self.canvas_2.radia_plot(text,dnr_wt0)
        if text == "DR":
            self.canvas_2.radia_plot(text,dhr_wt0)

    def illumi_graph(self, text = "DNI"):
        dni = self.dni
        ghi = self.ghi
        # for illuminance data plot removing 0 #
        self.data_4 = []
        self.data_5 = []
        self.ri = []
        self.si = []
        c = 0
        days_0 = [0, 744, 1416, 2160, 2880, 3624, 4344, 5088, 5832, 6552, 7296, 8016]
        days_1 = [744, 1416, 2160, 2880, 3624, 4344, 5088, 5832, 6552, 7296, 8016, 8760]
        for i, j in zip(days_0, days_1):
            for z in dni[i:j]:
                if z != 0:
                    self.data_4.append(z)
                    c = c + 1
            self.ri.append(c)
        c = 0
        for i, j in zip(days_0, days_1):
            for z in ghi[i:j]:
                if z != 0:
                    self.data_5.append(z)
                    c = c + 1
            self.si.append(c)
        dni_wt0 = [self.data_4[:self.ri[0]], self.data_4[self.ri[0]:self.ri[1]], self.data_4[self.ri[1]:self.ri[2]],
                   self.data_4[self.ri[2]:self.ri[3]], self.data_4[self.ri[3]:self.ri[4]], self.data_4[self.ri[4]:self.ri[5]],
                   self.data_4[self.ri[5]:self.ri[6]], self.data_4[self.ri[6]:self.ri[7]], self.data_4[self.ri[7]:self.ri[8]],
                   self.data_4[self.ri[8]:self.ri[9]], self.data_4[self.ri[9]:self.ri[10]],
                   self.data_4[self.ri[10]:self.ri[11]]]
        ghi_wt0 = [self.data_5[:self.si[0]], self.data_5[self.si[0]:self.si[1]], self.data_5[self.si[1]:self.si[2]],
                   self.data_5[self.si[2]:self.si[3]], self.data_5[self.si[3]:self.si[4]], self.data_5[self.si[4]:self.si[5]],
                   self.data_5[self.si[5]:self.si[6]], self.data_5[self.si[6]:self.si[7]], self.data_5[self.si[7]:self.si[8]],
                   self.data_5[self.si[8]:self.si[9]], self.data_5[self.si[9]:self.si[10]],
                   self.data_5[self.si[10]:self.si[11]]]
        self.label_annual_avg_illumi_val_1.setText("DNI = " + str(round(sum(self.data_4) / len(self.data_4))) + ' Lux')
        self.label_annual_avg_illumi_val_2.setText("GHI = " + str(round(sum(self.data_5) / len(self.data_5))) + ' Lux')
        if text == "DNI":
            self.canvas_3.illumi_plot(text, dni_wt0)
        if text == "GHI":
            self.canvas_3.illumi_plot(text, ghi_wt0)

    def windv_graph(self):
        self.label_annual_avg_wind_val_1.setText(str(round(sum(self.wvr)/len(self.wvr),1))+"m/s")
        self.label_annual_max_wind_val_1.setText(str(max(self.wvr)) + "m/s")
        self.canvas_4.windv_plot(self.wvr)

    def grd_graph(self):
        self.canvas_5.grd_plot(self.grd_0, self.grd_1, self.grd_2)

    def hour_graph(self):
        dbt_array = []
        for i in range(24):
            dbt_day = []
            c = i
            for j in range(365):
                dbt_day.append(self.dbt[c])
                c = c + 24
            dbt_array.append(dbt_day)
        self.canvas_6.hour_plot(dbt_array)

    def d_graph(self):
        from mpl_toolkits.mplot3d import Axes3D
        dbt = self.dbt
        d = self.d
        h = self.h
        fig = plt.figure(figsize=(24,16))
        ax = Axes3D(fig)
        x = np.linspace(1, 365, 365)
        y = np.linspace(0, 23, 24)
        Y, X = np.meshgrid(y, x)
        dbt_array = []
        for i in range(365):
            dbt_day = []
            for j in range(24):
                c = i * 24 + j
                dbt_day.append(dbt[c])
            dbt_array.append(dbt_day)
        Z = np.array(dbt_array)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
        ax.set_zlabel('Temperature $°C$')
        ax.xaxis.set_major_locator(ticker.IndexLocator(base=30.4166, offset=0.5))
        ax.xaxis.set_minor_locator(ticker.IndexLocator(base=30.4166, offset=15.5))
        ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
        ax.xaxis.set_minor_formatter(ticker.NullFormatter())
        ax.yaxis.set_major_locator(ticker.IndexLocator(base=2, offset=0))
        ax.yaxis.set_major_formatter(ticker.FixedFormatter(
            ['0 a.m.', '2 a.m.', '4 a.m.', '6 a.m.', '8 a.m.', '10 a.m.', '12 noon', '2 p.m.', '4 p.m.', '6 p.m.',
             '8 p.m.', '10 p.m.', '12 p.m.']))
        for tick in ax.xaxis.get_minor_ticks():
            tick.tick1line.set_markersize(0)
            tick.tick2line.set_markersize(0)
            tick.label1.set_horizontalalignment('center')

        plt.show()

    def psychrometric_graph(self, text = "0 - 0.5 m/s", comf = 1, epw = 1, evap = 1, thm = 1, sun = 1, custom_dbt = 0, custom_rh = 0, custom_count_psycho = 8760, evap_efficiency = 80 ):
        import psychrolib
        import chart
        dbt = self.dbt
        rh = self.rh
        if custom_dbt == 0 and custom_rh == 0:
            custom_dbt = self.dbt
            custom_rh = self.rh

        psychrolib.SetUnitSystem(psychrolib.SI)
        altitude = self.elevation
        tem = [0, 50]
        hum = [0, 32]

        ################ EPW points as per selection #############

        p = psychrolib.GetStandardAtmPressure(altitude)
        w = []
        for i, j in zip(custom_dbt, custom_rh):
            h = psychrolib.GetHumRatioFromRelHum(i, j / 100, p)
            w.append(h)

        if text == "0 - 0.5 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(28.5, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(28.5, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 28.5, 80, 80, 18, 32, 20, 20, 18, 18, 20, 80, 32, 32, 20, 50, 28.5, 80, 32, 50, 28.5, 80, 34,
                      58.51, 18, 20, 37.4, 6.43, 28.5, 80, 50, b, 18, 20, 24.64, 0, 28.5, 80, 39.587, 43.129, 39.587, 8.433, 24.34, 20, 698.324, 42.952, 2271.766, 75.516, 0.020256, 0.002610, 188.574, 37.902]

        if text == "0.5 - 1.0 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(30, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(30, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 30, 80, 80, 18, 33, 20, 20, 18, 18, 20, 80, 33, 33, 20, 50, 30, 80, 33, 50, 30, 80, 36.5,
                      55.57, 18, 20, 39.9, 5.62, 30, 80, 50, b, 18, 20, 24.64, 0, 30, 80, 39.862, 46.344, 39.862, 8.310, 24.34, 20, 498.421, 41.2822, 2240.896, 80.7249, 0.022154, 0.002610, 170.255, 36.953]

        if text == "1.0 - 1.5 m/s":
            a = psychrolib.GetTWetBulbFromRelHum(31, .8, p)
            b = 100 * psychrolib.GetRelHumFromTWetBulb(50, a, p)
            c = [psychrolib.GetHumRatioFromRelHum(31, .8, p), psychrolib.GetHumRatioFromRelHum(18, .2, p)]
            points = [18, 31, 80, 80, 18, 34.5, 20, 20, 18, 18, 20, 80, 34.5, 34.5, 20, 50, 31, 80, 34.5, 50, 31, 80,
                      36.5, 58.84, 18, 20, 39.9, 5.62, 31, 80, 50, b, 18, 20, 24.64, 0, 31, 80, 40.212, 48.165, 40.212, 8.156, 24.34, 20, 592.316, 45.227, 2218.0714, 84.278, 0.023507, 0.002610, 159.22, 40.744]

        count = [0, 0, 0, 0]
        for tem_dbt, rehum, humratio in zip(custom_dbt, custom_rh, w):
            ## for evaporative cooler efficiency ##
            comfort_through_evap_cooler = 0
            if evap_efficiency < 100 and evap_efficiency > 0:
                tem_wbt = psychrolib.GetTWetBulbFromRelHum(tem_dbt, rehum/100, p)
                dbt_out_evap_cooler = tem_dbt - (evap_efficiency/100)*(tem_dbt - tem_wbt)
                rh_out_evap_cooler = 100*psychrolib.GetRelHumFromTWetBulb(dbt_out_evap_cooler, tem_wbt, p)
                hum_ratio_out_evap_cooler = psychrolib.GetHumRatioFromRelHum(dbt_out_evap_cooler, round(rh_out_evap_cooler/100, 2), p)
                #print(tem_dbt, rehum, dbt_out_evap_cooler, rh_out_evap_cooler)
                if dbt_out_evap_cooler <= points[5] and rh_out_evap_cooler >= 20 and hum_ratio_out_evap_cooler < ((points[45] - dbt_out_evap_cooler) / points[44]):
                    comfort_through_evap_cooler = 1
            if evap_efficiency == 100:
                comfort_through_evap_cooler = 1
            

            ##counting hours for every zone ###
            if comf == 1 and tem_dbt >= 18 and tem_dbt <= points[5] and rehum >= 20 and rehum <= 80 and humratio < ((points[45] - tem_dbt) / points[44]):
                count[0] = count[0] + 1
            else:
                if evap == 1 and tem_dbt > 18 and rehum < 80 and humratio < ((points[47] - tem_dbt) / points[46]) and humratio > ((24.64 - tem_dbt) / 2490.6226) and comfort_through_evap_cooler == 1:
                    count[1] = count[1] + 1
                if thm == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > points[49] and humratio < ((points[51] - tem_dbt) / points[50]):
                    count[2] = count[2] + 1
                if sun == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > 0.003941434281894339 and tem_dbt < points[38]:
                    count[3] = count[3] + 1

        dbt_can_comf = [[],[],[]]
        rh_can_comf = [[],[],[]]
        dbt_out_comf = []
        rh_out_comf = []
        dbt_comf = []
        rh_comf = []

        c = [0, 0, 0, 0, 0]
        for tem_dbt, rehum, humratio in zip(custom_dbt, custom_rh, w):

            ## for evaporative cooler efficiency ##
            comfort_through_evap_cooler = 0
            if evap_efficiency < 100 and evap_efficiency > 0:
                tem_wbt = psychrolib.GetTWetBulbFromRelHum(tem_dbt, rehum / 100, p)
                dbt_out_evap_cooler = tem_dbt - (evap_efficiency / 100) * (tem_dbt - tem_wbt)
                rh_out_evap_cooler = 100 * psychrolib.GetRelHumFromTWetBulb(dbt_out_evap_cooler, tem_wbt, p)
                hum_ratio_out_evap_cooler = psychrolib.GetHumRatioFromRelHum(dbt_out_evap_cooler,
                                                                             round(rh_out_evap_cooler / 100, 2), p)
                #print(tem_dbt, rehum, dbt_out_evap_cooler, rh_out_evap_cooler)
                if dbt_out_evap_cooler <= points[5] and rh_out_evap_cooler >= 20 and hum_ratio_out_evap_cooler < (
                        (points[45] - dbt_out_evap_cooler) / points[44]):
                    comfort_through_evap_cooler = 1
            if evap_efficiency == 100:
                comfort_through_evap_cooler = 1


            if  tem_dbt >= 18 and tem_dbt <= points[
                5] and rehum >= 20 and rehum <= 80 and humratio < (
                    (points[45] - tem_dbt) / points[44]):
                dbt_comf.append(tem_dbt)
                rh_comf.append(rehum)
                c[0] = c[0] + 1
            else:
                if evap == 1 and tem_dbt > 18 and rehum < 80 and humratio < (
                        (points[47] - tem_dbt) / points[46]) and humratio > ((24.64 - tem_dbt) / 2490.6226) and comfort_through_evap_cooler == 1:
                    dbt_can_comf[0].append(tem_dbt)
                    rh_can_comf[0].append(rehum)
                    c[1] = c[1] + 1
                elif thm == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[48] and humratio > points[
                    49] and humratio < ((points[51] - tem_dbt) / points[50]):
                    dbt_can_comf[1].append(tem_dbt)
                    rh_can_comf[1].append(rehum)
                    c[2] = c[2] + 1
                elif sun == 1 and tem_dbt > 18 and rehum < 80 and humratio < points[
                    48] and humratio > 0.003941434281894339 and tem_dbt < points[38]:
                    dbt_can_comf[2].append(tem_dbt)
                    rh_can_comf[2].append(rehum)
                    c[3] = c[3] + 1
                else:
                    dbt_out_comf.append(tem_dbt)
                    rh_out_comf.append(rehum)
                    c[4] = c[4] + 1
        max_c_value = max(count[1],count[2],count[3])
        max_passive  = ""
        if max_c_value == count[1]:
            max_passive = "Evaporative Cooling"
        if max_c_value == count[2]:
            max_passive = "Thermal Mass"
        if max_c_value == count[3]:
            max_passive = "Sun Shading"

        self.label_max_passive.setText( "o  " + str(round(((count[0] * 100) / custom_count_psycho), 2)) + "% of hours of outdoor conditions are already comfortable.\n"
                                        "o  " + str(round(((count[1] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Evaporative cooling system is used in building.\n"
                                        "o  " + str(round(((count[2] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Thermal mass is used in building.\n"
                                        "o  " + str(round(((count[3] * 100) / custom_count_psycho), 2)) +"% of hours can be made comfortable if Sun shading devices is used in building.\n"
                                        "o  " + "The possible comfortable hours using the selected passive design strategies is " + str(round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 2)) + "%.")
        self.checkbox_comf.setText("Comfortable Outdoor Conditions (" + str(round(((count[0]*100)/custom_count_psycho), 1)) + "%)")
        self.checkbox_evap.setText("Evaporative cooling (" + str(round(((count[1] * 100) / custom_count_psycho), 1)) + "%)")
        self.checkbox_thml.setText("Thermal mass (" + str(round(((count[2] * 100) / custom_count_psycho), 1)) + "%)")
        self.checkbox_sunshad.setText("Sun shading (" + str(round(((count[3] * 100) / custom_count_psycho))) + "%)")
        self.checkbox_comf_net.setText("Possible Comfort hours (passive) (" + str(round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 1)) + "%)")
        self.checkbox_active_points.setText("Active Cooling/Heating/Dehum (" + str(round(100 - round((((c[0]+c[1]+c[2]+c[3]) * 100) / custom_count_psycho), 1))) + "%)")
        self.canvas_8.psycho_plot(dbt, rh, w, altitude, tem, hum, text, comf, epw, evap, thm, sun, points, dbt_can_comf, rh_can_comf, dbt_out_comf, rh_out_comf, dbt_comf, rh_comf, c)

    def file_input_widget(self):
        ####################################
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(184, 255, 164);")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)
        self.line_2_0 = QtWidgets.QFrame(self.centralwidget)
        self.line_2_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_0.setObjectName("line_2_0")
        self.gridLayout_2.addWidget(self.line_2_0, 1, 0, 1, 1)
        self.line_2_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_2_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_1.setObjectName("line_2_1")
        self.gridLayout_2.addWidget(self.line_2_1, 1, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.select_butt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.select_butt.setFont(font)
        self.select_butt.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "color: #003333;\n"
                                        "background-color: #66FFFF;\n"
                                        "border: 5px solid transparent;\n"
                                        "font-size: 15px;\n"
                                        "border-radius: 5px;\n"
                                        "\n"
                                        "}\n"
                                       "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: #00CCCC;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #33FFFF, stop: 1 #009999);\n"
                                        "}\n"
                                        "")
        self.select_butt.setObjectName("select_butt")
        self.verticalLayout_2.addWidget(self.select_butt)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.browse_butt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.browse_butt.setFont(font)
        self.browse_butt.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "color: #003333;\n"
                                        "background-color: #66FFFF;\n"
                                        "border: 5px solid transparent;\n"
                                        "font-size: 15px;\n"
                                        "border-radius: 5px;\n"
                                        "\n"
                                        "}\n"
                                       "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: #00CCCC;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #33FFFF, stop: 1 #009999);\n"
                                        "}\n"
                                        "")
        self.browse_butt.setObjectName("browse_butt")
        self.verticalLayout_2.addWidget(self.browse_butt)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.mnit_logo = QtWidgets.QLabel(self.widget)
        mnit_logo_path = self.resource_path("MNIT_logo.png")
        self.mnit_pixmap = QtGui.QPixmap(mnit_logo_path)
        self.mnit_logo.setPixmap(self.mnit_pixmap)
        self.gridLayout_2.addWidget(self.mnit_logo, 2, 0, 1, 1)
        self.pdc_logo = QtWidgets.QLabel(self.widget)
        pdc_logo_path = self.resource_path("PDC_logo.png")
        self.pdc_pixmap = QtGui.QPixmap(pdc_logo_path)
        self.pdc_logo.setPixmap(self.pdc_pixmap)
        self.gridLayout_2.addWidget(self.pdc_logo, 0, 0, 1, 1)
        self.devlop_detail = QtWidgets.QTextEdit(self.widget)
        self.devlop_detail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.devlop_detail.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                 "p, li { white-space: pre-wrap; }\n"
                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                 "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; font-weight:600;\">Developed by:</span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\"> Raj Gupta </span></p>\n"
                                 "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; font-weight:600;\">Supervisor:</span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\"> Prof. Jyotirmay Mathur (CEE, MNIT, Jaipur)</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                 "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria,serif\'; font-size:12pt; font-weight:600;\">Developed under:</span><span style=\" font-family:\'Cambria,serif\'; font-size:12pt;\"> PG Project grant from ISHRAE in 2019-2020.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")
        self.devlop_detail.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.gridLayout_2.addWidget(self.devlop_detail, 2, 1, 1, 1)
        self.ishrae_logo = QtWidgets.QLabel(self.widget)
        ishrae_logo_path = self.resource_path("ISHRAE_logo.png")
        self.ishrae_pixmap = QtGui.QPixmap(ishrae_logo_path)
        self.ishrae_logo.setPixmap(self.ishrae_pixmap)
        self.gridLayout_2.addWidget(self.ishrae_logo, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi_input(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ####################################

        #######################
        self.select_butt.clicked.connect(lambda: self.select_file())
        self.browse_butt.clicked.connect(lambda: self.browse_file())
        #######################

    def Next_wid(self,fpath):
        #################################

        self.canvas_1 = myCanvas()
        self.canvas_2 = myCanvas()
        self.canvas_3 = myCanvas()
        self.canvas_4 = myCanvas()
        self.canvas_5 = myCanvas()
        self.canvas_6 = myCanvas()
        self.canvas_8 = myCanvas()
        self.canvas_9 = myCanvas()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.WFS_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.WFS_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.WFS_tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.WFS_tab.setStyleSheet("QTabBar::tab:selected\n"
                                        "{\n"
                                        "background: #3399FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                    "QTabBar::tab:!selected\n"
                                        "{\n"
                                        "background: #99CCFF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                   )
        self.WFS_tab.setDocumentMode(False)
        self.WFS_tab.setTabsClosable(False)
        self.WFS_tab.setMovable(False)
        self.WFS_tab.setTabBarAutoHide(False)
        self.WFS_tab.setObjectName("WFS_tab")
        self.WFS_tab1 = QtWidgets.QWidget()
        self.WFS_tab1.setObjectName("WFS_tab1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.WFS_tab1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Monthly_mean = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Monthly_mean.sizePolicy().hasHeightForWidth())
        self.Monthly_mean.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Monthly_mean.setFont(font)
        self.Monthly_mean.setAutoFillBackground(True)
        self.Monthly_mean.setFrameShape(QtWidgets.QFrame.Box)
        self.Monthly_mean.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Monthly_mean.setObjectName("Monthly_mean")
        self.verticalLayout_3.addWidget(self.Monthly_mean)
        self.label_15 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(True)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_16 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(True)
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_2 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_10 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_4 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)

        self.label_tm = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tm.sizePolicy().hasHeightForWidth())
        self.label_tm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tm.setFont(font)
        self.label_tm.setAutoFillBackground(True)
        self.label_tm.setFrameShape(QtWidgets.QFrame.Box)
        self.label_tm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_tm.setObjectName("label_tm")
        self.verticalLayout_3.addWidget(self.label_tm)

        self.horizontalLayout_19.addLayout(self.verticalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Jan = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Jan.sizePolicy().hasHeightForWidth())
        self.Jan.setSizePolicy(sizePolicy)
        self.Jan.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Jan.setAutoFillBackground(True)
        self.Jan.setFrameShape(QtWidgets.QFrame.Box)
        self.Jan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Jan.setAlignment(QtCore.Qt.AlignCenter)
        self.Jan.setObjectName("Jan")
        self.gridLayout_2.addWidget(self.Jan, 0, 1, 1, 1)
        self.Feb = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Feb.sizePolicy().hasHeightForWidth())
        self.Feb.setSizePolicy(sizePolicy)
        self.Feb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Feb.setAutoFillBackground(True)
        self.Feb.setFrameShape(QtWidgets.QFrame.Box)
        self.Feb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Feb.setAlignment(QtCore.Qt.AlignCenter)
        self.Feb.setObjectName("Feb")
        self.gridLayout_2.addWidget(self.Feb, 0, 2, 1, 1)
        self.Mar = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mar.sizePolicy().hasHeightForWidth())
        self.Mar.setSizePolicy(sizePolicy)
        self.Mar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Mar.setAutoFillBackground(True)
        self.Mar.setFrameShape(QtWidgets.QFrame.Box)
        self.Mar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mar.setAlignment(QtCore.Qt.AlignCenter)
        self.Mar.setObjectName("Mar")
        self.gridLayout_2.addWidget(self.Mar, 0, 3, 1, 1)
        self.Apr = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Apr.sizePolicy().hasHeightForWidth())
        self.Apr.setSizePolicy(sizePolicy)
        self.Apr.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Apr.setAutoFillBackground(True)
        self.Apr.setFrameShape(QtWidgets.QFrame.Box)
        self.Apr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Apr.setAlignment(QtCore.Qt.AlignCenter)
        self.Apr.setObjectName("Apr")
        self.gridLayout_2.addWidget(self.Apr, 0, 4, 1, 1)
        self.May = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.May.sizePolicy().hasHeightForWidth())
        self.May.setSizePolicy(sizePolicy)
        self.May.setMaximumSize(QtCore.QSize(16777215, 25))
        self.May.setAutoFillBackground(True)
        self.May.setFrameShape(QtWidgets.QFrame.Box)
        self.May.setFrameShadow(QtWidgets.QFrame.Raised)
        self.May.setAlignment(QtCore.Qt.AlignCenter)
        self.May.setObjectName("May")
        self.gridLayout_2.addWidget(self.May, 0, 5, 1, 1)
        self.Jun = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Jun.sizePolicy().hasHeightForWidth())
        self.Jun.setSizePolicy(sizePolicy)
        self.Jun.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Jun.setAutoFillBackground(True)
        self.Jun.setFrameShape(QtWidgets.QFrame.Box)
        self.Jun.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Jun.setAlignment(QtCore.Qt.AlignCenter)
        self.Jun.setObjectName("Jun")
        self.gridLayout_2.addWidget(self.Jun, 0, 6, 1, 1)
        self.Jul = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Jul.sizePolicy().hasHeightForWidth())
        self.Jul.setSizePolicy(sizePolicy)
        self.Jul.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Jul.setAutoFillBackground(True)
        self.Jul.setFrameShape(QtWidgets.QFrame.Box)
        self.Jul.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Jul.setAlignment(QtCore.Qt.AlignCenter)
        self.Jul.setObjectName("Jul")
        self.gridLayout_2.addWidget(self.Jul, 0, 7, 1, 1)
        self.Aug = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Aug.sizePolicy().hasHeightForWidth())
        self.Aug.setSizePolicy(sizePolicy)
        self.Aug.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Aug.setAutoFillBackground(True)
        self.Aug.setFrameShape(QtWidgets.QFrame.Box)
        self.Aug.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Aug.setAlignment(QtCore.Qt.AlignCenter)
        self.Aug.setObjectName("Aug")
        self.gridLayout_2.addWidget(self.Aug, 0, 8, 1, 1)
        self.Sep = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sep.sizePolicy().hasHeightForWidth())
        self.Sep.setSizePolicy(sizePolicy)
        self.Sep.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Sep.setAutoFillBackground(True)
        self.Sep.setFrameShape(QtWidgets.QFrame.Box)
        self.Sep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Sep.setAlignment(QtCore.Qt.AlignCenter)
        self.Sep.setObjectName("Sep")
        self.gridLayout_2.addWidget(self.Sep, 0, 9, 1, 1)
        self.Oct = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Oct.sizePolicy().hasHeightForWidth())
        self.Oct.setSizePolicy(sizePolicy)
        self.Oct.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Oct.setAutoFillBackground(True)
        self.Oct.setFrameShape(QtWidgets.QFrame.Box)
        self.Oct.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Oct.setAlignment(QtCore.Qt.AlignCenter)
        self.Oct.setObjectName("Oct")
        self.gridLayout_2.addWidget(self.Oct, 0, 10, 1, 1)
        self.Nov = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Nov.sizePolicy().hasHeightForWidth())
        self.Nov.setSizePolicy(sizePolicy)
        self.Nov.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Nov.setAutoFillBackground(True)
        self.Nov.setFrameShape(QtWidgets.QFrame.Box)
        self.Nov.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Nov.setAlignment(QtCore.Qt.AlignCenter)
        self.Nov.setObjectName("Nov")
        self.gridLayout_2.addWidget(self.Nov, 0, 11, 1, 1)
        self.Dec = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dec.sizePolicy().hasHeightForWidth())
        self.Dec.setSizePolicy(sizePolicy)
        self.Dec.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Dec.setAutoFillBackground(True)
        self.Dec.setFrameShape(QtWidgets.QFrame.Box)
        self.Dec.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Dec.setAlignment(QtCore.Qt.AlignCenter)
        self.Dec.setObjectName("Dec")
        self.gridLayout_2.addWidget(self.Dec, 0, 12, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.WFS_tab1)
        self.label_73.setMinimumSize(QtCore.QSize(0, 21))
        self.label_73.setText("")
        self.label_73.setObjectName("label_73")
        self.gridLayout_2.addWidget(self.label_73, 0, 0, 1, 1)
        self.jan_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_1.sizePolicy().hasHeightForWidth())
        self.jan_1.setSizePolicy(sizePolicy)
        self.jan_1.setAutoFillBackground(True)
        self.jan_1.setReadOnly(True)
        self.jan_1.setObjectName("jan_1")
        self.gridLayout_2.addWidget(self.jan_1, 1, 1, 1, 1)
        self.feb_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_1.sizePolicy().hasHeightForWidth())
        self.feb_1.setSizePolicy(sizePolicy)
        self.feb_1.setAutoFillBackground(True)
        self.feb_1.setReadOnly(True)
        self.feb_1.setObjectName("feb_1")
        self.gridLayout_2.addWidget(self.feb_1, 1, 2, 1, 1)
        self.mar_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_1.sizePolicy().hasHeightForWidth())
        self.mar_1.setSizePolicy(sizePolicy)
        self.mar_1.setAutoFillBackground(True)
        self.mar_1.setReadOnly(True)
        self.mar_1.setObjectName("mar_1")
        self.gridLayout_2.addWidget(self.mar_1, 1, 3, 1, 1)
        self.apr_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_1.sizePolicy().hasHeightForWidth())
        self.apr_1.setSizePolicy(sizePolicy)
        self.apr_1.setAutoFillBackground(True)
        self.apr_1.setReadOnly(True)
        self.apr_1.setObjectName("apr_1")
        self.gridLayout_2.addWidget(self.apr_1, 1, 4, 1, 1)
        self.may_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_1.sizePolicy().hasHeightForWidth())
        self.may_1.setSizePolicy(sizePolicy)
        self.may_1.setAutoFillBackground(True)
        self.may_1.setReadOnly(True)
        self.may_1.setObjectName("may_1")
        self.gridLayout_2.addWidget(self.may_1, 1, 5, 1, 1)
        self.jun_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_1.sizePolicy().hasHeightForWidth())
        self.jun_1.setSizePolicy(sizePolicy)
        self.jun_1.setAutoFillBackground(True)
        self.jun_1.setReadOnly(True)
        self.jun_1.setObjectName("jun_1")
        self.gridLayout_2.addWidget(self.jun_1, 1, 6, 1, 1)
        self.jul_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_1.sizePolicy().hasHeightForWidth())
        self.jul_1.setSizePolicy(sizePolicy)
        self.jul_1.setAutoFillBackground(True)
        self.jul_1.setReadOnly(True)
        self.jul_1.setObjectName("jul_1")
        self.gridLayout_2.addWidget(self.jul_1, 1, 7, 1, 1)
        self.aug_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_1.sizePolicy().hasHeightForWidth())
        self.aug_1.setSizePolicy(sizePolicy)
        self.aug_1.setAutoFillBackground(True)
        self.aug_1.setReadOnly(True)
        self.aug_1.setObjectName("aug_1")
        self.gridLayout_2.addWidget(self.aug_1, 1, 8, 1, 1)
        self.sep_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_1.sizePolicy().hasHeightForWidth())
        self.sep_1.setSizePolicy(sizePolicy)
        self.sep_1.setAutoFillBackground(True)
        self.sep_1.setReadOnly(True)
        self.sep_1.setObjectName("sep_1")
        self.gridLayout_2.addWidget(self.sep_1, 1, 9, 1, 1)
        self.oct_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_1.sizePolicy().hasHeightForWidth())
        self.oct_1.setSizePolicy(sizePolicy)
        self.oct_1.setAutoFillBackground(True)
        self.oct_1.setReadOnly(True)
        self.oct_1.setObjectName("oct_1")
        self.gridLayout_2.addWidget(self.oct_1, 1, 10, 1, 1)
        self.nov_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_1.sizePolicy().hasHeightForWidth())
        self.nov_1.setSizePolicy(sizePolicy)
        self.nov_1.setAutoFillBackground(True)
        self.nov_1.setReadOnly(True)
        self.nov_1.setObjectName("nov_1")
        self.gridLayout_2.addWidget(self.nov_1, 1, 11, 1, 1)
        self.dec_1 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_1.sizePolicy().hasHeightForWidth())
        self.dec_1.setSizePolicy(sizePolicy)
        self.dec_1.setAutoFillBackground(True)
        self.dec_1.setReadOnly(True)
        self.dec_1.setObjectName("dec_1")
        self.gridLayout_2.addWidget(self.dec_1, 1, 12, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setAutoFillBackground(True)
        self.label_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 1, 0, 1, 1)
        self.jan_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_2.sizePolicy().hasHeightForWidth())
        self.jan_2.setSizePolicy(sizePolicy)
        self.jan_2.setAutoFillBackground(True)
        self.jan_2.setReadOnly(True)
        self.jan_2.setObjectName("jan_2")
        self.gridLayout_2.addWidget(self.jan_2, 2, 1, 1, 1)
        self.feb_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_2.sizePolicy().hasHeightForWidth())
        self.feb_2.setSizePolicy(sizePolicy)
        self.feb_2.setAutoFillBackground(True)
        self.feb_2.setReadOnly(True)
        self.feb_2.setObjectName("feb_2")
        self.gridLayout_2.addWidget(self.feb_2, 2, 2, 1, 1)
        self.mar_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_2.sizePolicy().hasHeightForWidth())
        self.mar_2.setSizePolicy(sizePolicy)
        self.mar_2.setAutoFillBackground(True)
        self.mar_2.setReadOnly(True)
        self.mar_2.setObjectName("mar_2")
        self.gridLayout_2.addWidget(self.mar_2, 2, 3, 1, 1)
        self.apr_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_2.sizePolicy().hasHeightForWidth())
        self.apr_2.setSizePolicy(sizePolicy)
        self.apr_2.setAutoFillBackground(True)
        self.apr_2.setReadOnly(True)
        self.apr_2.setObjectName("apr_2")
        self.gridLayout_2.addWidget(self.apr_2, 2, 4, 1, 1)
        self.may_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_2.sizePolicy().hasHeightForWidth())
        self.may_2.setSizePolicy(sizePolicy)
        self.may_2.setAutoFillBackground(True)
        self.may_2.setReadOnly(True)
        self.may_2.setObjectName("may_2")
        self.gridLayout_2.addWidget(self.may_2, 2, 5, 1, 1)
        self.jun_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_2.sizePolicy().hasHeightForWidth())
        self.jun_2.setSizePolicy(sizePolicy)
        self.jun_2.setAutoFillBackground(True)
        self.jun_2.setReadOnly(True)
        self.jun_2.setObjectName("jun_2")
        self.gridLayout_2.addWidget(self.jun_2, 2, 6, 1, 1)
        self.jul_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_2.sizePolicy().hasHeightForWidth())
        self.jul_2.setSizePolicy(sizePolicy)
        self.jul_2.setAutoFillBackground(True)
        self.jul_2.setReadOnly(True)
        self.jul_2.setObjectName("jul_2")
        self.gridLayout_2.addWidget(self.jul_2, 2, 7, 1, 1)
        self.aug_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_2.sizePolicy().hasHeightForWidth())
        self.aug_2.setSizePolicy(sizePolicy)
        self.aug_2.setAutoFillBackground(True)
        self.aug_2.setReadOnly(True)
        self.aug_2.setObjectName("aug_2")
        self.gridLayout_2.addWidget(self.aug_2, 2, 8, 1, 1)
        self.sep_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_2.sizePolicy().hasHeightForWidth())
        self.sep_2.setSizePolicy(sizePolicy)
        self.sep_2.setAutoFillBackground(True)
        self.sep_2.setReadOnly(True)
        self.sep_2.setObjectName("sep_2")
        self.gridLayout_2.addWidget(self.sep_2, 2, 9, 1, 1)
        self.oct_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_2.sizePolicy().hasHeightForWidth())
        self.oct_2.setSizePolicy(sizePolicy)
        self.oct_2.setAutoFillBackground(True)
        self.oct_2.setReadOnly(True)
        self.oct_2.setObjectName("oct_2")
        self.gridLayout_2.addWidget(self.oct_2, 2, 10, 1, 1)
        self.nov_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_2.sizePolicy().hasHeightForWidth())
        self.nov_2.setSizePolicy(sizePolicy)
        self.nov_2.setAutoFillBackground(True)
        self.nov_2.setReadOnly(True)
        self.nov_2.setObjectName("nov_2")
        self.gridLayout_2.addWidget(self.nov_2, 2, 11, 1, 1)
        self.dec_2 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_2.sizePolicy().hasHeightForWidth())
        self.dec_2.setSizePolicy(sizePolicy)
        self.dec_2.setAutoFillBackground(True)
        self.dec_2.setReadOnly(True)
        self.dec_2.setObjectName("dec_2")
        self.gridLayout_2.addWidget(self.dec_2, 2, 12, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setAutoFillBackground(True)
        self.label_51.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 2, 0, 1, 1)
        self.jan_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_3.sizePolicy().hasHeightForWidth())
        self.jan_3.setSizePolicy(sizePolicy)
        self.jan_3.setAutoFillBackground(True)
        self.jan_3.setReadOnly(True)
        self.jan_3.setObjectName("jan_3")
        self.gridLayout_2.addWidget(self.jan_3, 3, 1, 1, 1)
        self.feb_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_3.sizePolicy().hasHeightForWidth())
        self.feb_3.setSizePolicy(sizePolicy)
        self.feb_3.setAutoFillBackground(True)
        self.feb_3.setReadOnly(True)
        self.feb_3.setObjectName("feb_3")
        self.gridLayout_2.addWidget(self.feb_3, 3, 2, 1, 1)
        self.mar_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_3.sizePolicy().hasHeightForWidth())
        self.mar_3.setSizePolicy(sizePolicy)
        self.mar_3.setAutoFillBackground(True)
        self.mar_3.setReadOnly(True)
        self.mar_3.setObjectName("mar_3")
        self.gridLayout_2.addWidget(self.mar_3, 3, 3, 1, 1)
        self.apr_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_3.sizePolicy().hasHeightForWidth())
        self.apr_3.setSizePolicy(sizePolicy)
        self.apr_3.setAutoFillBackground(True)
        self.apr_3.setReadOnly(True)
        self.apr_3.setObjectName("apr_3")
        self.gridLayout_2.addWidget(self.apr_3, 3, 4, 1, 1)
        self.may_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_3.sizePolicy().hasHeightForWidth())
        self.may_3.setSizePolicy(sizePolicy)
        self.may_3.setAutoFillBackground(True)
        self.may_3.setReadOnly(True)
        self.may_3.setObjectName("may_3")
        self.gridLayout_2.addWidget(self.may_3, 3, 5, 1, 1)
        self.jun_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_3.sizePolicy().hasHeightForWidth())
        self.jun_3.setSizePolicy(sizePolicy)
        self.jun_3.setAutoFillBackground(True)
        self.jun_3.setReadOnly(True)
        self.jun_3.setObjectName("jun_3")
        self.gridLayout_2.addWidget(self.jun_3, 3, 6, 1, 1)
        self.jul_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_3.sizePolicy().hasHeightForWidth())
        self.jul_3.setSizePolicy(sizePolicy)
        self.jul_3.setAutoFillBackground(True)
        self.jul_3.setReadOnly(True)
        self.jul_3.setObjectName("jul_3")
        self.gridLayout_2.addWidget(self.jul_3, 3, 7, 1, 1)
        self.aug_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_3.sizePolicy().hasHeightForWidth())
        self.aug_3.setSizePolicy(sizePolicy)
        self.aug_3.setAutoFillBackground(True)
        self.aug_3.setReadOnly(True)
        self.aug_3.setObjectName("aug_3")
        self.gridLayout_2.addWidget(self.aug_3, 3, 8, 1, 1)
        self.sep_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_3.sizePolicy().hasHeightForWidth())
        self.sep_3.setSizePolicy(sizePolicy)
        self.sep_3.setAutoFillBackground(True)
        self.sep_3.setReadOnly(True)
        self.sep_3.setObjectName("sep_3")
        self.gridLayout_2.addWidget(self.sep_3, 3, 9, 1, 1)
        self.oct_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_3.sizePolicy().hasHeightForWidth())
        self.oct_3.setSizePolicy(sizePolicy)
        self.oct_3.setAutoFillBackground(True)
        self.oct_3.setReadOnly(True)
        self.oct_3.setObjectName("oct_3")
        self.gridLayout_2.addWidget(self.oct_3, 3, 10, 1, 1)
        self.nov_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_3.sizePolicy().hasHeightForWidth())
        self.nov_3.setSizePolicy(sizePolicy)
        self.nov_3.setAutoFillBackground(True)
        self.nov_3.setReadOnly(True)
        self.nov_3.setObjectName("nov_3")
        self.gridLayout_2.addWidget(self.nov_3, 3, 11, 1, 1)
        self.dec_3 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_3.sizePolicy().hasHeightForWidth())
        self.dec_3.setSizePolicy(sizePolicy)
        self.dec_3.setAutoFillBackground(True)
        self.dec_3.setReadOnly(True)
        self.dec_3.setObjectName("dec_3")
        self.gridLayout_2.addWidget(self.dec_3, 3, 12, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setAutoFillBackground(True)
        self.label_52.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_52.setObjectName("label_52")
        self.gridLayout_2.addWidget(self.label_52, 3, 0, 1, 1)
        self.jan_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_4.sizePolicy().hasHeightForWidth())
        self.jan_4.setSizePolicy(sizePolicy)
        self.jan_4.setAutoFillBackground(True)
        self.jan_4.setReadOnly(True)
        self.jan_4.setObjectName("jan_4")
        self.gridLayout_2.addWidget(self.jan_4, 4, 1, 1, 1)
        self.feb_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_4.sizePolicy().hasHeightForWidth())
        self.feb_4.setSizePolicy(sizePolicy)
        self.feb_4.setAutoFillBackground(True)
        self.feb_4.setReadOnly(True)
        self.feb_4.setObjectName("feb_4")
        self.gridLayout_2.addWidget(self.feb_4, 4, 2, 1, 1)
        self.mar_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_4.sizePolicy().hasHeightForWidth())
        self.mar_4.setSizePolicy(sizePolicy)
        self.mar_4.setAutoFillBackground(True)
        self.mar_4.setReadOnly(True)
        self.mar_4.setObjectName("mar_4")
        self.gridLayout_2.addWidget(self.mar_4, 4, 3, 1, 1)
        self.apr_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_4.sizePolicy().hasHeightForWidth())
        self.apr_4.setSizePolicy(sizePolicy)
        self.apr_4.setAutoFillBackground(True)
        self.apr_4.setReadOnly(True)
        self.apr_4.setObjectName("apr_4")
        self.gridLayout_2.addWidget(self.apr_4, 4, 4, 1, 1)
        self.may_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_4.sizePolicy().hasHeightForWidth())
        self.may_4.setSizePolicy(sizePolicy)
        self.may_4.setAutoFillBackground(True)
        self.may_4.setReadOnly(True)
        self.may_4.setObjectName("may_4")
        self.gridLayout_2.addWidget(self.may_4, 4, 5, 1, 1)
        self.jun_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_4.sizePolicy().hasHeightForWidth())
        self.jun_4.setSizePolicy(sizePolicy)
        self.jun_4.setAutoFillBackground(True)
        self.jun_4.setReadOnly(True)
        self.jun_4.setObjectName("jun_4")
        self.gridLayout_2.addWidget(self.jun_4, 4, 6, 1, 1)
        self.jul_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_4.sizePolicy().hasHeightForWidth())
        self.jul_4.setSizePolicy(sizePolicy)
        self.jul_4.setAutoFillBackground(True)
        self.jul_4.setReadOnly(True)
        self.jul_4.setObjectName("jul_4")
        self.gridLayout_2.addWidget(self.jul_4, 4, 7, 1, 1)
        self.aug_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_4.sizePolicy().hasHeightForWidth())
        self.aug_4.setSizePolicy(sizePolicy)
        self.aug_4.setAutoFillBackground(True)
        self.aug_4.setReadOnly(True)
        self.aug_4.setObjectName("aug_4")
        self.gridLayout_2.addWidget(self.aug_4, 4, 8, 1, 1)
        self.sep_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_4.sizePolicy().hasHeightForWidth())
        self.sep_4.setSizePolicy(sizePolicy)
        self.sep_4.setAutoFillBackground(True)
        self.sep_4.setReadOnly(True)
        self.sep_4.setObjectName("sep_4")
        self.gridLayout_2.addWidget(self.sep_4, 4, 9, 1, 1)
        self.oct_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_4.sizePolicy().hasHeightForWidth())
        self.oct_4.setSizePolicy(sizePolicy)
        self.oct_4.setAutoFillBackground(True)
        self.oct_4.setReadOnly(True)
        self.oct_4.setObjectName("oct_4")
        self.gridLayout_2.addWidget(self.oct_4, 4, 10, 1, 1)
        self.nov_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_4.sizePolicy().hasHeightForWidth())
        self.nov_4.setSizePolicy(sizePolicy)
        self.nov_4.setAutoFillBackground(True)
        self.nov_4.setReadOnly(True)
        self.nov_4.setObjectName("nov_4")
        self.gridLayout_2.addWidget(self.nov_4, 4, 11, 1, 1)
        self.dec_4 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_4.sizePolicy().hasHeightForWidth())
        self.dec_4.setSizePolicy(sizePolicy)
        self.dec_4.setAutoFillBackground(True)
        self.dec_4.setReadOnly(True)
        self.dec_4.setObjectName("dec_4")
        self.gridLayout_2.addWidget(self.dec_4, 4, 12, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setAutoFillBackground(True)
        self.label_53.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_53.setObjectName("label_53")
        self.gridLayout_2.addWidget(self.label_53, 4, 0, 1, 1)
        self.jan_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_5.sizePolicy().hasHeightForWidth())
        self.jan_5.setSizePolicy(sizePolicy)
        self.jan_5.setAutoFillBackground(True)
        self.jan_5.setReadOnly(True)
        self.jan_5.setObjectName("jan_5")
        self.gridLayout_2.addWidget(self.jan_5, 5, 1, 1, 1)
        self.feb_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_5.sizePolicy().hasHeightForWidth())
        self.feb_5.setSizePolicy(sizePolicy)
        self.feb_5.setAutoFillBackground(True)
        self.feb_5.setReadOnly(True)
        self.feb_5.setObjectName("feb_5")
        self.gridLayout_2.addWidget(self.feb_5, 5, 2, 1, 1)
        self.mar_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_5.sizePolicy().hasHeightForWidth())
        self.mar_5.setSizePolicy(sizePolicy)
        self.mar_5.setAutoFillBackground(True)
        self.mar_5.setReadOnly(True)
        self.mar_5.setObjectName("mar_5")
        self.gridLayout_2.addWidget(self.mar_5, 5, 3, 1, 1)
        self.apr_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_5.sizePolicy().hasHeightForWidth())
        self.apr_5.setSizePolicy(sizePolicy)
        self.apr_5.setAutoFillBackground(True)
        self.apr_5.setReadOnly(True)
        self.apr_5.setObjectName("apr_5")
        self.gridLayout_2.addWidget(self.apr_5, 5, 4, 1, 1)
        self.may_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_5.sizePolicy().hasHeightForWidth())
        self.may_5.setSizePolicy(sizePolicy)
        self.may_5.setAutoFillBackground(True)
        self.may_5.setReadOnly(True)
        self.may_5.setObjectName("may_5")
        self.gridLayout_2.addWidget(self.may_5, 5, 5, 1, 1)
        self.jun_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_5.sizePolicy().hasHeightForWidth())
        self.jun_5.setSizePolicy(sizePolicy)
        self.jun_5.setAutoFillBackground(True)
        self.jun_5.setReadOnly(True)
        self.jun_5.setObjectName("jun_5")
        self.gridLayout_2.addWidget(self.jun_5, 5, 6, 1, 1)
        self.jul_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_5.sizePolicy().hasHeightForWidth())
        self.jul_5.setSizePolicy(sizePolicy)
        self.jul_5.setAutoFillBackground(True)
        self.jul_5.setReadOnly(True)
        self.jul_5.setObjectName("jul_5")
        self.gridLayout_2.addWidget(self.jul_5, 5,7, 1, 1)
        self.aug_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_5.sizePolicy().hasHeightForWidth())
        self.aug_5.setSizePolicy(sizePolicy)
        self.aug_5.setAutoFillBackground(True)
        self.aug_5.setReadOnly(True)
        self.aug_5.setObjectName("aug_5")
        self.gridLayout_2.addWidget(self.aug_5, 5, 8, 1, 1)
        self.sep_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_5.sizePolicy().hasHeightForWidth())
        self.sep_5.setSizePolicy(sizePolicy)
        self.sep_5.setAutoFillBackground(True)
        self.sep_5.setReadOnly(True)
        self.sep_5.setObjectName("sep_5")
        self.gridLayout_2.addWidget(self.sep_5, 5, 9, 1, 1)
        self.oct_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_5.sizePolicy().hasHeightForWidth())
        self.oct_5.setSizePolicy(sizePolicy)
        self.oct_5.setAutoFillBackground(True)
        self.oct_5.setReadOnly(True)
        self.oct_5.setObjectName("oct_5")
        self.gridLayout_2.addWidget(self.oct_5, 5, 10, 1, 1)
        self.nov_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_5.sizePolicy().hasHeightForWidth())
        self.nov_5.setSizePolicy(sizePolicy)
        self.nov_5.setAutoFillBackground(True)
        self.nov_5.setReadOnly(True)
        self.nov_5.setObjectName("nov_5")
        self.gridLayout_2.addWidget(self.nov_5, 5, 11, 1, 1)
        self.dec_5 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_5.sizePolicy().hasHeightForWidth())
        self.dec_5.setSizePolicy(sizePolicy)
        self.dec_5.setAutoFillBackground(True)
        self.dec_5.setReadOnly(True)
        self.dec_5.setObjectName("dec_5")
        self.gridLayout_2.addWidget(self.dec_5, 5, 12, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setAutoFillBackground(True)
        self.label_55.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 5, 0, 1, 1)
        self.jan_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_6.sizePolicy().hasHeightForWidth())
        self.jan_6.setSizePolicy(sizePolicy)
        self.jan_6.setAutoFillBackground(True)
        self.jan_6.setReadOnly(True)
        self.jan_6.setObjectName("jan_6")
        self.gridLayout_2.addWidget(self.jan_6, 6, 1, 1, 1)
        self.feb_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_6.sizePolicy().hasHeightForWidth())
        self.feb_6.setSizePolicy(sizePolicy)
        self.feb_6.setAutoFillBackground(True)
        self.feb_6.setReadOnly(True)
        self.feb_6.setObjectName("feb_6")
        self.gridLayout_2.addWidget(self.feb_6, 6, 2, 1, 1)
        self.mar_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_6.sizePolicy().hasHeightForWidth())
        self.mar_6.setSizePolicy(sizePolicy)
        self.mar_6.setAutoFillBackground(True)
        self.mar_6.setReadOnly(True)
        self.mar_6.setObjectName("mar_6")
        self.gridLayout_2.addWidget(self.mar_6, 6, 3, 1, 1)
        self.apr_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_6.sizePolicy().hasHeightForWidth())
        self.apr_6.setSizePolicy(sizePolicy)
        self.apr_6.setAutoFillBackground(True)
        self.apr_6.setReadOnly(True)
        self.apr_6.setObjectName("apr_6")
        self.gridLayout_2.addWidget(self.apr_6, 6, 4, 1, 1)
        self.may_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_6.sizePolicy().hasHeightForWidth())
        self.may_6.setSizePolicy(sizePolicy)
        self.may_6.setAutoFillBackground(True)
        self.may_6.setReadOnly(True)
        self.may_6.setObjectName("may_6")
        self.gridLayout_2.addWidget(self.may_6, 6, 5, 1, 1)
        self.jun_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_6.sizePolicy().hasHeightForWidth())
        self.jun_6.setSizePolicy(sizePolicy)
        self.jun_6.setAutoFillBackground(True)
        self.jun_6.setReadOnly(True)
        self.jun_6.setObjectName("jun_6")
        self.gridLayout_2.addWidget(self.jun_6, 6, 6, 1, 1)
        self.jul_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_6.sizePolicy().hasHeightForWidth())
        self.jul_6.setSizePolicy(sizePolicy)
        self.jul_6.setAutoFillBackground(True)
        self.jul_6.setReadOnly(True)
        self.jul_6.setObjectName("jul_6")
        self.gridLayout_2.addWidget(self.jul_6, 6, 7, 1, 1)
        self.aug_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_6.sizePolicy().hasHeightForWidth())
        self.aug_6.setSizePolicy(sizePolicy)
        self.aug_6.setAutoFillBackground(True)
        self.aug_6.setReadOnly(True)
        self.aug_6.setObjectName("aug_6")
        self.gridLayout_2.addWidget(self.aug_6, 6, 8, 1, 1)
        self.sep_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_6.sizePolicy().hasHeightForWidth())
        self.sep_6.setSizePolicy(sizePolicy)
        self.sep_6.setAutoFillBackground(True)
        self.sep_6.setReadOnly(True)
        self.sep_6.setObjectName("sep_6")
        self.gridLayout_2.addWidget(self.sep_6, 6, 9, 1, 1)
        self.oct_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_6.sizePolicy().hasHeightForWidth())
        self.oct_6.setSizePolicy(sizePolicy)
        self.oct_6.setAutoFillBackground(True)
        self.oct_6.setReadOnly(True)
        self.oct_6.setObjectName("oct_6")
        self.gridLayout_2.addWidget(self.oct_6, 6, 10, 1, 1)
        self.nov_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_6.sizePolicy().hasHeightForWidth())
        self.nov_6.setSizePolicy(sizePolicy)
        self.nov_6.setAutoFillBackground(True)
        self.nov_6.setReadOnly(True)
        self.nov_6.setObjectName("nov_6")
        self.gridLayout_2.addWidget(self.nov_6, 6, 11, 1, 1)
        self.dec_6 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_6.sizePolicy().hasHeightForWidth())
        self.dec_6.setSizePolicy(sizePolicy)
        self.dec_6.setAutoFillBackground(True)
        self.dec_6.setReadOnly(True)
        self.dec_6.setObjectName("dec_6")
        self.gridLayout_2.addWidget(self.dec_6, 6, 12, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        self.label_57.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_57.setFont(font)
        self.label_57.setAutoFillBackground(True)
        self.label_57.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_57.setObjectName("label_57")
        self.gridLayout_2.addWidget(self.label_57, 6, 0, 1, 1)
        self.jan_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_7.sizePolicy().hasHeightForWidth())
        self.jan_7.setSizePolicy(sizePolicy)
        self.jan_7.setAutoFillBackground(True)
        self.jan_7.setReadOnly(True)
        self.jan_7.setObjectName("jan_7")
        self.gridLayout_2.addWidget(self.jan_7, 7, 1, 1, 1)
        self.feb_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_7.sizePolicy().hasHeightForWidth())
        self.feb_7.setSizePolicy(sizePolicy)
        self.feb_7.setAutoFillBackground(True)
        self.feb_7.setReadOnly(True)
        self.feb_7.setObjectName("feb_7")
        self.gridLayout_2.addWidget(self.feb_7, 7, 2, 1, 1)
        self.mar_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_7.sizePolicy().hasHeightForWidth())
        self.mar_7.setSizePolicy(sizePolicy)
        self.mar_7.setAutoFillBackground(True)
        self.mar_7.setReadOnly(True)
        self.mar_7.setObjectName("mar_7")
        self.gridLayout_2.addWidget(self.mar_7, 7, 3, 1, 1)
        self.apr_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_7.sizePolicy().hasHeightForWidth())
        self.apr_7.setSizePolicy(sizePolicy)
        self.apr_7.setAutoFillBackground(True)
        self.apr_7.setReadOnly(True)
        self.apr_7.setObjectName("apr_7")
        self.gridLayout_2.addWidget(self.apr_7, 7, 4, 1, 1)
        self.may_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_7.sizePolicy().hasHeightForWidth())
        self.may_7.setSizePolicy(sizePolicy)
        self.may_7.setAutoFillBackground(True)
        self.may_7.setReadOnly(True)
        self.may_7.setObjectName("may_7")
        self.gridLayout_2.addWidget(self.may_7, 7, 5, 1, 1)
        self.jun_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_7.sizePolicy().hasHeightForWidth())
        self.jun_7.setSizePolicy(sizePolicy)
        self.jun_7.setAutoFillBackground(True)
        self.jun_7.setReadOnly(True)
        self.jun_7.setObjectName("jun_7")
        self.gridLayout_2.addWidget(self.jun_7, 7, 6, 1, 1)
        self.jul_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_7.sizePolicy().hasHeightForWidth())
        self.jul_7.setSizePolicy(sizePolicy)
        self.jul_7.setAutoFillBackground(True)
        self.jul_7.setReadOnly(True)
        self.jul_7.setObjectName("jul_7")
        self.gridLayout_2.addWidget(self.jul_7, 7, 7, 1, 1)
        self.aug_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_7.sizePolicy().hasHeightForWidth())
        self.aug_7.setSizePolicy(sizePolicy)
        self.aug_7.setAutoFillBackground(True)
        self.aug_7.setReadOnly(True)
        self.aug_7.setObjectName("aug_7")
        self.gridLayout_2.addWidget(self.aug_7, 7, 8, 1, 1)
        self.sep_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_7.sizePolicy().hasHeightForWidth())
        self.sep_7.setSizePolicy(sizePolicy)
        self.sep_7.setAutoFillBackground(True)
        self.sep_7.setReadOnly(True)
        self.sep_7.setObjectName("sep_7")
        self.gridLayout_2.addWidget(self.sep_7, 7, 9, 1, 1)
        self.oct_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_7.sizePolicy().hasHeightForWidth())
        self.oct_7.setSizePolicy(sizePolicy)
        self.oct_7.setAutoFillBackground(True)
        self.oct_7.setReadOnly(True)
        self.oct_7.setObjectName("oct_7")
        self.gridLayout_2.addWidget(self.oct_7, 7, 10, 1, 1)
        self.nov_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_7.sizePolicy().hasHeightForWidth())
        self.nov_7.setSizePolicy(sizePolicy)
        self.nov_7.setAutoFillBackground(True)
        self.nov_7.setReadOnly(True)
        self.nov_7.setObjectName("nov_7")
        self.gridLayout_2.addWidget(self.nov_7, 7, 11, 1, 1)
        self.dec_7 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_7.sizePolicy().hasHeightForWidth())
        self.dec_7.setSizePolicy(sizePolicy)
        self.dec_7.setAutoFillBackground(True)
        self.dec_7.setReadOnly(True)
        self.dec_7.setObjectName("dec_7")
        self.gridLayout_2.addWidget(self.dec_7, 7, 12, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setAutoFillBackground(True)
        self.label_54.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_54.setObjectName("label_54")
        self.gridLayout_2.addWidget(self.label_54, 7, 0, 1, 1)
        self.jan_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_8.sizePolicy().hasHeightForWidth())
        self.jan_8.setSizePolicy(sizePolicy)
        self.jan_8.setAutoFillBackground(True)
        self.jan_8.setReadOnly(True)
        self.jan_8.setObjectName("jan_8")
        self.gridLayout_2.addWidget(self.jan_8, 8, 1, 1, 1)
        self.feb_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_8.sizePolicy().hasHeightForWidth())
        self.feb_8.setSizePolicy(sizePolicy)
        self.feb_8.setAutoFillBackground(True)
        self.feb_8.setReadOnly(True)
        self.feb_8.setObjectName("feb_8")
        self.gridLayout_2.addWidget(self.feb_8, 8, 2, 1, 1)
        self.mar_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_8.sizePolicy().hasHeightForWidth())
        self.mar_8.setSizePolicy(sizePolicy)
        self.mar_8.setAutoFillBackground(True)
        self.mar_8.setReadOnly(True)
        self.mar_8.setObjectName("mar_8")
        self.gridLayout_2.addWidget(self.mar_8, 8, 3, 1, 1)
        self.apr_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_8.sizePolicy().hasHeightForWidth())
        self.apr_8.setSizePolicy(sizePolicy)
        self.apr_8.setAutoFillBackground(True)
        self.apr_8.setReadOnly(True)
        self.apr_8.setObjectName("apr_8")
        self.gridLayout_2.addWidget(self.apr_8, 8, 4, 1, 1)
        self.may_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_8.sizePolicy().hasHeightForWidth())
        self.may_8.setSizePolicy(sizePolicy)
        self.may_8.setAutoFillBackground(True)
        self.may_8.setReadOnly(True)
        self.may_8.setObjectName("may_8")
        self.gridLayout_2.addWidget(self.may_8, 8, 5, 1, 1)
        self.jun_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_8.sizePolicy().hasHeightForWidth())
        self.jun_8.setSizePolicy(sizePolicy)
        self.jun_8.setAutoFillBackground(True)
        self.jun_8.setReadOnly(True)
        self.jun_8.setObjectName("jun_8")
        self.gridLayout_2.addWidget(self.jun_8, 8, 6, 1, 1)
        self.jul_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_8.sizePolicy().hasHeightForWidth())
        self.jul_8.setSizePolicy(sizePolicy)
        self.jul_8.setAutoFillBackground(True)
        self.jul_8.setReadOnly(True)
        self.jul_8.setObjectName("jul_8")
        self.gridLayout_2.addWidget(self.jul_8, 8, 7, 1, 1)
        self.aug_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_8.sizePolicy().hasHeightForWidth())
        self.aug_8.setSizePolicy(sizePolicy)
        self.aug_8.setAutoFillBackground(True)
        self.aug_8.setReadOnly(True)
        self.aug_8.setObjectName("aug_8")
        self.gridLayout_2.addWidget(self.aug_8, 8, 8, 1, 1)
        self.sep_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_8.sizePolicy().hasHeightForWidth())
        self.sep_8.setSizePolicy(sizePolicy)
        self.sep_8.setAutoFillBackground(True)
        self.sep_8.setReadOnly(True)
        self.sep_8.setObjectName("sep_8")
        self.gridLayout_2.addWidget(self.sep_8, 8, 9, 1, 1)
        self.oct_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_8.sizePolicy().hasHeightForWidth())
        self.oct_8.setSizePolicy(sizePolicy)
        self.oct_8.setAutoFillBackground(True)
        self.oct_8.setReadOnly(True)
        self.oct_8.setObjectName("oct_8")
        self.gridLayout_2.addWidget(self.oct_8, 8, 10, 1, 1)
        self.nov_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_8.sizePolicy().hasHeightForWidth())
        self.nov_8.setSizePolicy(sizePolicy)
        self.nov_8.setAutoFillBackground(True)
        self.nov_8.setReadOnly(True)
        self.nov_8.setObjectName("nov_8")
        self.gridLayout_2.addWidget(self.nov_8, 8, 11, 1, 1)
        self.dec_8 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_8.sizePolicy().hasHeightForWidth())
        self.dec_8.setSizePolicy(sizePolicy)
        self.dec_8.setAutoFillBackground(True)
        self.dec_8.setReadOnly(True)
        self.dec_8.setObjectName("dec_8")
        self.gridLayout_2.addWidget(self.dec_8, 8, 12, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_56.setFont(font)
        self.label_56.setAutoFillBackground(True)
        self.label_56.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 8, 0, 1, 1)
        self.jan_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_9.sizePolicy().hasHeightForWidth())
        self.jan_9.setSizePolicy(sizePolicy)
        self.jan_9.setAutoFillBackground(True)
        self.jan_9.setReadOnly(True)
        self.jan_9.setObjectName("jan_9")
        self.gridLayout_2.addWidget(self.jan_9, 9, 1, 1, 1)
        self.feb_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_9.sizePolicy().hasHeightForWidth())
        self.feb_9.setSizePolicy(sizePolicy)
        self.feb_9.setAutoFillBackground(True)
        self.feb_9.setReadOnly(True)
        self.feb_9.setObjectName("feb_9")
        self.gridLayout_2.addWidget(self.feb_9, 9, 2, 1, 1)
        self.mar_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_9.sizePolicy().hasHeightForWidth())
        self.mar_9.setSizePolicy(sizePolicy)
        self.mar_9.setAutoFillBackground(True)
        self.mar_9.setReadOnly(True)
        self.mar_9.setObjectName("mar_9")
        self.gridLayout_2.addWidget(self.mar_9, 9, 3, 1, 1)
        self.apr_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_9.sizePolicy().hasHeightForWidth())
        self.apr_9.setSizePolicy(sizePolicy)
        self.apr_9.setAutoFillBackground(True)
        self.apr_9.setReadOnly(True)
        self.apr_9.setObjectName("apr_9")
        self.gridLayout_2.addWidget(self.apr_9, 9, 4, 1, 1)
        self.may_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_9.sizePolicy().hasHeightForWidth())
        self.may_9.setSizePolicy(sizePolicy)
        self.may_9.setAutoFillBackground(True)
        self.may_9.setReadOnly(True)
        self.may_9.setObjectName("may_9")
        self.gridLayout_2.addWidget(self.may_9, 9, 5, 1, 1)
        self.jun_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_9.sizePolicy().hasHeightForWidth())
        self.jun_9.setSizePolicy(sizePolicy)
        self.jun_9.setAutoFillBackground(True)
        self.jun_9.setReadOnly(True)
        self.jun_9.setObjectName("jun_9")
        self.gridLayout_2.addWidget(self.jun_9, 9, 6, 1, 1)
        self.jul_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_9.sizePolicy().hasHeightForWidth())
        self.jul_9.setSizePolicy(sizePolicy)
        self.jul_9.setAutoFillBackground(True)
        self.jul_9.setReadOnly(True)
        self.jul_9.setObjectName("jul_9")
        self.gridLayout_2.addWidget(self.jul_9, 9, 7, 1, 1)
        self.aug_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_9.sizePolicy().hasHeightForWidth())
        self.aug_9.setSizePolicy(sizePolicy)
        self.aug_9.setAutoFillBackground(True)
        self.aug_9.setReadOnly(True)
        self.aug_9.setObjectName("aug_9")
        self.gridLayout_2.addWidget(self.aug_9, 9, 8, 1, 1)
        self.sep_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_9.sizePolicy().hasHeightForWidth())
        self.sep_9.setSizePolicy(sizePolicy)
        self.sep_9.setAutoFillBackground(True)
        self.sep_9.setReadOnly(True)
        self.sep_9.setObjectName("sep_9")
        self.gridLayout_2.addWidget(self.sep_9, 9, 9, 1, 1)
        self.oct_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_9.sizePolicy().hasHeightForWidth())
        self.oct_9.setSizePolicy(sizePolicy)
        self.oct_9.setAutoFillBackground(True)
        self.oct_9.setReadOnly(True)
        self.oct_9.setObjectName("oct_9")
        self.gridLayout_2.addWidget(self.oct_9, 9, 10, 1, 1)
        self.nov_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_9.sizePolicy().hasHeightForWidth())
        self.nov_9.setSizePolicy(sizePolicy)
        self.nov_9.setAutoFillBackground(True)
        self.nov_9.setReadOnly(True)
        self.nov_9.setObjectName("nov_9")
        self.gridLayout_2.addWidget(self.nov_9, 9, 11, 1, 1)
        self.dec_9 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_9.sizePolicy().hasHeightForWidth())
        self.dec_9.setSizePolicy(sizePolicy)
        self.dec_9.setAutoFillBackground(True)
        self.dec_9.setReadOnly(True)
        self.dec_9.setObjectName("dec_9")
        self.gridLayout_2.addWidget(self.dec_9, 9, 12, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setAutoFillBackground(True)
        self.label_59.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_59.setObjectName("label_59")
        self.gridLayout_2.addWidget(self.label_59, 9, 0, 1, 1)
        self.jan_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_10.sizePolicy().hasHeightForWidth())
        self.jan_10.setSizePolicy(sizePolicy)
        self.jan_10.setAutoFillBackground(True)
        self.jan_10.setReadOnly(True)
        self.jan_10.setObjectName("jan_10")
        self.gridLayout_2.addWidget(self.jan_10, 10, 1, 1, 1)
        self.feb_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_10.sizePolicy().hasHeightForWidth())
        self.feb_10.setSizePolicy(sizePolicy)
        self.feb_10.setAutoFillBackground(True)
        self.feb_10.setReadOnly(True)
        self.feb_10.setObjectName("feb_10")
        self.gridLayout_2.addWidget(self.feb_10, 10, 2, 1, 1)
        self.mar_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_10.sizePolicy().hasHeightForWidth())
        self.mar_10.setSizePolicy(sizePolicy)
        self.mar_10.setAutoFillBackground(True)
        self.mar_10.setReadOnly(True)
        self.mar_10.setObjectName("mar_10")
        self.gridLayout_2.addWidget(self.mar_10, 10, 3, 1, 1)
        self.apr_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_10.sizePolicy().hasHeightForWidth())
        self.apr_10.setSizePolicy(sizePolicy)
        self.apr_10.setAutoFillBackground(True)
        self.apr_10.setReadOnly(True)
        self.apr_10.setObjectName("apr_10")
        self.gridLayout_2.addWidget(self.apr_10, 10, 4, 1, 1)
        self.may_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_10.sizePolicy().hasHeightForWidth())
        self.may_10.setSizePolicy(sizePolicy)
        self.may_10.setAutoFillBackground(True)
        self.may_10.setReadOnly(True)
        self.may_10.setObjectName("may_10")
        self.gridLayout_2.addWidget(self.may_10, 10, 5, 1, 1)
        self.jun_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_10.sizePolicy().hasHeightForWidth())
        self.jun_10.setSizePolicy(sizePolicy)
        self.jun_10.setAutoFillBackground(True)
        self.jun_10.setReadOnly(True)
        self.jun_10.setObjectName("jun_10")
        self.gridLayout_2.addWidget(self.jun_10, 10, 6, 1, 1)
        self.jul_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_10.sizePolicy().hasHeightForWidth())
        self.jul_10.setSizePolicy(sizePolicy)
        self.jul_10.setAutoFillBackground(True)
        self.jul_10.setReadOnly(True)
        self.jul_10.setObjectName("jul_10")
        self.gridLayout_2.addWidget(self.jul_10, 10, 7, 1, 1)
        self.aug_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_10.sizePolicy().hasHeightForWidth())
        self.aug_10.setSizePolicy(sizePolicy)
        self.aug_10.setAutoFillBackground(True)
        self.aug_10.setReadOnly(True)
        self.aug_10.setObjectName("aug_10")
        self.gridLayout_2.addWidget(self.aug_10, 10, 8, 1, 1)
        self.sep_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_10.sizePolicy().hasHeightForWidth())
        self.sep_10.setSizePolicy(sizePolicy)
        self.sep_10.setAutoFillBackground(True)
        self.sep_10.setReadOnly(True)
        self.sep_10.setObjectName("sep_10")
        self.gridLayout_2.addWidget(self.sep_10, 10, 9, 1, 1)
        self.oct_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_10.sizePolicy().hasHeightForWidth())
        self.oct_10.setSizePolicy(sizePolicy)
        self.oct_10.setAutoFillBackground(True)
        self.oct_10.setReadOnly(True)
        self.oct_10.setObjectName("oct_10")
        self.gridLayout_2.addWidget(self.oct_10, 10, 10, 1, 1)
        self.nov_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_10.sizePolicy().hasHeightForWidth())
        self.nov_10.setSizePolicy(sizePolicy)
        self.nov_10.setAutoFillBackground(True)
        self.nov_10.setReadOnly(True)
        self.nov_10.setObjectName("nov_10")
        self.gridLayout_2.addWidget(self.nov_10, 10, 11, 1, 1)
        self.dec_10 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_10.sizePolicy().hasHeightForWidth())
        self.dec_10.setSizePolicy(sizePolicy)
        self.dec_10.setAutoFillBackground(True)
        self.dec_10.setReadOnly(True)
        self.dec_10.setObjectName("dec_10")
        self.gridLayout_2.addWidget(self.dec_10, 10, 12, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setAutoFillBackground(True)
        self.label_61.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_61.setObjectName("label_61")
        self.gridLayout_2.addWidget(self.label_61, 10, 0, 1, 1)
        self.jan_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_11.sizePolicy().hasHeightForWidth())
        self.jan_11.setSizePolicy(sizePolicy)
        self.jan_11.setAutoFillBackground(True)
        self.jan_11.setReadOnly(True)
        self.jan_11.setObjectName("jan_11")
        self.gridLayout_2.addWidget(self.jan_11, 11, 1, 1, 1)
        self.feb_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_11.sizePolicy().hasHeightForWidth())
        self.feb_11.setSizePolicy(sizePolicy)
        self.feb_11.setAutoFillBackground(True)
        self.feb_11.setReadOnly(True)
        self.feb_11.setObjectName("feb_11")
        self.gridLayout_2.addWidget(self.feb_11, 11, 2, 1, 1)
        self.mar_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_11.sizePolicy().hasHeightForWidth())
        self.mar_11.setSizePolicy(sizePolicy)
        self.mar_11.setAutoFillBackground(True)
        self.mar_11.setReadOnly(True)
        self.mar_11.setObjectName("mar_11")
        self.gridLayout_2.addWidget(self.mar_11, 11, 3, 1, 1)
        self.apr_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_11.sizePolicy().hasHeightForWidth())
        self.apr_11.setSizePolicy(sizePolicy)
        self.apr_11.setAutoFillBackground(True)
        self.apr_11.setReadOnly(True)
        self.apr_11.setObjectName("apr_11")
        self.gridLayout_2.addWidget(self.apr_11, 11, 4, 1, 1)
        self.may_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_11.sizePolicy().hasHeightForWidth())
        self.may_11.setSizePolicy(sizePolicy)
        self.may_11.setAutoFillBackground(True)
        self.may_11.setReadOnly(True)
        self.may_11.setObjectName("may_11")
        self.gridLayout_2.addWidget(self.may_11, 11, 5, 1, 1)
        self.jun_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_11.sizePolicy().hasHeightForWidth())
        self.jun_11.setSizePolicy(sizePolicy)
        self.jun_11.setAutoFillBackground(True)
        self.jun_11.setReadOnly(True)
        self.jun_11.setObjectName("jun_11")
        self.gridLayout_2.addWidget(self.jun_11, 11, 6, 1, 1)
        self.jul_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_11.sizePolicy().hasHeightForWidth())
        self.jul_11.setSizePolicy(sizePolicy)
        self.jul_11.setAutoFillBackground(True)
        self.jul_11.setReadOnly(True)
        self.jul_11.setObjectName("jul_11")
        self.gridLayout_2.addWidget(self.jul_11, 11, 7, 1, 1)
        self.aug_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_11.sizePolicy().hasHeightForWidth())
        self.aug_11.setSizePolicy(sizePolicy)
        self.aug_11.setAutoFillBackground(True)
        self.aug_11.setReadOnly(True)
        self.aug_11.setObjectName("aug_11")
        self.gridLayout_2.addWidget(self.aug_11, 11, 8, 1, 1)
        self.sep_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_11.sizePolicy().hasHeightForWidth())
        self.sep_11.setSizePolicy(sizePolicy)
        self.sep_11.setAutoFillBackground(True)
        self.sep_11.setReadOnly(True)
        self.sep_11.setObjectName("sep_11")
        self.gridLayout_2.addWidget(self.sep_11, 11, 9, 1, 1)
        self.oct_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_11.sizePolicy().hasHeightForWidth())
        self.oct_11.setSizePolicy(sizePolicy)
        self.oct_11.setAutoFillBackground(True)
        self.oct_11.setReadOnly(True)
        self.oct_11.setObjectName("oct_11")
        self.gridLayout_2.addWidget(self.oct_11, 11, 10, 1, 1)
        self.nov_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_11.sizePolicy().hasHeightForWidth())
        self.nov_11.setSizePolicy(sizePolicy)
        self.nov_11.setAutoFillBackground(True)
        self.nov_11.setReadOnly(True)
        self.nov_11.setObjectName("nov_11")
        self.gridLayout_2.addWidget(self.nov_11, 11, 11, 1, 1)
        self.dec_11 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_11.sizePolicy().hasHeightForWidth())
        self.dec_11.setSizePolicy(sizePolicy)
        self.dec_11.setAutoFillBackground(True)
        self.dec_11.setReadOnly(True)
        self.dec_11.setObjectName("dec_11")
        self.gridLayout_2.addWidget(self.dec_11, 11, 12, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setAutoFillBackground(True)
        self.label_58.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_58.setObjectName("label_58")
        self.gridLayout_2.addWidget(self.label_58, 11, 0, 1, 1)
        self.jan_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_12.sizePolicy().hasHeightForWidth())
        self.jan_12.setSizePolicy(sizePolicy)
        self.jan_12.setAutoFillBackground(True)
        self.jan_12.setReadOnly(True)
        self.jan_12.setObjectName("jan_12")
        self.gridLayout_2.addWidget(self.jan_12, 12, 1, 1, 1)
        self.feb_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_12.sizePolicy().hasHeightForWidth())
        self.feb_12.setSizePolicy(sizePolicy)
        self.feb_12.setAutoFillBackground(True)
        self.feb_12.setReadOnly(True)
        self.feb_12.setObjectName("feb_12")
        self.gridLayout_2.addWidget(self.feb_12, 12, 2, 1, 1)
        self.mar_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_12.sizePolicy().hasHeightForWidth())
        self.mar_12.setSizePolicy(sizePolicy)
        self.mar_12.setAutoFillBackground(True)
        self.mar_12.setReadOnly(True)
        self.mar_12.setObjectName("mar_12")
        self.gridLayout_2.addWidget(self.mar_12, 12, 3, 1, 1)
        self.apr_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_12.sizePolicy().hasHeightForWidth())
        self.apr_12.setSizePolicy(sizePolicy)
        self.apr_12.setAutoFillBackground(True)
        self.apr_12.setReadOnly(True)
        self.apr_12.setObjectName("apr_12")
        self.gridLayout_2.addWidget(self.apr_12, 12, 4, 1, 1)
        self.may_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_12.sizePolicy().hasHeightForWidth())
        self.may_12.setSizePolicy(sizePolicy)
        self.may_12.setAutoFillBackground(True)
        self.may_12.setReadOnly(True)
        self.may_12.setObjectName("may_12")
        self.gridLayout_2.addWidget(self.may_12, 12, 5, 1, 1)
        self.jun_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_12.sizePolicy().hasHeightForWidth())
        self.jun_12.setSizePolicy(sizePolicy)
        self.jun_12.setAutoFillBackground(True)
        self.jun_12.setReadOnly(True)
        self.jun_12.setObjectName("jun_12")
        self.gridLayout_2.addWidget(self.jun_12, 12, 6, 1, 1)
        self.jul_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_12.sizePolicy().hasHeightForWidth())
        self.jul_12.setSizePolicy(sizePolicy)
        self.jul_12.setAutoFillBackground(True)
        self.jul_12.setReadOnly(True)
        self.jul_12.setObjectName("jul_12")
        self.gridLayout_2.addWidget(self.jul_12, 12, 7, 1, 1)
        self.aug_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_12.sizePolicy().hasHeightForWidth())
        self.aug_12.setSizePolicy(sizePolicy)
        self.aug_12.setAutoFillBackground(True)
        self.aug_12.setReadOnly(True)
        self.aug_12.setObjectName("aug_12")
        self.gridLayout_2.addWidget(self.aug_12, 12, 8, 1, 1)
        self.sep_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_12.sizePolicy().hasHeightForWidth())
        self.sep_12.setSizePolicy(sizePolicy)
        self.sep_12.setAutoFillBackground(True)
        self.sep_12.setReadOnly(True)
        self.sep_12.setObjectName("sep_12")
        self.gridLayout_2.addWidget(self.sep_12, 12, 9, 1, 1)
        self.oct_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_12.sizePolicy().hasHeightForWidth())
        self.oct_12.setSizePolicy(sizePolicy)
        self.oct_12.setAutoFillBackground(True)
        self.oct_12.setReadOnly(True)
        self.oct_12.setObjectName("oct_12")
        self.gridLayout_2.addWidget(self.oct_12, 12, 10, 1, 1)
        self.nov_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_12.sizePolicy().hasHeightForWidth())
        self.nov_12.setSizePolicy(sizePolicy)
        self.nov_12.setAutoFillBackground(True)
        self.nov_12.setReadOnly(True)
        self.nov_12.setObjectName("nov_12")
        self.gridLayout_2.addWidget(self.nov_12, 12, 11, 1, 1)
        self.dec_12 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_12.sizePolicy().hasHeightForWidth())
        self.dec_12.setSizePolicy(sizePolicy)
        self.dec_12.setAutoFillBackground(True)
        self.dec_12.setReadOnly(True)
        self.dec_12.setObjectName("dec_12")
        self.gridLayout_2.addWidget(self.dec_12, 12, 12, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_60.setFont(font)
        self.label_60.setAutoFillBackground(True)
        self.label_60.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_60.setObjectName("label_60")
        self.gridLayout_2.addWidget(self.label_60, 12, 0, 1, 1)

        self.jan_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jan_13.sizePolicy().hasHeightForWidth())
        self.jan_13.setSizePolicy(sizePolicy)
        self.jan_13.setAutoFillBackground(True)
        self.jan_13.setReadOnly(True)
        self.jan_13.setObjectName("jan_13")
        self.gridLayout_2.addWidget(self.jan_13, 13, 1, 1, 1)
        self.feb_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feb_13.sizePolicy().hasHeightForWidth())
        self.feb_13.setSizePolicy(sizePolicy)
        self.feb_13.setAutoFillBackground(True)
        self.feb_13.setReadOnly(True)
        self.feb_13.setObjectName("feb_13")
        self.gridLayout_2.addWidget(self.feb_13, 13, 2, 1, 1)
        self.mar_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mar_13.sizePolicy().hasHeightForWidth())
        self.mar_13.setSizePolicy(sizePolicy)
        self.mar_13.setAutoFillBackground(True)
        self.mar_13.setReadOnly(True)
        self.mar_13.setObjectName("mar_13")
        self.gridLayout_2.addWidget(self.mar_13, 13, 3, 1, 1)
        self.apr_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apr_13.sizePolicy().hasHeightForWidth())
        self.apr_13.setSizePolicy(sizePolicy)
        self.apr_13.setAutoFillBackground(True)
        self.apr_13.setReadOnly(True)
        self.apr_13.setObjectName("apr_13")
        self.gridLayout_2.addWidget(self.apr_13, 13, 4, 1, 1)
        self.may_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.may_13.sizePolicy().hasHeightForWidth())
        self.may_13.setSizePolicy(sizePolicy)
        self.may_13.setAutoFillBackground(True)
        self.may_13.setReadOnly(True)
        self.may_13.setObjectName("may_13")
        self.gridLayout_2.addWidget(self.may_13, 13, 5, 1, 1)
        self.jun_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jun_13.sizePolicy().hasHeightForWidth())
        self.jun_13.setSizePolicy(sizePolicy)
        self.jun_13.setAutoFillBackground(True)
        self.jun_13.setReadOnly(True)
        self.jun_13.setObjectName("jun_13")
        self.gridLayout_2.addWidget(self.jun_13, 13, 6, 1, 1)
        self.jul_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jul_13.sizePolicy().hasHeightForWidth())
        self.jul_13.setSizePolicy(sizePolicy)
        self.jul_13.setAutoFillBackground(True)
        self.jul_13.setReadOnly(True)
        self.jul_13.setObjectName("jul_13")
        self.gridLayout_2.addWidget(self.jul_13, 13, 7, 1, 1)
        self.aug_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aug_13.sizePolicy().hasHeightForWidth())
        self.aug_13.setSizePolicy(sizePolicy)
        self.aug_13.setAutoFillBackground(True)
        self.aug_13.setReadOnly(True)
        self.aug_13.setObjectName("aug_13")
        self.gridLayout_2.addWidget(self.aug_13, 13, 8, 1, 1)
        self.sep_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sep_13.sizePolicy().hasHeightForWidth())
        self.sep_13.setSizePolicy(sizePolicy)
        self.sep_13.setAutoFillBackground(True)
        self.sep_13.setReadOnly(True)
        self.sep_13.setObjectName("sep_13")
        self.gridLayout_2.addWidget(self.sep_13, 13, 9, 1, 1)
        self.oct_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oct_13.sizePolicy().hasHeightForWidth())
        self.oct_13.setSizePolicy(sizePolicy)
        self.oct_13.setAutoFillBackground(True)
        self.oct_13.setReadOnly(True)
        self.oct_13.setObjectName("oct_13")
        self.gridLayout_2.addWidget(self.oct_13, 13, 10, 1, 1)
        self.nov_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nov_13.sizePolicy().hasHeightForWidth())
        self.nov_13.setSizePolicy(sizePolicy)
        self.nov_13.setAutoFillBackground(True)
        self.nov_13.setReadOnly(True)
        self.nov_13.setObjectName("nov_13")
        self.gridLayout_2.addWidget(self.nov_13, 13, 11, 1, 1)
        self.dec_13 = QtWidgets.QLineEdit(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dec_12.sizePolicy().hasHeightForWidth())
        self.dec_13.setSizePolicy(sizePolicy)
        self.dec_13.setAutoFillBackground(True)
        self.dec_13.setReadOnly(True)
        self.dec_13.setObjectName("dec_13")
        self.gridLayout_2.addWidget(self.dec_13, 13, 12, 1, 1)
        self.label_t = QtWidgets.QLabel(self.WFS_tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t.sizePolicy().hasHeightForWidth())
        self.label_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_t.setFont(font)
        self.label_t.setAutoFillBackground(True)
        self.label_t.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_t.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_t.setObjectName("label_t")
        self.gridLayout_2.addWidget(self.label_t, 13, 0, 1, 1)

        self.horizontalLayout_19.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 2, 0, 1, 1)
        self.line_below = QtWidgets.QFrame(self.WFS_tab1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line_below.setFont(font)
        self.line_below.setLineWidth(4)
        self.line_below.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_below.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_below.setObjectName("line_below")
        self.gridLayout_3.addWidget(self.line_below, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.WFS_tab1)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Weather_sum = QtWidgets.QLabel(self.WFS_tab1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum.setFont(font)
        self.Weather_sum.setObjectName("Weather_sum")
        self.horizontalLayout.addWidget(self.Weather_sum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Location = QtWidgets.QLabel(self.WFS_tab1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location.setFont(font)
        self.Location.setObjectName("Location")
        self.verticalLayout_2.addWidget(self.Location)
        self.Lat_Log = QtWidgets.QLabel(self.WFS_tab1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log.setFont(font)
        self.Lat_Log.setObjectName("Lat_Log")
        self.verticalLayout_2.addWidget(self.Lat_Log)
        self.Ele_TZ = QtWidgets.QLabel(self.WFS_tab1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ.setFont(font)
        self.Ele_TZ.setObjectName("Ele_TZ")
        self.verticalLayout_2.addWidget(self.Ele_TZ)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.location = QtWidgets.QLineEdit(self.WFS_tab1)
        self.location.setAutoFillBackground(True)
        self.location.setFrame(False)
        self.location.setReadOnly(True)
        self.location.setObjectName("location")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location.setFont(font)
        self.verticalLayout.addWidget(self.location)
        self.lat_lon = QtWidgets.QLineEdit(self.WFS_tab1)
        self.lat_lon.setAutoFillBackground(True)
        self.lat_lon.setFrame(False)
        self.lat_lon.setReadOnly(True)
        self.lat_lon.setObjectName("lat_lon")
        self.verticalLayout.addWidget(self.lat_lon)
        self.ele_tz = QtWidgets.QLineEdit(self.WFS_tab1)
        self.ele_tz.setAutoFillBackground(True)
        self.ele_tz.setFrame(False)
        self.ele_tz.setReadOnly(True)
        self.ele_tz.setObjectName("ele_tz")
        self.verticalLayout.addWidget(self.ele_tz)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_butt = QtWidgets.QPushButton(self.WFS_tab1)
        self.back_butt.setObjectName("back_butt")
        self.back_butt.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "color: #000066;\n"
                                        "background-color: #CCCCFF;\n"
                                        "border: 5px solid transparent;\n"
                                        "font-size: 15px;\n"
                                        "border-radius: 5px;\n"
                                        "\n"
                                        "}\n"
                                     "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: #6666FF;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #39FF11);\n"
                                        "}\n"
                                        "")
        self.horizontalLayout_2.addWidget(self.back_butt)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.WFS_tab.addTab(self.WFS_tab1, "")
        self.temp_tab = QtWidgets.QWidget()
        self.temp_tab.setObjectName("temp_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.temp_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Weather_sum_2 = QtWidgets.QLabel(self.temp_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_2.setFont(font)
        self.Weather_sum_2.setObjectName("Weather_sum_2")
        self.horizontalLayout_3.addWidget(self.Weather_sum_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Location_2 = QtWidgets.QLabel(self.temp_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_2.setFont(font)
        self.Location_2.setObjectName("Location_2")
        self.verticalLayout_6.addWidget(self.Location_2)
        self.Lat_Log_2 = QtWidgets.QLabel(self.temp_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_2.setFont(font)
        self.Lat_Log_2.setObjectName("Lat_Log_2")
        self.verticalLayout_6.addWidget(self.Lat_Log_2)
        self.Ele_TZ_2 = QtWidgets.QLabel(self.temp_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_2.setFont(font)
        self.Ele_TZ_2.setObjectName("Ele_TZ_2")
        self.verticalLayout_6.addWidget(self.Ele_TZ_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.location_2 = QtWidgets.QLineEdit(self.temp_tab)
        self.location_2.setAutoFillBackground(True)
        self.location_2.setFrame(False)
        self.location_2.setReadOnly(True)
        self.location_2.setObjectName("location_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_2.setFont(font)
        self.verticalLayout_7.addWidget(self.location_2)
        self.lat_lon_2 = QtWidgets.QLineEdit(self.temp_tab)
        self.lat_lon_2.setAutoFillBackground(True)
        self.lat_lon_2.setFrame(False)
        self.lat_lon_2.setReadOnly(True)
        self.lat_lon_2.setObjectName("lat_lon_2")
        self.verticalLayout_7.addWidget(self.lat_lon_2)
        self.ele_tz_2 = QtWidgets.QLineEdit(self.temp_tab)
        self.ele_tz_2.setAutoFillBackground(True)
        self.ele_tz_2.setFrame(False)
        self.ele_tz_2.setReadOnly(True)
        self.ele_tz_2.setObjectName("ele_tz_2")
        self.verticalLayout_7.addWidget(self.ele_tz_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.temp_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.temp_tab)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_8.addWidget(self.line_3)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.legend_violen_path = self.resource_path("legend_violen_3.png")
        pixmap = QPixmap(self.legend_violen_path)
        self.label_12.setPixmap(pixmap)
        self.verticalLayout_8.addWidget(self.label_12)
        #spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.verticalLayout_8.addItem(spacerItem)
        self.label_radio_select_temp = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_radio_select_temp.setFont(font)
        self.label_radio_select_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_radio_select_temp.setObjectName("label_radio_select_temp")
        self.label_radio_select_temp.setText("Select\nTemperature")
        self.verticalLayout_8.addWidget(self.label_radio_select_temp)
        self.radiobut_1 = QtWidgets.QRadioButton("DBT")
        self.radiobut_1.setChecked(True)
        self.radiobut_1.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_8.addWidget(self.radiobut_1)
        self.radiobut_2 = QtWidgets.QRadioButton("WBT")
        self.radiobut_2.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_8.addWidget(self.radiobut_2)
        self.radiobut_3 = QtWidgets.QRadioButton("DPT")
        self.radiobut_3.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_8.addWidget(self.radiobut_3)

        self.label_design_cond_temp = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_design_cond_temp.setFont(font)
        self.label_design_cond_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_design_cond_temp.setObjectName("label_design_cond_temp")
        self.label_design_cond_temp.setText("Design Conditions\n(Cooling DB)")
        self.verticalLayout_8.addWidget(self.label_design_cond_temp)

        self.label_design_cond_val_temp_1 = QtWidgets.QLabel(self.widget_2)
        self.label_design_cond_val_temp_1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_design_cond_val_temp_1.setObjectName("label_design_cond_val_temp_1")
        self.label_design_cond_val_temp_1.setText("0.4% =")
        self.verticalLayout_8.addWidget(self.label_design_cond_val_temp_1)
        self.label_design_cond_val_temp_2 = QtWidgets.QLabel(self.widget_2)
        self.label_design_cond_val_temp_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_design_cond_val_temp_2.setObjectName("label_design_cond_val_temp_2")
        self.label_design_cond_val_temp_2.setText("1% =")
        self.verticalLayout_8.addWidget(self.label_design_cond_val_temp_2)
        self.label_design_cond_val_temp_3 = QtWidgets.QLabel(self.widget_2)
        self.label_design_cond_val_temp_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_design_cond_val_temp_3.setObjectName("label_design_cond_val_temp_3")
        self.label_design_cond_val_temp_3.setText("2% =")
        self.verticalLayout_8.addWidget(self.label_design_cond_val_temp_3)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_6.addWidget(self.line_5, 0, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.widget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_6.addWidget(self.line_6, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout_4.addWidget(self.canvas_1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.temp_tab, "")
        self.rad_tab = QtWidgets.QWidget()
        self.rad_tab.setObjectName("rad_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.rad_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Weather_sum_3 = QtWidgets.QLabel(self.rad_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_3.setFont(font)
        self.Weather_sum_3.setObjectName("Weather_sum_3")
        self.horizontalLayout_5.addWidget(self.Weather_sum_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Location_3 = QtWidgets.QLabel(self.rad_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_3.setFont(font)
        self.Location_3.setObjectName("Location_3")
        self.verticalLayout_10.addWidget(self.Location_3)
        self.Lat_Log_3 = QtWidgets.QLabel(self.rad_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_3.setFont(font)
        self.Lat_Log_3.setObjectName("Lat_Log_3")
        self.verticalLayout_10.addWidget(self.Lat_Log_3)
        self.Ele_TZ_3 = QtWidgets.QLabel(self.rad_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_3.setFont(font)
        self.Ele_TZ_3.setObjectName("Ele_TZ_3")
        self.verticalLayout_10.addWidget(self.Ele_TZ_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.location_3 = QtWidgets.QLineEdit(self.rad_tab)
        self.location_3.setAutoFillBackground(True)
        self.location_3.setFrame(False)
        self.location_3.setReadOnly(True)
        self.location_3.setObjectName("location_3")
        self.verticalLayout_11.addWidget(self.location_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_3.setFont(font)
        self.lat_lon_3 = QtWidgets.QLineEdit(self.rad_tab)
        self.lat_lon_3.setAutoFillBackground(True)
        self.lat_lon_3.setFrame(False)
        self.lat_lon_3.setReadOnly(True)
        self.lat_lon_3.setObjectName("lat_lon_3")
        self.verticalLayout_11.addWidget(self.lat_lon_3)
        self.ele_tz_3 = QtWidgets.QLineEdit(self.rad_tab)
        self.ele_tz_3.setAutoFillBackground(True)
        self.ele_tz_3.setFrame(False)
        self.ele_tz_3.setReadOnly(True)
        self.ele_tz_3.setObjectName("ele_tz_3")
        self.verticalLayout_11.addWidget(self.ele_tz_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.line_7 = QtWidgets.QFrame(self.rad_tab)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_9.addWidget(self.line_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget = QtWidgets.QWidget(self.rad_tab)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.line_8 = QtWidgets.QFrame(self.widget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_12.addWidget(self.line_8)
        self.label_19 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_12.addWidget(self.label_19)
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        pixmap = QPixmap(self.legend_violen_path)
        self.label_13.setPixmap(pixmap)
        self.verticalLayout_12.addWidget(self.label_13)
        self.label_radio_select_radia = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_radio_select_radia.setFont(font)
        self.label_radio_select_radia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_radio_select_radia.setObjectName("label_radio_select_radia")
        self.label_radio_select_radia.setText("Select\nRadiation")
        self.verticalLayout_12.addWidget(self.label_radio_select_radia)
        self.radiobut_4 = QtWidgets.QRadioButton("GHR")
        self.radiobut_4.setObjectName("radiobut_4")
        self.radiobut_4.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_12.addWidget(self.radiobut_4)
        self.radiobut_5 = QtWidgets.QRadioButton("DNR")
        self.radiobut_5.setObjectName("radiobut_5")
        self.radiobut_5.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_12.addWidget(self.radiobut_5)
        self.radiobut_6 = QtWidgets.QRadioButton("DR")
        self.radiobut_6.setObjectName("radiobut_6")
        self.radiobut_4.setChecked(True)
        self.radiobut_6.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_12.addWidget(self.radiobut_6)

        self.label_annual_avg_radia = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_annual_avg_radia.setFont(font)
        self.label_annual_avg_radia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_avg_radia.setObjectName("label_annual_avg_radia")
        self.label_annual_avg_radia.setText("Annual Average")
        self.verticalLayout_12.addWidget(self.label_annual_avg_radia)
        self.label_annual_avg_radia_val_1 = QtWidgets.QLabel(self.widget_2)
        self.label_annual_avg_radia_val_1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_annual_avg_radia_val_1.setObjectName("label_annual_avg_radia_val_1")
        self.label_annual_avg_radia_val_1.setText("GHR = ")
        self.verticalLayout_12.addWidget(self.label_annual_avg_radia_val_1)
        self.label_annual_avg_radia_val_2 = QtWidgets.QLabel(self.widget_2)
        self.label_annual_avg_radia_val_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_annual_avg_radia_val_2.setObjectName("label_annual_avg_radia_val_2")
        self.label_annual_avg_radia_val_2.setText("DNR = ")
        self.verticalLayout_12.addWidget(self.label_annual_avg_radia_val_2)
        self.label_annual_avg_radia_val_3 = QtWidgets.QLabel(self.widget_2)
        self.label_annual_avg_radia_val_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_annual_avg_radia_val_3.setObjectName("label_annual_avg_radia_val_3")
        self.label_annual_avg_radia_val_3.setText("DR = ")
        self.verticalLayout_12.addWidget(self.label_annual_avg_radia_val_3)
        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_12.addWidget(self.line_9)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_5.addWidget(self.line_10, 0, 2, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.widget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_5.addWidget(self.line_11, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.widget)
        self.horizontalLayout_6.addWidget(self.canvas_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.rad_tab, "")
        self.illumi_tab = QtWidgets.QWidget()
        self.illumi_tab.setObjectName("illumi_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.illumi_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Weather_sum_4 = QtWidgets.QLabel(self.illumi_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_4.setFont(font)
        self.Weather_sum_4.setObjectName("Weather_sum_4")
        self.horizontalLayout_7.addWidget(self.Weather_sum_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Location_4 = QtWidgets.QLabel(self.illumi_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_4.setFont(font)
        self.Location_4.setObjectName("Location_4")
        self.verticalLayout_14.addWidget(self.Location_4)
        self.Lat_Log_4 = QtWidgets.QLabel(self.illumi_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_4.setFont(font)
        self.Lat_Log_4.setObjectName("Lat_Log_4")
        self.verticalLayout_14.addWidget(self.Lat_Log_4)
        self.Ele_TZ_4 = QtWidgets.QLabel(self.illumi_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_4.setFont(font)
        self.Ele_TZ_4.setObjectName("Ele_TZ_4")
        self.verticalLayout_14.addWidget(self.Ele_TZ_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.location_4 = QtWidgets.QLineEdit(self.illumi_tab)
        self.location_4.setAutoFillBackground(True)
        self.location_4.setFrame(False)
        self.location_4.setReadOnly(True)
        self.location_4.setObjectName("location_4")
        self.verticalLayout_15.addWidget(self.location_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_4.setFont(font)
        self.lat_lon_4 = QtWidgets.QLineEdit(self.illumi_tab)
        self.lat_lon_4.setAutoFillBackground(True)
        self.lat_lon_4.setFrame(False)
        self.lat_lon_4.setReadOnly(True)
        self.lat_lon_4.setObjectName("lat_lon_4")
        self.verticalLayout_15.addWidget(self.lat_lon_4)
        self.ele_tz_4 = QtWidgets.QLineEdit(self.illumi_tab)
        self.ele_tz_4.setAutoFillBackground(True)
        self.ele_tz_4.setFrame(False)
        self.ele_tz_4.setReadOnly(True)
        self.ele_tz_4.setObjectName("ele_tz_4")
        self.verticalLayout_15.addWidget(self.ele_tz_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_15)
        self.verticalLayout_13.addLayout(self.horizontalLayout_7)
        self.line_12 = QtWidgets.QFrame(self.illumi_tab)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_13.addWidget(self.line_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_3 = QtWidgets.QWidget(self.illumi_tab)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.line_13 = QtWidgets.QFrame(self.widget_3)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_16.addWidget(self.line_13)
        self.label_25 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_16.addWidget(self.label_25)
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        pixmap = QPixmap(self.legend_violen_path)
        self.label_14.setPixmap(pixmap)
        self.verticalLayout_16.addWidget(self.label_14)
        self.label_radio_select_illumi = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_radio_select_illumi.setFont(font)
        self.label_radio_select_illumi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_radio_select_illumi.setObjectName("label_radio_select_illumi")
        self.label_radio_select_illumi.setText("Select\nIllumination")
        self.verticalLayout_16.addWidget(self.label_radio_select_illumi)
        self.radiobut_7 = QtWidgets.QRadioButton("DNI")
        self.verticalLayout_16.addWidget(self.radiobut_7)
        self.radiobut_7.setChecked(True)
        self.radiobut_7.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.radiobut_8 = QtWidgets.QRadioButton("GHI")
        self.radiobut_8.setStyleSheet(
                                    "QRadioButton::indicator::checked\n"
                                        "{\n"
                                        "background: #0080FF;\n"
                                        "color: #001933;\n"
                                        "}\n"
                                      "QRadioButton\n"
                                      "{\n"
                                      "background: #CCe5FF;\n"
                                      "color: #001933;\n"
                                      "}\n")
        self.verticalLayout_16.addWidget(self.radiobut_8)
        self.label_annual_avg_illumi = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_annual_avg_illumi.setFont(font)
        self.label_annual_avg_illumi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_avg_illumi.setObjectName("label_annual_avg_illumi")
        self.label_annual_avg_illumi.setText("Annual Average")
        self.verticalLayout_16.addWidget(self.label_annual_avg_illumi)
        self.label_annual_avg_illumi_val_1 = QtWidgets.QLabel(self.widget_2)
        self.label_annual_avg_illumi_val_1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_annual_avg_illumi_val_1.setObjectName("label_annual_avg_illumi_val_1")
        self.label_annual_avg_illumi_val_1.setText("DNI = ")
        self.verticalLayout_16.addWidget(self.label_annual_avg_illumi_val_1)
        self.label_annual_avg_illumi_val_2 = QtWidgets.QLabel(self.widget_2)
        self.label_annual_avg_illumi_val_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_annual_avg_illumi_val_2.setObjectName("label_annual_avg_illumi_val_2")
        self.label_annual_avg_illumi_val_2.setText("GHI = ")
        self.verticalLayout_16.addWidget(self.label_annual_avg_illumi_val_2)
        self.line_14 = QtWidgets.QFrame(self.widget_3)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_16.addWidget(self.line_14)
        self.gridLayout_9.addLayout(self.verticalLayout_16, 0, 1, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.widget_3)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_9.addWidget(self.line_15, 0, 2, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.widget_3)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_9.addWidget(self.line_16, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.widget_3)
        self.horizontalLayout_8.addWidget(self.canvas_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.gridLayout_10.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.illumi_tab, "")
        self.win_tab = QtWidgets.QWidget()
        self.win_tab.setObjectName("win_tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.win_tab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Weather_sum_5 = QtWidgets.QLabel(self.win_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_5.setFont(font)
        self.Weather_sum_5.setObjectName("Weather_sum_5")
        self.horizontalLayout_9.addWidget(self.Weather_sum_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Location_5 = QtWidgets.QLabel(self.win_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_5.setFont(font)
        self.Location_5.setObjectName("Location_5")
        self.verticalLayout_18.addWidget(self.Location_5)
        self.Lat_Log_5 = QtWidgets.QLabel(self.win_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_5.setFont(font)
        self.Lat_Log_5.setObjectName("Lat_Log_5")
        self.verticalLayout_18.addWidget(self.Lat_Log_5)
        self.Ele_TZ_5 = QtWidgets.QLabel(self.win_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_5.setFont(font)
        self.Ele_TZ_5.setObjectName("Ele_TZ_5")
        self.verticalLayout_18.addWidget(self.Ele_TZ_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.location_5 = QtWidgets.QLineEdit(self.win_tab)
        self.location_5.setAutoFillBackground(True)
        self.location_5.setFrame(False)
        self.location_5.setReadOnly(True)
        self.location_5.setObjectName("location_5")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_5.setFont(font)
        self.verticalLayout_19.addWidget(self.location_5)
        self.lat_lon_5 = QtWidgets.QLineEdit(self.win_tab)
        self.lat_lon_5.setAutoFillBackground(True)
        self.lat_lon_5.setFrame(False)
        self.lat_lon_5.setReadOnly(True)
        self.lat_lon_5.setObjectName("lat_lon_5")
        self.verticalLayout_19.addWidget(self.lat_lon_5)
        self.ele_tz_5 = QtWidgets.QLineEdit(self.win_tab)
        self.ele_tz_5.setAutoFillBackground(True)
        self.ele_tz_5.setFrame(False)
        self.ele_tz_5.setReadOnly(True)
        self.ele_tz_5.setObjectName("ele_tz_5")
        self.verticalLayout_19.addWidget(self.ele_tz_5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_19)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.line_17 = QtWidgets.QFrame(self.win_tab)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_17.addWidget(self.line_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_4 = QtWidgets.QWidget(self.win_tab)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.line_18 = QtWidgets.QFrame(self.widget_4)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_20.addWidget(self.line_18)
        self.label_32 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_20.addWidget(self.label_32)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        pixmap = QPixmap(self.legend_violen_path)
        self.label_17.setPixmap(pixmap)
        self.verticalLayout_20.addWidget(self.label_17)

        self.label_annual_avg_wind = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_annual_avg_wind.setFont(font)
        self.label_annual_avg_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_avg_wind.setObjectName("label_annual_avg_wind")
        self.label_annual_avg_wind.setText("Annual Average\nWind Velocity")
        self.verticalLayout_20.addWidget(self.label_annual_avg_wind)
        self.label_annual_avg_wind_val_1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setPointSize(8)
        font.setWeight(75)
        self.label_annual_avg_wind_val_1.setFont(font)
        self.label_annual_avg_wind_val_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_avg_wind_val_1.setObjectName("label_annual_avg_wind_val_1")
        self.label_annual_avg_wind_val_1.setText("")
        self.verticalLayout_20.addWidget(self.label_annual_avg_wind_val_1)

        self.label_annual_max_wind = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_annual_max_wind.setFont(font)
        self.label_annual_max_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_max_wind.setObjectName("label_annual_max_wind")
        self.label_annual_max_wind.setText("Annual Maximum\nWind Velocity")
        self.verticalLayout_20.addWidget(self.label_annual_max_wind)
        self.label_annual_max_wind_val_1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setPointSize(8)
        font.setWeight(75)
        self.label_annual_max_wind_val_1.setFont(font)
        self.label_annual_max_wind_val_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_annual_max_wind_val_1.setObjectName("label_annual_max_wind_val_1")
        self.label_annual_max_wind_val_1.setText("")
        self.verticalLayout_20.addWidget(self.label_annual_max_wind_val_1)
        self.line_19 = QtWidgets.QFrame(self.widget_4)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_20.addWidget(self.line_19)
        self.gridLayout_11.addLayout(self.verticalLayout_20, 0, 1, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.widget_4)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout_11.addWidget(self.line_20, 0, 2, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.widget_4)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_11.addWidget(self.line_21, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.widget_4)
        self.horizontalLayout_10.addWidget(self.canvas_4)
        self.verticalLayout_17.addLayout(self.horizontalLayout_10)
        self.gridLayout_12.addLayout(self.verticalLayout_17, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.win_tab, "")
        self.Grd_tab = QtWidgets.QWidget()
        self.Grd_tab.setObjectName("Grd_tab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.Grd_tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Weather_sum_6 = QtWidgets.QLabel(self.Grd_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_6.setFont(font)
        self.Weather_sum_6.setObjectName("Weather_sum_6")
        self.horizontalLayout_11.addWidget(self.Weather_sum_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.Location_6 = QtWidgets.QLabel(self.Grd_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_6.setFont(font)
        self.Location_6.setObjectName("Location_6")
        self.verticalLayout_22.addWidget(self.Location_6)
        self.Lat_Log_6 = QtWidgets.QLabel(self.Grd_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_6.setFont(font)
        self.Lat_Log_6.setObjectName("Lat_Log_6")
        self.verticalLayout_22.addWidget(self.Lat_Log_6)
        self.Ele_TZ_6 = QtWidgets.QLabel(self.Grd_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_6.setFont(font)
        self.Ele_TZ_6.setObjectName("Ele_TZ_6")
        self.verticalLayout_22.addWidget(self.Ele_TZ_6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.location_6 = QtWidgets.QLineEdit(self.Grd_tab)
        self.location_6.setAutoFillBackground(True)
        self.location_6.setFrame(False)
        self.location_6.setReadOnly(True)
        self.location_6.setObjectName("location_6")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_6.setFont(font)
        self.verticalLayout_23.addWidget(self.location_6)
        self.lat_lon_6 = QtWidgets.QLineEdit(self.Grd_tab)
        self.lat_lon_6.setAutoFillBackground(True)
        self.lat_lon_6.setFrame(False)
        self.lat_lon_6.setReadOnly(True)
        self.lat_lon_6.setObjectName("lat_lon_6")
        self.verticalLayout_23.addWidget(self.lat_lon_6)
        self.ele_tz_6 = QtWidgets.QLineEdit(self.Grd_tab)
        self.ele_tz_6.setAutoFillBackground(True)
        self.ele_tz_6.setFrame(False)
        self.ele_tz_6.setReadOnly(True)
        self.ele_tz_6.setObjectName("ele_tz_6")
        self.verticalLayout_23.addWidget(self.ele_tz_6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_23)
        self.verticalLayout_21.addLayout(self.horizontalLayout_11)
        self.line_22 = QtWidgets.QFrame(self.Grd_tab)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.verticalLayout_21.addWidget(self.line_22)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_5 = QtWidgets.QWidget(self.Grd_tab)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.line_23 = QtWidgets.QFrame(self.widget_5)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.verticalLayout_24.addWidget(self.line_23)
        self.label_38 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_24.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.widget_5)
        self.label_39.setObjectName("label_39")
        self.label_39.setText("DEPTH")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_24.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.widget_5)
        self.label_40.setObjectName("label_40")
        self.label_40.setText("0.5 meters")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #004C99;\n"
                                    "background: #99CCFF;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_24.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.widget_5)
        self.label_41.setObjectName("label_41")
        self.label_41.setText("2.0 meters")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #FF8000;\n"
                                    "background: #FFCC99;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_24.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.widget_5)
        self.label_42.setObjectName("label_42")
        self.label_42.setText("4.0 meters")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #009900;\n"
                                    "background: #99FF99;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_24.addWidget(self.label_42)
        self.line_24 = QtWidgets.QFrame(self.widget_5)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.verticalLayout_24.addWidget(self.line_24)
        self.gridLayout_13.addLayout(self.verticalLayout_24, 0, 1, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.widget_5)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_13.addWidget(self.line_25, 0, 2, 1, 1)
        self.line_26 = QtWidgets.QFrame(self.widget_5)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.gridLayout_13.addWidget(self.line_26, 0, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.widget_5)
        self.horizontalLayout_12.addWidget(self.canvas_5)
        self.verticalLayout_21.addLayout(self.horizontalLayout_12)
        self.gridLayout_14.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.Grd_tab, "")
        self.Hou_tab = QtWidgets.QWidget()
        self.Hou_tab.setObjectName("Hou_tab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.Hou_tab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Weather_sum_7 = QtWidgets.QLabel(self.Hou_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_7.setFont(font)
        self.Weather_sum_7.setObjectName("Weather_sum_7")
        self.horizontalLayout_13.addWidget(self.Weather_sum_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.Location_7 = QtWidgets.QLabel(self.Hou_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Location_7.setFont(font)
        self.Location_7.setObjectName("Location_7")
        self.verticalLayout_26.addWidget(self.Location_7)
        self.Lat_Log_7 = QtWidgets.QLabel(self.Hou_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lat_Log_7.setFont(font)
        self.Lat_Log_7.setObjectName("Lat_Log_7")
        self.verticalLayout_26.addWidget(self.Lat_Log_7)
        self.Ele_TZ_7 = QtWidgets.QLabel(self.Hou_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ele_TZ_7.setFont(font)
        self.Ele_TZ_7.setObjectName("Ele_TZ_7")
        self.verticalLayout_26.addWidget(self.Ele_TZ_7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.location_7 = QtWidgets.QLineEdit(self.Hou_tab)
        self.location_7.setAutoFillBackground(True)
        self.location_7.setFrame(False)
        self.location_7.setReadOnly(True)
        self.location_7.setObjectName("location_7")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.location_7.setFont(font)
        self.verticalLayout_27.addWidget(self.location_7)
        self.lat_lon_7 = QtWidgets.QLineEdit(self.Hou_tab)
        self.lat_lon_7.setAutoFillBackground(True)
        self.lat_lon_7.setFrame(False)
        self.lat_lon_7.setReadOnly(True)
        self.lat_lon_7.setObjectName("lat_lon_7")
        self.verticalLayout_27.addWidget(self.lat_lon_7)
        self.ele_tz_7 = QtWidgets.QLineEdit(self.Hou_tab)
        self.ele_tz_7.setAutoFillBackground(True)
        self.ele_tz_7.setFrame(False)
        self.ele_tz_7.setReadOnly(True)
        self.ele_tz_7.setObjectName("ele_tz_7")
        self.verticalLayout_27.addWidget(self.ele_tz_7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_27)
        self.verticalLayout_25.addLayout(self.horizontalLayout_13)
        self.line_27 = QtWidgets.QFrame(self.Hou_tab)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.verticalLayout_25.addWidget(self.line_27)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.widget_6 = QtWidgets.QWidget(self.Hou_tab)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.line_28 = QtWidgets.QFrame(self.widget_6)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.verticalLayout_28.addWidget(self.line_28)
        self.label_44 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_28.addWidget(self.label_44)

        self.label_45 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(False)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_45.setText("Temperature Range")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_28.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_46.setText("< 15°C")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #330000;\n"
                                    "background: #0066CC;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_28.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.widget_5)
        self.label_47.setObjectName("label_47")
        self.label_47.setText("> 15°C and < 25°C ")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #330000;\n"
                                    "background: #66B2FF;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_28.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.widget_5)
        self.label_48.setObjectName("label_48")
        self.label_48.setText("> 25°C and < 35°C ")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #330000;\n"
                                    "background: #FF7474;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_28.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(self.widget_5)
        self.label_49.setObjectName("label_49")
        self.label_49.setText("> 35°C")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(False)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setStyleSheet("QLabel\n"
                                    "{\n"
                                    "color: #330000;\n"
                                    "background: #CC0000;\n"
                                    "}\n"
                                    "")
        self.verticalLayout_28.addWidget(self.label_49)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_28.addItem(spacerItem7)
        self.label_colormap_def = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_colormap_def.setFont(font)
        self.label_colormap_def.setObjectName("label_45")
        self.label_colormap_def.setText("Colormap")
        self.label_colormap_def.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_28.addWidget(self.label_colormap_def)
        self.label_colormap_def_1 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(False)
        self.label_colormap_def_1.setFont(font)
        self.label_colormap_def_1.setObjectName("label_45")
        self.label_colormap_def_1.setText("A colormap is matrix that\ndefine the colors for graphics\nobjects by mapping data values\nto colors in colormap.")
        self.label_colormap_def_1.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_28.addWidget(self.label_colormap_def_1)
        self.line_29 = QtWidgets.QFrame(self.widget_6)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.verticalLayout_28.addWidget(self.line_29)
        self.gridLayout_15.addLayout(self.verticalLayout_28, 0, 1, 1, 1)
        self.line_30 = QtWidgets.QFrame(self.widget_6)
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.gridLayout_15.addWidget(self.line_30, 0, 2, 1, 1)
        self.line_31 = QtWidgets.QFrame(self.widget_6)
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.gridLayout_15.addWidget(self.line_31, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.widget_6)
        self.horizontalLayout_14.addWidget(self.canvas_6)
        self.verticalLayout_25.addLayout(self.horizontalLayout_14)
        self.gridLayout_16.addLayout(self.verticalLayout_25, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.Hou_tab, "")
        self.D_tab = QtWidgets.QWidget()
        self.D_tab.setObjectName("D_tab")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.D_tab)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.D_butt = QtWidgets.QPushButton(self.D_tab)
        self.D_butt.setObjectName("D_butt")
        self.D_butt.setFixedHeight(100)
        self.D_butt.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "color: #000066;\n"
                                        "background-color: #CCCCFF;\n"
                                        "border: 5px solid transparent;\n"
                                        "font-size: 15px;\n"
                                        "border-radius: 5px;\n"
                                        "\n"
                                        "}\n"
                                     "QPushButton:hover\n"
                                        "{\n"
                                        "background-color: #6666FF;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #39FF11);\n"
                                        "}\n"
                                        "")
        self.horizontalLayout_16.addWidget(self.D_butt)
        self.verticalLayout_29.addLayout(self.horizontalLayout_16)
        self.gridLayout_18.addLayout(self.verticalLayout_29, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.D_tab, "")


        ### Psy_tab
        self.Psy_tab = QtWidgets.QWidget()
        self.Psy_tab.setObjectName("Psy_tab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.Psy_tab)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.Weather_sum_9 = QtWidgets.QLabel(self.Psy_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Weather_sum_9.setFont(font)
        self.Weather_sum_9.setObjectName("Weather_sum_9")
        self.horizontalLayout_17.addWidget(self.Weather_sum_9)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.Location_9 = QtWidgets.QLabel(self.Psy_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Location_9.setFont(font)
        self.Location_9.setObjectName("Location_9")
        self.verticalLayout_34.addWidget(self.Location_9)
        self.Lat_Log_9 = QtWidgets.QLabel(self.Psy_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lat_Log_9.setFont(font)
        self.Lat_Log_9.setObjectName("Lat_Log_9")
        self.verticalLayout_34.addWidget(self.Lat_Log_9)
        self.Ele_TZ_9 = QtWidgets.QLabel(self.Psy_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ele_TZ_9.setFont(font)
        self.Ele_TZ_9.setObjectName("Ele_TZ_9")
        self.verticalLayout_34.addWidget(self.Ele_TZ_9)
        self.horizontalLayout_17.addLayout(self.verticalLayout_34)
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.location_9 = QtWidgets.QLineEdit(self.Psy_tab)
        self.location_9.setAutoFillBackground(True)
        self.location_9.setFrame(False)
        self.location_9.setReadOnly(True)
        self.location_9.setObjectName("location_9")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.location_9.setFont(font)
        self.verticalLayout_35.addWidget(self.location_9)
        self.lat_lon_9 = QtWidgets.QLineEdit(self.Psy_tab)
        self.lat_lon_9.setAutoFillBackground(True)
        self.lat_lon_9.setFrame(False)
        self.lat_lon_9.setReadOnly(True)
        self.lat_lon_9.setObjectName("lat_lon_9")
        self.verticalLayout_35.addWidget(self.lat_lon_9)
        self.ele_tz_9 = QtWidgets.QLineEdit(self.Psy_tab)
        self.ele_tz_9.setAutoFillBackground(True)
        self.ele_tz_9.setFrame(False)
        self.ele_tz_9.setReadOnly(True)
        self.ele_tz_9.setObjectName("ele_tz_9")
        self.verticalLayout_35.addWidget(self.ele_tz_9)
        self.horizontalLayout_17.addLayout(self.verticalLayout_35)
        self.verticalLayout_33.addLayout(self.horizontalLayout_17)
        self.line_37 = QtWidgets.QFrame(self.Psy_tab)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.verticalLayout_33.addWidget(self.line_37)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.widget_8 = QtWidgets.QWidget(self.Psy_tab)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_19.setObjectName("gridLayout_19")

        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        ################################################
    
        ### Time Input
        self.line_for_time_input = QtWidgets.QFrame(self.widget_8)
        self.line_for_time_input.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_for_time_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_for_time_input.setObjectName("line_for_time_input")
        self.verticalLayout_36.addWidget(self.line_for_time_input)

        self.gridLayout_time_change = QtWidgets.QGridLayout()
        self.gridLayout_time_change.setObjectName("gridLayout_time_change")
        self.to_label = QtWidgets.QLabel(self.widget_8)
        self.to_label.setText(("To"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_label.sizePolicy().hasHeightForWidth())
        self.to_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.to_label.setFont(font)
        self.to_label.setObjectName("to_label")
        self.gridLayout_time_change.addWidget(self.to_label, 1, 2, 1, 1)
        self.month_label = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_label.sizePolicy().hasHeightForWidth())
        self.month_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setText("MONTH :")
        self.month_label.setObjectName("month_label")
        self.gridLayout_time_change.addWidget(self.month_label, 2, 0, 1, 1)
        self.hour_label = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_label.sizePolicy().hasHeightForWidth())
        self.hour_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.hour_label.setFont(font)
        self.hour_label.setText("HOUR   :")
        self.hour_label.setObjectName("hour_label")
        self.gridLayout_time_change.addWidget(self.hour_label, 4, 0, 1, 1)
        self.hour_from_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_from_comboBox.sizePolicy().hasHeightForWidth())
        self.hour_from_comboBox.setSizePolicy(sizePolicy)
        self.hour_from_comboBox.setObjectName("hour_from_comboBox")
        self.hour_from_comboBox.addItem("1")
        self.hour_from_comboBox.addItem("2")
        self.hour_from_comboBox.addItem("3")
        self.hour_from_comboBox.addItem("4")
        self.hour_from_comboBox.addItem("5")
        self.hour_from_comboBox.addItem("6")
        self.hour_from_comboBox.addItem("7")
        self.hour_from_comboBox.addItem("8")
        self.hour_from_comboBox.addItem("9")
        self.hour_from_comboBox.addItem("10")
        self.hour_from_comboBox.addItem("11")
        self.hour_from_comboBox.addItem("12")
        self.hour_from_comboBox.addItem("13")
        self.hour_from_comboBox.addItem("14")
        self.hour_from_comboBox.addItem("15")
        self.hour_from_comboBox.addItem("16")
        self.hour_from_comboBox.addItem("17")
        self.hour_from_comboBox.addItem("18")
        self.hour_from_comboBox.addItem("19")
        self.hour_from_comboBox.addItem("20")
        self.hour_from_comboBox.addItem("21")
        self.hour_from_comboBox.addItem("22")
        self.hour_from_comboBox.addItem("23")
        self.hour_from_comboBox.addItem("24")
        self.hour_from_comboBox.setCurrentIndex(0)
        self.hour_from_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.hour_from_comboBox, 4, 1, 1, 1)
        self.day_label = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_label.sizePolicy().hasHeightForWidth())
        self.day_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.day_label.setFont(font)
        self.day_label.setText("DAY     :")
        self.day_label.setObjectName("day_label")
        self.gridLayout_time_change.addWidget(self.day_label, 3, 0, 1, 1)
        self.from_label = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.from_label.setFont(font)
        self.from_label.setText("From")
        self.from_label.setObjectName("from_label")
        self.gridLayout_time_change.addWidget(self.from_label, 1, 1, 1, 1)
        self.day_to_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_to_comboBox.sizePolicy().hasHeightForWidth())
        self.day_to_comboBox.setSizePolicy(sizePolicy)
        self.day_to_comboBox.setObjectName("day_to_comboBox")
        self.day_to_comboBox.addItem("1")
        self.day_to_comboBox.addItem("2")
        self.day_to_comboBox.addItem("3")
        self.day_to_comboBox.addItem("4")
        self.day_to_comboBox.addItem("5")
        self.day_to_comboBox.addItem("6")
        self.day_to_comboBox.addItem("7")
        self.day_to_comboBox.addItem("8")
        self.day_to_comboBox.addItem("9")
        self.day_to_comboBox.addItem("10")
        self.day_to_comboBox.addItem("11")
        self.day_to_comboBox.addItem("12")
        self.day_to_comboBox.addItem("13")
        self.day_to_comboBox.addItem("14")
        self.day_to_comboBox.addItem("15")
        self.day_to_comboBox.addItem("16")
        self.day_to_comboBox.addItem("17")
        self.day_to_comboBox.addItem("18")
        self.day_to_comboBox.addItem("19")
        self.day_to_comboBox.addItem("20")
        self.day_to_comboBox.addItem("21")
        self.day_to_comboBox.addItem("22")
        self.day_to_comboBox.addItem("23")
        self.day_to_comboBox.addItem("24")
        self.day_to_comboBox.addItem("25")
        self.day_to_comboBox.addItem("26")
        self.day_to_comboBox.addItem("27")
        self.day_to_comboBox.addItem("28")
        self.day_to_comboBox.addItem("29")
        self.day_to_comboBox.addItem("30")
        self.day_to_comboBox.addItem("31")
        self.day_to_comboBox.setCurrentIndex(30)
        self.day_to_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.day_to_comboBox, 3, 2, 1, 1)
        self.day_from_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_from_comboBox.sizePolicy().hasHeightForWidth())
        self.day_from_comboBox.setSizePolicy(sizePolicy)
        self.day_from_comboBox.setObjectName("day_from_comboBox")
        self.day_from_comboBox.addItem("1")
        self.day_from_comboBox.addItem("2")
        self.day_from_comboBox.addItem("3")
        self.day_from_comboBox.addItem("4")
        self.day_from_comboBox.addItem("5")
        self.day_from_comboBox.addItem("6")
        self.day_from_comboBox.addItem("7")
        self.day_from_comboBox.addItem("8")
        self.day_from_comboBox.addItem("9")
        self.day_from_comboBox.addItem("10")
        self.day_from_comboBox.addItem("11")
        self.day_from_comboBox.addItem("12")
        self.day_from_comboBox.addItem("13")
        self.day_from_comboBox.addItem("14")
        self.day_from_comboBox.addItem("15")
        self.day_from_comboBox.addItem("16")
        self.day_from_comboBox.addItem("17")
        self.day_from_comboBox.addItem("18")
        self.day_from_comboBox.addItem("19")
        self.day_from_comboBox.addItem("20")
        self.day_from_comboBox.addItem("21")
        self.day_from_comboBox.addItem("22")
        self.day_from_comboBox.addItem("23")
        self.day_from_comboBox.addItem("24")
        self.day_from_comboBox.addItem("25")
        self.day_from_comboBox.addItem("26")
        self.day_from_comboBox.addItem("27")
        self.day_from_comboBox.addItem("28")
        self.day_from_comboBox.addItem("29")
        self.day_from_comboBox.addItem("30")
        self.day_from_comboBox.addItem("31")
        self.day_from_comboBox.setCurrentIndex(0)
        self.day_from_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.day_from_comboBox, 3, 1, 1, 1)
        self.month_to_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_to_comboBox.sizePolicy().hasHeightForWidth())
        self.month_to_comboBox.setSizePolicy(sizePolicy)
        self.month_to_comboBox.setObjectName("month_to_comboBox")
        self.month_to_comboBox.addItem("January")
        self.month_to_comboBox.addItem("February")
        self.month_to_comboBox.addItem("March")
        self.month_to_comboBox.addItem("April")
        self.month_to_comboBox.addItem("May")
        self.month_to_comboBox.addItem("June")
        self.month_to_comboBox.addItem("July")
        self.month_to_comboBox.addItem("August")
        self.month_to_comboBox.addItem("September")
        self.month_to_comboBox.addItem("October")
        self.month_to_comboBox.addItem("November")
        self.month_to_comboBox.addItem("December")
        self.month_to_comboBox.setCurrentIndex(11)
        self.month_to_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.month_to_comboBox, 2, 2, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_70")
        self.label_71.setText("TIME")
        self.gridLayout_time_change.addWidget(self.label_71, 0, 0, 2, 1)
        self.time_type_combo_box = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_type_combo_box.sizePolicy().hasHeightForWidth())
        self.time_type_combo_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.time_type_combo_box.setFont(font)
        self.time_type_combo_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_type_combo_box.setAutoFillBackground(True)
        self.time_type_combo_box.setMaxVisibleItems(10)
        self.time_type_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.time_type_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.time_type_combo_box.setObjectName("time_type_combo_box")
        self.time_type_combo_box.addItem("Annual")
        self.time_type_combo_box.addItem("Custom")
        self.time_type_combo_box.addItem("Summer")
        self.time_type_combo_box.addItem("Spring")
        self.time_type_combo_box.addItem("Monsoon")
        self.time_type_combo_box.addItem("Autumn")
        self.time_type_combo_box.addItem("Winter")
        self.time_type_combo_box.setCurrentIndex(0)
        self.gridLayout_time_change.addWidget(self.time_type_combo_box, 0, 1, 1, 2)
        self.hour_to_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_to_comboBox.sizePolicy().hasHeightForWidth())
        self.hour_to_comboBox.setSizePolicy(sizePolicy)
        self.hour_to_comboBox.setObjectName("hour_to_comboBox")
        self.hour_to_comboBox.addItem("1")
        self.hour_to_comboBox.addItem("2")
        self.hour_to_comboBox.addItem("3")
        self.hour_to_comboBox.addItem("4")
        self.hour_to_comboBox.addItem("5")
        self.hour_to_comboBox.addItem("6")
        self.hour_to_comboBox.addItem("7")
        self.hour_to_comboBox.addItem("8")
        self.hour_to_comboBox.addItem("9")
        self.hour_to_comboBox.addItem("10")
        self.hour_to_comboBox.addItem("11")
        self.hour_to_comboBox.addItem("12")
        self.hour_to_comboBox.addItem("13")
        self.hour_to_comboBox.addItem("14")
        self.hour_to_comboBox.addItem("15")
        self.hour_to_comboBox.addItem("16")
        self.hour_to_comboBox.addItem("17")
        self.hour_to_comboBox.addItem("18")
        self.hour_to_comboBox.addItem("19")
        self.hour_to_comboBox.addItem("20")
        self.hour_to_comboBox.addItem("21")
        self.hour_to_comboBox.addItem("22")
        self.hour_to_comboBox.addItem("23")
        self.hour_to_comboBox.addItem("24")
        self.hour_to_comboBox.setCurrentIndex(23)
        self.hour_to_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.hour_to_comboBox, 4, 2, 1, 1)
        self.month_from_comboBox = QtWidgets.QComboBox(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_from_comboBox.sizePolicy().hasHeightForWidth())
        self.month_from_comboBox.setSizePolicy(sizePolicy)
        self.month_from_comboBox.setObjectName("month_from_comboBox")
        self.month_from_comboBox.addItem("January")
        self.month_from_comboBox.addItem("February")
        self.month_from_comboBox.addItem("March")
        self.month_from_comboBox.addItem("April")
        self.month_from_comboBox.addItem("May")
        self.month_from_comboBox.addItem("June")
        self.month_from_comboBox.addItem("July")
        self.month_from_comboBox.addItem("August")
        self.month_from_comboBox.addItem("September")
        self.month_from_comboBox.addItem("October")
        self.month_from_comboBox.addItem("November")
        self.month_from_comboBox.addItem("December")
        self.month_from_comboBox.setCurrentIndex(0)
        self.month_from_comboBox.setDisabled(True)
        self.gridLayout_time_change.addWidget(self.month_from_comboBox, 2, 1, 1, 1)
        self.verticalLayout_36.addLayout(self.gridLayout_time_change)
        self.line_38 = QtWidgets.QFrame(self.widget_8)
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.verticalLayout_36.addWidget(self.line_38)
        ## Evaporative saturation efficiency
        self.line_for_evap_efficiency_input = QtWidgets.QFrame(self.widget_8)
        self.line_for_evap_efficiency_input.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_for_evap_efficiency_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_for_evap_efficiency_input.setObjectName("line_for_evap_efficiency_input")
        self.verticalLayout_36.addWidget(self.line_for_evap_efficiency_input)
        self.gridLayout_evap_efficiency = QtWidgets.QGridLayout()
        self.gridLayout_evap_efficiency.setObjectName("gridLayout_evap_efficiency")
        self.Evaporative_efficiency_input_label= QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        self.Evaporative_efficiency_input_label.setFont(font)
        self.Evaporative_efficiency_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Evaporative_efficiency_input_label.setObjectName("Evaporative_efficiency_input_label")
        self.Evaporative_efficiency_input_label.setText("Evaporative cooler Efficiency (%)")
        self.gridLayout_evap_efficiency.addWidget(self.Evaporative_efficiency_input_label, 0, 0, 1, 1)
        self.evap_efficiency_value = QtWidgets.QLineEdit(self.widget_8)
        self.evap_efficiency_value.setAlignment(QtCore.Qt.AlignCenter)
        self.evap_efficiency_value.setFixedHeight(23)
        self.evap_efficiency_value.setFixedWidth(35)
        self.evap_efficiency_value.setText("100")
        self.gridLayout_evap_efficiency.addWidget(self.evap_efficiency_value, 0, 1, 1, 1)
        self.verticalLayout_36.addLayout(self.gridLayout_evap_efficiency)
        self.line_42 = QtWidgets.QFrame(self.widget_8)
        self.line_42.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.verticalLayout_36.addWidget(self.line_42)
        ## Calling passive function
        self.passive_view()

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_36.addItem(spacerItem)
        self.line_39 = QtWidgets.QFrame(self.widget_8)
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.verticalLayout_36.addWidget(self.line_39)
        self.gridLayout_19.addLayout(self.verticalLayout_36, 0, 1, 1, 1)
        self.line_40 = QtWidgets.QFrame(self.widget_8)
        self.line_40.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.gridLayout_19.addWidget(self.line_40, 0, 2, 1, 1)
        self.line_41 = QtWidgets.QFrame(self.widget_8)
        self.line_41.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.gridLayout_19.addWidget(self.line_41, 0, 0, 1, 1)
        self.horizontalLayout_18.addWidget(self.widget_8)
        self.horizontalLayout_18.addWidget(self.canvas_8)
        self.verticalLayout_33.addLayout(self.horizontalLayout_18)
        self.gridLayout_20.addLayout(self.verticalLayout_33, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.Psy_tab, "")



        self.Recom_tab = QtWidgets.QWidget()
        self.Recom_tab.setObjectName("Recom_tab")
        self.gridLayout_recom = QtWidgets.QGridLayout(self.Recom_tab)
        self.gridLayout_recom.setObjectName("gridLayout_recom")
        self.verticalLayout_recom = QtWidgets.QVBoxLayout()
        self.verticalLayout_recom.setObjectName("verticalLayout_recom")
        self.label_recom = QtWidgets.QLabel(self.Recom_tab)
        self.label_recom.setText("Design Recommendations")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_recom.setFont(font)
        self.label_recom.setObjectName("label_recom")
        self.verticalLayout_recom.addWidget(self.label_recom)
        self.line_recom = QtWidgets.QFrame(self.Recom_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_recom.setFont(font)
        self.line_recom.setLineWidth(2)
        self.line_recom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_recom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_recom.setObjectName("line_recom")
        self.verticalLayout_recom.addWidget(self.line_recom)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_recom.addItem(spacerItem)
        self.label_max_passive = QtWidgets.QLabel(self.Recom_tab)
        self.label_max_passive.setObjectName("label_max_passive")
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_max_passive.setFont(font)
        self.verticalLayout_recom.addWidget(self.label_max_passive)
        self.line_2_recom = QtWidgets.QFrame(self.Recom_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_2_recom.setFont(font)
        self.line_2_recom.setLineWidth(2)
        self.line_2_recom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2_recom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2_recom.setObjectName("line_2_recom")
        self.verticalLayout_recom.addWidget(self.line_2_recom)
        self.textEdit_design_recom = QtWidgets.QTextEdit(self.Recom_tab)
        self.textEdit_design_recom.setReadOnly(True)
        self.textEdit_design_recom.setObjectName("textEdit_design_recom")
        self.textEdit_design_recom.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Symbol\'; font-size:14pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">     </span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Evaporative cooling methods:</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Humidify hot dry air before it enters the building from enclosed outdoor spaces with spray-like fountains, misters, wet pavement, or cooling towers.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">An Evaporative Cooler can provide enough cooling capacity (if water is available and humidity is low) thus reducing or even eliminating air conditioning).</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Traditional passive homes in hot windy dry climates used enclosed well shaded courtyards, with a small fountain to provide wind-protected microclimates and increase humidity to reduce temperature.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Symbol\'; font-size:14pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">     </span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Thermal mass design methods:</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Traditional passive homes in hot dry season in composite climates used high mass construction with small recessed shaded openings, operable for night ventilation to cool the mass.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Use light coloured building materials and cool roofs (with high emissivity) to minimize conducted heat gain.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">The best high mass walls use exterior insulation (like EIFS foam) and expose the mass on the interior or add plaster or direct contact drywall.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Symbol\'; font-size:14pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">     </span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Natural and forced ventilation methods:</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">On hot days ceiling fans or indoor air motion can make it seem cooler by 2.8</span><span style=\" font-size:12pt; vertical-align:super;\">o</span><span style=\" font-size:12pt;\">C or more, thus less air conditioning is needed.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Shaded outdoor buffer zones (porch, patio, lanai) oriented to the prevailing breezes can extend living and working areas in warm or humid weather.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Use open plan interiors to promote natural cross ventilation, or use louvered doors, or instead use jump ducts if privacy is required.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Good natural ventilation can reduce or eliminate air conditioning in warm weather, if windows are well shaded and oriented to prevailing breezes.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Symbol\'; font-size:14pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">     </span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Sun shading methods:</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Window overhangs (designed for this latitude) or operable sunshades (awnings that extend in summer) can reduce or eliminate air conditioning.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Minimize or eliminate west facing glazing to reduce summer and fall afternoon heat gain.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Provide double pane high performance glazing (Low-E) on west, north, and east, but clear on south for maximum passive solar gain.</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Symbol\'; font-size:14pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">     </span><span style=\" font-family:\'Verdana,sans-serif\'; font-size:14pt; font-weight:600;\">Use of ground temperature:</span><span style=\" font-size:8pt;\"> </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-size:12pt;\">Earth sheltering, occupied basements, or earth tubes reduce heat loads in very hot dry climates because the earth stays near average annual temperature.</span><span style=\" font-size:8pt;\"> </span></p></body></html>")

        self.verticalLayout_recom.addWidget(self.textEdit_design_recom)
        self.line_3_recom = QtWidgets.QFrame(self.Recom_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_3_recom.setFont(font)
        self.line_3_recom.setLineWidth(2)
        self.line_3_recom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3_recom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3_recom.setObjectName("line_2")
        self.verticalLayout_recom.addWidget(self.line_3_recom)
        self.gridLayout_recom.addLayout(self.verticalLayout_recom, 0, 0, 1, 1)
        self.WFS_tab.addTab(self.Recom_tab, "")
        self.gridLayout.addWidget(self.WFS_tab, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi_merge(MainWindow)
        self.WFS_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.back_butt.clicked.connect(lambda: self.back_page())

        self.collect_epw(fpath)
        self.radiobut_1.clicked.connect(lambda: self.temp_graph(text = self.radiobut_1.text()))
        self.radiobut_2.clicked.connect(lambda: self.temp_graph(text = self.radiobut_2.text()))
        self.radiobut_3.clicked.connect(lambda: self.temp_graph(text = self.radiobut_3.text()))
        self.radiobut_4.clicked.connect(lambda: self.radia_graph(text = self.radiobut_4.text()))
        self.radiobut_5.clicked.connect(lambda: self.radia_graph(text = self.radiobut_5.text()))
        self.radiobut_6.clicked.connect(lambda: self.radia_graph(text = self.radiobut_6.text()))
        self.radiobut_7.clicked.connect(lambda: self.illumi_graph(text = self.radiobut_7.text()))
        self.radiobut_8.clicked.connect(lambda: self.illumi_graph(text = self.radiobut_8.text()))
        self.radiobut_v_00_05.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.radiobut_v_05_10.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.radiobut_v_10_15.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.checkbox_comf.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.checkbox_evap.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.checkbox_active_points.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.checkbox_thml.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.checkbox_sunshad.clicked.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.D_butt.clicked.connect(lambda: self.d_graph())

        self.time_type_combo_box.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.month_from_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.month_to_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.day_from_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.day_to_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.hour_from_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        self.hour_to_comboBox.currentTextChanged.connect(lambda: self.checkbox_clicked_bioclimatic())
        
    def passive_view(self):
        self.label_69 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.label_69.setText("Select Design Strategies")
        self.verticalLayout_36.addWidget(self.label_69)
        self.checkbox_comf = QtWidgets.QCheckBox("Comfort Zone")
        self.checkbox_comf.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_comf.setFont(font)
        self.verticalLayout_36.addWidget(self.checkbox_comf)
        self.checkbox_comf.setStyleSheet("QCheckBox:checked\n"
                                         "{\n"
                                         "background: #CCFFFF;\n"
                                         "color: #4169E1;\n"
                                         "}\n"
                                         "QCheckBox\n"
                                         "{\n"
                                         "spacing: 5px;\n"
                                         "}\n"
                                         "QCheckBox::indicator\n"
                                         "{\n"
                                         "width: 12px;\n"
                                         "height: 12px;\n"
                                         "}\n"
                                         "QCheckBox::indicator:checked\n"
                                         "{\n"
                                         "background: #4169E1;\n"
                                         "}\n"
                                         "")
        self.checkbox_evap = QtWidgets.QCheckBox("Evaporative cooling")
        self.checkbox_evap.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_evap.setFont(font)
        self.verticalLayout_36.addWidget(self.checkbox_evap)
        self.checkbox_evap.setStyleSheet("QCheckBox:checked\n"
                                         "{\n"
                                         "background: #99FF99;\n"
                                         "color: #008000;\n"
                                         "}\n"
                                         "QCheckBox\n"
                                         "{\n"
                                         "spacing: 5px;\n"
                                         "}\n"
                                         "QCheckBox::indicator\n"
                                         "{\n"
                                         "width: 12px;\n"
                                         "height: 12px;\n"
                                         "}\n"
                                         "QCheckBox::indicator:checked\n"
                                         "{\n"
                                         "background: #008000;\n"
                                         "}\n"
                                         "")
        self.checkbox_thml = QtWidgets.QCheckBox("Thermal mass")
        self.checkbox_thml.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_thml.setFont(font)
        self.verticalLayout_36.addWidget(self.checkbox_thml)
        self.checkbox_thml.setStyleSheet("QCheckBox:checked\n"
                                         "{\n"
                                         "background: #FFFF99;\n"
                                         "color: #CCCC00;\n"
                                         "}\n"
                                         "QCheckBox\n"
                                         "{\n"
                                         "spacing: 5px;\n"
                                         "}\n"
                                         "QCheckBox::indicator\n"
                                         "{\n"
                                         "width: 12px;\n"
                                         "height: 12px;\n"
                                         "}\n"
                                         "QCheckBox::indicator:checked\n"
                                         "{\n"
                                         "background: #FFFF00;\n"
                                         "}\n"
                                         "")
        self.checkbox_sunshad = QtWidgets.QCheckBox("Sun shading")
        self.checkbox_sunshad.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_sunshad.setFont(font)
        self.verticalLayout_36.addWidget(self.checkbox_sunshad)
        self.checkbox_sunshad.setStyleSheet("QCheckBox:checked\n"
                                            "{\n"
                                            "background: #FFB266;\n"
                                            "color: #FF4500;\n"
                                            "}\n"
                                            "QCheckBox\n"
                                            "{\n"
                                            "spacing: 5px;\n"
                                            "}\n"
                                            "QCheckBox::indicator\n"
                                            "{\n"
                                            "width: 12px;\n"
                                            "height: 12px;\n"
                                            "}\n"
                                            "QCheckBox::indicator:checked\n"
                                            "{\n"
                                            "background: #FF4500;\n"
                                            "}\n"
                                            "")

        self.checkbox_active_points = QtWidgets.QCheckBox("Active Cooling/Heating/Dehumidification")
        self.checkbox_active_points.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_active_points.setFont(font)
        self.checkbox_active_points.setToolTip("Active Cooling/Heating/Humidification/Dehumidification")
        self.verticalLayout_36.addWidget(self.checkbox_active_points)
        self.checkbox_active_points.setStyleSheet("QCheckBox:checked\n"
                                                  "{\n"
                                                  "background: #FFCCCC;\n"
                                                  "color: red;\n"
                                                  "}\n"
                                                  "QCheckBox\n"
                                                  "{\n"
                                                  "spacing: 5px;\n"
                                                  "}\n"
                                                  "QCheckBox::indicator\n"
                                                  "{\n"
                                                  "width: 12px;\n"
                                                  "height: 12px;\n"
                                                  "}\n"
                                                  "QCheckBox::indicator:checked\n"
                                                  "{\n"
                                                  "background: red;\n"
                                                  "}\n"
                                                  "")
        self.checkbox_comf_net = QtWidgets.QCheckBox("Comfort Zone")
        self.checkbox_comf_net.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(False)
        self.checkbox_comf_net.setFont(font)
        self.verticalLayout_36.addWidget(self.checkbox_comf_net)
        self.checkbox_comf_net.setStyleSheet("QCheckBox:checked\n"
                                             "{\n"
                                             "background: #CCFFFF;\n"
                                             "color: #4169E1;\n"
                                             "}\n"
                                             "QCheckBox\n"
                                             "{\n"
                                             "spacing: 5px;\n"
                                             "}\n"
                                             "QCheckBox::indicator\n"
                                             "{\n"
                                             "width: 12px;\n"
                                             "height: 12px;\n"
                                             "}\n"
                                             "QCheckBox::indicator:checked\n"
                                             "{\n"
                                             "background: #4169E1;\n"
                                             "}\n"
                                             "")
        ### Velocity input
        self.line_for_velocity_input = QtWidgets.QFrame(self.widget_8)
        self.line_for_velocity_input.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_for_velocity_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_for_velocity_input.setObjectName("line_for_velocity_input")
        self.verticalLayout_36.addWidget(self.line_for_velocity_input)

        self.verticalLayout_passive_velocity_range = QtWidgets.QVBoxLayout()
        self.label_70 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.label_70.setText("Select Air Velocity")
        self.verticalLayout_passive_velocity_range.addWidget(self.label_70)
        self.radiobut_v_00_05 = QtWidgets.QRadioButton("0 - 0.5 m/s")
        self.radiobut_v_00_05.setStyleSheet(
            "QRadioButton::indicator::checked\n"
            "{\n"
            "background: #0080FF;\n"
            "color: #001933;\n"
            "}\n"
            "QRadioButton\n"
            "{\n"
            "background: #CCe5FF;\n"
            "color: #001933;\n"
            "}\n")
        self.verticalLayout_passive_velocity_range.addWidget(self.radiobut_v_00_05)
        self.radiobut_v_00_05.setChecked(True)
        self.radiobut_v_05_10 = QtWidgets.QRadioButton("0.5 - 1.0 m/s")
        self.radiobut_v_05_10.setStyleSheet(
            "QRadioButton::indicator::checked\n"
            "{\n"
            "background: #0080FF;\n"
            "color: #001933;\n"
            "}\n"
            "QRadioButton\n"
            "{\n"
            "background: #CCe5FF;\n"
            "color: #001933;\n"
            "}\n")
        self.verticalLayout_passive_velocity_range.addWidget(self.radiobut_v_05_10)
        self.radiobut_v_10_15 = QtWidgets.QRadioButton("1.0 - 1.5 m/s")
        self.radiobut_v_10_15.setStyleSheet(
            "QRadioButton::indicator::checked\n"
            "{\n"
            "background: #0080FF;\n"
            "color: #001933;\n"
            "}\n"
            "QRadioButton\n"
            "{\n"
            "background: #CCe5FF;\n"
            "color: #001933;\n"
            "}\n")
        self.verticalLayout_passive_velocity_range.addWidget(self.radiobut_v_10_15)
        self.verticalLayout_36.addLayout(self.verticalLayout_passive_velocity_range)

    def checkbox_clicked_bioclimatic(self):

        if self.radiobut_v_00_05.isChecked():
            text = self.radiobut_v_00_05.text()
        if self.radiobut_v_05_10.isChecked():
            text = self.radiobut_v_05_10.text()
        if self.radiobut_v_10_15.isChecked():
            text = self.radiobut_v_10_15.text()
        if self.checkbox_comf.checkState() == 2:
            comf = 1
        else:
            comf = 0
        if self.checkbox_active_points.checkState() == 2:
            epw = 1
        else:
            epw = 0
        if self.checkbox_evap.checkState() == 2:
            evap = 1
        else:
            evap = 0
        if self.checkbox_thml.checkState() == 2:
            thm = 1
        else:
            thm = 0
        if self.checkbox_sunshad.checkState() == 2:
            sun = 1
        else:
            sun = 0

        if self.time_type_combo_box.currentText() == "Annual":
            self.month_from_comboBox.setCurrentIndex(0)
            self.month_to_comboBox.setCurrentIndex(11)
            self.day_from_comboBox.setCurrentIndex(0)
            self.day_to_comboBox.setCurrentIndex(30)
            self.hour_from_comboBox.setCurrentIndex(0)
            self.hour_to_comboBox.setCurrentIndex(23)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(True)
            self.hour_to_comboBox.setDisabled(True)

        if self.time_type_combo_box.currentText() == "Custom":
            self.month_from_comboBox.setDisabled(False)
            self.month_to_comboBox.setDisabled(False)
            self.day_from_comboBox.setDisabled(False)
            self.day_to_comboBox.setDisabled(False)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)

        if self.time_type_combo_box.currentText() == "Spring":
            self.month_from_comboBox.setCurrentIndex(1)
            self.month_to_comboBox.setCurrentIndex(2)
            self.day_from_comboBox.setCurrentIndex(0)
            self.day_to_comboBox.setCurrentIndex(30)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)

        if self.time_type_combo_box.currentText() == "Summer":
            self.month_from_comboBox.setCurrentIndex(3)
            self.month_to_comboBox.setCurrentIndex(5)
            self.day_from_comboBox.setCurrentIndex(0)
            self.day_to_comboBox.setCurrentIndex(30)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)

        if self.time_type_combo_box.currentText() == "Monsoon":
            self.month_from_comboBox.setCurrentIndex(6)
            self.month_to_comboBox.setCurrentIndex(8)
            self.day_from_comboBox.setCurrentIndex(0)
            self.day_to_comboBox.setCurrentIndex(14)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)

        if self.time_type_combo_box.currentText() == "Autumn":
            self.month_from_comboBox.setCurrentIndex(8)
            self.month_to_comboBox.setCurrentIndex(10)
            self.day_from_comboBox.setCurrentIndex(15)
            self.day_to_comboBox.setCurrentIndex(30)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)

        if self.time_type_combo_box.currentText() == "Winter":
            self.month_from_comboBox.setCurrentIndex(11)
            self.month_to_comboBox.setCurrentIndex(0)
            self.day_from_comboBox.setCurrentIndex(0)
            self.day_to_comboBox.setCurrentIndex(30)
            self.month_from_comboBox.setDisabled(True)
            self.month_to_comboBox.setDisabled(True)
            self.day_from_comboBox.setDisabled(True)
            self.day_to_comboBox.setDisabled(True)
            self.hour_from_comboBox.setDisabled(False)
            self.hour_to_comboBox.setDisabled(False)



        m1 = self.month_from_comboBox.currentIndex() + 1
        m2 = self.month_to_comboBox.currentIndex() + 1
        d1 = self.day_from_comboBox.currentIndex() + 1
        d2 = self.day_to_comboBox.currentIndex() + 1
        t1 = self.hour_from_comboBox.currentIndex() +1
        t2 = self.hour_to_comboBox.currentIndex() + 1
        print(m1,m2,d1,d2,t1,t2)
        custom_dbt, custom_rh, custom_count_psycho = self.time_hours_range_change(m1,m2,d1,d2,t1,t2)

        print(custom_count_psycho)
        if self.evap_efficiency_value.text() != "":
            evap_efficiency = int(self.evap_efficiency_value.text())
            print(evap_efficiency)
        else:
            evap_efficiency = 0

        if custom_count_psycho != 0:
            self.psychrometric_graph(text, comf, epw, evap, thm, sun, custom_dbt, custom_rh, custom_count_psycho, evap_efficiency)
        #else:
            #self.messagebox_error(MainWindow)

    def time_hours_range_change(self, m1,m2,d1,d2,t1,t2):
        custom_dbt_run = []
        custom_rh_run = []
        custom_count_run = 0
        for temo, relo, mo, do, ho in zip(self.dbt, self.rh, self.m, self.d, self.h):
            if m1 < m2:
                if int(mo) == int(m1):
                    if int(do) in range(d1, 32):
                        if int(ho) in range(t1, t2 + 1):
                            custom_dbt_run.append(temo)
                            custom_rh_run.append(relo)
                            custom_count_run = custom_count_run + 1
                if int(mo) > int(m1) and int(mo) < int(m2):
                    if int(ho) in range(t1, t2 + 1):
                        custom_dbt_run.append(temo)
                        custom_rh_run.append(relo)
                        custom_count_run = custom_count_run + 1
                if int(mo) == int(m2):
                    if int(do) in range(1, d2 + 1):
                        if int(ho) in range(t1, t2 + 1):
                            custom_dbt_run.append(temo)
                            custom_rh_run.append(relo)
                            custom_count_run = custom_count_run + 1

            if int(m1) == int(m2):
                if int(d1) < int(d2):
                    if int(mo) == int(m1):
                        if int(do) in range(d1, d2 + 1):
                            if int(ho) in range(t1, t2 + 1):
                                custom_dbt_run.append(temo)
                                custom_rh_run.append(relo)
                                custom_count_run = custom_count_run + 1

            if int(m2) < int(m1):
                if int(mo) == int(m2):
                    if int(do) in range(1, d2 + 1):
                        if int(ho) in range(t1, t2 + 1):
                            custom_dbt_run.append(temo)
                            custom_rh_run.append(relo)
                            custom_count_run = custom_count_run + 1
                if int(mo) < int(m2) or int(mo) > int(m1):
                    if int(ho) in range(t1, t2 + 1):
                        custom_dbt_run.append(temo)
                        custom_rh_run.append(relo)
                        custom_count_run = custom_count_run + 1
                if int(mo) == int(m1):
                    if int(do) in range(d1, 32):
                        if int(ho) in range(t1, t2 + 1):
                            custom_dbt_run.append(temo)
                            custom_rh_run.append(relo)
                            custom_count_run = custom_count_run + 1

        return custom_dbt_run, custom_rh_run, custom_count_run

    def messagebox_error(self, MainWindow):
            message_count_error = QtWidgets.QMessageBox.about(self, "Error", "Please check input values.")

    def retranslateUi_merge(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Monthly_mean.setText(_translate("MainWindow", "MONTHLY MEANS"))
        self.label_15.setText(_translate("MainWindow", "Global Horizontal Radiation (avg. hr.)"))
        self.label.setText(_translate("MainWindow", "Direct Normal Radiation (avg. hr.)"))
        self.label_3.setText(_translate("MainWindow", "Diffuse Radiation (avg. hr.)"))
        self.label_5.setText(_translate("MainWindow", "Global Horizontal Radiation (max. hr.)"))
        self.label_16.setText(_translate("MainWindow", "Direct Normal Radiation (max. hr.)"))
        self.label_2.setText(_translate("MainWindow", "Diffuse Radiation (max. hr.)"))
        self.label_10.setText(_translate("MainWindow", "Dry Bulb Temperature (avg. monthly)"))
        self.label_4.setText(_translate("MainWindow", "Dry Bulb Temperature (max.)"))
        self.label_6.setText(_translate("MainWindow", "Relative Humidity (avg. monthly)"))
        self.label_7.setText(_translate("MainWindow", "Wet Bulb Temperature (avg. monthly)"))
        self.label_8.setText(_translate("MainWindow", "Dew Point Temperature (avg. monthly)"))
        self.label_9.setText(_translate("MainWindow", "Global Horizontal Illumination (avg. hr.)"))
        self.label_tm.setText(_translate("MainWindow", "Direct Normal Illumination (avg. hr.)"))
        self.May.setText(_translate("MainWindow", "MAY"))
        self.Jun.setText(_translate("MainWindow", "JUN"))
        self.Apr.setText(_translate("MainWindow", "APR"))
        self.Jul.setText(_translate("MainWindow", "JUL"))
        self.Sep.setText(_translate("MainWindow", "SEP"))
        self.Oct.setText(_translate("MainWindow", "OCT"))
        self.Nov.setText(_translate("MainWindow", "NOV"))
        self.Dec.setText(_translate("MainWindow", "DEC"))
        self.Aug.setText(_translate("MainWindow", "AUG"))
        self.Feb.setText(_translate("MainWindow", "FEB"))
        self.Jan.setText(_translate("MainWindow", "JAN"))
        self.Mar.setText(_translate("MainWindow", "MAR"))
        self.Weather_sum.setText(_translate("MainWindow", "Weather File Summary"))
        self.Location.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_30.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_51.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_52.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_53.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_55.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_57.setText(_translate("MainWindow", "Wh/sq.m"))
        self.label_54.setText(_translate("MainWindow", "Degree C"))
        self.label_56.setText(_translate("MainWindow", "degree C"))
        self.label_59.setText(_translate("MainWindow", "Percent"))
        self.label_61.setText(_translate("MainWindow", "Degree C"))
        self.label_58.setText(_translate("MainWindow", "Degree C"))
        self.label_60.setText(_translate("MainWindow", "Lux"))
        self.label_t.setText(_translate("MainWindow", "Lux"))
        self.back_butt.setText(_translate("MainWindow", "Back to the Home Page"))
        self.D_butt.setText(_translate("MainWindow", "Click To View 3D Plot of Dry Bulb Temperature"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.WFS_tab1), _translate("MainWindow", "Weather File Summary"))
        self.Weather_sum_2.setText(_translate("MainWindow", "Temperature Range"))
        self.Location_2.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_2.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_2.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_11.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.temp_tab), _translate("MainWindow", "Temperature Range"))
        self.Weather_sum_3.setText(_translate("MainWindow", "Radiation Range"))
        self.Location_3.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_3.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_3.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_19.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.rad_tab), _translate("MainWindow", "Radiation Range"))
        self.Weather_sum_4.setText(_translate("MainWindow", "Illumination Range"))
        self.Location_4.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_4.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_4.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_25.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.illumi_tab), _translate("MainWindow", "Illumination Range"))
        self.Weather_sum_5.setText(_translate("MainWindow", "Wind Velocity Range"))
        self.Location_5.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_5.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_5.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_32.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.win_tab), _translate("MainWindow", "Wind Velocity Range"))
        self.Weather_sum_6.setText(_translate("MainWindow", "Ground Temperature (Monthly Average)"))
        self.Location_6.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_6.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_6.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_38.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.Grd_tab), _translate("MainWindow", "Ground Temperature"))
        self.Weather_sum_7.setText(_translate("MainWindow", "Hourly Colormap (DBT)"))
        self.Location_7.setText(_translate("MainWindow", "Location:"))
        self.Lat_Log_7.setText(_translate("MainWindow", "Latitude/Longitude:"))
        self.Ele_TZ_7.setText(_translate("MainWindow", "Elevation / Time zone:"))
        self.label_44.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.Hou_tab), _translate("MainWindow", "Hourly Colormap"))
        #self.Weather_sum_8.setText(_translate("MainWindow", "3D Charts"))
        #self.Location_8.setText(_translate("MainWindow", "Location:"))
        #self.Lat_Log_8.setText(_translate("MainWindow", "Latitude/Longitude:"))
        #self.Ele_TZ_8.setText(_translate("MainWindow", "Elevation / Time zone:"))
        #self.label_50.setText(_translate("MainWindow", "LEGEND"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.D_tab), _translate("MainWindow", "3D Plot"))
        self.Weather_sum_9.setText(_translate("MainWindow", "Bioclimatic Design Chart"))

        self.Location_9.setText(_translate("MainWindow", "Location:"))

        self.Lat_Log_9.setText(_translate("MainWindow", "Latitude/Longitude:"))

        self.Ele_TZ_9.setText(_translate("MainWindow", "Elevation / Time zone:"))

        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.Psy_tab), _translate("MainWindow", "Bioclimatic Design Chart"))
        self.WFS_tab.setTabText(self.WFS_tab.indexOf(self.Recom_tab), _translate("MainWindow", "Design Recommendations "))

    def retranslateUi_input(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passive Design Consultant"))
        self.label_10.setStatusTip(_translate("MainWindow", "select weather file"))
        self.label_10.setText(_translate("MainWindow", "Select Weather Data File"))
        self.select_butt.setText(_translate("MainWindow", "Select Indian Composite Climate city Weather File"))
        self.browse_butt.setText(_translate("MainWindow", "Browse Existing EPW Weather file"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passive Design Consultant"))
        self.label_10.setStatusTip(_translate("MainWindow", "select weather file"))
        self.label_10.setText(_translate("MainWindow", "Select Weather Data File"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionChange_weather_data.setText(_translate("MainWindow", "Select other data file"))
        self.actionTerms_of_use.setText(_translate("MainWindow", "Terms of use"))
        self.actionUser_help.setText(_translate("MainWindow", "User help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

class myCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure(figsize=(20, 16), dpi=100)
        FigureCanvas.__init__(self, self.fig)

    def temp_plot(self, text, data):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        self.ax1 = self.fig.add_subplot()
        labels = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.ax1.violinplot([data[:744],data[744:1416],data[1416:2160],data[2160:2880],data[2880:3624],data[3624:4344],data[4344:5088],data[5088:5832],data[5832:6552],data[6552:7296],data[7296:8016],data[8016:8760]], points=40, widths=0.5, showmeans=True, showextrema=True, showmedians=False, bw_method='silverman')
        self.ax1.set_xticks(np.arange(1, len(labels) + 1))
        self.ax1.set_xticklabels(labels)
        self.ax1.set_xlabel('Month')
        self.ax1.grid(True, zorder = 0)
        if text == "DBT":
            self.ax1.set_title('Dry Bulb Temperature')
            self.ax1.set_ylabel('Temperature $°C$')
        if text == "WBT":
            self.ax1.set_title('Wet Bulb Temperature')
            self.ax1.set_ylabel('Temperature $°C$')
        if text == "DPT":
            self.ax1.set_title('Dew Point Temperature')
            self.ax1.set_ylabel('Temperature $°C$')
        self.draw()

    def radia_plot(self, text, data1):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        self.ax2 = self.fig.add_subplot()
        labels = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.ax2.violinplot(data1, points=40, widths=0.5, showmeans=True, showextrema=True, showmedians=False, bw_method='silverman')
        self.ax2.set_xticks(np.arange(1, len(labels) + 1))
        self.ax2.set_xticklabels(labels)
        self.ax2.grid(True, zorder=0)
        if text == "GHR":
            self.ax2.set_ylabel('Radiation $Wh/m^2$')
            self.ax2.set_title('Global Horizontal Radiation')
        if text == "DNR":
            self.ax2.set_ylabel('Radiation $Wh/m^2$')
            self.ax2.set_title('Direct Normal Radiation')
        if text == "DR":
            self.ax2.set_ylabel('Radiation $Wh/m^2$')
            self.ax2.set_title('Diffused Horizontal Radiation')
        self.draw()

    def illumi_plot(self, text, data2):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        self.ax3 = self.fig.add_subplot()
        self.ax3.grid(True, zorder=0)
        labels = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.ax3.violinplot(data2, points=40, widths=0.5, showmeans=True, showextrema=True, showmedians=False, bw_method='silverman')
        self.ax3.set_xticks(np.arange(1, len(labels) + 1))
        self.ax3.set_xticklabels(labels)
        if text == "DNI":
            self.ax3.set_ylabel('Illumination $Lux$')
            self.ax3.set_title('Direct Normal Illumination')
        if text == "GHI":
            self.ax3.set_ylabel('Illumination $Lux$')
            self.ax3.set_title('Global Horizontal Illumination')
        self.draw()

    def windv_plot(self, data3):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        self.ax4 = self.fig.add_subplot()
        self.ax4.grid(True, zorder=0)
        labels = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.ax4.violinplot([data3[:744], data3[744:1416], data3[1416:2160], data3[2160:2880], data3[2880:3624], data3[3624:4344],data3[4344:5088], data3[5088:5832], data3[5832:6552], data3[6552:7296], data3[7296:8016], data3[8016:8760]], points=40, widths=0.5, showmeans=True, showextrema=True, showmedians=False, bw_method='silverman')
        self.ax4.set_xticks(np.arange(1, len(labels) + 1))
        self.ax4.set_xticklabels(labels)
        self.ax4.set_ylabel('Velocity $m/s$')
        self.draw()

    def grd_plot(self, data4, data5, data6):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        self.ax5 = self.fig.add_subplot()
        self.ax5.grid(True, zorder=0)
        labels = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        self.ax5.plot(labels, [data4[0], data4[1], data4[2], data4[3], data4[4], data4[5], data4[6], data4[7], data4[8], data4[9], data4[10], data4[11]],  ".-", labels, [data5[0], data5[1], data5[2], data5[3], data5[4], data5[5], data5[6], data5[7], data5[8], data5[9], data5[10], data5[11]], "*-", labels,[data6[0], data6[1], data6[2], data6[3], data6[4], data6[5], data6[6], data6[7], data6[8], data6[9], data6[10], data6[11]], "o-")
        self.ax5.set_ylabel('Temperature $°C$')
        self.draw()

    def hour_plot(self, data7):
        self.fig.clear()
        self.fig.set_tight_layout("pad")
        ax6 = self.fig.add_subplot()
        ax6.set_ylabel('Hour')
        ax6.grid(True, zorder=5)
        cax = ax6.imshow(data7, interpolation='sinc', cmap=cm.coolwarm, aspect = 'auto', origin='lower', filternorm=True)

        ax6.xaxis.set_major_locator(ticker.IndexLocator(base=30.4166, offset=0.5))
        ax6.xaxis.set_minor_locator(ticker.IndexLocator(base=30.4166, offset=15.5))
        ax6.xaxis.set_major_formatter(ticker.NullFormatter())
        ax6.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
        ax6.yaxis.set_major_locator(ticker.IndexLocator(base=2, offset=0))
        ax6.yaxis.set_major_formatter(ticker.FixedFormatter(
            ['0 a.m.', '2 a.m.', '4 a.m.', '6 a.m.', '8 a.m.', '10 a.m.', '12 noon', '2 p.m.', '4 p.m.', '6 p.m.',
             '8 p.m.', '10 p.m.', '12 p.m.']))
        for tick in ax6.xaxis.get_minor_ticks():
            tick.tick1line.set_markersize(0)
            tick.tick2line.set_markersize(0)
            tick.label1.set_horizontalalignment('center')

        cbar = self.fig.colorbar(cax, ticks=[5, 15, 25, 35, 40])
        cbar.ax.set_yticklabels(["5°C", "15°C", "25°C", "35°C", "40°C"])
        self.draw()

    def psycho_plot(self, dbt, rh, w, altitude, tem, hum, text, comf, epw, evap, thm, sun, points, dbt_can_comf, rh_can_comf, dbt_out_comf, rh_out_comf, dbt_comf, rh_comf, c):
        self.fig.clear()
        self.fig.clear()
        ax8 = self.fig.add_subplot()
        import psychrolib
        import chart
        psychrolib.SetUnitSystem(psychrolib.SI)

        custom_style = {
            "figure": {
                #"figsize": [12, 12],
                "base_fontsize": 40,
                "title": "",
                #"title": "PSYCHROMETRIC CHART " + "(Altitude = " + str(altitude) + " m)",
                "x_label": "Dry-bulb temperature, $°C$",
                "y_label": "Humidity ratio $w, g_w / kg_{da}$",
                "x_axis": {"color": [0.2, 0.2, 0.2], "linewidth": 2, "linestyle": "-"},
                "x_axis_labels": {"color": [0.2, 0.2, 0.2], "fontsize": 10},
                "y_axis": {"color": [0.3, 0.3, 0.3], "linewidth": 2, "linestyle": "-"},
                "y_axis_labels": {"color": [0.3, 0.3, 0.3], "fontsize": 10},
                "x_axis_ticks": {"direction": "out", "color": [0.2, 0.2, 0.2]},
                "y_axis_ticks": {"direction": "out", "color": [0.3, 0.3, 0.3]},
                "partial_axis": True,
                "position": [0.025, 0.075, 0.925, 0.875]
            },
            "limits": {
                "range_temp_c": tem,
                "range_humidity_g_kg": hum,
                "altitude_m": altitude,
                "step_temp": .5
            },

            "saturation": {"color": [0, .3, 1.], "linewidth": 1, "linestyle": "-"},
            "constant_rh": {"color": [0.0, 0.498, 1.0, .7], "linewidth": 1, "linestyle": ":"},
            "constant_v": {"color": [0.0, 0.502, 0.337], "linewidth": 1, "linestyle": "--"},
            "constant_h": {"color": [0.251, 0.0, 0.502], "linewidth": 1, "linestyle": "--"},
            "constant_wet_temp": {"color": [0.498, 0.875, 1.0], "linewidth": 1, "linestyle": "-."},
            "constant_dry_temp": {"color": [0.855, 0.145, 0.114], "linewidth": 1, "linestyle": ":"},
            "constant_humidity": {"color": [0.0, 0.125, 0.376], "linewidth": 1, "linestyle": ":"},

            "chart_params": {
                "with_constant_rh": True,
                "constant_rh_label": "Constant relative humidity",
                "constant_rh_curves": [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "constant_rh_labels": [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "constant_rh_labels_loc": 0.95,

                "with_constant_v": False,
                "constant_v_label": "Constant specific volume",
                "constant_v_step": 0.02,
                "range_vol_m3_kg": [0.78, 1.22],
                "constant_v_labels": [0.86, 0.90, ],
                "constant_v_labels_loc": 1,

                "with_constant_h": False,
                "constant_h_label": "Constant enthalpy",
                "constant_h_step": 10,
                "range_h": [5, 155],
                "constant_h_labels": [5, 15, 25, 65],
                "constant_h_labels_loc": 1,

                "with_constant_wet_temp": True,
                "constant_wet_temp_label": "Constant wet bulb temperature",
                "constant_wet_temp_step": 5,
                "range_wet_temp": [-10, 45],
                "constant_wet_temp_labels": [0, 5, 10, 15, 20, 25, 30, 35],
                "constant_wet_temp_labels_loc": 0.05,

                "with_constant_dry_temp": True,
                "constant_temp_label": "Dry bulb temperature",
                "constant_temp_step": 5,
                "constant_temp_label_step": 5,
                "constant_temp_label_include_limits": True,

                "with_constant_humidity": True,
                "constant_humid_label": "Absolute humidity",
                "constant_humid_step": 4,
                "constant_humid_label_step": 4,
                "constant_humid_label_include_limits": True,

                "with_zones": False,
            }
        }
        chart_custom_2 = chart.PsychroChart(custom_style)
        chart_custom_2.plot(ax8)


        if comf == 1 or comf == 0:
            zones_comf_P = {
                "zones": [
                    {  # upper_line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[0], points[1]],
                        "points_y": [points[2], points[3]],
                        "label": ""
                    },
                    {  # lower _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[4], points[5]],
                        "points_y": [points[6], points[7]],
                        "label": ""
                    },
                    {  # left _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[8], points[9]],
                        "points_y": [points[10], points[11]],
                        "label": ""
                    },
                    {  # right _line
                        "zone_type": "dbt-rh",
                        "style": {"edgecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "facecolor": [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                                  "linewidth": 3,
                                  "linestyle": "-"},
                        "points_x": [points[12], points[13]],
                        "points_y": [points[14], points[15]],
                        "label": ""
                    }

                ]}

            points_comf = {
                'point_10_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                              'marker': '.', 'markersize': 3},
                    'xy': (points[16], points[17])},
                'point_11_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[18], points[19])}
            }

            connectors_comf = [
                {'start': 'point_10_name',
                 'end': 'point_11_name',
                 'style': {'color': [0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0],
                           "linewidth": 3, "linestyle": "-"}},
            ]


            # plot of comfort zone
            chart_custom_2.append_zones(zones_comf_P)
            chart_custom_2.plot(ax8)
            chart_custom_2.plot_points_dbt_rh(points_comf, connectors_comf)

        if thm == 1:
            points_t = {
                'point_6_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[20], points[21])},
                'point_7_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[22], points[23])},
                'point_8_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[24], points[25])},
                'point_9_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[26], points[27])}
            }

            connectors_t = [
                {'start': 'point_6_name',
                 'end': 'point_7_name',
                 'style'
                 : {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_7_name',
                 'end': 'point_9_name',
                 'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_8_name',
                 'end': 'point_9_name',
                 'style': {'color': [1.0, 0.8431372549019608, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}}

            ]
            chart_custom_2.plot_points_dbt_rh(points_t, connectors_t)
        #evap points[28.5, 80, 50, 14.43, 18, 20, 50, .0001]
        #evap points[30, 80, 50, 17.47, 18, 20, 50, .0001]
        #evap points[31, 80, 50, 19.6, 18, 20, 50, .0001]
        if evap == 1:
            points_evap = {
                'point_1_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[28], points[29])},
                'point_3_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[30], points[31])},
                'point_4_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[32], points[33])},
                'point_5_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                              'marker': '.', 'markersize': 2},
                    'xy': (points[34], points[35])}

            }

            connectors_evap = [
                {'start': 'point_1_name',
                 'end': 'point_3_name',
                 'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_4_name',
                 'end': 'point_5_name',
                 'style': {'color': [0.0, 0.5019607843137255, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}}
            ]
            chart_custom_2.plot_points_dbt_rh(points_evap, connectors_evap)
        #[28.5, 80, 39.587, 43.129, 39.587, 8.433, 24.34, 20]
        #[30, 80, 39.862, 46.344, 39.862, 8.310, 24.34, 20]
        #[31, 80, 40.212, 48.165, 40.212, 8.156, 24.34, 20]
        if sun == 1:
            points_sun = {
                'point_12_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.', 'markersize': 3},
                    'xy': (points[36], points[37])},
                'point_13_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[38], points[39])},
                'point_14_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[40], points[41])},
                'point_15_name': {
                    'label': 'label_for_legend',
                    'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                              'marker': '.',
                              'markersize': 3},
                    'xy': (points[42], points[43])}
            }

            connectors_sun = [
                {'start': 'point_12_name',
                 'end': 'point_13_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_13_name',
                 'end': 'point_14_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
                {'start': 'point_14_name',
                 'end': 'point_15_name',
                 'style': {'color': [1.0, 0.27058823529411763, 0.0, 1.0],
                           "linewidth": 2, "linestyle": "-"}},
            ]
            chart_custom_2.plot_points_dbt_rh(points_sun, connectors_sun)

        ################ EPW points all #############

        if c[0] != 0:
            points_comf_epw = {'points_series_name': (dbt_comf, rh_comf)}
            my_comf_style1 = {'s': 1, 'alpha': .8, 'color': 'lightblue'}
            chart_custom_2.plot_points_dbt_rh(points_comf_epw, scatter_style=my_comf_style1)
        if c[1] !=0 :
            points_can_comf_epw_0 = {'points_series_name': (dbt_can_comf[0], rh_can_comf[0])}
            my_comf_style2_0 = {'s': 1, 'alpha': .8, 'color': 'green'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_0, scatter_style=my_comf_style2_0)
        if c[2] != 0:
            points_can_comf_epw_1 = {'points_series_name': (dbt_can_comf[1], rh_can_comf[1])}
            my_comf_style2_1 = {'s': 1, 'alpha': .8, 'color': 'yellow'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_1, scatter_style=my_comf_style2_1)
        if c[3] != 0:
            points_can_comf_epw_2 = {'points_series_name': (dbt_can_comf[2], rh_can_comf[2])}
            my_comf_style2_2 = {'s': 1, 'alpha': .8, 'color': 'orange'}
            chart_custom_2.plot_points_dbt_rh(points_can_comf_epw_2, scatter_style=my_comf_style2_2)
        if epw == 1:
            if  c[4] != 0:
                points_out_comf_epw = {'points_series_name': (dbt_out_comf, rh_out_comf)}
                my_comf_style3 = {'s': 1, 'alpha': .8, 'color': 'red'}
                chart_custom_2.plot_points_dbt_rh(points_out_comf_epw, scatter_style=my_comf_style3)
        self.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



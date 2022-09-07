# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport
import os
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import pandas as pd
import sys
#import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QScreen


zoomIn_scale=0.5
zoomOut_scale=2
data1=[]
data2=[]
data3=[]

def print_widget(widget, filename):
    printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
    printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
    printer.setOutputFileName(filename)
    painter = QtGui.QPainter(printer)

    # start scale
    xscale = printer.pageRect().width() * 1.0 / widget.width()
    yscale = printer.pageRect().height() * 1.0 / widget.height()
    scale = min(xscale, yscale)
    painter.translate(printer.paperRect().center())
    painter.scale(scale, scale)
    painter.translate(-widget.width() / 2, -widget.height() / 2)
    # end scale

    widget.render(painter)
    painter.end()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SIGVIEW")
        MainWindow.resize(1238, 1008)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 610, 601, 291))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.graphicsView_3 = PlotWidget(self.verticalLayoutWidget_3)
        self.graphicsView_3.setStyleSheet("background: rgb(0,0,0)")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_3.addWidget(self.graphicsView_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 310, 601, 291))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.graphicsView_2 = PlotWidget(self.verticalLayoutWidget_4)
        self.graphicsView_2.setStyleSheet("background: rgb(0,0,0)")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_4.addWidget(self.graphicsView_2)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 601, 291))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.graphicsView = PlotWidget(self.verticalLayoutWidget_5)
        self.graphicsView.setStyleSheet("background: rgb(255,255,255)")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(630, 10, 591, 291))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_6.addWidget(self.checkBox_4)
 
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(630, 310, 591, 291))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_7.addWidget(self.checkBox_5)

        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(630, 610, 591, 291))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_8.addWidget(self.checkBox_6)
      
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_signal = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_signal.setObjectName("menuOpen_signal")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPlay_Navigate = QtWidgets.QMenu(self.menubar)
        self.menuPlay_Navigate.setObjectName("menuPlay_Navigate")
        self.menu3D_Tools = QtWidgets.QMenu(self.menubar)
        self.menu3D_Tools.setObjectName("menu3D_Tools")
        self.menuSpectrogram = QtWidgets.QMenu(self.menu3D_Tools)
        self.menuSpectrogram.setObjectName("menuSpectrogram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        
        self.actionleft = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("E:\CUFE\Scroll_Left.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionleft.setIcon(icon6)
        self.actionright = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()

        icon7.addPixmap(QtGui.QPixmap("E:\CUFE\Scroll_Right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionright.setIcon(icon7)
        self.actionup = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionup.setIcon(icon8)
        self.actiondown = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondown.setIcon(icon9)
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPlay_Signal = QtWidgets.QAction(MainWindow)
        self.actionPlay_Signal.setObjectName("actionPlay_Signal")
        self.actionzoomIn = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/EGYPT_LAPTOP/Downloads/zoom_in_alt-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Zoom In.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionzoomIn.setIcon(icon)
        self.actionzoomIn.setObjectName("actionzoomIn")
        self.actionplay = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:\CUFE\Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionplay.setIcon(icon1)
        self.actionplay.setObjectName("actionplay")
        self.actionstop = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\CUFE\Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionstop.setIcon(icon2)
        self.actionstop.setObjectName("actionstop")
        self.actionopen_signal = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("signal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("C:/Users/EGYPT_LAPTOP/Downloads/Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionopen_signal.setIcon(icon3)
        self.actionopen_signal.setObjectName("actionopen_signal")
        self.actionzoomOut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/EGYPT_LAPTOP/Downloads/zoom-out-2672773-2217490.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionzoomOut.setIcon(icon4)
        self.actionzoomOut.setObjectName("actionzoomOut")
        self.actionspect = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/EGYPT_LAPTOP/Downloads/download (8).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionspect.setIcon(icon5)
        self.actionspect.setObjectName("actionspect")
        self.actionChannel1 = QtWidgets.QAction(MainWindow)
        self.actionChannel1.setObjectName("actionChannel1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_4 = QtWidgets.QAction(MainWindow)
        self.actionChannel_4.setObjectName("actionChannel_4")
        self.actionChannel_5 = QtWidgets.QAction(MainWindow)
        self.actionChannel_5.setObjectName("actionChannel_5")
        self.menuOpen_signal.addAction(self.actionChannel1)
        self.menuOpen_signal.addAction(self.actionChannel_2)
        self.menuOpen_signal.addAction(self.actionChannel_3)
        self.menuFile.addAction(self.menuOpen_signal.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuPlay_Navigate.addAction(self.actionPlay_Signal)
        self.menuSpectrogram.addAction(self.actionChannel_1)
        self.menuSpectrogram.addAction(self.actionChannel_4)
        self.menuSpectrogram.addAction(self.actionChannel_5)
        self.menu3D_Tools.addAction(self.menuSpectrogram.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPlay_Navigate.menuAction())
        self.menubar.addAction(self.menu3D_Tools.menuAction())
        self.toolBar.addAction(self.actionopen_signal)
        self.toolBar.addAction(self.actionplay)
        self.toolBar.addAction(self.actionstop)
        self.toolBar.addAction(self.actionzoomIn)
        self.toolBar.addAction(self.actionzoomOut)
        self.toolBar.addAction(self.actionspect)
        self.toolBar.addAction(self.actionleft)
        self.toolBar.addAction(self.actionright)
        self.toolBar.addAction(self.actionup)
        self.toolBar.addAction(self.actiondown)
        
        self.graphicsView.hide()
        self.graphicsView_2.hide()
        self.graphicsView_3.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()
       
        self.xmax_scale1=10
        self.xmin_scale1=0
        self.xmax_scale2=10
        self.xmin_scale2=0
        self.xmax_scale3=10
        self.xmin_scale3=0


        self.actionChannel1.triggered.connect(lambda: self.Open_file(1))
        self.actionChannel_2.triggered.connect(lambda: self.Open_file(2))
        self.actionChannel_3.triggered.connect(lambda: self.Open_file(3))

        self.actionzoomIn.triggered.connect(lambda:self.zoom_in(zoomIn_scale))
        self.actionzoomOut.triggered.connect(lambda:self.zoom_out(zoomOut_scale))
        self.actionplay.triggered.connect(lambda:self.play())
        self.actionstop.triggered.connect(lambda:self.pause_btn())
        self.actionspect.triggered.connect(lambda:self.spectrogram())

        self.actionSave_As.triggered.connect(lambda:self.Save_As_Pdf())
        self.actionleft.triggered.connect(self.move_left)
        self.actionright.triggered.connect(self.move_right)
     
        self.pen1=pg.mkPen((255,0,0) ,width = 3)
        self.pen2=pg.mkPen((0,255,0) ,width = 3)
        self.pen3=pg.mkPen((0,0,255) ,width = 3)
  
        self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
        self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
        self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_3.setText(_translate("MainWindow", "Ch3"))
        self.checkBox_2.setText(_translate("MainWindow", "Ch2"))
        self.checkBox.setText(_translate("MainWindow", "Ch1"))
        self.checkBox_4.setText(_translate("MainWindow", "Spect1"))
        self.checkBox_5.setText(_translate("MainWindow", "Spect2"))
        self.checkBox_6.setText(_translate("MainWindow", "Spect3"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_signal.setTitle(_translate("MainWindow", "Open signal"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuPlay_Navigate.setTitle(_translate("MainWindow", "Play"))
        self.menu3D_Tools.setTitle(_translate("MainWindow", "3D Tools"))
        self.menuSpectrogram.setTitle(_translate("MainWindow", "Spectrogram"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As PDF"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionPlay_Signal.setText(_translate("MainWindow", "Play Signal"))
        self.actionzoomIn.setText(_translate("MainWindow", "zoomIn"))
        self.actionzoomIn.setToolTip(_translate("MainWindow", "zoomIn"))
        self.actionzoomIn.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionzoomOut.setText(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setToolTip(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionplay.setText(_translate("MainWindow", "play"))
        self.actionplay.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionstop.setText(_translate("MainWindow", "stop"))
        self.actionstop.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionopen_signal.setText(_translate("MainWindow", "open_signal"))
        self.actionopen_signal.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionzoomOut.setText(_translate("MainWindow", "zoomOut"))
        self.actionzoomOut.setToolTip(_translate("MainWindow", "zoomOut"))
        self.actionspect.setText(_translate("MainWindow", "spect"))
        self.actionspect.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionleft.setToolTip(_translate("MainWindow", "Scroll_Left"))
        self.actionleft.setText(_translate("MainWindow", "Scroll_Left"))
        self.actionleft.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionright.setToolTip(_translate("MainWindow", "Scroll_Right"))
        self.actionright.setText(_translate("MainWindow", "Scroll_Right"))
        self.actionright.setShortcut(_translate("MainWindow", "Ctrl+R"))
  
        self.actionChannel1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionChannel_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionChannel_1.setText(_translate("MainWindow", "Spect1"))
        self.actionChannel_4.setText(_translate("MainWindow", "Spect2"))
        self.actionChannel_5.setText(_translate("MainWindow", "Spect3"))

        


        
        
    def spectrogram(self):
        
        if self.checkBox.isChecked():
            self.checkBox_4.show()
            self.spec = MplCanvas(self, width=1 , height=0.1)

            self.spec.axes.specgram(F1,900 ,cmap="jet") 
            self.verticalLayout_6.addWidget(self.spec)

            
        elif self.checkBox_2.isChecked():
            self.checkBox_5.show()
            self.spec = MplCanvas(self, width=1 , height=0.1)

            self.spec.axes.specgram(F2,900) 
            self.verticalLayout_7.addWidget(self.spec)
            
            
        
        elif self.checkBox_3.isChecked():
            self.checkBox_6.show()
            self.sc = MplCanvas(self, width=1 , height=0.1)

            self.sc.axes.specgram(F3,900) 
            self.verticalLayout_8.addWidget(self.sc)

            
    def play(self):
        if self.checkBox.isChecked():
            self.timer1 =pg.QtCore.QTimer()
            self.timer1.setInterval(50)
            self.timer1.timeout.connect(self.update)
            self.timer1.start(500)
        elif self.checkBox_2.isChecked():
            self.timer2 =pg.QtCore.QTimer()
            self.timer2.setInterval(50)
            self.timer2.timeout.connect(self.update)
            self.timer2.start(500)
        elif self.checkBox_3.isChecked():
            self.timer3 =pg.QtCore.QTimer()
            self.timer3.setInterval(50)
            self.timer3.timeout.connect(self.update)
            self.timer3.start(500)

    def Open_file(self,flag):
        global F1, F2, F3,data2, data3, data1, time
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None,"Open File", r"\Signals","Signals(*.csv)", options=options)
        data_set=pd.read_csv(fileName,header=1)
        data_set=data_set[1:].astype(float)
        File =data_set.iloc[:,0]
        
        data =[]
        time =[]
        
        for i in range(1,(len(File)+1)):
            data.append(File[i])

    
        
        for i in range(0,(len(File))):
            time.append(i)

        
        if flag == 1:
            F1=File
            data1=data
            self.graphicsView.setXRange(self.xmin_scale1,self.xmax_scale1)
            self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
            self.checkBox.show()
            self.graphicsView.show()
           
        elif flag == 2:
            F2=File
            data2=data
            self.graphicsView_2.setXRange(self.xmin_scale2,self.xmax_scale2)
            self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
            self.checkBox_2.show()
            self.graphicsView_2.show()
            
        else :
            F3=File
            data3=data
            self.graphicsView_3.setXRange(self.xmin_scale3,self.xmax_scale3)
            self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]
            self.checkBox_3.show()
            self.graphicsView_3.show()
    
    def update(self):
        if self.checkBox.isChecked():
            self.x_range1[0]=self.x_range1[0]+1
            self.x_range1[1]=self.x_range1[1]+1
            self.graphicsView.plot(time,data1,pen=self.pen1)
            self.graphicsView.setXRange(self.x_range1[0],self.x_range1[1])
            
        elif self.checkBox_2.isChecked():
            self.x_range2[0]=self.x_range2[0]+1
            self.x_range2[1]=self.x_range2[1]+1
            self.graphicsView_2.plot(time,data2,pen=self.pen2)
            self.graphicsView_2.setXRange(self.x_range2[0],self.x_range2[1])
            
        elif self.checkBox_3.isChecked():
            self.x_range3[0]=self.x_range3[0]+1
            self.x_range3[1]=self.x_range3[1]+1
            self.graphicsView_3.plot(time,data3,pen=self.pen3)
            self.graphicsView_3.setXRange(self.x_range3[0],self.x_range3[1])

    def zoom_in(self,val):
        if self.checkBox.isChecked():
            self.x_range1[1]=self.x_range1[1]*val
            self.x_range1[0]=self.x_range1[0]*val
            self.graphicsView.setXRange(self.x_range1[0],self.x_range1[1])
            self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
        elif self.checkBox_2.isChecked():
            self.x_range2[1]=self.x_range2[1]*val
            self.x_range2[0]=self.x_range2[0]*val
            self.graphicsView_2.setXRange(self.x_range2[0],self.x_range2[1])
            self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
        elif self.checkBox_3.isChecked():
            self.x_range3[1]=self.x_range3[1]*val
            self.x_range3[0]=self.x_range3[0]*val
            self.graphicsView_3.setXRange(self.x_range3[0],self.x_range3[1])
            self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]

    def zoom_out(self,val):

        if self.checkBox.isChecked():
            self.x_range1[1]=self.x_range1[1]*val
            self.x_range1[0]=self.x_range1[0]*val
            self.graphicsView.setXRange(self.x_range1[0],self.x_range1[1])
            self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
        elif self.checkBox_2.isChecked():
            self.x_range2[1]=self.x_range2[1]*val
            self.x_range2[0]=self.x_range2[0]*val
            self.graphicsView_2.setXRange(self.x_range2[0],self.x_range2[1])
            self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
        elif self.checkBox_3.isChecked():
            self.x_range3[1]=self.x_range3[1]*val
            self.x_range3[0]=self.x_range3[0]*val
            self.graphicsView_3.setXRange(self.x_range3[0],self.x_range3[1])
            self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]


    def pause_btn(self):
        if self.checkBox.isChecked():
            self.timer1.stop()
        elif self.checkBox_2.isChecked():
            self.timer2.stop()
        elif self.checkBox_3.isChecked():
            self.timer3.stop()

    def Save_As_Pdf(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"

            print_widget(self.centralwidget, fn)


    def move_left(self):
        if self.checkBox.isChecked():
            self.x_range1[1]=self.x_range1[1]-4
            self.x_range1[0]=self.x_range1[0]-4
            self.graphicsView.setXRange(self.x_range1[0],self.x_range1[1])
            self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
        elif self.checkBox_2.isChecked():
            self.x_range2[1]=self.x_range2[1]-4
            self.x_range2[0]=self.x_range2[0]-4
            self.graphicsView_2.setXRange(self.x_range2[0],self.x_range2[1])
            self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
        elif self.checkBox_3.isChecked():
            self.x_range3[1]=self.x_range3[1]-4
            self.x_range3[0]=self.x_range3[0]-4
            self.graphicsView_3.setXRange(self.x_range3[0],self.x_range3[1])
            self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]


    def move_right(self):

        if self.checkBox.isChecked():
            self.x_range1[1]=self.x_range1[1]+4
            self.x_range1[0]=self.x_range1[0]+4
            self.graphicsView.setXRange(self.x_range1[0],self.x_range1[1])
            self.x_range1=self.graphicsView.getViewBox().state['viewRange'][0]
        elif self.checkBox_2.isChecked():
            self.x_range2[1]=self.x_range2[1]+4
            self.x_range2[0]=self.x_range2[0]+4
            self.graphicsView_2.setXRange(self.x_range2[0],self.x_range2[1])
            self.x_range2=self.graphicsView_2.getViewBox().state['viewRange'][0]
        elif self.checkBox_3.isChecked():
            self.x_range3[1]=self.x_range3[1]+4
            self.x_range3[0]=self.x_range3[0]+4
            self.graphicsView_3.setXRange(self.x_range3[0],self.x_range3[1])
            self.x_range3=self.graphicsView_3.getViewBox().state['viewRange'][0]



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
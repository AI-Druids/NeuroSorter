# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sorter_mpl.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from QTDesigner.mplwidget import MplWidget

class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(1334, 847)
        MainWindows.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindows.setStyleSheet("")
        MainWindows.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.windows_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.windows_tabWidget.setObjectName("windows_tabWidget")
        self.principal_tab = QtWidgets.QWidget()
        self.principal_tab.setObjectName("principal_tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.principal_tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.controlsGroup_verticalLayout = QtWidgets.QVBoxLayout()
        self.controlsGroup_verticalLayout.setSpacing(6)
        self.controlsGroup_verticalLayout.setObjectName("controlsGroup_verticalLayout")
        self.external_groupBox = QtWidgets.QGroupBox(self.principal_tab)
        self.external_groupBox.setMinimumSize(QtCore.QSize(220, 60))
        self.external_groupBox.setMaximumSize(QtCore.QSize(200, 60))
        self.external_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.external_groupBox.setObjectName("external_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.external_groupBox)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_load = QtWidgets.QPushButton(self.external_groupBox)
        self.btn_load.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_load.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout_2.addWidget(self.btn_load)
        self.btn_save = QtWidgets.QPushButton(self.external_groupBox)
        self.btn_save.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_save.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.controlsGroup_verticalLayout.addWidget(self.external_groupBox)
        self.connect_groupBox = QtWidgets.QGroupBox(self.principal_tab)
        self.connect_groupBox.setMinimumSize(QtCore.QSize(220, 200))
        self.connect_groupBox.setMaximumSize(QtCore.QSize(200, 200))
        self.connect_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.connect_groupBox.setObjectName("connect_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.connect_groupBox)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.undo_btn = QtWidgets.QPushButton(self.connect_groupBox)
        self.undo_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.undo_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.undo_btn.setObjectName("undo_btn")
        self.gridLayout.addWidget(self.undo_btn, 4, 1, 1, 1)
        self.U2ID_comboBox = QtWidgets.QComboBox(self.connect_groupBox)
        self.U2ID_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.U2ID_comboBox.setObjectName("U2ID_comboBox")
        self.gridLayout.addWidget(self.U2ID_comboBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.connect_groupBox)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.connect_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.delete_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 4, 0, 1, 1)
        self.clean_btn = QtWidgets.QPushButton(self.connect_groupBox)
        self.clean_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.clean_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.clean_btn.setObjectName("clean_btn")
        self.gridLayout.addWidget(self.clean_btn, 5, 0, 1, 1)
        self.sorting_btn = QtWidgets.QPushButton(self.connect_groupBox)
        self.sorting_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.sorting_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.sorting_btn.setObjectName("sorting_btn")
        self.gridLayout.addWidget(self.sorting_btn, 5, 1, 1, 1)
        self.unit_comboBox = QtWidgets.QComboBox(self.connect_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_comboBox.sizePolicy().hasHeightForWidth())
        self.unit_comboBox.setSizePolicy(sizePolicy)
        self.unit_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.gridLayout.addWidget(self.unit_comboBox, 1, 1, 1, 1)
        self.channel_comboBox = QtWidgets.QComboBox(self.connect_groupBox)
        self.channel_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.channel_comboBox.setObjectName("channel_comboBox")
        self.gridLayout.addWidget(self.channel_comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.connect_groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.connect_groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.Threshold_Edit = QtWidgets.QLineEdit(self.connect_groupBox)
        self.Threshold_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Threshold_Edit.setObjectName("Threshold_Edit")
        self.gridLayout.addWidget(self.Threshold_Edit, 3, 1, 1, 1)
        self.threshold_btn = QtWidgets.QPushButton(self.connect_groupBox)
        self.threshold_btn.setObjectName("threshold_btn")
        self.gridLayout.addWidget(self.threshold_btn, 3, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.controlsGroup_verticalLayout.addWidget(self.connect_groupBox)
        self.log_groupBox = QtWidgets.QGroupBox(self.principal_tab)
        self.log_groupBox.setMinimumSize(QtCore.QSize(220, 200))
        self.log_groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.log_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.log_groupBox.setObjectName("log_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.log_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logger = QtWidgets.QPlainTextEdit(self.log_groupBox)
        self.logger.setReadOnly(True)
        self.logger.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logger.setObjectName("logger")
        self.verticalLayout_2.addWidget(self.logger)
        self.controlsGroup_verticalLayout.addWidget(self.log_groupBox)
        self.horizontalLayout_4.addLayout(self.controlsGroup_verticalLayout)
        self.signals_groupBox = QtWidgets.QGroupBox(self.principal_tab)
        self.signals_groupBox.setObjectName("signals_groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.signals_groupBox)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MplWidget = MplWidget(self.signals_groupBox)
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout_6.addWidget(self.MplWidget)
        self.horizontalLayout_4.addWidget(self.signals_groupBox)
        self.windows_tabWidget.addTab(self.principal_tab, "")
        self.others_tab = QtWidgets.QWidget()
        self.others_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.others_tab.setObjectName("others_tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.others_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 1311, 761))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.btn_run = QtWidgets.QPushButton(self.groupBox)
        self.btn_run.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.btn_run.setObjectName("btn_run")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 281, 691))
        self.listWidget_3.setObjectName("listWidget_3")
        self.btn_save_changes = QtWidgets.QPushButton(self.groupBox)
        self.btn_save_changes.setGeometry(QtCore.QRect(160, 30, 111, 23))
        self.btn_save_changes.setObjectName("btn_save_changes")
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.RawCode = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.RawCode.setGeometry(QtCore.QRect(10, 30, 991, 721))
        self.RawCode.setObjectName("RawCode")
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.windows_tabWidget.addTab(self.others_tab, "")
        self.horizontalLayout_6.addWidget(self.windows_tabWidget)
        MainWindows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1334, 20))
        self.menubar.setObjectName("menubar")
        MainWindows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        self.windows_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "PySorter"))
        self.external_groupBox.setTitle(_translate("MainWindows", "File"))
        self.btn_load.setText(_translate("MainWindows", "Load"))
        self.btn_save.setText(_translate("MainWindows", "Save"))
        self.connect_groupBox.setTitle(_translate("MainWindows", "Manual curation"))
        self.undo_btn.setText(_translate("MainWindows", "Undo"))
        self.label.setText(_translate("MainWindows", "SelectedUnit2ID"))
        self.delete_btn.setText(_translate("MainWindows", "Delete"))
        self.clean_btn.setText(_translate("MainWindows", "Clean"))
        self.sorting_btn.setText(_translate("MainWindows", "Sorting"))
        self.label_2.setText(_translate("MainWindows", "ChannelID"))
        self.label_3.setText(_translate("MainWindows", "UnitID"))
        self.Threshold_Edit.setText(_translate("MainWindows", "[-300, 300]"))
        self.threshold_btn.setText(_translate("MainWindows", "Set Threshold"))
        self.log_groupBox.setTitle(_translate("MainWindows", "Log viewer"))
        self.signals_groupBox.setTitle(_translate("MainWindows", "Spike waveforms"))
        self.windows_tabWidget.setTabText(self.windows_tabWidget.indexOf(self.principal_tab), _translate("MainWindows", "Spikes_View"))
        self.groupBox.setTitle(_translate("MainWindows", "CUSTOM SCRIPTS"))
        self.btn_run.setText(_translate("MainWindows", "RUN SCRIPT"))
        self.btn_save_changes.setText(_translate("MainWindows", "SAVE CHANGES"))
        self.groupBox_2.setTitle(_translate("MainWindows", "PYTHON RAW CODE"))
        self.windows_tabWidget.setTabText(self.windows_tabWidget.indexOf(self.others_tab), _translate("MainWindows", "Others"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindows = QtWidgets.QMainWindow()
#     ui = Ui_MainWindows()
#     ui.setupUi(MainWindows)
#     MainWindows.show()
#     sys.exit(app.exec_())


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1163, 842)
        self.main_window = QtWidgets.QWidget(parent=MainWindow)
        self.main_window.setStyleSheet("""
            /* Info Frame Styles */
            #info_frame {
                background-color: #fff;
                border: none;
                border-radius: 5px;
            }

            #info_frame QLabel,
            #info_frame QLineEdit,
            #info_frame QComboBox,
            #function_frame QPushButton,
            QHeaderView::section {
                font-family: 'Segoe UI Semibold';
                font-size: 12px;
                color: #000;
            }

            #info_frame QLineEdit,
            #info_frame QComboBox {
                padding: 4px 5px;
                border: 1px solid #838383;
                border-radius: 2px;
            }

            #info_frame QLineEdit:focus,
            #info_frame QComboBox:focus {
                border-color: #0055ff;
            }

            /* ComboBox Styles */
            QComboBox::drop-down { 
                background: transparent; 
                border: none;
                margin-right: 5px;
            } 

            QComboBox::down-arrow {
                image: url(./icons/expand_more.svg);
            }

            /* Result Frame Styles */
            #result_frame {
                border-radius: 5px;
                background-color: #fff;
            }

            /* Table Styles */
            QTableWidget::Item {
                border-bottom: 1px solid #d0c6ff;
                color: black;
                padding-left: 3px;
            }

            /* Function Frame Button Styles */
            #function_frame QPushButton {
                font-size: 14px;
                padding: 5px 10px;
                border: 2px solid #f0f0f0;
                border-radius: 5px;
                background-color: #84e8f7;
            }

            #function_frame QPushButton:hover {
                border-color: #4c96f7;
                font-size: 15px;
            }

            #function_frame #delete_btn {
                background-color: #ff8183;
            }

            #function_frame #delete_btn:hover {
                border-color: #dc0004;
            }
        """)

        self.main_window.setObjectName("main_window")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.main_window)
        self.gridLayout_6.setContentsMargins(20, 10, 20, 20)
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(parent=self.main_window)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.title_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout_4.addWidget(self.title_label, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.info_frame = QtWidgets.QFrame(parent=self.main_window)
        self.info_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout_3.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_3.setHorizontalSpacing(50)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setMaxLength(11)
        self.gridLayout.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.info_frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.info_frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.info_frame, 1, 0, 1, 1)
        self.function_frame = QtWidgets.QFrame(parent=self.main_window)
        self.function_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout.setContentsMargins(30, 20, 30, 20)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add .svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/update.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.update_btn.setIcon(icon1)
        self.update_btn.setIconSize(QtCore.QSize(20, 20))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.select_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/select.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.select_btn.setIcon(icon2)
        self.select_btn.setIconSize(QtCore.QSize(20, 20))
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.search_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.clear_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clear_btn.setIcon(icon4)
        self.clear_btn.setIconSize(QtCore.QSize(20, 20))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.delete_btn = QtWidgets.QPushButton(parent=self.function_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setIconSize(QtCore.QSize(20, 20))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.gridLayout_6.addWidget(self.function_frame, 2, 0, 1, 1)
        self.table_frame = QtWidgets.QFrame(parent=self.main_window)
        self.table_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.table_frame.setObjectName("table_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.table_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.table_frame)
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        # Set column widths
        self.tableWidget.setColumnWidth(0, 200)  # Student ID
        self.tableWidget.setColumnWidth(1, 200)  # First Name
        self.tableWidget.setColumnWidth(2, 200)  # Last Name
        self.tableWidget.setColumnWidth(3, 200)  # Email
        self.tableWidget.setColumnWidth(4, 200)  # Phone Number
        self.tableWidget.setColumnWidth(5, 200)  # Address
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setStyleSheet("alternate-background-color: #f0f0f0;")
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.table_frame, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_window)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Managment App", "Managment App"))
        MainWindow.setWindowIcon(QtGui.QIcon("icons/management.png"))
        self.title_label.setText(_translate("MainWindow", "Students Information System"))
        self.label_2.setText(_translate("MainWindow", "Student ID"))
        self.label_3.setText(_translate("MainWindow", "First Name"))
        self.label_6.setText(_translate("MainWindow", "Last name"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.label_8.setText(_translate("MainWindow", "Phone"))
        self.label_7.setText(_translate("MainWindow", "Address"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.select_btn.setText(_translate("MainWindow", "Select"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

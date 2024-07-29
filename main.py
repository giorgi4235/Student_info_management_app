# import necessary moduls
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QLabel, QMessageBox, QTableWidgetItem, QMainWindow
from PyQt6.QtGui import QIntValidator

# import the ui and database connection class
from main_ui import Ui_MainWindow
import database as db

# main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connect ui elements to class variables
        self.student_id = self.ui.lineEdit_6
        #restrict input to integer
        self.student_id.setValidator(QIntValidator())

        self.first_name = self.ui.lineEdit_4
        self.last_name = self.ui.lineEdit_5
        self.email = self.ui.lineEdit
        self.phone = self.ui.lineEdit_2
        self.address = self.ui.lineEdit_3


        #buttons
        self.add_btn = self.ui.add_btn
        self.update_btn = self.ui.update_btn
        self.select_btn = self.ui.select_btn
        self.search_btn = self.ui.search_btn
        self.clear_btn = self.ui.clear_btn
        self.delete_btn = self.ui.delete_btn

        #table
        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)

        # initialize signal-slot connections
        self.init_signal_slot()

        # Populate the initial data in the table and\
        self.load_data()

    # Connect buttons to the functions
    def init_signal_slot(self):
        #connect buttons to their functions
        self.add_btn.clicked.connect(self.add_info)
        self.update_btn.clicked.connect(self.update_info)
        self.select_btn.clicked.connect(self.select_info)
        self.search_btn.clicked.connect(self.search_info)
        self.clear_btn.clicked.connect(self.clear_info)
        self.delete_btn.clicked.connect(self.delete_info)

    def check_student_id(self):
        if self.student_id.isValid():
            self.student_id.setText(self.student_id.text())

    # Load information on Table from database
    def load_data(self):
        try:
            students = db.get_all_students()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(students):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(f"Error loading data: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")

    # Get infromation from input text
    def get_input_data(self):
        return{
            "student_id": self.student_id.text(),
            "first_name": self.first_name.text(),
            "last_name": self.last_name.text(),
            "email": self.email.text(),
            "phone": self.phone.text(),
            "address": self.address.text()
        }

    # Add new student
    def add_info(self):
        try:
            print("add button clicked")
            data = self.get_input_data()
            print(data)
            if all(data.values()):
                db.add_student(data["student_id"], data['first_name'], data['last_name'], data['email'], data['phone'], data["address"])
                print("student added in db")
                self.load_data()
            else:
                QMessageBox.warning(self.ui.main_window, "Error", "All fields must be filled")
        except Exception as e:
            print(f"Error adding info: {e}")


    #Update student information
    def update_info(self):
        data = self.get_input_data()
        if all(data.values()):
            db.update_student(data["student_id"], data['first_name'], data['last_name'], data['email'], data['phone'], data['address'])
            self.load_data()
        else:
            QMessageBox.warning(self.ui.main_window, "Error", "All fields must be filled")

    def select_info(self):
        selected_row = self.ui.tableWidget.currentRow()

        if selected_row < 0:
            # No row is selected
            return

        student_id_item = self.ui.tableWidget.item(selected_row, 0)
        first_name_item = self.ui.tableWidget.item(selected_row, 1)
        last_name_item = self.ui.tableWidget.item(selected_row, 2)
        email_item = self.ui.tableWidget.item(selected_row, 3)
        phone_item = self.ui.tableWidget.item(selected_row, 4)
        address_item = self.ui.tableWidget.item(selected_row, 5)

        self.student_id.setText(student_id_item.text() if student_id_item else "")
        self.first_name.setText(first_name_item.text() if first_name_item else "")
        self.last_name.setText(last_name_item.text() if last_name_item else "")
        self.email.setText(email_item.text() if email_item else "")
        self.phone.setText(phone_item.text() if phone_item else "")
        self.address.setText(address_item.text() if address_item else "")

        return student_id_item.text() if student_id_item else None

    def search_info(self):
        search_items = {
            "student_id": self.student_id.text().lower(),
            "first_name": self.first_name.text().lower(),
            "last_name": self.last_name.text().lower(),
            "email": self.email.text().lower(),
            "phone": self.phone.text().lower(),
            "address": self.address.text().lower()
        }

        for row in range(self.ui.tableWidget.rowCount()):
            match = True
            for col, key in enumerate(search_items):
                if search_items[key]:  # Only check non-empty search fields
                    item = self.ui.tableWidget.item(row, col)
                    if item is None or search_items[key] not in item.text().lower():
                        match = False
                        break
            self.ui.tableWidget.setRowHidden(row, not match)


    def clear_info(self):
        self.student_id.setText("")
        self.first_name.setText("")
        self.last_name.setText("")
        self.email.setText("")
        self.phone.setText("")
        self.address.setText("")


    def delete_info(self):
        try:
            student = self.select_info()
            print(student)
            if student:
                db.delete_student(student)
            elif not student:
                QMessageBox.warning(self.ui.main_window, "Error", "No student selected")
            else:
                QMessageBox.warning(self.ui.main_window, "Error", "Something went wrong")
        except Exception as e:
            print(f"Error deleting info: {e}")
        finally:
            self.load_data()




# app entry
if __name__ == '__main__':
    app = QApplication(sys.argv)
    db.create_table()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())




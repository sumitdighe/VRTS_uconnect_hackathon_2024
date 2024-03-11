import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox


def show_permission_dialog():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Permission Required")
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setText("Do you want to give permission to access log data?")
    msg_box.setInformativeText("Granting permission will allow the application to access log data, which may contain sensitive information.")
    msg_box.addButton(QMessageBox.Yes)
    msg_box.addButton(QMessageBox.No)
    msg_box.setDefaultButton(QMessageBox.Yes)
    msg_box.setWindowModality(2)  # WindowModal

    result = msg_box.exec_()
    if result == QMessageBox.Yes:
        # Add code to run the application here
        command = 'python threadingCode.py'

        print("Running anomaly detector...")
        os.system(command)
    else:
        # Close the application or handle accordingly
        sys.exit()


def main():
    app = QApplication(sys.argv)
    show_permission_dialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget,QSizePolicy
from PyQt5.QtCore import Qt


class MoreInfoWindow(QWidget):
    def __init__(self, parent_position):
        super().__init__()
        self.setWindowTitle("More Info")
        self.setGeometry(parent_position.x(), parent_position.y() - 150, 300, 250)

        # Remove maximize button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        ok_button = QPushButton("OK")


        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Suspicious or unusual activity detected please review once.You are seeing this message because there is some unusual behavior in system.")
        msg_box.setInformativeText("Our system has flagged potential issues related to unusual disk activity, CPU utilization, or network parameters. Please review and address these aspects promptly to ensure optimal system performance.")

        # Set size policy to expanding
        msg_box.setSizeGripEnabled(True)
        msg_box.addButton(ok_button,QMessageBox.ActionRole)
        msg_box.setMinimumSize(250, 250)
        ok_button.clicked.connect(AnomalyPopup.handle_ok_button)

        layout.addWidget(msg_box)



class AnomalyPopup(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the initial size and title of the window
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Anomaly Detected')

        # Display the anomaly popup message box
        self.showPopup()

    def showPopup(self):
        # Create a QMessageBox instance for displaying the anomaly message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)  # Set the warning icon
        msg.setText("Anomaly Detected")
        msg.setInformativeText("An anomaly has been detected. Please take appropriate action.")
        msg.setWindowTitle("Anomaly Detected")

        # Add "View" and "OK" buttons to the message box
        view_button = QPushButton("View")
        ok_button = QPushButton("OK")
        msg.addButton(view_button, QMessageBox.ActionRole)
        msg.addButton(ok_button, QMessageBox.ActionRole)

        # Connect button clicks to their respective handler methods
        ok_button.clicked.connect(self.handle_ok_button)
        view_button.clicked.connect(self.handle_view_button)

        # Connect the acceptance of the message box (clicking OK) to closing the window
        msg.accepted.connect(self.close)

        # Display the message box
        msg.exec_()

    def handle_ok_button(self):
        # Handle OK button click - Quit the application
        QApplication.quit()

    def handle_view_button(self):
        # Handle View button click - Show the MoreInfoWindow
        self.more_info_window = MoreInfoWindow(self.center_position())
        self.more_info_window.show()

    def center_position(self):
        # Calculate the center position of the screen
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()
        center = screen_rect.center()
        return center


def main():
    app = QApplication(sys.argv)
    ex = AnomalyPopup()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
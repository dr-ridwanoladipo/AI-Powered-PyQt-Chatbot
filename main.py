import sys
import threading
import os
from dotenv import load_dotenv
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from PyQt6.QtCore import QMetaObject, Qt, Q_ARG
from backend import Chatbot

# Load environment variables from a .env file
load_dotenv()
api_key = os.getenv("API_KEY")


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot(api_key)
        self.setMinimumSize(700, 500)

        # Initialize UI components
        self.setup_ui()

        self.show()

    def setup_ui(self):
        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the send button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

    def send_message(self):
        user_input = self.input_field.text().strip()
        if not user_input:
            return  # Do nothing if input is empty

        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        # Use threading for API call to avoid blocking the UI
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        # Use thread-safe method to update the UI
        QMetaObject.invokeMethod(self.chat_area, "append", Qt.ConnectionType.QueuedConnection,
                                 Q_ARG(str, f"<p style='color:#333333; background-color: "
                                            f"#E9E9E9'>Bot: {response}</p>"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())
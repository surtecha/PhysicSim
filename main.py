import sys
import os
import importlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget, QLabel, QScrollArea, QSizePolicy, QGridLayout, QDialog, QHBoxLayout, QSpacerItem, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QPainter, QPainterPath

class SimulationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Multi-Physics Simulation Engine')

        layout = QVBoxLayout()  # Main layout for the window

        # Create tabs for each category
        tabs = QTabWidget()
        categories = ["Atomics", "Fluids", "Kinematics", "Gravitation", "Materials"]  # List of simulation categories

        # Add a tab for each category
        for category in categories:
            tabs.addTab(self.createCategory(category), category)

        layout.addWidget(tabs)  # Add tabs to the main layout
        self.setLayout(layout)  # Set the layout for the window

        self.applyDarkTheme()  # Apply dark theme to the application

        # Show the window in full screen
        self.showMaximized()

    def createCategory(self, category):
        """
        Create a widget for a simulation category with buttons to run each simulation.
        :param category: The name of the category (e.g., "Kinematics");
        :return: A QWidget containing the buttons for the category.
        """
        category_widget = QWidget()  # Create a new widget for the category
        layout = QGridLayout()  # Grid layout for the category widget

        # Path to the category folder
        folder_path = os.path.join(os.path.dirname(__file__), category)
        # List of python files in the category folder
        simulation_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

        # Set a fixed size for the buttons
        size = 300  # Adjust the button size to be larger

        # Create a button for each simulation file
        row = 0
        col = 0
        max_cols = 3  # Number of columns to be displayed

        for sim_file in simulation_files:
            sim_name = self.format_simulation_name(os.path.splitext(sim_file)[0])  # Extract and format the simulation name

            # Read the description file
            description_path = os.path.join(folder_path, f"{sim_file.split('.')[0]}_description.txt")
            if os.path.exists(description_path):
                with open(description_path, 'r') as file:
                    description = file.read().strip()
            else:
                description = "No description available."

            # Create and set up the button
            button = QPushButton()
            button.setFixedSize(size, size)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Load the image for the button
            image_path = os.path.join(folder_path, f"{sim_file.split('.')[0]}.jpg")
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path).scaled(size - 30, size - 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                rounded_pixmap = self.create_rounded_pixmap(pixmap, 10)
                button.setIcon(QIcon(rounded_pixmap))
                button.setIconSize(rounded_pixmap.size())

            # Connect the button click to the function that shows the description popup
            button.clicked.connect(lambda checked, c=category, s=sim_file, d=description: self.show_description_popup(c, s, d))

            # Style the button to center the icon and give it a modern look
            button.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 10px;
                    background-color: #2d2d30;
                }
                QPushButton:pressed {
                    background-color: #5a5a5f;
                }
                QPushButton:hover {
                    border: 2px solid #42a5f5;
                }
            """)

            # Create and set up the simulation name label
            name_label = QLabel(sim_name)
            name_label.setStyleSheet("QLabel { color : white; }")
            name_label.setAlignment(Qt.AlignHCenter)

            # Create a container widget for the button and label
            container = QWidget()
            vbox = QVBoxLayout(container)
            vbox.addWidget(button, alignment=Qt.AlignHCenter)
            vbox.addWidget(name_label, alignment=Qt.AlignHCenter)

            # Add the container to the layout
            layout.addWidget(container, row, col, alignment=Qt.AlignHCenter | Qt.AlignVCenter)

            col += 1
            if col == max_cols:
                col = 0
                row += 1

        # Add stretch factors to center the buttons
        for i in range(max_cols):
            layout.setColumnStretch(i, 1)
        layout.setRowStretch(row + 1, 1)

        category_widget.setLayout(layout)  # Set the layout for the category widget

        # Create a scroll area and set its widget to the category widget
        scroll_area = QScrollArea()
        scroll_area.setWidget(category_widget)
        scroll_area.setWidgetResizable(True)

        return scroll_area

    def create_rounded_pixmap(self, pixmap, radius):
        """
        Create a rounded pixmap with the specified radius.
        :param pixmap: The original pixmap to be rounded.
        :param radius: The radius for the rounded corners.
        :return: A new pixmap with rounded corners.
        """
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        path = QPainterPath()
        path.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded

    def format_simulation_name(self, sim_name):
        """
        Format the simulation name to be more readable.
        :param sim_name: The original simulation name (e.g., "example_code");
        :return: The formatted simulation name (e.g., "Example Code").
        """
        return ' '.join(word.capitalize() for word in sim_name.split('_'))

    def show_description_popup(self, category, sim_file, description):
        """
        Show a popup with the simulation description and a simulate button.
        :param category: The category of the simulation (e.g., "Kinematics").
        :param sim_file: The name of the simulation file (e.g., "projectile.py").
        :param description: The description of the simulation.
        """
        sim_name = self.format_simulation_name(os.path.splitext(sim_file)[0])
        dialog = QDialog(self)
        dialog.setWindowTitle(sim_name)
        dialog.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        description_label = QLabel(description)
        description_label.setWordWrap(True)
        description_label.setStyleSheet("QLabel { color : white; }")

        simulate_button = QPushButton("Simulate")
        simulate_button.clicked.connect(lambda: self.run_simulation_and_close(dialog, category, sim_file))

        layout.addWidget(description_label)
        layout.addWidget(simulate_button, alignment=Qt.AlignCenter)

        dialog.setLayout(layout)
        dialog.exec_()

    def run_simulation_and_close(self, dialog, category, sim_file):
        """
        Run the simulation and close the dialog.
        :param dialog: The dialog to close.
        :param category: The category of the simulation (e.g., "Kinematics").
        :param sim_file: The name of the simulation file (e.g., "projectile.py").
        """
        dialog.accept()  # Close the dialog
        self.run_simulation(category, sim_file)

    def run_simulation(self, category, sim_file):
        """
        Dynamically import and run the simulation function from the specified module.
        :param category: The category of the simulation (e.g., "Kinematics").
        :param sim_file: The name of the simulation file (e.g., "projectile.py").
        """
        sim_name = os.path.splitext(sim_file)[0]  # Extract the simulation name without the .py extension
        module_name = f"{category}.{sim_name}"  # Create the module name string
        module = importlib.import_module(module_name)  # Import the module dynamically
        module.main()  # Call the main function of the imported module

    def applyDarkTheme(self):
        """Apply a dark theme to the application."""
        dark_palette = QPalette()

        # Set the color palette for the dark theme
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        self.setPalette(dark_palette)  # Apply the dark palette to the Application


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
        
    # Load and set the application icon
    icon_path = os.path.join(os.path.dirname(__file__), 'logo.jpg')  
    app.setWindowIcon(QIcon(icon_path))
    
    ex = SimulationApp()  # Create an instance of the SimulationApp
    ex.show()  # Show the application window
    sys.exit(app.exec_())  # Run the application event loop

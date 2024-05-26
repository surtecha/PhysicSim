import sys
import os
import importlib
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class SimulationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialize the user interface."""
        self.setWindowTitle('Simulation Categories')
        self.setGeometry(100, 100, 800, 600)  # Set window size and position

        layout = QVBoxLayout()  # Main layout for the window

        # Create tabs for each category
        tabs = QTabWidget()
        categories = ["Kinematics", "atomics", "fluids", "gravitation", "materials"]  # List of simulation categories

        # Add a tab for each category
        for category in categories:
            tabs.addTab(self.createCategory(category), category)

        layout.addWidget(tabs)  # Add tabs to the main layout
        self.setLayout(layout)  # Set the layout for the window

        self.applyDarkTheme()  # Apply dark theme to the application

    def createCategory(self, category):
        """
        Create a widget for a simulation category with buttons to run each simulation.
        :param category: The name of the category (e.g., "Kinematics");
        :return: A QWidget containing the buttons for the category.
        """
        category_widget = QWidget()  # Create a new widget for the category
        layout = QVBoxLayout()  # Layout for the category widget

        # Path to the category folder
        folder_path = os.path.join(os.path.dirname(__file__), category)
        # List of python files in the category folder
        simulation_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

        # Create a button for each simulation file
        for sim_file in simulation_files:
            sim_name = os.path.splitext(sim_file)[0]  # Extract the simulation name without the .py extension
            button = QPushButton(sim_name)
            # Connect the button click to the function that runs the simulation
            button.clicked.connect(lambda checked, c=category, s=sim_name: self.run_simulation(c, s))
            layout.addWidget(button)  # Add the button to the layout

        category_widget.setLayout(layout)  # set the layout for the category widget

        return category_widget

    def run_simulation(self, category, sim_name):
        """
        Dynamically import and run the simulation function from the specified module.
        :param category: The category of the simulation (e.g., "Kinematics").
        :param sim_name: The name of the simulation file (e.g., "projectile").
        """
        module_name = f"{category}.{sim_name}"  # Create the module name string
        module = importlib.import_module(module_name)  # import the module dynamically
        module.main()  # call the run function of the imported module

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
    ex = SimulationApp()  # Create an instance of the SimulationApp
    ex.show()  # Show the application window
    sys.exit(app.exec_())  # Run the application event loop

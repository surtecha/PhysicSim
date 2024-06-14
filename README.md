<p align="center">
  <img src="https://github.com/surtecha/multi-physics-simulation-engine/assets/91011302/c01a2393-45a0-4ad7-8899-e883aeaa90bd" alt="MPSE logo" width="200" height="200"/>
</p>

<h1 align="center">Multi-Physics Simulation Engine</h1>

## Overview

The Multi-Physics Simulation Engine is a comprehensive application designed to facilitate the exploration and simulation of various physical phenomena. The application provides an intuitive and user-friendly interface for running simulations in multiple categories such as Atomics, Fluids, Kinematics, Gravitation, and Materials. Each category contains a set of predefined simulations that users can easily run and visualize.

## Features

- **Multi-Category Support**: Simulate physical phenomena across diverse categories including Atomics, Fluids, Kinematics, Gravitation, and Materials.
- **User-Friendly Interface**: A modern, dark-themed GUI with categorized tabs for easy navigation.
- **Dynamic Simulation Loading**: Simulations are dynamically loaded and executed, allowing for easy extension and customization.
- **Detailed Descriptions**: Each simulation comes with a detailed description to help users understand the underlying concepts.
- **High-Quality Visualization**: Buttons and icons are designed for high-quality display with rounded, smooth transformations.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.7+
- PyQt5

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/surtecha/multi-physics-simulation-engine.git
    cd multi-physics-simulation-engine
    ```

2. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To start the application, navigate to the project directory and run the following command:

```sh
python main.py
```

The application will launch and display the main window with tabs for each simulation category.

## Project Structure

- **main.py**: The main application script that initializes the GUI and handles user interactions.
- **/Atomics**: Directory containing atomic simulations and their resources (Python scripts, images, and description files).
- **/Fluids**: Directory containing fluid simulations and their resources.
- **/Kinematics**: Directory containing kinematic simulations and their resources.
- **/Gravitation**: Directory containing gravitational simulations and their resources.
- **/Materials**: Directory containing material simulations and their resources.
- **logo.jpg**: The application icon.

## Usage

### Interface

Upon launching the application, you will see a window with tabs representing different categories of simulations. Each tab contains buttons for individual simulations. 

1. **Select a Category**: Click on the tab corresponding to the category of interest (e.g., Kinematics).
2. **Choose a Simulation**: Click on the button representing the simulation you want to run.
3. **View Description**: A popup will appear showing a description of the simulation. 
4. **Run Simulation**: Click the "Simulate" button in the popup to run the simulation.

### Adding New Simulations

To add a new simulation:

1. **Create the Simulation Script**: Write your simulation code in a Python script and place it in the appropriate category directory (e.g., `/Kinematics`).
2. **Add a Description**: Create a text file with the same name as your script (e.g., `your_simulation_description.txt`) and write a description of the simulation.
3. **Add an Image (Optional)**: Add an image with the same name as your script (e.g., `your_simulation.jpg`) to be used as the button icon.

### Example

If you have a new simulation called `projectile.py` for the Kinematics category:

1. Place `projectile.py` in the `/Kinematics` directory.
2. Create `projectile_description.txt` with a description of the simulation.
3. (Optional) Add `projectile.jpg` for the button icon.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

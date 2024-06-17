<p align="center">
  <img src="https://github.com/surtecha/multi-physics-simulation-engine/assets/91011302/c01a2393-45a0-4ad7-8899-e883aeaa90bd" alt="MPSE logo" width="200" height="200"/>
</p>

<h1 align="center">Multi-Physics Simulation Engine</h1>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Requirements](#requirements)
    - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
    - [Interface](#interface)
    - [Adding New Simulations](#adding-new-simulations)
    - [Example](#example)
- [Contributing](#contributing)
- [License](#license)

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

### Requirements

Ensure the following packages are listed in your `requirements.txt` file:

```
jax==0.4.28
jaxlib==0.4.28
matplotlib==3.9.0
matplotlib-inline==0.1.7
numpy==1.26.4
phiflow==2.5.4
phiml==1.5.1
pillow==10.3.0
pygame==2.5.2
pymunk==6.8.0
PyQt5==5.15.10
PyQt5-Qt5==5.15.13
PyQt5-sip==12.13.0
pytz==2024.1
PyYAML==6.0.1
pyzmq==26.0.3
qtconsole==5.5.2
QtPy==2.4.1
sympy==1.12
tqdm==4.66.4
```

### Running the Application

To start the application, navigate to the project directory and run the following command:

```sh
python main.py
```

The application will launch and display the main window with tabs for each simulation category.

## UI Preview

<p align="center">
  <img src="https://github.com/surtecha/multi-physics-simulation-engine/assets/91011302/496f5d4b-c4dd-4791-83df-e8579e506780" alt="Starting window upon launching (Atomics section)" width="600"/>
</p>
<p align="center">
  Starting window upon launching (Atomics section)
</p>

<p align="center">
  <img src="https://github.com/surtecha/multi-physics-simulation-engine/assets/91011302/74fde5d3-c209-4b59-b7b7-f72b4e88ab7c" alt="Description of simulation displayed when clicked" width="600"/>
</p>
<p align="center">
  Description of simulation displayed when clicked
</p>

<p align="center">
  <img src="https://github.com/surtecha/multi-physics-simulation-engine/assets/91011302/6b690cee-3953-4768-a33b-bdfe2546b3b3" alt="Simulation window" width="600"/>
</p>
<p align="center">
  Simulation window
</p>

## Project Structure

- **main.py**: The main application script that initializes the GUI and handles user interactions.
- **/Atomics**: Directory containing atomic simulations and their resources.
- **/Fluids**: Directory containing fluid simulations and their resources.
- **/Kinematics**: Directory containing kinematic simulations and their resources.
- **/Gravitation**: Directory containing gravitational simulations and their resources.
- **/Materials**: Directory containing material simulations and their resources.
- **logo.jpg**: The application icon.

Each directory contains python scripts, images, and description files for respective simulations.

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

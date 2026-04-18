# Python GUI Calculator

A modern, responsive graphical calculator built with Python and `customtkinter`. This project demonstrates object-oriented programming, clean user interface design, and advanced state management to handle complex user inputs smoothly.

## 🌟 Features

* **Modern Dark Interface**: Uses `customtkinter` for a sleek, visually appealing dark-mode design.
* **Core Mathematics**: Supports basic arithmetic (Addition, Subtraction, Multiplication, Division) as well as Modulo (`%`) and Exponentiation (`^`).
* **Keyboard Integration**: Fully supports physical keyboard inputs (numbers, operators, Enter/Return for equals, Backspace, and Escape for clear) for a faster user experience.
* **Robust State Management**: Built using the **State Design Pattern**. It dynamically transitions between different states (Init, Typing, Operator, Result, Error) to prevent crashes and ensure accurate calculations.
* **Smart Formatting**: Automatically formats whole number results as integers while preserving decimals for floating-point calculations.
* **Error Handling**: Gracefully catches invalid operations (like dividing by zero or malformed equations) and displays a clear "ERROR" message without crashing the application.

## 📋 Prerequisites

To run this project, you will need:
* Python 3.x installed on your computer.
* `pip` (Python package installer).

## 🚀 Installation & Usage

Follow these simple steps to run the calculator on your local machine:

1. **Clone the repository** (or download the ZIP file):
   ```bash
   git clone https://github.com/mynhleeh/calculator.git
   cd calculator
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 📂 Project Structure

This project follows a clean architecture, separating the user interface from the underlying mathematical logic:

* **`main.py`**: The main entry point of the application. It acts as the controller and implements the State Pattern to manage how the calculator responds to user inputs based on its current context.
* **`ui.py`**: Contains the `CalculatorView` class. It is strictly responsible for rendering the CustomTkinter graphical interface and capturing user inputs (clicks and keystrokes).
* **`math_engine.py`**: The mathematical core. It safely executes the calculations using Python's built-in `operator` module and formats the final output.
* **`requirements.txt`**: Lists the necessary third-party Python packages required to run the app.
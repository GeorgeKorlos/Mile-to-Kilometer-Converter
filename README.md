# Mile to Kilometer Converter: A Simple Tkinter GUI Application

This repository contains a Python script that implements a graphical user interface (GUI) application using Tkinter. The application converts a distance from miles to kilometers. This project is perfect for beginners who want to learn about GUI development in Python using Tkinter.

## Description

The script creates a simple GUI application that allows users to input a distance in miles and then converts it to kilometers when the user clicks the "Calculate" button.

### Key Features

- **Entry Widget:** Allows the user to input the distance in miles.
- **Labels:** Provides instructions and displays the conversion result.
- **Button:** Triggers the conversion from miles to kilometers.
- **Responsive Layout:** The GUI is arranged using Tkinter's grid system, making it easy to manage the layout.

### How It Works

1. **User Input:**
   - The user enters a value in miles into the entry widget.

2. **Conversion Calculation:**
   - When the "Calculate" button is pressed, the input value is retrieved, converted from miles to kilometers using the formula:
     \[
     \text{{kilometers}} = \text{{miles}} \times 1.609
     \]
   - The result is then displayed in the GUI.

3. **Output:**
   - The converted distance in kilometers is shown next to the "Km" label.

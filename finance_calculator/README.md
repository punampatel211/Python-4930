# Finance Calculator

This code provides a comprehensive finance calculator designed to assist with loan payments, savings growth, and retirement planning. Using Python, the calculator collects user inputs and performs accurate financial calculations to offer clear insights, enabling users to make informed financial decisions.

In this program, Python functions and classes work together to process user data and return calculated results. Below are the main components and functionalities of the program:

## Main Components and Functionalities

1. **User Input:**
   - The program prompts the user to input financial details, such as loan principal, interest rate, and the number of years.

2. **Loan Calculation:**
   - Calculates monthly loan payments based on user-provided principal, annual interest rate, and loan term.
   - Utilizes the `Loan` class to encapsulate loan-related data and methods.

3. **Savings Growth Calculation:**
   - Projects future savings value considering the initial amount, monthly contributions, and annual interest rate over a specified period.
   - Employs the `Savings` class to manage savings-related data and calculations.

4. **Retirement Savings Calculation:**
   - Estimates retirement savings by projecting current savings and regular contributions over a defined period until retirement.
   - Also utilizes the `Savings` class to handle retirement-specific scenarios.

5. **Control Statements:**
   - Uses `if/elif` statements to navigate user choices and execute the corresponding financial calculations.
   - Implements a `while` loop to keep the program running until the user chooses to exit.

6. **Modules and Structure:**
   - The code is organized into separate modules (`functions.py` for calculation functions and `classes.py` for class definitions) and integrated through `main.py`.
   - Ensures modularity and maintainability, allowing for future enhancements and scalability.

## How to Use

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/punampatel211/Python-4930.git

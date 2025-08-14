# **Project: py-ledger \- A Professional Command-Line Transaction Logger**

A robust, well-tested, and installable Python command-line tool for managing financial transactions, built following professional software engineering best practices.

This repository documents a practice project developed to master the concepts from the "Advanced Python for Production Systems" module of the  \- \- \- Roadmap. The objective was to apply foundational software engineering principles to a practical problem, transforming a simple idea into a complete, professional-grade software package.

## **Table of Contents**

1. [Overview](https://www.google.com/search?q=%23overview)  
2. [Core Features](https://www.google.com/search?q=%23core-features)  
3. [Architectural Design](https://www.google.com/search?q=%23architectural-design)  
4. [Project Structure](https://www.google.com/search?q=%23project-structure)  
5. [Robustness](https://www.google.com/search?q=%23robustness-and-automated-testing) and [Automated Testing](https://www.google.com/search?q=%23robustness-and-automated-testing)  
6. [Installation and Usage](https://www.google.com/search?q=%23installation-and-usage)  
7. [Command-Line Interface (CLI) Reference](https://www.google.com/search?q=%23command-line-interface-cli-reference)  
8. [License](https://www.google.com/search?q=%23license)

## **Overview**

Effective personal finance starts with diligent tracking. py-ledger is a command-line tool designed to make this process simple, fast, and scriptable. It provides a clean interface for adding income and expense transactions, which are persistently stored in a universally compatible CSV format.

More than just a utility, this project served as a case study in modern Python development. It was an exercise in building software the "right way"—starting with a clean project structure, designing an efficient object-oriented core, building a comprehensive "safety net" of automated tests, and packaging the final product into a distributable command-line application.

## **Core Features**

* **Multi-Command CLI:** A user-friendly command-line interface built with click provides distinct commands for add, balance, and history.  
* **Persistent Storage:** All transactions are safely stored in a CSV file, making the data portable and easily accessible by spreadsheet applications.  
* **Object-Oriented Design:** The core logic is encapsulated within a Ledger class, promoting code that is clean, reusable, and easy to maintain.  
* **Robust** and **Efficient:** The application is designed to be efficient by loading data into memory once and includes robust error handling for file operations.  
* **100%** Test **Coverage:** A full suite of unit tests written with pytest ensures the code's reliability and correctness, achieving complete test coverage.

## **Architectural Design**

The application is designed with a clear separation of concerns, a core principle of good software architecture.

1. **Core Logic (ledger.py):** The Ledger class is the "engine" of the application. It is solely responsible for all business logic: managing the in-memory list of transactions, reading from the CSV file, writing to the CSV file, and calculating the balance. It has no knowledge of the user interface.  
2. **User Interface (cli.py):** The cli.py module is the "dashboard" of the application. Its only job is to handle user input from the command line, parse the arguments, and then call the appropriate methods on a Ledger object to perform the requested actions.

This separation ensures that the core logic can be tested independently of the user interface and could easily be reused in a different context, such as a web application.

## **Project Structure**

The project is organized using a standard, professional blueprint that enables robust testing and distribution.

py-ledger/  
├── .venv/               \# Isolated virtual environment for dependencies  
├── py\_ledger/           \# The installable Python package  
│   ├── \_\_init\_\_.py      \# Makes the directory a package  
│   ├── cli.py           \# The command-line interface logic  
│   └── ledger.py        \# Main application logic (the Ledger class)  
├── tests/                 \# Directory for all automated tests  
│   └── test\_ledger.py     \# Unit tests for the Ledger class  
├── .gitignore             \# Specifies files for Git to ignore (like .venv)  
├── pyproject.toml         \# Project configuration for installation via pip  
├── README.md              \# Project documentation (this file)  
└── requirements.txt       \# List of project dependencies

## **Robustness and Automated Testing**

A key goal of this project was to build a "safety net" of automated tests to guarantee the reliability of the core logic. We used **pytest**, the industry-standard testing framework for Python.

### **Unit Tests**

A comprehensive suite of unit tests was developed in tests/test\_ledger.py. These tests are small, focused, and run in an isolated environment using temporary files to ensure they are repeatable and do not affect each other. The tests cover all critical functionalities:

* **test\_ledger\_creates\_new\_csv:** Verifies that a new, correctly formatted CSV file is created if one doesn't exist.  
* **test\_add\_transaction\_and\_read\_csv:** Confirms that a new transaction is correctly appended to the CSV file.  
* **test\_get\_balance\_income\_and\_expense:** Asserts that the balance calculation correctly handles both income and expenses.  
* **test\_get\_transaction\_history:** Ensures that the history is read correctly from the CSV.  
* **test\_loading\_existing\_ledger:** A crucial test that verifies the application can correctly load and process a pre-existing ledger file.

### **Test Coverage**

Using the pytest-cov plugin, we measured our test coverage to ensure our tests were thorough. This project achieved **100% test coverage**, meaning every single line of our core ledger.py logic is protected by our automated safety net.

## **Installation and Usage**

This tool is packaged to be easily installable via pip.

1. **Clone the repository:**  
   git clone (https://github.com/triv321/py_ledger_project)  
   cd py-ledger

2. **Create and activate a virtual environment:**  
   python3 \-m venv .venv  
   source .venv/bin/activate

3. Install the tool in editable mode:  
   The \-e flag allows you to continue developing the tool without needing to reinstall it after every change.  
   pip install \-e .

## **Command-Line Interface (CLI) Reference**

Once installed, you can use the ledger command directly in your terminal.

#### **Add a new transaction**

ledger add \<file\_path\> \<date\> \<description\> \<amount\> \<type\>

* \<type\> must be either income or expense.  
* **Example:**  
  ledger add my\_transactions.csv 2025-08-13 "Coffee" 5.00 expense

#### **Check the current balance**

ledger balance \<file\_path\>

* **Example:**  
  ledger balance my\_transactions.csv

#### **View the full transaction history**

ledger history \<file\_path\>

* **Example:**  
  ledger history my\_transactions.csv

## **License**

This project is licensed under the MIT License.

# Library Management System

This is a simple Library Managemnet System built using Python, that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. The project follows Test-Driven-Development (TDD) principles to ensure high-quality and maintainable code.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Running Tests](#running-tests)
5. [Git Workflow](#git-workflow)

## Features
- Add new books to the library
- Borrow books from the library
- Return borrowed books
- View a list of all available books

## Installation

1. Clone the Git repository:
   bash
   git clone <your-repository-url>

2. Navigate into the project directory:

cd library-management-system

## Usage

1. Run the Library Management System:
     bash
     py library_management_system.py

## Running Tests

The project uses [testing framework] (e.g., unittest for Python).

1. Make sure you are in the project directory.

2. Run the tests:
   - [For Python]
     bash
     python -m unittest discover

Test Results:
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

## Git Workflow

Follow the Git workflow for TDD:

1. Initialize Git repository:
   bash
   git init

2. Create an initial README:

echo "# Library Management System" > README.md
git add README.md
git commit -m "Initial commit with README"

3. Follow this pattern for each feature:

Write a test for the feature:

git add .
git commit -m "Add test for [feature]"

Implement the feature:
git add .
git commit -m "Implement [feature]"



4. Push your changes to the remote repository:

git remote add origin <remote-repository-url>
git push -u origin master
## Description

This repository contains solutions for Homework 5 of the GoIT Python course.
The project demonstrates how these concepts can be applied to real-world problems, including performance optimization, text processing, log analysis, and improving the robustness of CLI applications.

## Technologies & Stack

The project is implemented using:
- Python 3
- Standard Python libraries:
   - re - regular expressions
   - sys - command-line arguments
   - collections - data aggregation
- Core programming concepts:
   - Recursion and memoization
   - Closures
   - Generators (yield)
   - Functional programming (functions as arguments)
   - Decorators
   - Exception handling
   - CLI applications

## Functionality

The repository includes the following tasks:


1. Cached Fibonacci Calculator 
Implements Fibonacci number calculation.
Stores previously calculated values in a cache dictionary.
Significantly improves performance for repeated calls.
Returns an inner function fibonacci(n) that preserves state between calls.
Key concepts: recursion, closures, memory optimization.


2. Income Extraction with Generators
- generator_numbers(text: str)
  
Parses a text string and extracts all valid floating-point numbers.
Returns a generator for memory-efficient iteration.
Uses regular expressions for accurate number detection.

- sum_profit(text: str, func: Callable)
  
Uses the provided generator function to calculate total income.
Demonstrates passing functions as arguments.
Efficiently processes large text inputs.
Key concepts: generators, functional programming, regex.

3. Log File Analyzer

Accepts:
- path to a log file
- optional log level filter (e.g. error, info)

Features:
- parsing log entries
- counting logs by level (INFO, DEBUG, ERROR, WARNING)
- filtering logs by level
- formatted table output
- 
CLI tool for analyzing log files.

4. Console Assistant Bot with Decorators

Extended version of the assistant bot from the previous homework.

Adds centralized error handling using a decorator input_error.
Supports commands:
- hello
- add <name> <phone>
- change <name> <phone>
- phone <name>
- all
- exit / close

Handles common input errors:
- ValueError
- KeyError
- IndexError

Ensures the application does not crash due to invalid user input.

Key concepts: decorators, error handling, CLI design.

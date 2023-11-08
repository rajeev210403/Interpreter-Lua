# Lua Interpreter 🌟

This repository contains a lightweight Lua interpreter implemented in Python using recursive descent parsing. The interpreter allows you to parse Lua code, generate an Abstract Syntax Tree (AST), and execute Lua programs. It supports various language features, including assignment statements, arithmetic operators, comparison operators, if statements, nested if statements, while loops, and single/multiline comments.

## Features ✨

- **Lexer:** Converts Lua programs into tokens, providing type, textual representation, and position information.
- **Parser:** Breaks down code into individual chunks, verifies syntax, and builds an AST based on the code's structure.
- **Interpreter:** Executes Lua programs using the generated AST, displaying output and variable values after execution.
- **NodeVisitor Class:** A fundamental class enabling the visitation of each node in the AST.

## Usage 🚀

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the Python file to execute the Lua interpreter.

### How to Run 🛠️

```bash
python interpreter.py
```

### Example 📝

```lua
-- Sample Lua Code
local x = 10
if x > 5 then
    print("x is greater than 5")
else
    print("x is less than or equal to 5")
```

**Output:**
```
x is greater than 5
```

## Dependencies 📦

The only dependency for running this program is Python.

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the interpreter's functionality or fix any issues.

## Author 🌍

- **Rajeev Thota**  
- **Email:** thotarajeev2003@gmail.com  
- **GitHub:** [rajeev210403](https://github.com/rajeev210403)

Feel free to reach out for any questions or feedback. Happy coding! 🚀

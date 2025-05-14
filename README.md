# SymPy MCP Server

A FastMCP server for solving algebraic equations using SymPy.

## Features

- Solve linear equations algebraically
- Get step-by-step solutions
- Easy integration with Claude Desktop and other MCP clients

## Installation

This project uses pipenv for dependency management. The required dependencies are:

- sympy
- fastmcp

These dependencies are already specified in the Pipfile at the root of the project.

## Usage

### Starting the Server

To start the server, run:

```bash
cd sympy-mcp-server
pipenv run python run_server.py
```

Or alternatively:

```bash
cd sympy-mcp-server
pipenv run python -m src.server
```

The server will start on `http://0.0.0.0:8000`.

### Using with Claude Desktop

To use this server with Claude Desktop:

1. Start the server as described above
2. In Claude Desktop, go to Settings > MCP Servers
3. Add the configuration file path: `/path/to/sympy-mcp-experiment/sympy-mcp-server/mcp_config.json`
4. Claude will now have access to the `solve_equation` tool

### Testing the Server

A test client is provided to verify that the server is working correctly:

```bash
cd sympy-mcp-server
pipenv run python test_client.py
```

This will send a sample equation to the server and display the step-by-step solution.

### Using the Equation Solver Tool

The server exposes a tool called `solve_equation` that can be used to solve linear equations.

#### Input Format

```json
{
  "equation": "2*x + 3 = 7",
  "variable": "x"
}
```

#### Output Format

```json
{
  "solution": {
    "variable": "x",
    "value": 2.0
  },
  "steps": [
    "Original equation: 2*x + 3 = 7",
    "Equation in symbolic form: 2*x + 3 = 7",
    "Subtract 3 from both sides: 2*x = 4",
    "Divide both sides by 2: x = 2.0",
    "Solution: x = 2.0"
  ]
}
```

## Examples

### Example 1: Simple Linear Equation

Input:
```json
{
  "equation": "2*x + 3 = 7",
  "variable": "x"
}
```

Output:
```json
{
  "solution": {
    "variable": "x",
    "value": 2.0
  },
  "steps": [
    "Original equation: 2*x + 3 = 7",
    "Equation in symbolic form: 2*x + 3 = 7",
    "Subtract 3 from both sides: 2*x = 4",
    "Divide both sides by 2: x = 2.0",
    "Solution: x = 2.0"
  ]
}
```

### Example 2: Linear Equation with Negative Coefficient

Input:
```json
{
  "equation": "-3*y + 5 = 8",
  "variable": "y"
}
```

Output:
```json
{
  "solution": {
    "variable": "y",
    "value": -1.0
  },
  "steps": [
    "Original equation: -3*y + 5 = 8",
    "Equation in symbolic form: -3*y + 5 = 8",
    "Subtract 5 from both sides: -3*y = 3",
    "Divide both sides by -3: y = -1.0",
    "Solution: y = -1.0"
  ]
}
```

## Future Enhancements

- Support for quadratic equations
- Support for systems of linear equations
- Support for symbolic solutions (with parameters)

"""
Equation solver using SymPy.

This module provides functionality to solve linear equations and generate
step-by-step solutions.
"""

import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from typing import List, Tuple, Dict, Any


def sympy_solve_linear_equation(equation_str: str, variable_str: str) -> Tuple[float, List[str]]:
    """
    Solve a linear equation and provide step-by-step solution.
    
    Args:
        equation_str (str): The equation to solve, e.g., "2*x + 3 = 7"
        variable_str (str): The variable to solve for, e.g., "x"
        
    Returns:
        Tuple[float, List[str]]: A tuple containing the solution value and a list of steps
    
    Raises:
        ValueError: If the equation is not linear or cannot be solved
    """
    # Parse the variable
    variable = sp.Symbol(variable_str)
    
    # Parse the equation
    steps = [f"Original equation: {equation_str}"]
    
    # Split the equation into left and right sides
    if "=" not in equation_str:
        raise ValueError("Equation must contain an equals sign (=)")
    
    left_str, right_str = equation_str.split("=", 1)
    left_expr = parse_expr(left_str.strip())
    right_expr = parse_expr(right_str.strip())
    
    # Move all terms with the variable to the left side
    # and all other terms to the right side
    equation = sp.Eq(left_expr, right_expr)
    steps.append(f"Equation in symbolic form: {equation}")
    
    # Rearrange to standard form: ax + b = 0
    rearranged = sp.solve(equation, variable)[0]
    
    # Generate step-by-step solution
    # For a linear equation ax + b = c, we do:
    # 1. Subtract b from both sides: ax = c - b
    # 2. Divide both sides by a: x = (c - b) / a
    
    # Get coefficients from the original equation
    expanded = sp.expand(left_expr - right_expr)
    coeffs = sp.collect(expanded, variable, evaluate=False)
    
    # Extract the coefficient of the variable and the constant term
    a = coeffs.get(variable, 0)
    b = coeffs.get(1, 0)
    
    if a == 0:
        raise ValueError(f"Equation is not linear in {variable_str}")
    
    # Generate steps
    if b != 0:
        if b > 0:
            steps.append(f"Subtract {b} from both sides: {a}*{variable_str} = -{b}")
        else:
            steps.append(f"Add {-b} to both sides: {a}*{variable_str} = {-b}")
    
    if a != 1:
        steps.append(f"Divide both sides by {a}: {variable_str} = {rearranged}")
    
    # Final solution
    solution_value = float(rearranged)
    steps.append(f"Solution: {variable_str} = {solution_value}")
    
    return solution_value, steps


def format_solution(value: float, variable: str, steps: List[str]) -> Dict[str, Any]:
    """
    Format the solution and steps into the expected output format.
    
    Args:
        value (float): The solution value
        variable (str): The variable that was solved for
        steps (List[str]): The step-by-step solution
        
    Returns:
        Dict[str, Any]: Formatted solution
    """
    return {
        "solution": {
            "variable": variable,
            "value": value
        },
        "steps": steps
    }

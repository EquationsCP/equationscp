"""
Schemas for the SymPy MCP Server.

This module defines the Pydantic models for input and output of the equation solver.
"""

from pydantic import BaseModel, Field
from typing import List


class EquationInput(BaseModel):
    """
    Input schema for the equation solver.
    
    Attributes:
        equation (str): The equation to solve, e.g., "2*x + 3 = 7"
        variable (str): The variable to solve for, e.g., "x"
    """
    equation: str = Field(..., description="The equation to solve, e.g., '2*x + 3 = 7'")
    variable: str = Field(..., description="The variable to solve for, e.g., 'x'")


class Solution(BaseModel):
    """
    Schema for the solution of an equation.
    
    Attributes:
        variable (str): The variable that was solved for
        value (float): The value of the variable
    """
    variable: str = Field(..., description="The variable that was solved for")
    value: float = Field(..., description="The value of the variable")


class EquationOutput(BaseModel):
    """
    Output schema for the equation solver.
    
    Attributes:
        solution (Solution): The solution to the equation
        steps (List[str]): Step-by-step explanation of how the equation was solved
    """
    solution: Solution = Field(..., description="The solution to the equation")
    steps: List[str] = Field(..., description="Step-by-step explanation of how the equation was solved")

"""
FastMCP server for solving algebraic equations using SymPy.

This module sets up a FastMCP server that exposes a tool for solving
linear equations with step-by-step solutions.
"""

import logging
from fastmcp import FastMCP
import asyncio

from schemas import EquationInput, EquationOutput
from solver import sympy_solve_linear_equation, format_solution


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Create the FastMCP server
server = FastMCP(
    name="sympy-solver",
    title="SymPy Equation Solver",
    description="A FastMCP server for solving algebraic equations using SymPy",
    version="0.1.0"
)


@server.tool(
    name="solve_linear_equation",
    description="Solve a linear equation and provide step-by-step solutions",
)
async def solve_linear_equation(input_data: EquationInput) -> EquationOutput:
    """
    Solve a linear equation and provide a step-by-step solution.
    
    Args:
        input_data (EquationInput): The equation and variable to solve for
        
    Returns:
        EquationOutput: The solution and step-by-step explanation
    """
    logger.info(f"Solving equation: {input_data.equation} for {input_data.variable}")
    
    try:
        # Solve the equation
        loop = asyncio.get_event_loop()
        solution_value, steps = await loop.run_in_executor(
            None,
            lambda: sympy_solve_linear_equation(input_data.equation, input_data.variable)
        )
        '''
        solution_value, steps = sympy_solve_linear_equation(
            input_data.equation, 
            input_data.variable
        )
        '''
        # Format the solution
        result = format_solution(
            solution_value,
            input_data.variable,
            steps
        )
        
        return EquationOutput(**result)
    
    except Exception as e:
        logger.error(f"Error solving equation: {str(e)}")
        raise ValueError(f"Failed to solve equation: {str(e)}")



if __name__ == "__main__":
    logger.info("Starting SymPy Equation Solver MCP server")
    server.run()

from langchain.tools import tool

class CalculatorTools():
    
    @tool("Make a Calculation")
    def calculate(operation):
        """Useful to perform any mathematical operation
        Like Sum, Minus, multiplication and division etc.
        The input to this tool should be mathematical
        expression, a couple examples are '200*7' or '5000/2*10'
        """
        
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
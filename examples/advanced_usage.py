"""Advanced usage examples for NexusCalc."""

from nexuscalc.core.operations import Operations
from nexuscalc.utils.formatters import format_result, format_expression
from nexuscalc.evaluator.evaluator import Evaluator

def main():
    print("🔢 NexusCalc Advanced Examples")
    print("="*50)
    
    # Basic operations
    ops = Operations()
    
    print("\n📊 Basic Operations:")
    print("-"*30)
    
    result1 = ops.add(10, 20)
    print(f"Add: {format_expression('add', 10, 20, result1)}")
    
    result2 = ops.multiply(5, 6)
    print(f"Multiply: {format_expression('multiply', 5, 6, result2)}")
    
    result3 = ops.divide(15, 4)
    print(f"Divide: {format_expression('divide', 15, 4, result3)}")
    
    result4 = ops.floor_divide(15, 4)
    print(f"Floor divide: {format_expression('floor', 15, 4, result4)}")
    
    # Division by zero handling
    print("\n🛡️ Division by Zero Handling:")
    print("-"*30)
    
    try:
        result = ops.divide(10, 0)
    except Exception as e:
        print(f"❌ Error caught: {e}")
    
    # Safe division
    result = ops.safe_divide(10, 0)
    print(f"Safe division (10 / 0): {result}")
    
    # Expression evaluation
    print("\n📐 Expression Evaluation:")
    print("-"*30)
    
    evaluator = Evaluator()
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "sqrt(16) + abs(-5)",
        "ceil(3.7) + floor(3.7)",
        "2 * pi",
        "sin(30) + cos(60)"
    ]
    
    for expr in expressions:
        try:
            result = evaluator.evaluate_expression(expr)
            print(f"{expr:20} = {format_result(result)}")
        except Exception as e:
            print(f"{expr:20} ❌ {e}")
    
    print("\n" + "="*50)
    print("✅ Advanced examples completed!")

if __name__ == "__main__":
    main()

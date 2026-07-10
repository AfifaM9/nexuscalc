"""Main calculator implementation."""

import sys
import re
import math
from ..core.operations import Operations
from ..utils.validators import validate_number
from ..utils.formatters import format_result
from ..exceptions.calculator_errors import CalculatorError, DivisionByZeroError

class NexusCalc:
    """Main calculator class with interactive menu."""
    
    def __init__(self):
        self.operations = Operations()
        self.running = True
        self.calculation_count = 0
        self.menu_options = {
            '1': ('Add', self.operations.add, '+'),
            '2': ('Subtract', self.operations.subtract, '-'),
            '3': ('Multiply', self.operations.multiply, '×'),
            '4': ('Divide', self.operations.divide, '÷'),
            '5': ('Floor', self.operations.floor_divide, '//'),
            '6': ('Modulo', self.operations.modulo, '%'),
            '7': ('Exponent', self.operations.exponent, '^'),
            '8': ('Square Root', self.operations.square_root, '√'),
            '9': ('Nth Root', self.operations.nth_root, 'ⁿ√'),
            '10': ('Percentage', self.operations.percentage, '% of'),
            '11': ('Factorial', self.operations.factorial, '!'),
        }
        # Regex patterns for quit commands
        self.quit_patterns = [
            re.compile(r'^[Qq]$'),
            re.compile(r'^[Qq][Uu][Ii][Tt]$'),
            re.compile(r'^12$'),  # 12 is now quit
        ]
        # Help patterns
        self.help_patterns = [
            re.compile(r'^[Hh]$'),
            re.compile(r'^[Hh][Ee][Ll][Pp]$'),
            re.compile(r'^\?$'),
        ]
    
    def is_quit_command(self, text):
        if not text:
            return False
        text = text.strip()
        for pattern in self.quit_patterns:
            if pattern.match(text):
                return True
        return False
    
    def is_help_command(self, text):
        if not text:
            return False
        text = text.strip()
        for pattern in self.help_patterns:
            if pattern.match(text):
                return True
        return False
    
    def show_help(self):
        print("\n" + "="*60)
        print("📖 NEXUSCALC - Help & Documentation")
        print("="*60)
        print("\n🔢 WHAT IS NEXUSCALC?")
        print("-"*60)
        print("  A powerful interactive calculator for the command line.")
        print("  Perfect for quick calculations and learning Python.")
        print()
        print("📋 AVAILABLE OPERATIONS:")
        print("-"*60)
        print("  1. Add ➕        - Add two numbers")
        print("  2. Subtract ➖   - Subtract second from first")
        print("  3. Multiply ✖️   - Multiply two numbers")
        print("  4. Divide ➗     - Divide first by second")
        print("  5. Floor 🏠     - Floor division (integer result)")
        print("  6. Modulo 🔢    - Remainder after division")
        print("  7. Exponent ⚡   - Raise first to the power of second")
        print("  8. Square Root √ - Square root of a number")
        print("  9. Nth Root ⁿ√  - Nth root of a number")
        print(" 10. Percentage %  - Calculate percentage")
        print(" 11. Factorial !  - Factorial of a number")
        print(" 12. Quit 🚪      - Exit calculator")
        print()
        print("🎮 HOW TO USE:")
        print("-"*60)
        print("  1. Choose an operation (1-12)")
        print("  2. Enter your number(s)")
        print("  3. See the result!")
        print()
        print("⌨️  SPECIAL COMMANDS:")
        print("-"*60)
        print("  • 'h' or 'help' or '?'  - Show this help screen")
        print("  • 'q' or 'quit' or '12' - Exit the calculator")
        print("  • Ctrl+C                 - Cancel current operation")
        print("  • Ctrl+D                 - Exit calculator")
        print()
        print("📊 FEATURES:")
        print("-"*60)
        print("  ✅ Accurate floating-point calculations")
        print("  ✅ Division by zero error handling")
        print("  ✅ 11 operations available")
        print("  ✅ Calculation counter")
        print("  ✅ Clean result formatting")
        print("  ✅ Keyboard interrupt handling")
        print()
        print("📦 INSTALLATION:")
        print("-"*60)
        print("  python -m pip install nexuscalc")
        print()
        print("🚀 QUICK START:")
        print("-"*60)
        print("  from nexuscalc import start_calc")
        print("  start_calc()")
        print()
        print("🌐 MORE INFO:")
        print("-"*60)
        print("  PyPI: https://pypi.org/project/nexuscalc/")
        print("  GitHub: https://github.com/AfifaM9/nexuscalc")
        print("="*60)
    
    def run(self):
        try:
            while self.running:
                try:
                    self.show_menu()
                    choice = self.get_input("Use 1-12").strip()
                    
                    if self.is_help_command(choice):
                        self.show_help()
                        input("\nPress Enter to continue...")
                        continue
                    
                    if self.is_quit_command(choice):
                        self.show_goodbye()
                        self.running = False
                        break
                    
                    if choice not in self.menu_options:
                        print("❌ Invalid choice. Please select 1-12, h/help, or q/quit.")
                        continue
                    
                    operation_name, operation_func, operation_symbol = self.menu_options[choice]
                    
                    try:
                        if operation_name in ['Square Root', 'Nth Root']:
                            if operation_name == 'Square Root':
                                num = self.get_number("Enter a number")
                                result = self.operations.square_root(num)
                                self.calculation_count += 1
                                
                                print(f"\n{'='*50}")
                                print(f"📊 Calculation #{self.calculation_count}")
                                print(f"{'='*50}")
                                print(f"  √{format_result(num)} = {format_result(result)}")
                                print(f"{'='*50}")
                            else:  # Nth Root
                                num = self.get_number("Enter the number")
                                n = self.get_number("Enter the root (n)")
                                result = self.operations.nth_root(num, n)
                                self.calculation_count += 1
                                
                                print(f"\n{'='*50}")
                                print(f"📊 Calculation #{self.calculation_count}")
                                print(f"{'='*50}")
                                print(f"  {format_result(n)}√{format_result(num)} = {format_result(result)}")
                                print(f"{'='*50}")
                        elif operation_name == 'Percentage':
                            num1 = self.get_number("Enter the percentage")
                            num2 = self.get_number("Enter the number")
                            result = self.operations.percentage(num1, num2)
                            self.calculation_count += 1
                            
                            print(f"\n{'='*50}")
                            print(f"📊 Calculation #{self.calculation_count}")
                            print(f"{'='*50}")
                            print(f"  {format_result(num1)}% of {format_result(num2)} = {format_result(result)}")
                            print(f"{'='*50}")
                        elif operation_name == 'Factorial':
                            num = self.get_number("Enter a number")
                            result = self.operations.factorial(num)
                            self.calculation_count += 1
                            
                            print(f"\n{'='*50}")
                            print(f"📊 Calculation #{self.calculation_count}")
                            print(f"{'='*50}")
                            print(f"  {format_result(num)}! = {format_result(result)}")
                            print(f"{'='*50}")
                        else:
                            num1 = self.get_number("Enter first number")
                            num2 = self.get_number("Enter second number")
                            
                            result = operation_func(num1, num2)
                            self.calculation_count += 1
                            
                            print(f"\n{'='*50}")
                            print(f"📊 Calculation #{self.calculation_count}")
                            print(f"{'='*50}")
                            print(f"  {format_result(num1)} {operation_symbol} {format_result(num2)} = {format_result(result)}")
                            print(f"{'='*50}")
                        
                    except DivisionByZeroError as e:
                        print(f"\n❌ Division Error: {e}")
                        print("💡 Hint: You cannot divide by zero. Please try a different number.")
                    except CalculatorError as e:
                        print(f"\n❌ Error: {e}")
                    except ValueError:
                        print("\n❌ Error: Invalid number format. Please enter a valid number.")
                    except Exception as e:
                        print(f"\n❌ Unexpected error: {e}")
                    
                    print()
                    
                except KeyboardInterrupt:
                    print("\n\n⚠️ Operation cancelled by user.")
                    print("💡 Press Ctrl+C again to exit, or continue using the calculator.")
                    continue
                except EOFError:
                    print("\n\n⚠️ Input stream closed.")
                    print("💡 Exiting calculator...")
                    self.running = False
                    break
                
        except KeyboardInterrupt:
            self.show_goodbye()
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Fatal error: {e}")
            sys.exit(1)
    
    def show_menu(self):
        print("\n" + "="*50)
        print("🔢 NEXUSCALC - Powerful Calculator")
        print("="*50)
        
        if self.calculation_count > 0:
            print(f"📊 Calculations performed: {self.calculation_count}")
            print("-"*50)
        
        print("\nWhat are you trying to calculate?")
        print("List:")
        print()
        print("1. Add ➕")
        print("2. Subtract ➖")
        print("3. Multiply ✖️")
        print("4. Divide ➗")
        print("5. Floor 🏠")
        print("6. Modulo 🔢")
        print("7. Exponent ⚡")
        print("8. Square Root √")
        print("9. Nth Root ⁿ√")
        print("10. Percentage %")
        print("11. Factorial !")
        print("12. Quit 🚪")
        print()
        print("💡 Type 'h' or 'help' for help")
        print("💡 Press Ctrl+C to cancel operation")
        print("💡 Type '12', 'q', 'Q', 'quit', or 'QUIT' to exit")
        print("-"*50)
    
    def show_goodbye(self):
        print("\n" + "="*50)
        print("👋 Goodbye! Thanks for using NexusCalc!")
        print("="*50)
        if self.calculation_count > 0:
            print(f"📊 You performed {self.calculation_count} calculation(s)")
        print("="*50)
    
    def get_input(self, prompt):
        try:
            return input(f"{prompt}\nNEXUSCALC > ")
        except KeyboardInterrupt:
            print("\n\n⚠️ Input cancelled.")
            raise
        except EOFError:
            print("\n\n⚠️ End of input detected.")
            raise
    
    def get_number(self, prompt):
        while True:
            try:
                user_input = self.get_input(prompt)
                if self.is_help_command(user_input):
                    self.show_help()
                    input("\nPress Enter to continue...")
                    continue
                if self.is_quit_command(user_input):
                    print("\n⚠️ Quit requested during number input.")
                    raise KeyboardInterrupt
                return validate_number(user_input)
            except CalculatorError as e:
                print(f"❌ Error: {e}")
                print("💡 Please try again with a valid number.")
            except KeyboardInterrupt:
                print("\n⚠️ Number input cancelled.")
                raise
            except EOFError:
                print("\n⚠️ End of input detected.")
                raise

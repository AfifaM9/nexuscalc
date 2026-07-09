"""Main calculator implementation."""

import sys
import re
from ..core.operations import Operations
from ..utils.validators import validate_number
from ..utils.formatters import format_result
from ..exceptions.calculator_errors import CalculatorError, DivisionByZeroError

class NexusCalc:
    """Main calculator class with interactive menu."""
    
    def __init__(self):
        self.operations = Operations()
        self.running = True
        self.menu_options = {
            '1': ('Add', self.operations.add),
            '2': ('Subtract', self.operations.subtract),
            '3': ('Multiply', self.operations.multiply),
            '4': ('Divide', self.operations.divide),
            '5': ('Floor', self.operations.floor_divide),
        }
        # Regex patterns for quit commands
        self.quit_patterns = [
            re.compile(r'^[Qq]$'),           # q or Q
            re.compile(r'^[Qq][Uu][Ii][Tt]$'), # quit in any case
            re.compile(r'^6$'),               # number 6
        ]
    
    def is_quit_command(self, text):
        """Check if the input matches any quit pattern."""
        if not text:
            return False
        text = text.strip()
        for pattern in self.quit_patterns:
            if pattern.match(text):
                return True
        return False
    
    def run(self):
        """Run the calculator main loop."""
        try:
            while self.running:
                try:
                    self.show_menu()
                    choice = self.get_input("Use 1-5").strip().lower()
                    
                    # Check if it's a quit command using regex
                    if self.is_quit_command(choice):
                        print("\n👋 Goodbye! Thanks for using NexusCalc!")
                        self.running = False
                        break
                    
                    if choice not in self.menu_options:
                        print("❌ Invalid choice. Please select 1-5 or 6/q/quit to exit.")
                        continue
                    
                    operation_name, operation_func = self.menu_options[choice]
                    
                    try:
                        num1 = self.get_number("Enter first number")
                        num2 = self.get_number("Enter second number")
                        
                        result = operation_func(num1, num2)
                        print(f"\n✅ Result: {format_result(result)}")
                        
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
            print("\n\n👋 Goodbye! Calculator exited.")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Fatal error: {e}")
            sys.exit(1)
    
    def show_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("🔢 NEXUSCALC - Powerful Calculator")
        print("="*50)
        print("\nWhat are you trying to calculate?")
        print("List:")
        print()
        print("1. Add ➕")
        print("2. Subtract ➖")
        print("3. Multiply ✖️")
        print("4. Divide ➗")
        print("5. Floor 🏠")
        print("6. Quit 🚪")
        print()
        print("💡 Press Ctrl+C to cancel operation")
        print("💡 Type '6', 'q', 'Q', 'quit', or 'QUIT' to exit")
        print("-"*50)
    
    def get_input(self, prompt):
        """Get user input with NEXUSCALC > prompt."""
        try:
            return input(f"{prompt}\nNEXUSCALC > ")
        except KeyboardInterrupt:
            print("\n\n⚠️ Input cancelled.")
            raise
        except EOFError:
            print("\n\n⚠️ End of input detected.")
            raise
    
    def get_number(self, prompt):
        """Get and validate a number from user input."""
        while True:
            try:
                user_input = self.get_input(prompt)
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

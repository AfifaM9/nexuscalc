"""NexusCalc - A powerful calculator application."""

import sys
from .core.calculator import NexusCalc

__version__ = "2.0.0"
__all__ = ["NexusCalc", "start_calc", "nexuscalc", "help"]

def start_calc():
    """Main entry point for the calculator (recommended)."""
    try:
        calc = NexusCalc()
        calc.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Calculator exited.")
        sys.exit(0)
    except EOFError:
        print("\n\n👋 Input stream closed. Calculator exited.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)

def show_help():
    """Display help information."""
    calc = NexusCalc()
    calc.show_help()

# Wrapper class for compatibility
class nexuscalc:
    @staticmethod
    def start_calc():
        """Main entry point for the calculator (recommended)."""
        return start_calc()
    
    @staticmethod
    def help():
        """Show help information."""
        calc = NexusCalc()
        calc.show_help()

# Expose classes and helpers
NexusCalc = NexusCalc
help = show_help

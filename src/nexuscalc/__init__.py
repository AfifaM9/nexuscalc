"""NexusCalc - A powerful calculator application."""

import sys
from .core.calculator import NexusCalc

__version__ = "3.2.0-beta"
__all__ = ["NexusCalc", "start_calc", "nexuscalc", "help", "readme"]

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

def readme():
    """Display the README content."""
    import os
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(readme_path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("📖 README not found locally.")
        print("🌐 View online: https://github.com/AfifaM9/nexuscalc")
        print("📦 PyPI: https://pypi.org/project/nexuscalc/")

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
    
    @staticmethod
    def readme():
        """Display README content."""
        return readme()

# Expose classes and helpers
NexusCalc = NexusCalc
help = show_help

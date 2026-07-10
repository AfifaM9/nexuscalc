# 🔢 NexusCalc

[![PyPI version](https://badge.fury.io/py/nexuscalc.svg)](https://badge.fury.io/py/nexuscalc)
[![Python versions](https://img.shields.io/pypi/pyversions/nexuscalc.svg)](https://pypi.org/project/nexuscalc/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI downloads](https://img.shields.io/pypi/dm/nexuscalc.svg)](https://pypi.org/project/nexuscalc/)
[![Made with ☕](https://img.shields.io/badge/Made%20with-☕-orange.svg)](https://github.com/AfifaM9/nexuscalc)
[![Built with ❤️](https://img.shields.io/badge/Built%20with-❤️-red.svg)](https://github.com/AfifaM9/nexuscalc)

A powerful interactive CLI calculator that just works.

> **NexusCalc** - because sometimes you need to calculate things and your brain said "no."

## ✨ Features

- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract second from first
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide first by second (with zero division error handling)
- 🏠 **Floor** - Floor division (integer result)
- 🔢 **Modulo** - Remainder after division
- ⚡ **Exponent** - Raise first number to the power of second
- √ **Square Root** - Square root of a number
- 🔢 **Floating-point precision** - 0.1 + 0.2 = 0.3 (we fixed it!)
- 🛡️ **Error handling** - Division by zero? We got you
- ⌨️ **Regex quit patterns** - `q`, `Q`, `quit`, `QUIT`, `9`
- 📊 **Calculation counter** - Track your math history
- 🎨 **Beautiful formatting** - Clean, color-coded output
- 💡 **Built-in help** - Type `h` or `help` for documentation
- 🧠 **Keyboard interrupts** - Ctrl+C gracefully handled

## 📦 Installation

```bash
python -m pip install nexuscalc
```

## 🚀 Usage

### Interactive Mode (Recommended)

```python
from nexuscalc import start_calc
start_calc()
```

Or using the wrapper:

```python
from nexuscalc import nexuscalc
nexuscalc.start_calc()
```

Or after installation, just run:

```bash
nexuscalc
```

### Programmatic Usage

```python
from nexuscalc.core.operations import Operations

ops = Operations()

# Basic operations
result = ops.add(5, 3)           # Returns 8
result = ops.subtract(10, 4)     # Returns 6
result = ops.multiply(3, 4)      # Returns 12
result = ops.divide(10, 2)       # Returns 5.0

# Advanced operations
result = ops.floor_divide(10, 3) # Returns 3
result = ops.modulo(10, 3)       # Returns 1
result = ops.exponent(2, 3)      # Returns 8 (2^3)
result = ops.square_root(16)     # Returns 4.0 (√16)
```

## 🎮 Interactive Commands

While using the calculator, you can type:

| Command | Action |
|---------|--------|
| `1` | Add ➕ |
| `2` | Subtract ➖ |
| `3` | Multiply ✖️ |
| `4` | Divide ➗ |
| `5` | Floor 🏠 |
| `6` | Modulo 🔢 |
| `7` | Exponent ⚡ |
| `8` | Square Root √ |
| `9`, `q`, `Q`, `quit`, `QUIT` | Exit calculator |
| `h`, `help`, `?` | Show help |
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit calculator |

## 📝 Examples

```python
from nexuscalc import start_calc

# Start the calculator
start_calc()

# Example session:
# ==================================================
# 🔢 NEXUSCALC - Powerful Calculator
# ==================================================
# 
# 1. Add ➕
# 2. Subtract ➖
# 3. Multiply ✖️
# 4. Divide ➗
# 5. Floor 🏠
# 6. Modulo 🔢
# 7. Exponent ⚡
# 8. Square Root √
# 9. Quit 🚪
# 
# Use 1-9
# NEXUSCALC > 8
# Enter a number
# NEXUSCALC > 16
# 
# ==================================================
# 📊 Calculation #1
# ==================================================
#   √16 = 4.0
# ==================================================
```

## 🛡️ Error Handling

NexusCalc handles errors gracefully:

```python
# Square root of negative number
NEXUSCALC > 8
Enter a number
NEXUSCALC > -16

❌ Error: Cannot take square root of a negative number!

# Division by zero
NEXUSCALC > 4
Enter first number
NEXUSCALC > 10
Enter second number
NEXUSCALC > 0

❌ Division Error: Cannot divide by zero!
💡 Hint: You cannot divide by zero. Please try a different number.
```

## 📋 Version History

| Version | Changes |
|---------|---------|
| **2.6.0** | ✅ **STABLE** - Added Square Root, Quit moved to 9 |
| **2.5.0** | ✅ STABLE - Added Exponent, Quit moved to 8 |
| **2.1.0** | ✅ STABLE - Added Modulo, Quit moved to 7 |
| **2.0.0** | ✅ STABLE - Removed `calculate()`, `start_calc()` is the only entry point |
| **1.1.0** | ✅ STABLE - Added `start_calc()`, deprecated `calculate()` |
| **1.0.0** | ✅ STABLE - Initial release |

## 🧪 Development

Run tests:

```bash
python -m pytest tests/ -v
```

Run tests with coverage:

```bash
python -m pytest tests/ --cov=src/nexuscalc
```

## 📄 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Light Bulb Experiments** © 2026

---

**Made with ❤️ by Light Bulb Experiments**

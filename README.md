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
- 🔢 **Floating-point precision** - 0.1 + 0.2 = 0.3 (we fixed it!)
- 🛡️ **Error handling** - Division by zero? We got you
- ⌨️ **Regex quit patterns** - `q`, `Q`, `quit`, `QUIT`, `8`
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

### Quick Start

```python
# Method 1: Recommended - Direct function
from nexuscalc import start_calc
start_calc()

# Method 2: Recommended - Using wrapper
from nexuscalc import nexuscalc
nexuscalc.start_calc()

# Method 3: Using the class (advanced)
from nexuscalc import NexusCalc
calc = NexusCalc()
calc.run()

# Method 4: Show help
from nexuscalc import nexuscalc
nexuscalc.help()
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
| `8`, `q`, `Q`, `quit`, `QUIT` | Exit calculator |
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
# 8. Quit 🚪
# 
# Use 1-8
# NEXUSCALC > 7
# Enter first number
# NEXUSCALC > 2
# Enter second number
# NEXUSCALC > 3
# 
# ==================================================
# 📊 Calculation #1
# ==================================================
#   2 ^ 3 = 8
# ==================================================
```

## 🛡️ Error Handling

NexusCalc handles errors gracefully:

```python
# Division by zero
NEXUSCALC > 4
Enter first number
NEXUSCALC > 10
Enter second number
NEXUSCALC > 0

❌ Division Error: Cannot divide by zero!
💡 Hint: You cannot divide by zero. Please try a different number.

# Invalid input
NEXUSCALC > 1
Enter first number
NEXUSCALC > hello

❌ Error: 'hello' is not a valid number
💡 Please try again with a valid number.
```

## 📊 Why NexusCalc?

| Feature | NexusCalc | Other Calculators |
|---------|-----------|-------------------|
| CLI Interface | ✅ | ❌ |
| Error Handling | ✅ | ⚠️ |
| Regex Quit Patterns | ✅ | ❌ |
| Floating Point Precision | ✅ | ⚠️ |
| Built-in Help | ✅ | ❌ |
| Calculation Counter | ✅ | ❌ |
| Keyboard Interrupts | ✅ | ❌ |
| Beautiful Output | ✅ | ❌ |
| Modulo Operation | ✅ | ⚠️ |
| Exponent Operation | ✅ | ⚠️ |

## 📋 Version History

| Version | Changes |
|---------|---------|
| **2.5.0** | ✅ **STABLE** - Added Exponent, Quit moved to 8 |
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

## 📁 Project Structure

```
nexuscalc/
├── src/nexuscalc/
│   ├── core/          # Core calculator logic
│   ├── parsers/       # Expression parsing
│   ├── evaluator/     # Expression evaluation
│   ├── utils/         # Utilities and helpers
│   └── exceptions/    # Custom exceptions
├── tests/             # Unit tests
├── examples/          # Usage examples
└── setup.py          # Package setup
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Light Bulb Experiments** © 2026

## 🙏 Acknowledgments

- Built with ☕ and ❤️
- Inspired by the need for a simple, powerful CLI calculator
- Thanks to all users who made this better

## ⭐ Show Your Support

If you find NexusCalc useful, please consider:

- ⭐ Starring the repository on GitHub
- 🐛 Reporting issues
- 💡 Suggesting features
- 🔧 Contributing code

---

**Made with ❤️ by Light Bulb Experiments**

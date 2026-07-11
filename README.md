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
- ⁿ√ **Nth Root** - Nth root of a number
- 🔢 **Percentage** - Calculate percentage of a number
- ❗ **Factorial** - Factorial of a number
- 🔢 **Floating-point precision** - 0.1 + 0.2 = 0.3 (we fixed it!)
- 🛡️ **Error handling** - Division by zero? We got you
- ⌨️ **Regex quit patterns** - `q`, `Q`, `quit`, `QUIT`, `12`
- 📊 **Calculation counter** - Track your math history
- 🎨 **Beautiful formatting** - Clean, color-coded output
- 💡 **Built-in help** - Type `h` or `help` for documentation
- 🧠 **Keyboard interrupts** - Ctrl+C gracefully handled

## 📦 Installation

### Stable Version (Recommended)
```bash
python -m pip install nexuscalc
```

### Beta Version (For Testing)
```bash
python -m pip install nexuscalc==3.2.0b2
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

### Read the README from Terminal

```python
from nexuscalc import readme
readme()
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
result = ops.nth_root(8, 3)      # Returns 2.0 (³√8)
result = ops.percentage(20, 100) # Returns 20.0
result = ops.factorial(5)        # Returns 120
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
| `9` | Nth Root ⁿ√ |
| `10` | Percentage % |
| `11` | Factorial ! |
| `12`, `q`, `Q`, `quit`, `QUIT` | Exit calculator |
| `h`, `help`, `?` | Show help |
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit calculator |

## 📝 Examples

### Percentage Example
```python
from nexuscalc import start_calc

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
# 9. Nth Root ⁿ√
# 10. Percentage %
# 11. Factorial !
# 12. Quit 🚪
# 
# Use 1-12
# NEXUSCALC > 10
# Enter the percentage
# NEXUSCALC > 20
# Enter the number
# NEXUSCALC > 100
# 
# ==================================================
# 📊 Calculation #1
# ==================================================
#   20% of 100 = 20.0
# ==================================================
```

### Factorial Example
```
NEXUSCALC > 11
Enter a number
NEXUSCALC > 5

==================================================
📊 Calculation #2
==================================================
  5! = 120
==================================================
```

### Nth Root Example
```
NEXUSCALC > 9
Enter the number
NEXUSCALC > 8
Enter the root (n)
NEXUSCALC > 3

==================================================
📊 Calculation #3
==================================================
  ³√8 = 2.0
==================================================
```

## 🛡️ Error Handling

NexusCalc handles errors gracefully:

```python
# Even root of negative number
NEXUSCALC > 9
Enter the number
NEXUSCALC > -8
Enter the root (n)
NEXUSCALC > 2

❌ Error: Cannot take even root of a negative number!

# Factorial of negative number
NEXUSCALC > 11
Enter a number
NEXUSCALC > -5

❌ Error: Factorial is not defined for negative numbers!

# Division by zero
NEXUSCALC > 4
Enter first number
NEXUSCALC > 10
Enter second number
NEXUSCALC > 0

❌ Division Error: Cannot divide by zero!
💡 Hint: You cannot divide by zero. Please try a different number.
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
| Square Root Operation | ✅ | ⚠️ |
| Nth Root Operation | ✅ | ❌ |
| Percentage Operation | ✅ | ⚠️ |
| Factorial Operation | ✅ | ⚠️ |

## 📋 Version History

| Version | Status | Changes |
|---------|--------|---------|
| **3.2.0b2** | 🔄 **BETA** | Fixed README inclusion, readme() function |
| **3.2.0b1** | 🔄 BETA | Added Percentage, Factorial, Quit→12 |
| **3.0.0** | ✅ STABLE | Added Nth Root, Quit→10 |
| **2.6.0** | ✅ STABLE | Added Square Root, Quit→9 |
| **2.5.0** | ✅ STABLE | Added Exponent, Quit→8 |
| **2.1.0** | ✅ STABLE | Added Modulo, Quit→7 |
| **2.0.0** | ✅ STABLE | Removed `calculate()`, `start_calc()` only |
| **1.1.0** | ✅ STABLE | Added `start_calc()` |

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

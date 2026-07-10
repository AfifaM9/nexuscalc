# Changelog

All notable changes to NexusCalc will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.6.0] - 2026-07-10

### ✨ Added
- **Square Root** – Calculate the square root of a number (option 8)
  - Single number input required
  - Error handling for negative numbers
- `square_root()` function added to Operations class
- `safe_square_root()` for error-safe square root operations

### 🔄 Changed
- **Quit moved to 9** – The quit option is now number 9
- Menu options reordered (1-8 are operations, 9 is quit)
- Updated help screen to show square root
- Updated prompt to `Use 1-9`

### 🧪 Development
- Added square root tests

---

## [2.5.0] - 2026-07-10

### ✨ Added
- **Exponent** – Raise first number to the power of second (option 7)
- `exponent()` function added to Operations class
- `safe_exponent()` for error-safe power operations

### 🔄 Changed
- Quit moved to 8
- Updated menu and help screen

---

## [2.1.0] - 2026-07-09

### ✨ Added
- **Modulo** – Remainder after division (option 6)
- `modulo()` function added to Operations class
- `safe_modulo()` for error-safe remainder operations

### 🔄 Changed
- Quit moved to 7
- Updated menu and help screen

---

## [2.0.0] - 2026-07-09

### ⚠️ Breaking Changes
- **Removed `calculate()`** – This function has been fully removed
- **Use `start_calc()` instead** – This is now the only entry point
- **Removed `nexuscalc.nexuscalc.calculate()`** – Wrapper method removed

### ✨ Added
- `start_calc()` is now the recommended and only entry point
- Cleaner API with no deprecated functions
- `nexuscalc.start_calc()` wrapper method

### 📝 Migration Guide
```python
# Old (1.x.x)
from nexuscalc import calculate
calculate()

# New (2.0.0)
from nexuscalc import start_calc
start_calc()
```

---

## [1.1.0] - 2026-07-09

### ✨ Added
- `start_calc()` – new recommended entry point
- `nexuscalc.start_calc()` – wrapper method
- `nexuscalc.help()` – help method in wrapper

### ⚠️ Deprecated
- `calculate()` – will be removed in 2.0.0
- `nexuscalc.nexuscalc.calculate()` – will be removed in 2.0.0

### 📝 Migration Notice
```python
# Old (deprecated)
from nexuscalc import calculate
calculate()

# New (recommended)
from nexuscalc import start_calc
start_calc()
```

---

## [1.0.0] - 2026-07-08

### ✨ Added
- Initial release of NexusCalc
- **Core Operations:**
  - Addition (➕)
  - Subtraction (➖)
  - Multiplication (✖️)
  - Division (➗) with zero division error handling
  - Floor division (🏠)
- **Features:**
  - Interactive CLI menu
  - Error handling for invalid inputs
  - Regex quit patterns (`q`, `Q`, `quit`, `QUIT`, `6`)
  - Calculation counter
  - Clean result formatting
  - Keyboard interrupt handling (Ctrl+C)
  - EOF handling (Ctrl+D)
  - Built-in help system (`h`, `help`, `?`)
- **Programmatic Usage:**
  - `Operations` class with all operations
  - `NexusCalc` class for interactive mode
- **Project Structure:**
  - Modular design with core, parsers, evaluator, utils, exceptions
  - Unit tests for all functionality
  - Examples for basic and advanced usage

### 📦 Package
- Published to PyPI
- MIT License
- Python 3.7+ support
- Cross-platform (Windows, macOS, Linux)

---

## Upcoming Features

### [2.7.0] - Planned
- Percentage (%) operation
- Enhanced input validation

### [2.8.0] - Planned
- Factorial (!) operation
- Memory functions

### [2.9.0] - Planned
- Trigonometric functions (sin, cos, tan)
- Logarithmic functions

### [3.0.0] - Planned
- Scientific calculator mode
- Constants library (π, e, golden ratio)
- History tracking

---

## Legend

- ✨ **Added** – New features
- 🔄 **Changed** – Changes to existing functionality
- ⚠️ **Deprecated** – Soon-to-be removed features
- ❌ **Removed** – Removed features
- 🐛 **Fixed** – Bug fixes
- 🛡️ **Security** – Security improvements
- 📝 **Documentation** – Documentation updates
- 🧪 **Development** – Development/Testing updates

---

**Made with ❤️ by Light Bulb Experiments**

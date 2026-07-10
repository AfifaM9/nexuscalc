# Changelog

## [2.5.0-rc.1] - 2024-07-10

### ✨ Added
- **Exponent operation** – Raise first number to the power of second (option 7)
- Power calculation with `**` operator

### 🔄 Changed
- **Quit moved to 8** – The quit option is now number 8
- Menu options reordered (1-7 are operations, 8 is quit)
- Updated help screen to show exponent

### 🧪 New Features
- `exponent()` function added to Operations class
- `safe_exponent()` for error-safe power operations

---

## [2.1.0] - 2024-07-09

### ✨ Added
- Modulo operation (option 6)

### 🔄 Changed
- Quit moved to 7

---

## [2.0.0] - 2024-07-09

### ⚠️ Breaking Changes
- Removed `calculate()` – use `start_calc()` instead

---

## [1.1.0] - 2024-07-09

### ✨ Added
- `start_calc()` – new recommended entry point

### ⚠️ Deprecated
- `calculate()` – will be removed in 2.0.0

---

## [1.0.0] - 2024-07-08

### ✨ Added
- Initial release
- Addition, Subtraction, Multiplication, Division, Floor
- Error handling, Help system, Calculation counter

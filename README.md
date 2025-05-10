# DNA Pattern Finder

DNA Pattern Finder is a Python-based application that allows users to input a DNA sequence and highlight known patterns or custom markers within that sequence. Through a user-friendly Tkinter interface, patterns like codons, regulatory elements, and repeats can be detected and visualized quickly.

## Features
- A collection of predefined, biologically meaningful patterns (e.g., start/stop codons and repeats).
- Support for user-defined custom patterns.
- Overlapping matches are identified and highlighted.
- GUI with color-coded highlights for different pattern types.

## Requirements
- Python 3.x
- Tkinter (usually included with standard Python installations)
- (Optional) Virtual environment to isolate dependencies.

## Installation
1. Clone or download this repository.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```
## Usage
1. Run the application:
   ```bash
   python dnapatternfinder.py
   ```
2. Enter your DNA sequence in the text area.
3. (Optional) Specify a custom pattern in the text box.
4. Click the “Highlight Patterns” button to see color-coded matches.

## Custom Pattern Detection
- For patterns not pre-listed in the dictionary, simply type them into the “Custom pattern” field and click “Highlight Patterns.” Any matches will be highlighted in pink.

## License
This project is distributed under the MIT License (see LICENSE file for details).

## Contributing
Contributions are welcome! Feel free to create a fork, make changes, and submit a pull request.

## Contact
For questions or feedback, open an issue or contact the repository maintainer.

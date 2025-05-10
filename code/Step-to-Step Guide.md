# Step-to-Step Guide

Follow these steps to get the DNA Pattern Finder up and running on your system.

## 1. Installation
1. Ensure Python 3.x is installed on your machine.
2. Clone or download the repository:
   ```bash
   git clone https://github.com/username/dna-pattern-finder.git
   ```
3. (Optional) Create a virtual environment in the cloned directory:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```
4. Install any dependencies (if listed in requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

## 2. Running the Tool
1. Navigate to the project directory in your terminal or command prompt.
2. Run the main script:
   ```bash
   python dnapatternfinder.py
   ```
3. A Tkinter window should launch if all dependencies are met.

## 3. Using the App
1. Enter a DNA sequence (e.g., "ATGACGTAG...") in the text box.
2. To detect a known pattern (e.g., "Start Codon (ATG)"), simply click “Highlight Patterns.”
3. (Optional) Enter a custom marker in the “Custom pattern” field (e.g., “ACGT”).
4. Click the “Highlight Patterns” button. All matches will be highlighted in color-coded backgrounds according to their category.
5. Click “Clear Highlights” to remove any existing highlights before searching again.

## 4. Customizing Patterns
- You can modify or add patterns in the code by editing the KNOWN_PATTERNS dictionary near the top of the file. For example, add a new key-value pair to detect additional markers.

## 5. Troubleshooting
- If the GUI does not appear, ensure Tkinter is properly installed (usually included by default in most Python distributions).
- Check the console for error messages if patterns are not highlighted as expected.

## 6. Contributing
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit and push your changes to your branch.
4. Create a pull request detailing your modifications.

Enjoy exploring and decoding DNA sequences with the DNA Pattern Finder!

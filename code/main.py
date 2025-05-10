import tkinter as tk
from tkinter import messagebox

# Dictionary of biologically meaningful DNA patterns
KNOWN_PATTERNS = {
    # --- Gene Markers ---
    "Start Codon (ATG)": "ATG",
    "Stop Codon (TAA)": "TAA",
    "Stop Codon (TAG)": "TAG",
    "Stop Codon (TGA)": "TGA",

    # --- Promoters and Regulatory Elements ---
    "TATA Box (promoter)": "TATA",
    "CAAT Box (regulatory sequence)": "CAAT",
    "GC Box (GCGC)": "GCGC",

    # --- Repetitive Sequences / Microsatellites ---
    "AT Repeats (ATAT)": "ATAT",
    "CG Repeats (CGCG)": "CGCG",
    "GAGA Repeats": "GAGA",

    # --- Fictional & Known Markers ---
    "GATTACA Marker": "GATTACA",
    "Telomere Repeat (TTAGGG)": "TTAGGG",

    # --- Custom Learning & Pattern Test ---
    "Palindrome CGCG": "CGCG",
    "Random Marker ACGT": "ACGT"
}

def find_patterns(sequence, pattern):
    """
    Return a list of (start_index, end_index) for all occurrences of 'pattern' in 'sequence',
    including overlapping occurrences.
    """
    matches = []
    start = 0
    while True:
        start = sequence.find(pattern, start)
        if start == -1:
            break
        matches.append((start, start + len(pattern)))
        start += 1  # For overlapping matches, increment by 1 instead of len(pattern)
    return matches

def highlight_patterns():
    """
    Searches for multiple known patterns plus any custom pattern,
    highlighting all occurrences in the DNA sequence text widget.
    """
    # Remove old tags
    text_area.tag_remove("highlight0", "1.0", tk.END)
    text_area.tag_remove("highlight1", "1.0", tk.END)
    text_area.tag_remove("highlight2", "1.0", tk.END)
    text_area.tag_remove("highlight3", "1.0", tk.END)
    text_area.tag_remove("highlight4", "1.0", tk.END)
    text_area.tag_remove("highlight5", "1.0", tk.END)
    text_area.tag_remove("highlight6", "1.0", tk.END)
    text_area.tag_remove("highlight7", "1.0", tk.END)
    text_area.tag_remove("highlight8", "1.0", tk.END)
    text_area.tag_remove("highlight9", "1.0", tk.END)
    text_area.tag_remove("highlight_custom", "1.0", tk.END)

    sequence = text_area.get("1.0", tk.END).strip()
    custom_pat = custom_entry.get().strip()

    # Basic validation
    if not sequence:
        messagebox.showinfo("Error", "Please enter a DNA sequence in the text area.")
        return

    # Iterate through known patterns
    patterns_list = list(KNOWN_PATTERNS.values())
    pattern_keys = list(KNOWN_PATTERNS.keys())

    for idx, pattern_value in enumerate(patterns_list):
        color_tag = f"highlight{idx}"
        # Alternate background colors for clarity
        highlight_color = "yellow" if idx % 2 == 0 else "cyan"
        text_area.tag_configure(color_tag, background=highlight_color)

        matches = find_patterns(sequence, pattern_value)
        for start_idx, end_idx in matches:
            start_pos = f"1.0 + {start_idx}c"
            end_pos = f"1.0 + {end_idx}c"
            text_area.tag_add(color_tag, start_pos, end_pos)

    # Highlight custom pattern if provided
    if custom_pat:
        text_area.tag_configure("highlight_custom", background="pink")
        custom_matches = find_patterns(sequence, custom_pat)
        for start_idx, end_idx in custom_matches:
            start_pos = f"1.0 + {start_idx}c"
            end_pos = f"1.0 + {end_idx}c"
            text_area.tag_add("highlight_custom", start_pos, end_pos)

def clear_highlights():
    """
    Clears all highlight tags from the text widget.
    """
    for idx in range(len(KNOWN_PATTERNS)):
        text_area.tag_remove(f"highlight{idx}", "1.0", tk.END)
    text_area.tag_remove("highlight_custom", "1.0", tk.END)

def main():
    global text_area, custom_entry

    root = tk.Tk()
    root.title("Digital DNA Pattern Finder")

    # Frame for text area
    text_frame = tk.Frame(root)
    text_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # DNA sequence label & text area
    seq_label = tk.Label(text_frame, text="Enter DNA sequence below:")
    seq_label.pack(anchor="w")

    text_area = tk.Text(text_frame, wrap="word", height=10, width=50)
    text_area.pack(fill="both", expand=True)

    # Frame for custom pattern input
    custom_frame = tk.Frame(root)
    custom_frame.pack(padx=10, pady=5, fill="x")

    custom_label = tk.Label(custom_frame, text="Custom pattern:")
    custom_label.pack(side="left")

    custom_entry = tk.Entry(custom_frame, width=20)
    custom_entry.pack(side="left", padx=(5, 10))

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(padx=10, pady=5, fill="x")

    highlight_btn = tk.Button(button_frame, text="Highlight Patterns", command=highlight_patterns)
    highlight_btn.pack(side="left", padx=5)

    clear_btn = tk.Button(button_frame, text="Clear Highlights", command=clear_highlights)
    clear_btn.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()

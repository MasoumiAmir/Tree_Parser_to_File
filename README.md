#Directory Structure Generator 🗂️

A Python script that automatically creates files and folders based on a text-based tree diagram input. Perfect for quickly setting up project structures!

Key Features ✨
Text-to-Structure Conversion: Parses structure.txt to generate complete directory hierarchies

Cross-Platform: Works on Windows, macOS, and Linux

Smart Parsing:

Handles │, ├──, and └── symbols

Ignores comments and emojis

Auto-detects files vs directories

Safe Output: Creates everything inside an Output folder

Error Handling: Detailed error messages with line numbers

Installation & Usage 🚀

bash

# Clone repository
git clone https://github.com/yourusername/directory-structure-generator.git
cd directory-structure-generator

# Create your structure file
nano structure.txt

# Run the generator
python tree_parser.py
Sample Input 📝
structure.txt:

Copy
my-project/
│
├── src/
│   ├── __init__.py
│   └── main.py
│
└── README.md
Customization ⚙️
Change output directory: Modify output_dir in code

Use different input file: Update input_file parameter

Adjust parsing rules: Edit clean_line() method

License 📄
MIT License - Free for personal and commercial use

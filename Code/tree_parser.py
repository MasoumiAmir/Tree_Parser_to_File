import os
import re
import sys
from pathlib import Path

class TreeParser:
    def __init__(self, input_file='structure.txt'):
        self.input_file = input_file
        self.path_stack = []
        self.root_dir = None
        self.line_number = 0
        self.output_dir = Path("Output")

    def clean_line(self, line):
        line = re.sub(r'[│├└─➤📁📄]', '', line)
        line = re.sub(r'#.*', '', line)
        line = re.sub(r'\s+', ' ', line)
        return line.strip()

    def parse_line(self, line):
        self.line_number += 1
        original_line = line
        cleaned_line = self.clean_line(line)
        
        if not cleaned_line:
            return

        indent = 0
        while original_line.startswith(('│', '├──', '└──', '    ')):
            original_line = original_line[4:]
            indent += 1

        parts = cleaned_line.split()
        if not parts:
            return

        name = parts[0].rstrip('/')
        is_dir = '/' in cleaned_line or len(parts) > 1 or not '.' in name.split('/')[-1]

        while indent < len(self.path_stack):
            self.path_stack.pop()

        parent = self.path_stack[-1] if self.path_stack else self.root_dir
        new_path = parent / name

        try:
            if is_dir:
                new_path.mkdir(exist_ok=True, parents=True)
                print(f"Created directory: {new_path}")
                self.path_stack.append(new_path)
            else:
                new_path.parent.mkdir(exist_ok=True, parents=True)
                new_path.touch(exist_ok=True)
                print(f"Created file: {new_path}")

        except Exception as e:
            print(f"Error at line {self.line_number}: {str(e)}")
            sys.exit(1)

    def parse(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: Required file '{self.input_file}' not found")
            sys.exit(1)

        # Create Output directory
        self.output_dir.mkdir(exist_ok=True)
        
        # Set root directory inside Output
        root_line = self.clean_line(lines[0])
        root_name = root_line.split()[0]
        self.root_dir = self.output_dir / root_name
        self.root_dir.mkdir(exist_ok=True)
        self.path_stack = [self.root_dir]

        for line in lines[1:]:
            self.parse_line(line)

if __name__ == "__main__":
    parser = TreeParser()
    parser.parse()
    print("\nProject structure created successfully in Output folder!")
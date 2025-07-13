#!/usr/bin/env python3
import os
import re

def update_imports(root_dir):
    tests_dir = os.path.join(root_dir, 'tests')
    
    for dirpath, _, filenames in os.walk(tests_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # Update imports from the moved modules
                    updated_content = re.sub(
                        r'from (application|domain|errors|infra|ioc|presentation|utils)\.', 
                        r'from src.\1.', 
                        content
                    )
                    updated_content = re.sub(
                        r'import (application|domain|errors|infra|ioc|presentation|utils)\.', 
                        r'import src.\1.', 
                        updated_content
                    )
                    
                    # Update string literals used in decorators like @patch
                    updated_content = re.sub(
                        r"@patch\(['\"](?!src\.)(application|domain|errors|infra|ioc|presentation|utils)\.",
                        r"@patch('src.\2.",
                        updated_content
                    )
                    
                    # Update any other string reference to modules
                    updated_content = re.sub(
                        r"['\"](?!src\.)(application|domain|errors|infra|ioc|presentation|utils)\.",
                        r"'src.\1.",
                        updated_content
                    )
                    
                    if content != updated_content:
                        print(f"Updating: {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(updated_content)
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    
    # Also check for top-level Python files
    for filename in os.listdir(root_dir):
        if filename.endswith('.py') and filename != 'update_imports.py':
            filepath = os.path.join(root_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Update imports from the moved modules
                updated_content = re.sub(
                    r'from (application|domain|errors|infra|ioc|presentation|utils)\.', 
                    r'from src.\1.', 
                    content
                )
                updated_content = re.sub(
                    r'import (application|domain|errors|infra|ioc|presentation|utils)\.', 
                    r'import src.\1.', 
                    updated_content
                )
                
                # Update string literals used in decorators like @patch
                updated_content = re.sub(
                    r"@patch\(['\"](?!src\.)(application|domain|errors|infra|ioc|presentation|utils)\.",
                    r"@patch('src.\2.",
                    updated_content
                )
                
                # Update any other string reference to modules
                updated_content = re.sub(
                    r"['\"](?!src\.)(application|domain|errors|infra|ioc|presentation|utils)\.",
                    r"'src.\1.",
                    updated_content
                )
                
                if content != updated_content:
                    print(f"Updating: {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(updated_content)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath(__file__))
    update_imports(root_dir)
    print("Import paths updated successfully!")

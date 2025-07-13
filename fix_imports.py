#!/usr/bin/env python3
import os
import re

def fix_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Substitui importações como "from application." por "from src.application."
    new_content = re.sub(r'from\s+application\.', 'from src.application.', content)
    
    # Substitui importações como "from presentation." por "from src.presentation."
    new_content = re.sub(r'from\s+presentation\.', 'from src.presentation.', new_content)
    
    # Substitui importações como "from domain." por "from src.domain."
    new_content = re.sub(r'from\s+domain\.', 'from src.domain.', new_content)
    
    # Substitui importações como "from infra." por "from src.infra."
    new_content = re.sub(r'from\s+infra\.', 'from src.infra.', new_content)
    
    # Substitui importações como "from utils." por "from src.utils."
    new_content = re.sub(r'from\s+utils\.', 'from src.utils.', new_content)
    
    # Substitui importações como "from ioc." por "from src.ioc."
    new_content = re.sub(r'from\s+ioc\.', 'from src.ioc.', new_content)
    
    # Corrigir strings em decoradores como @patch
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(application)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(domain)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(errors)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(infra)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(ioc)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(presentation)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    new_content = re.sub(
        r"@patch\(['\"](?!src\.)(utils)\.", 
        r"@patch('src.\1.", 
        new_content
    )
    
    # Corrigir outras strings com referências a módulos
    for module in ['application', 'domain', 'errors', 'infra', 'ioc', 'presentation', 'utils']:
        new_content = re.sub(
            fr"['\"](?!src\.){module}\.",
            f"'src.{module}.",
            new_content
        )
    
    if content != new_content:
        with open(file_path, 'w') as file:
            file.write(new_content)
        return True
    return False

def process_directory(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if fix_imports(file_path):
                    print(f"Corrigido: {file_path}")
                    count += 1
    return count

def process_tests_directory(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if fix_imports(file_path):
                    print(f"Corrigido: {file_path}")
                    count += 1
    return count

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, 'src')
    tests_dir = os.path.join(base_dir, 'tests')
    
    count_src = process_directory(src_dir)
    count_tests = process_tests_directory(tests_dir)
    
    print(f"\nTotal de arquivos corrigidos: {count_src + count_tests}")
    print(f"- Arquivos em src/: {count_src}")
    print(f"- Arquivos em tests/: {count_tests}")

#!/usr/bin/env python3
"""
Script para adicionar anotações de tipo básicas a funções Python.
Este script procura funções sem anotações de tipo e adiciona anotações 'Any'.
É uma solução temporária enquanto você adiciona tipos mais específicos.
"""
import os
import re
from pathlib import Path
import argparse

def add_return_annotation(content, lineno, line):
    """Adiciona uma anotação de retorno -> Any a uma função."""
    if "def " in line and "-> " not in line:
        # Se a linha termina com : então adicione antes
        if line.strip().endswith(":"):
            new_line = line.rstrip(":\n") + " -> Any:\n"
            return content.replace(line, new_line)
        return content
    return content

def add_param_annotations(content, file_path):
    """Adiciona anotações de parâmetro Any para funções."""
    lines = content.split("\n")
    modified_lines = []
    
    for i, line in enumerate(lines):
        if "def " in line and "(" in line and ")" in line:
            # Extrair os parâmetros entre parênteses
            match = re.search(r"def\s+\w+\s*\((.*?)\)", line)
            if match:
                params = match.group(1).strip()
                if params and not any(p for p in params.split(",") if ":" in p) and params != "self":
                    # Transformar os parâmetros não tipados em tipados com Any
                    new_params = []
                    for param in params.split(","):
                        param = param.strip()
                        if param and param != "self" and ":" not in param and "=" not in param:
                            new_params.append(f"{param}: Any")
                        elif param and "=" in param and ":" not in param:
                            name, default = param.split("=", 1)
                            new_params.append(f"{name.strip()}: Any = {default.strip()}")
                        else:
                            new_params.append(param)
                    
                    # Substituir os parâmetros na linha original
                    if "self" in params and "," in params:
                        new_param_str = "self, " + ", ".join([p for p in new_params if p != "self"])
                    else:
                        new_param_str = ", ".join(new_params)
                    
                    new_line = re.sub(r"\((.*?)\)", f"({new_param_str})", line)
                    modified_lines.append(new_line)
                    continue
        modified_lines.append(line)
    
    return "\n".join(modified_lines)

def process_file(file_path):
    """Processa um arquivo Python adicionando anotações de tipo."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar se precisamos importar Any
    if "from typing import " in content:
        if "from typing import Any" not in content:
            content = content.replace("from typing import ", "from typing import Any, ")
    else:
        # Adicionar importação de Any
        content = "from typing import Any\n" + content
    
    # Adicionar anotações aos parâmetros
    content = add_param_annotations(content, file_path)
    
    # Adicionar anotações de retorno
    lines = content.split("\n")
    for i, line in enumerate(lines):
        content = add_return_annotation(content, i+1, line + "\n")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Processado: {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Adicionar anotações de tipo a arquivos Python.')
    parser.add_argument('--path', default='src', help='Caminho para procurar arquivos Python')
    args = parser.parse_args()
    
    # Lista todos os arquivos Python no caminho
    for root, dirs, files in os.walk(args.path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    main()

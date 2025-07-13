#!/usr/bin/env python3
"""
Script para corrigir importações após mover módulos para pasta src/
Corrige imports simples e também caminhos em decoradores como @patch
"""
import os
import re
import sys

def fix_all_imports(root_dir):
    """
    Função principal que corrige todas as importações
    """
    print(f"Iniciando correção de importações no diretório: {root_dir}")
    
    tests_dir = os.path.join(root_dir, 'tests')
    src_dir = os.path.join(root_dir, 'src')
    
    files_fixed = 0
    # Corrigir arquivos na pasta tests/
    if os.path.exists(tests_dir):
        print(f"\nProcessando arquivos em: {tests_dir}")
        files_fixed += process_directory(tests_dir)
    
    # Corrigir arquivos na pasta src/
    if os.path.exists(src_dir):
        print(f"\nProcessando arquivos em: {src_dir}")
        files_fixed += process_directory(src_dir)
    
    # Corrigir arquivos Python na raiz
    print(f"\nProcessando arquivos Python na raiz: {root_dir}")
    for filename in os.listdir(root_dir):
        if filename.endswith('.py') and filename != os.path.basename(__file__):
            file_path = os.path.join(root_dir, filename)
            if fix_imports(file_path):
                print(f"  Corrigido: {filename}")
                files_fixed += 1
    
    print(f"\nTotal de arquivos corrigidos: {files_fixed}")
    return files_fixed

def fix_imports(file_path):
    """
    Corrige importações em um arquivo
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Backup do conteúdo original
        original_content = content
        
        # Substitui importações 'from module.' por 'from src.module.'
        for module in ['application', 'domain', 'errors', 'infra', 'ioc', 'presentation', 'utils']:
            content = re.sub(
                r'from\s+' + module + r'\.', 
                'from src.' + module + '.', 
                content
            )
            content = re.sub(
                r'import\s+' + module + r'\.', 
                'import src.' + module + '.', 
                content
            )
        
        # Substitui strings em decoradores @patch
        for module in ['application', 'domain', 'errors', 'infra', 'ioc', 'presentation', 'utils']:
            content = re.sub(
                r'@patch\([\'"](?!src\.)' + module + r'\.', 
                '@patch(\'src.' + module + '.', 
                content
            )
        
        # Substitui outras strings com referências a módulos
        for module in ['application', 'domain', 'errors', 'infra', 'ioc', 'presentation', 'utils']:
            content = re.sub(
                r'[\'"](?!src\.)' + module + r'\.', 
                '\'src.' + module + '.', 
                content
            )
        
        # Salva o arquivo apenas se houve alterações
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"  ERRO ao processar {file_path}: {e}")
        return False

def process_directory(directory):
    """
    Processa todos os arquivos Python em um diretório (recursivamente)
    """
    files_fixed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                try:
                    rel_path = os.path.relpath(file_path, directory)
                    if fix_imports(file_path):
                        print(f"  Corrigido: {rel_path}")
                        files_fixed += 1
                except Exception as e:
                    print(f"  ERRO ao processar {file_path}: {e}")
    
    return files_fixed

if __name__ == '__main__':
    # Use o diretório atual ou o diretório fornecido como argumento
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    fixed = fix_all_imports(root_dir)
    
    if fixed > 0:
        print(f"\nCorrigidos {fixed} arquivos com sucesso!")
    else:
        print("\nNenhum arquivo precisou ser corrigido.")

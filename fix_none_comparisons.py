import re

def fix_none_comparisons(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Substituir todas as comparações com None
        content = re.sub(r'([a-zA-Z0-9_.]+)\s*==\s*None', r'\1 is None', content)
        content = re.sub(r'([a-zA-Z0-9_.]+)\s*!=\s*None', r'\1 is not None', content)
        
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Arquivo {file_path} corrigido com sucesso.")
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")

# Corrigir os arquivos específicos
files_to_fix = [
    'src/infra/models/category_model.py',
    'src/infra/models/product_model.py'
]

for file_path in files_to_fix:
    try:
        fix_none_comparisons(file_path)
    except:
        print(f"Não foi possível corrigir {file_path}")

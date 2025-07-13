try:
    with open('src/infra/category/repositories/event_category_repository.py', 'r') as f:
        content = f.read()
    
    # Substituir categoryEvent por category_event
    content = content.replace('categoryEvent', 'category_event')
    
    with open('src/infra/category/repositories/event_category_repository.py', 'w') as f:
        f.write(content)
    
    print("Arquivo corrigido com sucesso!")
except Exception as e:
    print(f"Erro ao corrigir o arquivo: {e}")

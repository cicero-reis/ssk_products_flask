class ProductEventDTO:
    def __init__(self, id, product_id, action, data, version, timestamp):
        self.id = id
        self.product_id = product_id
        self.action = action
        self.data = data
        self.version = version  # Adicionando atributo que estava faltando
        self.timestamp = timestamp

    @staticmethod
    def from_entity(event):
        return ProductEventDTO(
            id=event.id,
            product_id=event.product_id,
            action=event.action,
            data=event.data,
            version=event.version,  # Adicionando o parâmetro version
            timestamp=event.timestamp,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,  # Corrigindo para product_id em vez de name
            "action": self.action,  # Corrigindo para action em vez de description
            "data": self.data,  # Corrigindo para data em vez de price
            "version": self.version,  # Adicionando version
            "timestamp": self.timestamp,  # Adicionando timestamp
        }

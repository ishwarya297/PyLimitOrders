from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener

class LimitOrderAgent(PriceListener):
    def __init__(self, execution_client: ExecutionClient) -> None:
        super().__init__()
        self.execution_client = execution_client
        self.orders = []

    def add_order(self, buy_order: bool, product_id: str, amount: int, limit_price: float):
        if buy_order == True:
            buy_type = 'buy'
        else:
            buy_type = 'sell'
        self.orders.append(buy_type, product_id, amount, limit_price)

    def on_price_tick(self, product_id: str, current_price: float):
        product_id_price = {'ibm': 2000, 'cts': 3000, 'tata': 900, 'hdfc': 800}
        if product_id in product_id_price:
            self.current_price = product_id_price[product_id]
            return self.current_price
        else:
            return None

    def execution_method(self, prod_lis: list):
        limit_price: float = 1000.0
        for product_id in prod_lis:  # Corrected variable name
            amount = self.on_price_tick(product_id)
            if amount is not None:
                if amount < limit_price:
                    buy_order = True
                else:
                    buy_order = False
                self.add_order(buy_order, product_id, amount, limit_price)

execution_client = ExecutionClient()

# Create an instance of LimitOrderAgent with the execution client
obj = LimitOrderAgent(execution_client)

# Define product list
product_lis = ['ibm', 'hdfc', 'tata']

# Call execution method
obj.execution_method(product_lis)

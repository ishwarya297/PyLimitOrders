import unittest
from unittest.mock import MagicMock
from trading_framework.execution_client import ExecutionClient
from limit_order_agent import LimitOrderAgent

class TestLimitOrderAgent(unittest.TestCase):

    def setUp(self):
        # Create a mock execution client
        self.execution_client = MagicMock(spec=ExecutionClient)

        # Initialize LimitOrderAgent with the mock execution client
        self.agent = LimitOrderAgent(self.execution_client)

    def test_add_order_buy(self):
        # Add a buy order
        self.agent.add_order(buy_order=True, product_id='ibm', amount=100, limit_price=50.0)

        # Assert that the order was added correctly
        self.assertEqual(len(self.agent.orders), 1)
        self.assertEqual(self.agent.orders[0], ('buy', 'ibm', 100, 50.0))

    def test_add_order_sell(self):
        # Add a sell order
        self.agent.add_order(buy_order=False, product_id='cts', amount=200, limit_price=60.0)

        # Assert that the order was added correctly
        self.assertEqual(len(self.agent.orders), 1)
        self.assertEqual(self.agent.orders[0], ('sell', 'cts', 200, 60.0))

    def test_execution_method(self):
        # Mock the on_price_tick method to return a known value
        self.agent.on_price_tick = MagicMock(return_value=800)

        # Call execution method
        self.agent.execution_method(['ibm', 'hdfc', 'tata'])

        # Assert that add_order is called with correct arguments
        self.execution_client.buy.assert_called_once_with('hdfc', 800, 1000.0)

if __name__ == '__main__':
    unittest.main()

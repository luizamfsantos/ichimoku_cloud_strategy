from strategy.strategy_ichimoku import (
    calculate_conversion_line, 
    calculate_baseline, 
    calculate_leading_span_A, 
    calculate_leading_span_B,
    calculate_lagging_span,
    calculate_cloud,
    IchimokuStrategy
)
import pandas as pd
from pathlib import Path
from unittest import TestCase
from data_market.datalake import load_data

class IchimokuTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = load_data()
        cls.ticker = 'PETR4'
        cls.stock_data = cls.data['prices_complete'].copy()
        cls.stock_data = cls.stock_data[cls.stock_data['Symbol'] == cls.ticker].copy().sort_values('Date').reset_index(drop=True)
        cls.strategy = IchimokuStrategy()

    def test_calculate_conversion_line(self):
        self.stock_data['conversion_line'] = calculate_conversion_line(self.stock_data)
        self.assertTrue('conversion_line' in self.stock_data.columns)
    
    def test_calculate_baseline(self):
        self.stock_data['baseline'] = calculate_baseline(self.stock_data)
        self.assertTrue('baseline' in self.stock_data.columns)

    def test_calculate_leading_span_A(self):
        self.stock_data['leading_span_A'] = calculate_leading_span_A(self.stock_data)
        self.assertTrue('leading_span_A' in self.stock_data.columns)

    def test_calculate_leading_span_B(self):
        self.stock_data['leading_span_B'] = calculate_leading_span_B(self.stock_data)
        self.assertTrue('leading_span_B' in self.stock_data.columns)

    def test_calculate_lagging_span(self):
        self.stock_data['lagging_span'] = calculate_lagging_span(self.stock_data)
        self.assertTrue('lagging_span' in self.stock_data.columns)

    def test_calculate_cloud(self):
        self.stock_data['cloud'] = calculate_cloud(self.stock_data)
        self.assertTrue('cloud' in self.stock_data.columns)
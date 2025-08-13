import os
import csv
import tempfile
import pytest
from ledger import Ledger

def test_ledger_creates_new_csv():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_ledger.csv')
        ledger = Ledger(file_path)
        assert os.path.exists(file_path)
        with open(file_path, 'r', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            assert header == ['date', 'description', 'amount', 'type']

def test_add_transaction_and_read_csv():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_ledger.csv')
        ledger = Ledger(file_path)
        ledger.add_transaction('2025-08-13', 'Salary', 1000.0, 'income')
        with open(file_path, 'r', newline='') as f:
            reader = list(csv.reader(f))
            assert reader[1] == ['2025-08-13', 'Salary', '1000.0', 'income']

def test_get_balance_income_and_expense():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_ledger.csv')
        ledger = Ledger(file_path)
        ledger.add_transaction('2025-08-13', 'Salary', 1000.0, 'income')
        ledger.add_transaction('2025-08-14', 'Groceries', 200.0, 'expense')
        assert ledger.get_balance() == 800.0

def test_get_transaction_history():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_ledger.csv')
        ledger = Ledger(file_path)
        ledger.add_transaction('2025-08-13', 'Salary', 1000.0, 'income')
        ledger.add_transaction('2025-08-14', 'Groceries', 200.0, 'expense')
        history = ledger.get_transaction_history()
        assert len(history) == 2
        assert history[0]['description'] == 'Salary'
        assert history[1]['description'] == 'Groceries'
        
def test_loading_existing_ledger():
    """
    Tests that the Ledger class can correctly load and process an existing CSV file.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'existing_ledger.csv')

        # 1. Setup: Manually create a pre-existing CSV file.
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'description', 'amount', 'type'])
            writer.writerow(['2025-08-15', 'Old Income', 500.0, 'income'])

        # 2. Execution: Create a new Ledger object pointing to the existing file.
        # This will run the 'else' block we want to test.
        ledger = Ledger(file_path)

        # 3. Assertion: Check if the data was loaded correctly into memory.
        assert len(ledger.entries) == 1
        assert ledger.get_balance() == 500.0
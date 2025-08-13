import csv
import os
from typing import List, Dict, Union

class Ledger:
    """Manages financial transactions by reading from and writing to a CSV file."""

    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.entries: List[Dict[str, Union[str, float]]] = []
        self._initialize_ledger()

    def _initialize_ledger(self):
        """Private method to create the CSV or load existing entries into memory."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['date', 'description', 'amount', 'type'])
        else:
            self.entries = self.get_transaction_history()

    def add_transaction(self, date: str, description: str, amount: float, type: str):
        """Adds a new transaction to the CSV file and updates the in-memory list."""
        new_entry = {
            'date': date,
            'description': description,
            'amount': amount,
            'type': type
        }
        # Add to our in-memory list first
        self.entries.append(new_entry)
        
        # Then, append it to the CSV file
        with open(self.file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, description, amount, type])

    def get_balance(self) -> float:
        """Calculates the balance from the transactions stored in memory."""
        total = 0.0
        for entry in self.entries:
            amount = float(entry['amount'])
            if entry['type'] == 'income':
                total += amount
            else:  # expense
                total -= amount
        return total

    def get_transaction_history(self) -> List[Dict[str, Union[str, float]]]:
        """Reads all transactions from the CSV file into a list of dictionaries."""
        transactions = []
        with open(self.file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                transactions.append(row)
        return transactions

import click
from .ledger import Ledger

@click.group()
@click.pass_context
def cli(ctx):
	"""
	A simple CLI for managing a financial ledger.
	"""
	pass

@cli.command()
@click.argument('file_path', type=click.Path())
@click.argument('date')
@click.argument('description')
@click.argument('amount', type=float)
@click.argument('type', type=click.Choice(['income', 'expense']))
def add(file_path, date, description, amount, type):
	"""Add a transaction to the ledger CSV file."""
	ledger = Ledger(file_path)
	ledger.add_transaction(date, description, amount, type)
	click.echo(f"Transaction added: {date}, {description}, {amount}, {type}")

@cli.command()
@click.argument('file_path', type=click.Path())
def balance(file_path):
	"""Show the current balance from the ledger CSV file."""
	ledger = Ledger(file_path)
	bal = ledger.get_balance()
	click.echo(f"Current balance: {bal}")

@cli.command()
@click.argument('file_path', type=click.Path())
def history(file_path):
	"""Show the transaction history from the ledger CSV file."""
	ledger = Ledger(file_path)
	transactions = ledger.get_transaction_history()
	if transactions:
		click.echo("--- Transaction History ---")
		for entry in transactions:
			click.echo(f"{entry['date']}, {entry['description']}, {entry['amount']}, {entry['type']}")
	else:
		click.echo("No transactions found.")

if __name__ == "__main__":
	cli()

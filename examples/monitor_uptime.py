import time
from ping3 import ping, verbose_ping
from rich.console import Console
from rich.table import Table

# List of targets
targets = ['nrk.no', 'vg.no','192.168.0.100']

# Initialize console
console = Console()

# Function to ping and return status
def ping_and_return_status(target):
    try:
        delay = ping(target)
        if delay is None:
            return 'red', 'No response'
        else:
            return 'green', f'Responded in {delay} seconds'
    except Exception as e:
        return 'red', str(e)

# Function to create and display table
def display_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Target", style="dim", width=14)
    table.add_column("Status", justify="right")
    table.add_column("Response", justify="right")

    for target in targets:
        color, response = ping_and_return_status(target)
        table.add_row(target, f'[bold {color}]●[/bold {color}]', response)

    console.clear()
    console.print(table)

# Continuously monitor
while True:
    display_table()
    time.sleep(10)
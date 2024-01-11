import sys
import time
import threading
from ping3 import ping
from rich.console import Console
from rich.table import Table

# List of targets
targets = ['nrk.no', 'vg.no']
targets.extend([f'login.p{i}.worldoftanks.eu' for i in range(1,4)])

# Initialize console
console = Console()

# Function to ping and return status
def ping_and_return_status(target, results):
    try:
        delay = ping(target)
        if delay is None:
            results[target] = ('red', 'No response')
        else:
            delay = delay * 1000
            delay = '{:.3f}'.format(delay)
            # delay = round(delay, 3)  # Round delay to 3 decimal places
            
            results[target] = ('green', f'{delay} ms')
    except Exception as e:
        results[target] = ('red', str(e))

# Function to create and display table
def display_table():
    # Dictionary to store the results
    results = {}
    # List to store the threads
    threads = []

    # Create and start a new thread for each target
    for target in targets:
        thread = threading.Thread(target=ping_and_return_status, args=(target, results))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Create the table
    USE_EMOJIS = False
    if USE_EMOJIS:
        target_str = "\U0001F5A5"
        up_str = "Status"
        response_str = "\U0001F553"
    else:
        target_str = "Target"
        up_str = "Up"
        response_str = "Response"

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(target_str, style="dim", width=24)
    table.add_column(up_str, justify="center", width=2)
    table.add_column(response_str, justify="right")

    # Add a row to the table for each target
    for target in targets:
        color, response = results[target]
        table.add_row(target, f'[bold {color}]●[/bold {color}]', response)

    # Clear the console and print the table
    console.clear()
    console.print(table)

# Continuously monitor
while True:
    display_table()
    time.sleep(1)
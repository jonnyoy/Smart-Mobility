#!/usr/bin/env python3

import click
import subprocess

@click.command()
@click.option('--fleet-size', type=int, required=True, help='Specify the fleet size for vehicle allocation and routing.')
def allocate_and_route(fleet_size):
    """Allocate and route vehicles."""
    click.echo(f'Allocating and routing vehicles for fleet size: {fleet_size}')

    # Call the ROS 2 Action Client CLI script
    try:
        subprocess.run(['ros2', 'run', 'your_package_name', 'fleet_management_client_cli.py', f'--fleet-size={fleet_size}'], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f'Error executing ROS 2 Action Client CLI: {e}')
        raise click.Abort()

if __name__ == '__main__':
    allocate_and_route()

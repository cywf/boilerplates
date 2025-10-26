#!/usr/bin/env python3
"""
CLI application entry point.
"""
import click
from rich.console import Console

console = Console()


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """My CLI Tool - A sample command-line application."""
    pass


@cli.command()
@click.option('--name', default='World', help='Name to greet')
def hello(name):
    """Say hello to someone."""
    console.print(f"[bold green]Hello, {name}![/bold green]")


@cli.command()
@click.option('--config', type=click.Path(exists=True), help='Configuration file')
def init(config):
    """Initialize the application."""
    console.print("[bold blue]Initializing application...[/bold blue]")
    if config:
        console.print(f"Using config file: {config}")
    else:
        console.print("Using default configuration")
    console.print("[bold green]✓[/bold green] Initialization complete!")


@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def run(verbose):
    """Run the main application task."""
    console.print("[bold blue]Running main task...[/bold blue]")
    if verbose:
        console.print("Verbose mode enabled")
    # Add your main logic here
    console.print("[bold green]✓[/bold green] Task completed!")


if __name__ == '__main__':
    cli()

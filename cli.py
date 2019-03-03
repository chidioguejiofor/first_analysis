
import click
from clean_raw_csv import export_clean_file


@click.group()
def cli():
    pass


@click.command()
def export():
    """Cleans up a CSV file and sends the output to an excel file

    This function cleans each question in the original CSV file
    and outputs the clean question dataset to sheets in an Excel file

    Returns:

    """
    export_clean_file()

@click.command()
def close():
    click.echo('Closing')


cli.add_command(export)
cli.add_command(close)

if __name__ == '__main__':
    cli()
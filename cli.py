
import click
from clean_raw_csv import export_clean_file, constants
from clean_raw_csv.dataframe_initializer import  DataframeInitializer

@click.group()
def cli():
    pass


@click.command()
@click.option('--output_filename', default=constants.TIDY_DATA_EXPORT_FILENAME)
def tidy_and_export(output_filename):
    """Cleans up a CSV file and sends the output to an excel file

    This function cleans each question in the original CSV file
    and outputs the clean question dataset to sheets in an Excel file

    Args:
        output_filename(str): The name of the excel file where the tidy data would
        be exported to.
    Returns:

    """
    DataframeInitializer.initialise_dataframes()
    export_clean_file(output_filename=output_filename)


@click.command()
def close():
    click.echo('Closing')


cli.add_command(tidy_and_export)
cli.add_command(close)

if __name__ == '__main__':
    cli()
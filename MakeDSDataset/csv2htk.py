import os
import csv
from decimal import Decimal
import click

def save_lab_file(filepath, ph_seq, ph_dur):
    start_time = Decimal('0.0000000')
    with open(filepath, 'w') as file:
        for phoneme, duration in zip(ph_seq, ph_dur):
            end_time = start_time + duration * Decimal('10000000')
            file.write(f"{int(start_time)} {int(end_time)} {phoneme}\n")
            start_time = end_time

def process_csv_file(filepath, output_directory):
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            name = row[0]
            ph_seq = row[1].split()
            ph_dur = list(map(Decimal, row[2].split()))
            
            output_path = os.path.join(output_directory, f"{name}.lab")
            save_lab_file(output_path, ph_seq, ph_dur)

@click.command()
@click.argument('csv_filepath', type=click.Path(exists=True, dir_okay=False))
@click.option('--output', type=click.Path(), default=None, help='Output HTK lab files path')
def main(csv_filepath, output):
    process_csv_file(csv_filepath, output)
    click.echo(f"Generated lab files in {output}.")

if __name__ == "__main__":
    main()

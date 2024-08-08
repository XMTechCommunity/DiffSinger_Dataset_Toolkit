import os
import csv
from decimal import Decimal, getcontext
import click

getcontext().prec = 10

def process_lab_file(filepath):
    ph_seq = []
    ph_dur = []
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            parts = lines[i].strip().split()
            start_time = Decimal(parts[0])
            end_time = Decimal(parts[1])
            phoneme = parts[2]
            
            duration = (end_time - start_time) * Decimal('0.0000001')
            
            ph_seq.append(phoneme)
            ph_dur.append(duration)
    
    return ph_seq, ph_dur

def process_lab_files_in_directory(directory):
    data = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".lab"):
            filepath = os.path.join(directory, filename)
            name = os.path.splitext(filename)[0]
            ph_seq, ph_dur = process_lab_file(filepath)
            data.append([name, ' '.join(ph_seq), ' '.join(map(str, ph_dur))])
    
    return data

def save_to_csv(data, output_filepath):
    with open(output_filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['name', 'ph_seq', 'ph_dur'])
        csvwriter.writerows(data)

@click.command()
@click.argument('lab_directory', type=click.Path(exists=True, file_okay=False))
@click.option('--output', type=click.Path(), default=None, help='Output CSV file path')
def main(lab_directory, output):
    if output is None:
        output = os.path.join(os.path.dirname(lab_directory), 'transcriptions.csv')
    
    data = process_lab_files_in_directory(lab_directory)
    save_to_csv(data, output)
    click.echo(f"Saved CSV file to {output}.")

if __name__ == "__main__":
    main()

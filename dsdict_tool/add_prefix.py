import click
import yaml
import os

@click.command()
@click.option('--input_file', '-i', default='output.yaml', help='Input file path')
@click.option('--output_file', '-o', default=None, help='Output file path, if not specified, will save to the input file directory with "update_" prefix')
@click.option('--prefix', '-p', default='zh', help='Which prefix to add')
@click.option('--additional_ignored_prefixes', '-aip', default='', help='Additional comma-separated list of prefixes to ignore (e.g., AP,Edge,SP) besides the fixed ones.')
def process_yaml(input_file, output_file, prefix, additional_ignored_prefixes):

    ignored_prefixes = {'AP', 'SP'}
    
    if additional_ignored_prefixes:
        additional_set = set(additional_ignored_prefixes.split(','))
        ignored_prefixes.update(additional_set)
    
    if output_file is None:
        directory, filename = os.path.split(input_file)
        output_file = os.path.join(directory, f'update_{filename}')
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        #'entries'
        for entry in data.get('entries', []):
            entry['phonemes'] = [
                f'{prefix}/{phoneme}' if phoneme not in ignored_prefixes else phoneme
                for phoneme in entry['phonemes']
            ]
        
        #'symbols'
        if 'symbols' in data:
            for symbol_entry in data['symbols']:
                symbol_entry['symbol'] = (
                    f'{prefix}/{symbol_entry["symbol"]}' 
                    if symbol_entry['symbol'] not in ignored_prefixes 
                    else symbol_entry['symbol']
                )

        with open(output_file, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)

        click.echo(f"File processed and saved to {output_file}")
    except Exception as e:
        click.echo(f"发生错误: {e}")

if __name__ == '__main__':
    process_yaml()

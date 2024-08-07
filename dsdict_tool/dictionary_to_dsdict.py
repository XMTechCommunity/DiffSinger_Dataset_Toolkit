import click
import yaml
import os

@click.command()
@click.option('--input_file', '-i', required=True, help='Input file path')
@click.option('--output_file', '-o', default=None, help='Output file path, if not specified, "dsdict.yaml" will be generated in the input file directory')
def convert_to_yaml(input_file, output_file):

    if output_file is None:
        directory, _ = os.path.split(input_file)
        output_file = os.path.join(directory, 'dsdict.yaml')

    entries = []

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                grapheme, phonemes_str = line.strip().split('\t')
                phonemes = phonemes_str.split()
                entries.append({'grapheme': grapheme, 'phonemes': phonemes})

        data = {'entries': entries}

        with open(output_file, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)

        click.echo(f"Data has been successfully converted and saved to {output_file}")
        click.echo(f"The 'symbols' column cannot be automatically generated. You need to create it manually or copy it from an existing dsdict.")

    except Exception as e:
        click.echo(f"发生错误: {e}", err=True)

if __name__ == '__main__':
    convert_to_yaml()

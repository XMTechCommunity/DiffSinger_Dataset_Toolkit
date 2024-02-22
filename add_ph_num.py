import click
import csv

@click.command()
@click.option('--csv_path',required = True, help='Path to CSV file')
@click.option('--dictionary',required = True, help='Path to dictionary file')
@click.option('--output',required = False,help='Path to output CSV file')
def add_ph_num(csv_path,dictionary,output):
    ph_seq_index = 1
    with open(csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        phonemes_tmp = []
        csv_reader = csv.reader(csvfile)
        
        for row in csv_reader:
            phonemes_tmp.append(row[ph_seq_index])
        # print(phonemes_tmp)
    
    dict = {}
    with open(dictionary, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            key = line.split('\t')[0]
            values = (line.split('\t')[1]).split(' ')
            dict.update({key: values})

    ph_num = []
    for phonemes in phonemes_tmp:
        tmp = []
        ph_tmp = []
        phonemes_split = phonemes.split(' ')
        # print(phonemes_split)
        for phoneme in phonemes_split:
            if phoneme == "AP" or phoneme == "SP":
                tmp.append(1)
            else:
                ph_tmp.append(phoneme)
                if ph_tmp in dict.values():
                    tmp.append(len(ph_tmp))
                    ph_tmp = []
        ph_num.append(tmp)
    print(ph_num)

if __name__ == '__main__':
    add_ph_num()

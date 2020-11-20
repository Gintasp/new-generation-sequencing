from typing import List, Dict

from Bio.SeqRecord import SeqRecord

from read_utils import FreqCalculator
import matplotlib.pyplot as plt


def extract_sequences(frequencies: Dict[int, List[SeqRecord]], freq: int, number: int) -> List[SeqRecord]:
    return frequencies[freq][:number]


def get_top_records(frequencies: Dict[int, List[SeqRecord]]) -> List[SeqRecord]:
    records = []

    # Extracting sequences with peak GC frequencies
    records += extract_sequences(frequencies, 31, 1)
    records += extract_sequences(frequencies, 33, 1)
    records += extract_sequences(frequencies, 35, 3)

    records += extract_sequences(frequencies, 50, 1)
    records += extract_sequences(frequencies, 52, 2)
    records += extract_sequences(frequencies, 54, 1)
    records += extract_sequences(frequencies, 56, 1)

    records += extract_sequences(frequencies, 66, 1)
    records += extract_sequences(frequencies, 68, 1)
    records += extract_sequences(frequencies, 70, 2)
    records += extract_sequences(frequencies, 72, 1)

    return records


def write_output_file(records: List[SeqRecord]) -> None:
    output = ''
    for top_record in records:
        output += f"{top_record.id}\n"
        output += f"{str(top_record.seq)}\n"
        output += "------------------------------\n\n"

    output_file = open('output.txt', 'w')
    output_file.write(output)


if __name__ == '__main__':
    print("Calculating GC frequencies...")
    calculator = FreqCalculator('data/reads.fastq')
    frequencies = calculator.get_frequencies()

    x_values = list(frequencies.keys())
    y_values = []
    for sequences in frequencies.values():
        y_values.append(len(sequences))

    print("Picking peak sequences...")
    top_records = get_top_records(frequencies)

    print("Writing output...")
    write_output_file(top_records)

    print("Generating chart...")
    plt.plot(x_values, y_values)
    plt.xlabel("Percentage of GC")
    plt.ylabel("Number of reads")
    plt.grid()
    plt.savefig("frequencies.png")

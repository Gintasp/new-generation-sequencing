from Bio.Blast import NCBIWWW, NCBIXML

from read_utils import FreqCalculator
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("Calculating GC frequencies...")
    calculator = FreqCalculator('data/reads.fastq')
    frequencies = calculator.get_frequencies()

    x_values = list(frequencies.keys())
    y_values = []
    for sequences in frequencies.values():
        y_values.append(len(sequences))

    print("Picking peak sequences...")
    top_records = []
    peak_keys = [35, 52, 54, 56]
    for key in peak_keys:
        top_records = top_records + frequencies[key][:5]

    for top_record in top_records:
        print(top_record.id)
        print(top_record.seq)
        print("--------------------------")

    print("Generating chart...")
    plt.plot(x_values, y_values)
    plt.xlabel("Percentage of GC")
    plt.ylabel("Number of reads")
    plt.grid()
    plt.savefig("frequencies.png")

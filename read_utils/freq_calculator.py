from typing import Dict, List
import math

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


class FreqCalculator:
    def __init__(self, filename: str):
        self._seq_records = SeqIO.parse(filename, 'fastq')

    def get_frequencies(self) -> Dict[int, List[SeqRecord]]:
        frequencies = dict.fromkeys(range(0, 101), [])

        for record in self._seq_records:
            char_counts = dict.fromkeys(record.seq, 0)
            for char in record.seq:
                char_counts[char] += 1

            if 'G' not in char_counts or 'C' not in char_counts or len(record.seq) == 0:
                continue

            frequency = math.floor((char_counts['C'] + char_counts['G']) / len(record.seq) * 100)
            frequencies[frequency] = frequencies[frequency] + [record]

        return frequencies

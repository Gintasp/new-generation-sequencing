from typing import Dict

from Bio import SeqIO


class QualityFormatDetector:
    def __init__(self, filename: str):
        self._seq_records = SeqIO.parse(filename, 'fastq')

    def detect(self, max_checks: int = None) -> str:
        chars = self.__get_char_count_dict(max_checks)

        for char in '!"#$%&\'()*+,-./0123456789:':
            if chars[char] > 0:
                if chars['J'] == 0:
                    return 'Sanger Phred+33'
                else:
                    return 'Illumina 1.8+ Phred+33'

        for char in ';<=>?':
            if chars[char] > 0:
                return 'Solexa Solexa+64'

        for char in '@AB':
            if chars[char] > 0:
                return 'Illumina 1.3+ Phred+64'

        if chars['i'] > 0:
            return 'Illumina 1.5+ Phred+64'

        return 'Undefined'

    @staticmethod
    def __get_alphabet():
        return "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    def __get_char_count_dict(self, max_checks: int = None) -> Dict[str, int]:
        chars = dict.fromkeys(self.__get_alphabet(), 0)
        records = list(self._seq_records)[:max_checks] if max_checks is not None else self._seq_records

        for record in records:
            for char_num in record.letter_annotations['phred_quality']:
                key = chr(char_num + 33)
                if key in chars:
                    chars[key] += 1

        return chars

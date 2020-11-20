New Generation Sequencing data Analysis
---

##### Instructions

1. Clone repository and `cd` into it.
2. Create virtual environment `python3 -m venv venv`
3. Log into created virtual environment using `source ./venv/bin/activate`
4. Install dependencies with `pip3 install -r requirements.txt`
5. Run `python3 ./main.py`.
6. Use `deactivate` CLI command to exit virtual environment.

##### Questions and Answers

Describe FASTQ format. Which additional information is available compared to FASTA?
> FASTQ contains quality score encoding for each nucleotide denoting how accurate read information is. FASTQ record has the following format:
> - Line starting with `@` which contains the sequence ID
> - One or more lines that contain the sequence
> - Newline starting with `+`
> - One or more lines that contain the quality scores

Which day of month were you born? Add 33 to day number, which ASCII symbol is it?
> 14 + 33 = 47 which is `/`

Why first 32 ASCII codes cannot be used as a quality score encoding?
> Because they are not representable as text (various SHIFT, ESC, SPACE, BACKSPACE etc. keys).

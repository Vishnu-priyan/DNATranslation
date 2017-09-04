from table import table
inputfile = "dna.txt"
f = open(inputfile,"r")
seq = f.read()
seq = seq.replace("\n","")
seq = seq.replace("\r","")
def translate(seq):
    """Translate string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids . Nucleotides are translated in triplets using the table dictionary; each amino acid 4 is encoded with a string of length 1. """
    
    protein=""
    if len(seq)% 3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein+=table[codon]
    return protein

print(translate(seq))

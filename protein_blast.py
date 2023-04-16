import ssl  # monkey patch for BioPython 1.68 & 1.69
ssl._create_default_https_context = ssl._create_unverified_context
from Bio.Blast import NCBIWWW
from Bio import SeqIO, SearchIO

if __name__ == "__main__":
    prot_record = SeqIO.read("prot_seq.fasta", format="fasta")
    print("Length of the Sequence: ", len(prot_record))
    print("Description of the record:\n")
    print(prot_record.description)
    print("Sequence: \n")
    print(prot_record.seq)

    #Blast analysis
    result_handle = NCBIWWW.qblast("blastp", "pdb", prot_record.seq)
    blast_result = SearchIO.read(result_handle, "blast-xml")
    print("First 2 Blast Result: \n", blast_result[0:2])

    Seq = blast_result[0]
    print(f"Sequence ID: {Seq.id}")
    print(f"Sequence Description: {Seq.description}")

    details = Seq[0]
    print(f"E-value: {details.evalue}")
    Seq = blast_result[0]
    print(f"Sequence ID: {Seq.id}")
    print(f"Sequence Description: {Seq.description}")

    details = Seq[0]
    print(f"E-value: {details.evalue}")
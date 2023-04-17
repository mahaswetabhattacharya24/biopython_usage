import ssl  # monkey patch for BioPython 1.68 & 1.69
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import ExPASy
from Bio.ExPASy import Prosite
from Bio.ExPASy import ScanProsite
from Bio import SeqIO

# Accessing databases of protein families and domains using PROSITE

if __name__=="__main__":
    #Access the raw data from prosite with the given ID
    handle = ExPASy.get_prosite_raw('PS51442')
    record = Prosite.read(handle)

    #print the description of the accessed record
    print("Description\n")
    print(record.description)

    # Find the PDB structures which match with the PROSITE pattern
    print(record.pdb_structs[:10])

    #Access the raw prosite record with a given accession number
    handle = ExPASy.get_prosite_raw('PS00001')
    record = Prosite.read(handle)
    print("PROSITE Record...\n")
    print(record.pattern)

    # Read a protein sequence from a file and find its length
    prot_record = SeqIO.read("prot_seq.fasta", format="fasta")
    print("Length of protein sequence: ", len(prot_record.seq))

    #Scan PROSITE for the protein motif
    handle = ScanProsite.scan(seq=prot_record.seq, mirror="https://prosite.expasy.org/")
    result = ScanProsite.read(handle)

    #Find matches
    if result.n_match == 0:
        print("No match found!")
    elif result.n_match == 1:
        print("%s match found" %result.n_match)
    else:
        print("%s matches found" % result.n_match)

    # Print the matched result
    print("Matched result\n")
    print(result[0])

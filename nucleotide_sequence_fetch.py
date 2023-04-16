import ssl  # monkey patch for BioPython 1.68 & 1.69
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez

if __name__ == "__main__":
    Entrez.email = "b.mahasweta24@gmail.com"
    handle = Entrez.einfo()

    #Types of databases available for access
    record = Entrez.read(handle)
    print("Databases:\n", record["DbList"])

    # Nucleotide records of SARS
    handle = Entrez.esearch(db="nucleotide", retmax=10, term="Severe acute respiratory syndrome")
    record = Entrez.read(handle)
    print("The record IDs for SARS are:\n")
    print(record["IdList"])
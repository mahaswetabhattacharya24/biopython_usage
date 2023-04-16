import ssl  # monkey patch for BioPython 1.68 & 1.69
ssl._create_default_https_context = ssl._create_unverified_context
from Bio import Entrez

if __name__ == "__main__":
    Entrez.email = "b.mahasweta24@gmail.com"
    handle = Entrez.einfo()

    #Types of databases available for access
    record = Entrez.read(handle)
    print("Databases:\n", record["DbList"])

    #Fetch pubmed database info
    handle = Entrez.einfo(db="pubmed")
    record = Entrez.read(handle)
    print("Q: What type of record is Pubmed?\n")
    print("A: ", record["DbInfo"]["Description"])

    # Number of records in pubmed database
    print("Q: How many records or literatures are there in the Pubmed database?\n")
    print("A: ", record["DbInfo"]["Count"])

    #Search literature with a specific term in title
    handle = Entrez.esearch(db="pubmed", term="biopython")
    record = Entrez.read(handle)
    print("Q: What are the ID of records or literatures are there in the Pubmed database based on biopython?\n")
    print(record["IdList"])

    #Print details of first 2 journals
    handle = Entrez.esummary(db="pubmed", id='36818783, 36245797')
    records = Entrez.parse(handle)
    print("The details of first 2 journals are:\n")
    for record in records:
        print(record['AuthorList'], record['Title'], record['PubDate'], record['FullJournalName'])

    #Visualize summary of a particular journal
    handle = Entrez.efetch(db="pubmed", id="19811691")
    print(handle.read())
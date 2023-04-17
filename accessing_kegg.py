import ssl  # monkey patch for BioPython 1.68 & 1.69
ssl._create_default_https_context = ssl._create_unverified_context
from Bio.KEGG import REST, Enzyme

#This script shows usage for accessing KEGG database for enzymes and pathways

if __name__ == "__main__":

    #Retrive details of the Kegg entry with a given enzyme commision number
    request = REST.kegg_get("ec:5.4.2.2")
    open("ec_5.4.2.2.txt", "w").write(request.read())

    #Open the downloaded enzyme file
    records = Enzyme.parse(open("ec_5.4.2.2.txt"))
    record = list(records)[0]
    print("Details of the KEGG file\n")
    print(record.classname)

    #Print the associated pathways
    print("The associated pathways are:\n")
    print(record.pathway)

    #Retrieve the gene attributes of the enzyme
    print("The first 10 gene attributes are:\n")
    print(record.genes[:10])

    #Print only the gene names
    print("The gene names are:\n")
    list_genes = []
    for x, y in record.genes:
        list_genes += x.split("\n")
    print(list_genes[:10])

from Bio.KEGG import REST, Enzyme

#This script shows usage for accessing KEGG database for enzymes and pathways

if __name__ == "__main__":

    #Retrive details of the Kegg entry with a given enzyme commision number
    request = REST.kegg_get("ec:5.4.2.2")
    open("ec_5.4.2.2.txt", "w").write(request.read())
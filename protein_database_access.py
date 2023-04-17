import warnings
warnings.filterwarnings("ignore")
from Bio.PDB import PDBParser,PDBList

if __name__ == "__main__":
    #Create a Protein Databse instance and download the file
    #with the ID 7BYR
    pdbl = PDBList()
    pdbl.retrieve_pdb_file("7BYR", file_format="pdb", pdir="dir")

    # Read the pdb file
    parser = PDBParser()
    structure = parser.get_structure("7BYR", "dir/pdb7byr.ent")

    #Retrive the chains and corresponding IDs
    for chain in structure[0]:
        print(f"Chain ID: {chain.id}")

    #Find resolution
    resolution = structure.header["resolution"]
    print("Resolution is %s Angstrom" %resolution)

    #Access the keyword related to the protein
    keywords = structure.header["keywords"]
    print("Protein associated keywords are:\n")
    print(keywords)



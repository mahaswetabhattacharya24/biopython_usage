# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    reversed = Reverse(Pattern)
    complemented = Complement(reversed)
    return complemented

def Reverse(Pattern):
    chars = list(Pattern)
    # Reverse the order of the characters in the list
    chars.reverse()
    # Convert the list of reversed characters back to a string
    reversed_pattern = ''.join(chars)
    return reversed_pattern

# Copy your Complement() function here.
def Complement(Pattern):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # Convert the input DNA string to a list of nucleotides
    nucleotides = list(Pattern)
    # Use a list comprehension to replace each nucleotide with its complement
    complemented = [complements[nuc] for nuc in nucleotides]
    # Convert the list of complemented nucleotides back to a string
    complemented_dna = ''.join(complemented)
    return complemented_dna

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

if __name__ == "__main__":
    sequence = input("Enter the nucleotide sequence: ")
    print("Reversed sequence:\n", Reverse(sequence))
    print("Complementary sequence:\n", Complement(sequence))
    print("Reversed complemented sequence:\n", ReverseComplement(sequence))

    pattern = input("Enter the pattern to look for: ")
    print("Positions of appearance of the pattern:\n ", PatternMatching(pattern, sequence))
    print("Done...")


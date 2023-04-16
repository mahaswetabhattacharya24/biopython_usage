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

def PatternCount(Text, Pattern):
    positions = [] # output variable
    c=0
    for i in range(len(Pattern) - len(Text) + 1):
        if Pattern[i:i+len(Text)] == Text:
            c+=1
    return (c)

def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
    return skew

def MinimumSkew(Genome):
    array = SkewArray(Genome)
    positions = []
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count +=1
    return positions


if __name__ == "__main__":
    sequence = input("Enter the nucleotide sequence: ")
    print("Reversed sequence:\n", Reverse(sequence))
    print("Complementary sequence:\n", Complement(sequence))
    print("Reversed complemented sequence:\n", ReverseComplement(sequence))

    pattern = input("Enter the pattern to look for: ")
    print("Positions of appearance of the pattern:\n ", PatternMatching(pattern, sequence))
    print("Done...")


def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)

    for key, v in profile.items():
        v[:] = [x / t for x in v]
    return profile

def Score(Motifs):
    consensus = Consensus(Motifs)
    count = 0
    for motif in Motifs:
        for index in range(len(motif)):
            if motif[index] != consensus[index]:
                count += 1
    return count

def pr(Motif):
    total = 1
    k = len(Motif)
    for i in range(k-1):
        for nucleotide in profile:
            if Motif[i] == nucleotide:
                total *= profile[nucleotide][i]
    return total
def Pr(Text, Profile):
    outcome = 1
    for i in range(len(Text)):
        outcome *= Profile[Text[i]][i]
    return outcome


def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    pr = {}
    most_prob_kmer = []
    for i in range(n-k+1):
        k_mer = text[i:i+k]
        probability = Pr(k_mer, profile)
        pr[k_mer] = probability
    m = max(pr.values())
    for key, value in pr.items():
        if pr[key] == m:
            most_prob_kmer.append(key)
    return most_prob_kmer[0]
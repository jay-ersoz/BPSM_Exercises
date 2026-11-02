#!/usr/bin/python3
#question 1
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_seq)
#count the number of A nucleotides
dna_seq.count("A")
#count the number of T nucleotides
dna_seq.count("T")
#add the numbers of A and T in the sequence and save it as a variable
AT_count = dna_seq.count("A") + dna_seq.count("T")
print(AT_count)
#37
#divide AT_count by the length of the sequence
AT_fraction = AT_count / len(dna_seq)
print(AT_fraction)
#0.6851851851851852

#question 2
dna_seq2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna_seq2)
#Write a program that will print the complement of this sequence
for nucleotide in dna_seq2:
    if nucleotide == "A":
        print("T", end="")
    elif nucleotide == "T":
        print("A", end="")
    elif nucleotide == "G":
        print("C", end="")
    elif nucleotide == "C":
        print("G", end="")

#question 3
dna_seq3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
'''
The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the
cut is indicated by an asterisk). Write a program which will calculate the size of the two fragments that will be produced when 
the DNA sequence is digested with EcoRI.
'''
#find the position of the motif in the sequence
dna_seq3.find("GAATTC")
#21

#use that to figure out the position of the cut
#22

#calculate the length of the second fragment based on the cut position
frag1 = dna_seq3[0:22]
len(frag1)
#22
frag2 = dna_seq3[22:]
len(frag2)
#33

#question 4
#Here's a short section (123 bases) of genomic DNA:
dna_seq4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

'''
It comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third real character, 
and the second exon runs from the ninety-first real character to the end of the sequence. Write a program that will print just the coding 
regions of the DNA sequence.
'''
#cut out both exons from sequence
exon1 = dna_seq4[0:63]
exon2 = dna_seq4[90:]
#concatenate the two exons
exons = exon1 + exon2
#Write a program that will calculate what percentage of the DNA sequence is coding.
#figure out the length of the coding sequence:
len(exons)
#divide by the length of the original sequence and multiply by 100:
(len(exons)/len(dna_seq4))*100
#78.04878048780488

#Write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.
#store the exons and intron separately as variables
#I already have the exons stored as variables exon1 and exon 2
intron = dna_seq4[63:90]
#convert the intron to lower case
lowercase_intron = intron.lower()
#concatenate the exons and intron to make one long sequence
print(exon1 + lowercase_intron + exon2)
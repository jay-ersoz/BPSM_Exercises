#!/usr/bin/python3
import os, sys
'Exercise 1: Processing tabular data'
#Copy the text file called data.csv from the directory /localdisk/data/BPSM/Lecture14/ to your area.
os.system("cp /localdisk/data/BPSM/Lecture14/data.csv .")
#The file contains some made-up data for a number of genes.
#Each line contains the following fields for a single gene in this order: species name, sequence, gene name, expression level.
#The fields are separated by commas (hence the "csv" suffix on the filename: csv stands for Comma Separated Values)

#You need to write a Python programme/script that can:
#Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.

#make a list where each index is one line:
genes_file = open("data.csv").read().split("\n")
#check the list we just generated:
print(genes_file)

for index in genes_file:
    if index.startswith("Drosophila melanogaster") or index.startswith("Drosophila simulans"):
        print(index.split(",")[2])
#kdy647
#jdg766
#kdy533

#Print out the gene names for all genes that are between 90 and 110 bases long.
for index in genes_file:
    index_list = index.split(",")
    if (len(index_list[1]) > 90) and (len(index_list[1]) < 110):
        print(index_list[2])
#kdy647
#teg436

#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
for index in genes_file:
    index_list = index.split(",")
    #print(index_list[1])
    #print((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1]))
    if ((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1])) < 0.5 and (int(index_list[3]) > 200):
        print(index_list[2])
#teg436

#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
for index in genes_file:
    index_list = index.split(",")
    if index_list[0] != "Drosophila melanogaster":
        if index_list[2].startswith("k") or index_list[2].startswith("h"):
            print(index_list[2])
#kdy533
#hdt739
#hdu045

#For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).
for index in genes_file:
    index_list = index.split(",")
    #print(index_list[1])
    #print((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1]))
    if ((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1])) > 0.65:
        print(index_list[2] + " has high AT content.")
    elif ((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1])) < 0.45:
        print(index_list[2] + " has low AT content.")
    elif ((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1])) > 0.45 and ((index_list[1].upper().count("A")+index_list[1].upper().count("T"))/len(index_list[1])) < 0.65:
        print(index_list[2] + " has medium AT content.")
#kdy647 has high AT content.
#jdg766 has medium AT content.
#kdy533 has medium AT content.
#hdt739 has low AT content.
#hdu045 has medium AT content.
#teg436 has medium AT content.

'Exercise 2: K-mer counting'
#K-mers are short DNA subsequences with length "k" bases, and are usually generated using the "sliding window" method we used in the last lecture's exercise.
#Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n (you chose what the number n is!).

#ask user input for the values of 'k', 'n', and the DNA sequence, and assign them to variables to be used in the code
k = int(input("Enter the desired k-mer length.\n"))
n = int(input("Enter 'n' (the code will print all the k-mers that occur more than 'n').\n"))
dna = input("Enter the DNA sequence you wish to analyse (case insensitive).\n").upper()

#write the for loop for the sliding window with the given DNA sequence and k-mer length
i=0
for base in dna:
    if i<(len(dna)-(k-1)):
        print((i*" ") + dna[i:i+k])
        i+=1

#write the loop that will only print out the k-mers that occur more than n times
i=0
kmer_list = []
for base in dna:
    if i<(len(dna)-(k-1)):
        kmer_list.append(dna[i:i+k])
        if kmer_list.count(kmer_list[i]) > n:
            print(kmer_list[i])
        i+=1

#test loop
#test_list = [0, 1, 1, 1, 2]
#i=0
#for num in test_list:
#    if test_list.count(test_list[i])>2:
#        print(test_list[i])
#    i+=1

'Exercise 3: Pairwise distances: how similar are two sequences?'
#Here is a list of DNA sequences that are all equal in length, with varying degrees of similarity to each other:
#['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
#Write a programme/script that calculates and prints, for each pair of sequences, the percentage of identical positions (e.g. base #4 in seq 1 is the same as base #4 in seq 4, and so on).
#Hint:
#if base_in_seq1 == base_in_seq2:
#   do something

#assign the sequences to a list variable
sequences = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

#assign each sequence its own variable
seq1 = sequences[0]
seq2 = sequences[1]
seq3 = sequences[2]
seq4 = sequences[3]

#set the index and count variables to zero
i=0
count1=0 #number of identical bases at the same positions for sequences 1 and 2
count2=0 #number of identical bases at the same positions for sequences 1 and 3
count3=0 #number of identical bases at the same positions for sequences 1 and 4
count4=0 #number of identical bases at the same positions for sequences 2 and 3
count5=0 #number of identical bases at the same positions for sequences 2 and 4
count6=0 #number of identical bases at the same positions for sequences 3 and 4

#write a loop for counting 
for base in seq1:
    if seq1[i] == seq2[i]:
        count1+=1
    if seq1[i] == seq3[i]:
        count2+=1
    if seq1[i] == seq4[i]:
        count3+=1
    if seq2[i] == seq3[i]:
        count4+=1
    if seq2[i] == seq4[i]:
        count5+=1
    if seq3[i] == seq4[i]:
        count6+=1
    i+=1

print("Percentage of identical positions between the first and the second sequence is " + str((count1/len(seq1))*100))
print("Percentage of identical positions between the first and the third sequence is " + str((count2/len(seq1))*100))
print("Percentage of identical positions between the first and the fourth sequence is " + str((count3/len(seq1))*100))
print("Percentage of identical positions between the second and the third sequence is " + str((count4/len(seq2))*100))
print("Percentage of identical positions between the second and the fourth sequence is " + str((count5/len(seq2))*100))
print("Percentage of identical positions between the third and the fourth sequence is " + str((count6/len(seq3))*100))

#first try that didn't work:
'''
for seq in sequences:
    if sequences.index(seq) == 0:
        seq2 = sequences[sequences.index(seq) + 1]
        seq3 = sequences[sequences.index(seq) + 2]
        seq4 = sequences[sequences.index(seq) + 3]
        if seq[i] == seq2[i]:
            count1 += 1
        if seq[i] == seq3[i]:
            count2 += 1
        if seq[i] == seq4[i]:
            count3 += 1  
    elif sequences.index(seq) == 1:
        seq3 = sequences[sequences.index(seq) + 1]
        seq4 = sequences[sequences.index(seq) + 2]
        if seq[i] == seq3[i]:
           count4 += 1
        if seq[i] == seq4[i]:
           count5 += 1
    elif sequences.index(seq) == 2:
        seq4 = sequences[sequences.index(seq) + 1]
        if seq[i] == seq4[i]:
            count6 += 1
    i+=1    

print("Percentage of identical positions between the first and the second sequence is " + str((count1/len(seq))*100))
print("Percentage of identical positions between the first and the third sequence is " + str((count2/len(seq))*100))
print("Percentage of identical positions between the first and the fourth sequence is " + str((count3/len(seq))*100))
print("Percentage of identical positions between the second and the third sequence is " + str((count4/len(seq))*100))
print("Percentage of identical positions between the second and the fourth sequence is " + str((count5/len(seq))*100))
print("Percentage of identical positions between the third and the fourth sequence is " + str((count6/len(seq))*100))

#expected answers:
#first & second: 66.7
#first & third: 55.6
#first & fourth: 33.3
#second & third: 88.9
#second & fourth: 44.4
#third & fourth: 44.4

'''
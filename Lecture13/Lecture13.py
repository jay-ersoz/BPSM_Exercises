#!/usr/bin/python3

#Where are your edirect programmes stored?
#which esearch
#/home/s3030309/edirect/esearch

#What things are in your edirect directory/folder on the bioinformatics server?
#ls /home/s3030309/edirect | wc -l
#139 things

#How many files in your edirect directory/folder start with the letter e or x?
#find /home/s3030309/edirect -name "e*" | wc -l
#25
#find /home/s3030309/edirect -name "x*" | wc -l
#23
#you can do both at the same time by:
#ls | egrep '^e|^x' | wc -l

#What edirect directory/folder directory items start with the letter e or x, and what do the programmes do?
#find /home/s3030309/edirect -name "e*"
#find /home/s3030309/edirect -name "x*"

'Exercise 1 : Processing DNA in a file'
#The file input.txt contains a number of DNA sequences, one per line.
#Each sequence starts with the same 14 base pairs: these are from a sequencing adapter that should have been removed.

#check what input.txt looks like
input_file = open('input.txt').read()
print(input_file)

#ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
#CGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
#ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
#ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
#ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
#ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA

#we need to remove the first 14 bases (ATTCGATTATAAGC)

#the new file needs to look like:
#TCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
#ACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
#ATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
#ACTATCGATGATCTAGCTACGATCGTAGCTGTA
#ACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA

#the lengths of each new line are:
#42
#37
#48
#33
#47

#Write a Python script/programme that will:
#(a) trim the adapter and write the 'cleaned' (adapter-free) sequences to a single new file

#make a new file for the edited input.txt sequences
input_edited = open('input_edited.txt', 'x')
input_file = open('input.txt')
#write a for loop that removes the first 14 characters of each line and appends this new line into a new file called input_edited.txt
for eachline in input_file:
    with open('input_edited.txt', 'a') as input_edited:
        line = eachline[14:].rstrip('\n')
        input_edited.write(line + "\n")
        #print(input_edited)

#check to see what your input_edited.txt file looks like
input_edited = open("input_edited.txt").read()
print(input_edited)
#everything looks good

#(b) print the length of each adapter-free sequence to the screen.
with open("input_edited.txt") as input_edited:
    for sequence in input_edited:
        len(sequence)

'Exercise 2 : Multiple exons from genomic DNA'
#The file genomic_dna2.txt contains a section of genomic DNA.

#check what the sequence looks like
genomic_dna2 = open("genomic_dna2.txt").read()
print(genomic_dna2)
#it looks like the sequence is all on one line

#The file exons.txt contains a list of start/stop positions of exons.
#Each exon is on a separate line and the start and stop positions are separated by a comma.

#check what the file looks like
exons = open("exons.txt").read()
print(exons)
#5,58
#72,133
#190,276
#340,398

#Write a Python script/programme that will extract the exon segments, concatenate them, and write them to a new file.

#make a list with all the positions separated by commas
with open("exons.txt") as exons:
    exons = exons.read()
    exons = exons.replace("\n", ",")
    exons_list = exons.split(",")

print(exons_list)
#['5', '58', '72', '133', '190', '276', '340', '398', '']

#remove the last index of exons_list
exons_list = exons_list[:-1]
print(exons_list)
#['5', '58', '72', '133', '190', '276', '340', '398']

#make a new file for the concatenated exons to go to
genomic_dna2_exons = open("genomic_dna2_exons.txt", "x")
i = 0
with open("genomic_dna2_exons.txt", "a") as genomic_dna2_exons:
    for location in exons_list:
        genomic_dna2_exons.write(genomic_dna2[int(exons_list[i])-1:int(exons_list[i+1])])
        i += 2

#check the file
genomic_dna2_exons = open("genomic_dna2_exons.txt").read()
print(genomic_dna2_exons)

'Exercise 3 : Sliding windows'
#You need to write a Python script/programme that will generate overlapping short segments from a long string (i.e. a sliding window approach); e.g. if your input sequence was:
#abcdefghijk
#and the window size chosen was 6, and the offset was 1, then the segments would be:
#abcdef
#bcdefg
#cdefgh
#defghi
#efghij
#fghijk

#Using the protein-coding region from the AJ223353 NCBI sequence ('remote_exon01.fasta', or whatever you called it) that you generated while doing the exercises in the last
#lecture, write a Python programme that generates segments that are 30 bases long, with a window offset of 3.

#name of my file: remote_sequence_exon1.txt 
#copy this file from Lecture12 directory to Lecture13 directory, so I can keep working from the same place

#NOTE: I accidentally forgot to set the window offset to 3 instead of 1, so all of these answers are technically wrong
#Modify your Python script/programme to print each sliding window segment to the screen.
i=0
with open("remote_sequence_exon1.txt") as remote_sequence:
    remote_sequence = remote_sequence.read()
    for base in remote_sequence:
        if i<(len(remote_sequence)-29):
            print(remote_sequence[i:i+30])
            i+=1

#Modify your Python script/programme to print the percentage GC content of each sliding window segment and the sequence.
i=0
with open("remote_sequence_exon1.txt") as remote_sequence:
    remote_sequence = remote_sequence.read()
    ((remote_sequence.count("G") + remote_sequence.count("C"))/len(remote_sequence))*100
    for base in remote_sequence:
        if i<(len(remote_sequence)-29):
            print(remote_sequence[i:i+30] + "\t" + str(((remote_sequence[i:i+30].count("G")+remote_sequence[i:i+30].count("C"))/30)*100))
            i+=1

#Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.
i=0
with open("../remote_sequence_exon1.txt") as remote_sequence:
    remote_sequence = remote_sequence.read()
    for base in remote_sequence:
        if i<(len(remote_sequence)-29):
            filename = "sliding_window_" + str(i) + ".fasta"
            file = open(filename, "x")
            with open(filename, "a") as file:
                file.write(">AJ223353:29-409bp CDS sliding_window_" + str(i) + "\n" + remote_sequence[i:i+30])
                i+=1

#check the first file to see if it worked
file = open("sliding_window_0.fasta").read()
print(file)

#Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into a single fasta file.
i=0
file = open("sliding_windows.fasta", "x")
with open("sliding_windows.fasta", "w") as file:
    file.write(">AJ223353:29-409bp CDS" + "\n")

with open("remote_sequence_exon1.txt") as remote_sequence:
    remote_sequence = remote_sequence.read()
    for base in remote_sequence:
        if i<(len(remote_sequence)-29):
            with open("sliding_windows.fasta", "a") as file:
                file.write(remote_sequence[i:i+30] + "\n")
                i+=1

file = open("sliding_windows.fasta").read()
print(file)

#Modify your Python script/programme to include the partial sliding window segments that we get at the end of the sequence.
i=0
with open("remote_sequence_exon1.txt") as remote_sequence:
    remote_sequence = remote_sequence.read()
    for base in remote_sequence:
        print(remote_sequence[i:i+30])
        i+=1

#Note that all of the above 'modifications' could/should be part of a single Python script/programme! For example, you might find it easier to add processing step (a), ensure it is working properly, then try adding (b), and so on.

'Exercise 4 : Size-binning DNA sequences'
#In the directory /localdisk/data/BPSM/Lecture13/ is a collection of files whose names end in .dna.
#Each file holds a collection of DNA sequences, one per line.

#Write a Python script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..
import os
import sys

os.system("mkdir 100-199")
os.system("mkdir 200-299")
os.system("mkdir 300-399")
os.system("mkdir 400-499")
os.system("mkdir 500-599")
os.system("mkdir 600-699")
os.system("mkdir 700-799")
os.system("mkdir 800-899")
os.system("mkdir 900-999")

# Choose any one of the .dna files as an input file, and write out each DNA sequence in that input file to a separate file in the appropriate 'size range' directory.
i=0
with open("xaa.dna") as xaa:
    for line in xaa:
        length = len(line)
        length_cat = int(round(length, -2))
        dir_name = str(length_cat) + "-" + str(length_cat + 99)
        filename = str(i) + ".txt"
        file = open(dir_name + "/" + filename, "x")
        with open(dir_name + "/" + filename, "w") as filename:
            filename.write(line)
        i+=1
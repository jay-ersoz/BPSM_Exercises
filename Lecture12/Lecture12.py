#!/usr/bin/python3
#"Mission One": Make some fasta sequences

'''
"local" DNA sequence: take a copy of the file called plain_genomic_seq.txt, which is in the /localdisk/data/BPSM/Lecture12/ directory. 
The first exon runs from the start of the sequence up to and including the sixty-third BASE, and the second exon runs from the ninety-first 
BASE to the end of the sequence.
'''
#total length of local text file = 136 characters (however, many of these characters are NOT "A", "T", "C" or "G", and not all of them are upper case)
#total length of local sequence (after removal of non-bases) = 127
#exon 1 = bases 1 to 63
#exon 2 = bases 91 to [end]
#the rest of the sequence is non-coding

'''
"remote" DNA sequence: get the DNA sequence for accession AJ223353 from NCBI in plain fasta format, and remove the whole of the fasta header line.
'''
#total length of remote sequence = 808 bp
#CDS (coding) = bases 29 to 409
#regulatory (non-coding) = bases 769 to 774
#the rest of the sequence is also non-coding

#get the remote sequence as a FASTA file
wget -O AJ223353.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=AJ223353.1&strand=1&seq_start=1&seq_stop=808&rettype=fasta&retmode=text"

'''
For both of the above sequences:
'''
#1. Write a Python programme/script that will split the genomic DNA into coding and non-coding parts, and write each of these sub-sequences to 
#individual files AND two separate files (so that we also have one for coding sequences, and one for non-coding sequences)

#assign the string from the local sequence to a variable
local_sequence = open("plain_genomic_seq.txt").read()
#check again to see what the sequence looks like
print(local_sequence)

#assign the string from the remote sequence to a variable
remote_sequence = open("AJ223353.fasta").read()
#check to see what the sequence looks like
print(remote_sequence)

#2. Your programme/script should make sure that all sequences are in upper case and are DNA

#in the local sequence, there are many characters that are not nucleotides and not all characters are in upper case
#make sure all the characters in the local sequence are upper case
local_sequence = local_sequence.upper()
#make sure to remove all the non-nucleotide characters
local_sequence = local_sequence.replace("X", "")
local_sequence = local_sequence.replace("S", "")
local_sequence = local_sequence.replace("K", "")
local_sequence = local_sequence.replace("L", "")
#check the new length of the local sequence string
len(local_sequence)
#127

#the remote sequence is in FASTA format and has a header line that needs to be removed
remote_sequence = remote_sequence.replace(">AJ223353.1:1-808 Homo sapiens mRNA for histone H2B, clone pJG4-5-15", "")
#there are also new line characters "\n" that need to be removed from this sequence
remote_sequence = remote_sequence.replace("\n", "")
#check the length of the sequence to make sure it matches its length specified on NCBI (808)
len(remote_sequence)
#808
#perfect, we now have just the nucleotides from both the sequences!
#note that we've only edited variables so far and not the actual files

#now let's separate the sequences into coding and non-coding regions and assign them separate variables
#remember that python indeces start at 0
#within the square brackets, the first number is included, the second number is excluded
local_exon1 = local_sequence[1:63]
local_exon2 = local_sequence[90:]
#we can concatenate the exons together to get all the coding regions together
local_exons = local_exon1 + local_exon2
#there is 1 non-coding region in the local sequence
local_intron = local_sequence[63:90]

remote_exon1 = remote_sequence[28:409]
remote_exon2 = remote_sequence[768:774]
#we can concatenate the exons together to get all the coding regions together
remote_exons = remote_exon1 + remote_exon2
#there are 3 separate non-coding regions in the remote sequence
remote_intron1 = remote_sequence[:28]
remote_intron2 = remote_sequence[409:768]
remote_intron3 = remote_sequence[774:]
#we can concatenate the introns together to get all the non-coding regions together
remote_introns = remote_intron1 + remote_intron2 + remote_intron3


#we need to create a new file for each of the fragments of the local and remote sequences with appropriate names
#the "x" within the open function creates a new file with the specified name; returns an error if the file already exists
/BPSM_Exercises
#making a plain text file for the edited local sequence
local_sequence_edited = open("local_sequence_edited.txt", "x")
with open("local_sequence_edited.txt", "w") as LSE_file:
    LSE_file.write(local_sequence)

#making plain text files for all the local sequence fragments
local_sequence_exon1 = open("local_sequence_exon1.txt", "x")
with open("local_sequence_exon1.txt", "w") as LE1_file:
    LE1_file.write(local_exon1)

local_sequence_exon2 = open("local_sequence_exon2.txt", "x")
with open("local_sequence_exon2.txt", "w") as LE2_file:
    LE2_file.write(local_exon2)

local_sequence_exons = open("local_sequence_exons.txt", "x")
with open("local_sequence_exons.txt", "w") as LE_file:
    LE_file.write(local_exons)

local_sequence_intron = open("local_sequence_intron.txt", "x")
with open("local_sequence_intron.txt", "w") as LI_file:
    LI_file.write(local_intron)

#making a plain text file for the edited remote sequence
remote_sequence_edited = open("remote_sequence_edited.txt", "x")
with open("remote_sequence_edited.txt", "w") as RSE_file:
    RSE_file.write(remote_sequence)

#making plain text files for all the remote sequence fragments
remote_sequence_exon1 = open("remote_sequence_exon1.txt", "x")
with open("remote_sequence_exon1.txt", "w") as RE1_file:
    RE1_file.write(remote_exon1)

remote_sequence_exon2 = open("remote_sequence_exon2.txt", "x")
with open("remote_sequence_exon2.txt", "w") as RE2_file:
    RE2_file.write(remote_exon2)

remote_sequence_exons = open("remote_sequence_exons.txt", "x")
with open("remote_sequence_exons.txt", "w") as RE_file:
    RE_file.write(remote_exons)

remote_sequence_intron1 = open("remote_sequence_intron1.txt", "x")
with open("remote_sequence_intron1.txt", "w") as RI1_file:
    RI1_file.write(remote_intron1)

remote_sequence_intron2 = open("remote_sequence_intron2.txt", "x")
with open("remote_sequence_intron2.txt", "w") as RI2_file:
    RI2_file.write(remote_intron2)

remote_sequence_intron3 = open("remote_sequence_intron3.txt", "x")
with open("remote_sequence_intron3.txt", "w") as RI3_file:
    RI3_file.write(remote_intron3)

remote_sequence_introns = open("remote_sequence_introns.txt", "x")
with open("remote_sequence_introns.txt", "w") as RI_file:
    RI_file.write(remote_introns)

#3. Your fasta headers should include the length of the sequence
#we know the length of both sequences: 127 bp for the local sequence and 808 bp for the remote sequence

#4. Your output fasta file names should, where possible, be the same as the fasta header, followed by the ".fasta" suffix, but not include any 
#spaces: this is Linux, remember!

#5. Your programme/script should include comments so that I/anyone can understand what you have done
#done!

#6. Your programmes/scripts should be committed in your personal git repository and pushed to GitHub
#done! under Lecture12 directory/folder


#"Mission Two": running BLAST with those sequences

#Using the files that you have generated in "Mission One", run a BLAST analysis against the nematode database (nem) we made previously in the BLAST 
#lecture. The commands should come from your Python session using the modules that we learnt about today.

#first, change the directory to BPSM/Exercises so that we can access both Lecture06 and Lecture12 directories
import os
os.chdir("/localdisk/home/s3030309/BPSM/Exercises")

import sys
os.system("blastx -db ./Lecture06/nem -query ./Lecture12/local_sequence_edited.txt > local_blast.out")
os.system("blastx -db ./Lecture06/nem -query ./Lecture12/remote_sequence_edited.txt > remote_blast.out")

#From the outputs that you get, what was the best hit for each of the sequences input?
os.system("open local_blast.out")
#no hits
os.system("open remote_blast.out")
#best hit score (bits): 179
#gi|341891943|gb|EGT47778.1| hypothetical protein CAEBREN_15210





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

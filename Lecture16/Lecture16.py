#!/usr/bin/python3

#Exercise #1: Interrogating the user...
'''
With the aid of a function and a dictionary, write an interactive Python programme/script that will ask the user the following questions:
    - What's your name?
    - How old are you?
    - What is your favourite colour?
    - Do you like Python?
    - The world is flat: True or False?
and then, based on their answers, make some comments back to them (this doesn't have to be at all serious, it's the methods used that we are trying out here....!)
'''

#Exercise #2: DNA translation

#Here's a dict that stores a codon usage table for translation:
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


# 1. Write a Python programme/script that will take any DNA sequence and translate it into protein using the translation table.
# 2. What happens if the DNA sequence contains undetermined bases (e.g. N)?
# 3. Can you generate a translation in all three "forward" frames (transcription is on the top strand, starting at base 1, 2, and 3)?
# 4. Can you generate a translation in all three "reverse" frames (transcription is on the bottom strand, starting at base end, end-1, and end-2)?


'''
Example input: ATGTTCGGT

Top strand frames:
ATG TTC GGT -->  1
 TGT TCG GT -->  2
  GTT CGG T -->  3

Bottom strand frames:
      ATG TTC GGT
1 <-- TAC AAG CCA

      AT GTT CGG
2 <-- TA CAA GCC

      A TGT TCG 
3 <-- T ACA AGC
'''

'''
What to do...(just a suggestion as to what you should ALWAYS do..!):
    - outline a workflow/pseudocode on paper/text file
    - figure out what inputs, processes, outputs might (need to) be
    - can any bits be made into a function?
    - test it with some very simple example data to see if it works as you think it should
'''
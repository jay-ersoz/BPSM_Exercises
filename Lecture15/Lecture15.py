#!/usr/bin/python3
import os, sys, MySQLdb

try:
    connection = MySQLdb.connect(
        host="127.0.0.1",      
        user="s3030309",
        passwd="yt1doswasplmsdT!",
        db="s3030309_blast"
    )
# Check our connection works
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    db_version = cursor.fetchone()
    print(f"Database version: {db_version[0]}")
# Lets remind ourselves of what tables we have
    cursor.execute("SHOW TABLES")
    print("+" * 60)
    for (table,) in cursor.fetchall():
       print(table)
    print("+" * 60)
# Let's check a specific table
    table_name="blast_output2"
    cursor.execute(f"DESCRIBE {table_name}")
# Get the query outputs
    columns = cursor.fetchall()
# Set up a display
    print(f"\nStructure for table: '{table_name}'")
    print("~" * 60)
    print(f"{'Field Name':<20} | {'Type':<15} | {'Null Allowed?':<12} | {'Key'}")
    print("~" * 60)
# Populate the display
    for col in columns:
        print(f"{col[0]:<20} | {col[1]:<15} | {col[2]:<13} | {col[3]}")
    print("-" * 60)
except MySQLdb.Error as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()

def get_table_choice(host, user, password, database):
# These are the Python comment lines in our function
    """
    Queries the database for all available tables and prompts the user to select one.
    Returns the string name of the chosen table, or None if exit/error.
    """
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        # Fetch all tables in the database
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        # Error trap...        
        if not tables:
            print("No tables found in this database.")
            return None
        # Display the tables as a numbered menu
        print("\nAvailable Tables:")
        print("-" * 30)
        for index, table_name in enumerate(tables, 1):
            print(f"[{index}] {table_name}")
        print("-" * 30)
        # Get the user to choose one!
        while True:
            try:
                choice = input(f"Pick a table number (1-{len(tables)}) or 'q' to quit: ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(tables):
                    return tables[choice_num - 1]
                else:
                    print(f"Invalid number. Please choose between 1 and {len(tables)}.")
            except ValueError:
                print("Please enter a valid number or 'q'.")
    except MySQLdb.Error as e:
        print(f"Database error while fetching tables: {e}")
        return None
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

'''Exercise 1: Amino acid percentages, part one'''
#Write a Python function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.

# prot_seq = str(input("Please enter a protein sequence: "))
# aa_residue = str(input("Please enter an amino acid residue code: "))

def percent_aa(prot_seq, aa_residue):
    prot_seq = str(prot_seq.upper())
    aa_residue = str(aa_residue.upper())
    count=0
    for aa in prot_seq:
        if aa == aa_residue:
            count+=1
    #result = f"The percentage of the protein that the amino acid residue makes up: " + str((count/len(prot_seq))*100) + "%"
    result = (count/len(prot_seq))*100
    return result

#Once you have written a function, use the following assertions to test your function:
#Remember to change the name of the function in these assert statements to match your function name!
assert round(percent_aa("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(percent_aa("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(percent_aa("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(percent_aa("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
#no errors!

'''Exercise 2: Amino acid percentages, part two'''
#Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence.
#If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V).
#Hint: To get this one to work, you'll have to go through the list of amino acid residues one at a time, generate the count for each one, and come up with a total count.
def percent_aa2(prot_seq, aa_residue_list=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    prot_seq = str(prot_seq.upper())
    count=0
    for aa in prot_seq:
        aa = str(aa.upper())
        for residue in aa_residue_list:
            residue = str(residue.upper())
            if aa == residue:
                count+=1
    result = (count/len(prot_seq))*100
    return result

#test:
#percent_aa2("MMMSSS", ["m", "A", "d"])

#Your function should pass the following assertions:
assert round(percent_aa2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(percent_aa2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(percent_aa2("MSRSLLLRFLLFLLLLPPLP")) == 65

'''Exercise 3: Base counter'''
#Write a Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether the DNA sequence contains a high 
#proportion of undetermined bases (i.e not A, T, G or C).

#undetermined bases are any characters that aren't A, T, G, or C
#defaulting the threshold to 0.5
#returns True if the proportion of undetermined bases is greater than or equal to threshold
def undetermined_bases(dna_seq, thresh=0.5):
    dna_seq = dna_seq.upper()
    count=0
    for base in dna_seq:
        if base!="A" and base!="G" and base!="C" and base!="T":
            count+=1
    if count/len(dna_seq) >= thresh:
        return True
    else:
        return False

#test:
#undetermined_bases("ACTGAC")

#Write some assertions to test whether the function works.

'''Exercise 4: Joined up SQL functions'''
#Using the lecture notes as a guide, write functions that will show the structure of a database table chosen by you, the user (i.e. one fuction might rely on the output 
#from the other).

'''Exercise 5: Kmer counting (again!)'''
#K-mers are short DNA subsequences with length "k" bases, and are usually generated using the sliding window method we used in previous lecture exercises.

#Write a Python function that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than n times.

#E.g. with dna="ATGCATCATG", kmersize=2 and minfrequency=2 will output:
#AT

#because the kmers (kmersize) are 2 bases long, and there are three (minfrequency was 2) instances of "AT"

#Code you wrote for the previous lecture's exercises could be useful here...

'''Exercise 6: Kmer counting (and yet again!)'''
#Write a Python script/programme that, given any DNA sequence, will print a list of k-mers that occur more than some number of times.

#The user should be asked to supply, on the command line, the following:
    # the sequence of interest
    # the kmer length for analysis
    # the threshold frequency of kmers found (i.e. the "more than this number" value)
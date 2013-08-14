from Bio.Seq import Seq

proteinFile = open("rosalind_prot.txt","r")
my_seq = Seq(proteinFile.read())
proteinFile.close

print my_seq.translate()



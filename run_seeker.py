from seeker import SeekerFasta
import sys

stdoutOrigin = sys.stdout
sys.stdout = open("log_group_5.txt", "w")
filename = ("/home/adralilla/Documents/new_thesis/MedbioTRP/output_group_5.fasta")
seeker_fasta = SeekerFasta(filename)
predictions = seeker_fasta.phage_or_bacteria() # This returns a list of phage/bacteria predictions for the Fasta
print("\n".join(predictions))

sys.stdout.close()
sys.stdout = stdoutOrigin

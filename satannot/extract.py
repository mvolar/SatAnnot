from Bio import SeqIO
import satannot.constants as constants
import satannot.utils as utils
from satannot.logging_config import logger
import os 

def extract_monomers(annotation_path: str, genome_path: str, output_path: str) -> None:
    
    if os.path.exists(output_path):
        raise FileExistsError(f"The directory '{output_path}' already exists. Please provide a different path.")
    else:
        # Create the directory
        os.makedirs(output_path)
        logger.info(f"Created directory: {output_path}")

    logger.info("Reading the genome")
    fasta_records = list(SeqIO.parse(genome_path, 'fasta'))
    logger.info(f"Extracting monomers from {annotation_path}")
    
    df = utils.read_gff_output(annotation_path, headers=False)
    grouped = df.group_by(["feature"])

    for group_key, group_df in grouped:
        subsequence_records = utils.extract_subsequences(fasta_records, group_df)
        full_outpath = output_path + "/" + group_key[0] + ".fasta"
        SeqIO.write(subsequence_records, full_outpath, 'fasta')


import subprocess
import argparse
import os
import glob
import satannot.constants as constants
import satannot.utils as utils
import polars as pl
from satannot.logging_config import logger


def create_blast_database(subject_file):
    subprocess.run(['makeblastdb', '-in', subject_file, '-dbtype', 'nucl', '-out', subject_file])
    return 

def cleanup_database_files(subject_file):
    # Clean up database files with the specified pattern
    pattern = f"./{subject_file}.n*"

    for file in glob.glob(pattern):
        print (f"removing databse file:{file}")
        os.remove(file)

def run_blast(query, subject, output,threads, evalue=10):
    # Define the BLAST command
    blast_cmd = [
        'blastn',  # Replace with the appropriate BLAST command (e.g., blastp, blastx, etc.)
        '-query', query,
        '-db', subject,
        '-out', output,
        '-evalue', str(evalue),
        '-outfmt', str(6),
        '-max_target_seqs', str(10000),
        '-task', "blastn",
        '-num_threads', str(threads)
    ]
    # Run the BLAST command
    subprocess.run(blast_cmd)


def annotate(sat_path, genome_path, blast_tmp="./tmp_blast.csv",gff_out=None,perc_id_filter=70,qcovhsp_filter=70,threads=8):
    logger.info("Creating a BLAST database")
    create_blast_database(genome_path)
    logger.info("Running a BLAST search")
    run_blast(sat_path, genome_path, blast_tmp,threads, 10)
    cleanup_database_files(genome_path)

    df = utils.read_blast_output(blast_tmp)
    df = df.with_columns(
        pl.when(df['s_start'] > df["s_end"]).then(df['s_end']).otherwise(df['s_start']).alias('new_start'),
        pl.when(df['s_start'] > df["s_end"]).then(df['s_start']).otherwise(df['s_end']).alias('new_end'),
        pl.when(df['s_start'] > df["s_end"]).then(pl.lit("-")).otherwise(pl.lit("+")).alias('strand'),
    )
    

    mlendf = (df
          .group_by('query')
          .agg([pl.col('q_end')
                .max()])
                .rename({"q_end":"max_len"}))
    df = df.join(mlendf,on="query")

    df = df.with_columns(
    qcovhsp = pl.col("al_len")*100/pl.col("max_len")
    )

    df = df.filter(
        (pl.col("perc_id") > perc_id_filter) &
        (pl.col("qcovhsp") > qcovhsp_filter)
    )
    logger.info("Writing the GFF annotations")
    df = utils.convert_df_to_gff(df)
    df.write_csv(gff_out, separator="\t", include_header=False)

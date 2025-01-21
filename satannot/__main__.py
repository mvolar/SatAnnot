import argparse
from satannot.blast_and_annotate import annotate
from satannot.extract import extract_monomers

def main():
    parser = argparse.ArgumentParser(description="satannot: A BLAST-based annotation and sequence extraction tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Annotate subcommand
    annotate_parser = subparsers.add_parser('annotate', help='Run BLAST-based annotation')
    annotate_parser.add_argument('sat_path', help='Path to the query sequence file in FASTA format')
    annotate_parser.add_argument('genome_path', help='Path to the subject file in FASTA format')
    annotate_parser.add_argument('--blast_tmp', '-b', default="./tmp_blast.csv", help='Temporary BLAST output file')
    annotate_parser.add_argument('--gff_out', '-g', required=True, help='Output GFF file')
    annotate_parser.add_argument('--perc_id_filter', type=float, default=70.0,
                                 help='Percentage identity filter (default: 70.0)')
    annotate_parser.add_argument('--qcovhsp_filter', type=float, default=70.0,
                                 help='Query coverage filter (default: 70.0)')
    annotate_parser.add_argument('--threads', type=int, default=8,
                                 help='Number of BLAST threads')
    annotate_parser.set_defaults(func=annotate)

  # Inside __main__.py
    extract_parser = subparsers.add_parser('extract', help='Extract monomers from a genome and annotation file')
    extract_parser.add_argument('genome_path', help='Path to the genome FASTA file')
    extract_parser.add_argument('annotation_path', help='Path to the annotation GFF file')
    extract_parser.add_argument('output_path', help='Folder to put the extracted monomers in.')
    extract_parser.set_defaults(func=lambda **kwargs: extract_monomers(
    kwargs['annotation_path'], kwargs['genome_path'], kwargs['output_path']
))

    # Parse arguments and execute
    args = parser.parse_args()

    # Call the assigned function with the correct arguments
    func_args = {k: v for k, v in vars(args).items() if k != "func" and k != "command"}
    args.func(**func_args)
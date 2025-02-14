# SatAnnot

satannot is a Python tool for BLAST-based annotation and sequence extraction. It provides functionalities for running BLAST searches, filtering results, and extracting sequences based on user-defined criteria.

---

Features
- Annotation: Annotate sequences using BLAST with customizable filtering options.
- Extraction: Extract sequences based on annotations in GFF format.


---

# Installation

## 0. Prerequisites
Ensure the following are installed on your system:
- Python: Version 3.8 or higher.
- NCBI BLAST+: Required for BLAST-based operations.

## 1. Installation

If you don't have NCBI-BLAST installed, best is done so with mamba/conda and to install `satannot` in a environment:

```
mamba create -c bioconda -c conda-forge -n satannot python=3.12 blast
mamba activate satannot
```

Then you can install satannot directly from GitHub:

```
pip install git+https://github.com/mvolar/satannot.git
```

# Usage


Run BLAST-based annotation and output results in GFF format followed by extractiong of FASTA sequences:
```
satannot annotate query.fasta genome.fasta --gff_out annotations.gff

Optional parameters:
--perc_id_filter: Minimum percentage identity (default: 70.0).
--qcovhsp_filter: Minimum query coverage per HSP (default: 70.0).

satannot extract genome.fasta annotations.gff output_directory
```
---

# License
This project is licensed under the MIT License (LICENSE).

---

# Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the tool.

---

# Citation
If you use SatAnnot in you work please cite:

```
Marin Volarić, Nevenka Meštrović, Evelin Despot-Slade,
SatXplor—a comprehensive pipeline for satellite DNA analyses in complex genome assemblies, Briefings in Bioinformatics, Volume 26, Issue 1, January 2025, bbae660, https://doi.org/10.1093/bib/bbae660

```

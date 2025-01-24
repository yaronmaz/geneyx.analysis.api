Unifying structural vcf files

UnifyVcf.py is a script that unifies different types of vcf files so that the unified file can be 
uploaded as sv-vcf into Geneyx application.

Please notice this script should be ran using python3

The vcf files that are unified by it are:
SV - structural variants vcf
CNV - copy number variants vcf
Repeats - tandem repeat variants vcf
ROH - Regions of Homozygosity bed

This script not only unifies the files but also modifies them when necessary, since each provider provides 
slightly different vcf files and the final file has to include specific fields for Geneyx application 
to be able to read it properly.
Hence, it's important to run the script that matches the pipeline with which the vcf files were created.

The optionts are:

DragenUnifyVcf.py - for DRAGEN pipeline
ONTUnifyVcf.py - for Oxford Nanopore sequences and pipeline
PacBioUnifyVcf.py - for PacBio sequences and pipeline

Running the Unifying scripts:
usage: DragenUnifyVcf.py [-h] -o OUTPUTPATH [-s SVPATH] [-c CNVPATH] [-r REPEATPATH] [-d ROH_BED_FILE]
usage: ONTUnifyVcf.py [-h] -o OUTPUTPATH [-s SVPATH] [-c CNVPATH] [-r REPEATPATH]
usage: PacBioUnifyVcf.py [-h] -o OUTPUTPATH [-s SVPATH] [-c CNVPATH] [-r FULLREPEATPATH] [-b REPEATLOCATIONSBEDFILEPATH]

-o        The path to the unified vcf file, including its name. The script compresses 
		  the output file, so its name should end with ".vcf" and not ".gz"
-s        The path to the structural variants (sv) vcf. This file can be either gzipped or unzipped, 
          but it must be a vcf file.
-c        The path to the Copy Number Variants (CNV) vcf. This file can be either gzipped or unzipped, 
          but it must be a vcf file.
-r        The path to the tandem repeats variants vcf. This file can be either gzipped or unzipped, 
          but it must be a vcf file.
-b        Relevant only for PacBio. A bed file used to filter the repeats vcf file. 
          If the PacBioUnifyVcf.py script is called without this parameter,
          the repeats vcf file (if given) will not be unified.
		  When called with this parameter, the PacBioUnifyVcf.py script creates a filtered repeats 
		  vcf file and unifies it (rather than the full repeats file) with the other vcf files.
		  This bed file can be downloaded from PacBio's github: 
		  https://github.com/PacificBiosciences/trgt/tree/main/repeats 
		  (named pathogenic_repeats.hg38.bed or the like)
		  Please notice that when running with this parameter you have to run on linux 
		  and have bedtools installed
-d        Relevant only for Dragen. Path to the Bed file of the Regions of Homozigosity (ROH) produced 
          by dragen when run with the --vc-enable-roh flag.
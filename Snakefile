import os
import yaml

configfile:'config_81176.yaml'

rule all:
    input:
        "logs/bedfiles.log",
        "logs/fastafiles.log"


rule make_beds:
    input:
        features_file = config['features_file']
    params:
        feature_column = config['feature_column'],
        chromosome_name = config['chromosome_name'],
        outdir = config["base_outdir"]
    output:
        outfile = "logs/bedfiles.log"
    script:
        "scripts/make_bedfiles.py"

rule make_fastas:
    input:
        fasta_file = config["fasta_file"]
    params:
        outdir = config["base_outdir"],
        input_dir = os.path.join(config["base_outdir"], "bedfiles")
    output:
        outfile = "logs/fastafiles.log"
    script:
        "scripts/make_fastas.py"

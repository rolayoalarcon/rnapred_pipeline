import os
import pandas as pd


def create_outdirectory(odir, subdir):
    complete_odir = os.path.join(odir, subdir)

    if not os.path.exists(complete_odir):
        os.mkdir(complete_odir)
    return complete_odir

def make_bed(complete_df, feature_type, feat_column, chr_name, odir):
    feat_df = complete_df.loc[complete_df[feat_column] == feature_type]
    
    # Add missing info
    feat_df["chr"] = chr_name
    feat_df["score"] = 0
    
    # Order columns
    feat_df = feat_df[["chr", "start", "end", "locus_tag", "score", "strand"]]
    feat_df["start"] = feat_df["start"] - 1

    # Create filename
    filename = feature_type + ".bed"
    complete_filename = os.path.join(odir, filename)

    # Write file 
    feat_df.to_csv(complete_filename, sep='\t', index=False, header=False)

    return True


def main(infile, feature_col, chromosome_name, output_dir, outfile):
    
    # Read in files
    features_df = pd.read_csv(infile, sep='\t')

    # Create output subdirectory
    out_subdir = create_outdirectory(output_dir, "bedfiles")

    # Write a bedfile for each feature type
    stat = [make_bed(features_df, ftype, feature_col, chromosome_name, out_subdir) for ftype in features_df[feature_col].unique()]

    
    if all(stat):
        print(f"complete bedfiles in {out_subdir}")
        with open(outfile, "w") as file:
            file.write("Successful bed")
    

if __name__ == "__main__":
    main(snakemake.input.features_file,
         snakemake.params.feature_column,
         snakemake.params.chromosome_name,
         snakemake.params.outdir,
         snakemake.output.outfile)





    



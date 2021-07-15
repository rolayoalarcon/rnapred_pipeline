import os
import glob
import pybedtools as pt

def create_outdirectory(odir, subdir):
    complete_odir = os.path.join(odir, subdir)

    if not os.path.exists(complete_odir):
        os.mkdir(complete_odir)
    return complete_odir

def create_fasta(infile, fasta, outdir):
    bed_coords = pt.BedTool(infile)

    # Output file
    ftype = os.path.basename(infile).split(".")[0]
    filename = ftype + ".fa"
    complete_filename = os.path.join(outdir, filename)

    bed_fasta = bed_coords.sequence(fi=fasta, s=True, nameOnly=True, fo=complete_filename)

    return True

def main(idir, odir, fasta_file, outfile):
    
    out_subdir = create_outdirectory(odir, "fastas")

    stat = [create_fasta(file, fasta_file, out_subdir) for file in glob.iglob(os.path.join(idir, "*.bed"))]

    if all(stat):
        print(f"Finished fastas as {out_subdir}")
        with open(outfile, "w") as file:
            file.write("Successful faastas")

if __name__ == "__main__":
    main(snakemake.params.input_dir,
         snakemake.params.outdir,
         snakemake.input.fasta_file,
         snakemake.output.outfile)



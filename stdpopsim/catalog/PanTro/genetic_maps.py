import stdpopsim

_panmap2012 = stdpopsim.Citation(
    doi="https://doi.org/10.1126/science.1216872",
    year=2012,
    author="Auton et al.",
)

_species = stdpopsim.get_species("PanTro")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="PanMap_GRCh37",
    description="PanMap lifted over to GRCh37",
    long_description="""
        This genetic map is from the Panmap project (http://panmap.uchicago.edu/data.html)
        and based on 3.1 million genotyped SNPs
        from 270 individuals across four populations (YRI, CEU, CHB and JPT).
        Genome wide recombination rates were estimated using LDHat.
        This version of the HapMap genetic map was lifted over to GRCh37
        (and adjusted in regions where the genome assembly had rearranged)
        for use in the 1000 Genomes project. Please see the README file on
        the 1000 Genomes download site for details of these adjustments.
        ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/working/20110106_recombination_hotspots
        """,
    url=(
        "https://stdpopsim.s3-us-west-2.amazonaws.com/genetic_maps/"
        "PanTro/Panmap_GRCh37_RecombinationHotspots.tar.gz"
    ),
    sha256="",
    file_pattern="genetic_map_GRCh37_chr{id}.txt",
    citations=[_panmap2012.because(stdpopsim.CiteReason.GEN_MAP)],
)

_species.add_genetic_map(_gm)
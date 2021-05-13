import stdpopsim

_panmap2012 = stdpopsim.Citation(
    doi="https://doi.org/10.1126/science.1216872",
    year=2012,
    author="Auton et al.",
)

_species = stdpopsim.get_species("PanTro")

_gm = stdpopsim.GeneticMap(
    species=_species,
    id="PanMap_Pan_tro_3.0",
    description="PanMap genetic map lifted over from panTro2 to Pan_tro_3.0 (panTro5)",
    long_description="""
        This genetic map is from the Panmap project (http://panmap.uchicago.edu/data.html).
        The original map was inferred using 10 Western chimpanzee individuals with the reference genome panTro2.
        Here, the genomic coordinates were converted from panTro2 to panTro3 first, then converted from panTro3 to Pan_tro_3.0 (panTro5) using the LiftOver service in the UCSC genome browser (https://genome.ucsc.edu/cgi-bin/hgLiftOver).
        The recombination rates were also converted from the population-scale recombinate rate per site (4Ner/kb) to the recombination rate per site (cM/Mb) by assuming the effective population size 10,000.
        """,
    url=(
        "https://stdpopsim.s3-us-west-2.amazonaws.com/genetic_maps/"
        "PanTro/Panmap_Pan_tro_3.0_RecombinationHotspots.tar.gz"
    ),
    sha256="",
    file_pattern="genetic_map_Pan_tro_3.0_chr{id}.txt",
    citations=[_panmap2012.because(stdpopsim.CiteReason.GEN_MAP)],
)

_species.add_genetic_map(_gm)
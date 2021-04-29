import stdpopsim

from . import genome_data

_assembly_citation = stdpopsim.Citation(
    author="The Chimpanzee Sequencing and Analysis Consortium",
    year="2005",
    doi="https://doi.org/10.1038/nature04072",
    reasons={stdpopsim.CiteReason.ASSEMBLY},
)

_mutation_rate_citation = stdpopsim.Citation(
    author="Kong et al.",
    year="2012",
    doi="https://doi.org/10.1038/nature11396",
    reasons={stdpopsim.CiteReason.MUT_RATE},
)

_recombination_rate_citation = stdpopsim.Citation(
    author="Stevison et al.",
    year="2016",
    doi="https://doi.org/10.1093/molbev/msv331",
    reasons={stdpopsim.CiteReason.REC_RATE},
)

_chromosomes = []

for name, data in genome_data.data["chromosomes"].items():
    _chromosomes.append(
        stdpopsim.Chromosome(
            id=name,
            length=data["length"],
            synonyms=data["synonyms"],
            mutation_rate=1.20e-8,
            recombination_rate=0.7e-8,
        )
    )

_genome = stdpopsim.Genome(
    chromosomes=_chromosomes,
    assembly_name=genome_data.data["assembly_name"],
    assembly_accession=genome_data.data["assembly_accession"],
    assembly_citations=[],
    citations=[
        _assembly_citation,
        _mutation_rate_citation.because(stdpopsim.CiteReason.MUT_RATE),
        _recombination_rate_citation.because(stdpopsim.CiteReason.REC_RATE),
    ]
)

_gen_time_citation = stdpopsim.Citation(
    author="Langergraber et al.",
    year="2012",
    doi="https://doi.org/10.1073/pnas.1211740109",
    reasons={stdpopsim.CiteReason.GEN_TIME},
)

_pop_size_citation = stdpopsim.Citation(
    author="de Manuel et al.",
    year="2016",
    doi="https://doi.org/10.1126/science.aag2602",
    reasons={stdpopsim.CiteReason.POP_SIZE},
)

_species = stdpopsim.Species(
    id="PanTro",
    name="Pan Troglodytes",
    common_name="Chimpanzee",
    genome=_genome,
    generation_time=25,
    population_size=15000,
    citations=[
        _gen_time_citation.because(stdpopsim.CiteReason.GEN_TIME),
        _pop_size_citation.because(stdpopsim.CiteReason.POP_SIZE)
    ]
)

stdpopsim.register_species(_species)
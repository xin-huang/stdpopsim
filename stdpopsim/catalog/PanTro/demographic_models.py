import math
import msprime

import stdpopsim

_species = stdpopsim.get_species("PanTro")

###########################################################
#
# Demographic models
#
###########################################################

# population definitions that are reused.

_bonoboo = stdpopsim.Population(
    id="Bon",
    description="Pan paniscus"
)

_western_chimpanzee = stdpopsim.Population(
    id="West",
    description="Pan troglodytes"
)

_eastern_chimpanzee = stdpopsim.Population(
    id="East",
    description="Pan troglodytes"
)

_central_chimpanzee = stdpopsim.Population(
    id="Cent",
    description="Pan troglodytes"
)

_nigeria_cameroon_chimpanzee = stdpopsim.Population(
    id="NigCam",
    description="Pan troglodytes"
)

_de_Manuel_et_al = stdpopsim.Citation(
    author="de Manuel et al.",
    year="2016",
    doi="https://doi.org/10.1126/science.aag2602",
    reasons={stdpopsim.CiteReason.DEM_MODEL},
)

def _bcen_4D16():
    id = "BCEN_4D16"
    description = "Demographic model for two wild tomato species"
    long_description = """"""
    populations = [_bonoboo, _eastern_chimpanzee, _central_chimpanzee, _nigeria_cameroon_chimpanzee]
    citations = [_de_Manuel_et_al]
    
    generation_time = 25
    
    N_A = 429021
    N_schi = 553437
    N_sper = 1621699
    T = 1295282
    # migration rate from schi to sper
    m_schi_sper = 1.575e-7
    # migration rate from sper to schi
    m_sper_schi = 3.17e-7
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_schi,
                metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=N_sper,
                metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=[
            [0, m_schi_sper],
            [m_sper_schi, 0],
        ],
        demographic_events=[
            msprime.MassMigration(time=T, source=1, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=T, rate=0),
            msprime.PopulationParametersChange(
                time=T, initial_size=N_A, population_id=0
            ),
        ],
    )
    
_species.add_demographic_model(_bcen_4D16())

def _bcew_4D16():
    id = "BCEW_4D16"
    description = "Demographic model for two wild tomato species"
    long_description = """"""
    populations = [_bonoboo, _eastern_chimpanzee, _central_chimpanzee, _western_chimpanzee]
    citations = [_de_Manuel_et_al]
    
    generation_time = 25
    
    N_A = 378830
    N_schi = 689546
    N_sper = 1868731
    T = 1034812
    # migration rate from schi to sper
    m_schi_sper = 1.74e-7
    # migration rate from sper to schi
    m_sper_schi = 2.04e-7
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=N_schi,
                metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=N_sper,
                metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=[
            [0, m_schi_sper],
            [m_sper_schi, 0],
        ],
        demographic_events=[
            msprime.MassMigration(time=T, source=1, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=T, rate=0),
            msprime.PopulationParametersChange(
                time=T, initial_size=N_A, population_id=0
            ),
        ],
    )
    
_species.add_demographic_model(_bcew_4D16())
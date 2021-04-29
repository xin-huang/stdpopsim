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
    description = "Demographic model for bonoboos, central, eastern, and Nigeria-Cameroon chimpanzees"
    long_description = """"""
    populations = [_bonoboo, _central_chimpanzee, _eastern_chimpanzee, _nigeria_cameroon_chimpanzee]
    citations = [_de_Manuel_et_al]
    
    generation_time = 25
    
    # population sizes
    N_A = 15299
    N_anc_Bon = 2947
    N_anc_NigCam = 12435
    N_Bon = 17490
    N_Cent = 33578
    N_East = 10634
    N_NigCam = 13279
    N_curr_Bon = 1369
    N_curr_Cent = 2705
    N_curr_East = 2150
    N_curr_NigCam = 453
    N_botl_Bon = 947
    N_botl_NigCam = 790
    N_botl_split_CChimp = 19
    N_botl_split_NigCam = 252
    N_botl_split_East = 561
    N_botl_split_Cent = 2133
    
    # migration rates
    # migration rates between bonoboos and central chimpanzees
    m_Bon_Cent = 0.24/(2*N_A)
    m_Cent_Bon = 0.14/(2*N_A)
    # migration rates between bonoboos and the most recent common ancestor of central and eastern chimpanzees
    m_Bon_aEC = 0
    m_aEC_Bon = 0
    # migration rates between bonoboos and the ancestral common chimpanzees
    m_Bon_aC = 0.03/(2*N_A)
    m_ac_Bon = 0.03/(2*N_A)
    # migration rates between central and eastern chimpanzees
    m_Cent_East = 1.17/(2*N_A)
    m_East_Cent = 4.34/(2*N_A)
    # migration rates between Nigeria-Cameroon and central chimpanzees
    m_NigCam_Cent = 0.76/(2*N_A)
    m_Cent_NigCam = 1.90/(2*N_A)
    # migration rates between Nigeria-Cameroon and eastern chimpanzees
    m_NigCam_East = 0.57/(2*N_A)
    m_East_NigCam = 0.45/(2*N_A)
    # migration rates between Nigeria-Cameroon and the most recent common ancestor of central and eastern chimpanzees
    m_NigCam_aEC = 0.02/(2*N_A)
    m_aEC_NigCam = 0.01/(2*N_A)
    
    # times (generation)
    T_Bon_split = int(1562000/generation_time)
    T_NigCam_split = int(429000/generation_time)
    T_East_Cent_split = int(104000/generation_time)
    T_Bon_mig_stop = int(77000/generation_time)
    T_NigCam_mig_stop = int(15000/generation_time)
    T_botl_Bon = int(439000/generation_time)
    T_botl_NigCam = int(86000/generation_time)
    
    population_configurations=[
        msprime.PopulationConfiguration(
            initial_size=N_curr_Bon,
            metadata=populations[0].asdict()
        ),
        msprime.PopulationConfiguration(
            initial_size=N_curr_Cent,
            metadata=populations[1].asdict()
        ),
        msprime.PopulationConfiguration(
            initial_size=N_curr_East,
            metadata=populations[2].asdict()
        ),
        msprime.PopulationConfiguration(
            initial_size=N_curr_NigCam,
            metadata=populations[3].asdict()
        ),
    ]
    
    migration_matrix=[
        [0, m_schi_sper],
        [m_sper_schi, 0],
    ]
    
    demographic_events=[
            msprime.MassMigration(time=T, source=1, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=T, rate=0),
            msprime.PopulationParametersChange(
                time=T, initial_size=N_A, population_id=0
            ),
    ]
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
    )
    
_species.add_demographic_model(_bcen_4D16())

def _bcew_4D16():
    id = "BCEW_4D16"
    description = "Demographic model for bonoboos, central, eastern, and western chimpanzees"
    long_description = """"""
    populations = [_bonoboo, _central_chimpanzee, _eastern_chimpanzee, _western_chimpanzee]
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
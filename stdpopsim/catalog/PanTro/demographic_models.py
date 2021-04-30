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

_bonobo = stdpopsim.Population(
    id="Bon",
    description="Pan Paniscus"
)

_western_chimpanzee = stdpopsim.Population(
    id="West",
    description="Pan Troglodytes Verus"
)

_eastern_chimpanzee = stdpopsim.Population(
    id="East",
    description="Pan Troglodytes Schweinfurthii"
)

_central_chimpanzee = stdpopsim.Population(
    id="Cent",
    description="Pan Troglodytes Troglodytes"
)

_nigeria_cameroon_chimpanzee = stdpopsim.Population(
    id="NigCam",
    description="Pan Troglodytes Ellioti"
)

_de_Manuel_et_al = stdpopsim.Citation(
    author="de Manuel et al.",
    year="2016",
    doi="https://doi.org/10.1126/science.aag2602",
    reasons={stdpopsim.CiteReason.DEM_MODEL},
)

_kuhlwilm_et_al = stdpopsim.Citation(
    author="Kuhlwilm et al.",
    year="2019",
    doi="https://doi.org/10.1038/s41559-019-0881-7",
    reasons={stdpopsim.CiteReason.DEM_MODEL}
)

def _bcen_4D16():
    
    id = "BCEN_4D16"
    description = "Demographic model for bonobos, central, eastern, and Nigeria-Cameroon chimpanzees"
    long_description = """"""
    populations = [_bonobo, _central_chimpanzee, _eastern_chimpanzee, _nigeria_cameroon_chimpanzee]
    citations = [_de_Manuel_et_al]
    
    generation_time = 25
    mutation_rate = 1.2e-8
    
    # Figure S54
    # Table S18
    # population sizes (Table S18 caption - all effective sizes are given as number of diploid individuals)
    N_A = 15299*2 # ancestral population size of bonobo-chimpanzees
    N_anc_Bon = 2947*2 # ancestral population size of bonobos before bottleneck
    N_anc_CChimp = 19326*2 # ancestral population size of common chimpanzees
    N_anc_NigCam = 12435*2 # ancestral population size of nigeria-cameroon chimpanzees before bottleneck
    N_anc_CE = 157757*2 # ancestral population size of central-eastern chimpanzees
    N_Bon = 17490*2 # population size of bonobos after bottleneck
    N_Cent = 33578*2 # population size of central chimpanzees before decline 
    N_East = 10634*2 # population size of eastern chimpanzees before decline
    N_NigCam = 13279*2 # population size of nigera-cameroon chimpanzees before decline
    N_curr_Bon = 1369*2 # current population size of bonobos after decline
    N_curr_Cent = 2705*2 # current population size of central chimpanzees after decline
    N_curr_East = 2150*2 # current population size of eastern chimpanzees after decline 
    N_curr_NigCam = 453*2 # current population size of nigeria-cameroon chimpanzees after decline
    N_botl_Bon = 947*2 # population size of bonobos during 100-generation bottleneck
    N_botl_NigCam = 790*2 # population size of nigeria-cameroon chimpanzees during 100-generation bottleneck
    N_botl_split_CChimp = 19*2 # population size of ancestral common chimpanzees during 100-generation bottleneck after split from ancestral pan population
    N_botl_split_NigCam = 252*2 # population size of nigeria-cameroon chimpanzees during 100-generation bottleneck after split from ancestral common chimpanzees
    N_botl_split_East = 561*2  # population size of eastern chimpanzees during 100-generation bottleneck after split from ancestral central-eastern chimpanzees
    N_botl_split_Cent = 2133*2 # population size of central chimpanzees during 100-generation bottleneck after split from ancestral central-eastern chimpanzees
    
    # migration rates
    # migration rates between bonobos and central chimpanzees
    m_Bon_Cent = 0.24/(2*N_A)
    m_Cent_Bon = 0.14/(2*N_A)
    # migration rates between bonobos and the most recent common ancestor of central and eastern chimpanzees
    m_Bon_aEC = 0
    m_aEC_Bon = 0
    # migration rates between bonobos and the ancestral common chimpanzees
    m_Bon_aC = 0.03/(2*N_A)
    m_aC_Bon = 0.03/(2*N_A)
    # migration rates between central and eastern chimpanzees
    m_Cent_East = 1.17/(2*N_A)
    m_East_Cent = 4.34/(2*N_A)
    # migration rates between nigeria-cameroon and central chimpanzees
    m_NigCam_Cent = 0.76/(2*N_A)
    m_Cent_NigCam = 1.90/(2*N_A)
    # migration rates between nigeria-cameroon and eastern chimpanzees
    m_NigCam_East = 0.57/(2*N_A)
    m_East_NigCam = 0.45/(2*N_A)
    # migration rates between nigeria-cameroon and the most recent common ancestor of central and eastern chimpanzees
    m_NigCam_aEC = 0.02/(2*N_A)
    m_aEC_NigCam = 0.01/(2*N_A)
    
    # times (generation)
    T_Bon_split = int(1562000/generation_time) # Time of bonobo split from the ancestral population
    T_botl_Bon = int(439000/generation_time) # Time of bonobo bottleneck
    T_NigCam_split = int(429000/generation_time) # Time of nigeria-cameroon chimpanzee split from the ancestral common chimpanzees
    T_East_Cent_split = int(104000/generation_time) # Time of eastern and central chimpanzee split
    T_botl_NigCam = int(86000/generation_time) # Time of nigeria-cameroon chimpanzee bottleneck
    T_Bon_mig_stop = int(77000/generation_time) # Time of bonobo migration stop
    T_NigCam_mig_stop = int(15000/generation_time) # Time of nigeria-cameroon chimpanzee migration stop
    T_resize = int(1700/generation_time) # Time of recent population decline
    
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
        # bonobo, central, eastern, nigeria_cameroon
        [0,       0,       0,       0], # bonobo
        [0,       0, m_Cent_East,   0], # central
        [0, m_East_Cent,   0,       0], # eastern
        [0,       0,       0,       0], # nigeria_cameroon
    ]
    
    demographic_events=[
        # Recent population decline
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_Bon, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_Cent, population_id=1
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_East, population_id=2
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_NigCam, population_id=3
        ),
        # migration between nigeria-cameroon and central chimpanzees
        msprime.MigrationRateChange(
            time=T_NigCam_mig_stop, rate=m_Cent_NigCam, matrix_index=(1, 3)
        ),
        msprime.MigrationRateChange(
            time=T_NigCam_mig_stop, rate=m_NigCam_Cent, matrix_index=(3, 1)
        ),
        # migration between nigeria-cameroon and eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_NigCam_mig_stop, rate=m_East_NigCam, matrix_index=(2, 3)
        ),
        msprime.MigrationRateChange(
            time=T_NigCam_mig_stop, rate=m_NigCam_East, matrix_index=(3, 2)
        ),
        # migration between bonobos and central chimpanzees
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Bon_Cent, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Cent_Bon, matrix_index=(1, 0)
        ),
        # 100-generation bottleneck in nigeria-cameroon chimpanzees
        msprime.PopulationParametersChange(
            time=T_botl_NigCam-100, initial_size=N_botl_NigCam, population_id=3
        ),
        msprime.PopulationParametersChange(
            time=T_botl_NigCam, initial_size=N_anc_NigCam, population_id=3
        ),
        # 100-generation bottleneck in central chimpanzees after split from ancestral central-eastern chimpanzees
        msprime.PopulationParametersChange(
            time=T_East_Cent_split-100, initial_size=N_botl_split_Cent, population_id=1
        ),
        # 100-generation bottleneck in eastern chimpanzees after split from ancestral central-eastern chimpanzees
        msprime.PopulationParametersChange(
            time=T_East_Cent_split-100, initial_size=N_botl_split_East, population_id=2
        ),
        # merge eastern chimpanzees into central chimpanzees
        msprime.MassMigration(
            time=T_East_Cent_split, source=2, destination=1, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_East_Cent_split, initial_size=N_anc_CE, population_id=1
        ),
        # migration between bonobos and ancestral central-eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_Bon_aEC, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_aEC_Bon, matrix_index=(1, 0)
        ),
        # migration between nigeria-cameroon and ancestral central-eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_aEC_NigCam, matrix_index=(1, 3)
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_NigCam_aEC, matrix_index=(3, 1)
        ),
        # 100-generation bottleneck in nigeria-cameroon chimpanzees after split from ancestral common chimpanzees
        msprime.PopulationParametersChange(
            time=T_NigCam_split-100, initial_size=N_botl_split_NigCam, population_id=2
        ),
        # merge ancestral central-eastern chimpanzees and nigeria-cameroon chimpanzees into ancestral common chimpanzees
        msprime.MassMigration(
            time=T_NigCam_split, source=3, destination=1, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_NigCam_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_NigCam_split, initial_size=N_anc_CChimp, population_id=1
        ),
        # migration between bonobos and ancestral common chimpanzees
        msprime.MigrationRateChange(
            time=T_NigCam_split, rate=m_Bon_aC, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_NigCam_split, rate=m_aC_Bon, matrix_index=(1, 0)
        ),
        # 100-generation bottleneck in bonobos
        msprime.PopulationParametersChange(
            time=T_botl_Bon-100, initial_size=N_botl_Bon, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_botl_Bon, initial_size=N_anc_Bon, population_id=0
        ),
        # merge ancestral common chimpanzees and bonobos
        msprime.MassMigration(
            time=T_Bon_split, source=1, destination=0, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_Bon_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_Bon_split, initial_size=N_A, population_id=0
        ),
    ]
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
        mutation_rate=mutation_rate,
        populations=populations,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )
    
_species.add_demographic_model(_bcen_4D16())

def _bcew_4D16():
    
    id = "BCEW_4D16"
    description = "Demographic model for bonobos, central, eastern, and western chimpanzees"
    long_description = """"""
    populations = [_bonobo, _central_chimpanzee, _eastern_chimpanzee, _western_chimpanzee]
    citations = [_de_Manuel_et_al]
    
    generation_time = 25
    mutation_rate = 1.2e-8
    
    # Figure S51
    # Table S15
    # population sizes (Table S15 caption - all effective sizes are given as number of diploid individuals)
    N_A = 5738*2 # ancestral population size of bonobo-chimpanzees
    N_anc_Bon = 23968*2 # ancestral population size of bonobos before bottleneck
    N_anc_CChimp = 12302*2 # ancestral population size of common chimpanzees
    N_anc_West = 1895*2 # ancestral population size of western chimpanzees before bottleneck
    N_anc_CE = 74044*2 # ancestral population size of central-eastern chimpanzees
    N_Bon = 16232*2 # population size of bonobos after bottleneck
    N_Cent = 48306*2 # population size of central chimpanzees before decline 
    N_East = 17650*2 # population size of eastern chimpanzees before decline
    N_West = 12323*2 # population size of western chimpanzees before decline
    N_curr_Bon = 2069*2 # current population size of bonobos after decline
    N_curr_Cent = 2444*2 # current population size of central chimpanzees after decline
    N_curr_East = 1738*2 # current population size of eastern chimpanzees after decline 
    N_curr_West = 545*2 # current population size of western chimpanzees after decline
    N_botl_Bon = 17*2 # population size of bonobos during 100-generation bottleneck
    N_botl_West = 1185*2 # population size of nigeria-cameroon chimpanzees during 100-generation bottleneck
    N_botl_split_CChimp = 1374*2 # population size of ancestral common chimpanzees during 100-generation bottleneck after split from ancestral pan population
    N_botl_split_West = 1409*2 # population size of western chimpanzees during 100-generation bottleneck after split from ancestral common chimpanzees
    N_botl_split_East = 508*2  # population size of eastern chimpanzees during 100-generation bottleneck after split from ancestral central-eastern chimpanzees
    N_botl_split_Cent = 2160*2 # population size of central chimpanzees during 100-generation bottleneck after split from ancestral central-eastern chimpanzees
    
    # migration rates
    # migration rates between bonobos and central chimpanzees
    m_Bon_Cent = 0/(2*N_A)
    m_Cent_Bon = 0.09/(2*N_A)
    # migration rates between bonobos and the most recent common ancestor of central and eastern chimpanzees
    m_Bon_aEC = 0.06/(2*N_A)
    m_aEC_Bon = 0.08/(2*N_A)
    # migration rates between bonobos and the ancestral common chimpanzees
    m_Bon_aC = 0.01/(2*N_A)
    m_aC_Bon = 0.18/(2*N_A)
    # migration rates between central and eastern chimpanzees
    m_Cent_East = 1.32/(2*N_A)
    m_East_Cent = 4.92/(2*N_A)
    # migration rates between western and central chimpanzees
    m_West_Cent = 0.02/(2*N_A)
    m_Cent_West = 0/(2*N_A)
    # migration rates between western and eastern chimpanzees
    m_West_East = 0.66/(2*N_A)
    m_East_West = 0/(2*N_A)
    # migration rates between western and the most recent common ancestor of central and eastern chimpanzees
    m_West_aEC = 0.93/(2*N_A)
    m_aEC_West = 0.14/(2*N_A)
    
    # times (generation)
    T_Bon_split = int(1989000/generation_time) # Time of bonobo split from the ancestral population
    T_West_split = int(603000/generation_time) # Time of western chimpanzee split from the ancestral common chimpanzees
    T_botl_Bon = int(555000/generation_time) # Time of bonobo bottleneck
    T_botl_West = int(221000/generation_time) # Time of western chimpanzee bottleneck
    T_East_Cent_split = int(164000/generation_time) # Time of eastern and central chimpanzee split
    T_Bon_mig_stop = int(125000/generation_time) # Time of bonobo migration stop
    T_West_mig_stop = int(112000/generation_time) # Time of western chimpanzee migration stop
    T_resize = int(1500/generation_time) # Time of recent population decline
    
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
            initial_size=N_curr_West,
            metadata=populations[3].asdict()
        ),
    ]
    
    migration_matrix=[
        # bonobo, central, eastern, western
        [0,       0,       0,       0], # bonobo
        [0,       0, m_Cent_East,   0], # central
        [0, m_East_Cent,   0,       0], # eastern
        [0,       0,       0,       0], # western
    ]
    
    demographic_events=[
        # Recent population decline
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_Bon, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_Cent, population_id=1
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_East, population_id=2
        ),
        msprime.PopulationParametersChange(
            time=T_resize, initial_size=N_West, population_id=3
        ),
        # migration between western and central chimpanzees
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_Cent_West, matrix_index=(1, 3)
        ),
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_West_Cent, matrix_index=(3, 1)
        ),
        # migration between western and eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_East_West, matrix_index=(2, 3)
        ),
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_West_East, matrix_index=(3, 2)
        ),
        # migration between bonobos and central chimpanzees
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Bon_Cent, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Cent_Bon, matrix_index=(1, 0)
        ),
        # 100-generation bottleneck in central chimpanzees after split from ancestral central-eastern chimpanzees
        msprime.PopulationParametersChange(
            time=T_East_Cent_split-100, initial_size=N_botl_split_Cent, population_id=1
        ),
        # 100-generation bottleneck in eastern chimpanzees after split from ancestral central-eastern chimpanzees
        msprime.PopulationParametersChange(
            time=T_East_Cent_split-100, initial_size=N_botl_split_East, population_id=2
        ),
        # merge eastern chimpanzees into central chimpanzees
        msprime.MassMigration(
            time=T_East_Cent_split, source=2, destination=1, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_East_Cent_split, initial_size=N_anc_CE, population_id=1
        ),
        # migration between bonobos and ancestral central-eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_Bon_aEC, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_aEC_Bon, matrix_index=(1, 0)
        ),
        # migration between western and ancestral central-eastern chimpanzees
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_aEC_West, matrix_index=(1, 3)
        ),
        msprime.MigrationRateChange(
            time=T_East_Cent_split, rate=m_West_aEC, matrix_index=(3, 1)
        ),
        # 100-generation bottleneck in western chimpanzees
        msprime.PopulationParametersChange(
            time=T_botl_West-100, initial_size=N_botl_West, population_id=3
        ),
        msprime.PopulationParametersChange(
            time=T_botl_West, initial_size=N_anc_West, population_id=3
        ),
        # 100-generation bottleneck in bonobos
        msprime.PopulationParametersChange(
            time=T_botl_Bon-100, initial_size=N_botl_Bon, population_id=0
        ),
        msprime.PopulationParametersChange(
            time=T_botl_Bon, initial_size=N_anc_Bon, population_id=0
        ),
        # 100-generation bottleneck in western chimpanzees after split from ancestral common chimpanzees
        msprime.PopulationParametersChange(
            time=T_West_split-100, initial_size=N_botl_split_West, population_id=2
        ),
        # merge ancestral central-eastern chimpanzees and western chimpanzees into ancestral common chimpanzees
        msprime.MassMigration(
            time=T_West_split, source=3, destination=1, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_West_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_West_split, initial_size=N_anc_CChimp, population_id=1
        ),
        # migration between bonobos and ancestral common chimpanzees
        msprime.MigrationRateChange(
            time=T_West_split, rate=m_Bon_aC, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_West_split, rate=m_aC_Bon, matrix_index=(1, 0)
        ),
        # merge ancestral common chimpanzees and bonobos
        msprime.MassMigration(
            time=T_Bon_split, source=1, destination=0, proportion=1.0
        ),
        msprime.MigrationRateChange(
            time=T_Bon_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_Bon_split, initial_size=N_A, population_id=0
        ),
    ]
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
        mutation_rate=mutation_rate,
        populations=populations,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )
    
_species.add_demographic_model(_bcew_4D16())

def _bonobo_archaic_admixture_4K19():
    
    id = "BonoboArchaicAdmixture_4K19"
    description = "Demographic model for bonobos, central and western chimpanzees with admixture from a ghost population"
    long_description = """"""
    populations = [
        _bonobo, 
        _central_chimpanzee, 
        _western_chimpanzee,
        stdpopsim.Population(
            "Ghost", "Putative pan population", sampling_time=None
        ),
    ]
    citations = [_kuhlwilm_et_al]
    
    generation_time = 25
    mutation_rate = 1.2e-8
    
    # Figure 3
    # Supplementary Table S2.3
    # population sizes (diploid Ne)
    N_A = 43566*2 # ancestral population size (Effective size of the ghost before split from the Pan population)
    N_anc_Bon_Chimp = 8378*2 # ancestral population size of the Pan population
    N_anc_CChimp = 12338*2 # ancestral population size of common chimpanzees
    N_anc_Bon = 2920*2 # ancestral population size of bonobos
    N_anc_Cent = 38996*2 # ancestral population size of central chimpanzees
    N_anc_West = 15222*2 # ancestral population size of western chimpanzees
    N_Bon = 20412*2 # population size of bonobos
    N_Cent = 64910*2 # population size of central chimpanzees
    N_West = 15222*2 # population size of western chimpanzees
    N_curr_Bon = 691*2 # current population size of bonobos
    N_curr_Cent = 1042*2 # current population size of central chimpanzees
    N_curr_West = 386*2 # current population size of western chimpanzees
    
    # migration rates
    # migration rates between western and central chimpanzees
    m_West_Cent = 1.211/(2*N_A)
    m_Cent_West = 1.750/(2*N_A)
    # migration rates between bonobos and central chimpanzees
    m_Bon_Cent = 0.062/(2*N_A)
    m_Cent_Bon = 0.089/(2*N_A)
    # migration rates between bonobos and ancestral common chimpanzees
    m_Bon_CChimp = 1.20e-3/(2*N_A)
    m_CChimp_Bon = 2.02e-2/(2*N_A)
    
    admix_prop = 0.11 # admixture proportion from the ghost
    
    # Times (generation)
    T_ghost_split = int(3229000/generation_time)
    T_Bon_split = int(1821000/generation_time)
    T_West_split = int(631000/generation_time)
    T_Bon_mig_stop = int(201000/generation_time)
    T_West_mig_stop = int(195000/generation_time)
    T_Bon_resize = int(388000/generation_time)
    T_Cent_resize = int(547000/generation_time)
    T_West_resize = int(207000/generation_time)
    T_ghost_admix = int(1209000/generation_time)
    
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
            initial_size=N_curr_West,
            metadata=populations[2].asdict()
        ),
        # the ghost
        msprime.PopulationConfiguration(
            initial_size=N_A, metadata=populations[3].asdict()
        ),
    ]
    
    migration_matrix=[
        # bonobo, central, western, ghost
        [0, 0, 0, 0], # bonobo
        [0, 0, 0, 0], # central
        [0, 0, 0, 0], # western
        [0, 0, 0, 0], # ghost
    ]
    
    demographic_events=[
        # migration between western and central chimpanzees
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_Cent_West, matrix_index=(1, 2)
        ),
        msprime.MigrationRateChange(
            time=T_West_mig_stop, rate=m_West_Cent, matrix_index=(2, 1)
        ),
        # migration between bonobos and central chimpanzees
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Bon_Cent, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_Bon_mig_stop, rate=m_Cent_Bon, matrix_index=(1, 0)
        ),
        # admixture from the ghost into bonobos
        msprime.MassMigration(
            time=T_ghost_admix,
            proportion=admix_prop,
            source=3,
            destination=0,
        ),
        # merge western into central chimpanzees
        msprime.MassMigration(
            time=T_West_split,
            proportion=1,
            source=2,
            destination=1,
        ),
        msprime.MigrationRateChange(
            time=T_West_split, rate=0
        ),
        msprime.MigrationRateChange(
            time=T_West_split, rate=m_Bon_CChimp, matrix_index=(0, 1)
        ),
        msprime.MigrationRateChange(
            time=T_West_split, rate=m_CChimp_Bon, matrix_index=(1, 0)
        ),
        msprime.PopulationParametersChange(
            time=T_West_split, initial_size=N_anc_CChimp, population_id=1
        ),
        # merge common chimpanzees and bonobos
        msprime.MassMigration(
            time=T_Bon_split,
            proportion=1,
            source=1,
            destination=0,
        ),
        msprime.MigrationRateChange(
            time=T_Bon_split, rate=0
        ),
        msprime.PopulationParametersChange(
            time=T_Bon_split, initial_size=N_anc_Bon_Chimp, population_id=0
        ),
        # merge the Pan population and the ghost
        msprime.MassMigration(
            time=T_ghost_split,
            proportion=1,
            source=0,
            destination=3,
        ),
        msprime.PopulationParametersChange(
            time=T_ghost_split, initial_size=N_A, population_id=3
        ),
    ]
    
    return stdpopsim.DemographicModel(
        id=id, 
        description=description,
        long_description=long_description,
        citations=citations,
        generation_time=generation_time,
        mutation_rate=mutation_rate,
        populations=populations,
        population_configurations=population_configurations,
        migration_matrix=migration_matrix,
        demographic_events=demographic_events,
    )

_species.add_demographic_model(_bonobo_archaic_admixture_4K19())
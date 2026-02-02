from init import *
maestro_tags = 'ttlhg4.fpga.logall'
PROJ_DEFS = proj_init.generate_fields(maestro_tags)
perspec_files = [PROJ_DEFS['_PRELOAD'], PROJ_DEFS['_PRELOAD_GNA'] , '/perspec/models/ace/standalone/ace.psf'  , '/perspec/models/gna/gna_inACE_pkg.psf' , '/perspec/scripts/utils/perspec_parameter_constraint_output.sln', '/perspec/scripts/utils/perspec_scenario_execution_sequence.sln']
perspec_args = PROJ_DEFS['_DEF']


dspmem_50_1 = {'job': 'dspmem_50_1', 'type': 'perspec_maestro', 'feature_list' :['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': 91230, 'perspec_seed_count': 1, 'maestro_seed_count': 50}]}


TESTLINES_TO_BE_EXECUTE = [dspmem_50_1, ]
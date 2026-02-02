from init import *
maestro_tags = 'ttlhg4.fpga.logall'
PROJ_DEFS = proj_init.generate_fields(maestro_tags)
#perspec_files = [PROJ_DEFS['_PRELOAD'], '/perspec/models/ace/standalone/ace.psf' , PROJ_DEFS['_PRELOAD_GNA'] , '/perspec/models/gna/gna_inACE_pkg.psf']
perspec_files = [PROJ_DEFS['_PRELOAD'], PROJ_DEFS['_PRELOAD_GNA'] , '/perspec/models/ace/standalone/ace.psf'  , '/perspec/models/gna/gna_inACE_pkg.psf' , '/perspec/scripts/utils/perspec_parameter_constraint_output.sln', '/perspec/scripts/utils/perspec_scenario_execution_sequence.sln']
#perspec_files = [PROJ_DEFS['_PRELOAD'], '/perspec/models/ace/standalone/ace.psf']
#perspec_files = [PROJ_DEFS['_PRELOAD'], '/perspec/models/ace/standalone/ace.psf' ,  'perspec/scripts/utils/perspec_parameter_constraint_output.sln', '/perspec/scripts/utils/perspec_scenario_execution_sequence.sln']
perspec_args = PROJ_DEFS['_DEF']

#UAOL generate command
perspec_files_uaol = [PROJ_DEFS['_PRELOAD'], '/perspec/models/uaol/standalone/uaol.psf', '/perspec/scripts/utils/perspec_parameter_constraint_output.sln', '/perspec/scripts/utils/perspec_scenario_execution_sequence.sln']
perspec_args_uaol = r' -define PORT_TABLE_NAME \"UsbTestcard\"' + r' -define CONFIG_FILE=\"/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.csv\"' + r' -define PORT_CONFIG_FILE=\"/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.csv\"'
perspec_args_uaol_conc = r' -max_actions 50 -max_requested_actions 50 -solver_timeout 1000 -define PORT_TABLE_NAME \"UsbTestcard\"' + r' -define CONFIG_FILE=\"/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.csv\"' + r' -define PORT_CONFIG_FILE=\"/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.csv\"'

#plat = '/nfs/png/disks/png_coesv_disk001/Platform_Bling/PGVICEWINCIcommon.bl'	#user need to specify the path to use own platform
perspec_seed_count = 1	#Seeds Iteration set in PVIM will overwrite this.
perspec_seed_count2 = 1
maestro_seed_count = 50

import random
perspec_seed    = random.randint(0,100000)
perspec_seed_0  = random.randint(0,100000)
perspec_seed_1 	= random.randint(0,100000)
perspec_seed_2 	= random.randint(0,100000)
perspec_seed_3 	= random.randint(0,100000)
perspec_seed_4 	= random.randint(0,100000)
perspec_seed_5 	= random.randint(0,100000)
perspec_seed_6 	= random.randint(0,100000)
perspec_seed_7 	= random.randint(0,100000)
perspec_seed_8 	= random.randint(0,100000)
perspec_seed_9 	= random.randint(0,100000)
perspec_seed_10 = random.randint(0,100000)
perspec_seed_11 = random.randint(0,100000)
perspec_seed_12 = random.randint(0,100000)
perspec_seed_13 = random.randint(0,100000)
perspec_seed_14 = random.randint(0,100000)
perspec_seed_15 = random.randint(0,100000)
perspec_seed_16 = random.randint(0,100000)
perspec_seed_17 = random.randint(0,100000)
perspec_seed_18 = random.randint(0,100000)
perspec_seed_19 = random.randint(0,100000)
perspec_seed_20 = random.randint(0,100000)
perspec_seed_21 = random.randint(0,100000)
perspec_seed_22 = random.randint(0,100000)
perspec_seed_23 = random.randint(0,100000)
perspec_seed_24 = random.randint(0,100000)
perspec_seed_25 = random.randint(0,100000)
perspec_seed_26 = random.randint(0,100000)
perspec_seed_27 = random.randint(0,100000)
perspec_seed_28 = random.randint(0,100000)
perspec_seed_29 = random.randint(0,100000)
perspec_seed_30 = random.randint(0,100000)
perspec_seed_31 = random.randint(0,100000)
perspec_seed_32 = random.randint(0,100000)

# maestro seed
maestro_seed    = random.randint(0,100000)
maestro_seed_0  = random.randint(0,100000)
maestro_seed_1	= random.randint(0,100000)
maestro_seed_2	= random.randint(0,100000)
maestro_seed_3	= random.randint(0,100000)
maestro_seed_4	= random.randint(0,100000)
maestro_seed_5	= random.randint(0,100000)
maestro_seed_6	= random.randint(0,100000)
maestro_seed_7	= random.randint(0,100000)
maestro_seed_8	= random.randint(0,100000)
maestro_seed_9	= random.randint(0,100000)
maestro_seed_10	= random.randint(0,100000)
maestro_seed_11	= random.randint(0,100000)
maestro_seed_12	= random.randint(0,100000)
maestro_seed_13	= random.randint(0,100000)
maestro_seed_14	= random.randint(0,100000)
maestro_seed_15	= random.randint(0,100000)
maestro_seed_16	= random.randint(0,100000)
maestro_seed_17	= random.randint(0,100000)
maestro_seed_18	= random.randint(0,100000)
maestro_seed_19	= random.randint(0,100000)
maestro_seed_20	= random.randint(0,100000)
maestro_seed_21	= random.randint(0,100000)
maestro_seed_22	= random.randint(0,100000)
maestro_seed_23	= random.randint(0,100000)
maestro_seed_24	= random.randint(0,100000)
maestro_seed_25	= random.randint(0,100000)
maestro_seed_26	= random.randint(0,100000)
maestro_seed_27	= random.randint(0,100000)
maestro_seed_28	= random.randint(0,100000)
maestro_seed_29	= random.randint(0,100000)
maestro_seed_30	= random.randint(0,100000)
maestro_seed_31	= random.randint(0,100000)
maestro_seed_32	= random.randint(0,100000)

plat = '/nfs/png/disks/png_coesv_disk001/Platform_Bling/PGVICEWINCIcommon.bl'
plat_uaol = '/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.bl'
plat_uaol_csv = '/nfs/png/disks/png_coesv_disk001/users/mohdjail/Platform_bling/nvlh/PGVICEWINCI605_nvlh_24ww01/Platform.csv'


### 11 DMIC (T=185)############################################################################################################
dmic_rand_ldma_0  = {'job': 'dmic_rand_ldma_0', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_0 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_1  = {'job': 'dmic_rand_ldma_1', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_2  = {'job': 'dmic_rand_ldma_2', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_3  = {'job': 'dmic_rand_ldma_3', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_4  = {'job': 'dmic_rand_ldma_4', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_5  = {'job': 'dmic_rand_ldma_5', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_5 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_6  = {'job': 'dmic_rand_ldma_6', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_6 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_7  = {'job': 'dmic_rand_ldma_7', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_7 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_8  = {'job': 'dmic_rand_ldma_8', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_8 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_9  = {'job': 'dmic_rand_ldma_9', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_9 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_10 = {'job': 'dmic_rand_ldma_10', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_10, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_11 = {'job': 'dmic_rand_ldma_11', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_11, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_12 = {'job': 'dmic_rand_ldma_12', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_12, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_13 = {'job': 'dmic_rand_ldma_13', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_13, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_14 = {'job': 'dmic_rand_ldma_14', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_14, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_ldma_15 = {'job': 'dmic_rand_ldma_15', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_15, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}


hq_mode_Mic3840Khz_Dec_A48Khz_B16Khz_19Mhz = {'job': 'hq_mode_Mic3840Khz_Dec_A48Khz_B16Khz_19Mhz', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/hq_mode_Mic3840Khz_Dec_A48Khz_B16Khz_19Mhz.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
lpal_Mic768Khz_Dec_A48Khz_B16Khz_19Mhz = {'job': 'lpal_Mic768Khz_Dec_A48Khz_B16Khz_19Mhz', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/lpal_Mic768Khz_Dec_A48Khz_B16Khz_19Mhz.sln','maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
normal_Mic2400Khz_Dec_A32Khz_B16Khz_19Mhz = {'job': 'normal_Mic2400Khz_Dec_A32Khz_B16Khz_19Mhz', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/normal_Mic2400Khz_Dec_A32Khz_B16Khz_19Mhz.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
normal_Mic2400Khz_Dec_A48Khz_B16Khz_19Mhz = {'job': 'normal_Mic2400Khz_Dec_A48Khz_B16Khz_19Mhz', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/normal_Mic2400Khz_Dec_A48Khz_B16Khz_19Mhz.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ultrasound_Mic3840Khz_Dec_A96Khz_B16Khz_19Mhz = {'job': 'ultrasound_Mic3840Khz_Dec_A96Khz_B16Khz_19Mhz', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/ultrasound_Mic3840Khz_Dec_A96Khz_B16Khz_19Mhz.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_clockedge_invert_mode = {'job': 'dmic_clockedge_invert_mode', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_clockedge_invert_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_clockedge_nonInvert_mode = {'job': 'dmic_clockedge_nonInvert_mode', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_clockedge_nonInvert_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_mono_mode = {'job': 'dmic_mono_mode', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_mono_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_stereo_mode = {'job': 'dmic_stereo_mode', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_stereo_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_wov_ptl_dmic_0 = {'job': 'dmic_wov_ptl_dmic_0', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_dmic_1 = {'job': 'dmic_wov_ptl_dmic_1', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_pio_mode = {'job': 'dmic_pio_mode', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_pio_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_pio_mode_0 = {'job': 'dmic_pio_mode_0', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_pio_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_polarity = {'job': 'dmic_polarity', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_polarity.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_ipm = {'job': 'dmic_ipm', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_ipm.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_dpdma_wov_ptl = {'job': 'dmic_dpdma_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_dpdma_wov_ptl_0 = {'job': 'dmic_dpdma_wov_ptl_0', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_dpdma_wov_ptl_1 = {'job': 'dmic_dpdma_wov_ptl_1', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

#scs=1, OF=24bit
dmic_of24_scs1 = {'job': 'dmic_of24_scs1', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_of24_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

#coupled mode
dmic_rand_allzero_coupled = {'job': 'dmic_rand_allzero_coupled', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_1 = {'job': 'dmic_rand_allzero_coupled_1', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_2 = {'job': 'dmic_rand_allzero_coupled_2', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_3 = {'job': 'dmic_rand_allzero_coupled_3', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_4 = {'job': 'dmic_rand_allzero_coupled_4', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_5 = {'job': 'dmic_rand_allzero_coupled_5', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_5 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_6 = {'job': 'dmic_rand_allzero_coupled_6', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_6 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_7 = {'job': 'dmic_rand_allzero_coupled_7', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_7 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_8 = {'job': 'dmic_rand_allzero_coupled_8', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_8 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_9 = {'job': 'dmic_rand_allzero_coupled_9', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_9 , 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_10 = {'job': 'dmic_rand_allzero_coupled_10', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_10, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_11 = {'job': 'dmic_rand_allzero_coupled_11', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_11, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_12 = {'job': 'dmic_rand_allzero_coupled_12', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_12, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_13 = {'job': 'dmic_rand_allzero_coupled_13', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_13, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_14 = {'job': 'dmic_rand_allzero_coupled_14', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_14, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_15 = {'job': 'dmic_rand_allzero_coupled_15', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_15, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_16 = {'job': 'dmic_rand_allzero_coupled_16', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_16, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_17 = {'job': 'dmic_rand_allzero_coupled_17', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_17, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_18 = {'job': 'dmic_rand_allzero_coupled_18', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_18, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_19 = {'job': 'dmic_rand_allzero_coupled_19', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_19, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_20 = {'job': 'dmic_rand_allzero_coupled_20', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_20, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_21 = {'job': 'dmic_rand_allzero_coupled_21', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_21, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_22 = {'job': 'dmic_rand_allzero_coupled_22', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_22, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_23 = {'job': 'dmic_rand_allzero_coupled_23', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_23, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_24 = {'job': 'dmic_rand_allzero_coupled_24', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_24, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rand_allzero_coupled_25 = {'job': 'dmic_rand_allzero_coupled_25', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_rand_allzero_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_25, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

#dmic_periodic_sync
dmic_periodic_sync = {'job': 'dmic_periodic_sync', 'type': 'perspec_maestro', 'feature_list': ['dmic'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_periodic_sync.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### () DMA (T=10)############################################################################################################
ace_dpdma_0 = {'job': 'ace_dpdma_0', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_0, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_1 = {'job': 'ace_dpdma_1', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_2 = {'job': 'ace_dpdma_2', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_3 = {'job': 'ace_dpdma_3', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_4 = {'job': 'ace_dpdma_4', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_5 = {'job': 'ace_dpdma_5', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_5, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_6 = {'job': 'ace_dpdma_6', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_6, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_7 = {'job': 'ace_dpdma_7', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_7, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_8 = {'job': 'ace_dpdma_8', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_8, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_9 = {'job': 'ace_dpdma_9', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_9, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_10 = {'job': 'ace_dpdma_10', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_10, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_dpdma_11 = {'job': 'ace_dpdma_11', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dpdma/ace_dpdma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_11, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### (10) DSPMEM 5 Cores (T=10)############################################################################################################
dspmem_hpsram_hpsram = {'job': 'dspmem_hpsram_hpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_hpsram_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_hpsram_lpsram = {'job': 'dspmem_hpsram_lpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_hpsram_lpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_hpsram_l2uncache = {'job': 'dspmem_hpsram_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_hpsram_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_lpsram_lpsram = {'job': 'dspmem_lpsram_lpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_lpsram_lpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_lpsram_hpsram = {'job': 'dspmem_lpsram_hpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_lpsram_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_lpsram_l2uncache = {'job': 'dspmem_lpsram_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_lpsram_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_l2uncache_l2uncache = {'job': 'dspmem_l2uncache_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_l2uncache_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_l2uncache_hpsram = {'job': 'dspmem_l2uncache_hpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_l2uncache_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_l2uncache_lpsram = {'job': 'dspmem_l2uncache_lpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_l2uncache_lpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
# PS: Temporarily only run core 0.
dspmem_dma_ulpsram = {'job': 'dspmem_dma_ulpsram', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dsp2cores/dspmem_dma_ulpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dspmem_50 = {'job': 'dspmem_50', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_0 = {'job': 'dspmem_50_0', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_0,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_1 = {'job': 'dspmem_50_1', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_2 = {'job': 'dspmem_50_2', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_3 = {'job': 'dspmem_50_3', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_4 = {'job': 'dspmem_50_4', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_5 = {'job': 'dspmem_50_5', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_5,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_6 = {'job': 'dspmem_50_6', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_6,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_7 = {'job': 'dspmem_50_7', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_7,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_8 = {'job': 'dspmem_50_8', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_8,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_9 = {'job': 'dspmem_50_9', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_9,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_10 = {'job': 'dspmem_50_10', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_10,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_11 = {'job': 'dspmem_50_11', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_11,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_12 = {'job': 'dspmem_50_12', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_12,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_13 = {'job': 'dspmem_50_13', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_13,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_14 = {'job': 'dspmem_50_14', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_14,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dspmem_50_15 = {'job': 'dspmem_50_15', 'type': 'perspec_maestro', 'feature_list': ['dspmem'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/dsp_all_cores/dspmem_50_imr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_15,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### (1) ADSP (T=1)############################################################################################################
ace_dsp_comm_widget = {'job': 'ace_dsp_comm_widget', 'type': 'perspec_maestro', 'feature_list': ['ADSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dsp_comm_widget.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_micpvc_fmmd1_nonwrap_2   = {'job': 'dmic_micpvc_fmmd1_nonwrap_2', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd1_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_pio_mode_1 = {'job': 'dmic_pio_mode_1', 'type': 'perspec_maestro', 'feature_list': ['ADSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/dmic/dmic_pio_mode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
# PS: Temporarily only run core 0.
### (1) Audio_Memory (T=1)############################################################################################################
ace_audioMem_concurrent_access = {'job': 'ace_audioMem_concurrent_access', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'],     'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_ttl/ace_audioMem_concurrent_access_ttlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_0 = {'job': 'ace_audioMem_concurrent_access_0', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_ttl/ace_audioMem_concurrent_access_ttlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_1 = {'job': 'ace_audioMem_concurrent_access_1', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_ttl/ace_audioMem_concurrent_access_ttlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_2 = {'job': 'ace_audioMem_concurrent_access_2', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_ttl/ace_audioMem_concurrent_access_ttlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

ace_audioMem_concurrent_access_wcl = {'job': 'ace_audioMem_concurrent_access_wcl', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_wcl/ace_audioMem_concurrent_access_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_wcl_0 = {'job': 'ace_audioMem_concurrent_access_wcl_0', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_wcl/ace_audioMem_concurrent_access_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_wcl_1 = {'job': 'ace_audioMem_concurrent_access_wcl_1', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_wcl/ace_audioMem_concurrent_access_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_audioMem_concurrent_access_wcl_2 = {'job': 'ace_audioMem_concurrent_access_wcl_2', 'type': 'perspec_maestro', 'feature_list': ['Audio_Memory'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_wcl/ace_audioMem_concurrent_access_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,  'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### (24) HDA (T=24)############################################################################################################
reset_hda_lpp = {'job': 'reset_hda_lpp', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_lpp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
reset_hda_lpp_0 = {'job': 'reset_hda_lpp_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_lpp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
reset_hda_lpp_1 = {'job': 'reset_hda_lpp_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_lpp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}


spa_whack_hda_lple = {'job': 'spa_whack_hda_lple', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_hda_lple.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_lpp_lnl = {'job': 'hda_lpp_lnl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/hda_lpp_lnl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_lpp_wcl = {'job': 'hda_lpp_wcl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_lpp_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
# hda_lpp_ptl = {'job': 'hda_lpp_ptl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_lpp_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_lpp_ptl = {'job': 'hda_lpp_ptl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/hda_lpp_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_wov_lnl = {'job': 'hda_wov_lnl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_wov_lnl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
# hda_wov_ptl = {'job': 'hda_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_wov_ptl = {'job': 'hda_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/hda_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_fw_icr = {'job': 'hda_fw_icr', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_fw_icr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_ssync_LDMA_input = {'job': 'hda_ssync_LDMA_input', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_ssync_LDMA_input.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_ssync_LDMA_output = {'job': 'hda_ssync_LDMA_output', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_ssync_LDMA_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_streams_with_crst = {'job': 'hda_streams_with_crst', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_streams_with_crst.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_streams_with_crst_1 = {'job': 'hda_streams_with_crst_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_streams_with_crst.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_streams_with_crst_2 = {'job': 'hda_streams_with_crst_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_streams_with_crst.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_streams_with_crst_3 = {'job': 'hda_streams_with_crst_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_streams_with_crst.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_LDMA_input_lple = {'job': 'hda_LDMA_input_lple', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_input_lple.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_lple = {'job': 'hda_LDMA_output_lple', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_lple.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_corb_rirb = {'job': 'hda_coupled_corb_rirb', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_corb_rirb_1 = {'job': 'hda_coupled_corb_rirb_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_corb_rirb_2 = {'job': 'hda_coupled_corb_rirb_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_corb_rirb_3 = {'job': 'hda_coupled_corb_rirb_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_corb_rirb_4 = {'job': 'hda_coupled_corb_rirb_4', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_corb_rirb_5 = {'job': 'hda_coupled_corb_rirb_5', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_rirb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_corb_gt_256 = {'job': 'hda_coupled_corb_gt_256', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_corb_gt_256.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_icr = {'job': 'hda_coupled_icr', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_icr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_10ms_buffering = {'job': 'hda_coupled_10ms_buffering', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_10ms_buffering.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_input_2sdi = {'job': 'hda_coupled_input_2sdi', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_input_2sdi.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_output_inst_0 = {'job': 'hda_coupled_output_inst_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_output_runbit_pause_resume = {'job': 'hda_coupled_output_runbit_pause_resume', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_output_runbit_pause_resume.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_SPIB_input = {'job': 'hda_coupled_SPIB_input', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_SPIB_input.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_SPIB_output = {'job': 'hda_coupled_SPIB_output', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_SPIB_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_SPIB_output_0 = {'job': 'hda_coupled_SPIB_output_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_SPIB_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_SPIB_output_1 = {'job': 'hda_coupled_SPIB_output_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_SPIB_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_SPIB_output_2 = {'job': 'hda_coupled_SPIB_output_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_SPIB_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_rand = {'job': 'hda_coupled_rand', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_0 = {'job': 'hda_coupled_rand_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_1 = {'job': 'hda_coupled_rand_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_2 = {'job': 'hda_coupled_rand_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_3 = {'job': 'hda_coupled_rand_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_4 = {'job': 'hda_coupled_rand_4', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_5 = {'job': 'hda_coupled_rand_5', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_6 = {'job': 'hda_coupled_rand_6', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_7 = {'job': 'hda_coupled_rand_7', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_7, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_8 = {'job': 'hda_coupled_rand_8', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_8, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_rand_9 = {'job': 'hda_coupled_rand_9', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_9, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_LDMA_bandwidth_sdi_464 = {'job': 'hda_LDMA_bandwidth_sdi_464', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_bandwidth_sdi_464.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_bandwidth_sdo_960 = {'job': 'hda_LDMA_bandwidth_sdo_960', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_bandwidth_sdo_960.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_LDMA_input_inst_0 = {'job': 'hda_LDMA_input_inst_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_input_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_input_inst_0 = {'job': 'hda_HDMA_input_inst_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_input_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_LDMA_output_inst_0 = {'job': 'hda_LDMA_output_inst_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_0 = {'job': 'hda_LDMA_output_inst_0_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_1 = {'job': 'hda_LDMA_output_inst_0_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_2 = {'job': 'hda_LDMA_output_inst_0_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_3 = {'job': 'hda_LDMA_output_inst_0_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_4 = {'job': 'hda_LDMA_output_inst_0_4', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_LDMA_output_inst_0_5 = {'job': 'hda_LDMA_output_inst_0_5', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_LDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_HDMA_output_inst_0 = {'job': 'hda_HDMA_output_inst_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_0 = {'job': 'hda_HDMA_output_inst_0_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_0 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_1 = {'job': 'hda_HDMA_output_inst_0_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_1 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_2 = {'job': 'hda_HDMA_output_inst_0_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_2 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_3 = {'job': 'hda_HDMA_output_inst_0_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_3 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_4 = {'job': 'hda_HDMA_output_inst_0_4', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_4 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_5 = {'job': 'hda_HDMA_output_inst_0_5', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_5 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_6 = {'job': 'hda_HDMA_output_inst_0_6', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_6 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_7 = {'job': 'hda_HDMA_output_inst_0_7', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_7 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_8 = {'job': 'hda_HDMA_output_inst_0_8', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_8 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_9 = {'job': 'hda_HDMA_output_inst_0_9', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files,   'perspec_seed': perspec_seed_9 , 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_10 = {'job': 'hda_HDMA_output_inst_0_10', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_10, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_output_inst_0_11 = {'job': 'hda_HDMA_output_inst_0_11', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_output_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_11, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_HDMA_SPIB_output = {'job': 'hda_HDMA_SPIB_output', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_SPIB_output.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_HDMA_SPIB_input = {'job': 'hda_HDMA_SPIB_input', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_HDMA_SPIB_input.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_decoupled_rand = {'job': 'hda_decoupled_rand', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_decoupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_decoupled_rand_1 = {'job': 'hda_decoupled_rand_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_decoupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_decoupled_rand_2 = {'job': 'hda_decoupled_rand_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_decoupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_decoupled_rand_3 = {'job': 'hda_decoupled_rand_3', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_decoupled_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_flush_0 = {'job': 'hda_coupled_flush_0', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_flush.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_flush_1 = {'job': 'hda_coupled_flush_1', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_flush.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
hda_coupled_flush_2 = {'job': 'hda_coupled_flush_2', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_flush.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

hda_coupled_rintcnt_focus = {'job': 'hda_coupled_rintcnt_focus', 'type': 'perspec_maestro', 'feature_list': ['hda_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/hda/hda_coupled_rintcnt_focus.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### (28) IDISP Coupled (T=156)############################################################################################################
Idisp_cmdrsp = {'job': 'Idisp_cmd_rsp', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'],'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_cmdrsp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_BPS_16 = {'job': 'Idisp_coupled_BPS_16', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_BPS_16.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_BPS_24 = {'job': 'Idisp_coupled_BPS_24', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_BPS_24.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_BPS_32 = {'job': 'Idisp_coupled_BPS_32', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_BPS_32.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_32k = {'job': 'Idisp_coupled_SR_32k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_32k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_44k = {'job': 'Idisp_coupled_SR_44k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_44k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_48k = {'job': 'Idisp_coupled_SR_48k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_48k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_88k = {'job': 'Idisp_coupled_SR_88k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_88k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_96k = {'job': 'Idisp_coupled_SR_96k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_96k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_176k = {'job': 'Idisp_coupled_SR_176k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_176k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_SR_192k = {'job': 'Idisp_coupled_SR_192k', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_SR_192k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc1 = {'job': 'Idisp_coupled_cc1', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc2 = {'job': 'Idisp_coupled_cc2', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc3 = {'job': 'Idisp_coupled_cc3', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc3.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc4 = {'job': 'Idisp_coupled_cc4', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc4.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc5 = {'job': 'Idisp_coupled_cc5', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc5.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc6 = {'job': 'Idisp_coupled_cc6', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc6.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc7 = {'job': 'Idisp_coupled_cc7', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc7.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_cc8 = {'job': 'Idisp_coupled_cc8', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_cc8.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

Idisp_coupled_out_inst_0 = {'job': 'Idisp_coupled_out_inst_0', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_0_0 = {'job': 'Idisp_coupled_out_inst_0_0', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_0_1 = {'job': 'Idisp_coupled_out_inst_0_1', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_0_2 = {'job': 'Idisp_coupled_out_inst_0_2', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_0_3 = {'job': 'Idisp_coupled_out_inst_0_3', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

Idisp_coupled_out_inst_1 = {'job': 'Idisp_coupled_out_inst_1', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_2 = {'job': 'Idisp_coupled_out_inst_2', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_3 = {'job': 'Idisp_coupled_out_inst_3', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_3.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_4 = {'job': 'Idisp_coupled_out_inst_4', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_4.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_5 = {'job': 'Idisp_coupled_out_inst_5', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_5.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_6 = {'job': 'Idisp_coupled_out_inst_6', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_6.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_7 = {'job': 'Idisp_coupled_out_inst_7', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_7.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_coupled_out_inst_8 = {'job': 'Idisp_coupled_out_inst_8', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_inst_8.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

Idisp_coupled_out_rand = {'job': 'Idisp_coupled_out_rand', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_coupled_out_rand.sln ', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_icr = {'job': 'Idisp_icr', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_icr.sln ', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_corb_rirb = {'job': 'Idisp_corb_rirb', 'type': 'perspec_maestro', 'feature_list': ['idisp_coupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_corb_rirb.sln ', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### (27) IDISP Decoupled (T=184)############################################################################################################
Idisp_decoupled_BPS_16 = {'job': 'Idisp_decoupled_BPS_16', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_BPS_16.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_BPS_24 = {'job': 'Idisp_decoupled_BPS_24', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_BPS_24.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_BPS_32 = {'job': 'Idisp_decoupled_BPS_32', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_BPS_32.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_32k = {'job': 'Idisp_decoupled_SR_32k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_32k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_44k = {'job': 'Idisp_decoupled_SR_44k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_44k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_48k = {'job': 'Idisp_decoupled_SR_48k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_48k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_88k = {'job': 'Idisp_decoupled_SR_88k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_88k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_96k = {'job': 'Idisp_decoupled_SR_96k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_96k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_176k = {'job': 'Idisp_decoupled_SR_176k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_176k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_SR_192k = {'job': 'Idisp_decoupled_SR_192k', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_SR_192k.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc1 = {'job': 'Idisp_decoupled_cc1', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc2 = {'job': 'Idisp_decoupled_cc2', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc3 = {'job': 'Idisp_decoupled_cc3', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc3.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc4 = {'job': 'Idisp_decoupled_cc4', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc4.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc5 = {'job': 'Idisp_decoupled_cc5', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc5.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc6 = {'job': 'Idisp_decoupled_cc6', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc6.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc7 = {'job': 'Idisp_decoupled_cc7', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc7.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_cc8 = {'job': 'Idisp_decoupled_cc8', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_cc8.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_0 = {'job': 'Idisp_decoupled_out_inst_0', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_1 = {'job': 'Idisp_decoupled_out_inst_1', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_2 = {'job': 'Idisp_decoupled_out_inst_2', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_3 = {'job': 'Idisp_decoupled_out_inst_3', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_3.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_4 = {'job': 'Idisp_decoupled_out_inst_4', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_4.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_5 = {'job': 'Idisp_decoupled_out_inst_5', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_5.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_6 = {'job': 'Idisp_decoupled_out_inst_6', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_6.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_7 = {'job': 'Idisp_decoupled_out_inst_7', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_7.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
Idisp_decoupled_out_inst_8 = {'job': 'Idisp_decoupled_out_inst_8', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_out_inst_8.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

Idisp_decoupled_bandwidth_sdo = {'job': 'Idisp_decoupled_bandwidth_sdo', 'type': 'perspec_maestro', 'feature_list': ['idisp_decoupled'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/idisp/Idisp_decoupled_bandwidth_sdo.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}



### LNL SNDW (T=4) ############################################################################################################
ace_sndw_loopback = {'job': 'ace_sndw_loopback', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_multilane_loopback = {'job': 'ace_sndw_multilane_loopback', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_multilane_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_in_stream = {'job': 'ace_sndw_in_stream', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_in_stream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_out_stream = {'job': 'ace_sndw_out_stream', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_out_stream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


### PTL SNDW (T= 59) ############################################################################################################
ace_sndw_loopback_rand = {'job': 'ace_sndw_loopback_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_0  = {'job': 'ace_sndw_loopback_rand_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_0 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_1  = {'job': 'ace_sndw_loopback_rand_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_1 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_2  = {'job': 'ace_sndw_loopback_rand_2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_2 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_3  = {'job': 'ace_sndw_loopback_rand_3', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_3 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_4  = {'job': 'ace_sndw_loopback_rand_4', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_4 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_5  = {'job': 'ace_sndw_loopback_rand_5', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_5 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_6  = {'job': 'ace_sndw_loopback_rand_6', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_6 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_7  = {'job': 'ace_sndw_loopback_rand_7', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_7 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_8  = {'job': 'ace_sndw_loopback_rand_8', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_8 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_9  = {'job': 'ace_sndw_loopback_rand_9', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':  perspec_seed_9 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_10 = {'job': 'ace_sndw_loopback_rand_10', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_10, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_11 = {'job': 'ace_sndw_loopback_rand_11', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_11, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_12 = {'job': 'ace_sndw_loopback_rand_12', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_12, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_13 = {'job': 'ace_sndw_loopback_rand_13', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_13, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_14 = {'job': 'ace_sndw_loopback_rand_14', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_14, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_15 = {'job': 'ace_sndw_loopback_rand_15', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_15, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_16 = {'job': 'ace_sndw_loopback_rand_16', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_16, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_17 = {'job': 'ace_sndw_loopback_rand_17', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_17, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_18 = {'job': 'ace_sndw_loopback_rand_18', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_18, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_19 = {'job': 'ace_sndw_loopback_rand_19', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_19, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_20 = {'job': 'ace_sndw_loopback_rand_20', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_20, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_21 = {'job': 'ace_sndw_loopback_rand_21', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_21, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_22 = {'job': 'ace_sndw_loopback_rand_22', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_22, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_23 = {'job': 'ace_sndw_loopback_rand_23', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_23, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_24 = {'job': 'ace_sndw_loopback_rand_24', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_24, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_25 = {'job': 'ace_sndw_loopback_rand_25', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_25, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_26 = {'job': 'ace_sndw_loopback_rand_26', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_26, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_27 = {'job': 'ace_sndw_loopback_rand_27', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_27, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_28 = {'job': 'ace_sndw_loopback_rand_28', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_28, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_29 = {'job': 'ace_sndw_loopback_rand_29', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_29, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_30 = {'job': 'ace_sndw_loopback_rand_30', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_30, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_31 = {'job': 'ace_sndw_loopback_rand_31', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_31, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_rand_32 = {'job': 'ace_sndw_loopback_rand_32', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_32, 'maestro_seed_count': maestro_seed_count}]}

ace_sndw_multilane_loopback_rand = {'job': 'ace_sndw_multilane_loopback_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_multilane_loopback_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream = {'job': 'lb_stream', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_rand = {'job': 'lb_stream_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_pause = {'job': 'lb_stream_pause', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_pause.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_stop = {'job': 'lb_stream_stop', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_stop.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_tts_host = {'job': 'lb_stream_tts_host', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_tts_host.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_2_master = {'job': 'lb_stream_2_master', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_2_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_2_master_chain = {'job': 'lb_stream_2_master_chain', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_2_master_chain.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_2_master_chain_coupled = {'job': 'lb_stream_2_master_chain_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_2_master_chain_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_2_master_chain_mix = {'job': 'lb_stream_2_master_chain_mix', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_2_master_chain_mix.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_2_master_chain_mix_coupled = {'job': 'lb_stream_2_master_chain_mix_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_2_master_chain_mix_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_4_lane = {'job': 'lb_stream_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_maxBw = {'job': 'lb_stream_4_lane_maxBw', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_maxBw.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_4_lane_rand = {'job': 'lb_stream_4_lane_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_0 = {'job': 'lb_stream_4_lane_rand_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_0 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_1 = {'job': 'lb_stream_4_lane_rand_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_1 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_2 = {'job': 'lb_stream_4_lane_rand_2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_2 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_3 = {'job': 'lb_stream_4_lane_rand_3', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_3 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_4 = {'job': 'lb_stream_4_lane_rand_4', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_4 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_5 = {'job': 'lb_stream_4_lane_rand_5', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_5 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_6 = {'job': 'lb_stream_4_lane_rand_6', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_6 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_7 = {'job': 'lb_stream_4_lane_rand_7', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_7 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_8 = {'job': 'lb_stream_4_lane_rand_8', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_8 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_9 = {'job': 'lb_stream_4_lane_rand_9', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed':   perspec_seed_9 , 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_10 = {'job': 'lb_stream_4_lane_rand_10', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_10, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_11 = {'job': 'lb_stream_4_lane_rand_11', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_11, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_12 = {'job': 'lb_stream_4_lane_rand_12', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_12, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_13 = {'job': 'lb_stream_4_lane_rand_13', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_13, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_lane_rand_14 = {'job': 'lb_stream_4_lane_rand_14', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_14, 'maestro_seed_count': maestro_seed_count}]}

ace_sndw_loopback_multilane_rand = {'job': 'ace_sndw_loopback_multilane_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_0 = {'job': 'ace_sndw_loopback_multilane_rand_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_0 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_1 = {'job': 'ace_sndw_loopback_multilane_rand_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_1 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_2 = {'job': 'ace_sndw_loopback_multilane_rand_2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_2 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_3 = {'job': 'ace_sndw_loopback_multilane_rand_3', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_3 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_4 = {'job': 'ace_sndw_loopback_multilane_rand_4', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_4 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_5 = {'job': 'ace_sndw_loopback_multilane_rand_5', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_5 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_6 = {'job': 'ace_sndw_loopback_multilane_rand_6', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_6 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_7 = {'job': 'ace_sndw_loopback_multilane_rand_7', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_7 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_8 = {'job': 'ace_sndw_loopback_multilane_rand_8', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_8 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_9 = {'job': 'ace_sndw_loopback_multilane_rand_9', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count':   perspec_seed_count, 'perspec_seed': perspec_seed_9 , 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_10 = {'job': 'ace_sndw_loopback_multilane_rand_10', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_10, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_11 = {'job': 'ace_sndw_loopback_multilane_rand_11', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_11, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_12 = {'job': 'ace_sndw_loopback_multilane_rand_12', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_12, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_13 = {'job': 'ace_sndw_loopback_multilane_rand_13', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_13, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_14 = {'job': 'ace_sndw_loopback_multilane_rand_14', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_14, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_multilane_rand_15 = {'job': 'ace_sndw_loopback_multilane_rand_15', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/ace_sndw_loopback_multilane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_14, 'maestro_seed_count': maestro_seed_count}]}


lb_stream_ac_timing_rand = {'job': 'lb_stream_ac_timing_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_4_master = {'job': 'lb_stream_4_master', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_master_1 = {'job': 'lb_stream_4_master_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_master_chain = {'job': 'lb_stream_4_master_chain', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master_chain.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_master_coupled = {'job': 'lb_stream_4_master_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_aggr_nonaggr_conc = {'job': 'lb_stream_aggr_nonaggr_conc', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_aggr_nonaggr_conc.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_coupled = {'job': 'lb_stream_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_coupled_4_lane = {'job': 'lb_stream_coupled_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_coupled_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_coupled_4_master_rand = {'job': 'lb_stream_coupled_4_master_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_coupled_4_master_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_4_master = {'job': 'lb_stream_4_master', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_master_0 = {'job': 'lb_stream_4_master_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_4_master_1 = {'job': 'lb_stream_4_master_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_master.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


lb_stream_external_clds_17clk_2400 = {'job': 'lb_stream_external_clds_17clk_2400', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_external_clds_17clk_2400.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_external_clds_3clk_default = {'job': 'lb_stream_external_clds_3clk_default', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_external_clds_3clk_default.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_external_clds_3clk_default_nagetive = {'job': 'lb_stream_external_clds_3clk_default_nagetive', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_external_clds_3clk_default_nagetive.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_external_clds_4clk_9600 = {'job': 'lb_stream_external_clds_4clk_9600', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_external_clds_4clk_9600.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_external_clds_8clk_9600 = {'job': 'lb_stream_external_clds_8clk_9600', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_external_clds_8clk_9600.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_internal_clds_17clk_2400 = {'job': 'lb_stream_internal_clds_17clk_2400', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_internal_clds_17clk_2400.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_internal_clds_3clk_default = {'job': 'lb_stream_internal_clds_3clk_default', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_internal_clds_3clk_default.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_internal_clds_4clk_9600 = {'job': 'lb_stream_internal_clds_4clk_9600', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_internal_clds_4clk_9600.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_internal_clds_8clk_9600 = {'job': 'lb_stream_internal_clds_8clk_9600', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_internal_clds_8clk_9600.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


out_stream = {'job': 'out_stream', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

out_stream_2_slave = {'job': 'out_stream_2_slave', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_2_slave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_2_slave_0 = {'job': 'out_stream_2_slave_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_2_slave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_2_slave_1 = {'job': 'out_stream_2_slave_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_2_slave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

out_stream_4_lane = {'job': 'out_stream_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_4_lane_icr = {'job': 'out_stream_4_lane_icr', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_4_lane_icr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_4_lane_rand = {'job': 'out_stream_4_lane_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_coupled = {'job': 'out_stream_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_coupled_4_lane = {'job': 'out_stream_coupled_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_coupled_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_icr = {'job': 'out_stream_icr', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_icr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_rand = {'job': 'out_stream_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

out_stream_ac_timing_rand	= {'job': 'out_stream_ac_timing_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_ac_timing_rand_0 = {'job': 'out_stream_ac_timing_rand_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_ac_timing_rand_1 = {'job': 'out_stream_ac_timing_rand_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_ac_timing_rand_2 = {'job': 'out_stream_ac_timing_rand_2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_ac_timing_rand_3 = {'job': 'out_stream_ac_timing_rand_3', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
out_stream_ac_timing_rand_4 = {'job': 'out_stream_ac_timing_rand_4', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/out_stream_ac_timing_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


in_stream = {'job': 'in_stream', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_4_lane = {'job': 'in_stream_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_4_lane_rand = {'job': 'in_stream_4_lane_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_4_lane_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_coupled = {'job': 'in_stream_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_coupled_4_lane = {'job': 'in_stream_coupled_4_lane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_coupled_4_lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_icr = {'job': 'in_stream_icr', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_icr.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
in_stream_rand = {'job': 'in_stream_rand', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/in_stream_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count2, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

sndw_scenarios_base = {'job': 'sndw_scenarios_base', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_scenarios_base.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_scenarios_lib = {'job': 'sndw_scenarios_lib', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_scenarios_lib.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

ace_sndw_bptin = {'job': 'ace_sndw_bptin', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_bptin.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_bptout = {'job': 'ace_sndw_bptout', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_bptout.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_loopback_asynchronous = {'job': 'ace_sndw_loopback_asynchronous', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_loopback_asynchronous.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_dsp_interrupt = {'job': 'ace_sndw_dsp_interrupt', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_dsp_interrupt.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_dsp_interrupt_0 = {'job': 'ace_sndw_dsp_interrupt_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_dsp_interrupt.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_0, 'maestro_seed_count': maestro_seed_count}]}
ace_sndw_dsp_interrupt_1 = {'job': 'ace_sndw_dsp_interrupt_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/lnl/ace_sndw_dsp_interrupt.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_1, 'maestro_seed_count': maestro_seed_count}]}
lb_stream_tx_rx_controlled = {'job': 'lb_stream_tx_rx_controlled', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_tx_rx_controlled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

lb_stream_4_lane_multi_master_conc = {'job': 'lb_stream_4_lane_multi_master_conc', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/lb_stream_4_lane_multi_master_conc.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


###SNDW nvlh (sndw/ptl/nvlh_ondie/) ### ############################################################################################################

#sndw_multimaster_multilane = {'job': 'sndw_multimaster_multilane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_multilane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#sndw_multimaster_singlelane = {'job': 'sndw_multimaster_singlelane', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#sndw_multimaster_singlelane_0 = {'job': 'sndw_multimaster_singlelane_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#sndw_multimaster_singlelane_1 = {'job': 'sndw_multimaster_singlelane_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

sndw_multimaster_multilane    = {'job': 'sndw_multimaster_multilane', 'type': 'perspec_maestro', 'feature_list': ['sndw'],    'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_multilane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_multimaster_singlelane   = {'job': 'sndw_multimaster_singlelane', 'type': 'perspec_maestro', 'feature_list': ['sndw'],   'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_multimaster_singlelane_0 = {'job': 'sndw_multimaster_singlelane_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_0, 'maestro_seed_count': maestro_seed_count}]}
sndw_multimaster_singlelane_1 = {'job': 'sndw_multimaster_singlelane_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_multimaster_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_1, 'maestro_seed_count': maestro_seed_count}]}




### SNDW IDISP (T= 8) ############################################################################################################
sndw_idisplay_codec1_4lane = {'job': 'sndw_idisplay_codec1_4lane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_4lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_codec1_4lane_coupled = {'job': 'sndw_idisplay_codec1_4lane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_4lane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_codec1_4lane_sampleSize32_coupled = {'job': 'sndw_idisplay_codec1_4lane_sampleSize32_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_4lane_sampleSize32_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

sndw_idisplay_codec2_1lane_sampleSize32_coupled = {'job': 'sndw_idisplay_codec2_1lane_sampleSize32_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane_sampleSize32_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

sndw_idisplay_codec2_1lane_sampleSize32 = {'job': 'sndw_idisplay_codec2_1lane_sampleSize32', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane_sampleSize32.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

#reset_coupled_sndw_idisp_codec1 = {'job': 'reset_coupled_sndw_idisp_codec1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#reset_coupled_sndw_idisp_codec1_0 = {'job': 'reset_coupled_sndw_idisp_codec1_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_0, 'maestro_seed_count': maestro_seed_count}]}
#reset_coupled_sndw_idisp_codec1_1 = {'job': 'reset_coupled_sndw_idisp_codec1_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_1, 'maestro_seed_count': maestro_seed_count}]}
#reset_coupled_sndw_idisp_codec2 = {'job': 'reset_coupled_sndw_idisp_codec2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#reset_sndw_idisp_codec1 = {'job': 'reset_sndw_idisp_codec1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#reset_sndw_idisp_codec1_0 = {'job': 'reset_sndw_idisp_codec1_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#reset_sndw_idisp_codec1_1 = {'job': 'reset_sndw_idisp_codec1_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
reset_sndw_idisp_codec2 = {'job': 'reset_sndw_idisp_codec2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

#sndw_idisplay_multislave_singlelane = {'job': 'sndw_idisplay_multislave_singlelane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_multislave_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
#sndw_idisplay_multislave_singlelane_coupled = {'job': 'sndw_idisplay_multislave_singlelane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_multislave_singlelane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

# sndw_idisplay_codec1_1lane = {'job': 'sndw_idisplay_codec1_1lane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_1lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
# sndw_idisplay_codec1_1lane_coupled = {'job': 'sndw_idisplay_codec1_1lane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_1lane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
# sndw_idisplay_codec2_1lane = {'job': 'sndw_idisplay_codec2_1lane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
# sndw_idisplay_codec2_1lane_coupled = {'job': 'sndw_idisplay_codec2_1lane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}



###SNDW IDISP nvlh (sndw/ptl/nvlh_ondie/) ### ############################################################################################################

reset_coupled_sndw_idisp_codec1   = {'job': 'reset_coupled_sndw_idisp_codec1', 'type': 'perspec_maestro', 'feature_list': ['sndw'],   'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
reset_coupled_sndw_idisp_codec1_0 = {'job': 'reset_coupled_sndw_idisp_codec1_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_0, 'maestro_seed_count': maestro_seed_count}]}
reset_coupled_sndw_idisp_codec1_1 = {'job': 'reset_coupled_sndw_idisp_codec1_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_1, 'maestro_seed_count': maestro_seed_count}]}

reset_coupled_sndw_idisp_codec2 = {'job': 'reset_coupled_sndw_idisp_codec2', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
reset_coupled_sndw_idisp_codec2_0 = {'job': 'reset_coupled_sndw_idisp_codec2_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
reset_coupled_sndw_idisp_codec2_1 = {'job': 'reset_coupled_sndw_idisp_codec2_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_coupled_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

reset_sndw_idisp_codec1   = {'job': 'reset_sndw_idisp_codec1', 'type': 'perspec_maestro', 'feature_list': ['sndw'],   'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
reset_sndw_idisp_codec1_0 = {'job': 'reset_sndw_idisp_codec1_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_0, 'maestro_seed_count': maestro_seed_count}]}
reset_sndw_idisp_codec1_1 = {'job': 'reset_sndw_idisp_codec1_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed_1, 'maestro_seed_count': maestro_seed_count}]}

reset_sndw_idisp_codec2_0 = {'job': 'reset_sndw_idisp_codec2_0', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

reset_sndw_idisp_codec2_1 = {'job': 'reset_sndw_idisp_codec2_1', 'type': 'perspec_maestro', 'feature_list': ['sndw'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/reset_sndw_idisp_codec2.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

sndw_idisplay_multislave_singlelane         = {'job': 'sndw_idisplay_multislave_singlelane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'],         'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_multislave_singlelane.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_multislave_singlelane_coupled = {'job': 'sndw_idisplay_multislave_singlelane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_multislave_singlelane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}


sndw_idisplay_codec1_1lane         = {'job': 'sndw_idisplay_codec1_1lane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'],         'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_1lane.sln',         'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_codec1_1lane_coupled = {'job': 'sndw_idisplay_codec1_1lane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec1_1lane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_codec2_1lane         = {'job': 'sndw_idisplay_codec2_1lane', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'],         'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane.sln',        'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}
sndw_idisplay_codec2_1lane_coupled = {'job': 'sndw_idisplay_codec2_1lane_coupled', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/sndw/ptl/sndw_idisplay_codec2_1lane_coupled.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}

test_sndw_idisp_enum = {'job': 'test_sndw_idisp_enum', 'type': 'perspec_maestro', 'feature_list': ['sndw_idisp'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sndw/ptl/test_sndw_idisp_enum.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'perspec_seed': perspec_seed, 'maestro_seed_count': maestro_seed_count}]}




### MICPRV  ############################################################################################################
sndw_micpvc_fmmd0_ddze_disable = {'job': 'sndw_micpvc_fmmd0_ddze_disable', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0_ddze_disable.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_ddze_disable = {'job': 'dmic_micpvc_fmmd0_ddze_disable', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_ddze_disable.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0 = {'job': 'sndw_micpvc_fmmd0', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0_1 = {'job': 'sndw_micpvc_fmmd0_1', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_dmic_micpvc_fmmd0 = {'job': 'sndw_dmic_micpvc_fmmd0', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/sndw_dmic_micpvc_fmmd0.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_nonwrap = {'job': 'dmic_micpvc_fmmd0_nonwrap', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_nonwrap_1 = {'job': 'dmic_micpvc_fmmd0_nonwrap_1', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_nonwrap_2 = {'job': 'dmic_micpvc_fmmd0_nonwrap_2', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd1 = {'job': 'sndw_micpvc_fmmd1', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd1_1 = {'job': 'sndw_micpvc_fmmd1_1', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd1_nonwrap = {'job': 'dmic_micpvc_fmmd1_nonwrap', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd1_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd1_nonwrap_1 = {'job': 'dmic_micpvc_fmmd1_nonwrap_1', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd1_nonwrap.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed_1': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_dsscs_reset = {'job': 'dmic_micpvc_fmmd0_dsscs_reset', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_dsscs_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_platform_reset = {'job': 'dmic_micpvc_fmmd0_platform_reset', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_platform_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_forcemute   = {'job': 'dmic_micpvc_fmmd0_forcemute', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_forcemute.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_micpvc_fmmd0_spa_whack   = {'job': 'dmic_micpvc_fmmd0_spa_whack', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/micpvc/dmic_micpvc_fmmd0_spa_whack.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0_dsscs_reset = {'job': 'sndw_micpvc_fmmd0_dsscs_reset', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0_dsscs_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0_platform_reset = {'job': 'sndw_micpvc_fmmd0_platform_reset', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0_platform_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0_forcemute = {'job': 'sndw_micpvc_fmmd0_forcemute', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0_forcemute.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_micpvc_fmmd0_spa_whack = {'job': 'sndw_micpvc_fmmd0_spa_whack', 'type': 'perspec_maestro', 'feature_list': ['MICPRV'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/micpvc/sndw_micpvc_fmmd0_spa_whack.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

### (3) SHA ############################################################################################################
sha_one_time_hashing = {'job': 'sha_one_time_hashing', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sha_one_time_hashing_0 = {'job': 'sha_one_time_hashing_0', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sha_one_time_hashing_1 = {'job': 'sha_one_time_hashing_1', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sha_one_time_hashing_2 = {'job': 'sha_one_time_hashing_2', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sha_one_time_hashing_3 = {'job': 'sha_one_time_hashing_3', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sha_one_time_hashing_4 = {'job': 'sha_one_time_hashing_4', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_one_time_hashing.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

sha_rand = {'job': 'sha_rand', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_0 = {'job': 'sha_rand_0', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_1 = {'job': 'sha_rand_1', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_2 = {'job': 'sha_rand_2', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_3 = {'job': 'sha_rand_3', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_4 = {'job': 'sha_rand_4', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_5 = {'job': 'sha_rand_5', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_6 = {'job': 'sha_rand_6', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_rand_7 = {'job': 'sha_rand_7', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_rand.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

sha_resume_interleave = {'job': 'sha_resume_interleave', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_resume_interleave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_resume_interleave_0 = {'job': 'sha_resume_interleave_0', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_resume_interleave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_resume_interleave_1 = {'job': 'sha_resume_interleave_1', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_resume_interleave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_resume_interleave_2 = {'job': 'sha_resume_interleave_2', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_resume_interleave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
sha_resume_interleave_3 = {'job': 'sha_resume_interleave_3', 'type': 'perspec_maestro', 'feature_list': ['SHA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/sha/sha_resume_interleave.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}


### (32) TTS ############################################################################################################
#####Multiple Tests in each single TC#####
timestamping_conc_hda_idisp_dmic_host_hhtse = {'job': 'timestamping_conc_hda_idisp_dmic_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_hda_idisp_dmic_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_conc_hda_idisp_ssp_host_hhtse  = {'job': 'timestamping_conc_hda_idisp_ssp_host_hhtse ', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_hda_idisp_ssp_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_conc_hda_idisp_sndw_host_hhtse = {'job': 'timestamping_conc_hda_idisp_sndw_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_hda_idisp_sndw_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
                                                                                                                                                                                                                                   
timestamping_conc_uaol_dmic_host_hhtse      = {'job': 'timestamping_conc_uaol_dmic_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_uaol_dmic_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol_conc, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_conc_uaol_ssp_host_hhtse       = {'job': 'timestamping_conc_uaol_ssp_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_uaol_ssp_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol_conc, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_conc_uaol_sndw_host_hhtse      = {'job': 'timestamping_conc_uaol_sndw_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_uaol_sndw_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol_conc, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
                                                                                                                                                                                                                                   
timestamping_hda_legacy_out_host_hhtse_1      = {'job': 'timestamping_hda_legacy_out_host_hhtse_1', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_in_host_hhtse_0       = {'job': 'timestamping_hda_legacy_in_host_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_idisp_ldma_out_host_hhtse_0      = {'job': 'timestamping_idisp_ldma_out_host_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_ldma_out_dsp_hhtse         = {'job': 'timestamping_hda_ldma_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_ldma_in_dsp_hhtse          = {'job': 'timestamping_hda_ldma_in_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_dsp_hhtse       = {'job': 'timestamping_hda_legacy_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_in_dsp_hhtse        = {'job': 'timestamping_hda_legacy_in_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_ldma_out_dsp_odts          = {'job': 'timestamping_hda_ldma_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_ldma_in_dsp_odts           = {'job': 'timestamping_hda_ldma_in_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_dsp_odts        = {'job': 'timestamping_hda_legacy_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_in_dsp_odts         = {'job': 'timestamping_hda_legacy_in_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_ldma_out_host_hhtse        = {'job': 'timestamping_hda_ldma_out_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_ldma_in_host_hhtse         = {'job': 'timestamping_hda_ldma_in_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_host_hhtse_2      = {'job': 'timestamping_hda_legacy_out_host_hhtse_2', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_in_host_hhtse_1      = {'job': 'timestamping_hda_legacy_in_host_hhtse_1', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_ldma_out_host_odts         = {'job': 'timestamping_hda_ldma_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_ldma_in_host_odts          = {'job': 'timestamping_hda_ldma_in_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_host_odts       = {'job': 'timestamping_hda_legacy_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_in_host_odts        = {'job': 'timestamping_hda_legacy_in_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_legacy_out_host_hhtse_mcdss_eocs_ocs        = {'job': 'timestamping_hda_legacy_out_host_hhtse_mcdss_eocs_ocs', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_host_hhtse_mcdss_eocs_ocs.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_host_hhtse_mcdss_dwcs        = {'job': 'timestamping_hda_legacy_out_host_hhtse_mcdss_dwcs', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse_mcdss_dwcs.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_host_dsp_hhtse_dwcs        = {'job': 'timestamping_hda_legacy_out_host_dsp_hhtse_dwcs', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_dsp_hhtse_dwcs.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_hda_legacy_out_host_hhtse_dwcs_eocs_ocs         = {'job': 'timestamping_hda_legacy_out_host_hhtse_dwcs_eocs_ocs', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse_dwcs_eocs_ocs.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
#####Single Test in each single TC#####
timestamping_conc_hda_idisp_uaol_host_hhtse = {'job': 'timestamping_conc_hda_idisp_uaol_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_conc_hda_idisp_uaol_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol_conc, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_dmic_dsp_hhtse               = {'job': 'timestamping_dmic_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_dmic_dsp_hhtse_0               = {'job': 'timestamping_dmic_dsp_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_dmic_dsp_hhtse_1               = {'job': 'timestamping_dmic_dsp_hhtse_1', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_dmic_dsp_odts                  = {'job': 'timestamping_dmic_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_dmic_host_hhtse                = {'job': 'timestamping_dmic_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_dmic_host_odts                 = {'job': 'timestamping_dmic_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_hda_legacy_out_host_hhtse_0    = {'job': 'timestamping_hda_legacy_out_host_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_idisp_ldma_out_dsp_hhtse       = {'job': 'timestamping_idisp_ldma_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_idisp_ldma_out_dsp_odts        = {'job': 'timestamping_idisp_ldma_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_idisp_ldma_out_host_hhtse      = {'job': 'timestamping_idisp_ldma_out_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_idisp_ldma_out_host_odts       = {'job': 'timestamping_idisp_ldma_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_sndw_dsp_hhtse                 = {'job': 'timestamping_sndw_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_sndw_dsp_odts                  = {'job': 'timestamping_sndw_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_sndw_host_hhtse                = {'job': 'timestamping_sndw_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_sndw_host_odts                 = {'job': 'timestamping_sndw_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

timestamping_ssp_dsp_hhtse                  = {'job': 'timestamping_ssp_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_ssp_dsp_odts                   = {'job': 'timestamping_ssp_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_ssp_host_hhtse                 = {'job': 'timestamping_ssp_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_ssp_host_odts                  = {'job': 'timestamping_ssp_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
                                                                                                                                                                                                                                   
timestamping_uaol_in_dsp_hhtse              = {'job': 'timestamping_uaol_in_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_uaol_in_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_uaol_in_dsp_odts               = {'job': 'timestamping_uaol_in_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_uaol_in_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_uaol_in_host_hhtse             = {'job': 'timestamping_uaol_in_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_uaol_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
timestamping_uaol_in_host_odts              = {'job': 'timestamping_uaol_in_host_odts', 'type': 'perspec_maestro', 'feature_list': ['tts'],  'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_uaol_in_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}



#timestamping_hda_ldma_out_dsp_hhtse = {'job': 'timestamping_hda_ldma_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_in_dsp_hhtse = {'job': 'timestamping_hda_ldma_in_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_dsp_hhtse = {'job': 'timestamping_hda_legacy_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_in_dsp_hhtse = {'job': 'timestamping_hda_legacy_in_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_idisp_ldma_out_dsp_hhtse = {'job': 'timestamping_idisp_ldma_out_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_sndw_dsp_hhtse = {'job': 'timestamping_sndw_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_ssp_dsp_hhtse = {'job': 'timestamping_ssp_dsp_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_dsp_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_dmic_dsp_odts = {'job': 'timestamping_dmic_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_out_dsp_odts = {'job': 'timestamping_hda_ldma_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_in_dsp_odts = {'job': 'timestamping_hda_ldma_in_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_dsp_odts = {'job': 'timestamping_hda_legacy_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_in_dsp_odts = {'job': 'timestamping_hda_legacy_in_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_idisp_ldma_out_dsp_odts = {'job': 'timestamping_idisp_ldma_out_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_sndw_dsp_odts = {'job': 'timestamping_sndw_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_ssp_dsp_odts = {'job': 'timestamping_ssp_dsp_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_dsp_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_dmic_host_hhtse = {'job': 'timestamping_dmic_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_out_host_hhtse = {'job': 'timestamping_hda_ldma_out_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_in_host_hhtse = {'job': 'timestamping_hda_ldma_in_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#
timestamping_hda_legacy_out_host_hhtse = {'job': 'timestamping_hda_legacy_out_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_host_hhtse_0 = {'job': 'timestamping_hda_legacy_out_host_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_host_hhtse_1 = {'job': 'timestamping_hda_legacy_out_host_hhtse_1', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_host_hhtse_2 = {'job': 'timestamping_hda_legacy_out_host_hhtse_2', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#
timestamping_hda_legacy_in_host_hhtse = {'job': 'timestamping_hda_legacy_in_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#
#timestamping_idisp_ldma_out_host_hhtse = {'job': 'timestamping_idisp_ldma_out_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_idisp_ldma_out_host_hhtse_0 = {'job': 'timestamping_idisp_ldma_out_host_hhtse_0', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#
#timestamping_sndw_host_hhtse = {'job': 'timestamping_sndw_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_ssp_host_hhtse = {'job': 'timestamping_ssp_host_hhtse', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_host_hhtse.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_dmic_host_odts = {'job': 'timestamping_dmic_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_dmic_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_out_host_odts = {'job': 'timestamping_hda_ldma_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_ldma_in_host_odts = {'job': 'timestamping_hda_ldma_in_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_ldma_in_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_out_host_odts = {'job': 'timestamping_hda_legacy_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_hda_legacy_in_host_odts = {'job': 'timestamping_hda_legacy_in_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_hda_legacy_in_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_idisp_ldma_out_host_odts = {'job': 'timestamping_idisp_ldma_out_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_idisp_ldma_out_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_sndw_host_odts = {'job': 'timestamping_sndw_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_sndw_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
#timestamping_ssp_host_odts = {'job': 'timestamping_ssp_host_odts', 'type': 'perspec_maestro', 'feature_list': ['TTS'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/timestamp/timestamping_ssp_host_odts.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

### (18) PM ############################################################################################################
dmic_wov_ptl   = {'job': 'dmic_wov_ptl',   'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed,   'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_0 = {'job': 'dmic_wov_ptl_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_0, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_1 = {'job': 'dmic_wov_ptl_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_2 = {'job': 'dmic_wov_ptl_2', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_3 = {'job': 'dmic_wov_ptl_3', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_4 = {'job': 'dmic_wov_ptl_4', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_5 = {'job': 'dmic_wov_ptl_5', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_6 = {'job': 'dmic_wov_ptl_6', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_7 = {'job': 'dmic_wov_ptl_7', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_8 = {'job': 'dmic_wov_ptl_8', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_rtd3wov = {'job': 'dmic_rtd3wov', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_rtd3wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

dmic_wov_ptl_gna_0 = {'job': 'dmic_wov_ptl_gna_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl_gna.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_wov_ptl_gna_1 = {'job': 'dmic_wov_ptl_gna_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl_gna.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_rtd3wov_gna = {'job': 'dmic_rtd3wov_gna', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_rtd3wov_gna.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_dpdma_wov_ptl_pm = {'job': 'dmic_dpdma_wov_ptl_pm', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_dpdma_wov_nvlh = {'job': 'dmic_dpdma_wov_nvlh', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
dmic_dpdma_wov_nvlh_0 = {'job': 'dmic_dpdma_wov_nvlh_0', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_dpdma_wov_nvlh_1 = {'job': 'dmic_dpdma_wov_nvlh_1', 'type': 'perspec_maestro', 'feature_list': ['DMA'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_dpdma_wov_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

sndw_wov_ptl = {'job': 'sndw_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/sndw_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_wov_ptl_0 = {'job': 'sndw_wov_ptl_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/sndw_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_wov_ptl_1 = {'job': 'sndw_wov_ptl_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/sndw_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sndw_rtd3wov = {'job': 'sndw_rtd3wov', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/sndw_rtd3wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

hda_lpp_wcl = {'job': 'hda_lpp_wcl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_lpp_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
hda_lpp_wcl_0 = {'job': 'hda_lpp_wcl_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_lpp_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
hda_lpp_wcl_1 = {'job': 'hda_lpp_wcl_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_lpp_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

hda_wov_wcl = {'job': 'hda_wov_wcl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_wov_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
hda_wov_wcl_0 = {'job': 'hda_wov_wcl_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_wov_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_0, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
hda_wov_wcl_1 = {'job': 'hda_wov_wcl_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_wov_wcl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

hda_rtd3wov = {'job': 'hda_rtd3wov', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/hda_rtd3wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

ssp_pcm_single_dma_rtd3wov_ptl = {'job': 'ssp_pcm_single_dma_rtd3wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/ssp_pcm_single_dma_rtd3wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_pcm_single_dma_wov_ptl = {'job': 'ssp_pcm_single_dma_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_single_dma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_pcm_single_dma_wov_ptl_1 = {'job': 'ssp_pcm_single_dma_wov_ptl_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_single_dma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_pcm_single_dma_wov_ptl_2 = {'job': 'ssp_pcm_single_dma_wov_ptl_2', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_single_dma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

spa_whack_gna_10_ldma = {'job': 'spa_whack_gna_10_ldma', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_gna_10_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_idisp = {'job': 'spa_whack_idisp', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_idisp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_hda = {'job': 'spa_whack_hda', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_hda.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_dmic_ldma = {'job': 'spa_whack_dmic_ldma', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_dmic_ldma.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_dsp_dspmem = {'job': 'spa_whack_dsp_dspmem', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_dsp_dspmem.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_sndw_ptl = {'job': 'spa_whack_sndw_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_sndw_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_ssp_ptl = {'job': 'spa_whack_ssp_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_ssp_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

ace_dynamic_power_gating_comm_widget = {'job': 'ace_dynamic_power_gating_comm_widget', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dynamic_power_gating_comm_widget.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_dynamic_power_gating_comm_widget_ptl = {'job': 'ace_dynamic_power_gating_comm_widget_ptl', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dynamic_power_gating_comm_widget_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_dynamic_power_gating_comm_widget_nvlh = {'job': 'ace_dynamic_power_gating_comm_widget_nvlh', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dynamic_power_gating_comm_widget_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_dynamic_power_gating_comm_widget_nvlh_0 = {'job': 'ace_dynamic_power_gating_comm_widget_nvlh_0', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dynamic_power_gating_comm_widget_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_dynamic_power_gating_comm_widget_nvlh_1 = {'job': 'ace_dynamic_power_gating_comm_widget_nvlh_1', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/comm_widget/ace_dynamic_power_gating_comm_widget_nvlh.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_dmic_wov_cycle_pm = {'job': 'reset_dmic_wov_cycle_pm', 'type': 'perspec_maestro', 'feature_list': ['PM'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}


### (30) RESET ############################################################################################################
reset_dmic_wov_cycle_0 = {'job': 'reset_dmic_wov_cycle_0', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_1 = {'job': 'reset_dmic_wov_cycle_1', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_2 = {'job': 'reset_dmic_wov_cycle_2', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_3 = {'job': 'reset_dmic_wov_cycle_3', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_4 = {'job': 'reset_dmic_wov_cycle_4', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_5 = {'job': 'reset_dmic_wov_cycle_5', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_cycle_6 = {'job': 'reset_dmic_wov_cycle_6', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_dmic_wov_gna_cycle_0 = {'job': 'reset_dmic_wov_gna_cycle_0', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_1 = {'job': 'reset_dmic_wov_gna_cycle_1', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_2 = {'job': 'reset_dmic_wov_gna_cycle_2', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_3 = {'job': 'reset_dmic_wov_gna_cycle_3', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_4 = {'job': 'reset_dmic_wov_gna_cycle_4', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_5 = {'job': 'reset_dmic_wov_gna_cycle_5', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_wov_gna_cycle_6 = {'job': 'reset_dmic_wov_gna_cycle_6', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_dmic_wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_dspmem_cycle = {'job': 'reset_dspmem_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_dspmem_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dsp_audio_rand_cycle = {'job': 'reset_dsp_audio_rand_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_hda_decoupled_cycle = {'job': 'reset_hda_decoupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_hda_decoupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_hda_coupled_cycle = {'job': 'reset_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_dmic_cycle = {'job': 'reset_dmic_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_dmic_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_cycle_ptl = {'job': 'reset_sndw_cycle_ptl', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_cycle_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_cycle = {'job': 'reset_sndw_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_sndw_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_cycle_ldma = {'job': 'reset_sndw_cycle_ldma', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_sndw_wov_cycle_0 = {'job': 'reset_sndw_wov_cycle_0', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_1 = {'job': 'reset_sndw_wov_cycle_1', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_2 = {'job': 'reset_sndw_wov_cycle_2', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_3 = {'job': 'reset_sndw_wov_cycle_3', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_4 = {'job': 'reset_sndw_wov_cycle_4', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_5 = {'job': 'reset_sndw_wov_cycle_5', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_sndw_wov_cycle_6 = {'job': 'reset_sndw_wov_cycle_6', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_sndw_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_init_with_cold_reset_hda_coupled_cycle = {'job': 'reset_init_with_cold_reset_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_cold_reset_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_init_with_flr_hda_coupled_cycle = {'job': 'reset_init_with_flr_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_flr_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_init_with_s3_hda_coupled_cycle = {'job': 'reset_init_with_s3_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_s3_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_init_with_s4_hda_coupled_cycle = {'job': 'reset_init_with_s4_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_s4_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_init_with_s5_hda_coupled_cycle = {'job': 'reset_init_with_s5_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_s5_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_init_with_warm_reset_hda_coupled_cycle = {'job': 'reset_init_with_warm_reset_hda_coupled_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_init_with_warm_reset_hda_coupled_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_hda_wov = {'job': 'reset_hda_wov', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_hda_wov = {'job': 'reset_hda_wov', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_hda_lpp = {'job': 'reset_hda_lpp', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_hda_lpp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_ssp_wov_cycle_0 = {'job': 'reset_ssp_wov_cycle_0', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_1 = {'job': 'reset_ssp_wov_cycle_1', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_2 = {'job': 'reset_ssp_wov_cycle_2', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_3 = {'job': 'reset_ssp_wov_cycle_3', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_4 = {'job': 'reset_ssp_wov_cycle_4', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_5 = {'job': 'reset_ssp_wov_cycle_5', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_wov_cycle_6 = {'job': 'reset_ssp_wov_cycle_6', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_dmic_rtd3wov_cycle = {'job': 'reset_dmic_rtd3wov_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_dmic_rtd3wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_dmic_rtd3wov_gna_cycle = {'job': 'reset_dmic_rtd3wov_gna_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_dmic_rtd3wov_gna_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_hda_rtd3wov = {'job': 'reset_hda_rtd3wov', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_hda_rtd3wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_hda_rtd3wov_cycle = {'job': 'reset_hda_rtd3wov_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_hda_rtd3wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_sndw_rtd3wov_cycle = {'job': 'reset_sndw_rtd3wov_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_sndw_rtd3wov_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_ssp_rtd3wov = {'job': 'reset_ssp_rtd3wov', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/reset_ssp_rtd3wov.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
reset_ssp_cycle_ptl = {'job': 'reset_ssp_cycle_ptl', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/reset/wcl/reset_ssp_cycle_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

reset_uaol_cycle = {'job': 'reset_uaol_cycle', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/reset_uaol_cycle.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}


ace_rand_graceful_warm_reset = {'job': 'ace_rand_graceful_warm_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_warm_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_cold_reset = {'job': 'ace_rand_graceful_cold_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_cold_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_flr_reset = {'job': 'ace_rand_graceful_flr_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_flr_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_s3_reset = {'job': 'ace_rand_graceful_s3_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_s3_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_s4_reset = {'job': 'ace_rand_graceful_s4_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_s4_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_s5_reset = {'job': 'ace_rand_graceful_s5_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_s5_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_graceful_dsscs_reset = {'job': 'ace_rand_graceful_dsscs_reset', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_graceful_dsscs_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

ace_rand_ungraceful_reset_0 = {'job': 'ace_rand_ungraceful_reset_0', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_1 = {'job': 'ace_rand_ungraceful_reset_1', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_2 = {'job': 'ace_rand_ungraceful_reset_2', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_3 = {'job': 'ace_rand_ungraceful_reset_3', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_4 = {'job': 'ace_rand_ungraceful_reset_4', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_5 = {'job': 'ace_rand_ungraceful_reset_5', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ace_rand_ungraceful_reset_6 = {'job': 'ace_rand_ungraceful_reset_6', 'type': 'perspec_maestro', 'feature_list': ['RESET'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_ungraceful_reset.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}


### () SIIP ############################################################################################################
dmic_wov_cro = {'job': 'dmic_wov_cro', 'type': 'perspec_maestro', 'feature_list': ['SIIP_Chasis'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_wov_cro.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_cro_0 = {'job': 'dmic_wov_cro_0', 'type': 'perspec_maestro', 'feature_list': ['SIIP_Chasis'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_wov_cro.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_cro_1 = {'job': 'dmic_wov_cro_1', 'type': 'perspec_maestro', 'feature_list': ['SIIP_Chasis'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/dmic_wov_cro.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

dmic_wov_ptl_siip_0 = {'job': 'dmic_wov_ptl_siip_0', 'type': 'perspec_maestro', 'feature_list': ['SIIP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
dmic_wov_ptl_siip_1 = {'job': 'dmic_wov_ptl_siip_1', 'type': 'perspec_maestro', 'feature_list': ['SIIP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/dmic_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

ssp_pcm_single_dma_wov_ptl_4 = {'job': 'ssp_pcm_single_dma_wov_ptl_4', 'type': 'perspec_maestro', 'feature_list': ['SIIP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_single_dma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

### (30) UAOL ############################################################################################################
uaol_in_HS8000Hz32bits8ch250us_0 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_0', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_1 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_1', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_2 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_2', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_3 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_3', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_4 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_4', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_5 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_5', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_6 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_6', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_7 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_7', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_8 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_8', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_9 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_9', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_10 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_10', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_11 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_11', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_12 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_12', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS8000Hz32bits8ch250us_13 = {'job': 'uaol_in_HS8000Hz32bits8ch250us_13', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS8000Hz32bits8ch250us.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

#uaol_in_HS32000Hz16bits7ch4000us_aps1792 = {'job': 'uaol_in_HS32000Hz16bits7ch4000us_aps1792', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS32000Hz16bits7ch4000us_aps1792.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_in_HS32000Hz16bits7ch4000us_aps1792 = {'job': 'uaol_in_HS32000Hz16bits7ch4000us_aps1792', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_in_HS32000Hz16bits7ch4000us_aps1792.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_instream_hdma_corb = {'job': 'uaol_instream_hdma_corb', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_instream_hdma_corb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_instream_hdma_corb_1 = {'job': 'uaol_instream_hdma_corb_1', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_instream_hdma_corb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_instream_hdma_corb_2 = {'job': 'uaol_instream_hdma_corb_2', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_instream_hdma_corb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_outstream_hdma_corb_0 = {'job': 'uaol_outstream_hdma_corb_0', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_outstream_hdma_corb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_outstream_hdma_corb_1 = {'job': 'uaol_outstream_hdma_corb_1', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_outstream_hdma_corb.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_outstream_hdma_sndw = {'job': 'uaol_outstream_hdma_sndw', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_outstream_hdma_sndw.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_out_HS32000Hz16bits7ch4000us_frameadj_0 = {'job': 'uaol_out_HS32000Hz16bits7ch4000us_frameadj_0', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz16bits7ch4000us_frameadj.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_out_HS32000Hz16bits7ch4000us_frameadj_1 = {'job': 'uaol_out_HS32000Hz16bits7ch4000us_frameadj_1', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz16bits7ch4000us_frameadj.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_out_HS32000Hz16bits7ch4000us_frameadj_2 = {'job': 'uaol_out_HS32000Hz16bits7ch4000us_frameadj_2', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz16bits7ch4000us_frameadj.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_out_HS32000Hz16bits7ch4000us_frameadj_3 = {'job': 'uaol_out_HS32000Hz16bits7ch4000us_frameadj_3', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz16bits7ch4000us_frameadj.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_out_HS32000Hz32bits6ch250us_rateadj_decrement = {'job': 'uaol_out_HS32000Hz32bits6ch250us_rateadj_decrement', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz32bits6ch250us_rateadj_decrement.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_out_HS32000Hz32bits6ch250us_rateadj_increment = {'job': 'uaol_out_HS32000Hz32bits6ch250us_rateadj_increment', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz32bits6ch250us_rateadj_increment.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_out_HS32000Hz8bits6ch16000us_aps3072 = {'job': 'uaol_out_HS32000Hz8bits6ch16000us_aps3072', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_out_HS32000Hz8bits6ch16000us_aps3072.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

UAOL_MULTI_2EP_OUT = {'job': 'UAOL_MULTI_2EP_OUT', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/UAOL_MULTI_2EP_OUT.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
UAOL_MULTI_2EP_INOUT = {'job': 'UAOL_MULTI_2EP_INOUT', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/UAOL_MULTI_2EP_INOUT.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_instream = {'job': 'uaol_instream', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_instream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_outstream = {'job': 'uaol_outstream', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_outstream.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_rand_fs = {'job': 'uaol_rand_fs', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_rand_fs.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_nocmdrsp = {'job': 'uaol_nocmdrsp', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_nocmdrsp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_conc_ssp_sndw_dmic = {'job': 'uaol_conc_ssp_sndw_dmic', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_ssp_sndw_dmic.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol_conc, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_ssp_sndw_dmic_dspmem1cores = {'job': 'uaol_conc_ssp_sndw_dmic_dspmem1cores', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_ssp_sndw_dmic_dspmem1cores.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_ssp_sndw_dmic_dspmem2cores = {'job': 'uaol_conc_ssp_sndw_dmic_dspmem2cores', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_ssp_sndw_dmic_dspmem2cores.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_ssp_sndw_dmic_commwidget = {'job': 'uaol_conc_ssp_sndw_dmic_commwidget', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_ssp_sndw_dmic_commwidget.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_conc_dspmem_1cores_l2uncache = {'job': 'uaol_conc_dspmem_1cores_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_1cores_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_dspmem_1cores_hpsram = {'job': 'uaol_conc_dspmem_1cores_hpsram', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_1cores_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_dspmem_2cores_l2uncache = {'job': 'uaol_conc_dspmem_2cores_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_2cores_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_dspmem_2cores_hpsram = {'job': 'uaol_conc_dspmem_2cores_hpsram', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_2cores_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_dspmem_3cores_l2uncache = {'job': 'uaol_conc_dspmem_2cores_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_3cores_l2uncache.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_dspmem_3cores_hpsram = {'job': 'uaol_conc_dspmem_2cores_hpsram', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_dspmem_3cores_hpsram.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
uaol_conc_sndw = {'job': 'uaol_conc_sndw', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_conc_sndw.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv,'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

uaol_error_injection = {'job': 'uaol_error_injection', 'type': 'perspec_maestro', 'feature_list': ['UAOL'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/uaol/uaol_error_injection.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files_uaol, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args_uaol, 'plat': plat_uaol, 'plat_csv': plat_uaol_csv, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}

### (11) Concurrency ############################################################################################################
ace_rand_dmic_dspmem_hda_idisp = {'job': 'ace_rand_dmic_dspmem_hda_idisp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_hda_idisp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_hda_idisp_sha = {'job': 'ace_rand_dmic_dspmem_hda_idisp_sha', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_hda_idisp_sha.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_hda_idisp_sha_sndw = {'job': 'ace_rand_dmic_dspmem_hda_idisp_sha_sndw', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_hda_idisp_sha_sndw.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_hda_idisp_sha_ssp = {'job': 'ace_rand_dmic_dspmem_hda_idisp_sha_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_hda_idisp_sha_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_hda_idisp_sha_sndw_ssp = {'job': 'ace_rand_dmic_dspmem_hda_idisp_sha_sndw_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_hda_idisp_sha_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

ace_rand_dmic_dspmem_gna_hda_idisp_sha_sndw_ssp = {'job': 'ace_rand_dmic_dspmem_gna_hda_idisp_sha_sndw_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_gna_hda_idisp_sha_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_gnacopysingle_hda_idisp_sha_sndw_ssp = {'job': 'ace_rand_dmic_dspmem_gnacopysingle_hda_idisp_sha_sndw_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_gnacopysingle_hda_idisp_sha_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp = {'job': 'ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp_1 = {'job': 'ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp_1', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

ace_rand_dmic_idisp_hdma_ssp = {'job': 'ace_rand_dmic_idisp_hdma_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_idisp_hdma_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count, 'seed_gen_count': 5}]}
ace_rand_dmic_idisp_hdma_sndw_ssp = {'job': 'ace_rand_dmic_idisp_hdma_sndw_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_idisp_hdma_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count, 'seed_gen_count': 5}]}
ace_rand_dmic_idisp_hdma_sndw_ssp_1 = {'job': 'ace_rand_dmic_idisp_hdma_sndw_ssp_1', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_idisp_hdma_sndw_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count, 'seed_gen_count': 5}]}
#ace_rand_dmic_idisp_hdma_ssp = {'job': 'ace_rand_dmic_idisp_hdma_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_idisp_hdma_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count, 'failure_threshold' : 500}]}
ace_rand_dmic_hda_idisp_ssp = {'job': 'ace_rand_dmic_hda_idisp_ssp', 'type': 'perspec_maestro', 'feature_list': ['concurrency'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ace_concurrency_nvl/ace_rand_dmic_hda_idisp_ssp.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count, 'failure_threshold' : 500}]}

### () SSP ############################################################################################################
ssp_3port_multi_dma_loopback = {'job': 'ssp_3port_multi_dma_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_multi_dma_loopback_1 = {'job': 'ssp_3port_multi_dma_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_multi_dma_loopback_2 = {'job': 'ssp_3port_multi_dma_loopback_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_multi_dma_loopback_3 = {'job': 'ssp_3port_multi_dma_loopback_3', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_multi_dma_loopback_4 = {'job': 'ssp_3port_multi_dma_loopback_4', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_slave_pcm_testCard = {'job': 'ssp_3port_slave_pcm_testCard', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_slave_pcm_testCard.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_received_without_transmit = {'job': 'ssp_1port_received_without_transmit', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_received_without_transmit.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_2port_singleDma_loopback_streamChain_evenChannel = {'job': 'ssp_2port_singleDma_loopback_streamChain_evenChannel', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_2port_singleDma_loopback_streamChain_evenChannel.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3port_singleDma_loopback_streamChain_mixChannel = {'job': 'ssp_3port_singleDma_loopback_streamChain_mixChannel', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_singleDma_loopback_streamChain_mixChannel.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback = {'job': 'ssp_1port_multi_dma_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_1 = {'job': 'ssp_1port_multi_dma_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_2 = {'job': 'ssp_1port_multi_dma_loopback_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_3 = {'job': 'ssp_1port_multi_dma_loopback_3', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_4 = {'job': 'ssp_1port_multi_dma_loopback_4', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_5 = {'job': 'ssp_1port_multi_dma_loopback_5', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_5, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_6 = {'job': 'ssp_1port_multi_dma_loopback_6', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_6, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_7 = {'job': 'ssp_1port_multi_dma_loopback_7', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_7, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_8 = {'job': 'ssp_1port_multi_dma_loopback_8', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_8, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_9 = {'job': 'ssp_1port_multi_dma_loopback_9', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_9, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_10 = {'job': 'ssp_1port_multi_dma_loopback_10', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_10, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_11 = {'job': 'ssp_1port_multi_dma_loopback_11', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_11, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_12 = {'job': 'ssp_1port_multi_dma_loopback_12', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_12, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_multi_dma_loopback_13 = {'job': 'ssp_1port_multi_dma_loopback_13', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_13, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_i2sMode = {'job': 'ssp_1port_i2sMode', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_i2sMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_i2sMode_1 = {'job': 'ssp_1port_i2sMode_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_i2sMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_i2sMode_2 = {'job': 'ssp_1port_i2sMode_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_i2sMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_pcmMode = {'job': 'ssp_1port_pcmMode', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_pcmMode_1 = {'job': 'ssp_1port_pcmMode_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_pcmMode_2 = {'job': 'ssp_1port_pcmMode_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_scs1 = {'job': 'ssp_1port_scs1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_scs1_1 = {'job': 'ssp_1port_scs1_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_1, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_scs1_2 = {'job': 'ssp_1port_scs1_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_2, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_scs1_3 = {'job': 'ssp_1port_scs1_3', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_3, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_1port_scs1_4 = {'job': 'ssp_1port_scs1_4', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_1port_scs1.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': perspec_seed_4, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_pcm_single_dma_wov_ptl_3 = {'job': 'ssp_pcm_single_dma_wov_ptl_3', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_single_dma_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_pcm_sync_wov_ptl = {'job': 'ssp_pcm_sync_wov_ptl', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/wov/wcl/ssp_pcm_sync_wov_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
spa_whack_ssp_ptl_1 = {'job': 'spa_whack_ssp_ptl_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/spa_whack/spa_whack_ssp_ptl.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_multi_dma_loopback_pcm = {'job': 'sync_3port_multi_dma_loopback_pcm', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_multi_dma_loopback_pcm.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_multi_dma_loopback_i2s = {'job': 'sync_3port_multi_dma_loopback_i2s', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_multi_dma_loopback_i2s.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_multi_dma_loopback_pcm_1 = {'job': 'sync_3port_multi_dma_loopback_pcm_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_multi_dma_loopback_pcm.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_multi_dma_loopback_i2s_1 = {'job': 'sync_3port_multi_dma_loopback_i2s_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_multi_dma_loopback_i2s.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_some_not_sync = {'job': 'sync_3port_some_not_sync', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_some_not_sync.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_couple_multidma_loopback = {'job': 'sync_3port_couple_multidma_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_couple_multidma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_couple_multidma_loopback_1 = {'job': 'sync_3port_couple_multidma_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_couple_multidma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_couple_same_framerate_loopback = {'job': 'sync_3port_couple_same_framerate_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_couple_same_framerate_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_couple_same_framerate_loopback_1 = {'job': 'sync_3port_couple_same_framerate_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_couple_same_framerate_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_same_framerate_loopback = {'job': 'sync_3port_same_framerate_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_same_framerate_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
sync_3port_same_framerate_loopback_1 = {'job': 'sync_3port_same_framerate_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/sync_3port_same_framerate_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
resync_3port_multi_dma_loopback = {'job': 'resync_3port_multi_dma_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/resync_3port_multi_dma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
resync_3port_same_framerate_loopback = {'job': 'resync_3port_same_framerate_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/resync_3port_same_framerate_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback = {'job': 'ssp_couple_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_1 = {'job': 'ssp_couple_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_i2sMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_2 = {'job': 'ssp_couple_loopback_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_3 = {'job': 'ssp_couple_loopback_3', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_3, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_4 = {'job': 'ssp_couple_loopback_4', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_4, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_5 = {'job': 'ssp_couple_loopback_5', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_5, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_6 = {'job': 'ssp_couple_loopback_6', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_6, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_7 = {'job': 'ssp_couple_loopback_7', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_7, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_8 = {'job': 'ssp_couple_loopback_8', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_8, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_9 = {'job': 'ssp_couple_loopback_9', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_9, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_10 = {'job': 'ssp_couple_loopback_10', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_10, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_11 = {'job': 'ssp_couple_loopback_11', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_11, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_12 = {'job': 'ssp_couple_loopback_12', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_12, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_13 = {'job': 'ssp_couple_loopback_13', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_13, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_14 = {'job': 'ssp_couple_loopback_14', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_14, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_i2sMode = {'job': 'ssp_couple_loopback_i2sMode', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_i2sMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_couple_loopback_pcmMode = {'job': 'ssp_couple_loopback_pcmMode', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_couple_loopback_pcmMode.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_3port_couple_multidma_loopback = {'job': 'ssp_3port_couple_multidma_loopback', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_couple_multidma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_3port_couple_multidma_loopback_1 = {'job': 'ssp_3port_couple_multidma_loopback_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_couple_multidma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_1, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_3port_couple_multidma_loopback_2 = {'job': 'ssp_3port_couple_multidma_loopback_2', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3port_couple_multidma_loopback.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_seed': perspec_seed_2, 'perspec_args': perspec_args, 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count':maestro_seed_count}]}
ssp_3ports_multi_dma_loopback_interrupt  = {'job': 'ssp_3ports_multi_dma_loopback_interrupt', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3ports_multi_dma_loopback_interrupt.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': random.randint(0,100000), 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}
ssp_3ports_multi_dma_loopback_interrupt_1 = {'job': 'ssp_3ports_multi_dma_loopback_interrupt_1', 'type': 'perspec_maestro', 'feature_list': ['SSP'], 'args': [{'content_location': r'/perspec/targets/ipsv/ace/fpga/ssp/ptl/ssp_3ports_multi_dma_loopback_interrupt.sln', 'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'perspec_seed': random.randint(0,100000), 'perspec_seed_count': perspec_seed_count, 'maestro_seed_count': maestro_seed_count}]}

### () ANNA [HPSRAM] ############################################################################################################
#Single Layer

#=======================================================================================================================================================================================

Affine_single_hpsram			= { 'job': 'Affine_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_hpsram_0			= { 'job': 'Affine_single_hpsram_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_hpsram_1			= { 'job': 'Affine_single_hpsram_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_hpsram_2			= { 'job': 'Affine_single_hpsram_2', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_hpsram_3			= { 'job': 'Affine_single_hpsram_3', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_single_hpsram			= { 'job': 'Affine_Mb_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Mb/Affine_Mb_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_single_hpsram			= { 'job': 'Diagonal_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Diagonal/Diagonal_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_single_hpsram				= { 'job': 'RNN_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/RNN/RNN_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_single_hpsram				= { 'job': 'CNN_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN/CNN_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_single_hpsram				= { 'job': 'CNN2D_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN2D/CNN2D_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_single_hpsram		= { 'job': 'DeInterleave_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DeInterleave/DeInterleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_single_hpsram		= { 'job': 'Interleave_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Interleave/Interleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_hpsram				= { 'job': 'Copy_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_hpsram_0				= { 'job': 'Copy_single_hpsram_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_hpsram_1				= { 'job': 'Copy_single_hpsram_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_hpsram_2				= { 'job': 'Copy_single_hpsram_2', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_hpsram_3				= { 'job': 'Copy_single_hpsram_3', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_single_hpsram		= { 'job': 'Enhanced_Copy_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_single_hpsram	= { 'job': 'Affine_Sparsity_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Sparsity/Affine_Sparsity_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Triple layer

#=======================================================================================================================================================================================

Affine_triple_hpsram			= { 'job': 'Affine_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_triple_hpsram			= { 'job': 'Affine_Mb_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Mb/Affine_Mb_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_triple_hpsram			= { 'job': 'Diagonal_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Diagonal/Diagonal_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_triple_hpsram				= { 'job': 'RNN_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/RNN/RNN_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_triple_hpsram				= { 'job': 'CNN_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN/CNN_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_triple_hpsram				= { 'job': 'CNN2D_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN2D/CNN2D_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_triple_hpsram		= { 'job': 'DeInterleave_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DeInterleave/DeInterleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_triple_hpsram		= { 'job': 'Interleave_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Interleave/Interleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_triple_hpsram				= { 'job': 'Copy_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_triple_hpsram		= { 'job': 'Enhanced_Copy_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_triple_hpsram	= { 'job': 'Affine_Sparsity_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Sparsity/Affine_Sparsity_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Multi layer

#=======================================================================================================================================================================================

Affine_multi_hpsram			= { 'job': 'Affine_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine/Affine_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_multi_hpsram			= { 'job': 'Affine_Mb_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Mb/Affine_Mb_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_multi_hpsram			= { 'job': 'Diagonal_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Diagonal/Diagonal_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_multi_hpsram				= { 'job': 'RNN_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/RNN/RNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_multi_hpsram				= { 'job': 'CNN_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN/CNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_multi_hpsram				= { 'job': 'CNN2D_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/CNN2D/CNN2D_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_multi_hpsram		= { 'job': 'DeInterleave_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DeInterleave/DeInterleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_multi_hpsram		= { 'job': 'Interleave_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Interleave/Interleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_multi_hpsram				= { 'job': 'Copy_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_multi_hpsram		= { 'job': 'Enhanced_Copy_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_multi_hpsram	= { 'job': 'Affine_Sparsity_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Affine_Sparsity/Affine_Sparsity_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

# With Enhanced Copy 4p5

#=======================================================================================================================================================================================

AllCombination_4p5_hpsram			= { 'job': 'AllCombination_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AllCombination_4p5_s_hpsram			= { 'job': 'AllCombination_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

AuxFunc_4p5_hpsram					= { 'job': 'AuxFunc_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AuxFunc_4p0_hpsram					= { 'job': 'AuxFunc_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

FuncAux_4p5_hpsram					= { 'job': 'FuncAux_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
FuncAux_4p0_hpsram					= { 'job': 'FuncAux_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationAux_4p5_hpsram			= { 'job': 'CombinationAux_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationAux_4p0_hpsram			= { 'job': 'CombinationAux_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationFunc_4p5_hpsram			= { 'job': 'CombinationFunc_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationFunc_4p0_hpsram			= { 'job': 'CombinationFunc_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

Mix_4p5_hpsram						= { 'job': 'Mix_4p5_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
Mix_4p0_hpsram						= { 'job': 'Mix_4p0_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

#=======================================================================================================================================================================================




# DWSC

#=======================================================================================================================================================================================
DWSC_single_hpsram				= { 'job': 'DWSC_single_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_single_hpsram_0				= { 'job': 'DWSC_single_hpsram_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_single_hpsram_1				= { 'job': 'DWSC_single_hpsram_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_triple_hpsram				= { 'job': 'DWSC_triple_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DWSC/DWSC_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_multi_hpsram				= { 'job': 'DWSC_multi_hpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/HPSRAM/DWSC/DWSC_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }




### () ANNA [L2UNCACHE] ############################################################################################################
#Single Layer

#=======================================================================================================================================================================================

Affine_single_l2uncache			= { 'job': 'Affine_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_l2uncache_0			= { 'job': 'Affine_single_l2uncache_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_l2uncache_1			= { 'job': 'Affine_single_l2uncache_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_single_l2uncache			= { 'job': 'Affine_Mb_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Mb/Affine_Mb_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_single_l2uncache			= { 'job': 'Diagonal_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Diagonal/Diagonal_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_single_l2uncache				= { 'job': 'RNN_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/RNN/RNN_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_single_l2uncache				= { 'job': 'CNN_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN/CNN_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_single_l2uncache				= { 'job': 'CNN2D_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN2D/CNN2D_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_single_l2uncache		= { 'job': 'DeInterleave_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DeInterleave/DeInterleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_single_l2uncache		= { 'job': 'Interleave_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Interleave/Interleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_l2uncache				= { 'job': 'Copy_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_single_l2uncache		= { 'job': 'Enhanced_Copy_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_single_l2uncache	= { 'job': 'Affine_Sparsity_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Sparsity/Affine_Sparsity_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Triple layer

#=======================================================================================================================================================================================

Affine_triple_l2uncache			= { 'job': 'Affine_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine/Affine_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_triple_l2uncache			= { 'job': 'Affine_Mb_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Mb/Affine_Mb_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_triple_l2uncache			= { 'job': 'Diagonal_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Diagonal/Diagonal_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_triple_l2uncache				= { 'job': 'RNN_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/RNN/RNN_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_triple_l2uncache				= { 'job': 'CNN_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN/CNN_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_triple_l2uncache				= { 'job': 'CNN2D_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN2D/CNN2D_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_triple_l2uncache		= { 'job': 'DeInterleave_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DeInterleave/DeInterleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_triple_l2uncache		= { 'job': 'Interleave_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Interleave/Interleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_triple_l2uncache				= { 'job': 'Copy_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_triple_l2uncache		= { 'job': 'Enhanced_Copy_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_triple_l2uncache	= { 'job': 'Affine_Sparsity_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Sparsity/Affine_Sparsity_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Multi layer

#=======================================================================================================================================================================================

Affine_multi_l2uncache			= { 'job': 'Affine_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine/Affine_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }



Affine_Mb_multi_l2uncache			= { 'job': 'Affine_Mb_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Mb/Affine_Mb_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_multi_l2uncache			= { 'job': 'Diagonal_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Diagonal/Diagonal_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_multi_l2uncache				= { 'job': 'RNN_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/RNN/RNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_multi_l2uncache				= { 'job': 'CNN_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN/CNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_multi_l2uncache				= { 'job': 'CNN2D_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/CNN2D/CNN2D_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_multi_l2uncache		= { 'job': 'DeInterleave_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DeInterleave/DeInterleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_multi_l2uncache		= { 'job': 'Interleave_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Interleave/Interleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_multi_l2uncache				= { 'job': 'Copy_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_multi_l2uncache		= { 'job': 'Enhanced_Copy_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_multi_l2uncache	= { 'job': 'Affine_Sparsity_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Affine_Sparsity/Affine_Sparsity_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

# With Enhanced Copy 4p5

#=======================================================================================================================================================================================

AllCombination_4p5_l2uncache			= { 'job': 'AllCombination_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AllCombination_4p0_l2uncache			= { 'job': 'AllCombination_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

AuxFunc_4p5_l2uncache					= { 'job': 'AuxFunc_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AuxFunc_4p0_l2uncache					= { 'job': 'AuxFunc_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

FuncAux_4p5_l2uncache					= { 'job': 'FuncAux_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
FuncAux_4p0_l2uncache					= { 'job': 'FuncAux_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationAux_4p5_l2uncache			= { 'job': 'CombinationAux_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationAux_4p0_l2uncache			= { 'job': 'CombinationAux_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationFunc_4p5_l2uncache			= { 'job': 'CombinationFunc_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationFunc_4p0_l2uncache			= { 'job': 'CombinationFunc_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

Mix_4p5_l2uncache						= { 'job': 'Mix_4p5_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
Mix_4p0_l2uncache						= { 'job': 'Mix_4p0_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

#=======================================================================================================================================================================================

#=======================================================================================================================================================================================

# DWSC

#=======================================================================================================================================================================================
DWSC_single_l2uncache				= { 'job': 'DWSC_single_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_triple_l2uncache				= { 'job': 'DWSC_triple_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DWSC/DWSC_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_multi_l2uncache				= { 'job': 'DWSC_multi_l2uncache', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/L2UNCACHE/DWSC/DWSC_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }


### () ANNA [IMR] ############################################################################################################
#Single Layer

#=======================================================================================================================================================================================

Affine_single_imr			= { 'job': 'Affine_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_imr_0			= { 'job': 'Affine_single_imr_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_imr_1			= { 'job': 'Affine_single_imr_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_imr_2			= { 'job': 'Affine_single_imr_2', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_single_imr_3			= { 'job': 'Affine_single_imr_3', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_single_imr			= { 'job': 'Affine_Mb_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Mb/Affine_Mb_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_single_imr			= { 'job': 'Diagonal_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Diagonal/Diagonal_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_single_imr				= { 'job': 'RNN_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/RNN/RNN_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_single_imr				= { 'job': 'CNN_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN/CNN_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_single_imr				= { 'job': 'CNN2D_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN2D/CNN2D_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_single_imr		= { 'job': 'DeInterleave_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DeInterleave/DeInterleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_single_imr		= { 'job': 'Interleave_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Interleave/Interleave_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_imr				= { 'job': 'Copy_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_imr_0				= { 'job': 'Copy_single_imr_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_imr_1				= { 'job': 'Copy_single_imr_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_imr_2				= { 'job': 'Copy_single_imr_2', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_single_imr_3				= { 'job': 'Copy_single_imr_3', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_single_imr		= { 'job': 'Enhanced_Copy_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_single_imr	= { 'job': 'Affine_Sparsity_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Sparsity/Affine_Sparsity_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Triple layer

#=======================================================================================================================================================================================

Affine_triple_imr			= { 'job': 'Affine_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_triple_imr			= { 'job': 'Affine_Mb_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Mb/Affine_Mb_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_triple_imr			= { 'job': 'Diagonal_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Diagonal/Diagonal_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_triple_imr				= { 'job': 'RNN_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/RNN/RNN_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_triple_imr				= { 'job': 'CNN_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN/CNN_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_triple_imr				= { 'job': 'CNN2D_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN2D/CNN2D_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_triple_imr		= { 'job': 'DeInterleave_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DeInterleave/DeInterleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_triple_imr		= { 'job': 'Interleave_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Interleave/Interleave_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_triple_imr				= { 'job': 'Copy_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_triple_imr		= { 'job': 'Enhanced_Copy_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_triple_imr	= { 'job': 'Affine_Sparsity_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Sparsity/Affine_Sparsity_triple.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

#Multi layer

#=======================================================================================================================================================================================

Affine_multi_imr			= { 'job': 'Affine_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine/Affine_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Mb_multi_imr			= { 'job': 'Affine_Mb_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Mb/Affine_Mb_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Diagonal_multi_imr			= { 'job': 'Diagonal_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Diagonal/Diagonal_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

RNN_multi_imr				= { 'job': 'RNN_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/RNN/RNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN_multi_imr				= { 'job': 'CNN_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN/CNN_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

CNN2D_multi_imr				= { 'job': 'CNN2D_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/CNN2D/CNN2D_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DeInterleave_multi_imr		= { 'job': 'DeInterleave_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DeInterleave/DeInterleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Interleave_multi_imr		= { 'job': 'Interleave_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Interleave/Interleave_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Copy_multi_imr				= { 'job': 'Copy_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Enhanced_Copy_multi_imr		= { 'job': 'Enhanced_Copy_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Copy/Copy_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

Affine_Sparsity_multi_imr	= { 'job': 'Affine_Sparsity_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Affine_Sparsity/Affine_Sparsity_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

#=======================================================================================================================================================================================

# With Enhanced Copy 4p5

#=======================================================================================================================================================================================

AllCombination_4p5_imr			= { 'job': 'AllCombination_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AllCombination_4p5_s_imr			= { 'job': 'AllCombination_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/AllCombination_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

AuxFunc_4p5_imr					= { 'job': 'AuxFunc_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
AuxFunc_4p0_imr					= { 'job': 'AuxFunc_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/AuxFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

FuncAux_4p5_imr					= { 'job': 'FuncAux_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
FuncAux_4p0_imr					= { 'job': 'FuncAux_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/FuncAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationAux_4p5_imr			= { 'job': 'CombinationAux_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationAux_4p0_imr			= { 'job': 'CombinationAux_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/CombinationAux_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

CombinationFunc_4p5_imr			= { 'job': 'CombinationFunc_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
CombinationFunc_4p0_imr			= { 'job': 'CombinationFunc_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/CombinationFunc_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

Mix_4p5_imr						= { 'job': 'Mix_4p5_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
								  
Mix_4p0_imr						= { 'job': 'Mix_4p0_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/Combination/Mix_4p5.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }								  

#=======================================================================================================================================================================================




# DWSC

#=======================================================================================================================================================================================
DWSC_single_imr				= { 'job': 'DWSC_single_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_single_imr_0				= { 'job': 'DWSC_single_imr_0', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_single_imr_1				= { 'job': 'DWSC_single_imr_1', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DWSC/DWSC_single_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_triple_imr				= { 'job': 'DWSC_triple_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DWSC/DWSC_triple_s.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

DWSC_multi_imr				= { 'job': 'DWSC_multi_imr', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/IMR/DWSC/DWSC_multi.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }




### () ANNA [ULPSRAM] ############################################################################################################
#Single Layer

#=======================================================================================================================================================================================

Copy_single_ulpsram				= { 'job': 'Copy_single_ulpsram', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p5/ULPSRAM/Copy/Copy_single.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 100,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }

### () GNA ############################################################################################################

Gna_traffic_reset				= { 'job': 'Gna_traffic_reset', 'type': 'perspec_maestro', 'feature_list': ['anna'],
									'args': [{
									'content_location': r'/perspec/targets/ipsv/ace/fpga/gna/gna_traffic_reset.sln',
									'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
									'perspec_seed': perspec_seed,
									'maestro_seed': 0,
									'perspec_seed_count': perspec_seed_count,
									'maestro_seed_count': maestro_seed_count,
									'failure_threshold' : 20,
									}]
								  }
# Focus test. GNA pause
Gna_pause_int 		            = { 'job': 'Gna_pause_int', 'type': 'perspec_maestro', 'feature_list': ['anna'],
                                	'args': [{
                                	'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p0/focus/gna_pause_int.sln',
                                	'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
                                	'perspec_seed': perspec_seed,
                                	'maestro_seed': 0,
                                	'perspec_seed_count': perspec_seed_count,
                                	'maestro_seed_count': maestro_seed_count,
                                	'failure_threshold' : 20,
                                	}]
                                  }

# Focus test. GNA pause
Gna_pause_int_disabled          = { 'job': 'Gna_pause_int_disabled', 'type': 'perspec_maestro', 'feature_list': ['anna'],
                                	'args': [{
                                	'content_location': r'/perspec/targets/ipsv/gna/fpga/emb/gna4p0/focus/gna_pause_int_disable.sln',
                                	'maestro_tags': maestro_tags, 'perspec_files': perspec_files, 'perspec_args': perspec_args, 'plat': plat,
                                	'perspec_seed': perspec_seed,
                                	'maestro_seed': 0,
                                	'perspec_seed_count': perspec_seed_count,
                                	'maestro_seed_count': maestro_seed_count,
                                	'failure_threshold' : 20,
                                	}]
                                  }

TESTLINES_TO_BE_EXECUTE = [
### 18 PM
							dmic_wov_ptl,
							dmic_wov_ptl_0,
							dmic_wov_ptl_1,
							dmic_wov_ptl_2,
							dmic_wov_ptl_3,
							dmic_wov_ptl_4,
							dmic_wov_ptl_5,
							dmic_wov_ptl_6,
							dmic_wov_ptl_7,
							dmic_wov_ptl_8,

							dmic_wov_cro_0,
							dmic_wov_cro_1,
							dmic_rtd3wov,
							dmic_wov_ptl_gna_0,
							dmic_wov_ptl_gna_1,
							dmic_rtd3wov_gna,
							sndw_wov_ptl,
							sndw_wov_ptl_0,
							sndw_wov_ptl_1,
							sndw_rtd3wov,
							hda_lpp_wcl,
							hda_lpp_wcl_0,
							hda_lpp_wcl_1,
							hda_wov_wcl,
							hda_wov_wcl_0,
							hda_wov_wcl_1,
							hda_rtd3wov,
							ssp_pcm_single_dma_rtd3wov_ptl,
							ssp_pcm_single_dma_wov_ptl,
							ssp_pcm_single_dma_wov_ptl_1,
							ssp_pcm_single_dma_wov_ptl_2,
							spa_whack_gna_10_ldma,
							spa_whack_idisp,
							spa_whack_hda,
							spa_whack_dmic_ldma,
							spa_whack_dsp_dspmem,
							spa_whack_sndw_ptl,
							spa_whack_ssp_ptl,

							ace_dynamic_power_gating_comm_widget,
							ace_dynamic_power_gating_comm_widget_ptl,
							ace_dynamic_power_gating_comm_widget_nvlh,
							ace_dynamic_power_gating_comm_widget_nvlh_0,
							ace_dynamic_power_gating_comm_widget_nvlh_1,

							reset_dmic_wov_cycle_pm,
							dmic_dpdma_wov_ptl_pm,
							dmic_dpdma_wov_nvlh,

### 30 RESET
							reset_dmic_wov_cycle_0,
							reset_dmic_wov_cycle_1,
							reset_dmic_wov_cycle_2,
							reset_dmic_wov_cycle_3,
							reset_dmic_wov_cycle_4,
							reset_dmic_wov_cycle_5,
							reset_dmic_wov_cycle_6,
							reset_dmic_wov_gna_cycle_0,
							reset_dmic_wov_gna_cycle_1,
							reset_dmic_wov_gna_cycle_2,
							reset_dmic_wov_gna_cycle_3,
							reset_dmic_wov_gna_cycle_4,
							reset_dmic_wov_gna_cycle_5,
							reset_dmic_wov_gna_cycle_6,
							reset_dspmem_cycle,
                            reset_dsp_audio_rand_cycle,
							reset_hda_decoupled_cycle,
							reset_hda_coupled_cycle,
							reset_dmic_cycle,
							reset_sndw_cycle_ptl,
							reset_sndw_cycle,
							reset_sndw_cycle_ldma,
							reset_sndw_wov_cycle_0,
							reset_sndw_wov_cycle_1,
							reset_sndw_wov_cycle_2,
							reset_sndw_wov_cycle_3,
							reset_sndw_wov_cycle_4,
							reset_sndw_wov_cycle_5,
							reset_sndw_wov_cycle_6,
							reset_init_with_cold_reset_hda_coupled_cycle,
							reset_init_with_flr_hda_coupled_cycle,
							reset_init_with_s3_hda_coupled_cycle,
							reset_init_with_s4_hda_coupled_cycle,
							reset_init_with_s5_hda_coupled_cycle,
							reset_init_with_warm_reset_hda_coupled_cycle,
							reset_hda_wov,
							reset_hda_lpp,
							reset_ssp_wov_cycle_0,
							reset_ssp_wov_cycle_1,
							reset_ssp_wov_cycle_2,
							reset_ssp_wov_cycle_3,
							reset_ssp_wov_cycle_4,
							reset_ssp_wov_cycle_5,
							reset_ssp_wov_cycle_6,
							reset_dmic_rtd3wov_cycle,
							reset_dmic_rtd3wov_gna_cycle,
							reset_hda_rtd3wov,
							reset_sndw_rtd3wov_cycle,
							reset_ssp_rtd3wov,
							reset_ssp_cycle_ptl,
							ace_rand_graceful_dsscs_reset,
							ace_rand_graceful_warm_reset,
							ace_rand_graceful_cold_reset,
							ace_rand_graceful_flr_reset,
							ace_rand_graceful_s3_reset,
							ace_rand_graceful_s4_reset,
							ace_rand_graceful_s5_reset,


### 32 DMIC decoupled
							dmic_rand_ldma_0,
							dmic_rand_ldma_1,
							dmic_rand_ldma_2,
							dmic_rand_ldma_3,
							dmic_rand_ldma_4,
							dmic_rand_ldma_5,
							dmic_rand_ldma_6,
							dmic_rand_ldma_7,
							dmic_rand_ldma_8,
							dmic_rand_ldma_9,
							dmic_rand_ldma_10,
							dmic_rand_ldma_11,
							dmic_rand_ldma_12,
							dmic_rand_ldma_13,
							dmic_rand_ldma_14,
							dmic_rand_ldma_15,

							hq_mode_Mic3840Khz_Dec_A48Khz_B16Khz_19Mhz,
							lpal_Mic768Khz_Dec_A48Khz_B16Khz_19Mhz,
							normal_Mic2400Khz_Dec_A32Khz_B16Khz_19Mhz,
							normal_Mic2400Khz_Dec_A48Khz_B16Khz_19Mhz,
							ultrasound_Mic3840Khz_Dec_A96Khz_B16Khz_19Mhz,

							dmic_clockedge_invert_mode,
							dmic_clockedge_nonInvert_mode,
							dmic_mono_mode,
							dmic_stereo_mode,

							dmic_pio_mode,
							dmic_pio_mode_0,

							dmic_dpdma_wov_ptl,
							dmic_dpdma_wov_ptl_0,
							dmic_dpdma_wov_ptl_1,

							dmic_of24_scs1,
							dmic_wov_ptl_dmic_0,
							dmic_wov_ptl_dmic_1,

### 26 DMIC coupled
							dmic_rand_allzero_coupled,
							dmic_rand_allzero_coupled_1,
							dmic_rand_allzero_coupled_2,
							dmic_rand_allzero_coupled_3,
							dmic_rand_allzero_coupled_4,
							dmic_rand_allzero_coupled_5,
							dmic_rand_allzero_coupled_6,
							dmic_rand_allzero_coupled_7,
							dmic_rand_allzero_coupled_8,
							dmic_rand_allzero_coupled_9,
							dmic_rand_allzero_coupled_10,
							dmic_rand_allzero_coupled_11,
							dmic_rand_allzero_coupled_12,
							dmic_rand_allzero_coupled_13,
							dmic_rand_allzero_coupled_14,
							dmic_rand_allzero_coupled_15,
							dmic_rand_allzero_coupled_16,
							dmic_rand_allzero_coupled_17,
							dmic_rand_allzero_coupled_18,
							dmic_rand_allzero_coupled_19,
							dmic_rand_allzero_coupled_20,
							dmic_rand_allzero_coupled_21,
							dmic_rand_allzero_coupled_22,
							dmic_rand_allzero_coupled_23,
							dmic_rand_allzero_coupled_24,
							dmic_rand_allzero_coupled_25,

							dmic_periodic_sync,

### DMA 
							ace_dpdma_0,
							ace_dpdma_1,
							ace_dpdma_2,
							ace_dpdma_3,
							ace_dpdma_4,
							ace_dpdma_5,
							ace_dpdma_6,
							ace_dpdma_7,
							ace_dpdma_8,
							ace_dpdma_9,
							ace_dpdma_10,
							ace_dpdma_11,
### 26 SSP
							ssp_3port_multi_dma_loopback,
							ssp_3port_multi_dma_loopback_1,
							ssp_3port_multi_dma_loopback_2,
							ssp_3port_multi_dma_loopback_3,
							ssp_3port_multi_dma_loopback_4,
							ssp_3port_slave_pcm_testCard,
							ssp_1port_received_without_transmit,
							ssp_2port_singleDma_loopback_streamChain_evenChannel,
							ssp_3port_singleDma_loopback_streamChain_mixChannel,
							ssp_1port_i2sMode,
							ssp_1port_i2sMode_1,
							ssp_1port_i2sMode_2,
							ssp_1port_pcmMode,
							ssp_1port_pcmMode_1,
							ssp_1port_pcmMode_2,
							ssp_1port_multi_dma_loopback,
							ssp_1port_multi_dma_loopback_1,
							ssp_1port_multi_dma_loopback_2,
							ssp_1port_multi_dma_loopback_3,
							ssp_1port_multi_dma_loopback_4,
							ssp_1port_multi_dma_loopback_5,
							ssp_1port_multi_dma_loopback_6,
							ssp_1port_multi_dma_loopback_7,
							ssp_1port_multi_dma_loopback_8,
							ssp_1port_multi_dma_loopback_9,
							ssp_1port_multi_dma_loopback_10,
							ssp_1port_multi_dma_loopback_11,
							ssp_1port_multi_dma_loopback_12,
							ssp_1port_multi_dma_loopback_13,
							ssp_1port_scs1,
							ssp_1port_scs1_1,
							ssp_1port_scs1_2,
							ssp_1port_scs1_3,
							ssp_1port_scs1_4,
							ssp_pcm_single_dma_wov_ptl_3,
							ssp_pcm_sync_wov_ptl,
							spa_whack_ssp_ptl_1,
							sync_3port_multi_dma_loopback_pcm,
							sync_3port_multi_dma_loopback_i2s,
							sync_3port_multi_dma_loopback_pcm_1,
							sync_3port_multi_dma_loopback_i2s_1,
							sync_3port_couple_multidma_loopback,
							sync_3port_couple_multidma_loopback_1,
							sync_3port_couple_same_framerate_loopback,
							sync_3port_couple_same_framerate_loopback_1,
							sync_3port_same_framerate_loopback,
							sync_3port_same_framerate_loopback_1,
							sync_3port_some_not_sync,
							resync_3port_multi_dma_loopback,
							resync_3port_same_framerate_loopback,
							ssp_couple_loopback,
							ssp_couple_loopback_1,
							ssp_couple_loopback_2,
							ssp_couple_loopback_3,
							ssp_couple_loopback_4,
							ssp_couple_loopback_5,
							ssp_couple_loopback_6,
							ssp_couple_loopback_7,
							ssp_couple_loopback_8,
							ssp_couple_loopback_9,
							ssp_couple_loopback_10,
							ssp_couple_loopback_11,
							ssp_couple_loopback_12,
							ssp_couple_loopback_13,
							ssp_couple_loopback_14,
							ssp_couple_loopback_i2sMode,
							ssp_couple_loopback_pcmMode,
							ssp_3port_couple_multidma_loopback,
							ssp_3port_couple_multidma_loopback_1,
							ssp_3port_couple_multidma_loopback_2,
							ssp_3ports_multi_dma_loopback_interrupt,
							ssp_3ports_multi_dma_loopback_interrupt_1,
### 10 DSPMEM
							dspmem_hpsram_hpsram,

							dspmem_50_0,
							dspmem_50_1,
							dspmem_50_2,
							dspmem_50_3,
							dspmem_50_4,
							dspmem_50_5,
							dspmem_50_6,
							dspmem_50_7,
							dspmem_50_8,
							dspmem_50_9,
							dspmem_50_10,
							dspmem_50_11,
							dspmem_50_12,
							dspmem_50_13,
							dspmem_50_14,
							dspmem_50_15,

							dspmem_hpsram_lpsram,
							dspmem_hpsram_l2uncache,
							dspmem_lpsram_lpsram,
							dspmem_lpsram_hpsram,
							dspmem_lpsram_l2uncache,
							dspmem_l2uncache_l2uncache,
							dspmem_l2uncache_hpsram,
							dspmem_l2uncache_lpsram,

							dspmem_dma_ulpsram,


### ADSP
							ace_dsp_comm_widget,
							dmic_micpvc_fmmd1_nonwrap_2,
							dmic_pio_mode_1,

### Audio Memory
							ace_audioMem_concurrent_access,
							ace_audioMem_concurrent_access_0,
							ace_audioMem_concurrent_access_1,
							ace_audioMem_concurrent_access_2,

							ace_audioMem_concurrent_access_wcl,
							ace_audioMem_concurrent_access_wcl_0,
							ace_audioMem_concurrent_access_wcl_1,
							ace_audioMem_concurrent_access_wcl_2,


### 24 HDA
                            reset_hda_lpp_0,
							reset_hda_lpp_1,
                            spa_whack_hda_lple,
							hda_lpp_lnl,
                            hda_lpp_wcl,
							hda_lpp_ptl,
                        	hda_wov_lnl,
							hda_wov_ptl,
							hda_fw_icr,
							hda_ssync_LDMA_input,
							hda_ssync_LDMA_output,

							hda_streams_with_crst,
							hda_streams_with_crst_1,
							hda_streams_with_crst_2,
							hda_streams_with_crst_3,

                            hda_LDMA_input_lple,
                            hda_LDMA_output_lple,

                            hda_coupled_corb_rirb,
							hda_coupled_corb_rirb_1,
							hda_coupled_corb_rirb_2,
							hda_coupled_corb_rirb_3,
							hda_coupled_corb_rirb_4,
							hda_coupled_corb_rirb_5,

                            hda_coupled_corb_gt_256,
                            hda_coupled_icr,
                            hda_coupled_10ms_buffering,
                            hda_coupled_input_2sdi,
                            hda_coupled_output_inst_0,
                            hda_coupled_output_runbit_pause_resume,
                            hda_coupled_SPIB_input,

							hda_coupled_SPIB_output,
							hda_coupled_SPIB_output_0,
							hda_coupled_SPIB_output_1,
							hda_coupled_SPIB_output_2,

                            hda_coupled_rand,
							hda_coupled_rand_0,
							hda_coupled_rand_1,
							hda_coupled_rand_2,
							hda_coupled_rand_3,
							hda_coupled_rand_4,
							hda_coupled_rand_5,
							hda_coupled_rand_6,
							hda_coupled_rand_7,
							hda_coupled_rand_8,
							hda_coupled_rand_9,

                            hda_LDMA_bandwidth_sdi_464,
                            hda_LDMA_bandwidth_sdo_960,

							hda_LDMA_input_inst_0,
							hda_HDMA_input_inst_0,

							hda_LDMA_output_inst_0,
							hda_LDMA_output_inst_0_0,
							hda_LDMA_output_inst_0_1,
							hda_LDMA_output_inst_0_2,
							hda_LDMA_output_inst_0_3,
							hda_LDMA_output_inst_0_4,
							hda_LDMA_output_inst_0_5,

                            hda_HDMA_output_inst_0,
                            hda_HDMA_output_inst_0_0,
							hda_HDMA_output_inst_0_1,
							hda_HDMA_output_inst_0_2,
							hda_HDMA_output_inst_0_3,
							hda_HDMA_output_inst_0_4,
							hda_HDMA_output_inst_0_5,
							hda_HDMA_output_inst_0_6,
							hda_HDMA_output_inst_0_7,
							hda_HDMA_output_inst_0_8,
							hda_HDMA_output_inst_0_9,
							hda_HDMA_output_inst_0_10,
							hda_HDMA_output_inst_0_11,

                            hda_HDMA_SPIB_output,
                            hda_HDMA_SPIB_input,

                            hda_decoupled_rand,
							hda_decoupled_rand_1,
                            hda_decoupled_rand_2,
                            hda_decoupled_rand_3,

							hda_coupled_flush_0,
							hda_coupled_flush_1,
							hda_coupled_flush_2,

							hda_coupled_rintcnt_focus,

### 28 IDISP Coupled
                            Idisp_cmdrsp,
                            Idisp_coupled_BPS_16,
                            Idisp_coupled_BPS_24,
                            Idisp_coupled_BPS_32,
                            Idisp_coupled_SR_32k,
                            Idisp_coupled_SR_44k,
                            Idisp_coupled_SR_48k,
                            Idisp_coupled_SR_88k,
                            Idisp_coupled_SR_96k,
                            Idisp_coupled_SR_176k,
                            Idisp_coupled_SR_192k,
                            Idisp_coupled_cc1,
                            Idisp_coupled_cc2,
                            Idisp_coupled_cc3,
                            Idisp_coupled_cc4,
                            Idisp_coupled_cc5,
                            Idisp_coupled_cc6,
                            Idisp_coupled_cc7,
                            Idisp_coupled_cc8,

                            Idisp_coupled_out_inst_0,
							Idisp_coupled_out_inst_0_0,
							Idisp_coupled_out_inst_0_1,
							Idisp_coupled_out_inst_0_2,
							Idisp_coupled_out_inst_0_3,

                            Idisp_coupled_out_inst_1,
                            Idisp_coupled_out_inst_2,
                            Idisp_coupled_out_inst_3,
                            Idisp_coupled_out_inst_4,
                            Idisp_coupled_out_inst_5,
                            Idisp_coupled_out_inst_6,
                            Idisp_coupled_out_inst_7,
                            Idisp_coupled_out_inst_8,

                            Idisp_coupled_out_rand,		#Run in QUAL only, Hardening haven't try.
                            Idisp_icr,
							Idisp_corb_rirb,


### 27 IDISP Decoupled
                            Idisp_decoupled_BPS_16,
                            Idisp_decoupled_BPS_24,
                            Idisp_decoupled_BPS_32,
                            Idisp_decoupled_SR_32k,
                            Idisp_decoupled_SR_44k,
                            Idisp_decoupled_SR_48k,
                            Idisp_decoupled_SR_88k,
                            Idisp_decoupled_SR_96k,
                            Idisp_decoupled_SR_176k,
                            Idisp_decoupled_SR_192k,
                            Idisp_decoupled_cc1,
                            Idisp_decoupled_cc2,
                            Idisp_decoupled_cc3,
                            Idisp_decoupled_cc4,
                            Idisp_decoupled_cc5,
                            Idisp_decoupled_cc6,
                            Idisp_decoupled_cc7,
                            Idisp_decoupled_cc8,
                            Idisp_decoupled_out_inst_0,
                            Idisp_decoupled_out_inst_1,
                            Idisp_decoupled_out_inst_2,
                            Idisp_decoupled_out_inst_3,
                            Idisp_decoupled_out_inst_4,
                            Idisp_decoupled_out_inst_5,
                            Idisp_decoupled_out_inst_6,
                            Idisp_decoupled_out_inst_7,
                            Idisp_decoupled_out_inst_8,

                            Idisp_decoupled_bandwidth_sdo, 		#Run in QUAL only, Hardening haven't try.


### LNL SNDW

							ace_sndw_loopback,
							ace_sndw_multilane_loopback,
							ace_sndw_in_stream,
							ace_sndw_out_stream,

### PTL SNDW

							ace_sndw_loopback_rand,
							ace_sndw_loopback_rand_0,
							ace_sndw_loopback_rand_1,
							ace_sndw_loopback_rand_2,
							ace_sndw_loopback_rand_3,
							ace_sndw_loopback_rand_4,
							ace_sndw_loopback_rand_5,
							ace_sndw_loopback_rand_6,
							ace_sndw_loopback_rand_7,
							ace_sndw_loopback_rand_8,
							ace_sndw_loopback_rand_9,
							ace_sndw_loopback_rand_10,
							ace_sndw_loopback_rand_11,
							ace_sndw_loopback_rand_12,
							ace_sndw_loopback_rand_13,
							ace_sndw_loopback_rand_14,
							ace_sndw_loopback_rand_15,
							ace_sndw_loopback_rand_16,
							ace_sndw_loopback_rand_17,
							ace_sndw_loopback_rand_18,
							ace_sndw_loopback_rand_19,
							ace_sndw_loopback_rand_20,
							ace_sndw_loopback_rand_21,
							ace_sndw_loopback_rand_22,
							ace_sndw_loopback_rand_23,
							ace_sndw_loopback_rand_24,
							ace_sndw_loopback_rand_25,
							ace_sndw_loopback_rand_26,
							ace_sndw_loopback_rand_27,
							ace_sndw_loopback_rand_28,
							ace_sndw_loopback_rand_29,
							ace_sndw_loopback_rand_30,
							ace_sndw_loopback_rand_31,
							ace_sndw_loopback_rand_32,

							ace_sndw_multilane_loopback_rand,
							lb_stream,
							lb_stream_ac_timing_rand,
							lb_stream_rand,
							lb_stream_pause,
							lb_stream_stop,
							lb_stream_tts_host,

							lb_stream_2_master,
							lb_stream_2_master_chain,
							lb_stream_2_master_chain_coupled,
							lb_stream_2_master_chain_mix,
							lb_stream_2_master_chain_mix_coupled,

							lb_stream_4_lane,
							lb_stream_4_lane_maxBw,

							lb_stream_4_lane_rand,
							lb_stream_4_lane_rand_0,
							lb_stream_4_lane_rand_1,
							lb_stream_4_lane_rand_2,
							lb_stream_4_lane_rand_3,
							lb_stream_4_lane_rand_4,
							lb_stream_4_lane_rand_5,
							lb_stream_4_lane_rand_6,
							lb_stream_4_lane_rand_7,
							lb_stream_4_lane_rand_8,
							lb_stream_4_lane_rand_9,
							lb_stream_4_lane_rand_10,
							lb_stream_4_lane_rand_11,
							lb_stream_4_lane_rand_12,
							lb_stream_4_lane_rand_13,
							lb_stream_4_lane_rand_14,

							ace_sndw_loopback_multilane_rand	,
							ace_sndw_loopback_multilane_rand_0  ,
							ace_sndw_loopback_multilane_rand_1  ,
							ace_sndw_loopback_multilane_rand_2  ,
							ace_sndw_loopback_multilane_rand_3  ,
							ace_sndw_loopback_multilane_rand_4  ,
							ace_sndw_loopback_multilane_rand_5  ,
							ace_sndw_loopback_multilane_rand_6  ,
							ace_sndw_loopback_multilane_rand_7  ,
							ace_sndw_loopback_multilane_rand_8  ,
							ace_sndw_loopback_multilane_rand_9  ,
							ace_sndw_loopback_multilane_rand_10 ,
							ace_sndw_loopback_multilane_rand_11 ,
							ace_sndw_loopback_multilane_rand_12 ,
							ace_sndw_loopback_multilane_rand_13 ,
							ace_sndw_loopback_multilane_rand_14 ,

							lb_stream_4_master,
							lb_stream_4_master_1,
							lb_stream_4_master_1,
							lb_stream_4_master_chain,
							lb_stream_4_master_coupled,
							lb_stream_aggr_nonaggr_conc,
							lb_stream_coupled,
							
							lb_stream_coupled_4_lane,
							
							lb_stream_coupled_4_master_rand,

							lb_stream_4_master,
							lb_stream_4_master_0,
							lb_stream_4_master_1,
							lb_stream_4_lane_multi_master_conc,

							lb_stream_external_clds_17clk_2400,
							lb_stream_external_clds_3clk_default,
							lb_stream_external_clds_3clk_default_nagetive,
							lb_stream_external_clds_4clk_9600,
							lb_stream_external_clds_8clk_9600,
							lb_stream_internal_clds_17clk_2400,
							lb_stream_internal_clds_3clk_default,
							lb_stream_internal_clds_4clk_9600,
							lb_stream_internal_clds_8clk_9600,


							out_stream,

							out_stream_2_slave,
							out_stream_2_slave_0,
							out_stream_2_slave_1,

							out_stream_4_lane,
							out_stream_4_lane_icr,
							out_stream_4_lane_rand,
							out_stream_coupled,
							out_stream_coupled_4_lane,
							out_stream_icr,
							out_stream_rand,

							out_stream_ac_timing_rand,
							out_stream_ac_timing_rand_0,
							out_stream_ac_timing_rand_1,
							out_stream_ac_timing_rand_2,
							out_stream_ac_timing_rand_3,
							out_stream_ac_timing_rand_4,

							in_stream,
							in_stream_4_lane,
							in_stream_4_lane_rand,
							in_stream_coupled,
							in_stream_coupled_4_lane,
							in_stream_icr,
							in_stream_rand,

							reset_coupled_sndw_idisp_codec1,
							reset_coupled_sndw_idisp_codec1_0,
							reset_coupled_sndw_idisp_codec1_1,

							reset_coupled_sndw_idisp_codec2,
							reset_coupled_sndw_idisp_codec2_0,
							reset_coupled_sndw_idisp_codec2_1,

							reset_sndw_idisp_codec1,
							reset_sndw_idisp_codec1_0,
							reset_sndw_idisp_codec1_1,

							reset_sndw_idisp_codec2,
							reset_sndw_idisp_codec2_0,
							reset_sndw_idisp_codec2_1,
							
							# reset_sndw_idisp_codec3,

							sndw_multimaster_multilane,

							sndw_multimaster_singlelane,
							sndw_multimaster_singlelane_0,
							sndw_multimaster_singlelane_1,

							sndw_scenarios_base,
							sndw_scenarios_lib,

							ace_sndw_bptin,
							ace_sndw_bptout,
							ace_sndw_loopback_asynchronous,
							ace_sndw_dsp_interrupt,
							ace_sndw_dsp_interrupt_0,
							ace_sndw_dsp_interrupt_1,
							lb_stream_tx_rx_controlled,

### SNDW IDISP
							sndw_idisplay_codec1_1lane,
							sndw_idisplay_codec1_1lane_coupled,
							sndw_idisplay_codec1_4lane,
                            sndw_idisplay_codec1_4lane_coupled,
							sndw_idisplay_codec1_4lane_sampleSize32_coupled,
							sndw_idisplay_codec2_1lane,
							sndw_idisplay_codec2_1lane_coupled,
							sndw_idisplay_multislave_singlelane,
							sndw_idisplay_multislave_singlelane_coupled,

							sndw_idisplay_codec2_1lane_sampleSize32_coupled,
							test_sndw_idisp_enum,
							
							sndw_idisplay_codec2_1lane_sampleSize32,

### MICPRV
							sndw_micpvc_fmmd0_ddze_disable,
							sndw_micpvc_fmmd1,
							sndw_micpvc_fmmd1_1,
							sndw_micpvc_fmmd0_forcemute,
							sndw_micpvc_fmmd0,
							sndw_micpvc_fmmd0_1,
							sndw_micpvc_fmmd0_dsscs_reset,
							sndw_micpvc_fmmd0_platform_reset,
							sndw_micpvc_fmmd0_spa_whack,
							dmic_micpvc_fmmd0_nonwrap,
							dmic_micpvc_fmmd0_nonwrap_1,
							dmic_micpvc_fmmd0_nonwrap_2,
							dmic_micpvc_fmmd1_nonwrap,
							dmic_micpvc_fmmd1_nonwrap_1,
							dmic_micpvc_fmmd0_ddze_disable,
							dmic_micpvc_fmmd0_forcemute,
							dmic_micpvc_fmmd0_dsscs_reset,
							dmic_micpvc_fmmd0_platform_reset,
							dmic_micpvc_fmmd0_spa_whack,
							sndw_dmic_micpvc_fmmd0,

### 30 UAOL
							uaol_in_HS8000Hz32bits8ch250us_0,
							uaol_in_HS8000Hz32bits8ch250us_1,
							uaol_in_HS8000Hz32bits8ch250us_2,
							uaol_in_HS8000Hz32bits8ch250us_3,
							uaol_in_HS8000Hz32bits8ch250us_4,
							uaol_in_HS8000Hz32bits8ch250us_5,
							uaol_in_HS8000Hz32bits8ch250us_6,
							uaol_in_HS8000Hz32bits8ch250us_7,
							uaol_in_HS8000Hz32bits8ch250us_8,
							uaol_in_HS8000Hz32bits8ch250us_9,
							uaol_in_HS8000Hz32bits8ch250us_10,
							uaol_in_HS8000Hz32bits8ch250us_11,
							uaol_in_HS8000Hz32bits8ch250us_12,
							uaol_in_HS8000Hz32bits8ch250us_13,
							#uaol_in_HS32000Hz16bits7ch4000us_aps1792,
							uaol_out_HS32000Hz8bits6ch16000us_aps3072,							
							uaol_out_HS32000Hz16bits7ch4000us_frameadj_0,
							uaol_out_HS32000Hz16bits7ch4000us_frameadj_1,
							uaol_out_HS32000Hz16bits7ch4000us_frameadj_2,
							uaol_out_HS32000Hz16bits7ch4000us_frameadj_3,
							uaol_out_HS32000Hz32bits6ch250us_rateadj_decrement,
							uaol_out_HS32000Hz32bits6ch250us_rateadj_increment,
							uaol_instream_hdma_corb,
							#uaol_outstream_hdma_sndw_0,
							#uaol_outstream_hdma_sndw_1,
							UAOL_MULTI_2EP_OUT,
							UAOL_MULTI_2EP_INOUT,
							uaol_instream,
							uaol_outstream,
							#uaol_conc_ssp_sndw_dmic_dspmem,
							uaol_conc_dspmem_3cores_l2uncache,
							uaol_conc_dspmem_3cores_hpsram,

### 3 SHA
                            sha_one_time_hashing,
							sha_one_time_hashing_0,
							sha_one_time_hashing_1,
							sha_one_time_hashing_2,
							sha_one_time_hashing_3,
							sha_one_time_hashing_4,

							sha_rand,
                            sha_rand_0,
                            sha_rand_1,
                            sha_rand_2,

                            sha_resume_interleave,
							sha_resume_interleave_0,
							sha_resume_interleave_1,
							sha_resume_interleave_2,
							sha_resume_interleave_3,


### 32 TTS
#####Multiple Tests in each single TC#####
							timestamping_conc_hda_idisp_dmic_host_hhtse 	,
							timestamping_conc_hda_idisp_ssp_host_hhtse      ,
							timestamping_conc_hda_idisp_sndw_host_hhtse     ,

							timestamping_conc_uaol_dmic_host_hhtse          ,
							timestamping_conc_uaol_ssp_host_hhtse           ,
							timestamping_conc_uaol_sndw_host_hhtse          ,

							timestamping_hda_legacy_out_host_hhtse_1        ,
							timestamping_hda_legacy_in_host_hhtse_0         ,
							timestamping_idisp_ldma_out_host_hhtse_0        ,

							timestamping_hda_ldma_out_dsp_hhtse             ,
							timestamping_hda_ldma_in_dsp_hhtse              ,
							timestamping_hda_legacy_out_dsp_hhtse           ,
							timestamping_hda_legacy_in_dsp_hhtse            ,

							timestamping_hda_ldma_out_dsp_odts              ,
							timestamping_hda_ldma_in_dsp_odts               ,
							timestamping_hda_legacy_out_dsp_odts            ,
							timestamping_hda_legacy_in_dsp_odts             ,

							timestamping_hda_ldma_out_host_hhtse            ,
							timestamping_hda_ldma_in_host_hhtse             ,
							timestamping_hda_legacy_out_host_hhtse_2        ,
							timestamping_hda_legacy_in_host_hhtse_1         ,

							timestamping_hda_ldma_out_host_odts             ,
							timestamping_hda_ldma_in_host_odts              ,
							timestamping_hda_legacy_out_host_odts           ,
							timestamping_hda_legacy_in_host_odts            ,


#####Single Test in each single TC#####
							timestamping_conc_hda_idisp_uaol_host_hhtse		,

							timestamping_dmic_dsp_hhtse_0                   ,
							timestamping_dmic_dsp_hhtse_1                   ,
							timestamping_dmic_dsp_odts                      ,
							timestamping_dmic_host_hhtse                    ,
							timestamping_dmic_host_odts                     ,

							timestamping_hda_legacy_out_host_hhtse_0        ,

							timestamping_idisp_ldma_out_dsp_hhtse           ,
							timestamping_idisp_ldma_out_dsp_odts            ,
							timestamping_idisp_ldma_out_host_hhtse          ,
							timestamping_idisp_ldma_out_host_odts           ,

							timestamping_sndw_dsp_hhtse                     ,
							timestamping_sndw_dsp_odts                      ,
							timestamping_sndw_host_hhtse                    ,
							timestamping_sndw_host_odts                     ,

							timestamping_ssp_dsp_hhtse                      ,
							timestamping_ssp_dsp_odts                       ,
							timestamping_ssp_host_hhtse                     ,
							timestamping_ssp_host_odts                      ,

							timestamping_uaol_in_dsp_hhtse                  ,
							timestamping_uaol_in_dsp_odts                   ,
							timestamping_uaol_in_host_hhtse                 ,
							timestamping_uaol_in_host_odts                  ,


							timestamping_dmic_dsp_hhtse,
							timestamping_dmic_dsp_hhtse_0,
							timestamping_dmic_dsp_hhtse_1,
#
#                           timestamping_hda_ldma_out_dsp_hhtse,
#                           timestamping_hda_ldma_in_dsp_hhtse,
#                           timestamping_hda_legacy_out_dsp_hhtse,
#                           timestamping_hda_legacy_in_dsp_hhtse,
#                           timestamping_idisp_ldma_out_dsp_hhtse,
#                           timestamping_sndw_dsp_hhtse,
#                           timestamping_ssp_dsp_hhtse,
#
#                           timestamping_dmic_dsp_odts,
#                           timestamping_hda_ldma_out_dsp_odts,
#                           timestamping_hda_ldma_in_dsp_odts,
#                           timestamping_hda_legacy_out_dsp_odts,
#                           timestamping_hda_legacy_in_dsp_odts,
#                           timestamping_idisp_ldma_out_dsp_odts,
#                           timestamping_sndw_dsp_odts,
#                           timestamping_ssp_dsp_odts,
#
#                           timestamping_dmic_host_hhtse,
#                           timestamping_hda_ldma_out_host_hhtse,
#                           timestamping_hda_ldma_in_host_hhtse,
#
							timestamping_hda_legacy_out_host_hhtse,
#							timestamping_hda_legacy_out_host_hhtse_0,
#							timestamping_hda_legacy_out_host_hhtse_1,
#							timestamping_hda_legacy_out_host_hhtse_2,
#
							timestamping_hda_legacy_in_host_hhtse,
							
							timestamping_hda_legacy_out_host_hhtse_mcdss_eocs_ocs,
							timestamping_hda_legacy_out_host_hhtse_mcdss_dwcs,
							timestamping_hda_legacy_out_host_dsp_hhtse_dwcs,
                            timestamping_hda_legacy_out_host_hhtse_dwcs_eocs_ocs,
#
#							timestamping_idisp_ldma_out_host_hhtse,
#							timestamping_idisp_ldma_out_host_hhtse_0,
#
#							timestamping_sndw_host_hhtse,
#                           timestamping_ssp_host_hhtse,
#
#                           timestamping_dmic_host_odts,
#                           timestamping_hda_ldma_out_host_odts,
#                           timestamping_hda_ldma_in_host_odts,
#                           timestamping_hda_legacy_out_host_odts,
#                           timestamping_hda_legacy_in_host_odts,
#                           timestamping_idisp_ldma_out_host_odts,
#                           timestamping_sndw_host_odts,
#                           timestamping_ssp_host_odts,

### 11 Concurrency
							ace_rand_dmic_dspmem_hda_idisp,
							ace_rand_dmic_dspmem_hda_idisp_sha,
							ace_rand_dmic_dspmem_hda_idisp_sha_sndw,
							ace_rand_dmic_dspmem_hda_idisp_sha_ssp,
							ace_rand_dmic_dspmem_hda_idisp_sha_sndw_ssp,

							ace_rand_dmic_dspmem_gna_hda_idisp_sha_sndw_ssp,
#							ace_rand_dmic_dspmem_gnacopysingle_hda_idisp_sha_sndw_ssp,
							ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp,
							ace_rand_dmic_dspmem_gna_hda_idisp_sndw_ssp_1,

							ace_rand_dmic_idisp_hdma_ssp,
							ace_rand_dmic_idisp_hdma_sndw_ssp,
							ace_rand_dmic_idisp_hdma_sndw_ssp_1,
#							ace_rand_dmic_hda_idisp_ssp,


###ANNA / GNA [HPSRAM]
#                           ### 1 Layer
#                           ##=====================
                           	Affine_single_hpsram			    ,
							Affine_single_hpsram_0			    ,
							Affine_single_hpsram_1			    ,
							Affine_single_hpsram_2			    ,
							Affine_single_hpsram_3			    ,
							Affine_Mb_single_hpsram             ,
							Diagonal_single_hpsram              ,
							RNN_single_hpsram                   ,
							CNN_single_hpsram                   ,
							CNN2D_single_hpsram                 ,
							DeInterleave_single_hpsram          ,
							Interleave_single_hpsram            ,
							Copy_single_hpsram                  ,
							Copy_single_hpsram_0                ,
							Copy_single_hpsram_1                ,
							Copy_single_hpsram_2				,
							Copy_single_hpsram_3				,
							Enhanced_Copy_single_hpsram         ,

#                           ### 3 Layer
#                           ##=====================
                           	Affine_triple_hpsram			    ,
							Affine_Mb_triple_hpsram             ,
							Diagonal_triple_hpsram              ,
							RNN_triple_hpsram                   ,
							CNN_triple_hpsram                   ,
							CNN2D_triple_hpsram                 ,
							DeInterleave_triple_hpsram          ,
							Interleave_triple_hpsram            ,
							Copy_triple_hpsram                  ,
							Enhanced_Copy_triple_hpsram         ,

#                           ### Multi Layer
#                           ##=====================
                           	Affine_multi_hpsram			        ,
							Affine_Mb_multi_hpsram              ,
							Diagonal_multi_hpsram               ,
							RNN_multi_hpsram                    ,
							CNN_multi_hpsram                    ,
							CNN2D_multi_hpsram                  ,
							DeInterleave_multi_hpsram           ,
							Interleave_multi_hpsram             ,
							Copy_multi_hpsram                   ,
							Enhanced_Copy_multi_hpsram          ,


                            ##with Enhanced Copy 4p5
                            ##===================
                            AllCombination_4p5_hpsram           ,
                            AuxFunc_4p5_hpsram                  ,
                            FuncAux_4p5_hpsram                  ,
                            CombinationAux_4p5_hpsram           ,
                            CombinationFunc_4p5_hpsram          ,
                            Mix_4p5_hpsram                      ,
							
							#AllCombination_4p0_hpsram           ,
							AuxFunc_4p0_hpsram                  ,
                            FuncAux_4p0_hpsram                  ,
                            CombinationAux_4p0_hpsram           ,
                            CombinationFunc_4p0_hpsram          ,
                            Mix_4p0_hpsram                      ,

#						    ##DWSC
#						    ##===================
							DWSC_single_hpsram                  ,
							DWSC_single_hpsram_0                ,
							DWSC_single_hpsram_1                ,

							DWSC_triple_hpsram                  ,
							DWSC_multi_hpsram                   ,


							Affine_Sparsity_single_hpsram       ,                  #Can take out if need follow QUAL TC
							Affine_Sparsity_triple_hpsram       ,                  #Can take out if need follow QUAL TC
							Affine_Sparsity_multi_hpsram        ,


###ANNA / GNA [L2UNCACHE]
#                           ### 1 Layer
#                           ##=====================
                           	Affine_single_l2uncache					,
							Affine_single_l2uncache_0				,
							Affine_single_l2uncache_1				,
							Affine_Mb_single_l2uncache              ,
							Diagonal_single_l2uncache               ,
							RNN_single_l2uncache                    ,
							CNN_single_l2uncache                    ,
							CNN2D_single_l2uncache                  ,
							DeInterleave_single_l2uncache           ,
							Interleave_single_l2uncache             ,
							Copy_single_l2uncache                   ,
							Enhanced_Copy_single_l2uncache          ,

#                           ### 3 Layer
#                           ##=====================
                           	Affine_triple_l2uncache			        ,
							Affine_Mb_triple_l2uncache              ,
							Diagonal_triple_l2uncache               ,
							RNN_triple_l2uncache                    ,
							CNN_triple_l2uncache                    ,
							CNN2D_triple_l2uncache                  ,
							DeInterleave_triple_l2uncache           ,
							Interleave_triple_l2uncache             ,
							Copy_triple_l2uncache                   ,
							Enhanced_Copy_triple_l2uncache          ,

#                           ### Multi Layer
#                           ##=====================
                           	Affine_multi_l2uncache			        ,
							Affine_Mb_multi_l2uncache               ,
							Diagonal_multi_l2uncache                ,
							RNN_multi_l2uncache                     ,
							CNN_multi_l2uncache                     ,
							CNN2D_multi_l2uncache                   ,
							DeInterleave_multi_l2uncache            ,
							Interleave_multi_l2uncache              ,
							Copy_multi_l2uncache                    ,
							Enhanced_Copy_multi_l2uncache           ,

#                           ##with Enhanced Copy
#                           ##===================
							AllCombination_4p5_l2uncache            ,
							AuxFunc_4p5_l2uncache                   ,
							FuncAux_4p5_l2uncache                   ,
							CombinationAux_4p5_l2uncache            ,
							CombinationFunc_4p5_l2uncache           ,
							Mix_4p5_l2uncache                       ,
							
							AllCombination_4p0_l2uncache            ,
							AuxFunc_4p0_l2uncache                   ,
							FuncAux_4p0_l2uncache                   ,
							CombinationAux_4p0_l2uncache            ,
							CombinationFunc_4p0_l2uncache           ,
							Mix_4p0_l2uncache                       ,

#						    ##DWSC
#						    ##===================
							DWSC_single_l2uncache                   ,
							DWSC_triple_l2uncache                   ,
							DWSC_multi_l2uncache                    ,

							Affine_Sparsity_single_l2uncache        ,                 #Can take out if need follow QUAL TC
							Affine_Sparsity_triple_l2uncache        ,                 #Can take out if need follow QUAL TC
							Affine_Sparsity_multi_l2uncache         ,

###ANNA / GNA [ULPSRAM]
							Copy_single_ulpsram						,

###GNA
							Gna_traffic_reset						,
                            Gna_pause_int                           ,
                            Gna_pause_int_disabled                  ,

###SIIP
							dmic_wov_ptl_siip_0,
                            dmic_wov_ptl_siip_1,
							ssp_pcm_single_dma_wov_ptl_4,



							]


PRE_GENERATED_MAESTRO_SEED_FOLDERS = []

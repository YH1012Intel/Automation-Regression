
phases = {
    'system_provisioning': [
        # Where setup.py located in sub directory
        {
            "BB_NAME": "PIP_INSTALL_VCS_URL",
            "branch": "master",
            #"branch": "biu-ltr",
            #"branch": "lkhaw-register-ml1-test",
            #"branch": "ttlhg4_core_num_fix",
            # "branch": "25WW44p3_neg_spsreq_dtf",
            # "branch": "WW43-leo-5p0-Register-Fix",
            # "branch": "ttlh-core0",
            # "branch": "update-requirestxt",
            # "branch": "namenodes-4p6-resetsignalfix",
            # "branch": "ttlh-namenodes-25ww35",
            # "branch": "25WW34_update_pysvtools",
            # "branch": "nvlh-namenodes-tam",
	    #"branch": "26WW05p3_pysvtools_version",
            #"commithash": "205133cdcbd1761fe9d1b8641b43f46d0721544e",
            "url": "https://github.com/intel-restricted/frameworks.validation.pythonsv.ipsv.ace",
            "subdirectory": "ipsv-pkg"
        },
        # {
        #  "BB_NAME": "PIP_INSTALL_VCS_URL",
        #  "branch": "master",
        #  "url": "https://github.com/intel-restricted/frameworks.validation.pythonsv.ipsv.ace",
        #  "subdirectory": "pysvext-pkg"
        # },
        {
            'BB_NAME': 'VERIFY_ITP_CONNECTION',
        },
        {
            'BB_NAME': 'RESET_ITP_CONNECTION',
        },
        {
            'BB_NAME': 'VERIFY_COREGROUPS_AND_DEVICES',
            'coregroups': ['GPC'],
            'devices': [],
        },
        
        #{
            #'BB_NAME': 'COVERAGE_GITHUB_SETUP',
            #'database': 'coverage_ttlh_ace_db',
            #'configure_db': True,
            #"branch": "lguntupa_falcon6_update"
        #},

        {
            'BB_NAME': 'HAPS_PROGRAMMING',
            # 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/NVL_nvldp-ace-ipfpga-cth-2024-05-21_HAPS_80_build1_upf_Vivado_par_directive_v6.2021.2/project.conf'
            # 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-07-29_HAPS_80_build1_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-07-29_HAPS_80_build2_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-08-28_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-08-28_HAPS_80_build0_upf_Vivado_par_directive.2021.2/project.conf'
            # 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-08_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-12_HAPS_80_build0_upf_Vivado_par_directive_v2.2021.2/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-12_HAPS_80_build1_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-25-drop_4.2_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-25-drop_4.2_HAPS_80_build0_upf_Vivado_par_directive_v2.2021.2/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-25-drop_4.2_HAPS_80_build1_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-09-24-smmu_HAPS_80_build0_upf_Vivado_par_directive_v2.2021.2/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-10-09-drop_5_HAPS_80_build6_upf_Vivado_par_directive_v6.2019.1/project.conf'
            #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-10-09-drop_5_HAPS_80_build6_upf_Vivado_par_directive_v2.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-10-09-drop_5_HAPS_80_build7_upf_Vivado_par_directive_v6.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-11-28-ace4px-drop-1_HAPS_80_build0_upf_Vivado_par_directive_v2.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-11-28-ace4px-drop-1_HAPS_80_build2_upf_Vivado_par_directive_v2.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2025-12-12-ace4px-drop-2_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2025-12-12-ace4px-drop-2_HAPS_80_build0_upf_Vivado_par_directive_v2.2019.1/project.conf'
             #'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2026-01-21-ace4px-drop-3_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
	     'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2026-01-21-ace4px-drop-3_HAPS_80_build0_upf_Vivado_par_directive_v6.2021.2/project.conf'

        },
        
        # {
            # 'BB_NAME': 'EXECUTE_COMMAND',
			# #'cmd': 'cd /nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/WCL_wcl-ace-ipfpga-cth-2023-08-02_HAPS_80_build7_upf_Vivado_par_directive_v2.2021.2;/p/ppa/farm/CAD_ROOT/synopsys/confpro/O-2018.09-2/bin/confprosh wcl_run.tcl',
            # 'cmd': 'cd /nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/;/p/ppa/farm/CAD_ROOT/synopsys/confpro/O-2018.09-2/bin/confprosh wcl_run.tcl',

            # 'os': 'linux',
            # 'timeout': 180,
        # },
        
        {
            'BB_NAME': 'USB_REDIRECTOR_UNSHARE_DEVICES',
        },
        {
            'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
            'port_value': 0,
            'duration': 10
        },
        # {
            # 'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
            # 'port_value': 1,
            # 'duration': 10
        # },
        {
            'BB_NAME': 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6',
        },
        {
            'BB_NAME': 'GENERATE_PLATFORM_CONFIG_XML',
        }
    ],

    'testline_execution': [
        {
            'BB_NAME': 'RESET_ITP_CONNECTION',
        },
         { 
            'BB_NAME': 'VERIFY_ITP_CONNECTION',
        },
        {
            'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
            'port_value': 0,
            'duration': 10
        },
        {
            'BB_NAME': 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6',
        },
        {
            'BB_NAME': 'RUN_PYTEST',
            "environment_variables":
            {
                'PYTHONPATH': r"D:\falcon\pytest\src\ipsv-ace\pysvext-pkg",
                'PYSV_PATH': r'D:\falcon\pytest\src\ipsv-ace\ipsv-pkg\ipsv\ace'
            }
        },
    ],
}

CONFIG = {
    'ip': 'ace',
#	'testcycle': 'ACE_TTLPCDH.ip_uv1.ip.ace.TTL_PCDH.QoVr1',
#	'testcycle': 'ACE_TTLPCDH.ip_uv2.ip.ace.TTL_PCDH.QoVr1',
#	'testcycle': 'ACE_TTLPCDH.ip_fv.ip.ace.TTL_PCDH.QoVr1',
#	'testcycle': 'ACE_TTLPCDH.ip_fv.ip.ace.TTL_PCDH_VVD.QoVr1',
#   'testcycle': 'ACE_TTLPCDH.ip_uv1.ip.ace.TTL_PCDH_IPC.QoVr1',
#    'testcycle': 'ACE_TTLPCDH.ip_uv2.ip.ace.TTL_PCDH_IPC.QoVr1',
#    'testcycle': 'ACE_TTLPCDH.ip_fv.ip.ace.TTL_PCDH_IPC.QoVr1',
	'testcycle': 'ACE_TTLPCDH_Gen4.ip_uv2.ip.ace.TTL_PCDH_IPC.QoVr1',
#	'testcycle': 'ACE_TTLPCDH_Gen4.ip_fv.ip.ace.TTL_PCDH_IPC.QoVr1',
#	'testcycle': 'ACE_TTLPCDH_Gen4.ip_uv2.ip.ace.TTL_PCDH_VVD.QoVr1',
#	'testcycle': 'ACE_TTLPCDH_Gen4.ip_fv.ip.ace.TTL_PCDH_VVD.QoVr1',
    'project': 'TTL',
    'environment': 'fpga',
    'val_framework': 'pytest',
    'val_environment': 'fpga',
    'manifest_args': phases,
    'hardwareclass': 'IP_ACE',
    #'hardwareclass': ['IP_GNA','HAPS80'],
    'environment_variables': {},
    'manifest_type': 'pytest',
    #'external_workarea': '/nfs/png/disks/png_coesv_disk001/',
}

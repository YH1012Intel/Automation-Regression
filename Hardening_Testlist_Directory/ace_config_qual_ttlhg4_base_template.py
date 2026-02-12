maestro_repo = {'BB_NAME': 'MAESTRO_REPO_LOCAL_NFS',
					'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/abdulla5/repo/r3/iag_maestro-repo',
				   'skip_copy': False
                  } # TODO

maestro_github_remote_side_branch = {'BB_NAME': 'MAESTRO_GITHUB_SETUP',
			            'branch': '26WW05p3_TAM_TTLHG4',
                                    }

coverage_github_setup =     {
                                'BB_NAME': 'COVERAGE_GITHUB_SETUP',
                                'database': 'coverage_ttl_ace_db',
                            }


haps_programming = {'BB_NAME': 'HAPS_PROGRAMMING',
                    # TTLH Gen 4
                    # 'BB_TAG' : "", 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-10-09-drop_5_HAPS_80_build7_upf_Vivado_par_directive_v6.2019.1/project.conf'
                    #'BB_TAG' : "25WW48_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-11-28-ace4px-drop-1_HAPS_80_build0_upf_Vivado_par_directive_v2.2019.1/project.conf'
                    #'BB_TAG' : "25WW48_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/TTL_ttl-ace-ipfpga-cth-2025-11-28-ace4px-drop-1_HAPS_80_build2_upf_Vivado_par_directive_v2.2019.1/project.conf'
                    #'BB_TAG' : "25WW50_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2025-12-12-ace4px-drop-2_HAPS_80_build0_upf_Vivado_par_directive_v2.2019.1/project.conf'
                    #'BB_TAG' : "25WW50_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2025-12-12-ace4px-drop-2_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
		    #'BB_TAG' : "25WW50_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2025-12-12-ace4px-drop-2_HAPS_80_build1_upf_Vivado_par_directive_v6.2019.1/project.conf'
                    #'BB_TAG' : "26WW05_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2026-01-21-ace4px-drop-3_HAPS_80_build0_upf_Vivado_par_directive_v6.2019.1/project.conf'
                    'BB_TAG' : "26WW05_TTLHGen4", 'ingredient_fpga_image': r'/nfs/png/disks/png_coesv_disk001/fpga_images/ACE/TTL_ttl-ace-ipfpga-cth-2026-01-21-ace4px-drop-3_HAPS_80_build0_upf_Vivado_par_directive_v6.2021.2/project.conf'
}#  TODO

sonora_fec = {
    "BB_NAME": "SONORA_FEC_PROGRAMMING",
    "ingredient_fec_sof_image_1": "/nfs/png/disks/png_coesv_disk001/Test_Card/Sonora2_enabling/SSP/230503/test_card_top_FEC1.sof",
    "ingredient_fec_sof_image_2": None,
    "ingredient_fec_sof_image_3": None,
    "ingredient_fec_sof_image_4": None, 
}

power_cycle_sut = {'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
                   'port_value': 0,
                   'duration': 10
                   }

maestro_system_discovery = {'BB_NAME': 'MAESTRO_SYSTEM_DISCOVERY',
                            'maestro_tags': 'ttlhg4.fpga.logall'
                            }

verify_fpga = {"BB_NAME": 'VERIFY_PLATFORM_CONFIG_XML',
                   "ingredient_devices": ["0x0BCD"]
                   }

fpga_perspec_maestro = { 
                        # 'acquire_ingredients': [coverage_github_setup, maestro_latest],
                        # 'acquire_ingredients': [coverage_github_setup, maestro_repo],
                        # 'acquire_ingredients': [coverage_github_setup, maestro_side_repo],
                        # 'acquire_ingredients': [coverage_github_setup, maestro_repo_local_anna_WW34],
                        # 'acquire_ingredients': [coverage_github_setup, maestro_repo_local_TTS_WW41],
                        'acquire_ingredients': [coverage_github_setup, maestro_github_remote_side_branch],
                        # 'acquire_ingredients': [coverage_github_setup, maestro_github_remote_side_branch_build0],
                        # 'acquire_ingredients': [maestro_github_remote_side_branch],
                        #'acquire_ingredients': [maestro_repo],

                        # 'system_provisioning': [haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
                        'system_provisioning': ['USB_REDIRECTOR_SHARE_DEVICES', haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML', verify_fpga],
                        # 'system_provisioning': [haps_programming, sonora_fec, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
                        # 'system_provisioning': [Turn_off_sonora3, Turn_on_sonora1_and_2, haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
                        # 'system_provisioning': [Power_cycle_sonora1, Power_cycle_sonora2, haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],

                        # 'system_discovery': [local_platform_bl],                        
                        # 'system_discovery': [maestro_system_discovery],
                        'system_discovery': [maestro_system_discovery, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],

                        # Here should have something like provisioning recovery (this should be included in system_provisioning)
                        'testline_recovery': [power_cycle_sut,'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],

                        'testline_execution': ['PERSPEC_CONTENT_GENERATION', 'MAESTRO_WORKFLOW'],
                        # 'testline_execution': [haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML', maestro_system_discovery, 'PERSPEC_CONTENT_GENERATION', 'MAESTRO_WORKFLOW'],
                        # 'testline_execution': ['MAESTRO_WORKFLOW'],
                        # 'testline_execution': ['PERSPEC_CONTENT_GENERATION', 'MAESTRO_WORKFLOW',power_cycle_sut,'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],
                        
                        'maestro_workflow_seed_recovery': [power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],
						}

CONFIG = {'ip': 'ace', 
          'project': 'TTL',
          'val_environment': 'fpga',
          'val_framework' : 'perspec_maestro',
          'hardwareclass': 'IP_ACE',
#          'hardwareclass': ['IP_GNA','HAPS80'],
          'manifest_type': 'fpga_perspec_maestro',
          'manifest_args': fpga_perspec_maestro,
#		  'testcycle': 'ACE_TTLPCDH.ip_uv1.ip.ace.TTL_PCDH_IPC.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH.ip_uv2.ip.ace.TTL_PCDH_IPC.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH.ip_fv.ip.ace.TTL_PCDH_IPC.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH.ip_fv.ip.ace.TTL_PCDH_VVD.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH_Gen4.ip_uv2.ip.ace.TTL_PCDH_IPC.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH_Gen4.ip_fv.ip.ace.TTL_PCDH_IPC.QoVr1',
		  'testcycle': 'ACE_TTLPCDH_Gen4.ip_uv2.ip.ace.TTL_PCDH_VVD.QoVr1',
#		  'testcycle': 'ACE_TTLPCDH_Gen4.ip_fv.ip.ace.TTL_PCDH_VVD.QoVr1',
#         'environment_variables': {'MAESTRO_FRAMEWORK': 'UNIFIED_ARTIFACT'},
#         'environment_variables': {'MAESTRO_FRAMEWORK': 'UNIFIED', 'DISCOVERY_SAFELIST_ACE': '1', 'DISCOVERY_SAFELIST_SONORA': '1'},
		  'environment_variables': {'MAESTRO_FRAMEWORK': 'UNIFIED', 'DISCOVERY_SAFELIST_ACE': '1', 'DISCOVERY_SAFELIST_SONORA': '1', 'ACEFW': 'DEBUG'},
#		  'environment_variables': {'MAESTRO_FRAMEWORK': 'UNIFIED', 'LM_PROJECT': 'DDG-TGL', 'DISCOVERY_SAFELIST_ACE': '1', 'DISCOVERY_SAFELIST_SONORA': '1'},
#		  'environment_variables': {'MAESTRO_FRAMEWORK': 'UNIFIED', 'LM_PROJECT': 'DDG-TGL', 'DISCOVERY_SAFELIST_ACE': '1', 'DISCOVERY_SAFELIST_SONORA': '1', 'ACEFW': 'DEBUG'},
          'setup_settings': [],
          #'external_workarea': '/nfs/png/disks/png_coesv_disk001/',
          }

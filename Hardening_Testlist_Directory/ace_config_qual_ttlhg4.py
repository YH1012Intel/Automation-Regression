maestro_repo = {'BB_NAME': 'MAESTRO_REPO_LOCAL_NFS',
                    #'ingredient_source': r'/nfs/png/stod/stod7002/w.chewyila.100/iag_maestro-repo', not working
				    #'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro3',
                    #'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro5',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro6',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro7',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro8',
					# 'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/ginhsien/maestro-github',
					#'ingredient_source': r'/nfs/png/stod/stod7002/w.ginhsien.100/maestro_lnl',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/proj_ptl/UV1',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/dhanagan/regression/maestro',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/dhanagan/testRepo/maestro',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/tino/sandbox/github_maestro_3/maestro_tino',
					#'ingredient_source': r'/nfs/png/disks/png_coesv_disk003/lkhaw/maestro',
					'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/abdulla5/repo/r3/iag_maestro-repo',
				   'skip_copy': False
                  } # TODO

maestro_repo_local_anna_WW34 = {'BB_NAME': 'MAESTRO_REPO_LOCAL_NFS',
					'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/abdulla5/repo/r2/iag_maestro-repo',
				   'skip_copy': False
                  } # TODO

maestro_repo_local_sndw_idisp = {'BB_NAME': 'MAESTRO_REPO_LOCAL_NFS',
					'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/jwee/repo/local_repo',
				   'skip_copy': False
                  } # TODO

maestro_repo_local_TTS_WW41 = {'BB_NAME': 'MAESTRO_REPO_LOCAL_NFS',
					'ingredient_source': r'/nfs/png/disks/png_coesv_disk001/users/jwee/repo/local_repo_2/frameworks.validation.maestro.maestro',
				   'skip_copy': False
                  } # TODO

maestro_latest = {'BB_NAME': 'MAESTRO_GITHUB_SETUP',
				  #'commithash': 'd66e9e74a9bf541e69199d8ee791d690cdea27a3',
                  'branch': 'integration',
                 }

maestro_repo_uhfi_dmmr_access = {'BB_NAME':'MAESTRO_REPO_CLONE_CHECKOUT_AND_BUILD',
                                'commithash': 'e794c23ca99285793ee9820ef8822962be86eb7e',
                                'branch': 'integration',
                                } 

maestro_github_remote_side_branch = {'BB_NAME': 'MAESTRO_GITHUB_SETUP',
                                    # 'commithash': '7c4e74c6c8f1a5ed226eab9f0434ab1c1a32b1cc',       # integration commit before Poey Seng merged latest artifactory fw  + 0702 b0
                                    # 'commithash': 'cdd0a8acd77e68d9b07ab26ffeae32e306d0a2ab',       # integration commit where Poey Seng merged latest artifactory fw   + 0702 b0
                                    # 'commithash': '6bf5d35e83884218b412ed4f0e881c0ba05571ad',       # latest remote side branch commit + artifactory fw                 + 0702 b0
                                    # 'commithash': 'a8176a5ae8f7ae681072feda14966801ef6baa82',       # latest remote side branch commit + Poey Seng local FW             + 0729 b2
                                    # 'commithash': '9df9065a222266a94d1e68140561d2d13ed0472b',       # latest remote side branch commit + Poey Seng local FW             + 0729 b2
                                    # 'branch': '25WW32p4_TAM_TTLH',
                                    # 'branch': '25WW36p3_TAM_TTLH',
                                    # 'branch': '25WW42p5_TAM_TTLH',
                                    # 'branch': '25WW32p4_TAM_TTLH_GNA',
                                    # 'branch': '25WW45p4_TAM_TTLH_NVLH',
                                    #'branch': '25WW49p3_TAM_TTLHG4',
                                    #'branch': 'kokheng_tts_clear_ntk',
			            'branch': '26WW05p3_TAM_TTLHG4',
                                    }

maestro_github_remote_side_branch_build0 = {'BB_NAME': 'MAESTRO_GITHUB_SETUP',
                                            'commithash': '256b5b8b88abc969ea3020b97fd06ab31236d77c',      
                                            'branch': '25WW36p3_TAM_TTLH',
                                           }



coverage_github_setup =     {
                                'BB_NAME': 'COVERAGE_GITHUB_SETUP',
                                'database': 'coverage_ttl_ace_db',
                                # 'configure_db': True,
                                # "branch": "lguntupa_falcon6_update"
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

#haps_programming = {
#                       'BB_NAME': 'EXECUTE_COMMAND',
#                       'cmd': 'cd /nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/WCL_wcl-ace-ipfpga-cth-2023-06-19_422_HAPS_80_build5_upf_Vivado_par_directive_v2.2021.2;/p/ppa/farm/CAD_ROOT/synopsys/confpro/O-2018.09-2/bin/confprosh wcl_run.tcl',
#                       'cmd': 'cd /nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/WCL_wcl-ace-ipfpga-cth-2023-06-19_422_HAPS_80_build7_upf_Vivado_par_directive_v6.2021.2;/p/ppa/farm/CAD_ROOT/synopsys/confpro/O-2018.09-2/bin/confprosh wcl_run.tcl',
#                       'cmd': 'cd /nfs/png/disks/png_viceipr_disk001/falcon_ingredients/staging/ACE/fpga_image/WCL_wcl-ace-ipfpga-cth-2023-08-02_HAPS_80_build1_upf_Vivado_par_directive_v6.2019.1;/p/ppa/farm/CAD_ROOT/synopsys/confpro/O-2018.09-2/bin/confprosh wcl_run.tcl',
#                       'os': 'linux',
#                       'timeout': 180,
#                   }

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
#duration 10sec
#port 0

maestro_system_discovery = {'BB_NAME': 'MAESTRO_SYSTEM_DISCOVERY',
                            # 'maestro_tags': 'fcl.fpga.logall'
                            # 'maestro_tags': 'ttlh.fpga.logall'
                            'maestro_tags': 'ttlhg4.fpga.logall'
                            #'maestro_tags': 'ttlhg4.fpga'
                            }

local_platform_bl = { 'BB_NAME': 'PLATFORM_BL_TO_CSV',
                    #"ingredient_platform_bl": r'/nfs/png/disks/png_coesv_disk001/users/dhanagan/plat/ci/lnl613/Platform.bl',
                    "ingredient_platform_bl": r'/nfs/png/disks/png_coesv_disk001/users/chewyi/Platform_bling/CI/wcl/23112023/Platform.bl'
                }

reset_itp_connection = {

                        "BB_NAME": "RESET_ITP_CONNECTION"

                        }

#=====================================================================================================================#

gna_postprocess_ibi = {'BB_NAME': 'IP_CP_POST_PROCESS',
                    'ip_script': r'/nfs/png/disks/png_coesv_disk001/users/abdulla5/CI/Falcon4/Coverage/gna_postprocess_ibi_v2.py',
                    'post_process_args': ['-l <logfolder_basepath>'],
                    'table_name': 'IPG_VICE_IPSV_COVERAGE_GNA'
                    }

gna_kibana = {'BB_NAME': 'UPLOAD_KIBANA',
                    'ip_index_path': r'/nfs/png/disks/png_viceipr_disk001/users/mabdulk1/config/gna/index_template.csv'
                    }

#=====================================================================================================================#

Turn_off_sonora3 = {'BB_NAME': 'POWER_SPLITTER_PORT_POWER_OFF',
					'port_value': 1,   
					#Turn off (sonora3)
					}
					
Turn_on_sonora1_and_2 = {'BB_NAME': 'POWER_SPLITTER_PORT_POWER_ON',
						 'port_value': 2,
						 # Turn On (Sonora1& Sonora2)
						 }

Power_cycle_sonora1 = {'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
						'port_value': 1,
						'duration': 5
					}

Power_cycle_sonora2 = {'BB_NAME': 'POWER_SPLITTER_PORT_POWER_CYCLE',
						'port_value': 2,
						'duration': 5
						}

verify_fpga = {"BB_NAME": 'VERIFY_PLATFORM_CONFIG_XML',
                   "ingredient_devices": ["0x0BCD"]
                   }

#=====================================================================================================================#

# fpga_perspec_maestro = {#'acquire_ingredients': [coverage_point, maestro_latest],
			# #'acquire_ingredients': [coverage_point, maestro_repo],
			# 'acquire_ingredients': [coverage_point, maestro_side_repo],
			# #'acquire_ingredients': [maestro_github_remote_side_branch],
			# 'testline_recovery': [power_cycle_sut,'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],
                        # 'maestro_workflow_seed_recovery': [power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],
			# #'system_provisioning': [haps_programming, sonora_fec, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
			# 'system_provisioning': [haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
                        # #'system_provisioning': [Turn_off_sonora3, Turn_on_sonora1_and_2, haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
			# #'system_provisioning': [Power_cycle_sonora1, Power_cycle_sonora2, haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML'],
			# #'system_discovery': [local_platform_bl],
                        # 'system_discovery': [maestro_system_discovery],
                        # 'testline_execution': ['PERSPEC_CONTENT_GENERATION', 'MAESTRO_WORKFLOW'],
			# #'testline_execution': [haps_programming, power_cycle_sut, 'BLOCKING_SUT_UNTIL_BOOT_INTO_F6', 'GENERATE_PLATFORM_CONFIG_XML', maestro_system_discovery, 'PERSPEC_CONTENT_GENERATION', 'MAESTRO_WORKFLOW'],
		         # 'testline_recovery': [power_cycle_sut,'BLOCKING_SUT_UNTIL_BOOT_INTO_F6'],
                        # #'testline_execution': ['MAESTRO_WORKFLOW']						  
						# }

#=====================================================================================================================#

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

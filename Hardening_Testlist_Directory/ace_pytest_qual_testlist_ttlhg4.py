namenodes_arg = "--pysv_config=ttlhg4"

################################################ BIU Tests ################################################
test_receive_qos_rsp = {
    'job': 'test_receive_qos_rsp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_receive_qos_rsp',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_receive_qos_rsp_0 = {
    'job': 'test_receive_qos_rsp_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_receive_qos_rsp',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_receive_qos_rsp_1 = {
    'job': 'test_receive_qos_rsp_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_receive_qos_rsp',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_cw_return_credit_fw_not_ack = {
    'job': 'test_cw_return_credit_fw_not_ack',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_cw_return_credit_fw_not_ack',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_send_nonposted = {
    'job': 'test_send_nonposted',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_send_nonposted',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_ltr = {
    'job': 'test_ltr',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_ltr',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_send_posted = {
    'job': 'test_send_posted',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_send_posted',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_send_qos_dmd = {
    'job': 'test_send_qos_dmd',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_send_qos_dmd',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_sb_msg_injection = {
    'job': 'test_stress_sb_msg_injection',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_sb_msg_injection',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_multiple_in_non_posted_completion = {
    'job': 'test_stress_multiple_in_non_posted_completion',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_multiple_in_non_posted_completion',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_multiple_in_posted_completion = {
    'job': 'test_stress_multiple_in_posted_completion',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_multiple_in_posted_completion',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_multiple_in_posted_non_posted = {
    'job': 'test_stress_multiple_in_posted_non_posted',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_multiple_in_posted_non_posted',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_multiple_out_non_posted_completion = {
    'job': 'test_stress_multiple_out_non_posted_completion',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_multiple_out_non_posted_completion',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_stress_multiple_out_posted_completion = {
    'job': 'test_stress_multiple_out_posted_completion',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_qos_sb_msg.py::TestQosSbMessaging::test_stress_multiple_out_posted_completion',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_hda_sdi_intx_interrupt = {
    'job': 'test_hda_sdi_intx_interrupt',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_intx_interrupt.py::TestIntxInterrupt::test_hda_sdi_intx_interrupt',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_msi_interrupt = {
    'job': 'test_msi_interrupt',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_msi_interrupt::TestMsiInterrupt',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}



################################################ Register Tests ################################################

test_pcie_config_space = {
    'job': 'test_pcie_config_space',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_pcie_config_space.py::TestPcieConfigSpace::test_pcie_config_space',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}

test_register_bar0_shadow_bar2 = {
    'job': 'test_register_bar0_shadow_bar2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_bar0_shadow_bar2.py::TestRegisterBar0ShadowBar2::test_register_bar0_shadow_bar2',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 1000,
        },
    ]
}

test_dmmr_attribute = {
    'job': 'test_dmmr_attribute',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_attribute.py::TestRegisterAttribute::test_dmmr_attribute',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 9000,
        },
    ]
}

test_dmmr_def_value = {
    'job': 'test_dmmr_def_value',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_default_value.py::TestRegisterDefaultValue::test_dmmr_def_value',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 2000,
        },
    ]
}
    
test_dmmr_def_value_0 = {
    'job': 'test_dmmr_def_value_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_default_value.py::TestRegisterDefaultValue::test_dmmr_def_value',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 2000,
        },
    ]
}

test_dmmr_def_value_1 = {
    'job': 'test_dmmr_def_value_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_default_value.py::TestRegisterDefaultValue::test_dmmr_def_value',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 2000,
        },
    ]
}

test_dmmr_register_reset = {
    'job': 'test_dmmr_register_reset',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_0 = {
    'job': 'test_dmmr_register_reset_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_1 = {
    'job': 'test_dmmr_register_reset_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_2 = {
    'job': 'test_dmmr_register_reset_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_3 = {
    'job': 'test_dmmr_register_reset_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_4 = {
    'job': 'test_dmmr_register_reset_4',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dmmr_register_reset_pltrst = {
    'job': 'test_dmmr_register_reset_pltrst',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset[\'pltrst\']',
            #'content_path': r"ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset['pltrst']",
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 14400,
        },
    ]
}

test_dmmr_register_reset_wrsm = {
    'job': 'test_dmmr_register_reset_wrsm',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset[\'wrsm\']',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 14400,
        },
    ]
}

test_dmmr_register_reset_crst = {
    'job': 'test_dmmr_register_reset_crst',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset[\'crst\']',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 14400,
        },
    ]
}

test_dmmr_register_reset_dsplrst = {
    'job': 'test_dmmr_register_reset_dsplrst',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset[\'dsplrst\']',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 14400,
        },
    ]
}

test_dmmr_register_reset_flr = {
    'job': 'test_dmmr_register_reset_flr',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dmmr_register_reset[\'flr\']',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 14400,
        },
    ]
}

test_dsp_register_reset = {
    'job': 'test_dsp_register_reset',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset.py::TestRegisterReset::test_dsp_register_reset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dsp_attribute_0 = {
    'job': 'test_dsp_attribute_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_attribute.py::TestRegisterAttribute::test_dsp_attribute',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dsp_attribute_1 = {
    'job': 'test_dsp_attribute_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_attribute.py::TestRegisterAttribute::test_dsp_attribute',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_dsp_attribute_2 = {
    'job': 'test_dsp_attribute_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_attribute.py::TestRegisterAttribute::test_dsp_attribute',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}
 
test_dsp_attribute_3 = {
    'job': 'test_dsp_attribute_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_attribute.py::TestRegisterAttribute::test_dsp_attribute',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 61200,
        },
    ]
}

test_sweep_through_hmmr = {
    'job': 'test_sweep_through_hmmr',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_sweep_through.py::TestSweepThrough::test_sweep_through_hmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_sweep_through_dmmr = {
    'job': 'test_sweep_through_dmmr',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_sweep_through.py::TestSweepThrough::test_sweep_through_dmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_reset_isolation_gated_io_0_complete = {
    'job': 'test_reset_isolation_gated_io_0_complete',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset_isolation.py::TestResetIsolation::test_reset_isolation_gated_io_0_complete',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_reset_isolation_gated_io_1_complete = {
    'job': 'test_reset_isolation_gated_io_1_complete',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_reset_isolation.py::TestResetIsolation::test_reset_isolation_gated_io_1_complete',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_dspx_gated_register_access = {
    'job': 'test_dspx_gated_register_access',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_dspx_access.py::TestRegAccessPG::test_dspx_gated_register_access',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_hst = {
    'job': 'test_hst',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_hst_access.py::TestRegAccessPG::test_hst',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_hub_hp = {
    'job': 'test_hub_hp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_hub_hp_access.py::TestRegAccessPG::test_hub_hp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_io0_gated_register_access = {
    'job': 'test_io0_gated_register_access',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_iox_access.py::TestRegAccessPG::test_io0_gated_register_access',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_io1_gated_register_access = {
    'job': 'test_io1_gated_register_access',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_iox_access.py::TestRegAccessPG::test_io1_gated_register_access',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_mlx_access = {
    'job': 'test_gated_mlx_access',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_mlx_access.py::TestRegAccessPG::test_ml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ml = {
    'job': 'test_ml',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_mlx_access.py::TestRegAccessPG::test_ml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ml_0 = {
    'job': 'test_ml_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_mlx_access.py::TestRegAccessPG::test_ml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ml_1 = {
    'job': 'test_ml_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_gated_mlx_access.py::TestRegAccessPG::test_ml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_dspx = {
    'job': 'test_gated_dspx',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_dspx',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_0_i2s = {
    'job': 'test_gated_io_0_i2s',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_0_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_0_i2s_0 = {
    'job': 'test_gated_io_0_i2s_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_0_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_0_i2s_1 = {
    'job': 'test_gated_io_0_i2s_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_0_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_1_sndw = {
    'job': 'test_gated_io_1_sndw',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_1_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_1_sndw_0 = {
    'job': 'test_gated_io_1_sndw_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_1_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_gated_io_1_sndw_1 = {
    'job': 'test_gated_io_1_sndw_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_pg_access_test\test_pgd_reset.py::TestPgdReset::test_gated_io_1_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_offload_dmic= {
    'job': 'test_offload_dmic',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_dmic',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_dmic_0 = {
    'job': 'test_offload_dmic_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_dmic',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_dmic_1 = {
    'job': 'test_offload_dmic_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_dmic',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}


test_offload_dmic_2 = {
    'job': 'test_offload_dmic_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_dmic',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_dmic_2 = {
    'job': 'test_offload_dmic_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_dmic',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_hda = {
    'job': 'test_offload_hda',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_hda',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_hda_0 = {
    'job': 'test_offload_hda_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_hda',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_hda_1 = {
    'job': 'test_offload_hda_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_hda',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_idisp = {
    'job': 'test_offload_idisp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_idisp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_idisp_0 = {
    'job': 'test_offload_idisp_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_idisp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_idisp_1 = {
    'job': 'test_offload_idisp_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_idisp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_sndw = {
    'job': 'test_offload_sndw',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 18600,
        },
    ]
}

test_offload_sndw_0 = {
    'job': 'test_offload_sndw_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 18600,
        },
    ]
}

test_offload_sndw_1 = {
    'job': 'test_offload_sndw_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_sndw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 18600,
        },
    ]
}

test_offload_i2s = {
    'job': 'test_offload_i2s',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_i2s_0 = {
    'job': 'test_offload_i2s_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_i2s_1 = {
    'job': 'test_offload_i2s_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_i2s',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7800,
        },
    ]
}

test_offload_uaol = {
    'job': 'test_offload_uaol',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_uaol',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_offload_uaol_0 = {
    'job': 'test_offload_uaol_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_uaol',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_offload_uaol_1 = {
    'job': 'test_offload_uaol_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_offload_uaol',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_ownership_dspc = {
    'job': 'test_ownership_dspc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_dspc',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_dspc_0 = {
    'job': 'test_ownership_dspc_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_dspc',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_mdiv = {
    'job': 'test_ownership_mdiv',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_mdiv',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_mdiv_0 = {
    'job': 'test_ownership_mdiv_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_mdiv',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_aonml= {
    'job': 'test_ownership_aonml',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_aonml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}


test_ownership_aonml_0 = {
    'job': 'test_ownership_aonml_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_aonml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_dspc_1 = {
    'job': 'test_ownership_dspc_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_dspc',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_mdiv_1 = {
    'job': 'test_ownership_mdiv_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_mdiv',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_aonml_1 = {
    'job': 'test_ownership_aonml_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_aonml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_dspc_2 = {
    'job': 'test_ownership_dspc_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_dspc',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_mdiv_2 = {
    'job': 'test_ownership_mdiv_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_mdiv',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_ownership_aonml_2 = {
    'job': 'test_ownership_aonml_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_ownership.py::TestRegisterOwnership::test_ownership_aonml',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_ACPSAI = {
    'job': 'test_register_SAI_ACPSAI',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_ACPSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_ACPSAI_0 = {
    'job': 'test_register_SAI_ACPSAI_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_ACPSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_ACPSAI_1 = {
    'job': 'test_register_SAI_ACPSAI_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_ACPSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWLDSAI = {
    'job': 'test_register_SAI_FWLDSAI',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWLDSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWLDSAI_0 = {
    'job': 'test_register_SAI_FWLDSAI_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWLDSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWLDSAI_1 = {
    'job': 'test_register_SAI_FWLDSAI_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWLDSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWVFSAI_0 = {
    'job': 'test_register_SAI_FWVFSAI_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWVFSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWVFSAI = {
    'job': 'test_register_SAI_FWVFSAI',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWVFSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_FWVFSAI_1 = {
    'job': 'test_register_SAI_FWVFSAI_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_FWVFSAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_IPCSASAI_0 = {
    'job': 'test_register_SAI_IPCSASAI_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_IPCSASAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_IPCSASAI_1 = {
    'job': 'test_register_SAI_IPCSASAI_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_IPCSASAI',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_THSTSAI_dmmr_0 = {
    'job': 'test_register_SAI_THSTSAI_dmmr_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_THSTSAI_dmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 10800,
        },
    ]
}

test_register_SAI_THSTSAI_dmmr_1 = {
    'job': 'test_register_SAI_THSTSAI_dmmr_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_THSTSAI_dmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 10800,
        },
    ]
}

test_register_SAI_THSTSAI_hmmr_0 = {
    'job': 'test_register_SAI_THSTSAI_hmmr_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_THSTSAI_hmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_THSTSAI_hmmr_1 = {
    'job': 'test_register_SAI_THSTSAI_hmmr_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_THSTSAI_hmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_dmmr_0 = {
    'job': 'test_register_SAI_UHSTSAI_dmmr_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_dmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_dmmr_1 = {
    'job': 'test_register_SAI_UHSTSAI_dmmr_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_dmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_hcfg_0 = {
    'job': 'test_register_SAI_UHSTSAI_hcfg_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_hcfg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_hcfg_1 = {
    'job': 'test_register_SAI_UHSTSAI_hcfg_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_hcfg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_hmmr_0 = {
    'job': 'test_register_SAI_UHSTSAI_hmmr_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_hmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_register_SAI_UHSTSAI_hmmr_1 = {
    'job': 'test_register_SAI_UHSTSAI_hmmr_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_UHSTSAI_hmmr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

################################################ Security Tests ################################################

test_l2uncache_host_mrp_1 = {
    'job': 'test_l2uncache_host_mrp_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_memory_region_protection.py::TestMemoryProtection::test_l2uncache_host_mrp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_l2uncache_host_mrp_2 = {
    'job': 'test_l2uncache_host_mrp_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_memory_region_protection.py::TestMemoryProtection::test_l2uncache_host_mrp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_l2uncache_host_mrp_3 = {
    'job': 'test_l2uncache_host_mrp_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_memory_region_protection.py::TestMemoryProtection::test_l2uncache_host_mrp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_hpsram_mrp = {
    'job': 'test_hpsram_mrp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_memory_region_protection.py::TestMemoryProtection::test_hpsram_mrp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_ulpsram_mrp = {
    'job': 'test_ulpsram_mrp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_memory_region_protection.py::TestMemoryProtection::test_ulpsram_mrp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_l2hpsramtlb_lock = {
    'job': 'test_l2hpsramtlb_lock',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_tlbx_lock_check.py::TestTlbxLock::test_l2hpsramtlb_lock',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}



test_l2uc_tlb_retention = {
    'job': 'test_l2uc_tlb_retention',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_l2uncache_tlb_retention.py::test_l2uc_tlb_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}


####################################### SIIP Tests ################################################

#insert siip test here
test_acepll_own_req_clkctl = {
    'job': 'test_acepll_own_req_clkctl',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_acepll_own_req.py::TestACEPLLOwnReq::test_acepll_own_req_clkctl',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_acepll_own_req_dmic = {
    'job': 'test_acepll_own_req_dmic',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_acepll_own_req.py::TestACEPLLOwnReq::test_acepll_own_req_dmic',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_acepll_own_req_ssp = {
    'job': 'test_acepll_own_req_ssp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_acepll_own_req.py::TestACEPLLOwnReq::test_acepll_own_req_ssp',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_dmic_apll_own_req_violation = {
    'job': 'test_dmic_apll_own_req_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_dmic_apll_own_req_violation',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_ssp_apll_own_req_violation = {
    'job': 'test_ssp_apll_own_req_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_ssp_apll_own_req_violation',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_clkctl_apll_own_req = {
    'job': 'test_clkctl_apll_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_clkctl_apll_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_crstb_apll_own_req = {
    'job': 'test_crstb_apll_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_crstb_apll_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_dmic_apll_own_req = {
    'job': 'test_dmic_apll_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_dmic_apll_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_ssp_apll_own_req = {
    'job': 'test_ssp_apll_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_apll_own_req.py::TestApllOwnReq::test_ssp_apll_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_ddr_nonsnoop_own_req = {
    'job': 'test_ddr_nonsnoop_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_ddr_own_req.py::TestDdrOwnReq::test_ddr_nonsnoop_own_req',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_ddr_snoop_own_req = {
    'job': 'test_ddr_snoop_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_ddr_own_req.py::TestDdrOwnReq::test_ddr_snoop_own_req',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_ddr_own_req = {
    'job': 'test_spsreq_ddr_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_ddr_own_req',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_neg_spsreq_dtf_own_req = {
    'job': 'test_neg_spsreq_dtf_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_spsreq_dtf_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_spsreq_sbp_own_req = {
    'job': 'test_neg_spsreq_sbp_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_spsreq_sbp_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_spsreq_vnn_own_req = {
    'job': 'test_neg_spsreq_vnn_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_spsreq_vnn_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_dtf_own_req_0 = {
    'job': 'test_neg_dtf_own_req_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_dtf_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_dtf_own_req_1 = {
    'job': 'test_neg_dtf_own_req_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_dtf_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_corb_rirb_psf_ownack = {
    'job': 'test_neg_corb_rirb_psf_ownack',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_corb_rirb_psf_ownack',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_neg_spsreq_prim_own_req = {
    'job': 'test_neg_spsreq_prim_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_siip2p2_opti.py::TestChassis2p2::test_neg_spsreq_prim_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_dtf_own_req = {
    'job': 'test_spsreq_dtf_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_dtf_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}


test_spsreq_prim_own_req = {
    'job': 'test_spsreq_prim_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_prim_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_side_own_req = {
    'job': 'test_spsreq_side_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_side_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_sbp_own_req = {
    'job': 'test_spsreq_sbp_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_sbp_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_vnn_own_req = {
    'job': 'test_spsreq_vnn_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_vnn_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_spsreq_xhci_own_req = {
    'job': 'test_spsreq_xhci_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_spsreq_request_own_req.py::TestSpsreq::test_spsreq_xhci_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_dtf_own_req = {
    'job': 'test_dtf_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_dtf_own_req.py::TestDtfOwnReq::test_dtf_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_dtf_own_req_violation = {
    'job': 'test_dtf_own_req_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_dtf_own_req.py::TestDtfOwnReq::test_dtf_own_req_violation',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_compulsory_cycle_0 = {
    'job': 'test_sbp_own_req_compulsory_cycle_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_compulsory_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_compulsory_cycle_1 = {
    'job': 'test_sbp_own_req_compulsory_cycle_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_compulsory_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_compulsory_cycle_2 = {
    'job': 'test_sbp_own_req_compulsory_cycle_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_compulsory_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_voluntary_cycle_0 = {
    'job': 'test_sbp_own_req_voluntary_cycle_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_voluntary_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_voluntary_cycle_1 = {
    'job': 'test_sbp_own_req_voluntary_cycle_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_voluntary_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_sbp_own_req_reset_cycle = {
    'job': 'test_sbp_own_req_reset_cycle',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_sbp_own_req.py::TestSbpOwnReq::test_sbp_own_req_reset_cycle',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 2000,
        },
    ]
}

test_clkctl_prim_own_req = {
    'job': 'test_clkctl_prim_own_req',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_clkctl_prim_own_req',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_clkctl_prim_own_req_dsp_iosfpc = {
    'job': 'test_clkctl_prim_own_req_dsp_iosfpc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_clkctl_prim_own_req_dsp_iosfpc',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_corb_rirb_prim_clkack_violation = {
    'job': 'test_corb_rirb_prim_clkack_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\hda_test\test_hda_cmd_resp.py::TestCmdResp::test_corb_rirb_prim_clkack_violation',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 1800,
        },
    ]
}

test_prim_own_req_hst_pgd_wake = {
    'job': 'test_prim_own_req_hst_pgd_wake',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_own_req_hst_pgd_wake',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_prim_voluntary_imr_0 = {
    'job': 'test_prim_voluntary_imr_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_voluntary_imr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_l2uncache_ack_violation = {
    'job': 'test_l2uncache_ack_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_l2uncache_ack_violation',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_corb_rirb_psf_ownack_violation = {
    'job': 'test_corb_rirb_psf_ownack_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\hda_test\test_hda_cmd_resp.py::TestCmdResp::test_corb_rirb_psf_ownack_violation',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_prim_voluntary_imr_1 = {
    'job': 'test_prim_voluntary_imr_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_voluntary_imr',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_prim_voluntary_l2uncache = {
    'job': 'test_prim_voluntary_l2uncache',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_voluntary_l2uncache',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_prim_own_req_msi_interrupt_0 = {
    'job': 'test_prim_own_req_msi_interrupt_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_own_req_msi_interrupt',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_prim_own_req_msi_interrupt_1 = {
    'job': 'test_prim_own_req_msi_interrupt_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_prim_own_req_msi_interrupt',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_vnn_voluntary_l2uncache = {
    'job': 'test_vnn_voluntary_l2uncache',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_vnn_voluntary_l2uncache',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_imr_ack_violation = {
    'job': 'test_imr_ack_violation',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\siip_test\test_prim_related_own_req.py::TestPrimRelatedOwnReq::test_imr_ack_violation',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}



################################################ SNDW Tests ################################################


test_sndw_coupled_instream_bankswitch = {
    'job': 'test_sndw_coupled_instream_bankswitch',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw_stream_bank_switch.py::TestSndwInBankSwitch::test_sndw_coupled_instream_bankswitch',
            'pytest_args': "-sv",
            'timeout': 300,
        },
    ]
}




test_sndw_coupled_loopback_stream_cmdrsp_conc = {
    'job': 'test_sndw_coupled_loopback_stream_cmdrsp_conc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw_coupled_loopback.py::TestSndwLoopbackStream::test_sndw_coupled_loopback_stream_cmdrsp_conc',
            'pytest_args': "-sv",
            'timeout': 1500,
        },
    ]
}
test_pdi_corbrirb_conc = {
    'job': 'test_pdi_corbrirb_conc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw_coupled_out.py::TestSndwOut::test_pdi_corbrirb_conc',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_sndw_clock_stop_pme_wake = {
    'job': 'test_sndw_clock_stop_pme_wake',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_clock_stop_pme_wake',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_sndw_two_slave_enumeration = {
    'job': 'test_sndw_two_slave_enumeration',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_two_slave_enumeration',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_slave_status_changes = {
    'job': 'test_sndw_slave_status_changes',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_slave_status_changes',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_slave_status_changes_0 = {
    'job': 'test_sndw_slave_status_changes_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_slave_status_changes',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_slave_status_changes_1 = {
    'job': 'test_sndw_slave_status_changes_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_slave_status_changes',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_data_port_control = {
    'job': 'test_sndw_data_port_control',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_data_port_control',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}
test_ace2px_sndw_allseg_hda_corb_rirb = {
    'job': 'test_ace2px_sndw_allseg_hda_corb_rirb',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_ace2px_sndw_allseg_hda_corb_rirb',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_ace2px_sndw_allseg_hda_corb_rirb_0 = {
    'job': 'test_ace2px_sndw_allseg_hda_corb_rirb_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_ace2px_sndw_allseg_hda_corb_rirb',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_ace2px_sndw_allseg_hda_corb_rirb_1 = {
    'job': 'test_ace2px_sndw_allseg_hda_corb_rirb_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_ace2px_sndw_allseg_hda_corb_rirb',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_sndw_legacypio_HdaSndwIcir = {
    'job': 'test_sndw_legacypio_HdaSndwIcir',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_legacypio_HdaSndwIcir',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

test_ace2px_sndw_hda_corb_rirb_gsync = {
    'job': 'test_ace2px_sndw_hda_corb_rirb_gsync',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_ace2px_sndw_hda_corb_rirb_gsync',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 180,
        },
    ]
}

################################################ SNDW IDISP Tests ################################################
test_sndw_idisp_async_wake = {
    'job': 'test_sndw_idisp_async_wake',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_async_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_async_wake_0 = {
    'job': 'test_sndw_idisp_async_wake_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_async_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_async_wake_1 = {
    'job': 'test_sndw_idisp_async_wake_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_async_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_pme_wake = {
    'job': 'test_sndw_idisp_clock_stop_pme_wake',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_pme_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_pme_wake_0 = {
    'job': 'test_sndw_idisp_clock_stop_pme_wake_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_pme_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_pme_wake_1 = {
    'job': 'test_sndw_idisp_clock_stop_pme_wake_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_pme_wake',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_slave_enum = {
    'job': 'test_sndw_idisp_clock_stop_slave_enum',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_slave_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_slave_enum_0 = {
    'job': 'test_sndw_idisp_clock_stop_slave_enum_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_slave_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_clock_stop_slave_enum_1 = {
    'job': 'test_sndw_idisp_clock_stop_slave_enum_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_clock_stop_slave_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}
test_sndw_idisp_slave_status_changes = {
    'job': 'test_sndw_idisp_slave_status_changes',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_slave_status_changes',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}
test_sndw_idisp_slave_status_changes_0 = {
    'job': 'test_sndw_idisp_slave_status_changes_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_slave_status_changes',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_idisp_slave_status_changes_1 = {
    'job': 'test_sndw_idisp_slave_status_changes_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_slave_status_changes',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 500,
        },
    ]
}

test_sndw_idisp_enum = {
    'job': 'test_sndw_idisp_enum',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_sndw_idisp_enum_0 = {
    'job': 'test_sndw_idisp_enum_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_sndw_idisp_enum_1 = {
    'job': 'test_sndw_idisp_enum_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_idisp_enum',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}


### HDA
test_walclk_warp_around = {
    'job': 'test_walclk_warp_around',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\hda_test\test_walclk_lwalfcx.py::TestWallClock::test_walclk_warp_around',
            'pytest_args': namenodes_arg + " -sv",
            # 'timeout': 180,
			'timeout': 700,
        },
    ]
}


################################################  PM  ################################################
test_prevent_power_gating_dsp_core_boot_ctrl = {
    'job': 'test_prevent_power_gating_dsp_core_boot_ctrl',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_gated_dsphpx.py::TestGatedDsphpx::test_prevent_power_gating_dsp_core_boot_ctrl',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d0i3_cycling = {
    'job': 'test_stress_d0i3_cycling',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d3_cycling = {
    'job': 'test_stress_d3_cycling',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d3_cycling',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 1800,
        },
    ]
}

test_fiq_irq_dmac = {
    'job': 'test_fiq_irq_dmac',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_fiq_irq.py::TestFiqIrqPowerGating::test_fiq_irq_dmac',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

test_force_power_gating_lctl_io1 = {
    'job': 'test_force_power_gating_lctl_io1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_gated_iox.py::TestGatedIox::test_force_power_gating_lctl_io1',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 3600,
        },
    ]
}

test_force_power_gating_lctl_io0 = {
    'job': 'test_force_power_gating_lctl_io0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_gated_iox.py::TestGatedIox::test_force_power_gating_lctl_io0',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 3600,
        },
    ]
}

test_l1cache = {
    'job': 'test_l1cache',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l1cache_test\test_l1cache_pge.py::test_l1cache',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 3600,
        },
    ]
}

test_l2_ulp_sram_retention = {
    'job': 'test_l2_ulp_sram_retention',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2ulpsram_pg_test\test_l2ulppg.py::TestL2UlpSram::test_l2_ulp_sram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 8000,
        },
    ]
}

test_l2_ulp_sram_retention_0 = {
    'job': 'test_l2_ulp_sram_retention_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2ulpsram_pg_test\test_l2ulppg.py::TestL2UlpSram::test_l2_ulp_sram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 8000,
        },
    ]
}

test_l2_ulp_sram_retention_1 = {
    'job': 'test_l2_ulp_sram_retention_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2ulpsram_pg_test\test_l2ulppg.py::TestL2UlpSram::test_l2_ulp_sram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 8000,
        },
    ]
}

test_l2_ulp_sram = {
    'job': 'test_l2_ulp_sram',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2ulpsram_pg_test\test_l2ulppg.py::TestL2UlpSram::test_l2_ulp_sram',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

test_l2hpsram_retention = {
    'job': 'test_l2hpsram_retention',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 10000,
        },
    ]
}

test_l2hpsram_retention_0 = {
    'job': 'test_l2hpsram_retention_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 10000,
        },
    ]
}

test_l2hpsram_retention_1 = {
    'job': 'test_l2hpsram_retention_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 10000,
        },
    ]
}

test_l2hpsram_pg = {
    'job': 'test_l2hpsram_pg',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_pg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2hpsram_pg_0 = {
    'job': 'test_l2hpsram_pg_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_pg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2hpsram_pg_1 = {
    'job': 'test_l2hpsram_pg_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_pg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

#####
##### WCL PM #####
#####

test_adsp_core_pm_3 = {
    'job': 'test_adsp_core_pm_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_dsp_core_power_gate_individually.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 4200,
        },
    ]
}

test_dsp_core_power_gate_individually = {
    'job': 'test_dsp_core_power_gate_individually',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_dsp_core_power_gate_individually.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 4200,
        },
    ]
}

#test_fiq_irq_dmac = {
#    'job': 'test_fiq_irq_dmac',
#    'type': 'pytest',
#    'args': [
#        {
#            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_fiq_irq.py::TestFiqIrqPowerGating::test_fiq_irq_dmac',
#            'pytest_args': namenodes_arg + " -sv",
#            'timeout': 6000,
#        },
#    ]
#}

#ace.controller.power_on_off_dsp_core(1)
power_on_off_dsp_core_0 = {
    'job': 'power_on_off_dsp_core_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\libs\drivers\controller.py::COMMONCONTROLLERlib::power_on_off_dsp_core',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

#ace.controller.power_on_off_dsp_core(1)
power_on_off_dsp_core_1 = {
    'job': 'power_on_off_dsp_core_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\libs\drivers\controller.py::COMMONCONTROLLERlib::power_on_off_dsp_core',
			#D:\ace_python_repo\User\Tam\pythonrepo\src\
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

#ace.pm.d0i3_entry_with_dsp_subsystem_off
d0i3_entry_with_dsp_subsystem_off_0 = {
    'job': 'd0i3_entry_with_dsp_subsystem_off_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\libs\drivers\pm.py::COMMONPMlib::d0i3_entry_with_dsp_subsystem_off',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

#ace.pm.d0i3_entry_with_dsp_subsystem_off
d0i3_entry_with_dsp_subsystem_off_1 = {
    'job': 'd0i3_entry_with_dsp_subsystem_off_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\libs\drivers\pm.py::COMMONPMlib::d0i3_entry_with_dsp_subsystem_off',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}


test_stress_d0i3_cycling_0 = {
    'job': 'test_stress_d0i3_cycling_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d0i3_cycling_1 = {
    'job': 'test_stress_d0i3_cycling_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d0i3_cycling_2 = {
    'job': 'test_stress_d0i3_cycling_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d0i3_cycling_3 = {
    'job': 'test_stress_d0i3_cycling_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d0i3_cycling_4 = {
    'job': 'test_stress_d0i3_cycling_4',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d0i3_cycling',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 1000,
        },
    ]
}

test_stress_d3_cycling_0 = {
    'job': 'test_stress_d3_cycling_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d3_cycling',
            #'pytest_args': "-sv",          ## NVLH having xtocd issue for this test. After Shih Wei checked, seems like no need xtocd as didn't touch dsp side.
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 1800,
        },
    ]
}

test_stress_d3_cycling_1 = {
    'job': 'test_stress_d3_cycling_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_d3_stress.py::TestD3::test_stress_d3_cycling',
            #'pytest_args': "-sv",          ## NVLH having xtocd issue for this test. After Shih Wei checked, seems like no need xtocd as didn't touch dsp side.
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 1800,
        },
    ]
}

#Need to clarify with DingShen
#test_hda_sdi_intx_interrupt_d0i3, test_sndw_clock_stop_wake_d0i3_interrupt
#HDA: /pytest/biu_test/test_intx_interrupt.py::test_hda_sdi_intx_interrupt_d0i3
#SNDW: /pytest/sndw_test/test_sndw.py::test_sndw_clock_stop_wake_d0i3_interrupt
test_hda_sdi_intx_interrupt_d0i3 = {
    'job': 'test_hda_sdi_intx_interrupt_d0i3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\biu_test\test_intx_interrupt.py::TestIntxInterrupt::test_hda_sdi_intx_interrupt_d0i3',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}
test_sndw_clock_stop_wake_d0i3_interrupt = {
    'job': 'test_sndw_clock_stop_wake_d0i3_interrupt',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sndw_test\test_sndw.py::TestSndw::test_sndw_clock_stop_wake_d0i3_interrupt',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

### (8) WDT ############################################################################################################
test_wdt_interrupt_host = {
    'job': 'test_wdt_interrupt_host',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_host',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_interrupt_dsp = {
    'job': 'test_wdt_interrupt_dsp',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_dsp',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_interrupt = {
    'job': 'test_wdt_interrupt',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
  ]
}

test_wdt_pause = {
    'job': 'test_wdt_pause',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_pause',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_reset = {
    'job': 'test_wdt_reset',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_reset',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_store = {
    'job': 'test_wdt_store',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_store',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_eoi_clear = {
    'job': 'test_wdt_eoi_clear',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_eoi_clear',
            'pytest_args': namenodes_arg + " --autoxtocd=yes -sv",
            'timeout': 900,
        },
    ]
}

test_wdt_timer_reset = {
    'job': 'test_wdt_timer_reset',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_timer_reset',
            'pytest_args': namenodes_arg + " --autoxtocd=yes -sv",
            'timeout': 900,
        },
    ]
}

################################################ ADSP Tests ################################################
test_adsp_pm_fncfg = {
    'job': 'test_adsp_pm_fncfg',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_pm_fncfg_pgd.py',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_agents_0 = {
    'job': 'test_adsp_sb_ipc_agents_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_dsp_to_sbagents',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_agents_1 = {
    'job': 'test_adsp_sb_ipc_agents_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_dsp_to_sbagents',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_agents_2 = {
    'job': 'test_adsp_sb_ipc_agents_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_dsp_to_sbagents',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_agents_3 = {
    'job': 'test_adsp_sb_ipc_agents_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_dsp_to_sbagents',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_agents_4 = {
    'job': 'test_adsp_sb_ipc_agents_4',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_dsp_to_sbagents',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_sb_ipc_invalid_sai = {
    'job': 'test_adsp_sb_ipc_invalid_sai',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\sbipc_dsp_to_sbagents_test\test_sbipc_dsp_to_sbagents.py::TestSbipcDspToSbAgests::test_sb_invalid_sai',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
            'timeout': 600,
        },
    ]
}

test_adsp_dash = {
    'job': 'test_adsp_dash',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\dash_board_regs_test.py::test_dash_board_regs',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 300,
        },
    ]
}

test_adsp_core_pm_0 = {
    'job': 'test_adsp_core_pm_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_dsp_core_power_gate_individually.py',
            'pytest_args': namenodes_arg + " ",
            'timeout': 4200,
        },
    ]
}

test_adsp_core_pm_1 = {
    'job': 'test_adsp_core_pm_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_dsp_core_power_gate_individually.py',
            'pytest_args': namenodes_arg + " ",
            'timeout': 4200,
        },
    ]
}

test_adsp_rw_wait_reset = {
    'job': 'test_adsp_rw_wait_reset',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_write_waiti.py',
            'pytest_args': namenodes_arg + " ",
            'timeout': 3600,
        },
    ]
}

test_adsp_fw_status_error_0 = {
    'job': 'test_adsp_fw_status_error_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_dsp_fw_rpt_reg.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 600,
        },
    ]
}

test_adsp_fw_status_error_1 = {
    'job': 'test_adsp_fw_status_error_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_dsp_fw_rpt_reg.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 600,
        },
    ]
}

test_adsp_shim_boot = {
    'job': 'test_adsp_shim_boot',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_shim_boot_regs_negative.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 3600,
        },
    ]
}

test_l2mhe_ulphub_clkreq_0 = {
    'job': 'test_l2mhe_ulphub_clkreq_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_l2mhe_ulphub_clkreq',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2mhe_ulphub_clkreq_1 = {
    'job': 'test_l2mhe_ulphub_clkreq_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_l2mhe_ulphub_clkreq',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2mhe_ulphub_clkreq_2 = {
    'job': 'test_l2mhe_ulphub_clkreq_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_l2mhe_ulphub_clkreq',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2mhe_ulphub_clkreq_3 = {
    'job': 'test_l2mhe_ulphub_clkreq_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_l2mhe_ulphub_clkreq',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_l2mhe_ulphub_clkreq_4 = {
    'job': 'test_l2mhe_ulphub_clkreq_4',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_l2mhe_ulphub_clkreq',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 9000,
        },
    ]
}

test_adsp_boot_l2sram = {
    'job': 'test_adsp_boot_l2sram',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_conditional_write_hpsram.py::test_rd_cond_write_hpsram',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 600,
        },
    ]
}

test_adsp_hor = {
    'job': 'test_adsp_hor',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_conditional_write_hpsram.py::test_dsp_hor',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 600,
        },
    ]
}

test_load_fw = {
    'job': 'test_load_fw',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_load_fw.py::test_load_fw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 600,
        },
    ]
}

test_timestamp_int = {
    'job': 'test_timestamp_int',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_timestamp_int.py::TestTimestampInt::test_timestamp_int',
            'pytest_args': namenodes_arg + " --autoxtocd=no -sv",
            'timeout': 600,
        },
    ]
}

test_adsp_tpe = {
    'job': 'test_adsp_tpe',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_dsp_tpe.py::test_dsp_tpe',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 5600,
        },
    ]
}

################################################ ADSP ROM Tests ################################################
test_adsp_interrupt_priority = {
    'job': 'test_adsp_interrupt_priority',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_fiq_irq.py::TestFiqIrqPowerGating::test_fiq_irq_dmac',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 1200,
        },
    ]
}

test_adsp_sb_to_dsp_0 = {
    'job': 'test_adsp_sb_to_dsp_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_sideband_ipc.py::TestIPCSideband::test_ipc_sideband_waiti_wakeup',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 1200,
        },
    ]
}

test_adsp_sb_to_dsp_1 = {
    'job': 'test_adsp_sb_to_dsp_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_sideband_ipc.py::TestIPCSideband::test_ipc_sideband_waiti_wakeup',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 1200,
        },
    ]
}

test_adsp_read_cond_write_0 = {
    'job': 'test_adsp_read_cond_write_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_conditional_write.py::test_rd_cond_write',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_adsp_read_cond_write_1 = {
    'job': 'test_adsp_read_cond_write_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_conditional_write.py::test_rd_cond_write',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_adsp_read_cond_write_2 = {
    'job': 'test_adsp_read_cond_write_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_rd_conditional_write.py::test_rd_cond_write',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

################################################ ANNA Tests ################################################
test_anna_register_from_host = {
    'job': 'test_anna_register_from_host',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_anna_host.py',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
#             'pytest_args': namenodes_arg + " ",
            'timeout': 180,
        },
    ]
}

test_anna_prevent_pg = {
    'job': 'test_anna_prevent_pg',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_gna_prevent_pg.py',
            'pytest_args': namenodes_arg + " --autoxtocd=no",
#             'pytest_args': namenodes_arg + " ",
            'timeout': 180,
        },
    ]
}

################################################ Audio Memory Tests ################################################

test_audiomem_memory_window = {
    'job': 'test_audiomem_memory_window',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_hpsram_rw',
            'pytest_args': namenodes_arg + " ",
            'timeout': 180,
        },
    ]
}

## start here
test_audiomem_memory_window_dmwlo = {
    'job': 'test_audiomem_memory_window_dmwlo',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_dmwlo',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_audiomem_memory_window_limit_offset_0 = {
    'job': 'test_audiomem_memory_window_limit_offset_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_limit_offset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_audiomem_memory_window_limit_offset_1 = {
    'job': 'test_audiomem_memory_window_limit_offset_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_limit_offset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_audiomem_memory_window_limit_offset_2 = {
    'job': 'test_audiomem_memory_window_limit_offset_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_limit_offset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_audiomem_memory_window_min_limit = {
    'job': 'test_audiomem_memory_window_min_limit',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_min_limit',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_audiomem_memory_window_hpsram_rw = {
    'job': 'test_audiomem_memory_window_hpsram_rw',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_hpsram_rw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_hpsram_ro = {
    'job': 'test_audiomem_memory_window_hpsram_ro',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_hpsram_ro',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_ulpsram_rw = {
    'job': 'test_audiomem_memory_window_ulpsram_rw',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_ulpsram_rw',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_ulpsram_ro = {
    'job': 'test_audiomem_memory_window_ulpsram_ro',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_ulpsram_ro',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_sb_host_neg = {
    'job': 'test_audiomem_memory_window_sb_host_neg',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_sb_access_sb_host_neg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_sb_neg = {
    'job': 'test_audiomem_memory_window_sb_neg',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_program_host_access_sb_neg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_audiomem_memory_window_disabled = {
    'job': 'test_audiomem_memory_window_disabled',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_access_when_disabled',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 180,
        },
    ]
}

test_memory_window_all = {
    'job': 'test_memory_window_all',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 800,
        },
    ]
}

test_mem_window_power_gated_0 = {
    'job': 'test_mem_window_power_gated_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_power_gated',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_mem_window_power_gated_1 = {
    'job': 'test_mem_window_power_gated_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py::TestMemWindow::test_mem_window_power_gated',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_audiomem_l2mem = {
    'job': 'test_audiomem_l2mem',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_l2mem_walkthrough.py::test_rom_l2mem_walkthrough',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 400,
        },
    ]
}

test_memory_window_sb_0 = {
    'job': 'test_memory_window_sb_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m sb -sv",
            'timeout': 900,
        },
    ]
}

test_memory_window_sb_1 = {
    'job': 'test_memory_window_sb_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m sb -sv",
            'timeout': 900,
        },
    ]
}

test_memory_window_sb_2 = {
    'job': 'test_memory_window_sb_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m sb -sv",
            'timeout': 900,
        },
    ]
}

test_memory_window_hpsram_0 = {
    'job': 'test_memory_window_hpsram_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m hpsram -sv",
            'timeout': 900,
        },
    ]
}

test_memory_window_hpsram_1 = {
    'job': 'test_memory_window_hpsram_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m hpsram -sv",
            'timeout': 900,
        },
    ]
}

test_memory_window_ulpsram = {
    'job': 'test_memory_window_ulpsram',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_window_test\test_memory_window.py',
            'pytest_args': namenodes_arg + " -m ulpsram -sv",
            'timeout': 900,
        },
    ]
}

## FAIL test. on debug

test_audiomem_hpsram_tlb_0 = {
    'job': 'test_audiomem_hpsram_tlb_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_hstlb_with_dmac',
            'pytest_args': namenodes_arg + " -sv",
            # 'timeout': 400,
            'timeout': 7500,
        },
    ]
}

test_audiomem_hpsram_tlb_1 = {
    'job': 'test_audiomem_hpsram_tlb_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_hstlb_with_dmac',
            'pytest_args': namenodes_arg + " -sv",
            # 'timeout': 400,
            'timeout': 7500,
        },
    ]
}

test_audiomem_l2uc_0 = {
    'job': 'test_audiomem_l2uc_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_all_host_dmac',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_audiomem_l2uc_1 = {
    'job': 'test_audiomem_l2uc_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_all_host_dmac',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_audiomem_l2uc_2 = {
    'job': 'test_audiomem_l2uc_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_all_host_dmac',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_audiomem_l2uc_3 = {
    'job': 'test_audiomem_l2uc_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dmac_test\test_host_dmac.py::test_all_host_dmac',
            'pytest_args': namenodes_arg + " -sv --autoxtocd=no",
            'timeout': 3600,
        },
    ]
}

test_audiomem_l2uc_limit_0 = {
    'job': 'test_audiomem_l2uc_limit_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_l2uc_limit.py::test_l2uc_limit_offset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 400,
        },
    ]
}

test_audiomem_l2uc_limit_1 = {
    'job': 'test_audiomem_l2uc_limit_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_l2uc_limit.py::test_l2uc_limit_offset',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 400,
        },
    ]
}

test_audiomem_neg_l2uc = {
    'job': 'test_audiomem_neg_l2uc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2uncache_test\test_negative_l2uctlb.py::test_negative_l2uctlb',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 6000,
        },
    ]
}

test_audiomem_hpsram_pg_0 = {
    'job': 'test_audiomem_hpsram_pg_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_pg_test\test_sram_pg.py::test_sram_pg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_audiomem_hpsram_pg_1 = {
    'job': 'test_audiomem_hpsram_pg_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\mem_pg_test\test_sram_pg.py::test_sram_pg',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 7200,
        },
    ]
}

test_audiomem_hpsram_retention = {
    'job': 'test_audiomem_hpsram_retention',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2hpsram_test\test_l2hpsram.py::TestL2Hpsram::test_l2hpsram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 900,
        },
    ]
}

test_audiomem_ulpsram_retention = {
    'job': 'test_audiomem_ulpsram_retention',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\l2ulpsram_pg_test\test_l2ulppg.py::TestL2UlpSram::test_l2_ulp_sram_retention',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 900,
        },
    ]
}

test_ecc_0 = {
    'job': 'test_ecc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\ecc_test\test_ecc.py::test_ecc',
            'pytest_args': "-sv",
            'timeout': 400,
        },
    ]
}

test_ecc_1 = {
    'job': 'test_ecc',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\ecc_test\test_ecc.py::test_ecc',
            'pytest_args': "-sv",
            'timeout': 400,
        },
    ]
}


################################################ MMU (ADSP) Tests ################################################

test_autorefill_test_0 = {
    'job': 'test_autorefill_test_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_autorefill_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_reset_way6_0 = {
    'job': 'test_mmu_reset_way6_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_reset_way6',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_reset_way6_1 = {
    'job': 'test_mmu_reset_way6_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_reset_way6',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_ring_priority_test_0 = {
    'job': 'test_mmu_ring_priority_test_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_ring_priority_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_ring_priority_test_1 = {
    'job': 'test_mmu_ring_priority_test_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_ring_priority_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_ring_priority_test_2 = {
    'job': 'test_mmu_ring_priority_test_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_ring_priority_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_ring_priority_test_3 = {
    'job': 'test_mmu_ring_priority_test_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_ring_priority_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_dynamic_asid_test = {
    'job': 'test_mmu_dynamic_asid_test',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_dynamic_asid_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_rand_map_way6 = {
    'job': 'test_mmu_rand_map_way6',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_rand_map_way6',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_probe_rd_test = {
    'job': 'test_probe_rd_test',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_probe_rd_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_autorefill_test_1 = {
    'job': 'test_autorefill_test_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_autorefill_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 300,
        },
    ]
}

test_mmu_cache_attr_test_0 = {
    'job': 'test_mmu_cache_attr_test_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_cache_attr_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_cache_attr_test_1 = {
    'job': 'test_mmu_cache_attr_test_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_cache_attr_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_cache_attr_test_2 = {
    'job': 'test_mmu_cache_attr_test_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_cache_attr_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_cache_attr_test_3 = {
    'job': 'test_mmu_cache_attr_test_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_cache_attr_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_exception_test_0 = {
    'job': 'test_mmu_exception_test_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_exception_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_exception_test_1 = {
    'job': 'test_mmu_exception_test_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_exception_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_exception_test_2 = {
    'job': 'test_mmu_exception_test_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_exception_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_mmu_exception_test_3 = {
    'job': 'test_mmu_exception_test_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_mmu_exception_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_all_mmu_test_0 = {
    'job': 'test_all_mmu_test_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_all_mmu_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_all_mmu_test_1 = {
    'job': 'test_all_mmu_test_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_all_mmu_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}

test_all_mmu_test_2 = {
    'job': 'test_all_mmu_test_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\dsp_test\test_mmu.py::TestMmu::test_all_mmu_test',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 700,
        },
    ]
}



################################################ TTS Timestamping ################################################

test_walclk_reset_dsplrst = {
    'job': 'test_walclk_reset_dsplrst',
    'type': 'pytest',
    'args': [
        {
            # 'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_wall_clock.py::test_walclk_reset_dsplrst',
			'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\pm_test\test_wall_clock.py::test_wall_clock_reset_dsplrst',
            'pytest_args': "-sv",
            'timeout': 500,
        },
    ]
}

# test_dmmr_def_value = {
    # 'job': 'test_dmmr_def_value',
    # 'type': 'pytest',
    # 'args': [
        # {
            # 'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_default_value.py::TestRegisterDefaultValue::test_dmmr_def_value',
            # 'pytest_args': namenodes_arg + " -sv",
            # 'timeout': 500,
        # },
    # ]
# }

test_wdt_interrupt = {
    'job': 'test_wdt_interrupt',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt',
            'pytest_args': namenodes_arg + " -sv",
            'timeout': 900,
        },
    ]
}

test_wdt_interrupt_dsp_0 = {
    'job': 'test_wdt_interrupt_dsp_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_dsp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout' : 900,
        },
    ]
}

test_wdt_interrupt_dsp_1 = {
    'job': 'test_wdt_interrupt_dsp_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_dsp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout' : 900,
        },
    ]
}

test_wdt_interrupt_dsp_2 = {
    'job': 'test_wdt_interrupt_dsp_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_dsp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout' : 900,
        }
    ]
}

test_wdt_interrupt_dsp_3 = {
    'job': 'test_wdt_interrupt_dsp_3',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_dsp',
            'pytest_args': namenodes_arg + " -sv",
            'timeout' : 900,
        }
    ]
}

test_wdt_interrupt_host_0 = {
    'job': 'test_wdt_interrupt_host_0',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_host',
            'pytest_args': namenodes_arg + " ",
            'timeout': 900,
        },
    ]
}

test_wdt_interrupt_host_1 = {
    'job': 'test_wdt_interrupt_host_1',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_host',
            'pytest_args': namenodes_arg + " ",
            'timeout' : 900,
        },
    ]
}

test_wdt_interrupt_host_2 = {
    'job': 'test_wdt_interrupt_host_2',
    'type': 'pytest',
    'args': [
        {
            'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\wdt_test\test_wdt.py::TestWdt::test_wdt_interrupt_host',
            'pytest_args': namenodes_arg + " ",
            'timeout' : 900,
        },
    ]
}

################################################ Other Tests ################################################

#insert other test here

TESTLINES_TO_BE_EXECUTE = [
#### PM

    test_fiq_irq_dmac,
    test_force_power_gating_lctl_io1,
    test_force_power_gating_lctl_io0,
    test_l1cache,
    test_l2_ulp_sram_retention,
    test_l2_ulp_sram_retention_0,
    test_l2_ulp_sram_retention_1,
    test_l2_ulp_sram,
    test_l2hpsram_retention,
    test_l2hpsram_retention_0,
    test_l2hpsram_retention_1,
    test_l2hpsram_pg,
    test_l2hpsram_pg_0,
    test_l2hpsram_pg_1,
	
	d0i3_entry_with_dsp_subsystem_off_0,
	d0i3_entry_with_dsp_subsystem_off_1,
	power_on_off_dsp_core_0,
	power_on_off_dsp_core_1,
	test_adsp_core_pm_3,
	test_dsp_core_power_gate_individually,
	test_fiq_irq_dmac,
	test_prevent_power_gating_dsp_core_boot_ctrl,
	
	test_stress_d0i3_cycling,
	test_stress_d0i3_cycling_0,
	test_stress_d0i3_cycling_1,
	test_stress_d0i3_cycling_2,
	test_stress_d0i3_cycling_3,
	test_stress_d0i3_cycling_4,
	
	test_stress_d3_cycling,
	test_stress_d3_cycling_0,
	test_stress_d3_cycling_1,
	
	#test_wdt_interrupt_dsp_0,
	
	#1503899917	15013397409	[PM][gated-HST] Dynamic power gating - D0i3 - HDA / SNDW link wake interrupt
	#TC with Multiple Tests
	test_hda_sdi_intx_interrupt_d0i3,
	test_sndw_clock_stop_wake_d0i3_interrupt,

    
#### BIU
     test_receive_qos_rsp,
     test_receive_qos_rsp_0,
     test_receive_qos_rsp_1,
    # test_send_nonposted,
    # test_send_posted,
    # test_send_qos_dmd,
    # test_stress_sb_msg_injection,
    # test_stress_multiple_in_non_posted_completion,
    # test_stress_multiple_in_posted_completion,
    # test_stress_multiple_in_posted_non_posted,
    # test_stress_multiple_out_non_posted_completion,
    # test_stress_multiple_out_posted_completion,
    # test_cw_return_credit_fw_not_ack,
    # test_hda_sdi_intx_interrupt,
    
#### Register
    test_register_bar0_shadow_bar2,
    test_dmmr_attribute,
    test_dmmr_def_value,
    test_dmmr_def_value_0,
    test_dmmr_def_value_1,
    test_dmmr_register_reset,
    test_dmmr_register_reset_0,
    test_dmmr_register_reset_1,
    test_dmmr_register_reset_2,
    test_dmmr_register_reset_3,
    test_dmmr_register_reset_4,
    # test_dmmr_register_reset_pltrst,
    # test_dmmr_register_reset_wrsm,
    # test_dmmr_register_reset_crst,
    # test_dmmr_register_reset_dsplrst,
    # test_dmmr_register_reset_flr,
    test_dsp_register_reset,
    test_dsp_attribute_0,
    test_dsp_attribute_1,
    test_dsp_attribute_2,
    test_dsp_attribute_3,
    test_sweep_through_hmmr,
    test_sweep_through_dmmr,
    test_reset_isolation_gated_io_0_complete,
    test_reset_isolation_gated_io_1_complete,
    test_dspx_gated_register_access,
    test_hst,
    test_hub_hp,
    test_io0_gated_register_access,
    test_io1_gated_register_access,
    test_gated_mlx_access,
    test_ml,
    test_ml_0,
    test_ml_1,
    test_gated_dspx,
    test_gated_io_0_i2s,
    test_gated_io_0_i2s_0,
    test_gated_io_1_sndw,
    test_gated_io_1_sndw_0,
    test_gated_io_0_i2s_1,
    test_gated_io_1_sndw_1,
    test_offload_dmic,
    test_offload_dmic_0,
    test_offload_dmic_1,
    test_offload_dmic_2,
    test_offload_hda,
    test_offload_hda_0,
    test_offload_idisp,
    test_offload_idisp_0,
    test_offload_sndw,
    test_offload_sndw_0,
    test_offload_i2s_0,
    test_offload_uaol,
    test_offload_uaol_0,
    test_offload_dmic_2,
    test_offload_hda_1,
    test_offload_idisp_1,
    test_offload_sndw_1,
    test_offload_i2s_1,
    test_offload_i2s,
    test_offload_uaol_1,
    test_ownership_dspc,
    test_ownership_dspc_0,
    test_ownership_mdiv,
    test_ownership_mdiv_0,
    test_ownership_aonml_0,
    test_ownership_aonml,
    test_ownership_dspc_1,
    test_ownership_mdiv_1,
    test_ownership_aonml_1,
    test_ownership_dspc_2,
    test_ownership_mdiv_2,
    test_ownership_aonml_2,
    test_register_SAI_ACPSAI,
    test_register_SAI_ACPSAI_0,
    test_register_SAI_FWLDSAI,
    test_register_SAI_FWLDSAI_0,
    test_register_SAI_FWVFSAI_0,
    test_register_SAI_IPCSASAI_0,
    test_register_SAI_THSTSAI_dmmr_0,
    test_register_SAI_THSTSAI_hmmr_0,
    test_register_SAI_UHSTSAI_dmmr_0,
    test_register_SAI_UHSTSAI_hcfg_0,
    test_register_SAI_UHSTSAI_hmmr_0,
    test_register_SAI_ACPSAI_1,
    test_register_SAI_FWLDSAI_1,
    test_register_SAI_FWVFSAI,
    test_register_SAI_FWVFSAI_1,
    test_register_SAI_IPCSASAI_1,
    # test_register_SAI_THSTSAI_dmmr,
    # test_register_SAI_THSTSAI_hmmr,
    # test_register_SAI_UHSTSAI_dmmr,
    # test_register_SAI_UHSTSAI_hcfg,
    # test_register_SAI_UHSTSAI_hmmr,


#### SIIP
    test_acepll_own_req_clkctl,
    test_acepll_own_req_dmic,
    test_acepll_own_req_ssp,
    test_dmic_apll_own_req_violation,
    test_ssp_apll_own_req_violation,
    test_clkctl_apll_own_req,
    test_crstb_apll_own_req,
    test_dmic_apll_own_req,
    test_ssp_apll_own_req,
    test_ddr_nonsnoop_own_req,
    test_ddr_snoop_own_req,
    test_spsreq_ddr_own_req,
    test_spsreq_dtf_own_req,
    test_spsreq_prim_own_req,
    test_spsreq_side_own_req,
    test_spsreq_sbp_own_req,
    test_spsreq_vnn_own_req,
    test_spsreq_xhci_own_req,
    test_dtf_own_req_violation,
    test_dtf_own_req,
    test_sbp_own_req_compulsory_cycle_0,
    test_sbp_own_req_compulsory_cycle_1,
    test_sbp_own_req_compulsory_cycle_2,
    test_sbp_own_req_voluntary_cycle_0,
    test_sbp_own_req_voluntary_cycle_1,
    test_sbp_own_req_reset_cycle,
    test_clkctl_prim_own_req,
    test_clkctl_prim_own_req_dsp_iosfpc,
    test_corb_rirb_prim_clkack_violation,
    test_prim_own_req_hst_pgd_wake,
    test_prim_voluntary_imr_0,
    test_prim_voluntary_imr_1,
    test_l2uncache_ack_violation,
    test_prim_own_req_msi_interrupt_0,
    test_prim_own_req_msi_interrupt_1,
    test_corb_rirb_psf_ownack_violation,
    #test_prim_voluntary_imr,
    test_prim_voluntary_l2uncache,
    #test_prim_own_req_msi_interrupt, 
    test_neg_spsreq_dtf_own_req,
    test_neg_spsreq_sbp_own_req,
    test_neg_spsreq_vnn_own_req,
    test_neg_dtf_own_req_0,
    test_neg_dtf_own_req_1,
    test_neg_corb_rirb_psf_ownack,  
    test_neg_spsreq_prim_own_req,

#### SNDW
    test_ace2px_sndw_allseg_hda_corb_rirb,
    test_ace2px_sndw_allseg_hda_corb_rirb_0,
    test_ace2px_sndw_allseg_hda_corb_rirb_1,
    test_sndw_two_slave_enumeration,
    test_sndw_slave_status_changes,
    test_sndw_slave_status_changes_0,
    test_sndw_slave_status_changes_1,
    test_sndw_coupled_loopback_stream_cmdrsp_conc,
    test_sndw_coupled_instream_bankswitch,
#### SNDW Idisp
    test_sndw_idisp_async_wake,
    test_sndw_idisp_async_wake_0,
	test_sndw_idisp_async_wake_1,
    test_sndw_idisp_clock_stop_pme_wake,
    test_sndw_idisp_clock_stop_pme_wake_0,
	test_sndw_idisp_clock_stop_pme_wake_1,
    test_sndw_idisp_clock_stop_slave_enum,
    test_sndw_idisp_clock_stop_slave_enum_0,
	test_sndw_idisp_clock_stop_slave_enum_1,
    test_sndw_idisp_slave_status_changes,
    test_sndw_idisp_slave_status_changes_0,
	test_sndw_idisp_slave_status_changes_1,
    test_sndw_idisp_enum,
	test_sndw_idisp_enum_0,
	test_sndw_idisp_enum_1,
#### HDA
    test_walclk_warp_around,

### WDT
    test_wdt_interrupt_host,
    test_wdt_interrupt_dsp,
    test_wdt_interrupt,
    test_wdt_pause,
    test_wdt_reset,
    test_wdt_store,
    test_wdt_timer_reset,
    test_wdt_eoi_clear,
    
### ADSP
    test_adsp_pm_fncfg,
    test_adsp_sb_ipc_agents_0,
    test_adsp_sb_ipc_agents_1,
    test_adsp_sb_ipc_agents_2,
    test_adsp_sb_ipc_agents_3,
    test_adsp_sb_ipc_agents_4,
    test_adsp_sb_ipc_invalid_sai,
    test_adsp_dash,
    test_l2mhe_ulphub_clkreq_0, 
    test_l2mhe_ulphub_clkreq_1, 
    test_l2mhe_ulphub_clkreq_2, 
    test_l2mhe_ulphub_clkreq_3, 

# Run at the end of the sequence
    test_adsp_core_pm_0,
    test_adsp_core_pm_1,
    test_adsp_rw_wait_reset,
######################################
    # GDB test
######################################    
    test_adsp_boot_l2sram,
    test_adsp_hor,
    test_adsp_fw_status_error_0,
    test_adsp_fw_status_error_1,
    test_adsp_shim_boot,
    
### ADSP ROM # need to seperate out on QUAL due to fw loading
# Load ROM
    test_adsp_interrupt_priority,
# Load ROM
    test_adsp_sb_to_dsp_0,
    test_adsp_sb_to_dsp_1,
# Run seperately (Load ROM)
    test_adsp_read_cond_write_0,
    test_adsp_read_cond_write_1,
    test_load_fw,   # require local changes
    
### ANNA
    test_anna_register_from_host,
    test_anna_prevent_pg,
    
### Audio Memory
   test_anna_register_from_host,
   test_audiomem_memory_window,
# Start here
    # Use GDB
   test_audiomem_memory_window_dmwlo,
   test_audiomem_memory_window_limit_offset_0,
   test_audiomem_memory_window_limit_offset_1,
   test_audiomem_memory_window_min_limit,
   test_audiomem_memory_window_hpsram_rw,
   test_audiomem_memory_window_hpsram_ro,
   test_audiomem_memory_window_ulpsram_rw,
   test_audiomem_memory_window_ulpsram_ro,
   test_audiomem_memory_window_sb_host_neg,
   test_audiomem_memory_window_sb_neg,
# Without GDB
   test_audiomem_memory_window_disabled,
   test_audiomem_hpsram_tlb_0,
   test_audiomem_hpsram_tlb_1,
   test_audiomem_l2uc_0,
   test_audiomem_l2uc_1,
   test_audiomem_l2uc_2,
   test_audiomem_l2uc_3,
#    # Use GDB
   test_audiomem_l2uc_limit_0,
   test_audiomem_l2uc_limit_1,
   test_audiomem_neg_l2uc,
   test_audiomem_hpsram_pg_0,
   test_audiomem_hpsram_pg_1,
   test_audiomem_hpsram_retention,
   test_audiomem_ulpsram_retention,
   test_ecc_0,
   test_ecc_1,

#ROM
   test_audiomem_l2mem,
   
#Security
	test_hpsram_mrp,
	test_l2uc_tlb_retention,
	test_l2uncache_host_mrp_1,
	test_l2uncache_host_mrp_2,
	test_l2uncache_host_mrp_3,
    test_l2hpsramtlb_lock,
	test_ulpsram_mrp,

#TTS
	test_dmmr_def_value,
	test_walclk_reset_dsplrst,
	#test_wdt_eoi_clear,
	test_wdt_interrupt,
	test_wdt_interrupt_dsp_1,
	test_wdt_interrupt_host_0,
	test_wdt_interrupt_host_1,
	test_wdt_interrupt_host_2,
	
	# For TC 1503899917	15013413423	WDT interrupt to Host/DSP
	# Multiple Test
	#test_wdt__1interrupt_host_1, 
	test_wdt_interrupt_dsp_2,
	test_wdt_interrupt_dsp_3,

	test_wdt_pause,
	test_wdt_reset,
	test_wdt_store,
	#test_wdt_timer_reset,


]

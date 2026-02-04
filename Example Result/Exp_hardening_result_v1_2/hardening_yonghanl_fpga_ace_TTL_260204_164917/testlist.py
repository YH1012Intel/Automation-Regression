
namenodes_arg = '--pysv_config=ttlhg4'

test_register_SAI_THSTSAI_hmmr_0 = {'job': 'test_register_SAI_THSTSAI_hmmr_0', 'type': 'pytest', 'args': [{'content_path': r'ipsv-ace\ipsv-pkg\ipsv\ace\pytest\register_test\test_register_SAI.py::TestRegisterSAI::test_register_SAI_THSTSAI_hmmr', 'pytest_args': namenodes_arg + '" -sv"', 'timeout': 7200}]}


TESTLINES_TO_BE_EXECUTE = [test_register_SAI_THSTSAI_hmmr_0, ]
##################################################
# DO NOT DELETE 
#################################################

PROJ_DEFS = {
    '_DEF': '',
    '_PRELOAD': '',  
    }

CONFIG = {}

def generate_fields(TAGS):
    tags = TAGS.split(".")
    if "sle" in tags:
        CONFIG['_ENV'] = "SLE"
    elif "fpga" in tags:
        CONFIG['_ENV'] = "FPGA"
    elif "qa" in tags:
        CONFIG['_ENV'] = "QA"
    else:
        print("CONFIG ERROR: supported sle, fpga and qa only")
        sys.exit(-1)

    CONFIG['_PROJECT'] = TAGS.split(".")[0]

    #PROJ_DEFS['_DEF'] = ''
    PROJ_DEFS['_DEF'] = "-define TGT_PLAT_%s" % CONFIG['_ENV'].upper()
    PROJ_DEFS['_DEF'] = PROJ_DEFS['_DEF'] + " -define PROJ_STR_U \\\"%s\\\"" % CONFIG['_PROJECT'].upper()
    PROJ_DEFS['_DEF'] = PROJ_DEFS['_DEF'] + " -define PROJ_STR_L \\\"%s\\\"" % CONFIG['_PROJECT'].lower()
    PROJ_DEFS['_PRELOAD'] = "/perspec/targets/ipsv/ace/fpga/preload_%s.sln" % CONFIG['_PROJECT'].lower()
    PROJ_DEFS['_PRELOAD_GNA'] = "perspec/targets/ipsv/gna/fpga/preload_gna_%s.sln" % CONFIG['_PROJECT'].lower()
    return PROJ_DEFS

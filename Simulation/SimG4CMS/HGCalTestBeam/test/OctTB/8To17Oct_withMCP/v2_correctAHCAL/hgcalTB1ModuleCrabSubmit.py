from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()


#submitVersion = "V0/8To17Oct"
#submitVersion = "V0/8To17Oct/with25umGold"
#submitVersion = "V0/8To17Oct/with1p1mmPCB"
#submitVersion = "V0/8To17Oct/noPCBinEE"
#submitVersion = "V1/8To17Oct_withMCP"
#submitVersion = "V2/8To17Oct_withMCP"
#submitVersion = "V2/noSmearingSamples_withBeamLine_NoAngle_vtxPosAsOnLayer1/8To17Oct_withMCP"
#submitVersion = "V2/noSmearingSamples_withBeamLine_NoAngle_vtxPosAsOnLayer1_EMN_106X/8To17Oct_withMCP"
#submitVersion = "V2/noSmearingSamples_withBeamLine_withAngle_EMN_106X/8To17Oct_withMCP"
submitVersion = "V2/noSmearingSamples_withBeamLine_withAngle_EMN_106X_correctAHCAL/8To17Oct_withMCP"
mainOutputDir = '/store/group/upgrade/HGCAL/simulation/2018/Oct/%s' % submitVersion

config.General.transferLogs = False
#config.General.transferLogs = True

config.JobType.pluginName  = 'PRIVATEMC'
config.Data.inputDBS = 'global'
#config.Data.publication = True
config.Data.publication = False
config.Data.splitting     = 'EventBased'
#config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob   = 2000
#config.Data.totalUnits    = 1000000

config.Data.unitsPerJob   = 100
#config.Data.totalUnits    = 1000000
config.Data.totalUnits    = 100000
#config.Data.totalUnits    = 5000

#config.Data.totalUnits    = 100000

config.JobType.allowUndistributedCMSSW = True

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist       = ['T3_TW_NCU']
#config.Site.storageSite = 'T3_TW_NCU'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_projects_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)





    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E20_cfg.py'
    config.General.requestName  = 'Ele20GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E30_cfg.py'
    config.General.requestName  = 'Ele30GeV'
    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E50_cfg.py'
    config.General.requestName  = 'Ele50GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E80_cfg.py'
    config.General.requestName  = 'Ele80GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E100_cfg.py'
    config.General.requestName  = 'Ele100GeV'
    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E120_cfg.py'
    config.General.requestName  = 'Ele120GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E150_cfg.py'
    config.General.requestName  = 'Ele150GeV'
    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E200_cfg.py'
    config.General.requestName  = 'Ele200GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E250_cfg.py'
    config.General.requestName  = 'Ele250GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E300_cfg.py'
    config.General.requestName  = 'Ele300GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_FlatE20To300_cfg.py'
    config.General.requestName  = 'EleFlatE20To300GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_FlatE5To350_cfg.py'
    config.General.requestName  = 'EleFlatE5To350GeV'
#    submit(config)



    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_ele_E300_Ereso0p7perc_cfg.py'
    config.General.requestName  = 'Ele300GeV_0p7percEreso'
##    submit(config)

################################pion

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E20_cfg.py'
    config.General.requestName  = 'Pi20GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E30_cfg.py'
    config.General.requestName  = 'Pi30GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E50_cfg.py'
    config.General.requestName  = 'Pi50GeV'
    submit(config)
    
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E80_cfg.py'
    config.General.requestName  = 'Pi80GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E100_cfg.py'
    config.General.requestName  = 'Pi100GeV'
    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E120_cfg.py'
    config.General.requestName  = 'Pi120GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E200_cfg.py'
    config.General.requestName  = 'Pi200GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E250_cfg.py'
    config.General.requestName  = 'Pi250GeV'
    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_E300_cfg.py'
    config.General.requestName  = 'Pi300GeV'
    submit(config)


###########################################w

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E20_cfg.py'
    config.General.requestName  = 'Pro20GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E30_cfg.py'
    config.General.requestName  = 'Pro30GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E50_cfg.py'
    config.General.requestName  = 'Pro50GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E80_cfg.py'
    config.General.requestName  = 'Pro80GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E100_cfg.py'
    config.General.requestName  = 'Pro100GeV'
#    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E120_cfg.py'
    config.General.requestName  = 'Pro120GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E200_cfg.py'
    config.General.requestName  = 'Pro200GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E250_cfg.py'
    config.General.requestName  = 'Pro250GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_p_E300_cfg.py'
    config.General.requestName  = 'Pro300GeV'
#    submit(config)


    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_mu_E200_cfg.py'
    config.General.requestName  = 'Mu200GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_mu_FlatE5To350_cfg.py'
    config.General.requestName  = 'Mu_Flat5To350GeV'
#    submit(config)

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.psetName  = 'HGCalTBCERN170_pi_FlatE5To350_cfg.py'
    config.General.requestName  = 'Pi_Flat5To350GeV'
#    submit(config)



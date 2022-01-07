import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/cms.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcal.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcalHE.xml',
        'Geometry/HGCalCommonData/data/hgcalwafer/v7/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcalBeam.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcalsense.xml',
        'Geometry/HGCalCommonData/data/TB181/hgcProdCuts.xml',
        'Geometry/HGCalCommonData/data/TB181/Oct18/8To17Oct_withMCP_0p1X0additionalFromAl/hgcalCons.xml'),
    rootNodeName = cms.string('cms:OCMS')
)



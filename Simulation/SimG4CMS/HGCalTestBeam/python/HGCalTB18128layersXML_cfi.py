import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/HGCalCommonData/data/TB181/cms.xml',
        'Geometry/HGCalCommonData/data/TB181/28layers/hgcal.xml',
        'Geometry/HGCalCommonData/data/TB181/28layers/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/hgcalwafer/v7/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/TB181/28layers/hgcalBeam.xml',
        'Geometry/HGCalCommonData/data/TB181/28layers/hgcalsense.xml',
        'Geometry/HGCalCommonData/data/TB181/hgcProdCuts.xml',
        'Geometry/HGCalCommonData/data/TB181/28layers/hgcalCons.xml'),
    rootNodeName = cms.string('cms:OCMS')
)



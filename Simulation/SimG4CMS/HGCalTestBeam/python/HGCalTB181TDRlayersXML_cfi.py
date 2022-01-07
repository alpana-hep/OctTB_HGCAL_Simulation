import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/HGCalCommonData/data/TB181/cms.xml',
        'Geometry/HGCalCommonData/data/TB181/TDRGeom/hgcal.xml',
        'Geometry/HGCalCommonData/data/TB181/TDRGeom/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/hgcalwafer/v7/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/TB181/TDRGeom/hgcalBeam.xml',
        'Geometry/HGCalCommonData/data/TB181/TDRGeom/hgcalsense.xml',
        'Geometry/HGCalCommonData/data/TB181/hgcProdCuts.xml',
        'Geometry/HGCalCommonData/data/TB181/TDRGeom/hgcalCons.xml'),
    rootNodeName = cms.string('cms:OCMS')
)



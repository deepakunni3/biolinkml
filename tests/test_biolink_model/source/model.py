# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: biolink_model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import Bool, URI, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uri

metamodel_version = "1.3.6"


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    pass


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    pass


class IriType(Uri):
    """ An IRI """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    pass


class SymbolType(String):
    pass


class Frequency(String):
    pass


class PerecentageFrequencyValue(Double):
    pass


class Quotient(Double):
    pass


class Unit(String):
    pass


class TimeType(Time):
    pass


class BiologicalSequence(String):
    pass


# Class references
class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class PhenotypicSexId(BiologicalSexId):
    pass


class GenotypicSexId(BiologicalSexId):
    pass


class SeverityValueId(AttributeId):
    pass


class FrequencyValueId(AttributeId):
    pass


class ClinicalModifierId(AttributeId):
    pass


class OnsetId(AttributeId):
    pass


class NamedThingId(IdentifierType):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class GeneOntologyClassId(OntologyClassId):
    pass


class OrganismTaxonId(OntologyClassId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class CaseId(IndividualOrganismId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class BiosampleId(OrganismalEntityId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class EnvironmentId(BiologicalEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class ProviderId(AdministrativeEntityId):
    pass


class MolecularEntityId(BiologicalEntityId):
    pass


class ChemicalSubstanceId(MolecularEntityId):
    pass


class CarbohydrateId(ChemicalSubstanceId):
    pass


class DrugId(ChemicalSubstanceId):
    pass


class MetaboliteId(ChemicalSubstanceId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(ClinicalEntityId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class DeviceId(NamedThingId):
    pass


class GenomicEntityId(MolecularEntityId):
    pass


class GenomeId(GenomicEntityId):
    pass


class TranscriptId(GenomicEntityId):
    pass


class ExonId(GenomicEntityId):
    pass


class CodingSequenceId(GenomicEntityId):
    pass


class MacromolecularMachineId(GenomicEntityId):
    pass


class GeneOrGeneProductId(MacromolecularMachineId):
    pass


class GeneId(GeneOrGeneProductId):
    pass


class GeneProductId(GeneOrGeneProductId):
    pass


class ProteinId(GeneProductId):
    pass


class GeneProductIsoformId(GeneProductId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class RNAProductId(GeneProductId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class MacromolecularComplexId(MacromolecularMachineId):
    pass


class GeneFamilyId(MolecularEntityId):
    pass


class ZygosityId(AttributeId):
    pass


class GenotypeId(GenomicEntityId):
    pass


class HaplotypeId(GenomicEntityId):
    pass


class SequenceVariantId(GenomicEntityId):
    pass


class DrugExposureId(EnvironmentId):
    pass


class TreatmentId(EnvironmentId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class AssociationId(IdentifierType):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseInteractionAssociationId(AssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class CellLineToThingAssociationId(AssociationId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToThingAssociationId(AssociationId):
    pass


class CaseToThingAssociationId(AssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class BiosampleToThingAssociationId(AssociationId):
    pass


class BiosampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class EntityToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToThingAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(DiseaseOrPhenotypicFeatureAssociationToThingAssociationId):
    pass


class ThingToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToThingAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class EnvironmentToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToThingAssociationId(AssociationId):
    pass


class VariantToThingAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GenotypeToThingAssociationId(AssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class GenomicSequenceLocalizationId(AssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneRegulatoryRelationshipId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class OccurrentId(NamedThingId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class ActivityAndBehaviorId(OccurrentId):
    pass


class ProcedureId(OccurrentId):
    pass


class PhenomenonId(OccurrentId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(BiosampleId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Attribute"
    type_curie: ClassVar[str] = "biolink:Attribute"
    type_name: ClassVar[str] = "attribute"

    id: Union[str, AttributeId]

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiologicalSex"
    type_curie: ClassVar[str] = "biolink:BiologicalSex"
    type_name: ClassVar[str] = "biological sex"

    id: Union[str, BiologicalSexId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)


@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PhenotypicSex"
    type_curie: ClassVar[str] = "biolink:PhenotypicSex"
    type_name: ClassVar[str] = "phenotypic sex"

    id: Union[str, PhenotypicSexId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenotypicSexId):
            self.id = PhenotypicSexId(self.id)


@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypicSex"
    type_curie: ClassVar[str] = "biolink:GenotypicSex"
    type_name: ClassVar[str] = "genotypic sex"

    id: Union[str, GenotypicSexId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypicSexId):
            self.id = GenotypicSexId(self.id)


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SeverityValue"
    type_curie: ClassVar[str] = "biolink:SeverityValue"
    type_name: ClassVar[str] = "severity value"

    id: Union[str, SeverityValueId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)


@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/FrequencyValue"
    type_curie: ClassVar[str] = "biolink:FrequencyValue"
    type_name: ClassVar[str] = "frequency value"

    id: Union[str, FrequencyValueId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, FrequencyValueId):
            self.id = FrequencyValueId(self.id)


@dataclass
class ClinicalModifier(Attribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology,
    with respect to severity, laterality, age of onset, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalModifier"
    type_curie: ClassVar[str] = "biolink:ClinicalModifier"
    type_name: ClassVar[str] = "clinical modifier"

    id: Union[str, ClinicalModifierId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalModifierId):
            self.id = ClinicalModifierId(self.id)


@dataclass
class Onset(Attribute):
    """
    The age group in which manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/HP_0003674"
    type_curie: ClassVar[str] = "HP:0003674"
    type_name: ClassVar[str] = "onset"

    id: Union[str, OnsetId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "physically_interacts_with", "affects", "regulates", "positively_regulates", "negatively_regulates", "disrupts", "homologous_to", "paralogous_to", "orthologous_to", "xenologous_to", "coexists_with", "colocalizes_with", "affects_risk_for", "predisposes", "contributes_to", "causes", "prevents", "occurs_in", "located_in", "location_of", "model_of", "overlaps", "has_part", "part_of", "participates_in", "actively_involved_in", "capable_of", "derives_into", "derives_from", "manifestation_of", "produces", "same_as", "has_molecular_consequence"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q35120"
    type_curie: ClassVar[str] = "WD:Q35120"
    type_name: ClassVar[str] = "named thing"

    id: Union[str, NamedThingId]
    name: Optional[Union[str, LabelType]] = None
    category: List[Union[str, IriType]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)
        self.category = [v if isinstance(v, IriType)
                         else IriType(v) for v in self.category]


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q28845870"
    type_curie: ClassVar[str] = "WD:Q28845870"
    type_name: ClassVar[str] = "biological entity"

    id: Union[str, BiologicalEntityId] = None

@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/OntologyClass"
    type_curie: ClassVar[str] = "biolink:OntologyClass"
    type_name: ClassVar[str] = "ontology class"

    id: Union[str, OntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/RelationshipType"
    type_curie: ClassVar[str] = "biolink:RelationshipType"
    type_name: ClassVar[str] = "relationship type"

    id: Union[str, RelationshipTypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneOntologyClass"
    type_curie: ClassVar[str] = "biolink:GeneOntologyClass"
    type_name: ClassVar[str] = "gene ontology class"

    id: Union[str, GeneOntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)


@dataclass
class OrganismTaxon(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q16521"
    type_curie: ClassVar[str] = "WD:Q16521"
    type_name: ClassVar[str] = "organism taxon"

    id: Union[str, OrganismTaxonId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)


@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q7239"
    type_curie: ClassVar[str] = "WD:Q7239"
    type_name: ClassVar[str] = "organismal entity"

    id: Union[str, OrganismalEntityId] = None

@dataclass
class IndividualOrganism(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010000"
    type_curie: ClassVar[str] = "SIO:010000"
    type_name: ClassVar[str] = "individual organism"

    id: Union[str, IndividualOrganismId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)


@dataclass
class Case(IndividualOrganism):
    """
    An individual organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Case"
    type_curie: ClassVar[str] = "biolink:Case"
    type_name: ClassVar[str] = "case"

    id: Union[str, CaseId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001061"
    type_curie: ClassVar[str] = "SIO:001061"
    type_name: ClassVar[str] = "population of individual organisms"

    id: Union[str, PopulationOfIndividualOrganismsId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)


@dataclass
class Biosample(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001050"
    type_curie: ClassVar[str] = "SIO:001050"
    type_name: ClassVar[str] = "biosample"

    id: Union[str, BiosampleId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeature"
    type_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    type_name: ClassVar[str] = "disease or phenotypic feature"

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/MONDO_0000001"
    type_curie: ClassVar[str] = "MONDO:0000001"
    type_name: ClassVar[str] = "disease"

    id: Union[str, DiseaseId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "correlated_with", "has_biomarker", "treated_by", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/UPHENO_0001001"
    type_curie: ClassVar[str] = "UPHENO:0001001"
    type_name: ClassVar[str] = "phenotypic feature"

    id: Union[str, PhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)


@dataclass
class Environment(BiologicalEntity):
    """
    A feature of the environment of an organism that influences one or more phenotypic features of that organism,
    potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000955"
    type_curie: ClassVar[str] = "SIO:000955"
    type_name: ClassVar[str] = "environment"

    id: Union[str, EnvironmentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some piece of biology or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/IAO_0000030"
    type_curie: ClassVar[str] = "IAO:0000030"
    type_name: ClassVar[str] = "information content entity"

    id: Union[str, InformationContentEntityId] = None

@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CIO_0000028"
    type_curie: ClassVar[str] = "CIO:0000028"
    type_name: ClassVar[str] = "confidence level"

    id: Union[str, ConfidenceLevelId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/ECO_0000000"
    type_curie: ClassVar[str] = "ECO:0000000"
    type_name: ClassVar[str] = "evidence type"

    id: Union[str, EvidenceTypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure
    legend, or section highlighted by NLP). The scope is intended to be general and include information published on
    the web as well as journals.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/IAO_0000311"
    type_curie: ClassVar[str] = "IAO:0000311"
    type_name: ClassVar[str] = "publication"

    id: Union[str, PublicationId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AdministrativeEntity"
    type_curie: ClassVar[str] = "biolink:AdministrativeEntity"
    type_name: ClassVar[str] = "administrative entity"

    id: Union[str, AdministrativeEntityId] = None

@dataclass
class Provider(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Provider"
    type_curie: ClassVar[str] = "biolink:Provider"
    type_name: ClassVar[str] = "provider"

    id: Union[str, ProviderId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProviderId):
            self.id = ProviderId(self.id)


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "positively_regulates_entity_to_entity", "negatively_regulates_entity_to_entity"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010004"
    type_curie: ClassVar[str] = "SIO:010004"
    type_name: ClassVar[str] = "molecular entity"

    id: Union[str, MolecularEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010004"
    type_curie: ClassVar[str] = "SIO:010004"
    type_name: ClassVar[str] = "chemical substance"

    id: Union[str, ChemicalSubstanceId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Carbohydrate"
    type_curie: ClassVar[str] = "biolink:Carbohydrate"
    type_name: ClassVar[str] = "carbohydrate"

    id: Union[str, CarbohydrateId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)


@dataclass
class Drug(ChemicalSubstance):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q12140"
    type_curie: ClassVar[str] = "WD:Q12140"
    type_name: ClassVar[str] = "drug"

    id: Union[str, DrugId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CHEBI_25212"
    type_curie: ClassVar[str] = "CHEBI:25212"
    type_name: ClassVar[str] = "metabolite"

    id: Union[str, MetaboliteId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010046"
    type_curie: ClassVar[str] = "SIO:010046"
    type_name: ClassVar[str] = "anatomical entity"

    id: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/LifeStage"
    type_curie: ClassVar[str] = "biolink:LifeStage"
    type_name: ClassVar[str] = "life stage"

    id: Union[str, LifeStageId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PlanetaryEntity"
    type_curie: ClassVar[str] = "biolink:PlanetaryEntity"
    type_name: ClassVar[str] = "planetary entity"

    id: Union[str, PlanetaryEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentalProcess"
    type_curie: ClassVar[str] = "biolink:EnvironmentalProcess"
    type_name: ClassVar[str] = "environmental process"

    id: Union[str, EnvironmentalProcessId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentalFeature"
    type_curie: ClassVar[str] = "biolink:EnvironmentalFeature"
    type_name: ClassVar[str] = "environmental feature"

    id: Union[str, EnvironmentalFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)


@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalEntity"
    type_curie: ClassVar[str] = "biolink:ClinicalEntity"
    type_name: ClassVar[str] = "clinical entity"

    id: Union[str, ClinicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalTrial"
    type_curie: ClassVar[str] = "biolink:ClinicalTrial"
    type_name: ClassVar[str] = "clinical trial"

    id: Union[str, ClinicalTrialId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ClinicalIntervention"
    type_curie: ClassVar[str] = "biolink:ClinicalIntervention"
    type_name: ClassVar[str] = "clinical intervention"

    id: Union[str, ClinicalInterventionId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Device"
    type_curie: ClassVar[str] = "biolink:Device"
    type_name: ClassVar[str] = "device"

    id: Union[str, DeviceId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000110"
    type_curie: ClassVar[str] = "SO:0000110"
    type_name: ClassVar[str] = "genomic entity"

    id: Union[str, GenomicEntityId] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0001026"
    type_curie: ClassVar[str] = "SO:0001026"
    type_name: ClassVar[str] = "genome"

    id: Union[str, GenomeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)


@dataclass
class Transcript(GenomicEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000673"
    type_curie: ClassVar[str] = "SO:0000673"
    type_name: ClassVar[str] = "transcript"

    id: Union[str, TranscriptId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000147"
    type_curie: ClassVar[str] = "SO:0000147"
    type_name: ClassVar[str] = "exon"

    id: Union[str, ExonId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000316"
    type_curie: ClassVar[str] = "SO:0000316"
    type_name: ClassVar[str] = "coding sequence"

    id: Union[str, CodingSequenceId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachine"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachine"
    type_name: ClassVar[str] = "macromolecular machine"

    id: Union[str, MacromolecularMachineId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneOrGeneProduct"
    type_curie: ClassVar[str] = "biolink:GeneOrGeneProduct"
    type_name: ClassVar[str] = "gene or gene product"

    id: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in", "genetically_interacts_with", "has_gene_product", "gene_associated_with_condition"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/SO_0000704"
    type_curie: ClassVar[str] = "SO:0000704"
    type_name: ClassVar[str] = "gene"

    id: Union[str, GeneId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)


@dataclass
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/WD/Q424689"
    type_curie: ClassVar[str] = "WD:Q424689"
    type_name: ClassVar[str] = "gene product"

    id: Union[str, GeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/PR_000000001"
    type_curie: ClassVar[str] = "PR:000000001"
    type_name: ClassVar[str] = "protein"

    id: Union[str, ProteinId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)


@dataclass
class GeneProductIsoform(GeneProduct):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneProductIsoform"
    type_curie: ClassVar[str] = "biolink:GeneProductIsoform"
    type_name: ClassVar[str] = "gene product isoform"

    id: Union[str, GeneProductIsoformId] = None

@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ProteinIsoform"
    type_curie: ClassVar[str] = "biolink:ProteinIsoform"
    type_name: ClassVar[str] = "protein isoform"

    id: Union[str, ProteinIsoformId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CHEBI_33697"
    type_curie: ClassVar[str] = "CHEBI:33697"
    type_name: ClassVar[str] = "RNA product"

    id: Union[str, RNAProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/RNAProductIsoform"
    type_curie: ClassVar[str] = "biolink:RNAProductIsoform"
    type_name: ClassVar[str] = "RNA product isoform"

    id: Union[str, RNAProductIsoformId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001235"
    type_curie: ClassVar[str] = "SIO:001235"
    type_name: ClassVar[str] = "noncoding RNA product"

    id: Union[str, NoncodingRNAProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon", "in_pathway_with", "in_complex_with", "in_cell_population_with", "expressed_in"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001397"
    type_curie: ClassVar[str] = "SIO:001397"
    type_name: ClassVar[str] = "microRNA"

    id: Union[str, MicroRNAId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_010046"
    type_curie: ClassVar[str] = "SIO:010046"
    type_name: ClassVar[str] = "macromolecular complex"

    id: Union[str, MacromolecularComplexId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001380"
    type_curie: ClassVar[str] = "SIO:001380"
    type_name: ClassVar[str] = "gene family"

    id: Union[str, GeneFamilyId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "subclass_of"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000133"
    type_curie: ClassVar[str] = "GENO:0000133"
    type_name: ClassVar[str] = "zygosity"

    id: Union[str, ZygosityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ZygosityId):
            self.id = ZygosityId(self.id)


@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some extablished background
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000536"
    type_curie: ClassVar[str] = "GENO:0000536"
    type_name: ClassVar[str] = "genotype"

    id: Union[str, GenotypeId] = None
    has_zygosity: Optional[Union[str, ZygosityId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)
        if self.has_zygosity is not None and not isinstance(self.has_zygosity, ZygosityId):
            self.has_zygosity = ZygosityId(self.has_zygosity)


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000871"
    type_curie: ClassVar[str] = "GENO:0000871"
    type_name: ClassVar[str] = "haplotype"

    id: Union[str, HaplotypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GENO_0000002"
    type_curie: ClassVar[str] = "GENO:0000002"
    type_name: ClassVar[str] = "sequence variant"

    id: Union[str, SequenceVariantId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)
        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)
        self.has_gene = [v if isinstance(v, GeneId)
                         else GeneId(v) for v in self.has_gene]


@dataclass
class DrugExposure(Environment):
    """
    A drug exposure is an intake of a particular chemical substance
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "http://example.org/UNKNOWN/ECTO/0000509"
    type_curie: ClassVar[str] = "ECTO:0000509"
    type_name: ClassVar[str] = "drug exposure"

    id: Union[str, DrugExposureId] = None
    drug: List[Union[str, ChemicalSubstanceId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)


@dataclass
class Treatment(Environment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "treats"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/OGMS_0000090"
    type_curie: ClassVar[str] = "OGMS:0000090"
    type_name: ClassVar[str] = "treatment"

    id: Union[str, TreatmentId] = None
    treats: List[Union[str, DiseaseOrPhenotypicFeatureId]] = empty_list()
    has_exposure_parts: List[Union[str, DrugExposureId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeographicLocation"
    type_curie: ClassVar[str] = "biolink:GeographicLocation"
    type_name: ClassVar[str] = "geographic location"

    id: Union[str, GeographicLocationId] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeographicLocationAtTime"
    type_curie: ClassVar[str] = "biolink:GeographicLocationAtTime"
    type_name: ClassVar[str] = "geographic location at time"

    id: Union[str, GeographicLocationAtTimeId] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)


@dataclass
class Association(YAMLRoot):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://purl.org/oban/association"
    type_curie: ClassVar[str] = "OBAN:association"
    type_name: ClassVar[str] = "association"

    id: Union[str, AssociationId]
    subject: Union[str, IriType]
    relation: Union[str, IriType]
    object: Union[str, IriType]
    negated: Optional[Bool] = None
    association_type: Optional[Union[str, OntologyClassId]] = None
    qualifiers: List[Union[str, OntologyClassId]] = empty_list()
    publications: List[Union[str, PublicationId]] = empty_list()
    provided_by: Optional[Union[str, ProviderId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)
        if not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if not isinstance(self.object, IriType):
            self.object = IriType(self.object)
        if self.association_type is not None and not isinstance(self.association_type, OntologyClassId):
            self.association_type = OntologyClassId(self.association_type)
        self.qualifiers = [v if isinstance(v, OntologyClassId)
                           else OntologyClassId(v) for v in self.qualifiers]
        self.publications = [v if isinstance(v, PublicationId)
                             else PublicationId(v) for v in self.publications]
        if self.provided_by is not None and not isinstance(self.provided_by, ProviderId):
            self.provided_by = ProviderId(self.provided_by)


@dataclass
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToGenotypePartAssociation"
    type_name: ClassVar[str] = "genotype to genotype part association"

    id: Union[str, GenotypeToGenotypePartAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenotypeId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToGeneAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToGeneAssociation"
    type_name: ClassVar[str] = "genotype to gene association"

    id: Union[str, GenotypeToGeneAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToVariantAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToVariantAssociation"
    type_name: ClassVar[str] = "genotype to variant association"

    id: Union[str, GenotypeToVariantAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, SequenceVariantId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToGeneAssociation"
    type_name: ClassVar[str] = "gene to gene association"

    id: Union[str, GeneToGeneAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneHomologyAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToGeneHomologyAssociation"
    type_name: ClassVar[str] = "gene to gene homology association"

    id: Union[str, GeneToGeneHomologyAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PairwiseGeneToGeneInteraction"
    type_curie: ClassVar[str] = "biolink:PairwiseGeneToGeneInteraction"
    type_name: ClassVar[str] = "pairwise gene to gene interaction"

    id: Union[str, PairwiseGeneToGeneInteractionId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class CellLineToThingAssociation(Association):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CellLineToThingAssociation"
    type_curie: ClassVar[str] = "biolink:CellLineToThingAssociation"
    type_name: ClassVar[str] = "cell line to thing association"

    id: Union[str, CellLineToThingAssociationId] = None
    subject: Union[str, CellLineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CellLineToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "cell line to disease or phenotypic feature association"

    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class ChemicalToThingAssociation(Association):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ChemicalToThingAssociation"
    type_curie: ClassVar[str] = "biolink:ChemicalToThingAssociation"
    type_name: ClassVar[str] = "chemical to thing association"

    id: Union[str, ChemicalToThingAssociationId] = None
    subject: Union[str, ChemicalSubstanceId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)


@dataclass
class CaseToThingAssociation(Association):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CaseToThingAssociation"
    type_curie: ClassVar[str] = "biolink:CaseToThingAssociation"
    type_name: ClassVar[str] = "case to thing association"

    id: Union[str, CaseToThingAssociationId] = None
    subject: Union[str, CaseId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000993"
    type_curie: ClassVar[str] = "SIO:000993"
    type_name: ClassVar[str] = "chemical to disease or phenotypic feature association"

    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001250"
    type_curie: ClassVar[str] = "SIO:001250"
    type_name: ClassVar[str] = "chemical to pathway association"

    id: Union[str, ChemicalToPathwayAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, PathwayId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_001257"
    type_curie: ClassVar[str] = "SIO:001257"
    type_name: ClassVar[str] = "chemical to gene association"

    id: Union[str, ChemicalToGeneAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class BiosampleToThingAssociation(Association):
    """
    An association between a biosample and something
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiosampleToThingAssociation"
    type_curie: ClassVar[str] = "biolink:BiosampleToThingAssociation"
    type_name: ClassVar[str] = "biosample to thing association"

    id: Union[str, BiosampleToThingAssociationId] = None
    subject: Union[str, BiosampleId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, BiosampleId):
            self.subject = BiosampleId(self.subject)


@dataclass
class BiosampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a biosample and a disease or phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiosampleToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:BiosampleToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "biosample to disease or phenotypic feature association"

    id: Union[str, BiosampleToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiosampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = BiosampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)


@dataclass
class EntityToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EntityToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:EntityToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "entity to phenotypic feature association"

    id: Union[str, EntityToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[str, BiologicalSexId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is not None and not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)
        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSexId):
            self.sex_qualifier = BiologicalSexId(self.sex_qualifier)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeatureAssociationToThingAssociation"
    type_name: ClassVar[str] = "disease or phenotypic feature association to thing association"

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToThingAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(DiseaseOrPhenotypicFeatureAssociationToThingAssociation):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/NCIT_R100"
    type_curie: ClassVar[str] = "NCIT:R100"
    type_name: ClassVar[str] = "disease or phenotypic feature association to location association"

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class ThingToDiseaseOrPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ThingToDiseaseOrPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:ThingToDiseaseOrPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "thing to disease or phenotypic feature association"

    id: Union[str, ThingToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.object is not None and not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)


@dataclass
class DiseaseToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseToThingAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseToThingAssociation"
    type_name: ClassVar[str] = "disease to thing association"

    id: Union[str, DiseaseToThingAssociationId] = None
    subject: Union[str, DiseaseId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "genotype to phenotypic feature association"

    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)


@dataclass
class EnvironmentToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/EnvironmentToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:EnvironmentToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "environment to phenotypic feature association"

    id: Union[str, EnvironmentToPhenotypicFeatureAssociationId] = None
    subject: Union[str, EnvironmentId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, EnvironmentToPhenotypicFeatureAssociationId):
            self.id = EnvironmentToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, EnvironmentId):
            self.subject = EnvironmentId(self.subject)


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/DiseaseToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:DiseaseToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "disease to phenotypic feature association"

    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/CaseToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:CaseToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "case to phenotypic feature association"

    id: Union[str, CaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)


@dataclass
class GeneToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToThingAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToThingAssociation"
    type_name: ClassVar[str] = "gene to thing association"

    id: Union[str, GeneToThingAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://bio2rdf.org/wormbase_vocabulary:Gene-Phenotype-Association"
    type_curie: ClassVar[str] = "None"
    type_name: ClassVar[str] = "gene to phenotypic feature association"

    id: Union[str, GeneToPhenotypicFeatureAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://semanticscience.org/resource/SIO_000983"
    type_curie: ClassVar[str] = "SIO:000983"
    type_name: ClassVar[str] = "gene to disease association"

    id: Union[str, GeneToDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToPopulationAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToPopulationAssociation"
    type_name: ClassVar[str] = "variant to population association"

    id: Union[str, VariantToPopulationAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PopulationToPopulationAssociation"
    type_curie: ClassVar[str] = "biolink:PopulationToPopulationAssociation"
    type_name: ClassVar[str] = "population to population association"

    id: Union[str, PopulationToPopulationAssociationId] = None
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    relation: Union[str, IriType] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToPhenotypicFeatureAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToPhenotypicFeatureAssociation"
    type_name: ClassVar[str] = "variant to phenotypic feature association"

    id: Union[str, VariantToPhenotypicFeatureAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/VariantToDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:VariantToDiseaseAssociation"
    type_name: ClassVar[str] = "variant to disease association"

    id: Union[str, VariantToDiseaseAssociationId] = None
    subject: Union[str, IriType] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, IriType):
            self.subject = IriType(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, IriType):
            self.object = IriType(self.object)


@dataclass
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneAsAModelOfDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:GeneAsAModelOfDiseaseAssociation"
    type_name: ClassVar[str] = "gene as a model of disease association"

    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation"
    type_curie: ClassVar[str] = "biolink:GeneHasVariantThatContributesToDiseaseAssociation"
    type_name: ClassVar[str] = "gene has variant that contributes to disease association"

    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)


@dataclass
class GenotypeToThingAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GenotypeToThingAssociation"
    type_curie: ClassVar[str] = "biolink:GenotypeToThingAssociation"
    type_name: ClassVar[str] = "genotype to thing association"

    id: Union[str, GenotypeToThingAssociationId] = None
    subject: Union[str, GenotypeId] = None
    relation: Union[str, IriType] = None
    object: Union[str, IriType] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation"
    type_curie: ClassVar[str] = "biolink:GeneToExpressionSiteAssociation"
    type_name: ClassVar[str] = "gene to expression site association"

    id: Union[str, GeneToExpressionSiteAssociationId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)
        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SequenceVariantModulatesTreatmentAssociation"
    type_curie: ClassVar[str] = "biolink:SequenceVariantModulatesTreatmentAssociation"
    type_name: ClassVar[str] = "sequence variant modulates treatment association"

    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = None
    subject: Union[str, SequenceVariantId] = None
    relation: Union[str, IriType] = None
    object: Union[str, TreatmentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)
        if self.object is not None and not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/FunctionalAssociation"
    type_curie: ClassVar[str] = "biolink:FunctionalAssociation"
    type_name: ClassVar[str] = "functional association"

    id: Union[str, FunctionalAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToMolecularActivityAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToMolecularActivityAssociation"
    type_name: ClassVar[str] = "macromolecular machine to molecular activity association"

    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, MolecularActivityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToBiologicalProcessAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToBiologicalProcessAssociation"
    type_name: ClassVar[str] = "macromolecular machine to biological process association"

    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, BiologicalProcessId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/MacromolecularMachineToCellularComponentAssociation"
    type_curie: ClassVar[str] = "biolink:MacromolecularMachineToCellularComponentAssociation"
    type_name: ClassVar[str] = "macromolecular machine to cellular component association"

    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = None
    subject: Union[str, MacromolecularMachineId] = None
    relation: Union[str, IriType] = None
    object: Union[str, CellularComponentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)
        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association"
    type_curie: ClassVar[str] = "None"
    type_name: ClassVar[str] = "gene to go term association"

    id: Union[str, GeneToGoTermAssociationId] = None
    subject: Union[str, MolecularEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOntologyClassId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)


@dataclass
class GenomicSequenceLocalization(Association):
    """
    A relationship between a sequence feature and an entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "http://biohackathon.org/resource/faldo#location"
    type_curie: ClassVar[str] = "faldo:location"
    type_name: ClassVar[str] = "genomic sequence localization"

    id: Union[str, GenomicSequenceLocalizationId] = None
    subject: Union[str, GenomicEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenomicEntityId] = None
    start_interbase_coordinate: Optional[str] = None
    end_interbase_coordinate: Optional[str] = None
    genome_build: Optional[str] = None
    phase: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/SequenceFeatureRelationship"
    type_curie: ClassVar[str] = "biolink:SequenceFeatureRelationship"
    type_name: ClassVar[str] = "sequence feature relationship"

    id: Union[str, SequenceFeatureRelationshipId] = None
    subject: Union[str, GenomicEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GenomicEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/TranscriptToGeneRelationship"
    type_curie: ClassVar[str] = "biolink:TranscriptToGeneRelationship"
    type_name: ClassVar[str] = "transcript to gene relationship"

    id: Union[str, TranscriptToGeneRelationshipId] = None
    subject: Union[str, TranscriptId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)
        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneToGeneProductRelationship"
    type_curie: ClassVar[str] = "biolink:GeneToGeneProductRelationship"
    type_name: ClassVar[str] = "gene to gene product relationship"

    id: Union[str, GeneToGeneProductRelationshipId] = None
    subject: Union[str, GeneId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ExonToTranscriptRelationship"
    type_curie: ClassVar[str] = "biolink:ExonToTranscriptRelationship"
    type_name: ClassVar[str] = "exon to transcript relationship"

    id: Union[str, ExonToTranscriptRelationshipId] = None
    subject: Union[str, ExonId] = None
    relation: Union[str, IriType] = None
    object: Union[str, TranscriptId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)
        if self.object is not None and not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/GeneRegulatoryRelationship"
    type_curie: ClassVar[str] = "biolink:GeneRegulatoryRelationship"
    type_name: ClassVar[str] = "gene regulatory relationship"

    id: Union[str, GeneRegulatoryRelationshipId] = None
    subject: Union[str, GeneOrGeneProductId] = None
    relation: Union[str, IriType] = None
    object: Union[str, GeneOrGeneProductId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)
        if self.subject is not None and not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity association"

    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"

    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    type_curie: ClassVar[str] = "biolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    type_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"

    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = None
    subject: Union[str, AnatomicalEntityId] = None
    relation: Union[str, IriType] = None
    object: Union[str, AnatomicalEntityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)
        if self.subject is not None and not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)


@dataclass
class Occurrent(NamedThing):
    """
    A processual entity
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes", "positively_regulates_process_to_process", "negatively_regulates_process_to_process"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/BFO_0000003"
    type_curie: ClassVar[str] = "BFO:0000003"
    type_name: ClassVar[str] = "occurrent"

    id: Union[str, OccurrentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OccurrentId):
            self.id = OccurrentId(self.id)


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/BiologicalProcessOrActivity"
    type_curie: ClassVar[str] = "biolink:BiologicalProcessOrActivity"
    type_name: ClassVar[str] = "biological process or activity"

    id: Union[str, BiologicalProcessOrActivityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0003674"
    type_curie: ClassVar[str] = "GO:0003674"
    type_name: ClassVar[str] = "molecular activity"

    id: Union[str, MolecularActivityId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)


@dataclass
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/ActivityAndBehavior"
    type_curie: ClassVar[str] = "biolink:ActivityAndBehavior"
    type_name: ClassVar[str] = "activity and behavior"

    id: Union[str, ActivityAndBehaviorId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ActivityAndBehaviorId):
            self.id = ActivityAndBehaviorId(self.id)


@dataclass
class Procedure(Occurrent):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Procedure"
    type_curie: ClassVar[str] = "biolink:Procedure"
    type_name: ClassVar[str] = "procedure"

    id: Union[str, ProcedureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)


@dataclass
class Phenomenon(Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/Phenomenon"
    type_curie: ClassVar[str] = "biolink:Phenomenon"
    type_name: ClassVar[str] = "phenomenon"

    id: Union[str, PhenomenonId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0008150"
    type_curie: ClassVar[str] = "GO:0008150"
    type_name: ClassVar[str] = "biological process"

    id: Union[str, BiologicalProcessId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0007165"
    type_curie: ClassVar[str] = "GO:0007165"
    type_name: ClassVar[str] = "pathway"

    id: Union[str, PathwayId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    type_uri: ClassVar[str] = "https://w3id.org/biolink/vocab/PhysiologicalProcess"
    type_curie: ClassVar[str] = "biolink:PhysiologicalProcess"
    type_name: ClassVar[str] = "physiological process"

    id: Union[str, PhysiologicalProcessId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0005575"
    type_curie: ClassVar[str] = "GO:0005575"
    type_name: ClassVar[str] = "cellular component"

    id: Union[str, CellularComponentId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/GO_0005623"
    type_curie: ClassVar[str] = "GO:0005623"
    type_name: ClassVar[str] = "cell"

    id: Union[str, CellId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellId):
            self.id = CellId(self.id)


@dataclass
class CellLine(Biosample):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/CLO_0000031"
    type_curie: ClassVar[str] = "CLO:0000031"
    type_name: ClassVar[str] = "cell line"

    id: Union[str, CellLineId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["related_to", "interacts_with", "has_phenotype", "expresses", "in_taxon"]

    type_uri: ClassVar[str] = "http://purl.obolibrary.org/obo/UBERON_0010000"
    type_curie: ClassVar[str] = "UBERON:0010000"
    type_name: ClassVar[str] = "gross anatomical structure"

    id: Union[str, GrossAnatomicalStructureId] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)

# ./citygml20/waterBody_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:758469a710dce3cc50e7f9e1eab0d3820acb06f3
# Generated 2016-02-05 01:56:38.811256 by PyXB version 1.2.4 using Python 2.7.10.final.0
# Namespace http://www.opengis.net/citygml/waterbody/2.0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4da3cca8-cba3-11e5-aad4-a0999b07c86f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import citygml20._xlink as _ImportedBinding_citygml20__xlink
import pyxb.binding.datatypes
import citygml20._core as _ImportedBinding_citygml20__core
import citygml20._gml as _ImportedBinding_citygml20__gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/waterbody/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = _ImportedBinding_citygml20__gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding_citygml20__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_core = _ImportedBinding_citygml20__core.Namespace
_Namespace_core.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}BoundedByWaterSurfacePropertyType with content type ELEMENT_ONLY
class BoundedByWaterSurfacePropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a WaterBody to its boundary surfaces, which are of type _WaterBoundarySurface. The
				BoundedByWaterSurfacePropertyType element must either carry a reference to a _WaterBoundarySurface object or contain a
				_WaterBoundarySurface object inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundedByWaterSurfacePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 72, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_WaterBoundarySurface uses Python identifier WaterBoundarySurface
    __WaterBoundarySurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_WaterBoundarySurface'), 'WaterBoundarySurface', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_opengis_netcitygmlwaterbody2_0_WaterBoundarySurface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 101, 1), )

    
    WaterBoundarySurface = property(__WaterBoundarySurface.value, __WaterBoundarySurface.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml20__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml20__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml20__xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml20__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml20__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml20__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlwaterbody2_0_BoundedByWaterSurfacePropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml20__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __WaterBoundarySurface.name() : __WaterBoundarySurface
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
Namespace.addCategoryObject('typeBinding', 'BoundedByWaterSurfacePropertyType', BoundedByWaterSurfacePropertyType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterObjectType with content type ELEMENT_ONLY
class AbstractWaterObjectType (_ImportedBinding_citygml20__core.AbstractCityObjectType):
    """Type describing the abstract superclass for water objects. As subclass of _CityObject, a _WaterObject
				inherits all attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractWaterObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 22, 1)
    _ElementMap = _ImportedBinding_citygml20__core.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_citygml20__core.AbstractCityObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_citygml20__core.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterObject uses Python identifier GenericApplicationPropertyOfWaterObject
    __GenericApplicationPropertyOfWaterObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterObject'), 'GenericApplicationPropertyOfWaterObject', '__httpwww_opengis_netcitygmlwaterbody2_0_AbstractWaterObjectType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterObject', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 39, 1), )

    
    GenericApplicationPropertyOfWaterObject = property(__GenericApplicationPropertyOfWaterObject.value, __GenericApplicationPropertyOfWaterObject.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfWaterObject.name() : __GenericApplicationPropertyOfWaterObject
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractWaterObjectType', AbstractWaterObjectType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType with content type ELEMENT_ONLY
class AbstractWaterBoundarySurfaceType (_ImportedBinding_citygml20__core.AbstractCityObjectType):
    """A WaterBoundarySurface is a thematic object which classifies surfaces bounding a water body.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractWaterBoundarySurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 84, 1)
    _ElementMap = _ImportedBinding_citygml20__core.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_citygml20__core.AbstractCityObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_citygml20__core.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod2Surface uses Python identifier lod2Surface
    __lod2Surface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface'), 'lod2Surface', '__httpwww_opengis_netcitygmlwaterbody2_0_AbstractWaterBoundarySurfaceType_httpwww_opengis_netcitygmlwaterbody2_0lod2Surface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5), )

    
    lod2Surface = property(__lod2Surface.value, __lod2Surface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod3Surface uses Python identifier lod3Surface
    __lod3Surface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface'), 'lod3Surface', '__httpwww_opengis_netcitygmlwaterbody2_0_AbstractWaterBoundarySurfaceType_httpwww_opengis_netcitygmlwaterbody2_0lod3Surface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5), )

    
    lod3Surface = property(__lod3Surface.value, __lod3Surface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod4Surface uses Python identifier lod4Surface
    __lod4Surface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface'), 'lod4Surface', '__httpwww_opengis_netcitygmlwaterbody2_0_AbstractWaterBoundarySurfaceType_httpwww_opengis_netcitygmlwaterbody2_0lod4Surface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5), )

    
    lod4Surface = property(__lod4Surface.value, __lod4Surface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterBoundarySurface uses Python identifier GenericApplicationPropertyOfWaterBoundarySurface
    __GenericApplicationPropertyOfWaterBoundarySurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface'), 'GenericApplicationPropertyOfWaterBoundarySurface', '__httpwww_opengis_netcitygmlwaterbody2_0_AbstractWaterBoundarySurfaceType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterBoundarySurface', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 104, 1), )

    
    GenericApplicationPropertyOfWaterBoundarySurface = property(__GenericApplicationPropertyOfWaterBoundarySurface.value, __GenericApplicationPropertyOfWaterBoundarySurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __lod2Surface.name() : __lod2Surface,
        __lod3Surface.name() : __lod3Surface,
        __lod4Surface.name() : __lod4Surface,
        __GenericApplicationPropertyOfWaterBoundarySurface.name() : __GenericApplicationPropertyOfWaterBoundarySurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractWaterBoundarySurfaceType', AbstractWaterBoundarySurfaceType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}WaterBodyType with content type ELEMENT_ONLY
class WaterBodyType (AbstractWaterObjectType):
    """Type describing Water Bodies, e.g., lakes, rivers. As subclass of _CityObject, a WaterBody inherits all
				attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WaterBodyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 41, 1)
    _ElementMap = AbstractWaterObjectType._ElementMap.copy()
    _AttributeMap = AbstractWaterObjectType._AttributeMap.copy()
    # Base type is AbstractWaterObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfWaterObject ({http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterObject) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterObjectType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0class', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 50, 5), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0function', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 51, 5), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0usage', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 52, 5), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod0MultiCurve uses Python identifier lod0MultiCurve
    __lod0MultiCurve = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiCurve'), 'lod0MultiCurve', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod0MultiCurve', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 53, 5), )

    
    lod0MultiCurve = property(__lod0MultiCurve.value, __lod0MultiCurve.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod0MultiSurface uses Python identifier lod0MultiSurface
    __lod0MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiSurface'), 'lod0MultiSurface', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod0MultiSurface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 54, 5), )

    
    lod0MultiSurface = property(__lod0MultiSurface.value, __lod0MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod1MultiCurve uses Python identifier lod1MultiCurve
    __lod1MultiCurve = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiCurve'), 'lod1MultiCurve', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod1MultiCurve', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 55, 5), )

    
    lod1MultiCurve = property(__lod1MultiCurve.value, __lod1MultiCurve.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod1MultiSurface uses Python identifier lod1MultiSurface
    __lod1MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface'), 'lod1MultiSurface', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod1MultiSurface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 56, 5), )

    
    lod1MultiSurface = property(__lod1MultiSurface.value, __lod1MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod1Solid uses Python identifier lod1Solid
    __lod1Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid'), 'lod1Solid', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod1Solid', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 57, 5), )

    
    lod1Solid = property(__lod1Solid.value, __lod1Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod2Solid uses Python identifier lod2Solid
    __lod2Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid'), 'lod2Solid', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod2Solid', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 58, 5), )

    
    lod2Solid = property(__lod2Solid.value, __lod2Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod3Solid uses Python identifier lod3Solid
    __lod3Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid'), 'lod3Solid', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod3Solid', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 59, 5), )

    
    lod3Solid = property(__lod3Solid.value, __lod3Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}lod4Solid uses Python identifier lod4Solid
    __lod4Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), 'lod4Solid', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0lod4Solid', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 60, 5), )

    
    lod4Solid = property(__lod4Solid.value, __lod4Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}boundedBy uses Python identifier boundedBy_
    __boundedBy_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), 'boundedBy_', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0boundedBy', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 61, 5), )

    
    boundedBy_ = property(__boundedBy_.value, __boundedBy_.set, None, None)

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterBody uses Python identifier GenericApplicationPropertyOfWaterBody
    __GenericApplicationPropertyOfWaterBody = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBody'), 'GenericApplicationPropertyOfWaterBody', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterBodyType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterBody', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 70, 1), )

    
    GenericApplicationPropertyOfWaterBody = property(__GenericApplicationPropertyOfWaterBody.value, __GenericApplicationPropertyOfWaterBody.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __lod0MultiCurve.name() : __lod0MultiCurve,
        __lod0MultiSurface.name() : __lod0MultiSurface,
        __lod1MultiCurve.name() : __lod1MultiCurve,
        __lod1MultiSurface.name() : __lod1MultiSurface,
        __lod1Solid.name() : __lod1Solid,
        __lod2Solid.name() : __lod2Solid,
        __lod3Solid.name() : __lod3Solid,
        __lod4Solid.name() : __lod4Solid,
        __boundedBy_.name() : __boundedBy_,
        __GenericApplicationPropertyOfWaterBody.name() : __GenericApplicationPropertyOfWaterBody
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WaterBodyType', WaterBodyType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}WaterSurfaceType with content type ELEMENT_ONLY
class WaterSurfaceType (AbstractWaterBoundarySurfaceType):
    """Type describing the surface of a water body, which separates the water from the air. As subclass of
				_CityObject, a WaterSurface inherits all attributes and relations, in particular an id, names, external references, and
				generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WaterSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 106, 1)
    _ElementMap = AbstractWaterBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractWaterBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractWaterBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod2Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod2Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod3Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod3Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod4Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod4Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfWaterBoundarySurface ({http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterBoundarySurface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}waterLevel uses Python identifier waterLevel
    __waterLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'waterLevel'), 'waterLevel', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterSurfaceType_httpwww_opengis_netcitygmlwaterbody2_0waterLevel', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 115, 5), )

    
    waterLevel = property(__waterLevel.value, __waterLevel.set, None, 'Type for the specification of the level of a water surface. The optional attribute waterLevel of a\n\t\t\t\t\t\t\t\tWaterSurface can be used to describe the water level, for which the given 3D surface geometry was acquired. This\n\t\t\t\t\t\t\t\tis especially important, when the water body is influenced by the tide. The values of this type are defined in\n\t\t\t\t\t\t\t\texternal code lists.')

    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterSurface uses Python identifier GenericApplicationPropertyOfWaterSurface
    __GenericApplicationPropertyOfWaterSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterSurface'), 'GenericApplicationPropertyOfWaterSurface', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterSurfaceType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterSurface', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 131, 1), )

    
    GenericApplicationPropertyOfWaterSurface = property(__GenericApplicationPropertyOfWaterSurface.value, __GenericApplicationPropertyOfWaterSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __waterLevel.name() : __waterLevel,
        __GenericApplicationPropertyOfWaterSurface.name() : __GenericApplicationPropertyOfWaterSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WaterSurfaceType', WaterSurfaceType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}WaterGroundSurfaceType with content type ELEMENT_ONLY
class WaterGroundSurfaceType (AbstractWaterBoundarySurfaceType):
    """Type describing the ground surface of a water body, i.e. the boundary to the digital terrain model. As
				subclass of _CityObject, a WaterGroundSurface inherits all attributes and relations, in particular an id, names, external
				references, and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WaterGroundSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 133, 1)
    _ElementMap = AbstractWaterBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractWaterBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractWaterBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod2Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod2Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod3Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod3Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod4Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod4Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfWaterBoundarySurface ({http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterBoundarySurface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterGroundSurface uses Python identifier GenericApplicationPropertyOfWaterGroundSurface
    __GenericApplicationPropertyOfWaterGroundSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterGroundSurface'), 'GenericApplicationPropertyOfWaterGroundSurface', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterGroundSurfaceType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterGroundSurface', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 150, 1), )

    
    GenericApplicationPropertyOfWaterGroundSurface = property(__GenericApplicationPropertyOfWaterGroundSurface.value, __GenericApplicationPropertyOfWaterGroundSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfWaterGroundSurface.name() : __GenericApplicationPropertyOfWaterGroundSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WaterGroundSurfaceType', WaterGroundSurfaceType)


# Complex type {http://www.opengis.net/citygml/waterbody/2.0}WaterClosureSurfaceType with content type ELEMENT_ONLY
class WaterClosureSurfaceType (AbstractWaterBoundarySurfaceType):
    """Type describing the closure surface between water bodys. As subclass of _CityObject, a WaterClosureSurface
				inherits all attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WaterClosureSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 152, 1)
    _ElementMap = AbstractWaterBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractWaterBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractWaterBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod2Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod2Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod3Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod3Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element lod4Surface ({http://www.opengis.net/citygml/waterbody/2.0}lod4Surface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfWaterBoundarySurface ({http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterBoundarySurface) inherited from {http://www.opengis.net/citygml/waterbody/2.0}AbstractWaterBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/waterbody/2.0}_GenericApplicationPropertyOfWaterClosureSurface uses Python identifier GenericApplicationPropertyOfWaterClosureSurface
    __GenericApplicationPropertyOfWaterClosureSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterClosureSurface'), 'GenericApplicationPropertyOfWaterClosureSurface', '__httpwww_opengis_netcitygmlwaterbody2_0_WaterClosureSurfaceType_httpwww_opengis_netcitygmlwaterbody2_0_GenericApplicationPropertyOfWaterClosureSurface', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 169, 1), )

    
    GenericApplicationPropertyOfWaterClosureSurface = property(__GenericApplicationPropertyOfWaterClosureSurface.value, __GenericApplicationPropertyOfWaterClosureSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfWaterClosureSurface.name() : __GenericApplicationPropertyOfWaterClosureSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WaterClosureSurfaceType', WaterClosureSurfaceType)


GenericApplicationPropertyOfWaterObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterObject'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterObject.name().localName(), GenericApplicationPropertyOfWaterObject)

GenericApplicationPropertyOfWaterBody = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBody'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterBody.name().localName(), GenericApplicationPropertyOfWaterBody)

GenericApplicationPropertyOfWaterBoundarySurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 104, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterBoundarySurface.name().localName(), GenericApplicationPropertyOfWaterBoundarySurface)

GenericApplicationPropertyOfWaterSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 131, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterSurface.name().localName(), GenericApplicationPropertyOfWaterSurface)

GenericApplicationPropertyOfWaterGroundSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterGroundSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 150, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterGroundSurface.name().localName(), GenericApplicationPropertyOfWaterGroundSurface)

GenericApplicationPropertyOfWaterClosureSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterClosureSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 169, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWaterClosureSurface.name().localName(), GenericApplicationPropertyOfWaterClosureSurface)

WaterObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_WaterObject'), AbstractWaterObjectType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 37, 1))
Namespace.addCategoryObject('elementBinding', WaterObject.name().localName(), WaterObject)

WaterBoundarySurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_WaterBoundarySurface'), AbstractWaterBoundarySurfaceType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 101, 1))
Namespace.addCategoryObject('elementBinding', WaterBoundarySurface.name().localName(), WaterBoundarySurface)

WaterBody = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaterBody'), WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', WaterBody.name().localName(), WaterBody)

WaterSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaterSurface'), WaterSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 129, 1))
Namespace.addCategoryObject('elementBinding', WaterSurface.name().localName(), WaterSurface)

WaterGroundSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaterGroundSurface'), WaterGroundSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 148, 1))
Namespace.addCategoryObject('elementBinding', WaterGroundSurface.name().localName(), WaterGroundSurface)

WaterClosureSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaterClosureSurface'), WaterClosureSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 167, 1))
Namespace.addCategoryObject('elementBinding', WaterClosureSurface.name().localName(), WaterClosureSurface)



BoundedByWaterSurfacePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_WaterBoundarySurface'), AbstractWaterBoundarySurfaceType, abstract=pyxb.binding.datatypes.boolean(1), scope=BoundedByWaterSurfacePropertyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 101, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 78, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BoundedByWaterSurfacePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_WaterBoundarySurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 79, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BoundedByWaterSurfacePropertyType._Automaton = _BuildAutomaton()




AbstractWaterObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterObject'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractWaterObjectType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 39, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 31, 5))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 31, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractWaterObjectType._Automaton = _BuildAutomaton_()




AbstractWaterBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface'), _ImportedBinding_citygml20__gml.SurfacePropertyType, scope=AbstractWaterBoundarySurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5)))

AbstractWaterBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface'), _ImportedBinding_citygml20__gml.SurfacePropertyType, scope=AbstractWaterBoundarySurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5)))

AbstractWaterBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface'), _ImportedBinding_citygml20__gml.SurfacePropertyType, scope=AbstractWaterBoundarySurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5)))

AbstractWaterBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractWaterBoundarySurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 104, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(AbstractWaterBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractWaterBoundarySurfaceType._Automaton = _BuildAutomaton_2()




WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), _ImportedBinding_citygml20__gml.CodeType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 50, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), _ImportedBinding_citygml20__gml.CodeType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 51, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), _ImportedBinding_citygml20__gml.CodeType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 52, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiCurve'), _ImportedBinding_citygml20__gml.MultiCurvePropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 53, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiSurface'), _ImportedBinding_citygml20__gml.MultiSurfacePropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 54, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiCurve'), _ImportedBinding_citygml20__gml.MultiCurvePropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 55, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface'), _ImportedBinding_citygml20__gml.MultiSurfacePropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 56, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid'), _ImportedBinding_citygml20__gml.SolidPropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 57, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid'), _ImportedBinding_citygml20__gml.SolidPropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 58, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid'), _ImportedBinding_citygml20__gml.SolidPropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 59, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), _ImportedBinding_citygml20__gml.SolidPropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 60, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), BoundedByWaterSurfacePropertyType, scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 61, 5)))

WaterBodyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBody'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WaterBodyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 70, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 31, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 50, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 51, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 52, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 53, 5))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 54, 5))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 55, 5))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 56, 5))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 57, 5))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 58, 5))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 59, 5))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 60, 5))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 61, 5))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 62, 5))
    counters.add(cc_25)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 31, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 50, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 51, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 52, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiCurve')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 53, 5))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod0MultiSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 54, 5))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiCurve')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 55, 5))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 56, 5))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 57, 5))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 58, 5))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 59, 5))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 60, 5))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 61, 5))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(WaterBodyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBody')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 62, 5))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    st_25._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WaterBodyType._Automaton = _BuildAutomaton_3()




WaterSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'waterLevel'), _ImportedBinding_citygml20__gml.CodeType, scope=WaterSurfaceType, documentation='Type for the specification of the level of a water surface. The optional attribute waterLevel of a\n\t\t\t\t\t\t\t\tWaterSurface can be used to describe the water level, for which the given 3D surface geometry was acquired. This\n\t\t\t\t\t\t\t\tis especially important, when the water body is influenced by the tide. The values of this type are defined in\n\t\t\t\t\t\t\t\texternal code lists.', location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 115, 5)))

WaterSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WaterSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 131, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 115, 5))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 123, 5))
    counters.add(cc_17)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'waterLevel')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 115, 5))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(WaterSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 123, 5))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WaterSurfaceType._Automaton = _BuildAutomaton_4()




WaterGroundSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterGroundSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WaterGroundSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 150, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 142, 5))
    counters.add(cc_16)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(WaterGroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterGroundSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 142, 5))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WaterGroundSurfaceType._Automaton = _BuildAutomaton_5()




WaterClosureSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterClosureSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WaterClosureSurfaceType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 169, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 161, 5))
    counters.add(cc_16)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 92, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 93, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Surface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 94, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterBoundarySurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 95, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(WaterClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWaterClosureSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/waterBody.xsd', 161, 5))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WaterClosureSurfaceType._Automaton = _BuildAutomaton_6()


WaterObject._setSubstitutionGroup(_ImportedBinding_citygml20__core.CityObject)

WaterBoundarySurface._setSubstitutionGroup(_ImportedBinding_citygml20__core.CityObject)

WaterBody._setSubstitutionGroup(WaterObject)

WaterSurface._setSubstitutionGroup(WaterBoundarySurface)

WaterGroundSurface._setSubstitutionGroup(WaterBoundarySurface)

WaterClosureSurface._setSubstitutionGroup(WaterBoundarySurface)

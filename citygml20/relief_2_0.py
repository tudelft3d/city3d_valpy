# ./citygml20/relief_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9e22771d63d76e71463410f78b93deedc21721e2
# Generated 2016-02-05 01:56:38.811812 by PyXB version 1.2.4 using Python 2.7.10.final.0
# Namespace http://www.opengis.net/citygml/relief/2.0

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
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/relief/2.0', create_if_missing=True)
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


# Complex type {http://www.opengis.net/citygml/relief/2.0}ReliefComponentPropertyType with content type ELEMENT_ONLY
class ReliefComponentPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a ReliefFeature to its components. The ReliefComponentPropertyType element must
				either carry a reference to a _ReliefComponent object or contain a _ReliefComponent object inline, but neither both nor
				none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReliefComponentPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 64, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/relief/2.0}_ReliefComponent uses Python identifier ReliefComponent
    __ReliefComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_ReliefComponent'), 'ReliefComponent', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_opengis_netcitygmlrelief2_0_ReliefComponent', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 60, 1), )

    
    ReliefComponent = property(__ReliefComponent.value, __ReliefComponent.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml20__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml20__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml20__xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml20__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml20__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml20__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlrelief2_0_ReliefComponentPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml20__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __ReliefComponent.name() : __ReliefComponent
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
Namespace.addCategoryObject('typeBinding', 'ReliefComponentPropertyType', ReliefComponentPropertyType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}tinPropertyType with content type ELEMENT_ONLY
class tinPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a TINRelief to its components. The tinPropertyType element must either carry a
				reference to a gml:TriangulatedSurface object or contain a gml:TriangulatedSurface object inline, but neither both nor
				none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tinPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 157, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}TriangulatedSurface uses Python identifier TriangulatedSurface
    __TriangulatedSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'TriangulatedSurface'), 'TriangulatedSurface', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_opengis_netgmlTriangulatedSurface', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/geometryPrimitives.xsd', 1364, 1), )

    
    TriangulatedSurface = property(__TriangulatedSurface.value, __TriangulatedSurface.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml20__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml20__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml20__xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml20__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml20__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml20__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlrelief2_0_tinPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml20__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __TriangulatedSurface.name() : __TriangulatedSurface
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
Namespace.addCategoryObject('typeBinding', 'tinPropertyType', tinPropertyType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}gridPropertyType with content type ELEMENT_ONLY
class gridPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a RasterReliefType to its components. The gridPropertyType element must either
				carry a reference to a gml:RectifiedGridCoverage object or contain a gml:RectifiedGridCoverage object inline, but neither
				both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gridPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 169, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/gml}RectifiedGridCoverage uses Python identifier RectifiedGridCoverage
    __RectifiedGridCoverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_gml, 'RectifiedGridCoverage'), 'RectifiedGridCoverage', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_opengis_netgmlRectifiedGridCoverage', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/coverage.xsd', 423, 1), )

    
    RectifiedGridCoverage = property(__RectifiedGridCoverage.value, __RectifiedGridCoverage.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml20__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml20__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml20__xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml20__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml20__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml20__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlrelief2_0_gridPropertyType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml20__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/1999/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __RectifiedGridCoverage.name() : __RectifiedGridCoverage
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
Namespace.addCategoryObject('typeBinding', 'gridPropertyType', gridPropertyType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}ReliefFeatureType with content type ELEMENT_ONLY
class ReliefFeatureType (_ImportedBinding_citygml20__core.AbstractCityObjectType):
    """Type describing the features of the Digital Terrain Model. As subclass of _CityObject, a ReliefFeature
				inherits all attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReliefFeatureType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 22, 1)
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
    
    # Element {http://www.opengis.net/citygml/relief/2.0}lod uses Python identifier lod
    __lod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod'), 'lod', '__httpwww_opengis_netcitygmlrelief2_0_ReliefFeatureType_httpwww_opengis_netcitygmlrelief2_0lod', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 31, 5), )

    
    lod = property(__lod.value, __lod.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}reliefComponent uses Python identifier reliefComponent
    __reliefComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reliefComponent'), 'reliefComponent', '__httpwww_opengis_netcitygmlrelief2_0_ReliefFeatureType_httpwww_opengis_netcitygmlrelief2_0reliefComponent', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 32, 5), )

    
    reliefComponent = property(__reliefComponent.value, __reliefComponent.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefFeature uses Python identifier GenericApplicationPropertyOfReliefFeature
    __GenericApplicationPropertyOfReliefFeature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefFeature'), 'GenericApplicationPropertyOfReliefFeature', '__httpwww_opengis_netcitygmlrelief2_0_ReliefFeatureType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfReliefFeature', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 41, 1), )

    
    GenericApplicationPropertyOfReliefFeature = property(__GenericApplicationPropertyOfReliefFeature.value, __GenericApplicationPropertyOfReliefFeature.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __lod.name() : __lod,
        __reliefComponent.name() : __reliefComponent,
        __GenericApplicationPropertyOfReliefFeature.name() : __GenericApplicationPropertyOfReliefFeature
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReliefFeatureType', ReliefFeatureType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType with content type ELEMENT_ONLY
class AbstractReliefComponentType (_ImportedBinding_citygml20__core.AbstractCityObjectType):
    """Type describing the components of a relief feature - either a TIN, a Grid, mass points or break lines. As
				subclass of _CityObject, a ReliefComponent inherits all attributes and relations, in particular an id, names, external
				references, and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractReliefComponentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 43, 1)
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
    
    # Element {http://www.opengis.net/citygml/relief/2.0}lod uses Python identifier lod
    __lod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod'), 'lod', '__httpwww_opengis_netcitygmlrelief2_0_AbstractReliefComponentType_httpwww_opengis_netcitygmlrelief2_0lod', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5), )

    
    lod = property(__lod.value, __lod.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extent'), 'extent', '__httpwww_opengis_netcitygmlrelief2_0_AbstractReliefComponentType_httpwww_opengis_netcitygmlrelief2_0extent', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5), )

    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefComponent uses Python identifier GenericApplicationPropertyOfReliefComponent
    __GenericApplicationPropertyOfReliefComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent'), 'GenericApplicationPropertyOfReliefComponent', '__httpwww_opengis_netcitygmlrelief2_0_AbstractReliefComponentType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfReliefComponent', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 62, 1), )

    
    GenericApplicationPropertyOfReliefComponent = property(__GenericApplicationPropertyOfReliefComponent.value, __GenericApplicationPropertyOfReliefComponent.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __lod.name() : __lod,
        __extent.name() : __extent,
        __GenericApplicationPropertyOfReliefComponent.name() : __GenericApplicationPropertyOfReliefComponent
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractReliefComponentType', AbstractReliefComponentType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}TINReliefType with content type ELEMENT_ONLY
class TINReliefType (AbstractReliefComponentType):
    """Type describing the TIN component of a relief feature. As subclass of _CityObject, a TINRelief inherits
				all attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TINReliefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 76, 1)
    _ElementMap = AbstractReliefComponentType._ElementMap.copy()
    _AttributeMap = AbstractReliefComponentType._AttributeMap.copy()
    # Base type is AbstractReliefComponentType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod ({http://www.opengis.net/citygml/relief/2.0}lod) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element extent ({http://www.opengis.net/citygml/relief/2.0}extent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element GenericApplicationPropertyOfReliefComponent ({http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefComponent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element {http://www.opengis.net/citygml/relief/2.0}tin uses Python identifier tin
    __tin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tin'), 'tin', '__httpwww_opengis_netcitygmlrelief2_0_TINReliefType_httpwww_opengis_netcitygmlrelief2_0tin', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 85, 5), )

    
    tin = property(__tin.value, __tin.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfTinRelief uses Python identifier GenericApplicationPropertyOfTinRelief
    __GenericApplicationPropertyOfTinRelief = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfTinRelief'), 'GenericApplicationPropertyOfTinRelief', '__httpwww_opengis_netcitygmlrelief2_0_TINReliefType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfTinRelief', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 94, 1), )

    
    GenericApplicationPropertyOfTinRelief = property(__GenericApplicationPropertyOfTinRelief.value, __GenericApplicationPropertyOfTinRelief.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __tin.name() : __tin,
        __GenericApplicationPropertyOfTinRelief.name() : __GenericApplicationPropertyOfTinRelief
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TINReliefType', TINReliefType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}RasterReliefType with content type ELEMENT_ONLY
class RasterReliefType (AbstractReliefComponentType):
    """Type describing the raster component of a relief feature. As subclass of _CityObject, a RasterRelief
				inherits all attributes and relations, in particular an id, names, external references, and generalization relations.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RasterReliefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 96, 1)
    _ElementMap = AbstractReliefComponentType._ElementMap.copy()
    _AttributeMap = AbstractReliefComponentType._AttributeMap.copy()
    # Base type is AbstractReliefComponentType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod ({http://www.opengis.net/citygml/relief/2.0}lod) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element extent ({http://www.opengis.net/citygml/relief/2.0}extent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element GenericApplicationPropertyOfReliefComponent ({http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefComponent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element {http://www.opengis.net/citygml/relief/2.0}grid uses Python identifier grid
    __grid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'grid'), 'grid', '__httpwww_opengis_netcitygmlrelief2_0_RasterReliefType_httpwww_opengis_netcitygmlrelief2_0grid', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 105, 5), )

    
    grid = property(__grid.value, __grid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfRasterRelief uses Python identifier GenericApplicationPropertyOfRasterRelief
    __GenericApplicationPropertyOfRasterRelief = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRasterRelief'), 'GenericApplicationPropertyOfRasterRelief', '__httpwww_opengis_netcitygmlrelief2_0_RasterReliefType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfRasterRelief', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 114, 1), )

    
    GenericApplicationPropertyOfRasterRelief = property(__GenericApplicationPropertyOfRasterRelief.value, __GenericApplicationPropertyOfRasterRelief.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __grid.name() : __grid,
        __GenericApplicationPropertyOfRasterRelief.name() : __GenericApplicationPropertyOfRasterRelief
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RasterReliefType', RasterReliefType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}MassPointReliefType with content type ELEMENT_ONLY
class MassPointReliefType (AbstractReliefComponentType):
    """Type describing the mass point component of a relief feature. As subclass of _CityObject, a MassPoint
				Relief inherits all attributes and relations, in particular an id, names, external references, and generalization
				relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassPointReliefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 116, 1)
    _ElementMap = AbstractReliefComponentType._ElementMap.copy()
    _AttributeMap = AbstractReliefComponentType._AttributeMap.copy()
    # Base type is AbstractReliefComponentType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod ({http://www.opengis.net/citygml/relief/2.0}lod) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element extent ({http://www.opengis.net/citygml/relief/2.0}extent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element GenericApplicationPropertyOfReliefComponent ({http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefComponent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element {http://www.opengis.net/citygml/relief/2.0}reliefPoints uses Python identifier reliefPoints
    __reliefPoints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reliefPoints'), 'reliefPoints', '__httpwww_opengis_netcitygmlrelief2_0_MassPointReliefType_httpwww_opengis_netcitygmlrelief2_0reliefPoints', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 125, 5), )

    
    reliefPoints = property(__reliefPoints.value, __reliefPoints.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfMassPointRelief uses Python identifier GenericApplicationPropertyOfMassPointRelief
    __GenericApplicationPropertyOfMassPointRelief = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfMassPointRelief'), 'GenericApplicationPropertyOfMassPointRelief', '__httpwww_opengis_netcitygmlrelief2_0_MassPointReliefType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfMassPointRelief', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 134, 1), )

    
    GenericApplicationPropertyOfMassPointRelief = property(__GenericApplicationPropertyOfMassPointRelief.value, __GenericApplicationPropertyOfMassPointRelief.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __reliefPoints.name() : __reliefPoints,
        __GenericApplicationPropertyOfMassPointRelief.name() : __GenericApplicationPropertyOfMassPointRelief
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MassPointReliefType', MassPointReliefType)


# Complex type {http://www.opengis.net/citygml/relief/2.0}BreaklineReliefType with content type ELEMENT_ONLY
class BreaklineReliefType (AbstractReliefComponentType):
    """Type describing the break line Component of a relief feature. A break line relief consists of break lines
				or ridgeOrValleyLines. As subclass of _CityObject, a BreaklineRelief inherits all attributes and relations, in particular
				an id, names, external references, and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BreaklineReliefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 136, 1)
    _ElementMap = AbstractReliefComponentType._ElementMap.copy()
    _AttributeMap = AbstractReliefComponentType._AttributeMap.copy()
    # Base type is AbstractReliefComponentType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element lod ({http://www.opengis.net/citygml/relief/2.0}lod) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element extent ({http://www.opengis.net/citygml/relief/2.0}extent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element GenericApplicationPropertyOfReliefComponent ({http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfReliefComponent) inherited from {http://www.opengis.net/citygml/relief/2.0}AbstractReliefComponentType
    
    # Element {http://www.opengis.net/citygml/relief/2.0}ridgeOrValleyLines uses Python identifier ridgeOrValleyLines
    __ridgeOrValleyLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ridgeOrValleyLines'), 'ridgeOrValleyLines', '__httpwww_opengis_netcitygmlrelief2_0_BreaklineReliefType_httpwww_opengis_netcitygmlrelief2_0ridgeOrValleyLines', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 145, 5), )

    
    ridgeOrValleyLines = property(__ridgeOrValleyLines.value, __ridgeOrValleyLines.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}breaklines uses Python identifier breaklines
    __breaklines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'breaklines'), 'breaklines', '__httpwww_opengis_netcitygmlrelief2_0_BreaklineReliefType_httpwww_opengis_netcitygmlrelief2_0breaklines', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 146, 5), )

    
    breaklines = property(__breaklines.value, __breaklines.set, None, None)

    
    # Element {http://www.opengis.net/citygml/relief/2.0}_GenericApplicationPropertyOfBreaklineRelief uses Python identifier GenericApplicationPropertyOfBreaklineRelief
    __GenericApplicationPropertyOfBreaklineRelief = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBreaklineRelief'), 'GenericApplicationPropertyOfBreaklineRelief', '__httpwww_opengis_netcitygmlrelief2_0_BreaklineReliefType_httpwww_opengis_netcitygmlrelief2_0_GenericApplicationPropertyOfBreaklineRelief', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 155, 1), )

    
    GenericApplicationPropertyOfBreaklineRelief = property(__GenericApplicationPropertyOfBreaklineRelief.value, __GenericApplicationPropertyOfBreaklineRelief.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __ridgeOrValleyLines.name() : __ridgeOrValleyLines,
        __breaklines.name() : __breaklines,
        __GenericApplicationPropertyOfBreaklineRelief.name() : __GenericApplicationPropertyOfBreaklineRelief
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BreaklineReliefType', BreaklineReliefType)


GenericApplicationPropertyOfReliefFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefFeature'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfReliefFeature.name().localName(), GenericApplicationPropertyOfReliefFeature)

GenericApplicationPropertyOfReliefComponent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 62, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfReliefComponent.name().localName(), GenericApplicationPropertyOfReliefComponent)

GenericApplicationPropertyOfTinRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfTinRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfTinRelief.name().localName(), GenericApplicationPropertyOfTinRelief)

GenericApplicationPropertyOfRasterRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRasterRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfRasterRelief.name().localName(), GenericApplicationPropertyOfRasterRelief)

GenericApplicationPropertyOfMassPointRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfMassPointRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 134, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfMassPointRelief.name().localName(), GenericApplicationPropertyOfMassPointRelief)

GenericApplicationPropertyOfBreaklineRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBreaklineRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 155, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBreaklineRelief.name().localName(), GenericApplicationPropertyOfBreaklineRelief)

Elevation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Elevation'), _ImportedBinding_citygml20__gml.LengthType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 184, 1))
Namespace.addCategoryObject('elementBinding', Elevation.name().localName(), Elevation)

ReliefFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReliefFeature'), ReliefFeatureType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', ReliefFeature.name().localName(), ReliefFeature)

ReliefComponent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_ReliefComponent'), AbstractReliefComponentType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 60, 1))
Namespace.addCategoryObject('elementBinding', ReliefComponent.name().localName(), ReliefComponent)

TINRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TINRelief'), TINReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 92, 1))
Namespace.addCategoryObject('elementBinding', TINRelief.name().localName(), TINRelief)

RasterRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RasterRelief'), RasterReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 112, 1))
Namespace.addCategoryObject('elementBinding', RasterRelief.name().localName(), RasterRelief)

MassPointRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MassPointRelief'), MassPointReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 132, 1))
Namespace.addCategoryObject('elementBinding', MassPointRelief.name().localName(), MassPointRelief)

BreaklineRelief = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BreaklineRelief'), BreaklineReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 153, 1))
Namespace.addCategoryObject('elementBinding', BreaklineRelief.name().localName(), BreaklineRelief)



ReliefComponentPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_ReliefComponent'), AbstractReliefComponentType, abstract=pyxb.binding.datatypes.boolean(1), scope=ReliefComponentPropertyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 60, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 70, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReliefComponentPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_ReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 71, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReliefComponentPropertyType._Automaton = _BuildAutomaton()




tinPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'TriangulatedSurface'), _ImportedBinding_citygml20__gml.TriangulatedSurfaceType, scope=tinPropertyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/geometryPrimitives.xsd', 1364, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 163, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tinPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'TriangulatedSurface')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 164, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tinPropertyType._Automaton = _BuildAutomaton_()




gridPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_gml, 'RectifiedGridCoverage'), _ImportedBinding_citygml20__gml.RectifiedGridCoverageType, scope=gridPropertyType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/coverage.xsd', 423, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 175, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gridPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'RectifiedGridCoverage')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 176, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
gridPropertyType._Automaton = _BuildAutomaton_2()




ReliefFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod'), _ImportedBinding_citygml20__core.integerBetween0and4, scope=ReliefFeatureType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 31, 5)))

ReliefFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reliefComponent'), ReliefComponentPropertyType, scope=ReliefFeatureType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 32, 5)))

ReliefFeatureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefFeature'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=ReliefFeatureType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 41, 1)))

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
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 33, 5))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 31, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 32, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ReliefFeatureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefFeature')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 33, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReliefFeatureType._Automaton = _BuildAutomaton_3()




AbstractReliefComponentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod'), _ImportedBinding_citygml20__core.integerBetween0and4, scope=AbstractReliefComponentType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5)))

AbstractReliefComponentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extent'), _ImportedBinding_citygml20__gml.PolygonPropertyType, scope=AbstractReliefComponentType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5)))

AbstractReliefComponentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractReliefComponentType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 62, 1)))

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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AbstractReliefComponentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AbstractReliefComponentType._Automaton = _BuildAutomaton_4()




TINReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tin'), tinPropertyType, scope=TINReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 85, 5)))

TINReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfTinRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=TINReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 94, 1)))

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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 86, 5))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tin')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 85, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(TINReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfTinRelief')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 86, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TINReliefType._Automaton = _BuildAutomaton_5()




RasterReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'grid'), gridPropertyType, scope=RasterReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 105, 5)))

RasterReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRasterRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=RasterReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 114, 1)))

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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 106, 5))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'grid')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 105, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(RasterReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRasterRelief')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 106, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RasterReliefType._Automaton = _BuildAutomaton_6()




MassPointReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reliefPoints'), _ImportedBinding_citygml20__gml.MultiPointPropertyType, scope=MassPointReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 125, 5)))

MassPointReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfMassPointRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=MassPointReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 134, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 126, 5))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reliefPoints')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 125, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(MassPointReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfMassPointRelief')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 126, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MassPointReliefType._Automaton = _BuildAutomaton_7()




BreaklineReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ridgeOrValleyLines'), _ImportedBinding_citygml20__gml.MultiCurvePropertyType, scope=BreaklineReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 145, 5)))

BreaklineReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'breaklines'), _ImportedBinding_citygml20__gml.MultiCurvePropertyType, scope=BreaklineReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 146, 5)))

BreaklineReliefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBreaklineRelief'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BreaklineReliefType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 155, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 145, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 146, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 147, 5))
    counters.add(cc_16)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 52, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 53, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfReliefComponent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 54, 5))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ridgeOrValleyLines')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 145, 5))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'breaklines')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 146, 5))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(BreaklineReliefType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBreaklineRelief')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/relief.xsd', 147, 5))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BreaklineReliefType._Automaton = _BuildAutomaton_8()


Elevation._setSubstitutionGroup(_ImportedBinding_citygml20__gml.Object)

ReliefFeature._setSubstitutionGroup(_ImportedBinding_citygml20__core.CityObject)

ReliefComponent._setSubstitutionGroup(_ImportedBinding_citygml20__core.CityObject)

TINRelief._setSubstitutionGroup(ReliefComponent)

RasterRelief._setSubstitutionGroup(ReliefComponent)

MassPointRelief._setSubstitutionGroup(ReliefComponent)

BreaklineRelief._setSubstitutionGroup(ReliefComponent)

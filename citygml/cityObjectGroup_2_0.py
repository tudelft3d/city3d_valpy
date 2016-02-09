# ./citygml/cityObjectGroup_2_0.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:43d20bd7d48ea2d384bf6d13d28b5a403d4223b2
# Generated 2016-02-09 15:38:06.039495 by PyXB version 1.2.4 using Python 2.7.10.final.0
# Namespace http://www.opengis.net/citygml/cityobjectgroup/2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b8daeacc-cf3a-11e5-ad3c-a0999b07c86f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import citygml.cgmlbase_2_0 as _ImportedBinding_citygml_cgmlbase_2_0
import citygml._xlink as _ImportedBinding_citygml__xlink
import pyxb.binding.datatypes
import citygml._gml as _ImportedBinding_citygml__gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/cityobjectgroup/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_core = _ImportedBinding_citygml_cgmlbase_2_0.Namespace
_Namespace_core.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = _ImportedBinding_citygml__gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding_citygml__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.opengis.net/citygml/cityobjectgroup/2.0}CityObjectGroupMemberType with content type ELEMENT_ONLY
class CityObjectGroupMemberType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a CityObjectGroup to its members, which are _CityObjects. The
				CityObjectGroupMemberType element must either carry a reference to a _CityObject object or contain a _CityObject object
				inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CityObjectGroupMemberType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/2.0}_CityObject uses Python identifier CityObject
    __CityObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject'), 'CityObject', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_opengis_netcitygml2_0_CityObject', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 71, 1), )

    
    CityObject = property(__CityObject.value, __CityObject.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_role', pyxb.binding.datatypes.string)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 64, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 64, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role_
    __role_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role_', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml__xlink.roleType)
    __role_._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 48, 1)
    __role_._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 114, 2)
    
    role_ = property(__role_.value, __role_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupMemberType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __CityObject.name() : __CityObject
    })
    _AttributeMap.update({
        __role.name() : __role,
        __remoteSchema.name() : __remoteSchema,
        __type.name() : __type,
        __href.name() : __href,
        __role_.name() : __role_,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
Namespace.addCategoryObject('typeBinding', 'CityObjectGroupMemberType', CityObjectGroupMemberType)


# Complex type {http://www.opengis.net/citygml/cityobjectgroup/2.0}CityObjectGroupParentType with content type ELEMENT_ONLY
class CityObjectGroupParentType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a CityObjectGroup to its parent, which is a CityObject. The
				CityObjectGroupParentType element must either carry a reference to a _CityObject object or contain a _CityObject object
				inline, but neither both nor none. The parent association allows for modelling of a generic hierarchical grouping concept.
				Named aggregations of components (CityObjects) can be added to specific CityObjects considered as the parent object. The
				parent association links to the aggregate, while the parts are given by the group members. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CityObjectGroupParentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 70, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/2.0}_CityObject uses Python identifier CityObject
    __CityObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject'), 'CityObject', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_opengis_netcitygml2_0_CityObject', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 71, 1), )

    
    CityObject = property(__CityObject.value, __CityObject.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinktype', _ImportedBinding_citygml__xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinkhref', _ImportedBinding_citygml__xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'role'), 'role', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinkrole', _ImportedBinding_citygml__xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinkarcrole', _ImportedBinding_citygml__xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'title'), 'title', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinktitle', _ImportedBinding_citygml__xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'show'), 'show', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinkshow', _ImportedBinding_citygml__xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'actuate'), 'actuate', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupParentType_httpwww_w3_org1999xlinkactuate', _ImportedBinding_citygml__xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/xlink/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __CityObject.name() : __CityObject
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
Namespace.addCategoryObject('typeBinding', 'CityObjectGroupParentType', CityObjectGroupParentType)


# Complex type {http://www.opengis.net/citygml/cityobjectgroup/2.0}CityObjectGroupType with content type ELEMENT_ONLY
class CityObjectGroupType (_ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType):
    """ A group may be used to aggregate arbitrary CityObjects according to some user-defined criteria. Examples
				for groups are the buildings in a specific region, the result of a query, or objects put together for visualization
				purposes. Each group has a name (inherited from AbstractGMLType), functions (e.g., building group), a class and zero or
				more usages. A geometry may optionally be attached to a group, if the geometry of the whole group differs from the
				geometry of the parts. Each member of a group may be qualified by a role name, reflecting the role each CityObject plays
				in the context of the group. As subclass of _CityObject, a CityObjectGroup inherits all attributes and relations, in
				particular an id, names, external references, and generalization relations. As CityObjectGroup itself is a CityObject, it
				may also be contained by another group. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CityObjectGroupType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 23, 1)
    _ElementMap = _ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/2.0}creationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/2.0}terminationDate) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/2.0}externalReference) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/2.0}generalizesTo) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToTerrain ({http://www.opengis.net/citygml/2.0}relativeToTerrain) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element relativeToWater ({http://www.opengis.net/citygml/2.0}relativeToWater) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/2.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/2.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0class', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 37, 5), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0function', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 38, 5), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0usage', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 39, 5), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}groupMember uses Python identifier groupMember
    __groupMember = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'groupMember'), 'groupMember', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0groupMember', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 40, 5), )

    
    groupMember = property(__groupMember.value, __groupMember.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parent'), 'parent', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0parent', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 41, 5), )

    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometry'), 'geometry', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0geometry', False, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 42, 5), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/cityobjectgroup/2.0}_GenericApplicationPropertyOfCityObjectGroup uses Python identifier GenericApplicationPropertyOfCityObjectGroup
    __GenericApplicationPropertyOfCityObjectGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObjectGroup'), 'GenericApplicationPropertyOfCityObjectGroup', '__httpwww_opengis_netcitygmlcityobjectgroup2_0_CityObjectGroupType_httpwww_opengis_netcitygmlcityobjectgroup2_0_GenericApplicationPropertyOfCityObjectGroup', True, pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 51, 1), )

    
    GenericApplicationPropertyOfCityObjectGroup = property(__GenericApplicationPropertyOfCityObjectGroup.value, __GenericApplicationPropertyOfCityObjectGroup.set, None, None)

    
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
        __groupMember.name() : __groupMember,
        __parent.name() : __parent,
        __geometry.name() : __geometry,
        __GenericApplicationPropertyOfCityObjectGroup.name() : __GenericApplicationPropertyOfCityObjectGroup
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CityObjectGroupType', CityObjectGroupType)


GenericApplicationPropertyOfCityObjectGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObjectGroup'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfCityObjectGroup.name().localName(), GenericApplicationPropertyOfCityObjectGroup)

CityObjectGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CityObjectGroup'), CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 49, 1))
Namespace.addCategoryObject('elementBinding', CityObjectGroup.name().localName(), CityObjectGroup)



CityObjectGroupMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject'), _ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType, abstract=pyxb.binding.datatypes.boolean(1), scope=CityObjectGroupMemberType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 71, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 61, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupMemberType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 62, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CityObjectGroupMemberType._Automaton = _BuildAutomaton()




CityObjectGroupParentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject'), _ImportedBinding_citygml_cgmlbase_2_0.AbstractCityObjectType, abstract=pyxb.binding.datatypes.boolean(1), scope=CityObjectGroupParentType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 71, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 78, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupParentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_CityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 79, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CityObjectGroupParentType._Automaton = _BuildAutomaton_()




CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), _ImportedBinding_citygml__gml.CodeType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 37, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), _ImportedBinding_citygml__gml.CodeType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 38, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), _ImportedBinding_citygml__gml.CodeType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 39, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'groupMember'), CityObjectGroupMemberType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 40, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parent'), CityObjectGroupParentType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 41, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), _ImportedBinding_citygml__gml.GeometryPropertyType, scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 42, 5)))

CityObjectGroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObjectGroup'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CityObjectGroupType, location=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 51, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/feature.xsd', 29, 5))
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
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 37, 5))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 38, 5))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 39, 5))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 40, 5))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 41, 5))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 42, 5))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 43, 5))
    counters.add(cc_18)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML1_0/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 59, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 60, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 61, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 62, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToTerrain')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 63, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'relativeToWater')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 64, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityGMLBase.xsd', 65, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 37, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 38, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 39, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'groupMember')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 40, 5))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parent')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 41, 5))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometry')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 42, 5))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CityObjectGroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObjectGroup')), pyxb.utils.utility.Location('/Users/octeufer/Work/workspace/virenvwspace/virtual_valcity3d/val3dpy/CGML2_0/CityGML/cityObjectGroup.xsd', 43, 5))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
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
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CityObjectGroupType._Automaton = _BuildAutomaton_2()


CityObjectGroup._setSubstitutionGroup(_ImportedBinding_citygml_cgmlbase_2_0.CityObject)

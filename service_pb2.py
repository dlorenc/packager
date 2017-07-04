# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rservice.proto\"<\n\tNpmConfig\x12\x14\n\x0cpackage_json\x18\x01 \x01(\x0c\x12\x19\n\x11package_lock_json\x18\x02 \x01(\x0c\"%\n\tPipConfig\x12\x18\n\x10requirements_txt\x18\x01 \x01(\x0c\"\x9d\x01\n\x15\x42uildContainerRequest\x12\x12\n\nbase_image\x18\x01 \x01(\t\x12\x19\n\x11\x64\x65stination_image\x18\x02 \x01(\t\x12 \n\nnpm_config\x18\x03 \x01(\x0b\x32\n.NpmConfigH\x00\x12 \n\npip_config\x18\x04 \x01(\x0b\x32\n.PipConfigH\x00\x42\x11\n\x0fpackage_manager\"2\n\x16\x42uildContainerResponse\x12\x18\n\x10\x63ontainer_digest\x18\x01 \x01(\t*\"\n\x0ePackageManager\x12\x07\n\x03NPM\x10\x00\x12\x07\n\x03PIP\x10\x01\x32O\n\nAppBuilder\x12\x41\n\x0e\x42uildContainer\x12\x16.BuildContainerRequest\x1a\x17.BuildContainerResponseb\x06proto3')
)

_PACKAGEMANAGER = _descriptor.EnumDescriptor(
  name='PackageManager',
  full_name='PackageManager',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NPM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=330,
  serialized_end=364,
)
_sym_db.RegisterEnumDescriptor(_PACKAGEMANAGER)

PackageManager = enum_type_wrapper.EnumTypeWrapper(_PACKAGEMANAGER)
NPM = 0
PIP = 1



_NPMCONFIG = _descriptor.Descriptor(
  name='NpmConfig',
  full_name='NpmConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_json', full_name='NpmConfig.package_json', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='package_lock_json', full_name='NpmConfig.package_lock_json', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=77,
)


_PIPCONFIG = _descriptor.Descriptor(
  name='PipConfig',
  full_name='PipConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requirements_txt', full_name='PipConfig.requirements_txt', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=116,
)


_BUILDCONTAINERREQUEST = _descriptor.Descriptor(
  name='BuildContainerRequest',
  full_name='BuildContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_image', full_name='BuildContainerRequest.base_image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination_image', full_name='BuildContainerRequest.destination_image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='npm_config', full_name='BuildContainerRequest.npm_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pip_config', full_name='BuildContainerRequest.pip_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='package_manager', full_name='BuildContainerRequest.package_manager',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=119,
  serialized_end=276,
)


_BUILDCONTAINERRESPONSE = _descriptor.Descriptor(
  name='BuildContainerResponse',
  full_name='BuildContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_digest', full_name='BuildContainerResponse.container_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=328,
)

_BUILDCONTAINERREQUEST.fields_by_name['npm_config'].message_type = _NPMCONFIG
_BUILDCONTAINERREQUEST.fields_by_name['pip_config'].message_type = _PIPCONFIG
_BUILDCONTAINERREQUEST.oneofs_by_name['package_manager'].fields.append(
  _BUILDCONTAINERREQUEST.fields_by_name['npm_config'])
_BUILDCONTAINERREQUEST.fields_by_name['npm_config'].containing_oneof = _BUILDCONTAINERREQUEST.oneofs_by_name['package_manager']
_BUILDCONTAINERREQUEST.oneofs_by_name['package_manager'].fields.append(
  _BUILDCONTAINERREQUEST.fields_by_name['pip_config'])
_BUILDCONTAINERREQUEST.fields_by_name['pip_config'].containing_oneof = _BUILDCONTAINERREQUEST.oneofs_by_name['package_manager']
DESCRIPTOR.message_types_by_name['NpmConfig'] = _NPMCONFIG
DESCRIPTOR.message_types_by_name['PipConfig'] = _PIPCONFIG
DESCRIPTOR.message_types_by_name['BuildContainerRequest'] = _BUILDCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['BuildContainerResponse'] = _BUILDCONTAINERRESPONSE
DESCRIPTOR.enum_types_by_name['PackageManager'] = _PACKAGEMANAGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NpmConfig = _reflection.GeneratedProtocolMessageType('NpmConfig', (_message.Message,), dict(
  DESCRIPTOR = _NPMCONFIG,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:NpmConfig)
  ))
_sym_db.RegisterMessage(NpmConfig)

PipConfig = _reflection.GeneratedProtocolMessageType('PipConfig', (_message.Message,), dict(
  DESCRIPTOR = _PIPCONFIG,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:PipConfig)
  ))
_sym_db.RegisterMessage(PipConfig)

BuildContainerRequest = _reflection.GeneratedProtocolMessageType('BuildContainerRequest', (_message.Message,), dict(
  DESCRIPTOR = _BUILDCONTAINERREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:BuildContainerRequest)
  ))
_sym_db.RegisterMessage(BuildContainerRequest)

BuildContainerResponse = _reflection.GeneratedProtocolMessageType('BuildContainerResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUILDCONTAINERRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:BuildContainerResponse)
  ))
_sym_db.RegisterMessage(BuildContainerResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class AppBuilderStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.BuildContainer = channel.unary_unary(
          '/AppBuilder/BuildContainer',
          request_serializer=BuildContainerRequest.SerializeToString,
          response_deserializer=BuildContainerResponse.FromString,
          )


  class AppBuilderServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def BuildContainer(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AppBuilderServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'BuildContainer': grpc.unary_unary_rpc_method_handler(
            servicer.BuildContainer,
            request_deserializer=BuildContainerRequest.FromString,
            response_serializer=BuildContainerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'AppBuilder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAppBuilderServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def BuildContainer(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAppBuilderStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def BuildContainer(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    BuildContainer.future = None


  def beta_create_AppBuilder_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('AppBuilder', 'BuildContainer'): BuildContainerRequest.FromString,
    }
    response_serializers = {
      ('AppBuilder', 'BuildContainer'): BuildContainerResponse.SerializeToString,
    }
    method_implementations = {
      ('AppBuilder', 'BuildContainer'): face_utilities.unary_unary_inline(servicer.BuildContainer),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AppBuilder_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('AppBuilder', 'BuildContainer'): BuildContainerRequest.SerializeToString,
    }
    response_deserializers = {
      ('AppBuilder', 'BuildContainer'): BuildContainerResponse.FromString,
    }
    cardinalities = {
      'BuildContainer': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'AppBuilder', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
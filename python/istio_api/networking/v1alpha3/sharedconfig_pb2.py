# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking/v1alpha3/sharedconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='networking/v1alpha3/sharedconfig.proto',
  package='istio.networking.v1alpha3',
  syntax='proto3',
  serialized_options=_b('Z istio.io/api/networking/v1alpha3'),
  serialized_pb=_b('\n&networking/v1alpha3/sharedconfig.proto\x12\x19istio.networking.v1alpha3\"V\n\x0cSharedConfig\x12\x46\n\x12rate_limit_configs\x18\x01 \x03(\x0b\x32*.istio.networking.v1alpha3.RateLimitConfig\"f\n\x0fRateLimitConfig\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12\x43\n\x0b\x64\x65scriptors\x18\x02 \x03(\x0b\x32..istio.networking.v1alpha3.RateLimitDescriptor\"\x87\x03\n\x13RateLimitDescriptor\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12L\n\nrate_limit\x18\x03 \x01(\x0b\x32\x38.istio.networking.v1alpha3.RateLimitDescriptor.RateLimit\x12\x43\n\x0b\x64\x65scriptors\x18\x04 \x03(\x0b\x32..istio.networking.v1alpha3.RateLimitDescriptor\x12\x0b\n\x03\x61pi\x18\x05 \x01(\t\x1a\xb3\x01\n\tRateLimit\x12\x19\n\x11requests_per_unit\x18\x01 \x01(\r\x12K\n\x04unit\x18\x02 \x01(\x0e\x32=.istio.networking.v1alpha3.RateLimitDescriptor.RateLimit.Unit\">\n\x04Unit\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SECOND\x10\x01\x12\n\n\x06MINUTE\x10\x02\x12\x08\n\x04HOUR\x10\x03\x12\x07\n\x03\x44\x41Y\x10\x04\x42\"Z istio.io/api/networking/v1alpha3b\x06proto3')
)



_RATELIMITDESCRIPTOR_RATELIMIT_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='istio.networking.v1alpha3.RateLimitDescriptor.RateLimit.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECOND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINUTE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOUR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=591,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_RATELIMITDESCRIPTOR_RATELIMIT_UNIT)


_SHAREDCONFIG = _descriptor.Descriptor(
  name='SharedConfig',
  full_name='istio.networking.v1alpha3.SharedConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate_limit_configs', full_name='istio.networking.v1alpha3.SharedConfig.rate_limit_configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=155,
)


_RATELIMITCONFIG = _descriptor.Descriptor(
  name='RateLimitConfig',
  full_name='istio.networking.v1alpha3.RateLimitConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='istio.networking.v1alpha3.RateLimitConfig.domain', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptors', full_name='istio.networking.v1alpha3.RateLimitConfig.descriptors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=259,
)


_RATELIMITDESCRIPTOR_RATELIMIT = _descriptor.Descriptor(
  name='RateLimit',
  full_name='istio.networking.v1alpha3.RateLimitDescriptor.RateLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests_per_unit', full_name='istio.networking.v1alpha3.RateLimitDescriptor.RateLimit.requests_per_unit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='istio.networking.v1alpha3.RateLimitDescriptor.RateLimit.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RATELIMITDESCRIPTOR_RATELIMIT_UNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=653,
)

_RATELIMITDESCRIPTOR = _descriptor.Descriptor(
  name='RateLimitDescriptor',
  full_name='istio.networking.v1alpha3.RateLimitDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.networking.v1alpha3.RateLimitDescriptor.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.networking.v1alpha3.RateLimitDescriptor.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='istio.networking.v1alpha3.RateLimitDescriptor.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptors', full_name='istio.networking.v1alpha3.RateLimitDescriptor.descriptors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api', full_name='istio.networking.v1alpha3.RateLimitDescriptor.api', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RATELIMITDESCRIPTOR_RATELIMIT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=653,
)

_SHAREDCONFIG.fields_by_name['rate_limit_configs'].message_type = _RATELIMITCONFIG
_RATELIMITCONFIG.fields_by_name['descriptors'].message_type = _RATELIMITDESCRIPTOR
_RATELIMITDESCRIPTOR_RATELIMIT.fields_by_name['unit'].enum_type = _RATELIMITDESCRIPTOR_RATELIMIT_UNIT
_RATELIMITDESCRIPTOR_RATELIMIT.containing_type = _RATELIMITDESCRIPTOR
_RATELIMITDESCRIPTOR_RATELIMIT_UNIT.containing_type = _RATELIMITDESCRIPTOR_RATELIMIT
_RATELIMITDESCRIPTOR.fields_by_name['rate_limit'].message_type = _RATELIMITDESCRIPTOR_RATELIMIT
_RATELIMITDESCRIPTOR.fields_by_name['descriptors'].message_type = _RATELIMITDESCRIPTOR
DESCRIPTOR.message_types_by_name['SharedConfig'] = _SHAREDCONFIG
DESCRIPTOR.message_types_by_name['RateLimitConfig'] = _RATELIMITCONFIG
DESCRIPTOR.message_types_by_name['RateLimitDescriptor'] = _RATELIMITDESCRIPTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedConfig = _reflection.GeneratedProtocolMessageType('SharedConfig', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDCONFIG,
  __module__ = 'networking.v1alpha3.sharedconfig_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.SharedConfig)
  ))
_sym_db.RegisterMessage(SharedConfig)

RateLimitConfig = _reflection.GeneratedProtocolMessageType('RateLimitConfig', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITCONFIG,
  __module__ = 'networking.v1alpha3.sharedconfig_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.RateLimitConfig)
  ))
_sym_db.RegisterMessage(RateLimitConfig)

RateLimitDescriptor = _reflection.GeneratedProtocolMessageType('RateLimitDescriptor', (_message.Message,), dict(

  RateLimit = _reflection.GeneratedProtocolMessageType('RateLimit', (_message.Message,), dict(
    DESCRIPTOR = _RATELIMITDESCRIPTOR_RATELIMIT,
    __module__ = 'networking.v1alpha3.sharedconfig_pb2'
    # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.RateLimitDescriptor.RateLimit)
    ))
  ,
  DESCRIPTOR = _RATELIMITDESCRIPTOR,
  __module__ = 'networking.v1alpha3.sharedconfig_pb2'
  # @@protoc_insertion_point(class_scope:istio.networking.v1alpha3.RateLimitDescriptor)
  ))
_sym_db.RegisterMessage(RateLimitDescriptor)
_sym_db.RegisterMessage(RateLimitDescriptor.RateLimit)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

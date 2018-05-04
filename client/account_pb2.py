# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='account',
  serialized_pb=_b('\n\raccount.proto\x12\x07\x61\x63\x63ount\"1\n\nREQ_VERIFY\x12\x0e\n\x03uid\x18\x01 \x01(\x07:\x01\x30\x12\x13\n\tkey_token\x18\x02 \x01(\t:\x00\"W\n\nRSP_VERIFY\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03uid\x18\x02 \x01(\x07:\x01\x30\x12\x13\n\tkey_token\x18\x04 \x01(\t:\x00\x12\x11\n\x07\x63hannel\x18\x05 \x01(\t:\x00\",\n\x14REQ_REGISTER_TOURIST\x12\x14\n\nseed_token\x18\x01 \x01(\t:\x00\"N\n\x14RSP_REGISTER_TOURIST\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\tkey_token\x18\x02 \x01(\t:\x00\x12\x0e\n\x03uid\x18\x03 \x01(\x07:\x01\x30\"I\n\x12REQ_REGISTER_PHONE\x12\x16\n\x0cphone_number\x18\x01 \x01(\t:\x00\x12\x1b\n\x11tourist_key_token\x18\x02 \x01(\t:\x00\"\'\n\x12RSP_REGISTER_PHONE\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\"B\n\x18REQ_VERIFY_REGISTER_CODE\x12\x16\n\x0cphone_number\x18\x01 \x01(\t:\x00\x12\x0e\n\x04\x63ode\x18\x02 \x01(\t:\x00\"o\n\x18RSP_VERIFY_REGISTER_CODE\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\tkey_token\x18\x02 \x01(\t:\x00\x12\x0e\n\x03uid\x18\x03 \x01(\x07:\x01\x30\x12\x1b\n\x11tourist_key_token\x18\x04 \x01(\t:\x00\",\n\x12REQ_GET_LOGIN_CODE\x12\x16\n\x0cphone_number\x18\x01 \x01(\t:\x00\"\'\n\x12RSP_GET_LOGIN_CODE\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\"?\n\x15REQ_VERIFY_LOGIN_CODE\x12\x16\n\x0cphone_number\x18\x01 \x01(\t:\x00\x12\x0e\n\x04\x63ode\x18\x02 \x01(\t:\x00\"O\n\x15RSP_VERIFY_LOGIN_CODE\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\tkey_token\x18\x02 \x01(\t:\x00\x12\x0e\n\x03uid\x18\x03 \x01(\x07:\x01\x30\"N\n\x0eREQ_MAKE_ORDER\x12\x15\n\nproduct_id\x18\x01 \x01(\x05:\x01\x30\x12\x15\n\nchannel_id\x18\x02 \x01(\x05:\x01\x30\x12\x0e\n\x03uid\x18\x03 \x01(\x07:\x01\x30\"7\n\x0eRSP_MAKE_ORDER\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x12\n\x08order_id\x18\x02 \x01(\t:\x00\":\n\x11REQ_CHECK_PAYMENT\x12\x11\n\x07receipt\x18\x01 \x01(\t:\x00\x12\x12\n\x08order_id\x18\x02 \x01(\t:\x00\"&\n\x11RSP_CHECK_PAYMENT\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\"I\n\x14REQ_VERIFY_3RD_LOGIN\x12\x0e\n\x03uid\x18\x01 \x01(\x07:\x01\x30\x12\x0e\n\x04\x63ode\x18\x02 \x01(\t:\x00\x12\x11\n\x07\x63hannel\x18\x03 \x01(\t:\x00\"a\n\x14RSP_VERIFY_3RD_LOGIN\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\tkey_token\x18\x02 \x01(\t:\x00\x12\x0e\n\x03uid\x18\x03 \x01(\x07:\x01\x30\x12\x11\n\x07\x63hannel\x18\x04 \x01(\t:\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQ_VERIFY = _descriptor.Descriptor(
  name='REQ_VERIFY',
  full_name='account.REQ_VERIFY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.REQ_VERIFY.uid', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.REQ_VERIFY.key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=75,
)


_RSP_VERIFY = _descriptor.Descriptor(
  name='RSP_VERIFY',
  full_name='account.RSP_VERIFY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_VERIFY.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.RSP_VERIFY.uid', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.RSP_VERIFY.key_token', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='account.RSP_VERIFY.channel', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=164,
)


_REQ_REGISTER_TOURIST = _descriptor.Descriptor(
  name='REQ_REGISTER_TOURIST',
  full_name='account.REQ_REGISTER_TOURIST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed_token', full_name='account.REQ_REGISTER_TOURIST.seed_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=210,
)


_RSP_REGISTER_TOURIST = _descriptor.Descriptor(
  name='RSP_REGISTER_TOURIST',
  full_name='account.RSP_REGISTER_TOURIST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_REGISTER_TOURIST.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.RSP_REGISTER_TOURIST.key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.RSP_REGISTER_TOURIST.uid', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=290,
)


_REQ_REGISTER_PHONE = _descriptor.Descriptor(
  name='REQ_REGISTER_PHONE',
  full_name='account.REQ_REGISTER_PHONE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='account.REQ_REGISTER_PHONE.phone_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tourist_key_token', full_name='account.REQ_REGISTER_PHONE.tourist_key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=365,
)


_RSP_REGISTER_PHONE = _descriptor.Descriptor(
  name='RSP_REGISTER_PHONE',
  full_name='account.RSP_REGISTER_PHONE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_REGISTER_PHONE.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=406,
)


_REQ_VERIFY_REGISTER_CODE = _descriptor.Descriptor(
  name='REQ_VERIFY_REGISTER_CODE',
  full_name='account.REQ_VERIFY_REGISTER_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='account.REQ_VERIFY_REGISTER_CODE.phone_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='account.REQ_VERIFY_REGISTER_CODE.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=474,
)


_RSP_VERIFY_REGISTER_CODE = _descriptor.Descriptor(
  name='RSP_VERIFY_REGISTER_CODE',
  full_name='account.RSP_VERIFY_REGISTER_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_VERIFY_REGISTER_CODE.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.RSP_VERIFY_REGISTER_CODE.key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.RSP_VERIFY_REGISTER_CODE.uid', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tourist_key_token', full_name='account.RSP_VERIFY_REGISTER_CODE.tourist_key_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=587,
)


_REQ_GET_LOGIN_CODE = _descriptor.Descriptor(
  name='REQ_GET_LOGIN_CODE',
  full_name='account.REQ_GET_LOGIN_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='account.REQ_GET_LOGIN_CODE.phone_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=633,
)


_RSP_GET_LOGIN_CODE = _descriptor.Descriptor(
  name='RSP_GET_LOGIN_CODE',
  full_name='account.RSP_GET_LOGIN_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_GET_LOGIN_CODE.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=674,
)


_REQ_VERIFY_LOGIN_CODE = _descriptor.Descriptor(
  name='REQ_VERIFY_LOGIN_CODE',
  full_name='account.REQ_VERIFY_LOGIN_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='account.REQ_VERIFY_LOGIN_CODE.phone_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='account.REQ_VERIFY_LOGIN_CODE.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=676,
  serialized_end=739,
)


_RSP_VERIFY_LOGIN_CODE = _descriptor.Descriptor(
  name='RSP_VERIFY_LOGIN_CODE',
  full_name='account.RSP_VERIFY_LOGIN_CODE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_VERIFY_LOGIN_CODE.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.RSP_VERIFY_LOGIN_CODE.key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.RSP_VERIFY_LOGIN_CODE.uid', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=820,
)


_REQ_MAKE_ORDER = _descriptor.Descriptor(
  name='REQ_MAKE_ORDER',
  full_name='account.REQ_MAKE_ORDER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='account.REQ_MAKE_ORDER.product_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='account.REQ_MAKE_ORDER.channel_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.REQ_MAKE_ORDER.uid', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=822,
  serialized_end=900,
)


_RSP_MAKE_ORDER = _descriptor.Descriptor(
  name='RSP_MAKE_ORDER',
  full_name='account.RSP_MAKE_ORDER',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_MAKE_ORDER.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='account.RSP_MAKE_ORDER.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=957,
)


_REQ_CHECK_PAYMENT = _descriptor.Descriptor(
  name='REQ_CHECK_PAYMENT',
  full_name='account.REQ_CHECK_PAYMENT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='receipt', full_name='account.REQ_CHECK_PAYMENT.receipt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='account.REQ_CHECK_PAYMENT.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=959,
  serialized_end=1017,
)


_RSP_CHECK_PAYMENT = _descriptor.Descriptor(
  name='RSP_CHECK_PAYMENT',
  full_name='account.RSP_CHECK_PAYMENT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_CHECK_PAYMENT.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1019,
  serialized_end=1057,
)


_REQ_VERIFY_3RD_LOGIN = _descriptor.Descriptor(
  name='REQ_VERIFY_3RD_LOGIN',
  full_name='account.REQ_VERIFY_3RD_LOGIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.REQ_VERIFY_3RD_LOGIN.uid', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='account.REQ_VERIFY_3RD_LOGIN.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='account.REQ_VERIFY_3RD_LOGIN.channel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1132,
)


_RSP_VERIFY_3RD_LOGIN = _descriptor.Descriptor(
  name='RSP_VERIFY_3RD_LOGIN',
  full_name='account.RSP_VERIFY_3RD_LOGIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='account.RSP_VERIFY_3RD_LOGIN.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_token', full_name='account.RSP_VERIFY_3RD_LOGIN.key_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='account.RSP_VERIFY_3RD_LOGIN.uid', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='account.RSP_VERIFY_3RD_LOGIN.channel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1134,
  serialized_end=1231,
)

DESCRIPTOR.message_types_by_name['REQ_VERIFY'] = _REQ_VERIFY
DESCRIPTOR.message_types_by_name['RSP_VERIFY'] = _RSP_VERIFY
DESCRIPTOR.message_types_by_name['REQ_REGISTER_TOURIST'] = _REQ_REGISTER_TOURIST
DESCRIPTOR.message_types_by_name['RSP_REGISTER_TOURIST'] = _RSP_REGISTER_TOURIST
DESCRIPTOR.message_types_by_name['REQ_REGISTER_PHONE'] = _REQ_REGISTER_PHONE
DESCRIPTOR.message_types_by_name['RSP_REGISTER_PHONE'] = _RSP_REGISTER_PHONE
DESCRIPTOR.message_types_by_name['REQ_VERIFY_REGISTER_CODE'] = _REQ_VERIFY_REGISTER_CODE
DESCRIPTOR.message_types_by_name['RSP_VERIFY_REGISTER_CODE'] = _RSP_VERIFY_REGISTER_CODE
DESCRIPTOR.message_types_by_name['REQ_GET_LOGIN_CODE'] = _REQ_GET_LOGIN_CODE
DESCRIPTOR.message_types_by_name['RSP_GET_LOGIN_CODE'] = _RSP_GET_LOGIN_CODE
DESCRIPTOR.message_types_by_name['REQ_VERIFY_LOGIN_CODE'] = _REQ_VERIFY_LOGIN_CODE
DESCRIPTOR.message_types_by_name['RSP_VERIFY_LOGIN_CODE'] = _RSP_VERIFY_LOGIN_CODE
DESCRIPTOR.message_types_by_name['REQ_MAKE_ORDER'] = _REQ_MAKE_ORDER
DESCRIPTOR.message_types_by_name['RSP_MAKE_ORDER'] = _RSP_MAKE_ORDER
DESCRIPTOR.message_types_by_name['REQ_CHECK_PAYMENT'] = _REQ_CHECK_PAYMENT
DESCRIPTOR.message_types_by_name['RSP_CHECK_PAYMENT'] = _RSP_CHECK_PAYMENT
DESCRIPTOR.message_types_by_name['REQ_VERIFY_3RD_LOGIN'] = _REQ_VERIFY_3RD_LOGIN
DESCRIPTOR.message_types_by_name['RSP_VERIFY_3RD_LOGIN'] = _RSP_VERIFY_3RD_LOGIN

REQ_VERIFY = _reflection.GeneratedProtocolMessageType('REQ_VERIFY', (_message.Message,), dict(
  DESCRIPTOR = _REQ_VERIFY,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_VERIFY)
  ))
_sym_db.RegisterMessage(REQ_VERIFY)

RSP_VERIFY = _reflection.GeneratedProtocolMessageType('RSP_VERIFY', (_message.Message,), dict(
  DESCRIPTOR = _RSP_VERIFY,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_VERIFY)
  ))
_sym_db.RegisterMessage(RSP_VERIFY)

REQ_REGISTER_TOURIST = _reflection.GeneratedProtocolMessageType('REQ_REGISTER_TOURIST', (_message.Message,), dict(
  DESCRIPTOR = _REQ_REGISTER_TOURIST,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_REGISTER_TOURIST)
  ))
_sym_db.RegisterMessage(REQ_REGISTER_TOURIST)

RSP_REGISTER_TOURIST = _reflection.GeneratedProtocolMessageType('RSP_REGISTER_TOURIST', (_message.Message,), dict(
  DESCRIPTOR = _RSP_REGISTER_TOURIST,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_REGISTER_TOURIST)
  ))
_sym_db.RegisterMessage(RSP_REGISTER_TOURIST)

REQ_REGISTER_PHONE = _reflection.GeneratedProtocolMessageType('REQ_REGISTER_PHONE', (_message.Message,), dict(
  DESCRIPTOR = _REQ_REGISTER_PHONE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_REGISTER_PHONE)
  ))
_sym_db.RegisterMessage(REQ_REGISTER_PHONE)

RSP_REGISTER_PHONE = _reflection.GeneratedProtocolMessageType('RSP_REGISTER_PHONE', (_message.Message,), dict(
  DESCRIPTOR = _RSP_REGISTER_PHONE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_REGISTER_PHONE)
  ))
_sym_db.RegisterMessage(RSP_REGISTER_PHONE)

REQ_VERIFY_REGISTER_CODE = _reflection.GeneratedProtocolMessageType('REQ_VERIFY_REGISTER_CODE', (_message.Message,), dict(
  DESCRIPTOR = _REQ_VERIFY_REGISTER_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_VERIFY_REGISTER_CODE)
  ))
_sym_db.RegisterMessage(REQ_VERIFY_REGISTER_CODE)

RSP_VERIFY_REGISTER_CODE = _reflection.GeneratedProtocolMessageType('RSP_VERIFY_REGISTER_CODE', (_message.Message,), dict(
  DESCRIPTOR = _RSP_VERIFY_REGISTER_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_VERIFY_REGISTER_CODE)
  ))
_sym_db.RegisterMessage(RSP_VERIFY_REGISTER_CODE)

REQ_GET_LOGIN_CODE = _reflection.GeneratedProtocolMessageType('REQ_GET_LOGIN_CODE', (_message.Message,), dict(
  DESCRIPTOR = _REQ_GET_LOGIN_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_GET_LOGIN_CODE)
  ))
_sym_db.RegisterMessage(REQ_GET_LOGIN_CODE)

RSP_GET_LOGIN_CODE = _reflection.GeneratedProtocolMessageType('RSP_GET_LOGIN_CODE', (_message.Message,), dict(
  DESCRIPTOR = _RSP_GET_LOGIN_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_GET_LOGIN_CODE)
  ))
_sym_db.RegisterMessage(RSP_GET_LOGIN_CODE)

REQ_VERIFY_LOGIN_CODE = _reflection.GeneratedProtocolMessageType('REQ_VERIFY_LOGIN_CODE', (_message.Message,), dict(
  DESCRIPTOR = _REQ_VERIFY_LOGIN_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_VERIFY_LOGIN_CODE)
  ))
_sym_db.RegisterMessage(REQ_VERIFY_LOGIN_CODE)

RSP_VERIFY_LOGIN_CODE = _reflection.GeneratedProtocolMessageType('RSP_VERIFY_LOGIN_CODE', (_message.Message,), dict(
  DESCRIPTOR = _RSP_VERIFY_LOGIN_CODE,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_VERIFY_LOGIN_CODE)
  ))
_sym_db.RegisterMessage(RSP_VERIFY_LOGIN_CODE)

REQ_MAKE_ORDER = _reflection.GeneratedProtocolMessageType('REQ_MAKE_ORDER', (_message.Message,), dict(
  DESCRIPTOR = _REQ_MAKE_ORDER,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_MAKE_ORDER)
  ))
_sym_db.RegisterMessage(REQ_MAKE_ORDER)

RSP_MAKE_ORDER = _reflection.GeneratedProtocolMessageType('RSP_MAKE_ORDER', (_message.Message,), dict(
  DESCRIPTOR = _RSP_MAKE_ORDER,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_MAKE_ORDER)
  ))
_sym_db.RegisterMessage(RSP_MAKE_ORDER)

REQ_CHECK_PAYMENT = _reflection.GeneratedProtocolMessageType('REQ_CHECK_PAYMENT', (_message.Message,), dict(
  DESCRIPTOR = _REQ_CHECK_PAYMENT,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_CHECK_PAYMENT)
  ))
_sym_db.RegisterMessage(REQ_CHECK_PAYMENT)

RSP_CHECK_PAYMENT = _reflection.GeneratedProtocolMessageType('RSP_CHECK_PAYMENT', (_message.Message,), dict(
  DESCRIPTOR = _RSP_CHECK_PAYMENT,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_CHECK_PAYMENT)
  ))
_sym_db.RegisterMessage(RSP_CHECK_PAYMENT)

REQ_VERIFY_3RD_LOGIN = _reflection.GeneratedProtocolMessageType('REQ_VERIFY_3RD_LOGIN', (_message.Message,), dict(
  DESCRIPTOR = _REQ_VERIFY_3RD_LOGIN,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.REQ_VERIFY_3RD_LOGIN)
  ))
_sym_db.RegisterMessage(REQ_VERIFY_3RD_LOGIN)

RSP_VERIFY_3RD_LOGIN = _reflection.GeneratedProtocolMessageType('RSP_VERIFY_3RD_LOGIN', (_message.Message,), dict(
  DESCRIPTOR = _RSP_VERIFY_3RD_LOGIN,
  __module__ = 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.RSP_VERIFY_3RD_LOGIN)
  ))
_sym_db.RegisterMessage(RSP_VERIFY_3RD_LOGIN)


# @@protoc_insertion_point(module_scope)

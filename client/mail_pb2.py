# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail.proto

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
  name='mail.proto',
  package='mail',
  serialized_pb=_b('\n\nmail.proto\x12\x04mail\"\x0f\n\rREQ_MAIL_LIST\"-\n\nAttachInfo\x12\r\n\x02id\x18\x01 \x01(\x05:\x01\x30\x12\x10\n\x05\x63ount\x18\x02 \x01(\x05:\x01\x30\"L\n\x0eMailAttachInfo\x12\x13\n\x08mail_seq\x18\x01 \x01(\x05:\x01\x30\x12%\n\x0b\x61ttach_list\x18\x02 \x03(\x0b\x32\x10.mail.AttachInfo\"\x80\x01\n\x08MailInfo\x12\x13\n\x08mail_seq\x18\x01 \x01(\x05:\x01\x30\x12\x0f\n\x05title\x18\x02 \x01(\t:\x00\x12\x11\n\x07\x63ontent\x18\x03 \x01(\t:\x00\x12\x14\n\tsend_time\x18\x04 \x01(\x05:\x01\x30\x12%\n\x0b\x61ttach_list\x18\x05 \x03(\x0b\x32\x10.mail.AttachInfo\"E\n\rRSP_MAIL_LIST\x12!\n\tmail_list\x18\x01 \x03(\x0b\x32\x0e.mail.MailInfo\x12\x11\n\x06result\x18\x02 \x01(\x05:\x01\x30\"#\n\x0cREQ_DEL_MAIL\x12\x13\n\x08mail_seq\x18\x01 \x01(\x05:\x01\x30\"6\n\x0cRSP_DEL_MAIL\x12\x13\n\x08mail_seq\x18\x01 \x01(\x05:\x01\x30\x12\x11\n\x06result\x18\x02 \x01(\x05:\x01\x30\"&\n\x0fREQ_TAKE_ATTACH\x12\x13\n\x08mail_seq\x18\x01 \x01(\x05:\x01\x30\"`\n\x0fRSP_TAKE_ATTACH\x12\x11\n\x06result\x18\x01 \x01(\x05:\x01\x30\x12%\n\x0b\x61ttach_list\x18\x02 \x03(\x0b\x32\x10.mail.AttachInfo\x12\x13\n\x08mail_seq\x18\x03 \x01(\x05:\x01\x30\"\x15\n\x13REQ_ALL_MAIL_ATTACH\"X\n\x13RSP_ALL_MAIL_ATTACH\x12.\n\x10mail_attach_list\x18\x01 \x03(\x0b\x32\x14.mail.MailAttachInfo\x12\x11\n\x06result\x18\x02 \x01(\x05:\x01\x30\" \n\x0cNTF_NEW_MAIL\x12\x10\n\x05\x63ount\x18\x01 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQ_MAIL_LIST = _descriptor.Descriptor(
  name='REQ_MAIL_LIST',
  full_name='mail.REQ_MAIL_LIST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=20,
  serialized_end=35,
)


_ATTACHINFO = _descriptor.Descriptor(
  name='AttachInfo',
  full_name='mail.AttachInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mail.AttachInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='mail.AttachInfo.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=37,
  serialized_end=82,
)


_MAILATTACHINFO = _descriptor.Descriptor(
  name='MailAttachInfo',
  full_name='mail.MailAttachInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.MailAttachInfo.mail_seq', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_list', full_name='mail.MailAttachInfo.attach_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=160,
)


_MAILINFO = _descriptor.Descriptor(
  name='MailInfo',
  full_name='mail.MailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.MailInfo.mail_seq', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='mail.MailInfo.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='mail.MailInfo.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_time', full_name='mail.MailInfo.send_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_list', full_name='mail.MailInfo.attach_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=163,
  serialized_end=291,
)


_RSP_MAIL_LIST = _descriptor.Descriptor(
  name='RSP_MAIL_LIST',
  full_name='mail.RSP_MAIL_LIST',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_list', full_name='mail.RSP_MAIL_LIST.mail_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='mail.RSP_MAIL_LIST.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=293,
  serialized_end=362,
)


_REQ_DEL_MAIL = _descriptor.Descriptor(
  name='REQ_DEL_MAIL',
  full_name='mail.REQ_DEL_MAIL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.REQ_DEL_MAIL.mail_seq', index=0,
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
  serialized_start=364,
  serialized_end=399,
)


_RSP_DEL_MAIL = _descriptor.Descriptor(
  name='RSP_DEL_MAIL',
  full_name='mail.RSP_DEL_MAIL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.RSP_DEL_MAIL.mail_seq', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='mail.RSP_DEL_MAIL.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=401,
  serialized_end=455,
)


_REQ_TAKE_ATTACH = _descriptor.Descriptor(
  name='REQ_TAKE_ATTACH',
  full_name='mail.REQ_TAKE_ATTACH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.REQ_TAKE_ATTACH.mail_seq', index=0,
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
  serialized_start=457,
  serialized_end=495,
)


_RSP_TAKE_ATTACH = _descriptor.Descriptor(
  name='RSP_TAKE_ATTACH',
  full_name='mail.RSP_TAKE_ATTACH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mail.RSP_TAKE_ATTACH.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_list', full_name='mail.RSP_TAKE_ATTACH.attach_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mail_seq', full_name='mail.RSP_TAKE_ATTACH.mail_seq', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=497,
  serialized_end=593,
)


_REQ_ALL_MAIL_ATTACH = _descriptor.Descriptor(
  name='REQ_ALL_MAIL_ATTACH',
  full_name='mail.REQ_ALL_MAIL_ATTACH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=595,
  serialized_end=616,
)


_RSP_ALL_MAIL_ATTACH = _descriptor.Descriptor(
  name='RSP_ALL_MAIL_ATTACH',
  full_name='mail.RSP_ALL_MAIL_ATTACH',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail_attach_list', full_name='mail.RSP_ALL_MAIL_ATTACH.mail_attach_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='mail.RSP_ALL_MAIL_ATTACH.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=618,
  serialized_end=706,
)


_NTF_NEW_MAIL = _descriptor.Descriptor(
  name='NTF_NEW_MAIL',
  full_name='mail.NTF_NEW_MAIL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='mail.NTF_NEW_MAIL.count', index=0,
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
  serialized_start=708,
  serialized_end=740,
)

_MAILATTACHINFO.fields_by_name['attach_list'].message_type = _ATTACHINFO
_MAILINFO.fields_by_name['attach_list'].message_type = _ATTACHINFO
_RSP_MAIL_LIST.fields_by_name['mail_list'].message_type = _MAILINFO
_RSP_TAKE_ATTACH.fields_by_name['attach_list'].message_type = _ATTACHINFO
_RSP_ALL_MAIL_ATTACH.fields_by_name['mail_attach_list'].message_type = _MAILATTACHINFO
DESCRIPTOR.message_types_by_name['REQ_MAIL_LIST'] = _REQ_MAIL_LIST
DESCRIPTOR.message_types_by_name['AttachInfo'] = _ATTACHINFO
DESCRIPTOR.message_types_by_name['MailAttachInfo'] = _MAILATTACHINFO
DESCRIPTOR.message_types_by_name['MailInfo'] = _MAILINFO
DESCRIPTOR.message_types_by_name['RSP_MAIL_LIST'] = _RSP_MAIL_LIST
DESCRIPTOR.message_types_by_name['REQ_DEL_MAIL'] = _REQ_DEL_MAIL
DESCRIPTOR.message_types_by_name['RSP_DEL_MAIL'] = _RSP_DEL_MAIL
DESCRIPTOR.message_types_by_name['REQ_TAKE_ATTACH'] = _REQ_TAKE_ATTACH
DESCRIPTOR.message_types_by_name['RSP_TAKE_ATTACH'] = _RSP_TAKE_ATTACH
DESCRIPTOR.message_types_by_name['REQ_ALL_MAIL_ATTACH'] = _REQ_ALL_MAIL_ATTACH
DESCRIPTOR.message_types_by_name['RSP_ALL_MAIL_ATTACH'] = _RSP_ALL_MAIL_ATTACH
DESCRIPTOR.message_types_by_name['NTF_NEW_MAIL'] = _NTF_NEW_MAIL

REQ_MAIL_LIST = _reflection.GeneratedProtocolMessageType('REQ_MAIL_LIST', (_message.Message,), dict(
  DESCRIPTOR = _REQ_MAIL_LIST,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.REQ_MAIL_LIST)
  ))
_sym_db.RegisterMessage(REQ_MAIL_LIST)

AttachInfo = _reflection.GeneratedProtocolMessageType('AttachInfo', (_message.Message,), dict(
  DESCRIPTOR = _ATTACHINFO,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.AttachInfo)
  ))
_sym_db.RegisterMessage(AttachInfo)

MailAttachInfo = _reflection.GeneratedProtocolMessageType('MailAttachInfo', (_message.Message,), dict(
  DESCRIPTOR = _MAILATTACHINFO,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.MailAttachInfo)
  ))
_sym_db.RegisterMessage(MailAttachInfo)

MailInfo = _reflection.GeneratedProtocolMessageType('MailInfo', (_message.Message,), dict(
  DESCRIPTOR = _MAILINFO,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.MailInfo)
  ))
_sym_db.RegisterMessage(MailInfo)

RSP_MAIL_LIST = _reflection.GeneratedProtocolMessageType('RSP_MAIL_LIST', (_message.Message,), dict(
  DESCRIPTOR = _RSP_MAIL_LIST,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.RSP_MAIL_LIST)
  ))
_sym_db.RegisterMessage(RSP_MAIL_LIST)

REQ_DEL_MAIL = _reflection.GeneratedProtocolMessageType('REQ_DEL_MAIL', (_message.Message,), dict(
  DESCRIPTOR = _REQ_DEL_MAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.REQ_DEL_MAIL)
  ))
_sym_db.RegisterMessage(REQ_DEL_MAIL)

RSP_DEL_MAIL = _reflection.GeneratedProtocolMessageType('RSP_DEL_MAIL', (_message.Message,), dict(
  DESCRIPTOR = _RSP_DEL_MAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.RSP_DEL_MAIL)
  ))
_sym_db.RegisterMessage(RSP_DEL_MAIL)

REQ_TAKE_ATTACH = _reflection.GeneratedProtocolMessageType('REQ_TAKE_ATTACH', (_message.Message,), dict(
  DESCRIPTOR = _REQ_TAKE_ATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.REQ_TAKE_ATTACH)
  ))
_sym_db.RegisterMessage(REQ_TAKE_ATTACH)

RSP_TAKE_ATTACH = _reflection.GeneratedProtocolMessageType('RSP_TAKE_ATTACH', (_message.Message,), dict(
  DESCRIPTOR = _RSP_TAKE_ATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.RSP_TAKE_ATTACH)
  ))
_sym_db.RegisterMessage(RSP_TAKE_ATTACH)

REQ_ALL_MAIL_ATTACH = _reflection.GeneratedProtocolMessageType('REQ_ALL_MAIL_ATTACH', (_message.Message,), dict(
  DESCRIPTOR = _REQ_ALL_MAIL_ATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.REQ_ALL_MAIL_ATTACH)
  ))
_sym_db.RegisterMessage(REQ_ALL_MAIL_ATTACH)

RSP_ALL_MAIL_ATTACH = _reflection.GeneratedProtocolMessageType('RSP_ALL_MAIL_ATTACH', (_message.Message,), dict(
  DESCRIPTOR = _RSP_ALL_MAIL_ATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.RSP_ALL_MAIL_ATTACH)
  ))
_sym_db.RegisterMessage(RSP_ALL_MAIL_ATTACH)

NTF_NEW_MAIL = _reflection.GeneratedProtocolMessageType('NTF_NEW_MAIL', (_message.Message,), dict(
  DESCRIPTOR = _NTF_NEW_MAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:mail.NTF_NEW_MAIL)
  ))
_sym_db.RegisterMessage(NTF_NEW_MAIL)


# @@protoc_insertion_point(module_scope)

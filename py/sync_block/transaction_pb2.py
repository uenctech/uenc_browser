# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11transaction.proto\"%\n\nCTxprevout\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\r\"\'\n\nCScriptSig\x12\x0c\n\x04sign\x18\x01 \x01(\x0c\x12\x0b\n\x03pub\x18\x02 \x01(\x0c\"X\n\x05\x43Txin\x12\x1c\n\x07prevout\x18\x01 \x01(\x0b\x32\x0b.CTxprevout\x12\x1e\n\tscriptSig\x18\x02 \x01(\x0b\x32\x0b.CScriptSig\x12\x11\n\tnSequence\x18\x03 \x01(\r\"-\n\x06\x43Txout\x12\r\n\x05value\x18\x01 \x01(\x03\x12\x14\n\x0cscriptPubKey\x18\x02 \x01(\t\")\n\x0c\x43SignPreHash\x12\x0c\n\x04sign\x18\x01 \x01(\x0c\x12\x0b\n\x03pub\x18\x02 \x01(\x0c\"\xd3\x01\n\x0c\x43Transaction\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0c\n\x04time\x18\x02 \x01(\x04\x12\"\n\x0bsignPreHash\x18\x03 \x03(\x0b\x32\r.CSignPreHash\x12\x0f\n\x07txOwner\x18\x04 \x01(\t\x12\t\n\x01n\x18\x05 \x01(\r\x12\n\n\x02ip\x18\x06 \x01(\t\x12\x0c\n\x04hash\x18\x07 \x01(\t\x12\x13\n\x03vin\x18\x08 \x03(\x0b\x32\x06.CTxin\x12\x15\n\x04vout\x18\t \x03(\x0b\x32\x07.CTxout\x12\r\n\x05\x65xtra\x18\n \x01(\t\x12\x0f\n\x07\x63omment\x18\x0b \x01(\tb\x06proto3'
)




_CTXPREVOUT = _descriptor.Descriptor(
  name='CTxprevout',
  full_name='CTxprevout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='CTxprevout.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='CTxprevout.n', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=21,
  serialized_end=58,
)


_CSCRIPTSIG = _descriptor.Descriptor(
  name='CScriptSig',
  full_name='CScriptSig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sign', full_name='CScriptSig.sign', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub', full_name='CScriptSig.pub', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=60,
  serialized_end=99,
)


_CTXIN = _descriptor.Descriptor(
  name='CTxin',
  full_name='CTxin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevout', full_name='CTxin.prevout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptSig', full_name='CTxin.scriptSig', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nSequence', full_name='CTxin.nSequence', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=101,
  serialized_end=189,
)


_CTXOUT = _descriptor.Descriptor(
  name='CTxout',
  full_name='CTxout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='CTxout.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptPubKey', full_name='CTxout.scriptPubKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=191,
  serialized_end=236,
)


_CSIGNPREHASH = _descriptor.Descriptor(
  name='CSignPreHash',
  full_name='CSignPreHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sign', full_name='CSignPreHash.sign', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub', full_name='CSignPreHash.pub', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=238,
  serialized_end=279,
)


_CTRANSACTION = _descriptor.Descriptor(
  name='CTransaction',
  full_name='CTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CTransaction.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='CTransaction.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signPreHash', full_name='CTransaction.signPreHash', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txOwner', full_name='CTransaction.txOwner', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='CTransaction.n', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='CTransaction.ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='CTransaction.hash', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vin', full_name='CTransaction.vin', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vout', full_name='CTransaction.vout', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra', full_name='CTransaction.extra', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='CTransaction.comment', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=282,
  serialized_end=493,
)

_CTXIN.fields_by_name['prevout'].message_type = _CTXPREVOUT
_CTXIN.fields_by_name['scriptSig'].message_type = _CSCRIPTSIG
_CTRANSACTION.fields_by_name['signPreHash'].message_type = _CSIGNPREHASH
_CTRANSACTION.fields_by_name['vin'].message_type = _CTXIN
_CTRANSACTION.fields_by_name['vout'].message_type = _CTXOUT
DESCRIPTOR.message_types_by_name['CTxprevout'] = _CTXPREVOUT
DESCRIPTOR.message_types_by_name['CScriptSig'] = _CSCRIPTSIG
DESCRIPTOR.message_types_by_name['CTxin'] = _CTXIN
DESCRIPTOR.message_types_by_name['CTxout'] = _CTXOUT
DESCRIPTOR.message_types_by_name['CSignPreHash'] = _CSIGNPREHASH
DESCRIPTOR.message_types_by_name['CTransaction'] = _CTRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CTxprevout = _reflection.GeneratedProtocolMessageType('CTxprevout', (_message.Message,), {
  'DESCRIPTOR' : _CTXPREVOUT,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CTxprevout)
  })
_sym_db.RegisterMessage(CTxprevout)

CScriptSig = _reflection.GeneratedProtocolMessageType('CScriptSig', (_message.Message,), {
  'DESCRIPTOR' : _CSCRIPTSIG,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CScriptSig)
  })
_sym_db.RegisterMessage(CScriptSig)

CTxin = _reflection.GeneratedProtocolMessageType('CTxin', (_message.Message,), {
  'DESCRIPTOR' : _CTXIN,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CTxin)
  })
_sym_db.RegisterMessage(CTxin)

CTxout = _reflection.GeneratedProtocolMessageType('CTxout', (_message.Message,), {
  'DESCRIPTOR' : _CTXOUT,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CTxout)
  })
_sym_db.RegisterMessage(CTxout)

CSignPreHash = _reflection.GeneratedProtocolMessageType('CSignPreHash', (_message.Message,), {
  'DESCRIPTOR' : _CSIGNPREHASH,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CSignPreHash)
  })
_sym_db.RegisterMessage(CSignPreHash)

CTransaction = _reflection.GeneratedProtocolMessageType('CTransaction', (_message.Message,), {
  'DESCRIPTOR' : _CTRANSACTION,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:CTransaction)
  })
_sym_db.RegisterMessage(CTransaction)


# @@protoc_insertion_point(module_scope)

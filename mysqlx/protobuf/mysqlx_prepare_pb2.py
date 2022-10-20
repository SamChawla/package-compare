# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_prepare.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mysqlx.protobuf import mysqlx_sql_pb2
from mysqlx.protobuf import mysqlx_crud_pb2
from mysqlx.protobuf import mysqlx_datatypes_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_prepare.proto',
  package='Mysqlx.Prepare',
  serialized_pb=_b('\n\x14mysqlx_prepare.proto\x12\x0eMysqlx.Prepare\x1a\x10mysqlx_sql.proto\x1a\x11mysqlx_crud.proto\x1a\x16mysqlx_datatypes.proto\"\x97\x03\n\x07Prepare\x12\x0f\n\x07stmt_id\x18\x01 \x02(\r\x12\x32\n\x04stmt\x18\x02 \x02(\x0b\x32$.Mysqlx.Prepare.Prepare.OneOfMessage\x1a\xc6\x02\n\x0cOneOfMessage\x12\x37\n\x04type\x18\x01 \x02(\x0e\x32).Mysqlx.Prepare.Prepare.OneOfMessage.Type\x12\x1f\n\x04\x66ind\x18\x02 \x01(\x0b\x32\x11.Mysqlx.Crud.Find\x12#\n\x06insert\x18\x03 \x01(\x0b\x32\x13.Mysqlx.Crud.Insert\x12#\n\x06update\x18\x04 \x01(\x0b\x32\x13.Mysqlx.Crud.Update\x12#\n\x06\x64\x65lete\x18\x05 \x01(\x0b\x32\x13.Mysqlx.Crud.Delete\x12-\n\x0cstmt_execute\x18\x06 \x01(\x0b\x32\x17.Mysqlx.Sql.StmtExecute\">\n\x04Type\x12\x08\n\x04\x46IND\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x04\x12\x08\n\x04STMT\x10\x05\"`\n\x07\x45xecute\x12\x0f\n\x07stmt_id\x18\x01 \x02(\r\x12#\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x15.Mysqlx.Datatypes.Any\x12\x1f\n\x10\x63ompact_metadata\x18\x03 \x01(\x08:\x05\x66\x61lse\"\x1d\n\nDeallocate\x12\x0f\n\x07stmt_id\x18\x01 \x02(\rB\x1b\n\x17\x63om.mysql.cj.x.protobufH\x03')
  ,
  dependencies=[mysqlx_sql_pb2.DESCRIPTOR,mysqlx_crud_pb2.DESCRIPTOR,mysqlx_datatypes_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREPARE_ONEOFMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Mysqlx.Prepare.Prepare.OneOfMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STMT', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=447,
  serialized_end=509,
)
_sym_db.RegisterEnumDescriptor(_PREPARE_ONEOFMESSAGE_TYPE)


_PREPARE_ONEOFMESSAGE = _descriptor.Descriptor(
  name='OneOfMessage',
  full_name='Mysqlx.Prepare.Prepare.OneOfMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='find', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.find', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insert', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.insert', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.update', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.delete', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmt_execute', full_name='Mysqlx.Prepare.Prepare.OneOfMessage.stmt_execute', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREPARE_ONEOFMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=509,
)

_PREPARE = _descriptor.Descriptor(
  name='Prepare',
  full_name='Mysqlx.Prepare.Prepare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stmt_id', full_name='Mysqlx.Prepare.Prepare.stmt_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmt', full_name='Mysqlx.Prepare.Prepare.stmt', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PREPARE_ONEOFMESSAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=509,
)


_EXECUTE = _descriptor.Descriptor(
  name='Execute',
  full_name='Mysqlx.Prepare.Execute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stmt_id', full_name='Mysqlx.Prepare.Execute.stmt_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='Mysqlx.Prepare.Execute.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compact_metadata', full_name='Mysqlx.Prepare.Execute.compact_metadata', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=511,
  serialized_end=607,
)


_DEALLOCATE = _descriptor.Descriptor(
  name='Deallocate',
  full_name='Mysqlx.Prepare.Deallocate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stmt_id', full_name='Mysqlx.Prepare.Deallocate.stmt_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=609,
  serialized_end=638,
)

_PREPARE_ONEOFMESSAGE.fields_by_name['type'].enum_type = _PREPARE_ONEOFMESSAGE_TYPE
_PREPARE_ONEOFMESSAGE.fields_by_name['find'].message_type = mysqlx_crud_pb2._FIND
_PREPARE_ONEOFMESSAGE.fields_by_name['insert'].message_type = mysqlx_crud_pb2._INSERT
_PREPARE_ONEOFMESSAGE.fields_by_name['update'].message_type = mysqlx_crud_pb2._UPDATE
_PREPARE_ONEOFMESSAGE.fields_by_name['delete'].message_type = mysqlx_crud_pb2._DELETE
_PREPARE_ONEOFMESSAGE.fields_by_name['stmt_execute'].message_type = mysqlx_sql_pb2._STMTEXECUTE
_PREPARE_ONEOFMESSAGE.containing_type = _PREPARE
_PREPARE_ONEOFMESSAGE_TYPE.containing_type = _PREPARE_ONEOFMESSAGE
_PREPARE.fields_by_name['stmt'].message_type = _PREPARE_ONEOFMESSAGE
_EXECUTE.fields_by_name['args'].message_type = mysqlx_datatypes_pb2._ANY
DESCRIPTOR.message_types_by_name['Prepare'] = _PREPARE
DESCRIPTOR.message_types_by_name['Execute'] = _EXECUTE
DESCRIPTOR.message_types_by_name['Deallocate'] = _DEALLOCATE

Prepare = _reflection.GeneratedProtocolMessageType('Prepare', (_message.Message,), dict(

  OneOfMessage = _reflection.GeneratedProtocolMessageType('OneOfMessage', (_message.Message,), dict(
    DESCRIPTOR = _PREPARE_ONEOFMESSAGE,
    __module__ = 'mysqlx_prepare_pb2'
    # @@protoc_insertion_point(class_scope:Mysqlx.Prepare.Prepare.OneOfMessage)
    ))
  ,
  DESCRIPTOR = _PREPARE,
  __module__ = 'mysqlx_prepare_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Prepare.Prepare)
  ))
_sym_db.RegisterMessage(Prepare)
_sym_db.RegisterMessage(Prepare.OneOfMessage)

Execute = _reflection.GeneratedProtocolMessageType('Execute', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTE,
  __module__ = 'mysqlx_prepare_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Prepare.Execute)
  ))
_sym_db.RegisterMessage(Execute)

Deallocate = _reflection.GeneratedProtocolMessageType('Deallocate', (_message.Message,), dict(
  DESCRIPTOR = _DEALLOCATE,
  __module__ = 'mysqlx_prepare_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Prepare.Deallocate)
  ))
_sym_db.RegisterMessage(Deallocate)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.mysql.cj.x.protobufH\003'))
# @@protoc_insertion_point(module_scope)

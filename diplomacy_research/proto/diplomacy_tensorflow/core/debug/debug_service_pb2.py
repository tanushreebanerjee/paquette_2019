# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/core/debug/debug_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from diplomacy_tensorflow.core.framework import tensor_pb2 as diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2
from diplomacy_tensorflow.core.profiler import tfprof_log_pb2 as diplomacy__tensorflow_dot_core_dot_profiler_dot_tfprof__log__pb2
from diplomacy_tensorflow.core.protobuf import debug_pb2 as diplomacy__tensorflow_dot_core_dot_protobuf_dot_debug__pb2
from diplomacy_tensorflow.core.util import event_pb2 as diplomacy__tensorflow_dot_core_dot_util_dot_event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/core/debug/debug_service.proto',
  package='diplomacy.tensorflow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3diplomacy_tensorflow/core/debug/debug_service.proto\x12\x14\x64iplomacy.tensorflow\x1a\x30\x64iplomacy_tensorflow/core/framework/tensor.proto\x1a\x33\x64iplomacy_tensorflow/core/profiler/tfprof_log.proto\x1a.diplomacy_tensorflow/core/protobuf/debug.proto\x1a*diplomacy_tensorflow/core/util/event.proto\"\xfc\x02\n\nEventReply\x12S\n\x16\x64\x65\x62ug_op_state_changes\x18\x01 \x03(\x0b\x32\x33.diplomacy.tensorflow.EventReply.DebugOpStateChange\x12\x31\n\x06tensor\x18\x02 \x01(\x0b\x32!.diplomacy.tensorflow.TensorProto\x1a\xe5\x01\n\x12\x44\x65\x62ugOpStateChange\x12H\n\x05state\x18\x01 \x01(\x0e\x32\x39.diplomacy.tensorflow.EventReply.DebugOpStateChange.State\x12\x11\n\tnode_name\x18\x02 \x01(\t\x12\x13\n\x0boutput_slot\x18\x03 \x01(\x05\x12\x10\n\x08\x64\x65\x62ug_op\x18\x04 \x01(\t\"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\r\n\tREAD_ONLY\x10\x02\x12\x0e\n\nREAD_WRITE\x10\x03\"\xcf\x03\n\rCallTraceback\x12?\n\tcall_type\x18\x01 \x01(\x0e\x32,.diplomacy.tensorflow.CallTraceback.CallType\x12\x10\n\x08\x63\x61ll_key\x18\x02 \x01(\t\x12:\n\x0corigin_stack\x18\x03 \x01(\x0b\x32$.diplomacy.tensorflow.tfprof.CodeDef\x12V\n\x13origin_id_to_string\x18\x04 \x03(\x0b\x32\x39.diplomacy.tensorflow.CallTraceback.OriginIdToStringEntry\x12@\n\x0fgraph_traceback\x18\x05 \x01(\x0b\x32\'.diplomacy.tensorflow.tfprof.OpLogProto\x12\x15\n\rgraph_version\x18\x06 \x01(\x03\x1a\x37\n\x15OriginIdToStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x08\x43\x61llType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x13\n\x0fGRAPH_EXECUTION\x10\x01\x12\x13\n\x0f\x45\x41GER_EXECUTION\x10\x02\x32\x99\x02\n\rEventListener\x12O\n\nSendEvents\x12\x1b.diplomacy.tensorflow.Event\x1a .diplomacy.tensorflow.EventReply(\x01\x30\x01\x12W\n\x0eSendTracebacks\x12#.diplomacy.tensorflow.CallTraceback\x1a .diplomacy.tensorflow.EventReply\x12^\n\x0fSendSourceFiles\x12).diplomacy.tensorflow.DebuggedSourceFiles\x1a .diplomacy.tensorflow.EventReplyb\x06proto3')
  ,
  dependencies=[diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,diplomacy__tensorflow_dot_core_dot_profiler_dot_tfprof__log__pb2.DESCRIPTOR,diplomacy__tensorflow_dot_core_dot_protobuf_dot_debug__pb2.DESCRIPTOR,diplomacy__tensorflow_dot_core_dot_util_dot_event__pb2.DESCRIPTOR,])



_EVENTREPLY_DEBUGOPSTATECHANGE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_ONLY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=578,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_EVENTREPLY_DEBUGOPSTATECHANGE_STATE)

_CALLTRACEBACK_CALLTYPE = _descriptor.EnumDescriptor(
  name='CallType',
  full_name='diplomacy.tensorflow.CallTraceback.CallType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAPH_EXECUTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EAGER_EXECUTION', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1050,
  serialized_end=1119,
)
_sym_db.RegisterEnumDescriptor(_CALLTRACEBACK_CALLTYPE)


_EVENTREPLY_DEBUGOPSTATECHANGE = _descriptor.Descriptor(
  name='DebugOpStateChange',
  full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange.node_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_slot', full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange.output_slot', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_op', full_name='diplomacy.tensorflow.EventReply.DebugOpStateChange.debug_op', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENTREPLY_DEBUGOPSTATECHANGE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=653,
)

_EVENTREPLY = _descriptor.Descriptor(
  name='EventReply',
  full_name='diplomacy.tensorflow.EventReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug_op_state_changes', full_name='diplomacy.tensorflow.EventReply.debug_op_state_changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='diplomacy.tensorflow.EventReply.tensor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENTREPLY_DEBUGOPSTATECHANGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=653,
)


_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY = _descriptor.Descriptor(
  name='OriginIdToStringEntry',
  full_name='diplomacy.tensorflow.CallTraceback.OriginIdToStringEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='diplomacy.tensorflow.CallTraceback.OriginIdToStringEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='diplomacy.tensorflow.CallTraceback.OriginIdToStringEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1048,
)

_CALLTRACEBACK = _descriptor.Descriptor(
  name='CallTraceback',
  full_name='diplomacy.tensorflow.CallTraceback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_type', full_name='diplomacy.tensorflow.CallTraceback.call_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_key', full_name='diplomacy.tensorflow.CallTraceback.call_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin_stack', full_name='diplomacy.tensorflow.CallTraceback.origin_stack', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin_id_to_string', full_name='diplomacy.tensorflow.CallTraceback.origin_id_to_string', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_traceback', full_name='diplomacy.tensorflow.CallTraceback.graph_traceback', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_version', full_name='diplomacy.tensorflow.CallTraceback.graph_version', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY, ],
  enum_types=[
    _CALLTRACEBACK_CALLTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=1119,
)

_EVENTREPLY_DEBUGOPSTATECHANGE.fields_by_name['state'].enum_type = _EVENTREPLY_DEBUGOPSTATECHANGE_STATE
_EVENTREPLY_DEBUGOPSTATECHANGE.containing_type = _EVENTREPLY
_EVENTREPLY_DEBUGOPSTATECHANGE_STATE.containing_type = _EVENTREPLY_DEBUGOPSTATECHANGE
_EVENTREPLY.fields_by_name['debug_op_state_changes'].message_type = _EVENTREPLY_DEBUGOPSTATECHANGE
_EVENTREPLY.fields_by_name['tensor'].message_type = diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY.containing_type = _CALLTRACEBACK
_CALLTRACEBACK.fields_by_name['call_type'].enum_type = _CALLTRACEBACK_CALLTYPE
_CALLTRACEBACK.fields_by_name['origin_stack'].message_type = diplomacy__tensorflow_dot_core_dot_profiler_dot_tfprof__log__pb2._CODEDEF
_CALLTRACEBACK.fields_by_name['origin_id_to_string'].message_type = _CALLTRACEBACK_ORIGINIDTOSTRINGENTRY
_CALLTRACEBACK.fields_by_name['graph_traceback'].message_type = diplomacy__tensorflow_dot_core_dot_profiler_dot_tfprof__log__pb2._OPLOGPROTO
_CALLTRACEBACK_CALLTYPE.containing_type = _CALLTRACEBACK
DESCRIPTOR.message_types_by_name['EventReply'] = _EVENTREPLY
DESCRIPTOR.message_types_by_name['CallTraceback'] = _CALLTRACEBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventReply = _reflection.GeneratedProtocolMessageType('EventReply', (_message.Message,), dict(

  DebugOpStateChange = _reflection.GeneratedProtocolMessageType('DebugOpStateChange', (_message.Message,), dict(
    DESCRIPTOR = _EVENTREPLY_DEBUGOPSTATECHANGE,
    __module__ = 'diplomacy_tensorflow.core.debug.debug_service_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.EventReply.DebugOpStateChange)
    ))
  ,
  DESCRIPTOR = _EVENTREPLY,
  __module__ = 'diplomacy_tensorflow.core.debug.debug_service_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.EventReply)
  ))
_sym_db.RegisterMessage(EventReply)
_sym_db.RegisterMessage(EventReply.DebugOpStateChange)

CallTraceback = _reflection.GeneratedProtocolMessageType('CallTraceback', (_message.Message,), dict(

  OriginIdToStringEntry = _reflection.GeneratedProtocolMessageType('OriginIdToStringEntry', (_message.Message,), dict(
    DESCRIPTOR = _CALLTRACEBACK_ORIGINIDTOSTRINGENTRY,
    __module__ = 'diplomacy_tensorflow.core.debug.debug_service_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CallTraceback.OriginIdToStringEntry)
    ))
  ,
  DESCRIPTOR = _CALLTRACEBACK,
  __module__ = 'diplomacy_tensorflow.core.debug.debug_service_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.CallTraceback)
  ))
_sym_db.RegisterMessage(CallTraceback)
_sym_db.RegisterMessage(CallTraceback.OriginIdToStringEntry)


_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY._options = None

_EVENTLISTENER = _descriptor.ServiceDescriptor(
  name='EventListener',
  full_name='diplomacy.tensorflow.EventListener',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1122,
  serialized_end=1403,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendEvents',
    full_name='diplomacy.tensorflow.EventListener.SendEvents',
    index=0,
    containing_service=None,
    input_type=diplomacy__tensorflow_dot_core_dot_util_dot_event__pb2._EVENT,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendTracebacks',
    full_name='diplomacy.tensorflow.EventListener.SendTracebacks',
    index=1,
    containing_service=None,
    input_type=_CALLTRACEBACK,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendSourceFiles',
    full_name='diplomacy.tensorflow.EventListener.SendSourceFiles',
    index=2,
    containing_service=None,
    input_type=diplomacy__tensorflow_dot_core_dot_protobuf_dot_debug__pb2._DEBUGGEDSOURCEFILES,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTLISTENER)

DESCRIPTOR.services_by_name['EventListener'] = _EVENTLISTENER

# @@protoc_insertion_point(module_scope)
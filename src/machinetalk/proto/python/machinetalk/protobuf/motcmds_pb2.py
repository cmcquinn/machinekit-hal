# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinetalk/protobuf/motcmds.proto

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


from machinetalk.protobuf import emcclass_pb2 as machinetalk_dot_protobuf_dot_emcclass__pb2
from machinetalk.protobuf import nanopb_pb2 as machinetalk_dot_protobuf_dot_nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinetalk/protobuf/motcmds.proto',
  package='machinetalk',
  syntax='proto2',
  serialized_pb=_b('\n\"machinetalk/protobuf/motcmds.proto\x12\x0bmachinetalk\x1a#machinetalk/protobuf/emcclass.proto\x1a!machinetalk/protobuf/nanopb.proto\"\xa7\x07\n\rMotionCommand\x12(\n\x07\x63ommand\x18\n \x02(\x0e\x32\x17.machinetalk.cmd_code_t\x12\x12\n\ncommandNum\x18\x14 \x02(\x07\x12\x14\n\x0cmotor_offset\x18\x1e \x01(\x01\x12\x10\n\x08maxLimit\x18( \x01(\x01\x12\x10\n\x08minLimit\x18\x32 \x01(\x01\x12!\n\x03pos\x18< \x01(\x0b\x32\x14.machinetalk.EmcPose\x12(\n\x06\x63\x65nter\x18\x46 \x01(\x0b\x32\x18.machinetalk.PmCartesian\x12(\n\x06normal\x18P \x01(\x0b\x32\x18.machinetalk.PmCartesian\x12\x0c\n\x04turn\x18Z \x01(\x07\x12\x0b\n\x03vel\x18\x64 \x01(\x01\x12\x12\n\nini_maxvel\x18n \x01(\x01\x12,\n\x0bmotion_type\x18x \x01(\x0e\x32\x17.machinetalk.MotionType\x12\x14\n\x0bspindlesync\x18\x82\x01 \x01(\x01\x12\x0c\n\x03\x61\x63\x63\x18\x8c\x01 \x01(\x01\x12\x11\n\x08\x62\x61\x63klash\x18\x96\x01 \x01(\x01\x12\x0b\n\x02id\x18\xa0\x01 \x01(\x07\x12\x11\n\x08termCond\x18\xaa\x01 \x01(\x07\x12\x12\n\ttolerance\x18\xb4\x01 \x01(\x01\x12\r\n\x04\x61xis\x18\xbe\x01 \x01(\x07\x12\x0e\n\x05scale\x18\xc8\x01 \x01(\x01\x12\x0f\n\x06offset\x18\xd2\x01 \x01(\x01\x12\r\n\x04home\x18\xdc\x01 \x01(\x01\x12\x17\n\x0ehome_final_vel\x18\xe6\x01 \x01(\x01\x12\x13\n\nsearch_vel\x18\xf0\x01 \x01(\x01\x12\x12\n\tlatch_vel\x18\xfa\x01 \x01(\x01\x12\x0e\n\x05\x66lags\x18\x84\x02 \x01(\x07\x12\x16\n\rhome_sequence\x18\x8e\x02 \x01(\x07\x12\x16\n\rvolatile_home\x18\x98\x02 \x01(\x07\x12\x12\n\tminFerror\x18\xa2\x02 \x01(\x01\x12\x12\n\tmaxFerror\x18\xac\x02 \x01(\x01\x12\x0f\n\x06wdWait\x18\xb6\x02 \x01(\x07\x12\x0e\n\x05\x64\x65\x62ug\x18\xc0\x02 \x01(\x07\x12\x0c\n\x03now\x18\xca\x02 \x01(\x05\x12\x0c\n\x03out\x18\xd4\x02 \x01(\x05\x12\x0e\n\x05start\x18\xde\x02 \x01(\x05\x12\x0c\n\x03\x65nd\x18\xe8\x02 \x01(\x05\x12\r\n\x04mode\x18\xf2\x02 \x01(\x05\x12\x15\n\x0c\x63omp_nominal\x18\xfc\x02 \x01(\x01\x12\x15\n\x0c\x63omp_forward\x18\x86\x03 \x01(\x01\x12\x15\n\x0c\x63omp_reverse\x18\x90\x03 \x01(\x01\x12\x13\n\nprobe_type\x18\x9a\x03 \x01(\x05\x12*\n\x0btool_offset\x18\xa4\x03 \x01(\x0b\x32\x14.machinetalk.EmcPose:\x06\x92?\x03H\xd8\x04\"\xba\x01\n\x0cMotionStatus\x12,\n\x0b\x63ommandEcho\x18\n \x02(\x0e\x32\x17.machinetalk.cmd_code_t\x12\x16\n\x0e\x63ommandNumEcho\x18\x14 \x02(\x07\x12\x30\n\rcommandStatus\x18\x1e \x02(\x0e\x32\x19.machinetalk.cmd_status_t\x12*\n\x0c\x63\x61rte_pos_fb\x18( \x01(\x0b\x32\x14.machinetalk.EmcPose:\x06\x92?\x03H\xd9\x04*\xdc\x01\n\nMotionType\x12\x19\n\x15_EMC_MOTION_TYPE_NONE\x10\x00\x12\x1d\n\x19_EMC_MOTION_TYPE_TRAVERSE\x10\x01\x12\x19\n\x15_EMC_MOTION_TYPE_FEED\x10\x02\x12\x18\n\x14_EMC_MOTION_TYPE_ARC\x10\x03\x12\x1f\n\x1b_EMC_MOTION_TYPE_TOOLCHANGE\x10\x04\x12\x1c\n\x18_EMC_MOTION_TYPE_PROBING\x10\x05\x12 \n\x1c_EMC_MOTION_TYPE_INDEXROTARY\x10\x06*\xfb\x0b\n\ncmd_code_t\x12\x11\n\x0c\x45MCMOT_ABORT\x10\xa0\x1f\x12\x16\n\x11\x45MCMOT_AXIS_ABORT\x10\xa1\x1f\x12\x12\n\rEMCMOT_ENABLE\x10\xa2\x1f\x12\x13\n\x0e\x45MCMOT_DISABLE\x10\xa3\x1f\x12\x1c\n\x17\x45MCMOT_ENABLE_AMPLIFIER\x10\xa4\x1f\x12\x1d\n\x18\x45MCMOT_DISABLE_AMPLIFIER\x10\xa5\x1f\x12\x1b\n\x16\x45MCMOT_ENABLE_WATCHDOG\x10\xa6\x1f\x12\x1c\n\x17\x45MCMOT_DISABLE_WATCHDOG\x10\xa7\x1f\x12\x1a\n\x15\x45MCMOT_ACTIVATE_JOINT\x10\xa8\x1f\x12\x1c\n\x17\x45MCMOT_DEACTIVATE_JOINT\x10\xa9\x1f\x12\x11\n\x0c\x45MCMOT_PAUSE\x10\xaa\x1f\x12\x12\n\rEMCMOT_RESUME\x10\xab\x1f\x12\x10\n\x0b\x45MCMOT_STEP\x10\xac\x1f\x12\x10\n\x0b\x45MCMOT_FREE\x10\xad\x1f\x12\x11\n\x0c\x45MCMOT_COORD\x10\xae\x1f\x12\x12\n\rEMCMOT_TELEOP\x10\xaf\x1f\x12\x19\n\x14\x45MCMOT_SPINDLE_SCALE\x10\xb0\x1f\x12\x15\n\x10\x45MCMOT_SS_ENABLE\x10\xb1\x1f\x12\x16\n\x11\x45MCMOT_FEED_SCALE\x10\xb2\x1f\x12\x15\n\x10\x45MCMOT_FS_ENABLE\x10\xb3\x1f\x12\x15\n\x10\x45MCMOT_FH_ENABLE\x10\xb4\x1f\x12\x15\n\x10\x45MCMOT_AF_ENABLE\x10\xb5\x1f\x12\x1b\n\x16\x45MCMOT_OVERRIDE_LIMITS\x10\xb6\x1f\x12\x10\n\x0b\x45MCMOT_HOME\x10\xb7\x1f\x12\x12\n\rEMCMOT_UNHOME\x10\xb8\x1f\x12\x14\n\x0f\x45MCMOT_JOG_CONT\x10\xb9\x1f\x12\x14\n\x0f\x45MCMOT_JOG_INCR\x10\xba\x1f\x12\x13\n\x0e\x45MCMOT_JOG_ABS\x10\xbb\x1f\x12\x14\n\x0f\x45MCMOT_SET_LINE\x10\xbc\x1f\x12\x16\n\x11\x45MCMOT_SET_CIRCLE\x10\xbd\x1f\x12\x1d\n\x18\x45MCMOT_SET_TELEOP_VECTOR\x10\xbe\x1f\x12\x1d\n\x18\x45MCMOT_CLEAR_PROBE_FLAGS\x10\xbf\x1f\x12\x11\n\x0c\x45MCMOT_PROBE\x10\xc0\x1f\x12\x15\n\x10\x45MCMOT_RIGID_TAP\x10\xc1\x1f\x12\x1f\n\x1a\x45MCMOT_SET_POSITION_LIMITS\x10\xc2\x1f\x12\x18\n\x13\x45MCMOT_SET_BACKLASH\x10\xc3\x1f\x12\x1a\n\x15\x45MCMOT_SET_MIN_FERROR\x10\xc4\x1f\x12\x1a\n\x15\x45MCMOT_SET_MAX_FERROR\x10\xc5\x1f\x12\x13\n\x0e\x45MCMOT_SET_VEL\x10\xc6\x1f\x12\x19\n\x14\x45MCMOT_SET_VEL_LIMIT\x10\xc7\x1f\x12\x1f\n\x1a\x45MCMOT_SET_JOINT_VEL_LIMIT\x10\xc8\x1f\x12\x1f\n\x1a\x45MCMOT_SET_JOINT_ACC_LIMIT\x10\xc9\x1f\x12\x13\n\x0e\x45MCMOT_SET_ACC\x10\xca\x1f\x12\x19\n\x14\x45MCMOT_SET_TERM_COND\x10\xcb\x1f\x12\x18\n\x13\x45MCMOT_SET_NUM_AXES\x10\xcc\x1f\x12\x1a\n\x15\x45MCMOT_SET_WORLD_HOME\x10\xcd\x1f\x12\x1d\n\x18\x45MCMOT_SET_HOMING_PARAMS\x10\xce\x1f\x12\x15\n\x10\x45MCMOT_SET_DEBUG\x10\xcf\x1f\x12\x14\n\x0f\x45MCMOT_SET_DOUT\x10\xd0\x1f\x12\x14\n\x0f\x45MCMOT_SET_AOUT\x10\xd1\x1f\x12\x1b\n\x16\x45MCMOT_SET_SPINDLESYNC\x10\xd2\x1f\x12\x16\n\x11\x45MCMOT_SPINDLE_ON\x10\xd3\x1f\x12\x17\n\x12\x45MCMOT_SPINDLE_OFF\x10\xd4\x1f\x12\x1c\n\x17\x45MCMOT_SPINDLE_INCREASE\x10\xd5\x1f\x12\x1c\n\x17\x45MCMOT_SPINDLE_DECREASE\x10\xd6\x1f\x12 \n\x1b\x45MCMOT_SPINDLE_BRAKE_ENGAGE\x10\xd7\x1f\x12!\n\x1c\x45MCMOT_SPINDLE_BRAKE_RELEASE\x10\xd8\x1f\x12\x1c\n\x17\x45MCMOT_SET_MOTOR_OFFSET\x10\xd9\x1f\x12\x1a\n\x15\x45MCMOT_SET_JOINT_COMP\x10\xda\x1f\x12\x16\n\x11\x45MCMOT_SET_OFFSET\x10\xdb\x1f*\xad\x01\n\x0c\x63md_status_t\x12\x15\n\x11\x45MCMOT_COMMAND_OK\x10\x00\x12\"\n\x1e\x45MCMOT_COMMAND_UNKNOWN_COMMAND\x10\x01\x12\"\n\x1e\x45MCMOT_COMMAND_INVALID_COMMAND\x10\x02\x12!\n\x1d\x45MCMOT_COMMAND_INVALID_PARAMS\x10\x03\x12\x1b\n\x17\x45MCMOT_COMMAND_BAD_EXEC\x10\x04')
  ,
  dependencies=[machinetalk_dot_protobuf_dot_emcclass__pb2.DESCRIPTOR,machinetalk_dot_protobuf_dot_nanopb__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MOTIONTYPE = _descriptor.EnumDescriptor(
  name='MotionType',
  full_name='machinetalk.MotionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_TRAVERSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_FEED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_ARC', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_TOOLCHANGE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_PROBING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_EMC_MOTION_TYPE_INDEXROTARY', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1251,
  serialized_end=1471,
)
_sym_db.RegisterEnumDescriptor(_MOTIONTYPE)

MotionType = enum_type_wrapper.EnumTypeWrapper(_MOTIONTYPE)
_CMD_CODE_T = _descriptor.EnumDescriptor(
  name='cmd_code_t',
  full_name='machinetalk.cmd_code_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_ABORT', index=0, number=4000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_AXIS_ABORT', index=1, number=4001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_ENABLE', index=2, number=4002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_DISABLE', index=3, number=4003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_ENABLE_AMPLIFIER', index=4, number=4004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_DISABLE_AMPLIFIER', index=5, number=4005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_ENABLE_WATCHDOG', index=6, number=4006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_DISABLE_WATCHDOG', index=7, number=4007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_ACTIVATE_JOINT', index=8, number=4008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_DEACTIVATE_JOINT', index=9, number=4009,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_PAUSE', index=10, number=4010,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_RESUME', index=11, number=4011,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_STEP', index=12, number=4012,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_FREE', index=13, number=4013,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COORD', index=14, number=4014,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_TELEOP', index=15, number=4015,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_SCALE', index=16, number=4016,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SS_ENABLE', index=17, number=4017,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_FEED_SCALE', index=18, number=4018,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_FS_ENABLE', index=19, number=4019,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_FH_ENABLE', index=20, number=4020,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_AF_ENABLE', index=21, number=4021,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_OVERRIDE_LIMITS', index=22, number=4022,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_HOME', index=23, number=4023,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_UNHOME', index=24, number=4024,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_JOG_CONT', index=25, number=4025,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_JOG_INCR', index=26, number=4026,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_JOG_ABS', index=27, number=4027,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_LINE', index=28, number=4028,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_CIRCLE', index=29, number=4029,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_TELEOP_VECTOR', index=30, number=4030,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_CLEAR_PROBE_FLAGS', index=31, number=4031,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_PROBE', index=32, number=4032,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_RIGID_TAP', index=33, number=4033,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_POSITION_LIMITS', index=34, number=4034,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_BACKLASH', index=35, number=4035,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_MIN_FERROR', index=36, number=4036,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_MAX_FERROR', index=37, number=4037,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_VEL', index=38, number=4038,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_VEL_LIMIT', index=39, number=4039,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_JOINT_VEL_LIMIT', index=40, number=4040,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_JOINT_ACC_LIMIT', index=41, number=4041,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_ACC', index=42, number=4042,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_TERM_COND', index=43, number=4043,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_NUM_AXES', index=44, number=4044,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_WORLD_HOME', index=45, number=4045,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_HOMING_PARAMS', index=46, number=4046,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_DEBUG', index=47, number=4047,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_DOUT', index=48, number=4048,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_AOUT', index=49, number=4049,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_SPINDLESYNC', index=50, number=4050,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_ON', index=51, number=4051,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_OFF', index=52, number=4052,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_INCREASE', index=53, number=4053,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_DECREASE', index=54, number=4054,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_BRAKE_ENGAGE', index=55, number=4055,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SPINDLE_BRAKE_RELEASE', index=56, number=4056,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_MOTOR_OFFSET', index=57, number=4057,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_JOINT_COMP', index=58, number=4058,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_SET_OFFSET', index=59, number=4059,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1474,
  serialized_end=3005,
)
_sym_db.RegisterEnumDescriptor(_CMD_CODE_T)

cmd_code_t = enum_type_wrapper.EnumTypeWrapper(_CMD_CODE_T)
_CMD_STATUS_T = _descriptor.EnumDescriptor(
  name='cmd_status_t',
  full_name='machinetalk.cmd_status_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COMMAND_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COMMAND_UNKNOWN_COMMAND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COMMAND_INVALID_COMMAND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COMMAND_INVALID_PARAMS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMCMOT_COMMAND_BAD_EXEC', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3008,
  serialized_end=3181,
)
_sym_db.RegisterEnumDescriptor(_CMD_STATUS_T)

cmd_status_t = enum_type_wrapper.EnumTypeWrapper(_CMD_STATUS_T)
_EMC_MOTION_TYPE_NONE = 0
_EMC_MOTION_TYPE_TRAVERSE = 1
_EMC_MOTION_TYPE_FEED = 2
_EMC_MOTION_TYPE_ARC = 3
_EMC_MOTION_TYPE_TOOLCHANGE = 4
_EMC_MOTION_TYPE_PROBING = 5
_EMC_MOTION_TYPE_INDEXROTARY = 6
EMCMOT_ABORT = 4000
EMCMOT_AXIS_ABORT = 4001
EMCMOT_ENABLE = 4002
EMCMOT_DISABLE = 4003
EMCMOT_ENABLE_AMPLIFIER = 4004
EMCMOT_DISABLE_AMPLIFIER = 4005
EMCMOT_ENABLE_WATCHDOG = 4006
EMCMOT_DISABLE_WATCHDOG = 4007
EMCMOT_ACTIVATE_JOINT = 4008
EMCMOT_DEACTIVATE_JOINT = 4009
EMCMOT_PAUSE = 4010
EMCMOT_RESUME = 4011
EMCMOT_STEP = 4012
EMCMOT_FREE = 4013
EMCMOT_COORD = 4014
EMCMOT_TELEOP = 4015
EMCMOT_SPINDLE_SCALE = 4016
EMCMOT_SS_ENABLE = 4017
EMCMOT_FEED_SCALE = 4018
EMCMOT_FS_ENABLE = 4019
EMCMOT_FH_ENABLE = 4020
EMCMOT_AF_ENABLE = 4021
EMCMOT_OVERRIDE_LIMITS = 4022
EMCMOT_HOME = 4023
EMCMOT_UNHOME = 4024
EMCMOT_JOG_CONT = 4025
EMCMOT_JOG_INCR = 4026
EMCMOT_JOG_ABS = 4027
EMCMOT_SET_LINE = 4028
EMCMOT_SET_CIRCLE = 4029
EMCMOT_SET_TELEOP_VECTOR = 4030
EMCMOT_CLEAR_PROBE_FLAGS = 4031
EMCMOT_PROBE = 4032
EMCMOT_RIGID_TAP = 4033
EMCMOT_SET_POSITION_LIMITS = 4034
EMCMOT_SET_BACKLASH = 4035
EMCMOT_SET_MIN_FERROR = 4036
EMCMOT_SET_MAX_FERROR = 4037
EMCMOT_SET_VEL = 4038
EMCMOT_SET_VEL_LIMIT = 4039
EMCMOT_SET_JOINT_VEL_LIMIT = 4040
EMCMOT_SET_JOINT_ACC_LIMIT = 4041
EMCMOT_SET_ACC = 4042
EMCMOT_SET_TERM_COND = 4043
EMCMOT_SET_NUM_AXES = 4044
EMCMOT_SET_WORLD_HOME = 4045
EMCMOT_SET_HOMING_PARAMS = 4046
EMCMOT_SET_DEBUG = 4047
EMCMOT_SET_DOUT = 4048
EMCMOT_SET_AOUT = 4049
EMCMOT_SET_SPINDLESYNC = 4050
EMCMOT_SPINDLE_ON = 4051
EMCMOT_SPINDLE_OFF = 4052
EMCMOT_SPINDLE_INCREASE = 4053
EMCMOT_SPINDLE_DECREASE = 4054
EMCMOT_SPINDLE_BRAKE_ENGAGE = 4055
EMCMOT_SPINDLE_BRAKE_RELEASE = 4056
EMCMOT_SET_MOTOR_OFFSET = 4057
EMCMOT_SET_JOINT_COMP = 4058
EMCMOT_SET_OFFSET = 4059
EMCMOT_COMMAND_OK = 0
EMCMOT_COMMAND_UNKNOWN_COMMAND = 1
EMCMOT_COMMAND_INVALID_COMMAND = 2
EMCMOT_COMMAND_INVALID_PARAMS = 3
EMCMOT_COMMAND_BAD_EXEC = 4



_MOTIONCOMMAND = _descriptor.Descriptor(
  name='MotionCommand',
  full_name='machinetalk.MotionCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='machinetalk.MotionCommand.command', index=0,
      number=10, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=4000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandNum', full_name='machinetalk.MotionCommand.commandNum', index=1,
      number=20, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motor_offset', full_name='machinetalk.MotionCommand.motor_offset', index=2,
      number=30, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxLimit', full_name='machinetalk.MotionCommand.maxLimit', index=3,
      number=40, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minLimit', full_name='machinetalk.MotionCommand.minLimit', index=4,
      number=50, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos', full_name='machinetalk.MotionCommand.pos', index=5,
      number=60, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center', full_name='machinetalk.MotionCommand.center', index=6,
      number=70, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normal', full_name='machinetalk.MotionCommand.normal', index=7,
      number=80, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turn', full_name='machinetalk.MotionCommand.turn', index=8,
      number=90, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vel', full_name='machinetalk.MotionCommand.vel', index=9,
      number=100, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ini_maxvel', full_name='machinetalk.MotionCommand.ini_maxvel', index=10,
      number=110, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motion_type', full_name='machinetalk.MotionCommand.motion_type', index=11,
      number=120, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spindlesync', full_name='machinetalk.MotionCommand.spindlesync', index=12,
      number=130, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc', full_name='machinetalk.MotionCommand.acc', index=13,
      number=140, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backlash', full_name='machinetalk.MotionCommand.backlash', index=14,
      number=150, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='machinetalk.MotionCommand.id', index=15,
      number=160, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='termCond', full_name='machinetalk.MotionCommand.termCond', index=16,
      number=170, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tolerance', full_name='machinetalk.MotionCommand.tolerance', index=17,
      number=180, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axis', full_name='machinetalk.MotionCommand.axis', index=18,
      number=190, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='machinetalk.MotionCommand.scale', index=19,
      number=200, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='machinetalk.MotionCommand.offset', index=20,
      number=210, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='home', full_name='machinetalk.MotionCommand.home', index=21,
      number=220, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='home_final_vel', full_name='machinetalk.MotionCommand.home_final_vel', index=22,
      number=230, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_vel', full_name='machinetalk.MotionCommand.search_vel', index=23,
      number=240, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latch_vel', full_name='machinetalk.MotionCommand.latch_vel', index=24,
      number=250, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='machinetalk.MotionCommand.flags', index=25,
      number=260, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='home_sequence', full_name='machinetalk.MotionCommand.home_sequence', index=26,
      number=270, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volatile_home', full_name='machinetalk.MotionCommand.volatile_home', index=27,
      number=280, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minFerror', full_name='machinetalk.MotionCommand.minFerror', index=28,
      number=290, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxFerror', full_name='machinetalk.MotionCommand.maxFerror', index=29,
      number=300, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wdWait', full_name='machinetalk.MotionCommand.wdWait', index=30,
      number=310, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='machinetalk.MotionCommand.debug', index=31,
      number=320, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now', full_name='machinetalk.MotionCommand.now', index=32,
      number=330, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='machinetalk.MotionCommand.out', index=33,
      number=340, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='machinetalk.MotionCommand.start', index=34,
      number=350, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='machinetalk.MotionCommand.end', index=35,
      number=360, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='machinetalk.MotionCommand.mode', index=36,
      number=370, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comp_nominal', full_name='machinetalk.MotionCommand.comp_nominal', index=37,
      number=380, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comp_forward', full_name='machinetalk.MotionCommand.comp_forward', index=38,
      number=390, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comp_reverse', full_name='machinetalk.MotionCommand.comp_reverse', index=39,
      number=400, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probe_type', full_name='machinetalk.MotionCommand.probe_type', index=40,
      number=410, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tool_offset', full_name='machinetalk.MotionCommand.tool_offset', index=41,
      number=420, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\330\004')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=1059,
)


_MOTIONSTATUS = _descriptor.Descriptor(
  name='MotionStatus',
  full_name='machinetalk.MotionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commandEcho', full_name='machinetalk.MotionStatus.commandEcho', index=0,
      number=10, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=4000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandNumEcho', full_name='machinetalk.MotionStatus.commandNumEcho', index=1,
      number=20, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandStatus', full_name='machinetalk.MotionStatus.commandStatus', index=2,
      number=30, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carte_pos_fb', full_name='machinetalk.MotionStatus.carte_pos_fb', index=3,
      number=40, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\331\004')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1248,
)

_MOTIONCOMMAND.fields_by_name['command'].enum_type = _CMD_CODE_T
_MOTIONCOMMAND.fields_by_name['pos'].message_type = machinetalk_dot_protobuf_dot_emcclass__pb2._EMCPOSE
_MOTIONCOMMAND.fields_by_name['center'].message_type = machinetalk_dot_protobuf_dot_emcclass__pb2._PMCARTESIAN
_MOTIONCOMMAND.fields_by_name['normal'].message_type = machinetalk_dot_protobuf_dot_emcclass__pb2._PMCARTESIAN
_MOTIONCOMMAND.fields_by_name['motion_type'].enum_type = _MOTIONTYPE
_MOTIONCOMMAND.fields_by_name['tool_offset'].message_type = machinetalk_dot_protobuf_dot_emcclass__pb2._EMCPOSE
_MOTIONSTATUS.fields_by_name['commandEcho'].enum_type = _CMD_CODE_T
_MOTIONSTATUS.fields_by_name['commandStatus'].enum_type = _CMD_STATUS_T
_MOTIONSTATUS.fields_by_name['carte_pos_fb'].message_type = machinetalk_dot_protobuf_dot_emcclass__pb2._EMCPOSE
DESCRIPTOR.message_types_by_name['MotionCommand'] = _MOTIONCOMMAND
DESCRIPTOR.message_types_by_name['MotionStatus'] = _MOTIONSTATUS
DESCRIPTOR.enum_types_by_name['MotionType'] = _MOTIONTYPE
DESCRIPTOR.enum_types_by_name['cmd_code_t'] = _CMD_CODE_T
DESCRIPTOR.enum_types_by_name['cmd_status_t'] = _CMD_STATUS_T

MotionCommand = _reflection.GeneratedProtocolMessageType('MotionCommand', (_message.Message,), dict(
  DESCRIPTOR = _MOTIONCOMMAND,
  __module__ = 'machinetalk.protobuf.motcmds_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.MotionCommand)
  ))
_sym_db.RegisterMessage(MotionCommand)

MotionStatus = _reflection.GeneratedProtocolMessageType('MotionStatus', (_message.Message,), dict(
  DESCRIPTOR = _MOTIONSTATUS,
  __module__ = 'machinetalk.protobuf.motcmds_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.MotionStatus)
  ))
_sym_db.RegisterMessage(MotionStatus)


_MOTIONCOMMAND.has_options = True
_MOTIONCOMMAND._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\330\004'))
_MOTIONSTATUS.has_options = True
_MOTIONSTATUS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\331\004'))
# @@protoc_insertion_point(module_scope)
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MPE(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MPE()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMPE(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def MPEBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x24\x4F\x4D\x4D", size_prefixed=size_prefixed)

    # MPE
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MPE
    def MEAN_MOTION(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def ECCENTRICITY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def INCLINATION(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def RA_OF_ASC_NODE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def ARG_OF_PERICENTER(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def MEAN_ANOMALY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def NORAD_CAT_ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MPE
    def BSTAR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def USER_DEFINED_EPOCH_TIMESTAMP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

def MPEStart(builder): builder.StartObject(9)
def Start(builder):
    return MPEStart(builder)
def MPEAddMEAN_MOTION(builder, MEAN_MOTION): builder.Prependfloat64Slot(0, MEAN_MOTION, 0.0)
def AddMEAN_MOTION(builder, MEAN_MOTION):
    return MPEAddMEAN_MOTION(builder, MEAN_MOTION)
def MPEAddECCENTRICITY(builder, ECCENTRICITY): builder.Prependfloat64Slot(1, ECCENTRICITY, 0.0)
def AddECCENTRICITY(builder, ECCENTRICITY):
    return MPEAddECCENTRICITY(builder, ECCENTRICITY)
def MPEAddINCLINATION(builder, INCLINATION): builder.Prependfloat64Slot(2, INCLINATION, 0.0)
def AddINCLINATION(builder, INCLINATION):
    return MPEAddINCLINATION(builder, INCLINATION)
def MPEAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE): builder.Prependfloat64Slot(3, RA_OF_ASC_NODE, 0.0)
def AddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE):
    return MPEAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE)
def MPEAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER): builder.Prependfloat64Slot(4, ARG_OF_PERICENTER, 0.0)
def AddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER):
    return MPEAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER)
def MPEAddMEAN_ANOMALY(builder, MEAN_ANOMALY): builder.Prependfloat64Slot(5, MEAN_ANOMALY, 0.0)
def AddMEAN_ANOMALY(builder, MEAN_ANOMALY):
    return MPEAddMEAN_ANOMALY(builder, MEAN_ANOMALY)
def MPEAddNORAD_CAT_ID(builder, NORAD_CAT_ID): builder.Prependuint32Slot(6, NORAD_CAT_ID, 0)
def AddNORAD_CAT_ID(builder, NORAD_CAT_ID):
    return MPEAddNORAD_CAT_ID(builder, NORAD_CAT_ID)
def MPEAddBSTAR(builder, BSTAR): builder.Prependfloat64Slot(7, BSTAR, 0.0)
def AddBSTAR(builder, BSTAR):
    return MPEAddBSTAR(builder, BSTAR)
def MPEAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP): builder.Prependfloat64Slot(8, USER_DEFINED_EPOCH_TIMESTAMP, 0.0)
def AddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP):
    return MPEAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP)
def MPEEnd(builder): return builder.EndObject()
def End(builder):
    return MPEEnd(builder)
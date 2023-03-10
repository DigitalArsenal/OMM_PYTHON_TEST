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
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def ECCENTRICITY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def INCLINATION(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def RA_OF_ASC_NODE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def ARG_OF_PERICENTER(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def MEAN_ANOMALY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
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
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # MPE
    def USER_DEFINED_EPOCH_TIMESTAMP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def MPEStart(builder): builder.StartObject(9)
def Start(builder):
    return MPEStart(builder)
def MPEAddMEAN_MOTION(builder, MEAN_MOTION): builder.PrependFloat64Slot(0, MEAN_MOTION, 0.0)
def AddMEAN_MOTION(builder, MEAN_MOTION):
    return MPEAddMEAN_MOTION(builder, MEAN_MOTION)
def MPEAddECCENTRICITY(builder, ECCENTRICITY): builder.PrependFloat64Slot(1, ECCENTRICITY, 0.0)
def AddECCENTRICITY(builder, ECCENTRICITY):
    return MPEAddECCENTRICITY(builder, ECCENTRICITY)
def MPEAddINCLINATION(builder, INCLINATION): builder.PrependFloat64Slot(2, INCLINATION, 0.0)
def AddINCLINATION(builder, INCLINATION):
    return MPEAddINCLINATION(builder, INCLINATION)
def MPEAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE): builder.PrependFloat64Slot(3, RA_OF_ASC_NODE, 0.0)
def AddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE):
    return MPEAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE)
def MPEAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER): builder.PrependFloat64Slot(4, ARG_OF_PERICENTER, 0.0)
def AddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER):
    return MPEAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER)
def MPEAddMEAN_ANOMALY(builder, MEAN_ANOMALY): builder.PrependFloat64Slot(5, MEAN_ANOMALY, 0.0)
def AddMEAN_ANOMALY(builder, MEAN_ANOMALY):
    return MPEAddMEAN_ANOMALY(builder, MEAN_ANOMALY)
def MPEAddNORAD_CAT_ID(builder, NORAD_CAT_ID): builder.PrependUint32Slot(6, NORAD_CAT_ID, 0)
def AddNORAD_CAT_ID(builder, NORAD_CAT_ID):
    return MPEAddNORAD_CAT_ID(builder, NORAD_CAT_ID)
def MPEAddBSTAR(builder, BSTAR): builder.PrependFloat64Slot(7, BSTAR, 0.0)
def AddBSTAR(builder, BSTAR):
    return MPEAddBSTAR(builder, BSTAR)
def MPEAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP): builder.PrependFloat64Slot(8, USER_DEFINED_EPOCH_TIMESTAMP, 0.0)
def AddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP):
    return MPEAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP)
def MPEEnd(builder): return builder.EndObject()
def End(builder):
    return MPEEnd(builder)

class MPET(object):

    # MPET
    def __init__(self):
        self.MEAN_MOTION = 0.0  # type: float
        self.ECCENTRICITY = 0.0  # type: float
        self.INCLINATION = 0.0  # type: float
        self.RA_OF_ASC_NODE = 0.0  # type: float
        self.ARG_OF_PERICENTER = 0.0  # type: float
        self.MEAN_ANOMALY = 0.0  # type: float
        self.NORAD_CAT_ID = 0  # type: int
        self.BSTAR = 0.0  # type: float
        self.USER_DEFINED_EPOCH_TIMESTAMP = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        MPE = MPE()
        MPE.Init(buf, pos)
        return cls.InitFromObj(MPE)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, MPE):
        x = MPET()
        x._UnPack(MPE)
        return x

    # MPET
    def _UnPack(self, MPE):
        if MPE is None:
            return
        self.MEAN_MOTION = MPE.MEAN_MOTION()
        self.ECCENTRICITY = MPE.ECCENTRICITY()
        self.INCLINATION = MPE.INCLINATION()
        self.RA_OF_ASC_NODE = MPE.RA_OF_ASC_NODE()
        self.ARG_OF_PERICENTER = MPE.ARG_OF_PERICENTER()
        self.MEAN_ANOMALY = MPE.MEAN_ANOMALY()
        self.NORAD_CAT_ID = MPE.NORAD_CAT_ID()
        self.BSTAR = MPE.BSTAR()
        self.USER_DEFINED_EPOCH_TIMESTAMP = MPE.USER_DEFINED_EPOCH_TIMESTAMP()

    # MPET
    def Pack(self, builder):
        MPEStart(builder)
        MPEAddMEAN_MOTION(builder, self.MEAN_MOTION)
        MPEAddECCENTRICITY(builder, self.ECCENTRICITY)
        MPEAddINCLINATION(builder, self.INCLINATION)
        MPEAddRA_OF_ASC_NODE(builder, self.RA_OF_ASC_NODE)
        MPEAddARG_OF_PERICENTER(builder, self.ARG_OF_PERICENTER)
        MPEAddMEAN_ANOMALY(builder, self.MEAN_ANOMALY)
        MPEAddNORAD_CAT_ID(builder, self.NORAD_CAT_ID)
        MPEAddBSTAR(builder, self.BSTAR)
        MPEAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, self.USER_DEFINED_EPOCH_TIMESTAMP)
        MPE = MPEEnd(builder)
        return MPE

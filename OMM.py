# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OMM(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OMM()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOMM(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def OMMBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x24\x4F\x4D\x4D", size_prefixed=size_prefixed)

    # OMM
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OMM
    def CCSDS_OMM_VERS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CREATION_DATE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def ORIGINATOR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def OBJECT_NAME(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def OBJECT_ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def CENTER_NAME(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def REF_FRAME(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.int8Flags, o + self._tab.Pos)
        return 9

    # OMM
    def REF_FRAME_EPOCH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def TIME_SYSTEM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.int8Flags, o + self._tab.Pos)
        return 11

    # OMM
    def MEAN_ELEMENT_THEORY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.int8Flags, o + self._tab.Pos)
        return 0

    # OMM
    def COMMENT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def EPOCH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def SEMI_MAJOR_AXIS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def MEAN_MOTION(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def ECCENTRICITY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def INCLINATION(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def RA_OF_ASC_NODE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def ARG_OF_PERICENTER(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def MEAN_ANOMALY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def GM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def MASS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def SOLAR_RAD_AREA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def SOLAR_RAD_COEFF(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def DRAG_AREA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def DRAG_COEFF(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def EPHEMERIS_TYPE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.int8Flags, o + self._tab.Pos)
        return 1

    # OMM
    def CLASSIFICATION_TYPE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def NORAD_CAT_ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # OMM
    def ELEMENT_SET_NO(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # OMM
    def REV_AT_EPOCH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def BSTAR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def MEAN_MOTION_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def MEAN_MOTION_DDOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def COV_REF_FRAME(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.int8Flags, o + self._tab.Pos)
        return 0

    # OMM
    def CX_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CX_DOT_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CX_DOT_Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CX_DOT_Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CX_DOT_X_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_DOT_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_DOT_Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_DOT_Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_DOT_X_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CY_DOT_Y_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_X_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_Y_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def CZ_DOT_Z_DOT(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def USER_DEFINED_BIP_0044_TYPE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # OMM
    def USER_DEFINED_OBJECT_DESIGNATOR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def USER_DEFINED_EARTH_MODEL(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OMM
    def USER_DEFINED_EPOCH_TIMESTAMP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

    # OMM
    def USER_DEFINED_MICROSECONDS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.float64Flags, o + self._tab.Pos)
        return 0.0

def OMMStart(builder): builder.StartObject(60)
def Start(builder):
    return OMMStart(builder)
def OMMAddCCSDS_OMM_VERS(builder, CCSDS_OMM_VERS): builder.Prependfloat64Slot(0, CCSDS_OMM_VERS, 0.0)
def AddCCSDS_OMM_VERS(builder, CCSDS_OMM_VERS):
    return OMMAddCCSDS_OMM_VERS(builder, CCSDS_OMM_VERS)
def OMMAddCREATION_DATE(builder, CREATION_DATE): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(CREATION_DATE), 0)
def AddCREATION_DATE(builder, CREATION_DATE):
    return OMMAddCREATION_DATE(builder, CREATION_DATE)
def OMMAddORIGINATOR(builder, ORIGINATOR): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(ORIGINATOR), 0)
def AddORIGINATOR(builder, ORIGINATOR):
    return OMMAddORIGINATOR(builder, ORIGINATOR)
def OMMAddOBJECT_NAME(builder, OBJECT_NAME): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(OBJECT_NAME), 0)
def AddOBJECT_NAME(builder, OBJECT_NAME):
    return OMMAddOBJECT_NAME(builder, OBJECT_NAME)
def OMMAddOBJECT_ID(builder, OBJECT_ID): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(OBJECT_ID), 0)
def AddOBJECT_ID(builder, OBJECT_ID):
    return OMMAddOBJECT_ID(builder, OBJECT_ID)
def OMMAddCENTER_NAME(builder, CENTER_NAME): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(CENTER_NAME), 0)
def AddCENTER_NAME(builder, CENTER_NAME):
    return OMMAddCENTER_NAME(builder, CENTER_NAME)
def OMMAddREF_FRAME(builder, REF_FRAME): builder.Prependint8Slot(6, REF_FRAME, 9)
def AddREF_FRAME(builder, REF_FRAME):
    return OMMAddREF_FRAME(builder, REF_FRAME)
def OMMAddREF_FRAME_EPOCH(builder, REF_FRAME_EPOCH): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(REF_FRAME_EPOCH), 0)
def AddREF_FRAME_EPOCH(builder, REF_FRAME_EPOCH):
    return OMMAddREF_FRAME_EPOCH(builder, REF_FRAME_EPOCH)
def OMMAddTIME_SYSTEM(builder, TIME_SYSTEM): builder.Prependint8Slot(8, TIME_SYSTEM, 11)
def AddTIME_SYSTEM(builder, TIME_SYSTEM):
    return OMMAddTIME_SYSTEM(builder, TIME_SYSTEM)
def OMMAddMEAN_ELEMENT_THEORY(builder, MEAN_ELEMENT_THEORY): builder.Prependint8Slot(9, MEAN_ELEMENT_THEORY, 0)
def AddMEAN_ELEMENT_THEORY(builder, MEAN_ELEMENT_THEORY):
    return OMMAddMEAN_ELEMENT_THEORY(builder, MEAN_ELEMENT_THEORY)
def OMMAddCOMMENT(builder, COMMENT): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(COMMENT), 0)
def AddCOMMENT(builder, COMMENT):
    return OMMAddCOMMENT(builder, COMMENT)
def OMMAddEPOCH(builder, EPOCH): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(EPOCH), 0)
def AddEPOCH(builder, EPOCH):
    return OMMAddEPOCH(builder, EPOCH)
def OMMAddSEMI_MAJOR_AXIS(builder, SEMI_MAJOR_AXIS): builder.Prependfloat64Slot(12, SEMI_MAJOR_AXIS, 0.0)
def AddSEMI_MAJOR_AXIS(builder, SEMI_MAJOR_AXIS):
    return OMMAddSEMI_MAJOR_AXIS(builder, SEMI_MAJOR_AXIS)
def OMMAddMEAN_MOTION(builder, MEAN_MOTION): builder.Prependfloat64Slot(13, MEAN_MOTION, 0.0)
def AddMEAN_MOTION(builder, MEAN_MOTION):
    return OMMAddMEAN_MOTION(builder, MEAN_MOTION)
def OMMAddECCENTRICITY(builder, ECCENTRICITY): builder.Prependfloat64Slot(14, ECCENTRICITY, 0.0)
def AddECCENTRICITY(builder, ECCENTRICITY):
    return OMMAddECCENTRICITY(builder, ECCENTRICITY)
def OMMAddINCLINATION(builder, INCLINATION): builder.Prependfloat64Slot(15, INCLINATION, 0.0)
def AddINCLINATION(builder, INCLINATION):
    return OMMAddINCLINATION(builder, INCLINATION)
def OMMAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE): builder.Prependfloat64Slot(16, RA_OF_ASC_NODE, 0.0)
def AddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE):
    return OMMAddRA_OF_ASC_NODE(builder, RA_OF_ASC_NODE)
def OMMAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER): builder.Prependfloat64Slot(17, ARG_OF_PERICENTER, 0.0)
def AddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER):
    return OMMAddARG_OF_PERICENTER(builder, ARG_OF_PERICENTER)
def OMMAddMEAN_ANOMALY(builder, MEAN_ANOMALY): builder.Prependfloat64Slot(18, MEAN_ANOMALY, 0.0)
def AddMEAN_ANOMALY(builder, MEAN_ANOMALY):
    return OMMAddMEAN_ANOMALY(builder, MEAN_ANOMALY)
def OMMAddGM(builder, GM): builder.Prependfloat64Slot(19, GM, 0.0)
def AddGM(builder, GM):
    return OMMAddGM(builder, GM)
def OMMAddMASS(builder, MASS): builder.Prependfloat64Slot(20, MASS, 0.0)
def AddMASS(builder, MASS):
    return OMMAddMASS(builder, MASS)
def OMMAddSOLAR_RAD_AREA(builder, SOLAR_RAD_AREA): builder.Prependfloat64Slot(21, SOLAR_RAD_AREA, 0.0)
def AddSOLAR_RAD_AREA(builder, SOLAR_RAD_AREA):
    return OMMAddSOLAR_RAD_AREA(builder, SOLAR_RAD_AREA)
def OMMAddSOLAR_RAD_COEFF(builder, SOLAR_RAD_COEFF): builder.Prependfloat64Slot(22, SOLAR_RAD_COEFF, 0.0)
def AddSOLAR_RAD_COEFF(builder, SOLAR_RAD_COEFF):
    return OMMAddSOLAR_RAD_COEFF(builder, SOLAR_RAD_COEFF)
def OMMAddDRAG_AREA(builder, DRAG_AREA): builder.Prependfloat64Slot(23, DRAG_AREA, 0.0)
def AddDRAG_AREA(builder, DRAG_AREA):
    return OMMAddDRAG_AREA(builder, DRAG_AREA)
def OMMAddDRAG_COEFF(builder, DRAG_COEFF): builder.Prependfloat64Slot(24, DRAG_COEFF, 0.0)
def AddDRAG_COEFF(builder, DRAG_COEFF):
    return OMMAddDRAG_COEFF(builder, DRAG_COEFF)
def OMMAddEPHEMERIS_TYPE(builder, EPHEMERIS_TYPE): builder.Prependint8Slot(25, EPHEMERIS_TYPE, 1)
def AddEPHEMERIS_TYPE(builder, EPHEMERIS_TYPE):
    return OMMAddEPHEMERIS_TYPE(builder, EPHEMERIS_TYPE)
def OMMAddCLASSIFICATION_TYPE(builder, CLASSIFICATION_TYPE): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(CLASSIFICATION_TYPE), 0)
def AddCLASSIFICATION_TYPE(builder, CLASSIFICATION_TYPE):
    return OMMAddCLASSIFICATION_TYPE(builder, CLASSIFICATION_TYPE)
def OMMAddNORAD_CAT_ID(builder, NORAD_CAT_ID): builder.Prependuint32Slot(27, NORAD_CAT_ID, 0)
def AddNORAD_CAT_ID(builder, NORAD_CAT_ID):
    return OMMAddNORAD_CAT_ID(builder, NORAD_CAT_ID)
def OMMAddELEMENT_SET_NO(builder, ELEMENT_SET_NO): builder.Prependuint32Slot(28, ELEMENT_SET_NO, 0)
def AddELEMENT_SET_NO(builder, ELEMENT_SET_NO):
    return OMMAddELEMENT_SET_NO(builder, ELEMENT_SET_NO)
def OMMAddREV_AT_EPOCH(builder, REV_AT_EPOCH): builder.Prependfloat64Slot(29, REV_AT_EPOCH, 0.0)
def AddREV_AT_EPOCH(builder, REV_AT_EPOCH):
    return OMMAddREV_AT_EPOCH(builder, REV_AT_EPOCH)
def OMMAddBSTAR(builder, BSTAR): builder.Prependfloat64Slot(30, BSTAR, 0.0)
def AddBSTAR(builder, BSTAR):
    return OMMAddBSTAR(builder, BSTAR)
def OMMAddMEAN_MOTION_DOT(builder, MEAN_MOTION_DOT): builder.Prependfloat64Slot(31, MEAN_MOTION_DOT, 0.0)
def AddMEAN_MOTION_DOT(builder, MEAN_MOTION_DOT):
    return OMMAddMEAN_MOTION_DOT(builder, MEAN_MOTION_DOT)
def OMMAddMEAN_MOTION_DDOT(builder, MEAN_MOTION_DDOT): builder.Prependfloat64Slot(32, MEAN_MOTION_DDOT, 0.0)
def AddMEAN_MOTION_DDOT(builder, MEAN_MOTION_DDOT):
    return OMMAddMEAN_MOTION_DDOT(builder, MEAN_MOTION_DDOT)
def OMMAddCOV_REF_FRAME(builder, COV_REF_FRAME): builder.Prependint8Slot(33, COV_REF_FRAME, 0)
def AddCOV_REF_FRAME(builder, COV_REF_FRAME):
    return OMMAddCOV_REF_FRAME(builder, COV_REF_FRAME)
def OMMAddCX_X(builder, CX_X): builder.Prependfloat64Slot(34, CX_X, 0.0)
def AddCX_X(builder, CX_X):
    return OMMAddCX_X(builder, CX_X)
def OMMAddCY_X(builder, CY_X): builder.Prependfloat64Slot(35, CY_X, 0.0)
def AddCY_X(builder, CY_X):
    return OMMAddCY_X(builder, CY_X)
def OMMAddCY_Y(builder, CY_Y): builder.Prependfloat64Slot(36, CY_Y, 0.0)
def AddCY_Y(builder, CY_Y):
    return OMMAddCY_Y(builder, CY_Y)
def OMMAddCZ_X(builder, CZ_X): builder.Prependfloat64Slot(37, CZ_X, 0.0)
def AddCZ_X(builder, CZ_X):
    return OMMAddCZ_X(builder, CZ_X)
def OMMAddCZ_Y(builder, CZ_Y): builder.Prependfloat64Slot(38, CZ_Y, 0.0)
def AddCZ_Y(builder, CZ_Y):
    return OMMAddCZ_Y(builder, CZ_Y)
def OMMAddCZ_Z(builder, CZ_Z): builder.Prependfloat64Slot(39, CZ_Z, 0.0)
def AddCZ_Z(builder, CZ_Z):
    return OMMAddCZ_Z(builder, CZ_Z)
def OMMAddCX_DOT_X(builder, CX_DOT_X): builder.Prependfloat64Slot(40, CX_DOT_X, 0.0)
def AddCX_DOT_X(builder, CX_DOT_X):
    return OMMAddCX_DOT_X(builder, CX_DOT_X)
def OMMAddCX_DOT_Y(builder, CX_DOT_Y): builder.Prependfloat64Slot(41, CX_DOT_Y, 0.0)
def AddCX_DOT_Y(builder, CX_DOT_Y):
    return OMMAddCX_DOT_Y(builder, CX_DOT_Y)
def OMMAddCX_DOT_Z(builder, CX_DOT_Z): builder.Prependfloat64Slot(42, CX_DOT_Z, 0.0)
def AddCX_DOT_Z(builder, CX_DOT_Z):
    return OMMAddCX_DOT_Z(builder, CX_DOT_Z)
def OMMAddCX_DOT_X_DOT(builder, CX_DOT_X_DOT): builder.Prependfloat64Slot(43, CX_DOT_X_DOT, 0.0)
def AddCX_DOT_X_DOT(builder, CX_DOT_X_DOT):
    return OMMAddCX_DOT_X_DOT(builder, CX_DOT_X_DOT)
def OMMAddCY_DOT_X(builder, CY_DOT_X): builder.Prependfloat64Slot(44, CY_DOT_X, 0.0)
def AddCY_DOT_X(builder, CY_DOT_X):
    return OMMAddCY_DOT_X(builder, CY_DOT_X)
def OMMAddCY_DOT_Y(builder, CY_DOT_Y): builder.Prependfloat64Slot(45, CY_DOT_Y, 0.0)
def AddCY_DOT_Y(builder, CY_DOT_Y):
    return OMMAddCY_DOT_Y(builder, CY_DOT_Y)
def OMMAddCY_DOT_Z(builder, CY_DOT_Z): builder.Prependfloat64Slot(46, CY_DOT_Z, 0.0)
def AddCY_DOT_Z(builder, CY_DOT_Z):
    return OMMAddCY_DOT_Z(builder, CY_DOT_Z)
def OMMAddCY_DOT_X_DOT(builder, CY_DOT_X_DOT): builder.Prependfloat64Slot(47, CY_DOT_X_DOT, 0.0)
def AddCY_DOT_X_DOT(builder, CY_DOT_X_DOT):
    return OMMAddCY_DOT_X_DOT(builder, CY_DOT_X_DOT)
def OMMAddCY_DOT_Y_DOT(builder, CY_DOT_Y_DOT): builder.Prependfloat64Slot(48, CY_DOT_Y_DOT, 0.0)
def AddCY_DOT_Y_DOT(builder, CY_DOT_Y_DOT):
    return OMMAddCY_DOT_Y_DOT(builder, CY_DOT_Y_DOT)
def OMMAddCZ_DOT_X(builder, CZ_DOT_X): builder.Prependfloat64Slot(49, CZ_DOT_X, 0.0)
def AddCZ_DOT_X(builder, CZ_DOT_X):
    return OMMAddCZ_DOT_X(builder, CZ_DOT_X)
def OMMAddCZ_DOT_Y(builder, CZ_DOT_Y): builder.Prependfloat64Slot(50, CZ_DOT_Y, 0.0)
def AddCZ_DOT_Y(builder, CZ_DOT_Y):
    return OMMAddCZ_DOT_Y(builder, CZ_DOT_Y)
def OMMAddCZ_DOT_Z(builder, CZ_DOT_Z): builder.Prependfloat64Slot(51, CZ_DOT_Z, 0.0)
def AddCZ_DOT_Z(builder, CZ_DOT_Z):
    return OMMAddCZ_DOT_Z(builder, CZ_DOT_Z)
def OMMAddCZ_DOT_X_DOT(builder, CZ_DOT_X_DOT): builder.Prependfloat64Slot(52, CZ_DOT_X_DOT, 0.0)
def AddCZ_DOT_X_DOT(builder, CZ_DOT_X_DOT):
    return OMMAddCZ_DOT_X_DOT(builder, CZ_DOT_X_DOT)
def OMMAddCZ_DOT_Y_DOT(builder, CZ_DOT_Y_DOT): builder.Prependfloat64Slot(53, CZ_DOT_Y_DOT, 0.0)
def AddCZ_DOT_Y_DOT(builder, CZ_DOT_Y_DOT):
    return OMMAddCZ_DOT_Y_DOT(builder, CZ_DOT_Y_DOT)
def OMMAddCZ_DOT_Z_DOT(builder, CZ_DOT_Z_DOT): builder.Prependfloat64Slot(54, CZ_DOT_Z_DOT, 0.0)
def AddCZ_DOT_Z_DOT(builder, CZ_DOT_Z_DOT):
    return OMMAddCZ_DOT_Z_DOT(builder, CZ_DOT_Z_DOT)
def OMMAddUSER_DEFINED_BIP_0044_TYPE(builder, USER_DEFINED_BIP_0044_TYPE): builder.Prependuint32Slot(55, USER_DEFINED_BIP_0044_TYPE, 0)
def AddUSER_DEFINED_BIP_0044_TYPE(builder, USER_DEFINED_BIP_0044_TYPE):
    return OMMAddUSER_DEFINED_BIP_0044_TYPE(builder, USER_DEFINED_BIP_0044_TYPE)
def OMMAddUSER_DEFINED_OBJECT_DESIGNATOR(builder, USER_DEFINED_OBJECT_DESIGNATOR): builder.PrependUOffsetTRelativeSlot(56, flatbuffers.number_types.UOffsetTFlags.py_type(USER_DEFINED_OBJECT_DESIGNATOR), 0)
def AddUSER_DEFINED_OBJECT_DESIGNATOR(builder, USER_DEFINED_OBJECT_DESIGNATOR):
    return OMMAddUSER_DEFINED_OBJECT_DESIGNATOR(builder, USER_DEFINED_OBJECT_DESIGNATOR)
def OMMAddUSER_DEFINED_EARTH_MODEL(builder, USER_DEFINED_EARTH_MODEL): builder.PrependUOffsetTRelativeSlot(57, flatbuffers.number_types.UOffsetTFlags.py_type(USER_DEFINED_EARTH_MODEL), 0)
def AddUSER_DEFINED_EARTH_MODEL(builder, USER_DEFINED_EARTH_MODEL):
    return OMMAddUSER_DEFINED_EARTH_MODEL(builder, USER_DEFINED_EARTH_MODEL)
def OMMAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP): builder.Prependfloat64Slot(58, USER_DEFINED_EPOCH_TIMESTAMP, 0.0)
def AddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP):
    return OMMAddUSER_DEFINED_EPOCH_TIMESTAMP(builder, USER_DEFINED_EPOCH_TIMESTAMP)
def OMMAddUSER_DEFINED_MICROSECONDS(builder, USER_DEFINED_MICROSECONDS): builder.Prependfloat64Slot(59, USER_DEFINED_MICROSECONDS, 0.0)
def AddUSER_DEFINED_MICROSECONDS(builder, USER_DEFINED_MICROSECONDS):
    return OMMAddUSER_DEFINED_MICROSECONDS(builder, USER_DEFINED_MICROSECONDS)
def OMMEnd(builder): return builder.EndObject()
def End(builder):
    return OMMEnd(builder)
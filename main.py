from os import write
import subprocess
import OMMCOLLECTION
import OMM
import flatbuffers
from web3.auto import w3
from eth_account.messages import encode_defunct
from eth_account import Account


def calculate_cid(file_path):
    cmd = ['ipfs', 'add', '-n', file_path]
    output = subprocess.run(cmd, capture_output=True)
    cid = output.stdout.decode().strip().split(" ")[1]
    return cid


provider_eth_address = "0x9858EfFD232B4033E47d90003D41EC34EcaEda94"
fb_cid = "QmepW1hutjHdrPMhWBJCyinz8bfjtJ3WKsspb5vvcD6DTz"
pdFP = f"data/{provider_eth_address}/{fb_cid}.OMM.fbs"

# Load OMMCOLLECTION from file
with open(pdFP, "rb") as f:
    xOMM = f.read()

# Load the signature from a text file
with open(pdFP+".sig", "r") as f:
    signature = f.read()

message = encode_defunct(text=fb_cid)
stuff = w3.eth.account.recover_message(
    message, signature=signature)

print("Valid Digital Signature: ", stuff == provider_eth_address)

yOMMCOLLECTION = OMMCOLLECTION.OMMCOLLECTION.GetRootAsOMMCOLLECTION(xOMM)

for yOMM in range(yOMMCOLLECTION.RECORDSLength()):
    yOMMRECORD = yOMMCOLLECTION.RECORDS(yOMM)
    # print(yOMMRECORD.NORAD_CAT_ID())

# create OMM object
ommt = OMM.OMMT()

# set OMM object properties
ommt.NORAD_CAT_ID = 25544
ommt.OBJECT_NAME = "ISS (ZARYA)"
ommt.OBJECT_ID = "1998-067A"
ommt.EPOCH = "2023-01-03T12:36:01.932768"
ommt.MEAN_MOTION = 15.49892242
ommt.ECCENTRICITY = 0.0005004
ommt.INCLINATION = 51.6453
ommt.RA_OF_ASC_NODE = 64.1711
ommt.ARG_OF_PERICENTER = 218.5032
ommt.MEAN_ANOMALY = 238.7671
ommt.EPHEMERIS_TYPE = 0
ommt.CLASSIFICATION_TYPE = "U"
ommt.ELEMENT_SET_NO = 999
ommt.REV_AT_EPOCH = 37625
ommt.BSTAR = 0.00030219
ommt.MEAN_MOTION_DOT = 0.00016767
ommt.MEAN_MOTION_DDOT = 0

# create builder and pack OMM properties
builder = flatbuffers.Builder()
builder.Finish(ommt.Pack(builder))
iss_buf = builder.Output()

# create OMMCOLLECTION and add OMM to the RECORDS list
ommc = OMMCOLLECTION.OMMCOLLECTIONT()
ommc.RECORDS = list()
ommc.RECORDS.append(ommt)
builder.Finish(ommc.Pack(builder))
ommc_buf = builder.Output()

# added OMM check
print("Added OMM has the same NORAD_CAT_ID: ",
      ommt.NORAD_CAT_ID == ommc.RECORDS[0].NORAD_CAT_ID)

iss = OMM.OMM.GetRootAs(iss_buf, 0)
print("CREATED OMM FOR ISS", iss.NORAD_CAT_ID())

ommc = OMMCOLLECTION.OMMCOLLECTION.GetRootAs(ommc_buf, 0)
print("CREATED OMMCOLLECTION, ADDED ISS", ommc.RECORDS(0).NORAD_CAT_ID())
print("\n")

iss_fp = "iss.fbs"
ommc_fp = "ommc.fbs"

iss_fpf = open(iss_fp, "wb")
iss_fpf.write(iss_buf)
iss_fpf.close()

ommc_fpf = open(ommc_fp, "wb")
ommc_fpf.write(ommc_buf)
ommc_fpf.close()

print(f"Original CID Match ({fb_cid[:7]}...{fb_cid[41:]}): ", fb_cid == calculate_cid(pdFP))

iss_cid = calculate_cid(iss_fp)
print("ISS CID: ", iss_cid)
ommc_cid = calculate_cid(ommc_fp)
print("OMMC CID: ", ommc_cid)
print("\n")
# `excess shallow future wheat amazing fee rug hammer hire crazy lumber mean`
key = "0x1ab42cc412b618bdea3a599e3c9bae199ebf030895b039e9db1e30dafb12b727"

signed_original = Account.sign_message(encode_defunct(text=fb_cid), key)
print(f"Original SIG Match ({signature[:7]}...{signature[127:]}): ", signature == signed_original.signature.hex())
signed_iss_cid = Account.sign_message(encode_defunct(text=iss_cid), key)
print("SIGNED ISS CID: ", signed_iss_cid.signature.hex())
signed_omm_cid = Account.sign_message(encode_defunct(text=ommc_cid), key)
print("SIGNED OMMC CID: ", signed_omm_cid.signature.hex())

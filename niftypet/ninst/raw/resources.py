"""Resources file for NiftyPET NIPET and NIMPA etc."""
__author__ = ("Pawel J. Markiewicz", "Casper O. da Costa-Luis")
__copyright__ = "Copyright 2018-20"

from math import ceil, pi

try:
    from numpy import array
except ImportError:

    def array(x):
        return x


# > logging represented by an integer: 10, 20, 30... for DEBUG, INFO, WARNING...
# > as it is in Python package logging, which is also used here.
LOG = 20

# Hardware (CT-based) mu-maps, which come with the mMR scanner.
# The names may be different
hrdwr_mu = [
    "umap_HNMCL_10606489.v.hdr",  # (1) Head and neck lower coil
    "umap_HNMCU_10606489.v.hdr",  # (2) Head and neck upper coil
    "umap_SPMC_10606491.v.hdr",  # (3) Spine coil
    "umap_PT_2291734.v.hdr",  # (4) Table
]

# Radioisotope look-up table
riLUT = {
    "Ge68": {"BF": 0.891, "thalf": 270.9516 * 24 * 60 * 60},
    "Ga68": {"BF": 0.891, "thalf": 67.71 * 60},
    "F18": {"BF": 0.967, "thalf": 109.77120 * 60},
    "C11": {"BF": 0.998, "thalf": 20.38 * 60},
    "O15": {"BF": 0.999, "thalf": 122.2416},
}

# -----------------------------------------------------
# The name and path to the NiftyPET tools (software)
DIRTOOLS = "NiftyPET_tools"
MSVC_VRSN = "Visual Studio 12 2013 Win64"
CMAKE_TLS_PAR = ""  # -DUSE_SSE=OFF'
# PATHTOOLS = os.path.join('/chosen/path/', DIRTOOLS)
# > path to Python wrapper of Vinci
VINCIPATH = ""

# > path to reference images for testing NiftyPET
REFPATH = ""
# -----------------------------------------------------

# -----------------------------------------------------
# DO NOT MODIFY BELOW--DONE AUTOMATICALLY
# # # start GPU properties # # #
# # # end GPU properties # # #

# paths to apps and tools needed by NiftyPET
# # # start NiftyPET tools # # #
# # # end NiftyPET tools # # #
# -----------------------------------------------------

# enable xnat module
ENBLXNAT = False
# enable Agg
ENBLAGG = False
# compile DCM2NIIX, otherwise download a compiled version for the system used
CMPL_DCM2NIIX = False

# ============ SIEMENS mMR SCANNER C O N S T A N T S ===============

# > LM header offset in bytes (for mMR it is in a separate DICOM format)
LMOFF = 0

# > bytes per event in list mode data
BPE = 4

# number of rings (axially) and crystals (transaxially)
NRNG = 64

# number of crystals transaxially
NCRS = 504

# > idealised crystal surface (used for scatter modelling)
SRFCRS = 0.1695112

# reduced number of crystals by the gaps (dead crystals)
NCRSR = 448

# maximum ring difference
MRD = 60

# number of linear indexes for 1/2 Michelogram (NRNG**2/2 + NRNG/2)
NLI2R = 2080 - 6

# number of angular indexes in a 2D sinogram
A = 252
# number of bin indexes in a 2D sino
W = 344
H = W / 2

NSN11 = 837
NSN1 = 4084
NSN64 = NRNG * NRNG
# 0: SSRB, 1: span-1, or 11: span-11 (11, default)
SPAN = 11

RNG_STRT = 0
RNG_END = 64


# ------------------------------------------------------
# > scatter axial ring definition
sct_irng = [0, 10, 19, 28, 35, 44, 53, 63]
# > resulting number of rings used for scatter modelling
NSRNG = len(sct_irng)
# ------------------------------------------------------


# no of sinos in a segment out of 11 segments
seg = array([127, 115, 115, 93, 93, 71, 71, 49, 49, 27, 27])

# minimum and maximum ring difference for each segment
minrd = array([-5, -16, 6, -27, 17, -38, 28, -49, 39, -60, 50])
maxrd = array([5, -6, 16, -17, 27, -28, 38, -39, 49, -50, 60])
# ----------


# ------------------------------------------------------
# > transaxial projection parameters (should be in
# > with the parameters as defined in def.h for C files)

# > parameters for each transaxial LOR
NTT = 10

# > all voxels intersected by a given LOR
NTV = 1807
# ------------------------------------------------------

# number of direct sinograms (i.e., for segment 0)
SEG0 = 127

# Reference image size (usually the default from Siemens)
# and GPU dimensions for optimal execution
# ~~~
SO_IMZ = 127
SO_IMY = 344
SO_IMX = 344
SO_VXX = 0.208626
SO_VXZ = 0.203125
SO_VXY = SO_VXX

SZ_IMZ = 127
SZ_IMY = 320
SZ_IMX = 320
SZ_VOXY = 0.208626
SZ_VOXZ = 0.203125
# ~~~
# SO_IMZ = 127
# SO_IMY = 384
# SO_IMX = 384
# SO_VXX = 0.1669
# SO_VXZ = 0.203125
# SO_VXY = SO_VXX

# SZ_IMZ = 127
# SZ_IMY = 384
# SZ_IMX = 384
# SZ_VOXY = 0.1669
# SZ_VOXZ = 0.203125
# ~~~
SIGMA_RM = 0

# > radius PSF kernel size used in CUDA convolution
RSZ_PSF_KRNL = 8

# ~~~
# inverse size
SZ_VOXZi = round(1 / SZ_VOXZ, 6)
# squared radius of the transaxial field of view
TFOV2 = 890.0

# -------Scatter image size in x,y,z directions
# target scale factors for scatter mu-map and emission image respectively
# transmission (mu-map)
TRGTSCT = [0.5, 0.33]
SS_IMX = int(ceil(TRGTSCT[0] * SO_IMX) // 2 * 2)
SS_IMY = int(ceil(TRGTSCT[0] * SO_IMY) // 2 * 2)
SS_IMZ = int(ceil(TRGTSCT[0] * SO_IMZ) // 2 * 2 - 1)
SS_VXY = round((SO_VXY * SO_IMX) / SS_IMX, 6)
SS_VXZ = round((SO_VXZ * SO_IMZ) / SS_IMZ, 6)
IS_VXZ = round(1 / SS_VXZ, 6)
# scaling [z,y,x]
SCTSCLMU = [float(SS_IMZ) / SO_IMZ, float(SS_IMY) / SO_IMY, float(SS_IMX) / SO_IMX]
# emission
SSE_IMX = int(ceil(TRGTSCT[1] * SO_IMX) // 2 * 2)
SSE_IMY = int(ceil(TRGTSCT[1] * SO_IMY) // 2 * 2)
SSE_IMZ = int(ceil(TRGTSCT[1] * SO_IMZ) // 2 * 2 + 1)
SSE_VXY = round((SO_VXY * SO_IMX) / SSE_IMX, 6)
SSE_VXZ = round((SO_VXZ * SO_IMZ) / SSE_IMZ, 6)
# scaling [z,y,x]
SCTSCLEM = [float(SSE_IMZ) / SO_IMZ, float(SSE_IMY) / SO_IMY, float(SSE_IMX) / SO_IMX]


# # scaling for the emission image [z,y,x]
# SCTSCLEM = [0.34, 0.33, 0.33]
# # scaling for the mu-map
# SCTSCLMU = [0.499, 0.5, 0.5]

# SS_IMX = int(ceil(SCTSCLMU[2]*SO_IMX)//2*2)#172
# SS_IMY = int(ceil(SCTSCLMU[1]*SO_IMY)//2*2)#172
# SS_IMZ = int(ceil(SCTSCLMU[0]*SO_IMZ)//2*2-1)#63
# SS_VXY = round((SO_VXY*SO_IMX)/SS_IMX,6) # 0.417252 #
# SS_VXZ = round((SO_VXZ*SO_IMZ)/SS_IMZ,6) # 0.409474 #
# IS_VXZ = round(1/SS_VXZ,6)

# SSE_IMX = int(ceil(SCTSCLEM[2]*SO_IMX)//2*2) #114
# SSE_IMY = int(ceil(SCTSCLEM[1]*SO_IMY)//2*2) #114
# SSE_IMZ = int(ceil(SCTSCLEM[0]*SO_IMZ)//2*2-1) #43

# SSE_VXY = round((SO_VXY*SO_IMX)/SSE_IMX,6) #0.629538
# SSE_VXZ = round((SO_VXZ*SO_IMZ)/SSE_IMZ,6) #0.599927
# -------

# > decay correction
DCYCRR = True

# --- Time of Flight ---
# speed of light
CLGHT = 29979245800  # cm/s
# coincidence time window [ps]
CWND = 5859.38e-12

# number of TOF bins
TOFBINN = 1
# size of TOF bin in [ps]
TOFBINS = 390e-12
# size of TOF BIN in cm of travelled distance
TOFBIND = TOFBINS * CLGHT
# inverse of the above
ITOFBIND = 1 / TOFBIND


# ring radius
R = 32.8
# effective ring radius accounting for the depth of interaction
RE = R + 0.67  # 0.67

RE_2 = float("{0:.6f}".format(RE ** 2))

# > inverse of the radius
IRE = float("{0:.6f}".format(RE ** -1))

# axial crystal width
AXR = 0.40625

# crystal angle
ALPHA = 0.714286 * pi / 180  # 2*pi/NCRS

# crystal gap period
TGAP = 9

# crystal gap offset (used for getting the sino gaps right at the position)
OFFGAP = 1

# --- FOR SCATTER ---
# electron radius **2
R02 = 7.940787449825884e-26
# detection lower energy threashold
LLD = 430000
E511 = 511008
# energy resolution
ER = 0  # 0.154
# discretisation of the scatter angle spectrum
NCOS = 256
# cosine of maximum allowed scatter angle
COSUPSMX = 0.725  # 0.58 #0.722 #Elow = E511/(2-cos(upsmx))
# step of the discreatisation
COSSTP = (1 - COSUPSMX) / (NCOS - 1)
# inverse of the step
ICOSSTP = 1 / COSSTP

# intensity percentage threshold of voxels to be considered in the image
ETHRLD = 0.05


# =================================================================================================
def get_gpu_constants(Cnt=None):
    """Return a dictionary of GPU related constants"""
    if Cnt is None:
        Cnt = {}

    for k in [
        "DEV_ID",  # device id; used for choosing the GPU device for calculations
        "CC_ARCH",  # chosen device architectures for NVCC compilation
    ]:
        val = globals().get(k)
        if val is not None:
            Cnt[k.replace("_", "")] = val

    return Cnt


# =================================================================================================
def get_setup(Cnt=None):
    """Return a dictionary of GPU, mu-map hardware and third party set-up."""
    if Cnt is None:
        Cnt = {}

    # the name of the folder for NiftyPET tools
    Cnt["DIRTOOLS"] = DIRTOOLS

    # additional paramteres for compiling tools with cmake
    Cnt["CMAKE_TLS_PAR"] = CMAKE_TLS_PAR

    # hardware mu-maps
    Cnt["HMULIST"] = hrdwr_mu

    # Microsoft Visual Studio Compiler version
    Cnt["MSVC_VRSN"] = MSVC_VRSN

    # GPU related setup
    Cnt = get_gpu_constants(Cnt)

    for k in [
        "PATHTOOLS",
        "RESPATH",  # image processing setup
        "REGPATH",
        "DCM2NIIX",
        "HMUDIR",  # hardware mu-maps
        "VINCIPATH",
        "REFPATH",  # > testing
    ]:
        val = globals().get(k)
        if val is not None:
            Cnt[k] = val

    Cnt["ENBLXNAT"] = ENBLXNAT
    Cnt["ENBLAGG"] = ENBLAGG
    Cnt["CMPL_DCM2NIIX"] = CMPL_DCM2NIIX

    return Cnt


# =================================================================================================
def get_mmr_constants():
    """
    Put all the constants together in a dictionary
    """

    Cnt = {
        "LOG": LOG,
        "VERBOSE": False,
        "BPE": BPE,
        "LMOFF": LMOFF,
        "ISOTOPE": "F18",
        "DCYCRR": DCYCRR,
        "ALPHA": ALPHA,
        "NRNG": NRNG,
        "NCRS": NCRS,
        "NCRSR": NCRSR,
        "SRFCRS": SRFCRS,
        "NBCKT": 224,
        "NSANGLES": A,
        "NSBINS": W,
        "Naw": -1,  # number of total active bins per 2D sino
        "NSN11": NSN11,  # number of sinos in span-11
        "NSN1": NSN1,  # number of sinos in span-1
        "NSN64": NSN64,  # number of sinos in span-1 with no MRD limit
        "MRD": MRD,  # maximum ring difference RD
        "SPN": SPAN,  # span-1 (1), span-11 (11), ssrb (0)
        "TFOV2": TFOV2,  # squared radius of TFOV
        "RNG_STRT": RNG_STRT,  # limit axial extension by defining start and end ring
        "RNG_END": RNG_END,  # only works with span-1 (Cnt['SPN']==1)
        "SS_IMZ": SS_IMZ,  # Scatter mu-map image size
        "SS_IMY": SS_IMY,
        "SS_IMX": SS_IMX,
        "SS_VXZ": SS_VXZ,
        "SS_VXY": SS_VXY,
        "IS_VXZ": IS_VXZ,
        "SSE_IMZ": SSE_IMZ,  # Scatter emission image size
        "SSE_IMY": SSE_IMY,
        "SSE_IMX": SSE_IMX,
        "SSE_VXZ": SSE_VXZ,
        "SSE_VXY": SSE_VXY,
        "SZ_IMZ": SZ_IMZ,  # GPU optimised image size
        "SZ_IMY": SZ_IMY,
        "SZ_IMX": SZ_IMX,
        "SZ_VOXZ": SZ_VOXZ,
        "SZ_VOXY": SZ_VOXY,
        "SZ_VOXZi": SZ_VOXZi,
        "SO_IMZ": SO_IMZ,  # Original image size (from Siemens)
        "SO_IMY": SO_IMY,
        "SO_IMX": SO_IMX,
        "SO_VXZ": SO_VXZ,
        "SO_VXY": SO_VXY,
        "SO_VXX": SO_VXX,
        "SIGMA_RM": SIGMA_RM,  # resolution modelling sigma
        "RSZ_PSF_KRNL": RSZ_PSF_KRNL,  # radius PSF kernel size used in CUDA convolution
        "NTT": NTT,
        "NTV": NTV,
        "NSEG0": SEG0,
        "R_RING": RE,  # effective ring radius
        "R_2": RE_2,
        "IR_RING": IRE,
        "R": R,
        "SEG": seg,
        "MNRD": minrd,
        "MXRD": maxrd,
        # > scatter moved to scatter LUTs script in sct folder
        # 'NSRNG':NSRNG, # number of scatter rings for modelling
        # 'SCTRNG':sct_irng, # scatter ring indexes
        "TGAP": TGAP,
        "OFFGAP": OFFGAP,
        "AXR": AXR,
        "R02": R02,  # squared electron radius
        "LLD": LLD,  # lower energy threashold
        "E511": E511,
        "ER": ER,  # energy resolution
        # > scatter:
        "SIRNG": sct_irng,  # scatter ring indices
        "NSRNG": NSRNG,  # number of rings for scatter modelling
        "COSUPSMX": COSUPSMX,  # cosine of max allowed scatter angle
        "NCOS": NCOS,  # number of cos samples for LUT
        "COSSTP": COSSTP,  # cosine step
        "ICOSSTP": ICOSSTP,  # inverse of cosine step
        "ETHRLD": ETHRLD,  # intensity emission image threshold (for scatter modelling)
        "CLGHT": CLGHT,  # speed of light [cm/s]
        "CWND": CWND,  # coincidence time window [ps]
        "TOFBINN": TOFBINN,  # number of TOF bins
        "TOFBINS": TOFBINS,  # TOF bin width [ps]
        "TOFBIND": TOFBIND,
        "ITOFBIND": ITOFBIND,
        # affine and image size for the reconstructed image,
        # assuming the centre of voxels in mm
        "AFFINE": array(
            [
                [-10 * SO_VXX, 0.0, 0.0, 5.0 * SO_IMX * SO_VXX],  # +5.*SO_VXX
                [0.0, 10 * SO_VXY, 0.0, -5.0 * SO_IMY * SO_VXY],  # +5.*SO_VXY
                [0.0, 0.0, 10 * SO_VXZ, -5.0 * SO_IMZ * SO_VXZ],  # -5.*SO_VXZ
                [0.0, 0.0, 0.0, 1.0],
            ]
        ),
        "IMSIZE": array([SO_IMZ, SO_IMY, SO_IMX]),
        "BTP": 0,  # 1:non parametric bootstrap, 2: parametric bootstrap (recommended)
        "BTPRT": 1.0,  # Ratio of bootstrapped/original events (enables downsampling)
        "SCTSCLEM": SCTSCLEM,
        "SCTSCLMU": SCTSCLMU,
    }

    # get the setup for GPU and third party apps
    Cnt = get_setup(Cnt=Cnt)

    return Cnt

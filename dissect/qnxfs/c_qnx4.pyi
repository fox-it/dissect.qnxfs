# Generated by cstruct-stubgen
from typing import BinaryIO, Literal, overload

import dissect.cstruct as __cs__
from typing_extensions import TypeAlias

class _c_qnx4(__cs__.cstruct):
    QNX4_ROOT_INO: Literal[1] = ...
    QNX4_MAX_XTNTS_PER_XBLK: Literal[60] = ...
    QNX4_FILE_USED: Literal[1] = ...
    QNX4_FILE_MODIFIED: Literal[2] = ...
    QNX4_FILE_BUSY: Literal[4] = ...
    QNX4_FILE_LINK: Literal[8] = ...
    QNX4_FILE_INODE: Literal[16] = ...
    QNX4_FILE_FSYSCLEAN: Literal[32] = ...
    QNX4_I_MAP_SLOTS: Literal[8] = ...
    QNX4_Z_MAP_SLOTS: Literal[64] = ...
    QNX4_VALID_FS: Literal[1] = ...
    QNX4_ERROR_FS: Literal[2] = ...
    QNX4_BLOCK_SIZE: Literal[512] = ...
    QNX4_BLOCK_SIZE_BITS: Literal[9] = ...
    QNX4_DIR_ENTRY_SIZE: Literal[64] = ...
    QNX4_DIR_ENTRY_SIZE_BITS: Literal[6] = ...
    QNX4_XBLK_ENTRY_SIZE: Literal[512] = ...
    QNX4_INODES_PER_BLOCK: Literal[8] = ...
    QNX4_SHORT_NAME_MAX: Literal[16] = ...
    QNX4_LONG_NAME_MAX: Literal[505] = ...
    QNX4_NAME_MAX: Literal[48] = ...
    __le16: TypeAlias = _c_qnx4.uint16
    __le32: TypeAlias = _c_qnx4.uint32
    qnx4_nxtnt_t: TypeAlias = _c_qnx4.uint16
    qnx4_ftype_t: TypeAlias = _c_qnx4.uint8
    class qnx4_xtnt_t(__cs__.Structure):
        xtnt_blk: _c_qnx4.uint32
        xtnt_size: _c_qnx4.uint32
        @overload
        def __init__(self, xtnt_blk: _c_qnx4.uint32 | None = ..., xtnt_size: _c_qnx4.uint32 | None = ...): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

    qnx4_mode_t: TypeAlias = _c_qnx4.uint16
    qnx4_muid_t: TypeAlias = _c_qnx4.uint16
    qnx4_mgid_t: TypeAlias = _c_qnx4.uint16
    qnx4_off_t: TypeAlias = _c_qnx4.uint32
    qnx4_nlink_t: TypeAlias = _c_qnx4.uint16
    class qnx4_inode_entry(__cs__.Structure):
        di_fname: __cs__.CharArray
        di_size: _c_qnx4.uint32
        di_first_xtnt: _c_qnx4.qnx4_xtnt_t
        di_xblk: _c_qnx4.uint32
        di_ftime: _c_qnx4.uint32
        di_mtime: _c_qnx4.uint32
        di_atime: _c_qnx4.uint32
        di_ctime: _c_qnx4.uint32
        di_num_xtnts: _c_qnx4.uint16
        di_mode: _c_qnx4.uint16
        di_uid: _c_qnx4.uint16
        di_gid: _c_qnx4.uint16
        di_nlink: _c_qnx4.uint16
        di_zero: __cs__.Array[_c_qnx4.uint8]
        di_type: _c_qnx4.uint8
        di_status: _c_qnx4.uint8
        @overload
        def __init__(
            self,
            di_fname: __cs__.CharArray | None = ...,
            di_size: _c_qnx4.uint32 | None = ...,
            di_first_xtnt: _c_qnx4.qnx4_xtnt_t | None = ...,
            di_xblk: _c_qnx4.uint32 | None = ...,
            di_ftime: _c_qnx4.uint32 | None = ...,
            di_mtime: _c_qnx4.uint32 | None = ...,
            di_atime: _c_qnx4.uint32 | None = ...,
            di_ctime: _c_qnx4.uint32 | None = ...,
            di_num_xtnts: _c_qnx4.uint16 | None = ...,
            di_mode: _c_qnx4.uint16 | None = ...,
            di_uid: _c_qnx4.uint16 | None = ...,
            di_gid: _c_qnx4.uint16 | None = ...,
            di_nlink: _c_qnx4.uint16 | None = ...,
            di_zero: __cs__.Array[_c_qnx4.uint8] | None = ...,
            di_type: _c_qnx4.uint8 | None = ...,
            di_status: _c_qnx4.uint8 | None = ...,
        ): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

    class qnx4_link_info(__cs__.Structure):
        dl_fname: __cs__.CharArray
        dl_inode_blk: _c_qnx4.uint32
        dl_inode_ndx: _c_qnx4.uint8
        dl_lfn_blk: _c_qnx4.uint32
        dl_spare: __cs__.Array[_c_qnx4.uint8]
        dl_status: _c_qnx4.uint8
        @overload
        def __init__(
            self,
            dl_fname: __cs__.CharArray | None = ...,
            dl_inode_blk: _c_qnx4.uint32 | None = ...,
            dl_inode_ndx: _c_qnx4.uint8 | None = ...,
            dl_lfn_blk: _c_qnx4.uint32 | None = ...,
            dl_spare: __cs__.Array[_c_qnx4.uint8] | None = ...,
            dl_status: _c_qnx4.uint8 | None = ...,
        ): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

    class qnx4_longfilename_entry(__cs__.Structure):
        lfn_unk0: _c_qnx4.uint32
        lfn_unk1: _c_qnx4.uint8
        lfn_unk2: _c_qnx4.uint8
        lfn_name: __cs__.CharArray
        @overload
        def __init__(
            self,
            lfn_unk0: _c_qnx4.uint32 | None = ...,
            lfn_unk1: _c_qnx4.uint8 | None = ...,
            lfn_unk2: _c_qnx4.uint8 | None = ...,
            lfn_name: __cs__.CharArray | None = ...,
        ): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

    class qnx4_xblk(__cs__.Structure):
        xblk_next_xblk: _c_qnx4.uint32
        xblk_prev_xblk: _c_qnx4.uint32
        xblk_num_xtnts: _c_qnx4.uint8
        xblk_spare: __cs__.Array[_c_qnx4.uint8]
        xblk_num_blocks: _c_qnx4.uint32
        class qnx4_xtnt_t(__cs__.Structure):
            xtnt_blk: _c_qnx4.uint32
            xtnt_size: _c_qnx4.uint32
            @overload
            def __init__(self, xtnt_blk: _c_qnx4.uint32 | None = ..., xtnt_size: _c_qnx4.uint32 | None = ...): ...
            @overload
            def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

        xblk_xtnts: __cs__.Array[qnx4_xtnt_t]
        xblk_signature: __cs__.CharArray
        xblk_first_xtnt: _c_qnx4.qnx4_xtnt_t
        @overload
        def __init__(
            self,
            xblk_next_xblk: _c_qnx4.uint32 | None = ...,
            xblk_prev_xblk: _c_qnx4.uint32 | None = ...,
            xblk_num_xtnts: _c_qnx4.uint8 | None = ...,
            xblk_spare: __cs__.Array[_c_qnx4.uint8] | None = ...,
            xblk_num_blocks: _c_qnx4.uint32 | None = ...,
            xblk_xtnts: __cs__.Array[qnx4_xtnt_t] | None = ...,
            xblk_signature: __cs__.CharArray | None = ...,
            xblk_first_xtnt: _c_qnx4.qnx4_xtnt_t | None = ...,
        ): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

    class qnx4_super_block(__cs__.Structure):
        RootDir: _c_qnx4.qnx4_inode_entry
        Inode: _c_qnx4.qnx4_inode_entry
        Boot: _c_qnx4.qnx4_inode_entry
        AltBoot: _c_qnx4.qnx4_inode_entry
        @overload
        def __init__(
            self,
            RootDir: _c_qnx4.qnx4_inode_entry | None = ...,
            Inode: _c_qnx4.qnx4_inode_entry | None = ...,
            Boot: _c_qnx4.qnx4_inode_entry | None = ...,
            AltBoot: _c_qnx4.qnx4_inode_entry | None = ...,
        ): ...
        @overload
        def __init__(self, fh: bytes | memoryview | bytearray | BinaryIO, /): ...

# Technically `c_qnx4` is an instance of `_c_qnx4`, but then we can't use it in type hints
c_qnx4: TypeAlias = _c_qnx4

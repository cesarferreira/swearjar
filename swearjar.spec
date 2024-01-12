import os
import sys

# Get the directory where the .spec file and resources are located
spec_dir = os.path.dirname(sys.argv[0])
resources_path = os.path.join(spec_dir, 'resources')

a = Analysis(
    ['swearjar.py'],
    pathex=[],
    binaries=[],
    datas=[(resources_path, 'resources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='swearjar',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

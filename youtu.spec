# -*- mode: python ; coding: utf-8 -*-

# Add Django static/template files
a = Analysis(
    ['youtu.py'],
    pathex=[r'C:\Users\LENOVO\youtu'],
    binaries=[],
    datas=[
        
        ('tube/templates/*', 'templates'),
    ],
    hiddenimports=[
        'django',
        'tube',  # Add all your Django apps here
    ],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='youtu',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

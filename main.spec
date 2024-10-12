# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('flower_template_1.png', '.'), ('flower_template_2.png', '.'), ('flower_template_3.png', '.'), ('flower_template_4.png', '.'), ('flower_template_5.png', '.'), ('flower_template_6.png', '.'), ('ice_template_1.png', '.'), ('ice_template_2.png', '.'), ('ice_template_3.png', '.'), ('bomb_template_1.png', '.'), ('bomb_template_2.png', '.'), ('bomb_template_3.png', '.'), ('play_button_template.png', '.'), ('home.png', '.'), ('play_home.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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

# -*- mode: python ; coding: utf-8 -*-
import shutil
import os

block_cipher = None

a = Analysis(
    ['src\\artisan.py'],
    pathex=['src'],
    binaries=[],
    datas=[], # ここは空のまま
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Artisan_ARARE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\mastphoto\\artisan.ico'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Artisan_ARARE',
)

# ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
# ここから下：PyInstallerの処理が終わった後に、手動でフォルダをコピーする処理
# ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

print("\n--- Manual Copy: Starting translations copy ---")

# コピー元のフォルダ（あなたのパス）
src_dir = r"C:\Artisan Revolution\ArtisanDev\artisan\src\translations"

# コピー先のフォルダ（dist/Artisan_ARARE/translations）
# DISTPATH は PyInstaller が自動で設定する変数です
dest_dir = os.path.join(DISTPATH, 'Artisan_ARARE', 'translations')

# もし既に古いフォルダがあったら消す（掃除）
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)

# フォルダごとコピーする
try:
    shutil.copytree(src_dir, dest_dir)
    print(f"--- Manual Copy: Success! Copied to {dest_dir} ---")
except Exception as e:
    print(f"--- Manual Copy: Failed! Error: {e} ---")
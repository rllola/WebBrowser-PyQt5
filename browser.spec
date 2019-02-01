# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files
from sys import platform

block_cipher = None

datas = Tree('icons', prefix='icons', excludes=[])

a = Analysis(['main.py'],
             binaries=[],
             datas=[],
             hiddenimports=['enum'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

icon = None
if platform.startswith("darwin"):
    icon = 'icons/zeronet-logo.icns'

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='WebBrowser',
          icon=icon,
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               datas,
               strip=False,
               upx=False,
               name='WebBrowser')


app = BUNDLE(coll,
             name='WebBrowser.app',
             icon=icon,
             bundle_identifier=None)

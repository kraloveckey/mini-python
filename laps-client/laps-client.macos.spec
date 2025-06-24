# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

# find the SHA-1 hash of you Developer ID Application certificate
# for signing via `security find-identity -v -p codesigning` or use `None`
codesign_identity = '4B7092469383AAFE294DA4B2B0CCB1BB0050DF72'


gui_a = Analysis(['laps-gui.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
cli_a = Analysis(['laps-cli.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
MERGE( (gui_a, 'laps-gui', 'laps-gui'), (cli_a, 'laps-cli', 'laps-cli') )

gui_pyz = PYZ(gui_a.pure, gui_a.zipped_data, cipher=block_cipher)
gui_exe = EXE(gui_pyz, gui_a.scripts, [],
          exclude_binaries=True,
          name='laps-gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=codesign_identity,
          entitlements_file=None )

cli_pyz = PYZ(cli_a.pure, cli_a.zipped_data, cipher=block_cipher)
cli_exe = EXE(cli_pyz, cli_a.scripts, [],
          exclude_binaries=True,
          name='laps-cli',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=codesign_identity,
          entitlements_file=None )

coll = COLLECT(gui_exe, gui_a.binaries, gui_a.zipfiles, gui_a.datas,
               cli_exe, cli_a.binaries, cli_a.zipfiles, cli_a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='laps-client')

app = BUNDLE(coll,
             name='laps-client.app',
             icon='assets/laps.icns',
             bundle_identifier='systems.sieber.laps4mac',
             version='1.7.2',
             info_plist={
               'CFBundleURLTypes': [
                  {
                    'CFBundleURLName': 'Local Administrator Password Solution',
                    'CFBundleURLSchemes': ['laps']
                  }
                ]
              })

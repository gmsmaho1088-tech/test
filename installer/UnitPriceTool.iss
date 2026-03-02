; Inno Setup script for Windows installer
; 使い方:
; 1. 先に PyInstaller で dist/UnitPriceTool/UnitPriceTool.exe を作成
; 2. Inno Setup でこの .iss を開いてビルド

#define MyAppName "UnitPriceTool"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Local"
#define MyAppExeName "UnitPriceTool.exe"

[Setup]
AppId={{C0DC58E6-22DB-4B33-A88F-9A13E1839B9E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputDir=..\dist\installer
OutputBaseFilename=UnitPriceToolInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Tasks]
Name: "desktopicon"; Description: "デスクトップにアイコンを作成する"; GroupDescription: "追加タスク:"; Flags: checkedonce

[Files]
Source: "..\dist\UnitPriceTool\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

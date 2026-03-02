# Windows11向け: EXE作成スクリプト
# 実行方法: PowerShellで `./build_windows.ps1`

python -m pip install --upgrade pip
python -m pip install pyinstaller

pyinstaller `
  --noconfirm `
  --windowed `
  --name UnitPriceTool `
  app/unit_price_tool.py

Write-Host "Build completed: dist/UnitPriceTool/UnitPriceTool.exe"

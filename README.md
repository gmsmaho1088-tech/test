# UnitPriceTool (Windows 11 Desktop App)

Windows 11で動作する単価計算ツールです。インストーラーを使うと、デスクトップにアイコンを作成できます。

## 機能
- 入力欄 × 60円
- 入力欄 × 66.6円
- 入力欄 × 80円
- 入力欄 × 100円
- 入力欄 × 120円
- 各行の計算結果と合計を自動表示

## 実際にダウンロードして使う手順（利用者向け）
1. 配布された `UnitPriceToolInstaller.exe` をダウンロード
2. ダウンロードしたファイルをダブルクリック
3. インストーラーで「デスクトップにアイコンを作成する」にチェックを入れてインストール
4. デスクトップに作成された `UnitPriceTool` アイコンをダブルクリックして起動
5. 数量を入力すると、各行と合計が自動計算されます

### 起動時に警告が出る場合
- Windows SmartScreen が表示されたら、`詳細情報` → `実行` を選ぶと起動できます。
- 社内PCなどで実行制限がある場合は、管理者へ許可申請してください。


## テスター向け（ダウンロードして動作確認したい場合）
詳しい手順は `TESTING.md` を参照してください。
- 推奨: `UnitPriceToolInstaller.exe` を受け取り、インストール後にデスクトップアイコンから起動
- 検証用の入力例と期待結果（合計 `1,492.20円`）も記載

## 配布ファイルを作る手順（開発者向け）

### 1) ローカル実行（動作確認）
```bash
python app/unit_price_tool.py
```

### 2) Windows EXE の作成
PowerShellで以下を実行:
```powershell
./build_windows.ps1
```
生成物:
- `dist/UnitPriceTool/UnitPriceTool.exe`

### 3) インストーラー作成（デスクトップアイコン付き）
1. [Inno Setup](https://jrsoftware.org/isinfo.php) をインストール
2. `installer/UnitPriceTool.iss` を開いてビルド
3. `dist/installer/UnitPriceToolInstaller.exe` が生成されるので、それを配布

インストール時に「デスクトップにアイコンを作成する」が選択され、
インストール後にデスクトップアイコンから起動できます。

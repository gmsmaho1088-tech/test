# ダウンロードしてテストする手順（Windows 11）

このファイルは「利用者（テスター）」向けです。

## A. いちばん簡単な方法（推奨）
配布者から `dist/installer/UnitPriceToolInstaller.exe`（ファイル名は `UnitPriceToolInstaller.exe`）を受け取り、以下を実施してください。

1. `UnitPriceToolInstaller.exe` をダウンロード
2. ファイルを右クリックして「プロパティ」を開き、`ブロックの解除` があればチェックして OK
3. インストーラーをダブルクリックして起動
4. 「デスクトップにアイコンを作成する」にチェックしたままインストール
5. デスクトップの `UnitPriceTool` アイコンをダブルクリックして起動
6. 以下を入力して計算結果を確認
   - 1 × 60円
   - 2 × 66.6円
   - 3 × 80円
   - 4 × 100円
   - 5 × 120円

期待値:
- 各行が自動計算される
- 合計が `1,492.20円` と表示される

## B. 配布者がまだインストーラーを作っていない場合
配布者に以下を依頼してください。

- `build_windows.ps1` を実行して EXE を生成
- `installer/UnitPriceTool.iss` を Inno Setup でビルドして `dist/installer/UnitPriceToolInstaller.exe` を生成
- 生成された `UnitPriceToolInstaller.exe` を共有

## C. よくある詰まりポイント
- SmartScreen 警告が出る: `詳細情報` → `実行` を選択
- 社内PCで実行できない: 管理者に実行許可を申請
- デスクトップアイコンがない: インストーラーを再実行し「デスクトップにアイコンを作成する」を有効化

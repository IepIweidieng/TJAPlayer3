■TJAPlayer2(仮)
PSPでtjaファイルを再生するアプリです

画像、音声は太鼓さん太郎、太鼓さん次郎、TJAPlayerから拝借しています
太鼓さん太郎 : http://www.mediafire.com/?nce5ymmm2il
太鼓さん次郎 : http://www.nicovideo.jp/watch/sm5463901
TJAPlayer    : http://www.geocities.jp/okiater/


■使用方法
CFW導入済みのPSPのGAMEフォルダにTJAPlayer2フォルダを追加して下さい


■操作方法（暫定）
選曲画面
  ↑↓   : 曲の選択
  ←→   : 難易度の選択
  ○     : 譜面の読み込み

演奏待機画面
  ×     : 選曲に戻る
  START  : 演奏開始

演奏画面
  SELECT : 演奏待機に戻る


■対応フォーマット
譜面 : tja
画像 : png
音声 : mp3


■譜面について
詳細は太鼓さん次郎のreadmeをご覧下さい
  ●未対応の命令があります
      以下の命令、音符には未対応です
      STYLE
      GAME
      SIDE
      SIDEREV
      LIFE
      DEMOSTART
      SONGVOL
      SEVOL
      SCOREMODE
      #START P1
      #START P2
      イモ音符
  
  ●譜面分岐の開始タイミングが異なります
      太鼓さん次郎では次のような仕様になっています
      >分岐判定は命令の一小節前に行われます（一小節前から連打が始まる場合、その連打もカウントします）
      このソフトでは括弧内の仕様を含まず、命令の一小節前に分岐判定を行います
  
  ●譜面がずれることがあります
      正しく譜面が読み込めず、ずれることがあるかもしれません
      また、BPMCHANGEが大量にある譜面は、太鼓さん次郎にて合わせた場合ずれることがあります


■画像について
512×512px以下のpngにのみ対応しています
ファイル名、仕様、座標の設定は基本的に太鼓さん次郎に準じます


■音声について
サンプリングレート44,100kHzのmp3にのみ対応しています
現在oggを読み込むことが出来ません、また対応も未定です


■更新履歴
04/??       飽きた。


■使用ライブラリ
zlib
Copyright (c) 1995-2004 Jean-loup Gailly and Mark Adler.

libpng
Copyright (c) 2004 Glenn Randers-Pehrson
distributed according to the same disclaimer and license as libpng-1.4.4
with the following individual added to the list of Contributing Authors

jpeglib
this software is based in part on the work of the Independent JPEG Group.

intraFont
Uses intraFont by BenHur

liblzr
Uses liblzr by BenHur

DXライブラリPortable
DX Library Portable Copyright (C) 2008-2010 Kawai Yuichi.
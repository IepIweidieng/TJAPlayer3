TJAPlayer2(仮) 改造版 ver0.065

○概要
タイトルのままです。
製作者はC#しか触ったことがないので過度な期待はしないでください。

○改造点
・コンボシステム追加
・背景画像実装
・それっぽいスコアの表示。四捨五入とか無い上に、まだSCOREMODE:2しか対応できてませんorz
以下自分が追加してないやつ
・LRトリガでのページ移動の実装
・デモ再生

○課題
・スコアの実装
・ゲージの実装
・色々な画像の実装
・リザルト画面実装
・曲選択画面の改良
・曲名画像対応
　・そもそも私自体仕様を理解できてません(汗)
・ドンカツ音のノイズ軽減
・フォルダ機能 
・ソート機能
・タイマー関連のクラスの構築(自分向け)



○現在見つかってるバグ
・TJAPlayer_End()が呼ばれるときPlayTJAThreadが終了していない
・効果音の同時再生数が少なすぎるためか、多く発声した場合に音が消える。
・強制終了する曲がある(原因不明)

○色々
・改造とか改良とか好きなだけやってください。
　・もともとそうされてほしいから、原作者様がソースの配布をされたのだと思ってますので。
・要望とかそこらへんはTJAPスレで投げてください。
　・私の未熟さ故に難しい機能は実装できないと思いますので悪しからず。

○仕様
・上背景画像はスクロールしません。
・下背景画像の座標移動はまた今度実装します。
・ログ出力を有効にしているため、多分重いかと。
・曲選択でSELECTを押すと操作タイプが2に切り替わります。

○SpecalThanks!
・toach氏 太鼓さん次郎原作、TJA形式譜面考案
・笑い男氏 TJAPlayer原作(多分名前はあっているかとは思いますが何分どこにも書いてないので・・・)
・650氏 TJAP2作成
・785(mafu)氏 DXライブラリPortable Kaiのogg対応

○更新履歴
2014/03/27	ver0.065 785氏の差分を適用。
2013/11/30	ver0.06　DXライブラリの更新。
2013/09/16	ver0.05　曲選択画面に簡易的な操作説明を書いた。
			 DXライブラリの更新。
			 wavファイルのノイズの対策が完了されたため、効果音をwavに戻した。
			 Config.iniから演奏中のデバッグ表示を消せるようにした。
			 スコアの10000点加算に対応したつもり。
2013/08/12	ver0.04　キー操作タイプ2の実装。
			 軽くスコアみたいなものの実装準備。
			 (スコアはSCOREMODE:2もどき。10000点ボーナスと四捨五入が未実装。)
			 急遽効果音をwav→mp3に戻した。
			 DXPの更新。
2013/05/15	ver0.03　DXライブラリPortableを785氏改造のものに差し替え。
			 これによりoggに対応。
			 太鼓音をwav形式のものに差し替え。
2013/04/27	ver0.02　最大コンボの実装。背景画像を表示できるようにしてみる。
2013/03/31	ver0.01　コンボシステム(仮)の実装


2014/03/27　原作:>>650氏　改造:kairera0467(IMARER◆dA2mWcqiao)
○使用ライブラリ
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

全角文字表示ライブラリ
このソフトウェアは mediumgauge 氏作成の全角文字表示ライブラリを使用しています。

libogg and libvorbisidec

Copyright (c) 2002, Xiph.org Foundation

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

- Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

- Neither the name of the Xiph.org Foundation nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

DXライブラリPortable
DX Library Portable Copyright (C) 2008-2010 Kawai Yuichi.
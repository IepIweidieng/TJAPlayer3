# TJA Format and on

This is an unofficial compilation and commentation of the TJA format & its related formats.

This article aims at providing a comprehensive enough overview & possible etymologies and addressing undocumented corner cases.

This article is still *in construction*:

* Information requiring verification is included and is marked with *(?)*.
* Missing, inaccurate, or even incorrect information is possible, especially about less known software behaviors, due to insufficient or misunderstood references. If it is the case, please do not hesitate to edit this article to fix it.
* The terminologies introduced in this article are not finalized and might be subject to changes.

This article also contains tentative proposals by the main maintainer ([@IepIweidieng](https://github.com/IepIweidieng)) of this article. These proposals are explicitly expressed to be *Proposal*s and are subject to changes.

See [Terminologies](#terminologies) for the explanation and conventions of some terminologies used in this article.

When there exist multiple equivalent usages accepted by the simulators, the conventional ones are represented in **bold**.

## Formats

Known notechart formats used in <ruby>**太**<rt>**T**ai</rt> 鼓<rt>ko</rt> の<rt>no</rt> **達**<rt>**T**atsu</rt> **人**<rt>**j**in</rt></ruby> games and simulators:

Extension | Full Name | Content | Supported by | Specification
--- | --- | --- | --- | ---
`.bin` | **Bin**ary (*<ruby>譜<rt>Fu</rt> 面<rt>men</rt></ruby>* Notechart File Format) | Notechart metadata + definition (binary file) | Official games, taiko-web (plugin "Fumen File Format") | Proprietary format, not explained in this article.
`.tjf` | **T**atsu**j**in *<ruby>**譜**<rt>**F**u</rt> 面<rt>men</rt></ruby>* Notechart Data (?) | Notechart metadata + definition | Taikosan, TaikoJiro 1 |
`.tja` | **T**atsu**j**in Notechart Format **A**(?) (?) | Notechart metadata + definition | TaikoJiro, TJAPlayer2 for PC, taiko-web ver.18.10.11, OutFox Alpha 4.9.9, TaikoManyGimmicks |
`.tjc` | **T**atsu**j**in **C**ourse (?) | Notechart set metadata | TaikoJiro v2.34, TaikoJiro 2 v0.98 |
`.osu` | **osu**! Beatmap | Notechart metadata + definition | osu!, taiko-web | See <https://osu.ppy.sh/wiki/en/Client/File_formats>
`.osz` | **os**u! Beatmap Archive ("**Z**ipped") | Notechart metadata + definition + resources (compressed binary file) | osu! | See <https://osu.ppy.sh/wiki/en/Client/File_formats>
`.tci` | Open **T**aiko **C**hart **I**nformation | Notechart metadata (JSON) | Koioto (plugin "OpenTaikoChart"), TJAPlayer3-f v1.6.0.1 | See <https://github.com/AioiLight/Open-Taiko-Chart>
`.tcc` | Open **T**aiko **C**hart **C**ourse | Notechart definition (JSON) | Koioto (plugin "OpenTaikoChart"), TJAPlayer3-f v1.6.0.1 | See <https://github.com/AioiLight/Open-Taiko-Chart>
`.tcm` | Open **T**aiko **C**hart **M**edley | Notechart set metadata (JSON) | TJAPlayer3-f v1.6.0.1 | See <https://github.com/AioiLight/Open-Taiko-Chart>
`.tmg` | **T**aiko**M**any**G**immicks | Notechart metadata + definition | TaikoManyGimmicks | Similar to `.tja` but has some syntax differences (explained right below).

The TMG format (`.tmg`) is similar to the TJA format (`.tja`) and has the following features:

* In TaikoManyGimmicks, the TMG and TJA formats share the same set of [headers](#tja-header) & [commands](#tja-command).
* Command arguments in the TMG format are comma-separated and requires parentheses `()` around the whole argument list, even if no arguments are specified. TMG commands are written in the format of **`#COMMAND(expressions, ...)`**.
* Math expressions and functions are allowed for each [`number`-typed and `complex-ri-number`&ndash;typed](#value-type) argument for commands.
* Substitution of predefined variables are allowed in each argument of headers & commands and in notechart definitions. For [`str`-typed](#value-type) argument, `#` (preserved after substitution) needed to be prepended for applying substitution (?).

Excluding `.bin` & `.osz`, all the formats listed above are text-based and can be edited with any text editor.

## About TJA

The TJA format (`.tja`, first used in TaikoJiro) was modified and extended from the much simpler TJF format (`.tjf`, first used in Taikosan), both share similarities with the `.bms` (**B**e-**M**usic **S**cript, not **B**eat**M**ania **S**core) format.

The etymology of both `.tjf` & `.tja` were unexplained.

* `tj` originally did ***NOT*** refer to *<ruby>**太**<rt>**T**ai</rt> 鼓<rt>ko</rt> さ<rt>sa</rt> ん<rt>n</rt> **次**<rt>**J**i</rt> 郎<rt>rou</rt></ruby>* **T**aiko**J**iro since it has already appeared in `.tjf`, which is already used in *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> さ<rt>sa</rt> ん<rt>n</rt> 太<rt>Ta</rt> 郎<rt>rou</rt></ruby>* Taikosan.
* `tj` could refer to (*<ruby>**太**<rt>**T**ai</rt> 鼓<rt>ko</rt> の<rt>no</rt></ruby>*) *<ruby>**達**<rt>**T**atsu</rt> **人**<rt>**j**in</rt></ruby>*, the official game series. `.ttf` might be one of the intended file extension but was not usable because it had already been used for TrueType font files.
* `f` in `.tjf` probably means *<ruby>**譜**<rt>**f**u</rt> 面<rt>men</rt> デー<rt>dee</rt> タ<rt>ta</rt></ruby>* notechart data, according to the notechart file selection dialog of Taikosan. \
  ![Taikosan's File Selection Dialog](https://i.imgur.com/qMYHS6j.png)
* `a` could just be the alphabet numbering, could instead mean "**a**dvanced" (refers to *<ruby>**次**<rt>**J**i</rt></ruby>* "next"), "**a**dd" (refers to *<ruby>＋<rt>**a**dd</rt></ruby>* "plus"), *etc.*, or could even instead mean *<ruby>譜<rt>fu</rt> 面<rt>men</rt> デー<rt>dee</rt> **タ**<rt>t**a**</rt></ruby>* notechart dat**a** as the `f` in `.tjf`.

Thus, `.tja` possibly means *(<ruby>**太**<rt>**T**ai</rt> 鼓<rt>ko</rt> の<rt>no</rt></ruby>) <ruby>**達**<rt>**T**atsu</rt> **人**<rt>**j**in</rt></ruby> (simulator) <ruby>譜<rt>fu</rt> 面<rt>men</rt> デー<rt>dee</rt> **タ**<rt>t**a**</rt></ruby>* "(Taiko no) **T**atsu**j**in (Simulator) Notechart Format A".

## TJA File Encoding

The mostly used character encoding for legacy TJA files is **Shift-JIS**.

However, the actual encoding depended on the system setting and can potentially be any non&ndash;UTF-8 encoding, including:

* Big5 (with or without extensions) for some legacy charts created by Traditional Chinese users
  * Most used extensions include Big5-UAO & Big5-HKSCS.
* GB 2312 (with or without extensions) for some legacy charts created by Simplified Chinese users
  * Most used extensions include GBK & GB 18030.

**UTF-8** (**with BOM** or not) is often used for modern TJA files.

#### Compatibility Issues

* Native encoding: TaikoJiro, TJAPlayer2 for PC, TJAPlayer3 before v1.5.2
* Shift-JIS: TJAPlayer3 v1.5.2+, taiko-web
* UTF-8 with BOM: TJAPlayer3, taiko-web
* Plain UTF-8: taiko-web

## TJA Lexical Rules

### Newlines

Lines are *separated* (may be unterminated) by either LF (`\n`) or CR+LF (`\r\n`) (see [Terminologies](#terminologies) for further explanation).

Lines containing only whitespaces or nothing at all are ignored.

### Comment & Whitespaces

Except when preceded by a `text` value, `//` starts a comment which ends at the end of the line and is ignored along with the `//`.

* Comments were never allowed in the original TJF format.

Except when preceded by a `text` value, line-final whitespaces (after ignoring comments) are ignored.

* *Unspecified*: Whether line-final whitespaces or optional whitespaces + comment after a `text` value is ignored.
  * In TaikoJiro, their are not ignored and are kept as-is in such a case

Line-initial whitespaces are allowed and ignored only within the notechart definition enclosed between `#START` & `#END` (excluding themselves).

* Line-initial whitespaces before headers & commands were never allowed in the original TJF format.

Consecutive whitespaces within a line is treated as a single space.

* Non-newline whitespaces in non-command lines within the notechart definition were not ignored in the original TJF format but ignored by TaikoJiro.

### Comma

For multiple values separated by comma (`,`), except for `text`-valued fields, optional whitespaces can occur before and/or after the comma.

* A trailing comma may present but is not universally supported.

### Value Type

* `number`: A real number. `number` indicates that it is *unspecified* whether a number with a fraction part is allowed. *Unspecified*: The supported upper limit & lower limit of the numeric range, unless otherwise specified.
  * `int`: An integer number in decimal, *e.g.*, `0` / `+10` / `-012`
  * `float`: A real number in decimal which can either be an integer or have the fraction part, *e.g.*, `0` / `+.3` / `-1.`
    * *Unspecified*: Whether a comma (`,`) can be used as the decimal point instead of a full-stop (`.`).
    * *Unspecified*: The supported precision.
    * *Proposal*: `+inf` for positive infinity (+∞) & `-inf` for negative infinity (−∞).
  * `enum-int` (enum-like, int-form): An `int` with specific accepted values.
  * *Unspecified*: Whether the positive sign (`+`) may appear for a non-negative or positive value, unless the type is indicated as `unsigned-`.
  * In TaikoJiro, leading non-newline whitespaces are always ignored.
* `complex-ri-number`: A complex number in the form of a real number, an imaginary number, or both added together. `complex-ri-number` indicates that it is *unspecified* whether a number with a fraction part is allowed for any of the real and imaginary components.
  * `complex-ri-float`: A complex number where each of the real and imaginary components can either be an integer or have the fraction part, *e.g.*, `1` / `i` / `.3+.3i`.
  * The format is one of:
    * `<number-real>`, a pure real number where the real component is `<number-real>`.
    * `<optional-sign-imaginary><unsigned-number-imaginary-specifier>`, a pure imaginary number where the imaginary component has the sign of `<optional-sign-imaginary>` (defaults to `+`) and the absolute value specified by `<unsigned-number-imaginary-specifier>`.
    * `<number-real><sign-imaginary><unsigned-number-imaginary-specifier>`, a general complex number where the real component is `<number-real>` and the imaginary component has the sign of `<sign-imaginary>` and the absolute value specified by `<unsigned-number-imaginary-specifier>`.
  * `<unsigned-number-imaginary-specifier>` can be one of:
    * `i`, the imaginary component has the absolute value of 1.
    * `<unsigned-number-imaginary>i`, the imaginary component has the absolute value of `<unsigned-float-imaginary>`.
    * *Unspecified*: whether `j` can be used in place of `i`.
* `string`: A string. `string` indicates that it is *unspecified* whether leading or trailing non-newline whitespaces are significant. *Unspecified*: The maximum supported length.
  * `text`: A string. Can contain leading or trailing non-newline whitespaces & comments.
  * `str`: A string. Leading and trailing new-newline whitespaces & comments are ignored.
  * In TJAPlayer3, in comma-separated lists, every comma (`,`) in `string` ***MUST*** be escaped as `\,` (while `\` itself requires no escaping).
  * `str-enum` (enum-like, string-form): A `str` with specific accepted values. Can be spelt in a form of one of `Value` / `VALUE` / `value`. *Unspecified*: Whether other spellings can be used.
    * In TaikoJiro:
      * If the string-form value begins with an upper-case letter and only this value begins with this letter, only the first 1 letter have effect (*e.g.*, `V` is also accepted).
      * If not, the value ***MUST*** begin with one of the above forms.
      * Leading non-newline whitespaces are ignored.
      * All trailing characters are ignored in TaikoJiro. (*e.g.*, `Vsomething` / `valuesomething` are also accepted)
* *Proposal*: `beats`
  * Format: `<float-upper-numeral>/<unsigned-float-lower-numeral><enum-str-delay-type>`
  * The beat duration of `<float-upper-numeral>` times of a 1/`unsigned-float-lower-numeral`-th note.
  * > Formula: Amount of beats = 4 × `upper` / `lower`
  * Analogy to the argument of [`#MEASURE`](#measure).
  * `<enum-str-delay-type>` can be one of:
    * (empty) / `-`, the time duration does not contain the `#DELAY` command(s) at the end of beat duration interval (if any).
    * `+`, the time duration contains the `#DELAY` command(s) at the end of beat duration interval (if any).
    * `d`, the specified beat duration includes beats which would otherwise pass during all `#DELAY` commands.
* *Proposal*: `relative-number`: Can be used as a `number` for a real number or the leading part of a compound number value. The specified value (include all numeric parts for a compound number value) is relative to a value equivalent to the last defined value. *Unspecified*: The behavior when being used as an `enum-int`.
  * Format:
    * `<relative-specifier><number>`, the value modified relative to a value equivalent to the last defined value
    * `=`, a value equivalent to the last defined value
  * `<relative-specifier>` can be one of:
    * `+=`, relatively increased.
    * `-=`, relatively decreased.
    * `*=`, relatively multiplied.
    * `/=`, relatively divided. The behavior is *unspecified* when `<number>` is 0.

## TJA Header

### Header Overview

#### Header Format

TJA header are written in the format of **`HEADER:values`**.

Each header ***MUST*** be placed on its own line.

The `HEADER:` part ***MUST*** be written in an all-upper-case manner and ***MUST NOT*** contain whitespaces in-between. No leading non-newline whitespaces are allowed.

Headers with an unrecognized `HEADER:` name are ignored.

If the `values` part is omitted, the default value is used, which can be used for resetting previously used headers from other difficulties or player sides to their default value.

For non-string values, whitespaces can immediately occur after `:`, *e.g.*, [`LEVEL: 8`](#level).

* Although the forms with whitespaces are seldom seen.

#### Header Scope

For headers placed outside any notechart definition enclosed between `#START` & `#END`, the effect of each header continues until the next occurrence of the same header or the end of the file, regardless of whether it is per-file or per&ndash;player-side.

Some headers are allowed to be placed in a notechart definition enclosed between `#START` & `#END` (*e.g.*, [the EXAM headers](#exam-headers)) and such usage is listed in their scope. Headers placed in a notechart definition are effectively [commands](#tja-command).

* *Unspecified*: The behavior when the same header occur multiple times within its scope.

### TITLE Headers

***Scope***: per-file

Specify the **title** of the song.

* `TITLE:<str-title>`
* `TITLE<enum-str-lang>:<str-title-localized>` &mdash; taiko-web ver.19.03.10, OpenTaiko (0auBSQ) v0.5.1
  * Specify the localized title.
  * `<enum-str-lang>` is an IETF BCP 47 language or region tag (see <https://en.wikipedia.org/wiki/IETF_language_tag>) and can be one of:
    * `EN`, **En**glish
    * `JA`, **Ja**panese &mdash; taiko-web, OpenTaiko (0auBSQ) v0.6.0+
    * `JP`, **J**a**p**anese (region tag) &mdash; OpenTaiko (0auBSQ) before v0.6.0
    * `FR`, _**Fr**ançais_ **Fr**ench &mdash; OpenTaiko (0auBSQ)
    * `ES`, _**Es**pañol_ Spanish &mdash; OpenTaiko (0auBSQ) v0.5.1.1
    * `ZH`, *<ruby>简<rt>Jiǎn</rt> 体<rt>tǐ</rt> **中**<rt>**Zh**ōng</rt> 文<rt>wén</rt></ruby>* Simplified Chinese &mdash; OpenTaiko (0auBSQ) v0.5.3
    * `CN`, Simplified **C**hi**n**ese (mainland **C**hi**n**a) (region tag) &mdash; taiko-web
    * `TW`, Traditional Chinese (<ruby>**臺**<rt>**T**ái</rt> **灣**<rt>**w**ān</rt></ruby>/<ruby>**台**<rt>**T**ái</rt> **灣**<rt>**w**ān</rt></ruby>) (region tag) &mdash; taiko-web
    * `NL`, _**N**eder**l**ands_ Dutch &mdash; OpenTaiko (0auBSQ) v0.6.0
    * `KO`, **Ko**rean &mdash; taiko-web, OpenTaiko (0auBSQ) v0.6.0

***From***: TJF format \
***Supported by***: (Universally supported)

### SUBTITLE Headers

***Scope***: per-file

Specify the **subtitle** (not of the meaning of *caption*) of the song (could be artist, game series, *etc.*).

The display details are *unspecified*.

* `SUBTITLE:<str-subtitle>`
  * `<str-subtitle>` can be one of:
    * `--<str-displayed-subtitle>`
      * Only show the subtitle in the song selection screen. Usually used for artist name.
      * The `--` prefix needs to be prepended to the displayed subtitle when the subtitle already begins with `--`.
    * `++<str-displayed-subtitle>` &mdash; TaikoJiro, TJAPlayer2 for PC, taiko-web ver.19.03.10 / `<str-displayed-subtitle>` &mdash; TaikoJiro, TJAPlayer2 for PC ver.2021xxxxxx, TJAPlayer3-f v1.7.2.0, OpenTaiko (0auBSQ) v0.6.0, taiko-web
      * Also show the subtitle during the gameplay screen & the result screen.
      * The `++` prefix needs to be prepended to the displayed subtitle when the subtitle begins with either `++` or `--`.
* `SUBTITLE<enum-str-lang>:<str-displayed-subtitle-localized>` &mdash; taiko-web ver.19.03.10, OpenTaiko (0auBSQ) v0.5.1
  * Specify the localized subtitle. The display mode (`++`/`--`) is instead specified by the `SUBTITLE:` header.
  * `<enum-str-lang>` can be one of the possible `<enum-str-lang>` for [the `TITLE<enum-str-lang>:` header](#title-headers).

***From***: TaikoJiro v2.64 \
***Supported by***: (Universally supported)

### MAKER:

***Scope***: per-file

Specify the creator (**maker**) of the notechart.

The display details are *unspecified*.

* `MAKER:<string-name-notechart-creator>`
* `MAKER:<string-name-notechart-creator> <string-notechart-creator-web-url>`
  * `<string-notechart-creator-web-url>` is immediately enclosed by a pair of angle brackets (`<` & `>`).

***From***: taiko-web ver.19.11.25 \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### NOTEDESIGNER Headers

***Scope***: per&ndash;player-side (?)

Specify the creator (**designer**) of the **note**chart.

The display details are *unspecified*.

* `NOTEDESIGNER<enum-int-diffculty-course>:<string-name-notechart-creator>` &mdash; (Better)TaikoCatsCaffe (?), OpenTaiko (0auBSQ) v0.6.0
  * `<enum-int-diffculty-course>` can one of the integer argument to [the `COURSE:` header](#course).
  * *Unspecified*: The behavior when the difficulty specified by `<enum-int-diffculty-course>` is different from the difficulty specified by `COURSE:` for the notechart definition.
* `NOTEDESIGNER:<string-name-notechart-creator>` &mdash; OpenTaiko (0auBSQ) v0.6.0

***From***: (Better)TaikoCatsCaffe (?) \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### GENRE:

***Scope***: per-file

Specify the **genre** of the song.

The display details are *unspecified*.

* `GENRE:<str-genre>`
  * *Unspecified*: The exact list of all supported `<str-genre>` and their aliases.
  * Usually supported:
    * `J-POP`
    * *`アニメ` (Anime)* "Animation"
    * *`ボーカロイド` (Bookaroido)* / `VOCALOID`
    * *`どうよう` (<ruby>童<rt>Dou</rt> 謡<rt>you</rt></ruby>)* "Child's Song"
    * *`バラエティ` (Baraeti)* "Variety"
    * *`クラシック` (Kurashikku)* "Classic"
    * *`ゲームミュージック` (Geemu Myuujikku)* "Game Music"
    * *`ナムコオリジナル` (Namuko Orijinaru)* "Namco Original"

***From***: TJAPlayer2 for PC \
***Supported by***: taiko-web ver.19.01.06

### SIDE:

***Scope***: per-file

Specify whether the corresponding song entry is displayed, regarding the *<ruby>裏<rt>ura</rt> 譜<rt>fu</rt> 面<rt>men</rt> 状<rt>jou</rt> 態<rt>tai</rt></ruby>* "inner notechart state/mode" ("*<ruby>裏 <rt>ura</rt></ruby>* inner or *<ruby>表 <rt>omote</rt></ruby>* outer **side**") of the song selection screen.

*Unspecified*: Whether and how inner mode is implemented.

* **`SIDE:1`** / **`SIDE:Normal`** / `SIDE:normal`
  * Displayed only outside the inner notechart mode.
* **`SIDE:2`** / **`SIDE:Ex`** / `SIDE:ex`
  * Displayed only during the inner notechart mode.
* **`SIDE:3`** / **`SIDE:Both`** / `SIDE:both` / **`SIDE:`**
  * Always displayed.

***From***: TaikoJiro v2.49 \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

#### Compatibility Issues

* In OpenTaiko (0auBSQ), `SIDE:` has been re-purposed to be used in conjunction with [`COURSE:Tower`](#course) to specify the actual difficulty and can be one of:
  * `SIDE:Normal`, the *<ruby>甘<rt>ama</rt> 口<rt>kuchi</rt></ruby>* "easy" difficulty.
  * `SIDE:Ex` / `SIDE:` / any other unrecogized argument, the *<ruby>辛<rt>kara</rt> 口<rt>kuchi</rt></ruby>* "hard" difficulty.

### SIDEREV:

***Scope***: per-file

Specify the filename of the *<ruby>裏<rt>ura</rt> 譜<rt>fu</rt> 面<rt>men</rt></ruby>* "inner notechart" or *<ruby>表<rt>omote</rt> 譜<rt>fu</rt> 面<rt>men</rt></ruby>* "outer notechart" version ("the **rev**erse **side**") of this notechart file.

* `SIDEREV:<string-filename-tja-inner-or-outer>`
  * If `SIDE:Normal` is used, specify the filename of the inner notechart.
  * If `SIDE:Ex` is used, specify the filename of the outer notechart.
  * If `SIDE:Both` is used, the behavior is *unspecified*.

***From***: TaikoJiro 2 v0.70

### WAVE:

***Scope***: per-file

Specify the audio file ("**wave**form audio file") of the song.

*Unspecified*: The exact list of supported file extensions.

*Unspecified*: Whether the notechart ends at the end of the audio file playback (if the audio file exist).

* `WAVE:<string-filepath-song-audio-file>`
  * `<string-filepath-song-audio-file>` has a file extension of one of, *e.g.*:
    * `.wav` &mdash; TaikoJiro
    * `.ogg` &mdash; TaikoJiro, TJAPlayer2 for PC
    * `.mp3` &mdash; TaikoJiro 1 with `lame.exe`
* `WAVE:`
  * No audio will be played.

***From***: TJF format \
***Supported by***: (Universally supported)

### DEMOSTART:

***Scope***: per-file

Specify the amount of seconds into the song audio for **start**ing playing the preview ("**demo**nstration") audio in the song selection screen.

* `DEMOSTART:<non-negative-float-seconds-preview-audio-offset>`
* `DEMOSTART:0` / `DEMOSTART:`

***From***: TaikoJiro v2.37 \
***Supported by***: (Universally supported)

### OFFSET:

***Scope***: per&ndash;player-side (?)

Specify the amount of seconds past ("**offset**ted") from the time position of `#START` of the notechart which the song audio should start playing from the beginning.

Equation: `offset` = `time-point-of-audio-beginning` − `time-point-of-chart-start` (Unit: Seconds)

* `OFFSET:<float-seconds-offset>`
* `OFFSET:0` / `OFFSET:`

Replaced the TJF command `#GOMUSIC` (starting ("**go**") playing the song audio ("**music**") from this point).

***From***: TaikoJiro \
***Supported by***: (Universally supported)

### SONGVOL:

***Scope***: per-file

Specify the relative amplitude percentage (%) of the desired **vol**ume gain of the **song** audio.

* `SONGVOL:<non-negative-number-percent-amplitude-gain>`
* `SONGVOL:`
  * The behavior is *unspecified*.

***From***: TaikoJiro v1.66 \
***Supported by***: TaikoJiro 2, TJAPlayer3 v1.5.2

#### Compatibility Issues

* Handled but ignored by TJAPlayer2 for PC & TJAPlayer3 before v1.5.2

### SEVOL:

***Scope***: per&ndash;player-side (?)

Specify the relative amplitude percentage (%) of the desired **vol**ume gain of the taiko sound ("**s**ound **e**ffect").

*Unspecified*: Whether the volume of system voice is affected.

* `SEVOL:<non-negative-number-percent-amplitude-gain>`
* `SEVOL:`
  * The behavior is *unspecified*.

***From***: TaikoJiro v1.66 \
***Supported by***: TaikoJiro 2

#### Compatibility Issues

* Handled but ignored by TJAPlayer2 for PC

### BPM:

***Scope***: per&ndash;player-side

Specify the initial **BPM** (**b**eat **p**er **m**inute) of the notechart.

* **`BPM:<non-zero-float-initial-bpm>`** &mdash; (Universally supported)
* `BPM:0`
  * The behavior is *unspecified* (may cause crashes in some existing simulators).
* `BPM:`
  * The behavior is *unspecified*.
  * In TaikoJiro, equivalent to `BPM:120`.

***From***: TJF format \
***Supported by***: (Universally supported)

### HEADSCROLL:

***Scope***: per&ndash;player-side, gimmicky

Specify the normal **scroll**ing velocity (before and non-after the beginning ("**head**") of the notechart), relative to the base scrolling velocity.

* `HEADSCROLL:<float-normal-scroll-velocity>`
* `HEADSCROLL:0`
  * The behavior is *unspecified*.

***From***: TJAPlayer2 for PC

### PREIMAGE:

***Scope***: per&ndash;player-side (?), decorative

Specify the jacket ("**pre**view") **image** of the song.

* `PREIMAGE:<string-filepath-background-image>`
* `PREIMAGE:`
  * No jacket image will be displayed.

***From***: OpenTaiko (0auBSQ) v0.5.4

### TAIKOWEBSKIN:

***Scope***: per-file, decorative

Specify the **skin** in the gameplay screen for **taiko-web**.

*Unspecified*: The behavior in other simulators.

* `TAIKOWEBSKIN:<comma-separated-list-string-key-value>`

Each element of `<comma-separated-list-string-key-value>` can be one of:

* `dir <string-dirpath-skin>`
  * `<string-dirpath-skin>` defaults to (empty).
* `name <str-skin-variation>`
  * Specify the `<text-suffix-skin-variation>` to be `_<str-skin-variation>` if not empty or to be (empty) if empty.
  * `<str-skin-variation>` defaults to (empty).
* `<enum-str-element> <enum-str-type>`, at least 1 element is required
  * `<enum-str-element>` can be one of:
    * `song`, the dancer background ("**song**" background) of the lower playback screen for single player.
    * `stage`, the horizontally repeating dancer floor ("**stage**") of the lower playback screen for single player.
    * `don`, the horizontally repeating and scrolling background behind the player character ("<ruby>**ど**<rt>**Do**</rt> **ん**<rt>**n**</rt> ちゃ<rt>cha</rt> ん<rt>n</rt></ruby>").
  * `<enum-str-type>` can be one of:
    * (Empty), use the element from the default skin.
    * `none`, blank
    * `static`, a still image, requires `bg_<str-element><text-suffix-skin-variation>.<text-file-extension>` to exist
    * `<enum-str-animation-type>`, animated image with pre-defined animation type, requires both `bg_<str-element><text-suffix-skin-variation>_a.<text-file-extension>` & `bg_<str-element><text-suffix-skin-variation>_b.<text-file-extension>` to exist.
      * Cannot be used when `<str-element>` is `stage`.

***From***: taiko-web ver.19.02.03

### SCENEPRESET:

***Scope***: per&ndash;player-side (?), decorative

Specify the pre-defined ("**preset**") skin ("**scene**") in the gameplay screen.

* `SCENEPRESET:<string-filepath-scene-preset>`
* `SCENEPRESET:`
  * The default skin is used.

***From***: OpenTaiko (0auBSQ) v0.6.0

### TOWERTYPE:

***Scope***: per&ndash;player-side (?), decorative

Specify the dedicated **tower** skin ("**type**") to use.

Used in conjunction with [`COURSE:Tower`](#course).

* `TOWERTYPE:<non-negative-int-tower-skin>`
* `TOWERTYPE:0` / `TOWERTYPE:`

***From***: OpenTaiko (0auBSQ) v0.5.0

### DANTICK:

***Scope***: per-file, decorative

Specify the dedicated *<ruby>**段**<rt>**Dan**'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" skin (*<ruby>コ<rt>ko</rt> ス<rt>su</rt> メ<rt>me</rt> **チッ**<rt>**chik**</rt> **ク**<rt>**ku**</rt></ruby>* "cosme**tic**" (?)) to use in the certification challenge selection screen.

*<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games.

Used in conjunction with [`COURSE:Dan`](#course).

* `DANTICK:<enum-int-dan-tick-skin>`
  * *Unspecified*: The support values.
  * In OpenTaiko (0auBSQ):
    * `0`: For ranks below the *<ruby>初<rt>Sho</rt> 級<rt>kyuu</rt></ruby>* "first level" rank
    * `1`: Blue ranks
    * `2`: Red ranks
    * `3`: Silver ranks, for <ruby>？<rt></rt> 人<rt>jin/uto</rt></ruby> ranks
    * `4`: Gold ranks, also for <ruby>？<rt></rt> 人<rt>jin/uto</rt></ruby> ranks
    * `5`: For *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby> <ruby>外<rt>Gai</rt> 伝<rt>den</rt></ruby>* Bonus Dojo ranks
      * Reference: <https://taiko.namco-ch.net/taiko/en/special/dani_dojo_gaiden/about.php>
* `DANTICK:0` / `DANTICK:`

***From***: OpenTaiko (0auBSQ) v0.5.1

### DANTICKCOLOR:

***Scope***: per-file, decorative

Specify the **color** filter to apply to the *<ruby>**段**<rt>**Dan**'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" skin (*<ruby>コ<rt>ko</rt> ス<rt>su</rt> メ<rt>me</rt> **チッ**<rt>**chik**</rt> **ク**<rt>**ku**</rt></ruby>* "cosme**tic**" (?)) objects in the certification challenge selection screen.

*<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games.

Used in conjunction with [`COURSE:Dan`](#course).

* `DANTICKCOLOR:<str-color-filter>`
  * `<str-color-filter>` can be one of:
    * `#<string-6-digit-24bit-rgb>`
    * `#<string-3-digit-12bit-rgb>`
    * `<enum-str-html-color-name>`
* `DANTICKCOLOR:#FFFFFF` / `DANTICKCOLOR:`

***From***: OpenTaiko (0auBSQ) v0.5.1

### SELECTBG:

***Scope***: per&ndash;player-side (?), decorative

Specify the **b**ack**g**round image of the song **select**ion screen. Override the skin settings.

* `SELECTBG:<string-filepath-selection-background-image>`
* `SELECTBG:`
  * The default song selection background for the containing song folder is used.

***From***: OpenTaiko (0auBSQ) v0.6.0

### BGIMAGE:

***Scope***: per&ndash;player-side (?), decorative

Specify the **b**ack**g**round **image** of the gameplay screen. Override the skin settings.

*Unspecified*: Whether the image is scaled or stretched to fill the gameplay screen.

* `BGIMAGE:<string-filepath-background-image>`
* `BGIMAGE:`
  * No background images will be displayed.

***From***: TJAPlayer2 for PC ver.2016021300

### BGOFFSET:

***Scope***: per&ndash;player-side (?), decorative

Specify the amount of seconds past ("**offset**ted") from the time position specified by [the `OFFSET:` header](#offset) which the background image ("**image**") should start displaying.

Equation: `bgoffset` = `time-point-of-image-displaying` − `time-point-of-audio-beginning` (Unit: Seconds)

* `BGOFFSET:<float-seconds-offset>`
* `BGOFFSET:0` / `BGOFFSET:`

***From***: ? \
Reference: TJA Format Support (vscode extension)

### BGMOVIE:

***Scope***: per&ndash;player-side (?), decorative

Specify the **b**ack**g**round video ("**movie**") of the gameplay screen. Override the skin settings.

*Unspecified*: Whether the video is scaled or stretched to fill the gameplay screen.

* `BGMOVIE:<string-filepath-background-video>`
* `BGMOVIE:`
  * No background videos will be displayed.

***From***: TJAPlayer2 for PC ver.2016021300

### MOVIEOFFSET:

***Scope***: per&ndash;player-side (?), decorative

Specify the amount of seconds past ("**offset**ted") from the time position specified by [the `OFFSET:` header](#offset) which the background video ("**movie**") should start playing from the beginning.

Equation: `movieoffset` = `time-point-of-video-beginning` − `time-point-of-audio-beginning` (Unit: Seconds)

* `MOVIEOFFSET:<positive-float-seconds-offset>`
* `MOVIEOFFSET:0` / `MOVIEOFFSET:`

***From***: TJAPlayer2 for PC ver.2015081100

#### Compatibility Issues

* In TJAPlayer3-f, the definition is changed to be relative to the time position of `#START` of the notechart.
  * Equation: `movieoffset_f` = `time-point-of-video-beginning` − `time-point-of-chart-start` (Unit: Seconds)

### BGA:

***Scope***: per&ndash;player-side (?), decorative

Specify a **b**ack**g**round video ("**a**nimation") to be used in the gameplay screen by [the `#BGAON` and `#BGAOFF` commands](#bgaon--bgaoff).

*Unspecified*: Whether the video is scaled or stretched to fill the gameplay screen.

Not reset by `BGA:` itself.

* `BGA:<string-filepath-background-video>`
* `BGA:`
  * The behavior is *unspecified*.

***From***: OpenTaiko (0auBSQ) v0.6.0

#### Compatibility Issues

* In OpenTaiko (0auBSQ) v0.6.0:
  * `<string-filepath-background-animation>` must start with `<unsigned-int-video-index>`, which must be exactly 2 decimal digits (with `0` prefixed if necessary) and is used to specify the background animation by [the `#BGAON` and `#BGAOFF` commands](#bgaon--bgaoff).

### LYRICS: / LYRICFILE:

***Scope***: per-file, decorative

Specify the lyric file(s) for the song to display **lyrics** in the playback screen.

*Unspecified*: The effective lyric file(s) when both the `LYRICS:` & `LYRICFILE:` headers are used.

*Unspecified*: Whether [`#LYRIC`](#lyric) commands are ignored if the lyric file is used.

* `LYRICS:<string-filepath-lyric-file>` &mdash; taiko-web, OpenTaiko (0auBSQ) v0.6.0 / `LYRICFILE:<string-filepath-lyric-file>` &mdash; TJAPlayer3-Develop-ReWrite, TJAPlayer3-f v1.6.0.0
  * `<string-filepath-lyric-file>` has a file extension of one of, *e.g.*:
    * `.vtt`, WebVTT, see <https://en.wikipedia.org/wiki/WebVTT> &mdash; taiko-web, OpenTaiko (0auBSQ) v0.6.0 (only for the `LYRICS:` header)
    * `.lrc`, LRC, see <https://en.wikipedia.org/wiki/LRC_(file_format)> &mdash; TJAPlayer3-Develop-ReWrite, TJAPlayer3-f v1.6.0.0
  * In TJAPlayer3-f & OpenTaiko (0auBSQ) v0.6.0, every comma (`,`) in `<string-filepath-lyric-file>` ***MUST*** be escaped as `\,`
* `LYRICS:<comma-separated-list-string-filepath-lyric-file>` &mdash; OpenTaiko (0auBSQ) v0.6.0 / `LYRICFILE:<comma-separated-list-string-filepath-lyric-file>` &mdash; TJAPlayer3-f v1.6.0.0, OpenTaiko (0auBSQ) v0.6.0
  * Specify the lyric file used for each song specified by [the `#NEXTSONG` command](#nextsong).
  * Used in conjunction with `COURSE:Dan`.
  * In TJAPlayer3-f & OpenTaiko (0auBSQ) v0.6.0, every comma (`,`) in the filepath specified in `<comma-separated-list-string-filepath-lyric-file>` ***MUST*** be escaped as `\,`
* `LYRICS:` / `LYRICFILE:`
  * Use only the lyric specified by [`#LYRIC`](#lyric) commands (if any).

***From***: taiko-web ver.20.03.31, TJAPlayer3-Develop-ReWrite \
***Supported by***: TJAPlayer3-f v1.6.0.0, OpenTaiko (0auBSQ) v0.6.0

#### Compatibility Issues

* In taiko-web, if the lyric file is used, all [`#LYRIC`](#lyric) commands are ignored.
* In TJAPlayer3-Develop-ReWrite but not OpenTaiko (0auBSQ), no effects.

### EXPLICIT:

***Scope***: per-file, decorative

If enabled, specify that the song has **explicit** (of the meaning of *not safe for work (NSFW)*) lyrics.

The display details are *unspecified*.

* `EXPLICIT:1`
  * The song has explicit lyrics.
* `EXPLICIT:0` / `EXPLICIT:`
  * The song has no explicit lyrics.

***From***: OpenTaiko (0auBSQ) v0.6.0

### GAME:

***Scope***: per&ndash;player-side (?)

Specify the **game** mode. The meaning of the symbols used in the notechart definition is changed accordingly; see [TJA Notechart Definition](#tja-notechart-definition).

*Unspecified*: The implemented game modes other than Taiko mode.

See [the `#GAMETYPE` command](#gametype) for specifying the game mode for specific notechart sections.

* `GAME:Taiko` / `GAME:`
  * A game mode similar to *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> の<rt>no</rt> 達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>*, developed by Namco (now Bandai Namco)
  * See [Note Symbols in Taiko Mode](#note-symbols-in-taiko-mode)
* `GAME:Jube` &mdash; TaikoJiro 1
  * A game mode similar to *Jubeat*, developed by Konami
  * See [Note Symbols in Jube Mode](#note-symbols-in-jube-mode)
* `GAME:Konga` / `GAME:Bongo` &mdash; taiko-web (plugin "Donkey Konga Mode")
  * A game mode similar to *Donkey Konga*, developed by Namco
  * See [Note Symbols in Konga Mode](#note-symbols-in-konga-mode)

***From***: TaikoJiro v2.13 \
***Supported by***: taiko-web (plugin "Donkey Konga Mode")

#### Compatibility Issues

* In TaikoJiro 1, the gameplay of `GAME:Jube` was unimplemented and was autoplay-only.

### COURSE:

***Scope***: per&ndash;player-side

Specify the *<ruby>コー<rt>koo</rt> ス<rt>su</rt></ruby> "course"/<ruby>む<rt>mu</rt> ず<rt>zu</rt> か<rt>ka</rt> し<rt>shi</rt> い<rt>i</rt></ruby> "difficulty"/<ruby>難<rt>nan'</rt> 易<rt>i</rt> 度<rt>do</rt></ruby> "difficulty (or easiness) level"* difficulty/difficulty level ("**course**").

Not to be confused with the difficulty star specified by [the `LEVEL:` header](#level).

"Course" in other rhythm games usually refers to playing multiple songs in a row. In early arcade console versions of the official game series, the player could only play a fixed difficulty during the *<ruby>ク<rt>ku</rt> レ<rt>re</rt></ruby>(<ruby>ジッ<rt>jet</rt> ト<rt>to</rt></ruby>)* "credit"/game session. "`<difficulty>`<ruby>コー<rt>koo</rt> ス<rt>su</rt></ruby>" ("`<difficulty>` course") was displayed in those official games.

Depending on the simulator, the `COURSE:` header may affect the judgment window, default scoring, the default increasing rate of the *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge, *etc.*

* **`COURSE:0`** / **`COURSE:Easy`** / `COURSE:easy`
  * The *<ruby>簡<rt>Kan</rt> 単<rt>tan</rt></ruby>/<ruby>か<rt>Ka</rt> ん<rt>n</rt> た<rt>ta</rt> ん<rt>n</rt></ruby>* Easy difficulty.
* **`COURSE:1`** / **`COURSE:Normal`** / `COURSE:normal`
  * The *<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>/<ruby>ふ<rt>Fu</rt> つ<rt>tsu</rt> う<rt>u</rt></ruby>* Normal difficulty.
* **`COURSE:2`** / **`COURSE:Hard`** / `COURSE:hard`
  * The *<ruby>難<rt>Muzuka</rt> し<rt>shi</rt> い<rt>i</rt></ruby>/<ruby>む<rt>Mu</rt> ず<rt>zu</rt> か<rt>ka</rt> し<rt>shi</rt> い<rt>i</rt></ruby>* Hard difficulty.
* **`COURSE:3`** / **`COURSE:Oni`** / `COURSE:oni`
  * The *<ruby>鬼<rt>Oni</rt></ruby>/<ruby>お<rt>O</rt> に<rt>ni</rt></ruby>* Oni/Extreme difficulty.
  * In the 7th arcade console version and before (specifically AC2&ndash;AC7) of the official game series, this difficulty was named *<ruby>ド<rt>Do</rt> ン<rt>n</rt> ダ<rt>da</rt> フ<rt>fu</rt>ル<rt>ru</rt></ruby>！<ruby>コー<rt>Koo</rt> ス<rt>su</rt></ruby>* "Donderful! Course" and had a different scoring rule from the other difficulties (see [`SCOREMODE:0`](#scoremode)). This difficulty was always named *<ruby>鬼<rt>Oni</rt></ruby>/<ruby>お<rt>O</rt> に<rt>ni</rt></ruby>* Oni in the PS2 console games but the same scoring rule still applied.
* **`COURSE:4`** / **`COURSE:Edit`** / `COURSE:edit`
  * This difficulty was meant for charters to freely specifying the scoring rules in earlier versions of TaikoJiro 1. However, the restriction of the scoring rules for other difficulties were lifted, which made this difficulty unnecessary for such a purpose.
  * This difficulty has been re-purposed as the *<ruby>お<rt>O</rt> に<rt>ni</rt></ruby> (<ruby>裏 <rt>Ura</rt></ruby>)* Oni/Extreme (Inner) difficulty.
* `COURSE:Ura` / `COURSE:ura` &mdash; taiko-web
  * Equivalent to `COURSE:Edit`
* **`COURSE:5`** / **`COURSE:Tower`** / `COURSE:tower` &mdash; TaikoJiro v1.79
  * This difficulty refers to the *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> タ<rt>Ta</rt> ワー<rt>waa</rt></ruby>* "Taiko Tower" notechart series in the *<ruby>わ<rt>Wa</rt> く<rt>ku</rt> わ<rt>wa</rt>く<rt>ku</rt> 冒<rt>Bou</rt> 険<rt>ken</rt> ラ<rt>Ra</rt> ン<rt>n</rt> ド<rt>do</rt></ruby>* "Wakuwaku (Exciting) Adventure land" mode from the 7th PS2 console game. To further simulate the mode, [the `LIFE:` header](#life) can be used in conjunction.
  * The actual behavior may differ from simulator to simulator.
  * In TaikoJiro, this cause the bar drumroll notes to be drawn above of all <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> & <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> notes. However, it was stated that *this behavior might be changed later.* (Original quote: "*この仕様は後に変更されるかもしれません。*")
  * This behavior is in reference to *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> タ<rt>Ta</rt> ワー<rt>waa</rt> 6<rt>Roku</rt></ruby>（<ruby>辛<rt>kara</rt> 口<rt>kuchi</rt></ruby>）* ("Taiko Tower 6 (hard)"), where the faster notes are drawn beneath the slower note (mainly the big bar drumroll notes) and thus make the notechart hard to read.
    * Exemplar Gameplay: <https://www.youtube.com/watch?v=8xU8uh5FSEw> <br />
      <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8xU8uh5FSEw" title="YouTube video player, playing &quot;【太鼓の達人 CS7】太鼓タワー その6&quot;, uploaded by Lunar. lu" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    * However, near to the end of this notechart, the big bar drumroll notes are drawn beneath the preceding big <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> note with the same scrolling velocity. The draw order is probably determined by the scrolling velocity rather than the note type in this case.
    * In TJAPlayer2 for PC, the draw order of bar drumroll notes is determined by the relative scrolling velocity regardless of the value of the `COURSE:` header.
* **`COURSE:6`** / **`COURSE:Dan`** / `COURSE:dan` &mdash; TJAPlayer3 v1.5.0
  * The special difficulty used for *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode", which resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games.
* `COURSE:`
  * An *unspecified* default difficulty is chosen by the simulator.
  * Usually equivalent to `COURSE:Oni`

***From***: TaikoJiro v1.76 \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TJAPlayer2 for PC but not TJAPlayer3, `COURSE:Tower` and its equivalent commands cause unintended behaviors. (?; deduced from source code)
  * <https://github.com/kairera0467/TJAP2fPC/blob/17e5c3bea5ccd5eaae5367128ec209384e12e954/DTXManiaプロジェクト/コード/スコア、曲/CDTX.cs#L4892>
  * <https://github.com/kairera0467/TJAP2fPC/blob/17e5c3bea5ccd5eaae5367128ec209384e12e954/DTXManiaプロジェクト/コード/スコア、曲/CDTX.cs#L2991>

### LEVEL:

***Scope***: per&ndash;player-side

Specify the *<ruby>難<rt>nan'</rt> 易<rt>i</rt> **度**<rt>do</rt></ruby>* "difficulty (or easiness) **level**"/difficulty star/? ("**level**").

Since the Japanese terminology is easily confused with the fore-mentioned "difficulty" specified by [the `COURSE:` header](#course), the difficulty star is often referred as *<ruby>星<rt>hoshi</rt> の<rt>no</rt> 数<rt>kazu</rt></ruby>/<ruby>★<rt>hoshi</rt> の<rt>no</rt> 数<rt>kazu</rt></ruby>* "amount of stars" and is displayed as "<ruby>★<rt>hoshi</rt></ruby>×*n*" in the official PC-generation arcade games.

Depending on the simulator and/or user settings, the `LEVEL:` header may affect the default scoring, the default increasing rate of the *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge, *etc.*

* `LEVEL:<positive-int-difficulty-star>` &mdash; (Universally supported)
  * *Unspecified*: The upper limit.
  * Universally supported range (as in the latest official games):
    * Easy: 1&ndash;5
    * Normal: 1&ndash;7
    * Hard: 1&ndash;8
    * Oni/Extreme and beyond: 1&ndash;10
* `LEVEL:0`
  * If supported, the difficulty star is displayed as 0 stars in the song selection screen. The other behaviors are *unspecified*.
* `LEVEL:`
  * An *unspecified* default difficulty star is chosen by the simulator.
  * Usually equivalent to `LEVEL:0`.
* `LEVEL:<non-negative-float-difficulty-star>` &mdash; TaikoJiro v2.78
  * The fraction part is considered for sorting by difficulty star but is not displayed.

***From***: TJF format \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TaikoJiro and TJAPlayer2 for PC, the difficulty star displayed in the song selection screen for each difficulty is determined differently from the actual difficulty star in the gameplay screen. For the difficulty star displayed in the song selection screen:
  * The scope of the `LEVEL:` header is per-difficulty instead of per&ndash;player-side. Each per-difficulty scope starts or resumes at `COURSE:` headers specifying the target difficulty and ends at another `COURSE:` header specifying a different difficulty.
    * A "deceptive difficulty star" (a displayed difficulty star in the song selection screen which is different from the actual difficulty star in the gameplay screen) can be defined by placing the `LEVEL:` for the deceptive difficulty star after all notechart definitions in the per-difficulty scope.
  * In TaikoJiro, if a `LEVEL:` header is defined before any `COURSE:` headers with difficulty specified, the specified difficulty star instead of 0 stars will be used as the default difficulty star.
  * In TJAPlayer2 for PC, if a `LEVEL:` header is defined before any `COURSE:` headers with value, the specified difficulty star become the difficulty star for the *<ruby>お<rt>O</rt> に<rt>ni</rt></ruby>* Oni/Extreme difficulty, even if no notecharts are defined for the Oni/Extreme difficulty.

### STYLE:

***Scope***: per&ndash;player-side

Specify the total amount of play-**side**s of the notechart(s).

The multiple-player-side notecharts of the difficulty is chosen if enough amount of players have chosen the same difficulty.

In the official games, some difficulties may have only 2-player-side notecharts but are still playable in single player mode, where the notechart for one of the player-side is chosen (always the 1st player-side in PC-generation games).

*Unspecified*: Whether such notecharts are chosen when some players have chosen different difficulties.

* In TaikoJiro 1, such notecharts are chosen as if all other players had chosen the same difficulty for each player.

If the specified amount of player-sides is not 1, [`#START <enum-str-player-side>`](#start--end) should be used for specifying the player-side of the notechart.

* `STYLE:1` / `STYLE:Single` / `STYLE:single` / `STYLE:`
* `STYLE:2` / `STYLE:Double` / `STYLE:double` / `STYLE:Couple` / `STYLE:couple`
* *Proposal*: `STYLE:<positive-int-amount-of-player-sides>`

Reference: *ダブルプレイ* ("Double Play"; "Two-player Charts"). 太鼓の達人 譜面とか Wiki\* ("Taiko no Tatsujin - Wiki\* about Notecharts and so on"). <https://wikiwiki.jp/taiko-fumen/収録曲/ダブルプレイ>

***From***: TaikoJiro v1.99 \
***Supported by***: TJAPlayer2 for PC

#### Compatibility Issues

* Ignored in TaikoJiro 2.

### BALLOON Headers

***Scope***: per&ndash;player-side

Specify the required amount of hits of *<ruby>激<rt>geki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>/<ruby>ゲ<rt>ge</rt> キ<rt>ki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>* "fierce drumroll" burst note / *<ruby>風<rt>fuu</rt> 船<rt>sen</rt></ruby>/<ruby>ふ <rt>fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* **balloon**&ndash;type notes (denoted by `7`, `9`, or `D` in the notechart definition), in the order of their definition, ***NOT*** the hit order during playing.

Each balloon-type note with unassigned hit amount requires an *unspecified* default amount of hits.

* In TaikoJiro & TJAPlayer2 for PC, the default amount of hits is `5`.

*Proposal*: The [`#BALLOON`](#proposal-balloon-command) command can be used in the notechart definition for the same purpose instead.

* `BALLOON:<comma-separated-list-non-negative-int-amount-of-hits>`
  * The list of amount is iterated over all sections of all *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart branches"/forked paths.
* `BALLOONNOR:<comma-separated-list-non-negative-int-amount-of-hits>` &mdash; TJAPlayer2 for PC
  * The list of amount is iterated over only sections of common & ***<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>*** **Nor**mal "branches"/paths.
* `BALLOONEXP:<comma-separated-list-non-negative-int-amount-of-hits>` &mdash; TJAPlayer2 for PC
  * The list of amount is iterated over only sections of ***<ruby>玄<rt>Kuro</rt> 人<rt>uto</rt></ruby>*** "Professional"/Advanced ("**Exp**ert") "branches"/paths.
* `BALLOONMAS:<comma-separated-list-non-negative-int-amount-of-hits>` &mdash; TJAPlayer2 for PC
  * The list of amount is iterated over only sections of ***<ruby>達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>*** **Mas**ter "branches"/paths.

For each element of `<comma-separated-list-non-negative-int-amount-of-hits>`, if the amount of hits is `0`, the per-note behavior is *unspecified*.

***From***: TaikoJiro \
***Supported by***: (Universally supported)

#### Compatibility Issues

* TJAPlayer2 for PC & TJAPlayer3: The `BALLOON:` header is *erroneously* treated as the `BALLOONNOR:` header.
* TJAPlayer3 but not TJAPlayer3-Develop: If a balloon-type note is defined in sections after [`#BRANCHEND`](#branchstart--branchend) and before another [`#BRANCHSTART`](#branchstart--branchend), it *erroneously* uses 3 values from the iteration of the `BALLOONNOR:` / `BALLOONEXP:` / `BALLOONMAS:` list according to the last defined "branch"/path before the `#BRANCHEND`. (?; deduced from source code)
  * <https://github.com/AioiLight/TJAPlayer3/blob/59835a522887c67b8db0e60d89a1e61ed3220742/TJAPlayer3/Songs/CDTX.cs#L3719>, <https://github.com/AioiLight/TJAPlayer3/blob/59835a522887c67b8db0e60d89a1e61ed3220742/TJAPlayer3/Songs/CDTX.cs#L4020-L4055>
  * *C.f.*, <https://github.com/kairera0467/TJAP2fPC/blob/17e5c3bea5ccd5eaae5367128ec209384e12e954/DTXManiaプロジェクト/コード/スコア、曲/CDTX.cs#L3872-L3877>, <https://github.com/kairera0467/TJAP2fPC/blob/17e5c3bea5ccd5eaae5367128ec209384e12e954/DTXManiaプロジェクト/コード/スコア、曲/CDTX.cs#L4118-L4149>
* TJAPlayer3-Develop: If a balloon-type note is defined in sections after [`#BRANCHEND`](#branchstart--branchend) and before another [`#BRANCHSTART`](#branchstart--branchend), it use 1 value from each iteration of `BALLOONNOR:`, `BALLOONEXP:`, & `BALLOONMAS:` instead of only `BALLOONNOR:`.
  * <https://github.com/TJAPlayer3-Develop/TJAPlayer3-Develop/blame/b6ab37cbdc25a4257c7d685de48b6997ae81fe95/TJAPlayer3/Songs/CDTX.cs#L4173-L4217>
  * See commit: <https://github.com/TJAPlayer3-Develop/TJAPlayer3-Develop/commit/abffd3204c437abaaf49fbd2ae890729a5485682>

### LIFE:

***Scope***: per&ndash;player-side

Specify the initial **life** count of the life count gauge (if used).

A *<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* bad judgment decreases the life count by 1 (missing). When the life count decreased to 0, the player is immediately judged to be failed and the notechart ends.

*Unspecified*: Whether there is invincible time after missing and how long is its time duration.

* In TaikoJiro, invincible time was not implemented.
* In OpenTaiko (0auBSQ), the invincible time is 2 seconds.

*Unspecified*: The behavior when a non-zero value is used not in conjunction with [`COURSE:Tower`](#course).

* `LIFE:<positive-int-life-count>`
  * Use the life count gauge rules.
* `LIFE:0`
  * Use the normal *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge rules unless there are other overriding user settings.
* `LIFE:`
  * The behavior is *unspecified*.
  * In TaikoJiro, equivalent to `LIFE:0`.
  * In OpenTaiko (0auBSQ), equivalent to `LIFE:5` when used in conjunction with `COURSE:Tower`.

***From***: TaikoJiro v2.19 \
***Supported by***: OpenTaiko (0auBSQ) v0.4.3

### TOTAL:

***Scope***: per&ndash;player-side

Specify the **total** *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge increment of the notechart when all hit-type notes are hit with *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD judgment, *i.e.*, *<ruby>ド<rt>Do</rt> ン<rt>n</rt> ダ<rt>da</rt> フ<rt>fu</rt> ル<rt>ru</rt> コ<rt>ko</rt> ン<rt>n</rt> ボ<rt>bo</rt></ruby>* Donderful Combo.

* `TOTAL:<non-negative-number-total-gauge-increment>`
  * The increasing rate of spirit gauge/soul gauge is calculated from the given total spirit gauge/soul gauge increment.
* `TOTAL:`
  * The increasing rate of spirit gauge/soul gauge is determined by the simulator. *Unspecified*: The details for determining it; usually one of the official games is followed.

***From***: TaikoJiro v2.92 & TaikoJiro 2 v0.93

### GAUGEINCR:

***Scope***: per&ndash;player-side

Specify the rounding mode of the **incr**ement of the *<ruby>魂<rt>tamashii</rt> **ゲー**<rt>**gee**</rt>**ジ**<rt>**ji**</rt></ruby>* spirit **gauge**/soul **gauge**.

* `GAUGEINCR:<enum-str-gauge-increment-rounding-mode>`
  * `<enum-str-gauge-increment-rounding-mode>` can be one of:
    * (Empty) / `Normal`
    * `Floor`
    * `Round`, round to the nearest.
    * `Notfix`, no rounding is performed.
    * `Ceiling`

***From***: TJAPlayer3 v1.5.4

### EXAM Headers

***Scope*** (placed outside of any notechart definition enclosed between `#START` & `#END`): per&ndash;player-side (?) \
***Scope*** (placed in a notechart definition enclosed between `#START` & `#END`): per-song (begins with a [`#NEXTSONG` command](#nextsong) and ends with another [`#NEXTSONG` command](#nextsong)) &mdash; TJAPlayer3-Develop-ReWrite

Specify a requirement for passing the notechart in *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" ("**exam**ination").

*<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games.

Used in conjunction with [`COURSE:Dan`](#course).

* `EXAM<exam-requirement-index-specifier>:<enum-str-requirement>, <number-pass-requirement>, <number-gold-requirement>, <enum-str-range>`
  * `<exam-requirement-index-specifier>` specifies the displayed order of this requirement. The display details are *unspecified*. Its value range is:
    * `1`&ndash;`3`
    * `1`&ndash;`4` &mdash; TJAPlayer3-Develop-ReWrite
      * For `1`, `<enum-str-requirement>` is expected to be `g`.
    * `1`&ndash;`7` &mdash; OpenTaiko (0auBSQ)
      * For `1`, `<enum-str-requirement>` is expected to be `g`.
  * `<enum-str-requirement>` can be one of:
    * `g`, final percentage (%) of *<ruby>魂<rt>tamashii</rt> **ゲー**<rt>**g**ee</rt>ジ<rt>ji</rt></ruby>* spirit **g**auge/soul **g**auge.
    * `jp`, amount of *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") **j**udgment.
    * `jg` amount of *<ruby>可<rt>Ka</rt></ruby>* **G**OOD/OK **j**udgment.
    * `jb`, amount of *<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* **B**AD **j**udgment.
    * `jm`, amount of caught bomb/**m**ine notes. &mdash; OpenTaiko (0auBSQ)
    * `ja`, amount of caught _**A**d libitum_ (**A**D-LIB) notes. &mdash; OpenTaiko (0auBSQ)
    * `s`, final **s**core.
    * `r`, amount of hits on *all* drum**r**oll-type notes.
      * Not to be confused with the `r` (bar drum**r**oll notes&ndash;only) used for the condition of [the `#BRANCHSTART` command](#branchstart--branchend).
    * `h`, amount of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, non-blank hits.
      * > Formula: `h` = `jp` + `jg` + `r`
    * `c`, maximum/longest **c**ombo.
    * `a`, final percentage (%) of **a**ccuracy. &mdash; OpenTaiko (0auBSQ)
      * > Formula: (*<ruby>良<rt>Ryou</rt></ruby>* GREAT/Good + 0.5 × *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK) / **max**{*<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD + *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK + *<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, 1} × 100(%) (Unit of variables: Amount of judgment results)
  * `<enum-str-range>` can be one of:
    * `m` / (*Proposal*) `>=`, **m**ore than or equal to ("≥") the given requirement
    * `l` / (*Proposal*) `<`, **l**ess than ("\<") the given requirement
* `EXAM<exam-requirement-index-specifier>:<enum-str-requirement>, <comma-separated-list-number-pass-and-gold-requirements>, <enum-str-range>` &mdash; TJAPlayer3-f
  * The elements of `<comma-separated-list-number-pass-and-gold-requirements>` are pairs of `<number-pass-requirement>, <number-gold-requirement>` for each song specified by [the `#NEXTSONG` command](#nextsong).
  * Corresponding to the per-song&ndash;scoped usage in TJAPlayer3-Develop-ReWrite & OpenTaiko (0auBSQ).
* `EXAMGAUGE:<number-pass-requirement>, <number-gold-requirement>, <enum-str-range>` &mdash; TJAPlayer3-f
  * The `<enum-str-requirement>` is implicitly fixed to `g`.
  * Corresponding to the `EXAM1:` header in TJAPlayer3-Develop-ReWrite & OpenTaiko (0auBSQ).

***From***: TJAPlayer3 v1.5.0

### SCOREMODE:

***Scope***: per&ndash;player-side, scoring

Specify the **scoring mode**.

Affects combo bonus, combo milestone bonus, *<ruby>ゴー<rt>Goo</rt> ゴー<rt>Goo</rt> タ<rt>Ta</rt> イ<rt>i</rt> ム<rt>mu</rt></ruby>* Go-Go Time bonus, & big note bonus.

The main scoring formula has two `int` variables: `init` & `diff`.

The "basic score" below refers to the score awarded per *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD judgment on non-big notes outside Go-Go Time sections.

When either the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true percussion (performance)"/"true performance" option is enabled or `SCOREMODE:3` is used, the basic score is fixed to `init` points and [the `SCOREDIFF:` header](#scorediff) is ignored.

* In TaikoJiro, the option with *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" enabled is referred as "Stable", while the disable of this option is referred as "StepWise".

*Unspecified*: Scoring details other than the basic score in each mode; usually one of the official games is followed.

* `SCOREMODE:0`
  * Follow the special scoring rule of *<ruby>ド<rt>Do</rt> ン<rt>n</rt> ダ<rt>da</rt> フ<rt>fu</rt>ル<rt>ru</rt></ruby>！<ruby>コー<rt>Koo</rt> ス<rt>su</rt></ruby>* "Donderful! Course" from AC2&ndash;AC7 (see [`COURSE:3`](#course) for explanation).
  * `init` & `diff` are both fixed to 1000 points and the [`SCOREINIT:`](#scoreinit) and [`SCOREDIFF:`](#scorediff) headers are both ignored.
  * Combo | 1&ndash;199 | 200&ndash;
    --- | --- | ---
    Basic score (points) | 1000 | 2000
  * *Unspecified*: The behavior when the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" option is enabled.
* `SCOREMODE:1`
  * Follow the normal scoring rule of the official PS1- and PS2-generation games (*<ruby>旧<rt>kyuu</rt> 筐<rt>kyou</rt> 体<rt>tai</rt></ruby>* "old (arcade) cabinet"; AC1&ndash;AC14).
  * Combo | 1&ndash;9 | 10&ndash;19 | 20&ndash;29 | 30&ndash;39 | 40&ndash;49 | 50&ndash;59 | 60&ndash;69 | 70&ndash;79 | 80&ndash;89 | 90&ndash;99 | 100&ndash;
    --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
    *n* | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
  * Only the first 9 notes of a combo reward exactly `init` points per note.
  * The basic score is `init` + *n* × `diff` points.
  * > An equivalent formula: Basic score = `init` + **min**{**floor**(`combo` / 10), 10} × `diff` (points).
  * In TaikoJiro, if the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" option is enabled, the scoring rules of the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" mode from the 14th arcade console version of the official game is followed.
* `SCOREMODE:2`
  * Follow the scoring rule of the official PS3-generation games (AC15).
  * Combo | 1&ndash;9 | 10&ndash;29 | 30&ndash;49 | 50&ndash;99 | 100&ndash;
    --- | --- | --- | --- | --- | ---
    *n* | 0 | 1 | 2 | 3 | 4
  * The basic score is `init` + *n* × `diff` points.
* `SCOREMODE:3` &mdash; TJAPlayer2 for PC but not TJAPlayer3 v1.4.0+, TJAPlayer3-f
  * Follow the scoring rule of the official PC-generation games (<ruby>虹<rt>Niji</rt> 色<rt>iro</rt></ruby>/<ruby>ニ<rt>Ni</rt> ジ<rt>ji</rt> イ<rt>i</rt> ロ<rt>ro</rt></ruby> version(s); AC16)
  * All types of score bonus are cancelled.
  * Combo | 1&ndash;
    --- | ---
    Basic score (points) | `init`
  * The scoring rules are the same regardless of the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" option.
* `SCOREMODE:`
  * The actual scoring mode used is *unspecified*.
  * In TaikoJiro: `SCOREMODE:1`
  * In TJAPlayer3: Depending on the user settings

Reference: *配点* ("Scoring"). 太鼓の達人 譜面とか Wiki\* ("Taiko no Tatsujin - Wiki\* about Notecharts and so on"). <https://wikiwiki.jp/taiko-fumen/システム/配点>

***From***: TaikoJiro v2.85 \
***Supported by***: TaikoJiro 2 v0.72, TJAPlayer2 for PC

#### Compatibility Issues

* In TJAPlayer3 v1.4.0+ but not TJAPlayer3-f, `SCOREMODE:3` is treated the same as `SCOREMODE:2`, where the behavior of the former `SCOREMODE:3` can be enabled by enabling the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" option.

### SCOREINIT:

***Scope***: per&ndash;player-side, scoring

Specify the *<ruby>**初**<rt>sho</rt> 項<rt>kou</rt></ruby>* **init**ial term (refers to an arithmetic progression) (`init`) used for calculate the basic **score**. See the explanation for [the `SCOREMODE:` header](#scoremode).

* `SCOREINIT:<non-negative-int-score-init>`
* `SCOREINIT:<non-negative-int-score-init>, <non-negative-int-score-init-shin'uchi>` &mdash; TaikoJiro v2.70
  * If supported, `<non-negative-int-score-init-shin'uchi>` is used for `init` when the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true percussion (performance)" option ("stable") is enabled
* `SCOREINIT:0`
  * The behavior is *unspecified*.
* `SCOREINIT:`
  * `init` is determined by the simulator. *Unspecified*: The details for determining it; usually one of the official games is followed.

***From***: TaikoJiro v1.67 \
***Supported by***: (Universally supported)

### SCOREDIFF:

***Scope***: per&ndash;player-side, scoring

Specify the *<ruby>公<rt>kou</rt> **差**<rt>sa</rt></ruby>* common **diff**erence (refers to an arithmetic progression) (`diff`) used for calculate the basic **score**. See the explanation for [the `SCOREMODE:` header](#scoremode).

* `SCOREDIFF:<non-negative-int-score-diff>`
* `SCOREDIFF:<non-negative-int-score-diff>d` &mdash; TaikoJiro v2.49
  * If supported, a scoring rule similar to *<ruby>ド<rt>Do</rt> ン<rt>n</rt> ダ<rt>da</rt> フ<rt>fu</rt>ル<rt>ru</rt></ruby>！<ruby>コー<rt>Koo</rt> ス<rt>su</rt></ruby>* "Donderful! Course" is used as if `SCOREMODE:0` were used, except that the `SCOREINIT:` & `SCOREDIFF:` are not ignored.
  * Combo | 1&ndash;199 | 200&ndash;
    --- | --- | ---
    Basic score | `init` | `init` + `diff`
* `SCOREDIFF:0`
  * `diff` is `0`.
* `SCOREDIFF:`
  * `diff` is determined by the simulator. *Unspecified*: The details for determining it; usually one of the official games is followed.

***From***: TaikoJiro v1.67 \
***Supported by***: (Universally supported)

### HIDDENBRANCH:

***Scope***: per&ndash;player-side, gimmicky

If enabled, make the *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart **branch**"/forked path indicator **hidden** in the song selection screen; hide the "branch"/path mark on the note field from the beginning of the notechart until time point when the "branch"/path&ndash;switching effects should play for the first "branch"/path section in the gameplay screen.

* `HIDDENBRANCH:1`
  * Hiding the "branch"/path indicator and note field mark.
* `HIDDENBRANCH:0`
  * The behavior is *unspecified*.
  * In TJAPlayer2 for PC: Equivalent to `HIDDENBRANCH:1`
* `HIDDENBRANCH:`
  * Disable such effects.

***From***: TJAPlayer2 for PC

## TJC Header

### TJC Header Overview

The descriptions of [Header Overview](#header-overview) for TJA mostly applies. However, sequential headers can appear multiple times within their scope.

Some TJA headers can be used as TJC headers and have similar or even identical effects. *Unspecified*: Which TJA headers can be used as TJC header aside from [`TITLE:`](#title-headers), [`COURSE:`](#course), & [`TOTAL:`](#total). Only non-TJA headers are listed in this section.

See [the `#NEXTSONG` command](#nextsong) for the TJA command version of TJC headers.

### SONG:

***Scope***: per-file, sequential

Specify a notechart ("**song**") of the notechart set.

* `SONG:<string-filepath-tja-from-game-root-directory>`

***From***: TaikoJiro v2.34 \
***Supported by***: (Universally supported)

## TJA Command

### Command Overview

#### Command Format

TJA commands are written in the format of **`#COMMAND values`**.

Each commands ***MUST*** be placed on its own line.

No leading non-newline whitespaces are allowed for the `#START` and `#END` commands & other commands placed outside of the notechart definition enclosed between `#START` & `#END`.

However, leading non-newline whitespaces are allowed and ignored in the notechart definition enclosed between `#START` & `#END`.

*Unspecified*: The behavior when any commands are placed before any headers outside the notechart definition, especially for the commands which are expected to be placed before the notechart definition.

The `#COMMAND` part ***MUST*** be written in an all-upper-case manner and ***MUST NOT*** contain whitespaces in-between.

Commands with an unrecognized `#COMMAND` name are ignored.

*Unspecified*: The behavior when the whitespaces before the `values` part is omitted for all-letter commands with numeric values (occurs in some legacy charts).

* In TaikoJiro, such a case is parsed as if there were whitespaces before the `values` part.

The arguments for commands introduced in TaikoJiro are comma-separated. However, the arguments for commands introduced in TJAPlayer2 for PC are instead whitespace-separated as in the `.bms` format (which is extended into the `.dtx` format for DTXMania).

*Unspecified*: The behavior when a comma (`,`) is used as the decimal point (normally a full-stop (`.`)).

#### Command Scope

No known per-file commands exist, which would be effectively [headers](#tja-header). Per&ndash;player-side commands are similar to [headers](#tja-header) but the effects of these commands reset at the end of their scope.

Except for one-shot commands, the effect of each command continues until the next occurrence of any command from the same command group or [`#END`](#start--end).

* For per&ndash;player-side commands, the behavior is *unspecified* when (the same or different) commands in the same command group occur together within its scope.
* For measure-based&ndash;scoped commands, the behavior is *unspecified* when any notechart symbols occur between such a command and the first symbol of the measure in the notechart definition.

Some branch-scoped commands are non-sequential, *i.e.*, they can be arranged freely within the same beat position without causing any behavior changes, as long as both their relative order to the sequential commands and the relative order among commands which override each other are not changed. All commands with other type of scope are implicitly sequential.

#### Command Late Effect Scope

A command may have some effects applied only when their approach phase is reached. These effects are defined as the late effects. The late effect scope is defined by the targeted game objects which are affected by the late effects.

The approach phase of a command occurs before the head of their defined beat position by a specified time or beat duration (if any) or no duration.

*Proposal*: Allow the late effect scope to be overridden for branch-scoped commands targeting notes & bar lines, see [*Proposal*: Command Modifier](#proposal-command-modifier).

#### Command Effect Target

Commands only affect their targeting game objects. The target of each command can be any (including none) of:

* Notes, including fake/dummy notes.
* Bar lines, including fake/dummy bar lines.
* Judgment mark(s). There may be multiple judgment marks for a single player when, *e.g.*, [the `#SPLITLANE` command](#splitlane--mergelane) is used or (*Proposed*) [the `#JPOSSCROLL` command](#jposscroll) is used inconsistently in any layers defined by [the `#LAYER` command](#proposal-layer).
* Note field(s): Any effects affecting the default scrolling path of notes and bar lines. There may be multiple note fields for a single player when there are multiple judgment marks.
* Gameplay screen: Any other visible effects not directly targeting the above objects.

### `#BMSCROLL` / `#HBSCROLL` / `#NMSCROLL`

***Scope*** (placed before [the `#START` command](#start--end)): per&ndash;player-side, gimmicky \
***Scope*** (placed after [the `#START` command](#start--end)): branch, non-before, gimmicky &mdash; OpenTaiko (0auBSQ) v0.6.0 \
***Late effect scope***: all (?) \
***Effect target***: notes, bar lines

Use a **scroll**ing mode similar to the scrolling method used in either **B**E**M**ANI-series or the official Taiko ("**n**or**m**al") game series, unless overridden by user settings.

*Unspecified*: Whether the final per-note velocity is kept as the base velocity when switching the scrolling mode.

*Unspecified*: Whether the switching of scrolling mode is taken into account for preventing the note position from being suddenly changed when switching the scrolling mode.

* `#BMSCROLL` &mdash; TaikoJiro v1.91
  * The [`#SCROLL`](#scroll) command is ignored.
  * Emulates the scrolling behavior of Taikosan.
* `#HBSCROLL` &mdash; TaikoJiro v2.31
  * Likes `#BMSCROLL` ("**B**E**M**ANI-like"), but [the `#SCROLL` command](#scroll) ("(per-note) **H**iSpeed") is not ignored and is effective.
* `#NMSCROLL` &mdash; OpenTaiko (0auBSQ) v0.6.0 / initial value
  * Use the default ("**n**or**m**al") Taiko-like scrolling behavior

Scrolling mode comparison: Consider BPM changes occur during notes traveling through the whole note field (including the part past the judgment mark).

* `scroll` is the scrolling rate multiplier specified by [the `#SCROLL` command](#scroll) and by [the `HEADSCROLL:` header](#headscroll).
  * Fixed to `1` when either `#BMSCROLL` or REGUL-SPEED (TaikoJiro) is used.
  * > Formula: `scroll` = `scroll_command` × `headscroll`, otherwise
* `modifier` is the scrolling rate multiplier specified by the speed modifier options.
  * Its value is the apparent BPM specified by REGUL-SPEED settings if REGUL-SPEED is used.

Scrolling mode | Taiko-like | BEMANI-like <br> XMod | CMod
--- | --- | --- | ---
Command or TaikoJiro setting | (Default) <br /> `#NMSCROLL` | `#BMSCROLL` <br> `#HBSCROLL` <br> User option | User option: REGUL-SPEED
Varing factor | Relative scrolling speed vector among notes | Scrolling speed vector during travel | Beats taken during traveling
Scrolling velocity <br> Note traveling takes 4 beats in what BPM | **abs**(BPM at the defined position of the note × `scroll` × `modifier`) | **abs**(Current effective BPM (0 during a positive [`#DELAY`](#delay)) × `scroll` × `modifier`) | The apparent BPM specified by REGUL-SPEED settings ("BPM HiSpeed") <br> `modifier`
Default scrolling changes of [`#BPMCHANGE`](#bpmchange) command | Set the per-note base BPM of non-preceding notes and bar lines | Suddenly change the apparent base BPM of all notes & all bar lines | (No changes)
Default scrolling changes of [`#DELAY`](#delay) command | (No changes) | Pause the scrolling if positive; <br> (no changes) if negative | (No changes)
Default scrolling changes of [`#SCROLL`](#scroll) command | Set the per-note `scroll` | (Ignored) (`#BMSCROLL`) <br> Set the per-note `scroll` (`#HBSCROLL`) | (Ignored)
*Proposal*: Mode-invariant `#BPMCHANGE` command | `#BPMCHANGE <value>; :` | `#BPMCHANGE <value>; *:*` | `#BPMCHANGE <value>; :` + `#SCROLL <non-zero-float-bpm>bpm; :*`
*Proposal*: Mode-invariant `#DELAY` command | `#DELAY <value>; :` | `#DELAY <value>; *:*` | `#DELAY <value>; :`
*Proposal*: Mode-invariant velocity-changing command | `#SCROLL <value>; :` (default) | `#SCROLL <value>; *:*` | `#SPEED <value>bpm; *:*; <changing-duration>`

In OutFox, the Taiko-like scrolling mode can be achieved by using CAMod (AMod/"Average BPM Scroll Mode" with constant per-note scrolling speed) with the BPM parameter set to the average BPM of the notechart.

See [The Measure-terminating Symbol and Timing](#the-measure-terminating-symbol-and-timing) for the behavior of timing commands.

*Proposal*: See [*Proposal*: Command Modifier](#proposal-command-modifier) for the syntax for mode-invariant commands.

***From***: TaikoJiro v1.91 \
***Supported by***: TaikoJiro 2, TJAPlayer2 for PC

#### Compatibility Issues

* In TaikoJiro, all notechart objects past the judgment timing keep a constant velocity even when `#BPMCHANGE` commands are used in BMS scrolling modes. This behavior can be utilized for creating bar drumroll notes which stretch when reaching the judgment timing.

### `#PAPAMAMA`

***Scope***: per&ndash;player-side (placed before [the `#START` command](#start--end)) \
***Effect target***: notes

Use the *<ruby>**パ**<rt>**Pa**</rt> **パ**<rt>**pa**</rt> **マ**<rt>**Ma**</rt> **マ**<rt>**ma**</rt> サ<rt>Sa</rt> ポー<rt>poo</rt> ト<rt>to</rt></ruby>* "Parent Support Mode"/Helping Hand Mode gameplay rules from the official arcade games for certain song in the *<ruby>簡<rt>Kan</rt> 単<rt>tan</rt></ruby>/<ruby>か<rt>Ka</rt> ん<rt>n</rt> た<rt>ta</rt> ん<rt>n</rt></ruby>* Easy difficulty, where the amount of players is fixed to 1 and the inputs from all players are combined to play the song.

Reference: <https://taiko.namco-ch.net/taiko/en/howto/papamama.php#papamama>

*Unspecified*: The behavior when the amount of player-sides specified by [the `STYLE:` header](#style) is not 1.

***From***: TJAPlayer3-f v1.7.2.0

### #START / `#END`

***Scope***: per&ndash;player-side (enclosing the notechart definition), sequential

Respectively **start** / **end** the region of notechart definition.

* `#START`
  * The notechart definition is for the only player-side if [the `STYLE:` header](#style) is ignored or this header specifies the amount of player-sides to be 1.
* `#START <enum-str-player-side>` &mdash; TaikoJiro v1.99 but not TaikoJiro 2
  * The notechart definition is for the player-side specified by `<enum-str-combination>`, which can be one of:
    * `P1`, for the 1st player-side (1P).
    * `P2`, for the 2nd player-side (2P) if the amount of player-sides specified by [the `STYLE:` header](#style) ≥ 2.
  * *Unspecified*: The behavior when other `<enum-str-combination>` is used.
    * In TaikoJiro, using any other `<enum-str-combination>` is treated as if the 0-argument `#START` were used.
* *Proposal*: `#START P<positive-int-player-side>`
  * The notechart definition is for the `<positive-int-player-side>`-th player-side if the amount of player-sides specified by [the `STYLE:` header](#style) ≥ `<positive-int-player-side>`.
* `#END`

*Unspecified*: The behavior when any of the followings are violated when defining each difficulty:

* The 1-player-side notechart should be defined using the 0-argument `#START`
* Each multiple-player-side notechart should be defined using the 1-argument `#START <enum-str-player-side>` or *proposed* `P<positive-int-player-side>`.
* At most 1 definition should exist for each player-side of each amount of player-sides
  * In TaikoJiro 1, only the earliest definition is used when multiple such definitions exist.
* Every player-side notechart should be defined if any notecharts for the same amount of player-sides are defined, otherwise the 1-player-side notechart should be the earliest defined notechart.
* The 1-player-side notechart should be defined if any multiple-player-side notecharts are defined
  * *Proposal*: Make the 1-player-side in such case optional when each defined player-side notechart has all other player-side notecharts defined for the same amount of player-sides. The chosen 1-player-side notechart will be the notechart for an *unspecified* player-side.

***From***: TJF format \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TaikoJiro 1, the actual notechart-choosing behavior is one of:
  * | Set of `STYLE:1` definitions | `STYLE:2` `P1` & `P2` defined | Chosen `STYLE:1` 1P | Chosen `STYLE:2` 1P | Chosen `STYLE:2` 2P
    | --- | --- | --- | --- | ---
    | Is `P2`(s) | Yes & Yes | Empty <br /> Or (crash) when quit from the gameplay after switching from `STYLE:2` in the gameplay screen | Earliest defined `STYLE:2` `P1` | Earliest defined `STYLE:2` `P2`
    | Otherwise | Yes & Yes | Earliest defined non-`P2` `STYLE:1` (if any) <br /> Or empty | Earliest defined `STYLE:2` `P1` | Earliest defined `STYLE:2` `P2`
    | Contains `P2`(s) | Yes & No | Earliest defined non-`P2` `STYLE:1` (if any) <br /> Or empty | (Crash) | (Crash)
    | Otherwise | Yes & No | Earliest defined non-`P2` `STYLE:1` (if any) <br /> Or empty | Earliest defined `STYLE:2` `P1` | Any earliest defined
    | Contains `P1`(s) | No & Yes | Earliest defined non-`P2` `STYLE:1` | Empty | Earliest defined `STYLE:2` `P2`
    | Otherwise | No & Yes | Any earliest defined | Any earliest defined | Earliest defined `STYLE:2` `P2`
    | (Empty) | No & No | Empty | (Crash) | (Crash)
    | Contains `P1`(s) & `P2`(s) | No & No | Earliest defined non-`P2` `STYLE:1` | (Crash) | (Crash)
    | Otherwise, contains `P1`(s) | No & No | Earliest defined non-`P2` `STYLE:1` | Empty | Any earliest defined
    | Otherwise, contains `P2`(s) | No & No | Any earliest defined | (Crash) | (Crash)
    | Otherwise (is 0-argument `#START`(s)) | No & No | Any earliest defined | Any earliest defined | Any earliest defined

### #BPMCHANGE

***Scope***: branch, non-before, timing \
***Late effect scope***: all ([BMS scrolling modes](#bmscroll--hbscroll--nmscroll)); (none) (otherwise) \
***Effect target***: notes, bar lines

**Change** the **BPM**.

* `#BPMCHANGE <non-zero-float-bpm>`
  * A negative value results in "negative BPM" and causes the beat duration and the total note distance to be in the opposite sign. The behavior depend on [the `#MEASURE` command](#measure) used in conjunction.
    * See [The Measure-terminating Symbol and Timing](#the-measure-terminating-symbol-and-timing) for the behavior.
* `#BPMCHANGE 0`
  * The behavior is *unspecified* (may cause crashes in some existing simulators).
* Initial value: The BPM specified by [the `BPM:` header](#bpm).

***From***: TJF format \
***Supported by***: (Universally supported)

### #MEASURE

***Scope***: branch, measure non-before, timing \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines

Change the time signature / meter signature / **measure** signature.

* `#MEASURE <number-upper-numeral>/<non-zero-number-lower-numeral>`
  * > Formula: Amount of beats = 4 × `upper` / `lower`
  * The definition of beat is unaffected by the specified lower numeral. *Unspecified*: The decorative visual/audio effects.
  * The measure duration is determined only by the result of dividing the upper numeral by the lower numeral.
  * The lower numeral is conventionally fixed to be positive.
  * A negative measure duration causes the note objects to be positioned backward and can even cause them to overlap.
    * See [The Measure-terminating Symbol and Timing](#the-measure-terminating-symbol-and-timing) for the behavior.
* `#MEASURE <number-upper-numeral>/0`
  * The behavior is *unspecified* (may cause crashes in some existing simulators).
* *Proposal*: `#MEASURE <beats-measure>`
  * The `<enum-str-delay-type>` part of the [`beats`](#value-type) value ***MUST*** be `d` or (empty) and specifies whether the specified measure duration includes the time duration of the `#DELAY` commands.
* Initial value: `#MEASURE 4/4`

Replaced the TJF command `#ONESYOSETU` (adjust the duration of this **one *<ruby>小<rt>shou</rt> 節<rt>setsu</rt></ruby>*** "measure" to fit all note symbols on the following line if placed after the previous measure (if any) and before the first symbol of this measure in the notechart definition).

***From***: TaikoJiro \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TaikoJiro, for `<number-upper-numeral>`, only non-zero integers are supported. Zero-duration measures can be constructed using a large `<number-upper-numeral>` value due to the limited timing precision.

### #DELAY

***Scope***: branch, non-before, timing, sequential \
***Late effect scope***: all ([BMS scrolling modes](#bmscroll--hbscroll--nmscroll), positive value); (none) (otherwise) \
***Effect target***: notes, bar lines

Adjust (**delay**) the time position of all notechart object (including commands) non-preceding the `#DELAY` command by the specified time duration.

The decorative visual/audio effects are *unspecified*.

For the timing of notechart object, multiple `#DELAY` commands placed at the same beat position act as a single `#DELAY` with the value of the sum of their duration, even when negative delay durations are used.

*Unspecified*: The visual note positioning behavior in [BMS scrolling modes](#bmscroll--hbscroll--nmscroll) when note objects are placed into the time interval of positive delays.

* `#DELAY <non-zero-float-seconds-delay-duration>`
  * In TaikoJiro, when either `#BMSCROLL` or `#HBSCROLL` is used, the notechart stops scrolling for the specified duration even when notechart objects are placed into the stop duration by using negative delays.
  * A negative duration results in "negative delay" and can cause note objects to overlap.
    * See [The Measure-terminating Symbol and Timing](#the-measure-terminating-symbol-and-timing) for the behavior.
* `#DELAY 0`
  * No effects
* *Proposal*: `#DELAY <beats-time-duration>`
  * The specified time duration is the beat amount of `<beats-time-duration>` under the current BPM.
  * The `<enum-str-delay-type>` part of the [`beats`](#value-type) value ***MUST*** be `d` or (empty) and specifies whether the specified measure duration includes the time duration of the `#DELAY` commands with overlapping time interval.

***From***: TaikoJiro v1.60 \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TaikoJiro, delays with the absolute value of duration < 0.001 are treated as 0 due to limited timing precision.
* In TaikoJiro, when either `#BMSCROLL` or `#HBSCROLL` is used, delays with positive duration cause the notechart to stop scrolling for the specified duration even when notechart objects are placed into the stop duration by using negative delays.
* In TJAPlayer2 for PC, a negative delay value causes unintended behaviors. (?)

### `#GOGOSTART` / `#GOGOEND`

***Scope***: branch, non-before, scoring, sequential \
***Late effect scope***: notes: (none), gameplay screen: all \
***Effect target***: notes, gameplay screen

Respectively **start** / **end** a *<ruby>ゴー<rt>Goo</rt> ゴー<rt>Goo</rt> タ<rt>Ta</rt> イ<rt>i</rt> ム<rt>mu</rt></ruby>* **Go-Go** Time section if not already respectively started / ended.

*Unspecified*: The behavior if `#GOGOSTART` occurs when a Go-Go Time section has already started.

For playing the Go-Go Time entering effects during an existing Go-Go Time section, a pair of `#GOGOEND` and `#GOGOSTART` can be placed together.

***From***: TaikoJiro \
***Supported by***: (Universally supported)

### `#DUMMYSTART` / `#DUMMYEND`

***Scope***: branch, non-before, sequential \
***Late effect scope***: (none) \
***Effect target***: notes

Respectively **start** / **end** a fake/dummy section if not already respectively started / ended.

***From***: TaikoManyGimmicks

### #SCROLL

***Scope***: branch, measure non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines

Change the **scroll**ing speed of notes & bar lines, relative to the normal scrolling velocity and direction.

*Unspecified*: Whether the notes & the bar lines are rotated around their center accordingly when a complex number value is used.

Unlike the `#BPMCHANGE` command, the `#SCROLL` command is measure-scoped.

*Proposal*: Make the scope simply non-before.

* `#SCROLL <float-scroll-speed-x>`
* `#SCROLL <complex-ri-float-scroll-speed-xy>` &mdash; TaikoJiro 2 v0.97, TJAPlayer2 for PC
  * Complex-number&ndash;valued, modeled after the rectangular form of complex number: *x* ± *yi*
  * Notecharts with this type of command are usually referred as *<ruby>複<rt>Fuku</rt> 素<rt>so</rt> 数<rt>suu</rt> 譜<rt>fu</rt> 面<rt>men</rt></ruby>* "Complex number notechart".
  * The imaginary component of `<complex-ri-float-scroll-speed-xy>` specifies the vertical scrolling speed from the top to the bottom of the screen (↓). The unit is the same as `<float-scroll-speed-x>`.
* `#SCROLL 0`
  * The behavior is *unspecified*.
* *Proposal*: `#SCROLL <value>bpm`
  * Use the corresponding scrolling speed vector as when the absolute value (velocity) of `<value>` were used for `#BPMCHANGE` and the unit direction of `<value>` were used for `#SCROLL`.
  * > Formula: `scroll` = `value` / `current_bpm`
* `#SCROLL <float-scroll-speed>, <number-pixel-rotation-center-x>, <float-degrees-angle>` &mdash; TaikoManyGimmicks
  * Complex-number&ndash;valued, modeled after the polar form of complex number: *r*∠*φ*
  * Set the scrolling speed vector to `<float-scroll-speed>` rotated `<float-degrees-angle>` degrees (°) counterclockwise (↺) centered around the position `<number-pixel-rotation-center-x>` from the visual judgment position.
  * Can cause the per&ndash;note/bar line visual judgment position to move away from the judgment mark.
* Initial value: `#SCROLL 1` / `#SCROLL 1+0i` / (TaikoManyGimmicks) `#SCROLL 1, 0, 0`
  * The normal scrolling speed vectors. The notes & the bar lines travel through the whole note field in 4 beats when no BPM changes occur.

***From***: TaikoJiro \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TJAPlayer2 for PC and TJAPlayer3, the imaginary component of `<complex-ri-float-scroll-speed-xy>` specifies the vertical scrolling speed from the bottom to the top of the screen (↑) instead.
* In TJAPlayer2 for PC and TJAPlayer3, the imaginary component of `<complex-ri-float-scroll-speed-xy>` makes bar lines rotate around their center. However, it is misinterpreted as the amount of rotation and the unit is 90 degrees (°) clockwise (↻), see:
  * <https://github.com/kairera0467/TJAP2fPC/blob/17e5c3bea5ccd5eaae5367128ec209384e12e954/DTXManiaプロジェクト/コード/ステージ/07.演奏/ドラム画面/CStage演奏ドラム画面.cs#L2026>
  * <https://github.com/AioiLight/TJAPlayer3/blob/59835a522887c67b8db0e60d89a1e61ed3220742/TJAPlayer3/Stages/07.Game/Taiko/CStage演奏ドラム画面.cs#L2034>
  * This behavior is utilized in some existing notecharts to achieve bar line rotation. Exemplar notechart: <https://www.youtube.com/watch?v=SR94XPuGoyQ> <br />
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/SR94XPuGoyQ" title="YouTube video player, playing &quot;【TJAPlayer3】Sense【創作譜面】[BilliumMoto × Silentroom] 《ギミック譜面》&quot;, uploaded by かれーどらい{きつね}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  * The [`#ANGLE`](#note--barline-commands) command introduced in TaikoManyGimmicks can achieve such effects without depending on the *unspecified* behavior.

### `#BARLINESCROLL`

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: bar lines

Change the **scroll**ing speed of only **bar** **line**s, relative to the normal scrolling velocity and direction and prevent this speed from being overridden by further [`#SCROLL`](#scroll).

* `#BARLINESCROLL <non-negative-float-scroll-speed-x>`
* **`#BARLINESCROLL Off`** / `#BARLINESCROLL off` / `#BARLINESCROLL`
  * Reset the scrolling speed of bar lines to the scrolling speed of notes and allow this speed to be overridden by further [`#SCROLL`](#scroll).

***From***: taiko-web (plugin "Custom Barlines")

### *Proposal*: #SPEED

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: all \
***Effect target***: notes, bar lines

Suddenly change the base scrolling **speed** of notes & bar lines. In other words, suddenly change the normal scrolling velocity and direction.

Targeted notes & bar lines have their distance and/or direction to the visual judgment position scaled and/or rotated. The `<approach-specifier>` from the *proposal* [Command Modifier](#proposal-command-modifier) is intended to be used in conjunction.

If the notes & the bar lines are rotated around their center accordingly when a [`#SCROLL`](#scroll) command with complex number value is used, they are also rotated accordingly when a `#SPEED` command with complex number value is used.

* `#SPEED <float-base-speed-x>`
* `#SPEED <complex-ri-float-base-speed-xy>`
  * The imaginary component of `<complex-ri-float-base-speed-xy>` specifies the vertical normal scrolling speed from the top to the bottom of the screen (↓). The unit is the same as `<float-base-speed-x>`.
* `#SPEED <value>bpm`
  * Use the corresponding normal scrolling speed as when the absolute value (velocity) of `<value>` were used for `#BPMCHANGE`, the unit direction of `<value>` were used for `#SPEED`, and `#SCROLL 1` were used.
  * > Formula: `base_speed` = `value` / `current_bpm` / `current_scroll`
* `#SPEED <float-base-speed>, <number-pixel-rotation-center-x>, <float-degrees-angle>`
  * Set the normal scrolling velocity to `<float-base-speed>` and the normal scrolling direction to `<float-degrees-angle>` degrees (°) counterclockwise (↺) centered around the position `<number-pixel-rotation-center-x>` from the visual judgment position.
* Initial value: `#SPEED 1` / `#SPEED 1+0i` / `#SPEED 1, 0, 0`

### #DIRECTION

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines

Change the scrolling **direction** of notes & bar lines.

*Unspecified*: Whether the notes & the bar lines are rotated around their center accordingly.

*Unspecified*: The behavior when a [`#SCROLL` command](#scroll) with complex value is active.

*Proposal*: The direction is relative to the scrolling direction specified by [the `#SCROLL` command](#scroll).

* `#DIRECTION <enum-int-direction>`
  * `<enum-int-direction>` specifies the degrees (°) of the counterclockwise (↺) rotation and can be one of:
    * | | Rotation (degrees CCW) | Scrolling direction under `#SCROLL 1`
      | --- | --- | ---
      | `0` | 0° ↺/↻ (no changes) | ←
      | `1` | 90° ↺ | ↓
      | `2` | 270° ↺ (≡ 90° ↻) | ↑
      | `3` | 45° ↺ | ↙
      | `4` | 315° ↺ (≡ 45° ↻) | ↖
      | `5` | 180° ↺ (≡ 180° ↻) | →
      | `6` | 135° ↺ | ↘
      | `7` | 225° ↺ (≡ 135° ↻) | ↗
* *Proposal*: `#DIRECTION <number-degrees>deg`
  * `<number-degrees-rotation>` specifies the degrees (°) of the counterclockwise (↺) rotation.

***From***: TJAPlayer2 for PC

### `#BARLINEOFF` / `#BARLINEON`

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: bar lines

Respectively disable ("turn **off**") / enable ("turn **on**") the display of all **bar** **line**s (including the special bar lines indicating the beginning of a *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart **branch**"/forked path section) from the definition position and on.

***From***: TaikoJiro v2.69 \
***Supported by***: (Universally supported)

### `#BARLINE`

***Scope***: branch, beat interval one-shot, gimmicky \
***Late effect scope***: (none) \
***Effect target***: bar lines

Insert a fake/dummy normal **bar** **line** displayed at the head of the current beat position.

***From***: taiko-web (plugin "Custom Barlines") \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #JPOSSCROLL

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: all \
***Effect target***: notes, bar lines, judgment mark, note field

Move ("**scroll**") the **pos**ition of the **j**udgment circle from the current position.

*Unspecified*: The behavior when another `#JPOSSCROLL` command is placed within the moving duration interval of the current `#JPOSSCROLL` command.

The arguments are whitespace-separated.

* `#JPOSSCROLL <approach-duration-specifier> <distance-specifier> <direction-specifier>`
  * `<approach-duration-specifier>` can be one of:
    * `<positive-float-seconds-approach-duration>`
    * *Proposal*: `<beats-approach-duration>`
  * `<distance-specifier>` can be one of:
    * `<number-pixel-distance-x>`
    * `<complex-ri-number-pixel-distance-xy>` &mdash; TJAPlayer3 v1.6.x, OpenTaiko (0auBSQ) v0.6.0
      * The imaginary component of `<complex-ri-number-pixel-distance-xy>` specifies the vertical movement toward the top of the screen (↑).
    * `<number-distance-x-upper>/<number-distance-x-lower>` &mdash; TaikoManyGimmicks
      * Specify the horizontal movement to be `<number-distance-x-upper>/<number-distance-x-lower>` of the default note field width.
    * *Proposal*: `<value> deg <float-degrees-angle>`
      * Specify the moving vector as `<value>` rotated `<float-degrees-angle>` degrees (°) counterclockwise (↺).
    * `default` &mdash; TaikoManyGimmicks
      * Move the judgment mark to the default position.
  * `<direction-specifier>` can be one of:
    * (Empty) / `0`
      * Specify the moving direction as the scrolling direction if `<pixel-distance-specifier>` were the argument of [the `#SCROLL` command](#scroll) when the BPM is positive.
    * `1`
      * The moving direction is reversed (rotated 180 degrees (°) (counter)clockwise (↺/↻)).

***From***: TJAPlayer2 for PC

#### Compatibility Issues

* In TJAPlayer2 for PC and TJAPlayer3, the imaginary component of `<complex-ri-number-pixel-distance-xy>` specifies the vertical movement toward the bottom of the screen (↓) instead.

### #JUDGEDELAY

***Scope***: branch, non-after, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines

Specify the per&ndash;note/bar line visual **judgment** point to be offset ("**delay**") from the judgment mark.

Reset by [`#RESETCOMMAND`](#note--barline-commands) (?)

The arguments are whitespace-separated.

* `#JUDGEDELAY 0`
  * **0**-parameter form.
  * Reset the effects.
* `#JUDGEDELAY 1 <float-seconds-duration>`
  * **1**-parameter form.
  * Specify the visual judgment point to be visually `<float-seconds-duration>` before the judgment mark.
* `#JUDGEDELAY 2 <float-pixel-position-x> <float-pixel-position-y>`
  * **2**-parameter form.
  * Specify the visual judgment point to be the given position relative to the judgment mark.
* `#JUDGEDELAY 3 <float-seconds-duration> <float-pixel-position-x> <float-pixel-position-y>`
  * **3**-parameter form.
  * Specify the visual judgment point to be visually `<float-seconds-duration>` before the given position relative to the judgment mark.

***From***: TaikoManyGimmicks

### SUDDEN / HIDDEN Commands

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes

Make non-preceding notes and their *<ruby>口<rt>Kuchi</rt> 唱<rt>Shou</rt> 歌<rt>ga</rt></ruby>* "Note phoneticization" respectively appear and move **sudden**ly / disappear ("**hidden**") and stop moving suddenly.

The arguments are whitespace-separated.

* `#SUDDEN <float-milliseconds-appear-duration> <float-milliseconds-moving-duration>`
  * The "note phoneticization" is displayed/hidden along the note.
* *Proposal*: `#SUDDEN <float-milliseconds-appear-duration> <float-milliseconds-moving-duration> <enum-str-affected-type>`
  * See below.
* *Proposal*: `#HIDDEN <float-milliseconds-disappear-duration> <float-milliseconds-stopping-duration>`
  * The "note phoneticization" is displayed/hidden along the note.
* *Proposal*: `#HIDDEN <float-milliseconds-disappear-duration> <float-milliseconds-stopping-duration> <enum-str-affected-type>`
  * See below.
* Initial value: `#SUDDEN 0 0` & (*Proposal*) `#HIDDEN 0 0`

`<float-milliseconds-*-duration>` specifies the time durations (ms; 0.001s) before the time point of judgment is reached; if its absolute value equals to `0`, the time duration is positive infinity (+∞) for the `#SUDDEN` command and is negative infinity (−∞) for the `#HIDDEN` command.

*Proposal*: `<enum-str-afftect-type>` can be one of:

* `n` / `Doron` &mdash; Affect only the **n**otes, as in the ***<ruby>ド<rt>Do</rt> ロ<rt>ro</rt> ン<rt>n</rt></ruby>*** "**n**ote-wise stealth" game modifier.
* `t` &mdash; Affect only the "note phoneticization" ("the **t**exts on the lower note field").
* (empty) / `nt` / `Stealth` &ndash; Affect both the **n**ote & the "note phoneticization" ("**t**ext") ("(true) **stealth**").
* `b` &mdash; Affect only the **b**ar lines.
* `nb` &mdash; Affect both the **n**ote & the **b**ar lines.
* `ntb` / `All` &mdash; Affect all notechart objects.

***From***: TJAPlayer2 for PC

#### Compatibility Issues

* In TJAPlayer2 for PC, the per-note effect is only applied non-before the time position of [the `#START` command](#start--end). (?)

### #NOTESPAWN

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes

Specify the displaying ("**spawn**") duration of **note**s before the time point of judgment.

The arguments are whitespace-separated.

* `#NOTESPAWN 0`
  * Reset to the default.
* `#NOTESPAWN 1 <float-seconds-duration>`
  * Set the sudden point.
  * Equivalent to `#SUDDEN <float-milliseconds-duration> 0` after unit conversion.
* `#NOTESPAWN 2 <float-seconds-duration>`
  * Set the hidden point.
  * Equivalent to (*Proposal*) `#HIDDEN <float-milliseconds-duration> 0` after unit conversion.

***From***: TaikoManyGimmicks

### `#ENABLEDORON` / `#DISABLEDORON`

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: all \
***Effect target***: notes

Respectively **enable** / **disable** the ***<ruby>ド<rt>Do</rt> ロ<rt>ro</rt> ン<rt>n</rt></ruby>*** "note-wise stealth" game modifier. The *<ruby>口<rt>Kuchi</rt> 唱<rt>Shou</rt> 歌<rt>ga</rt></ruby>* "Note phoneticization" is not hidden by this game modifier.

***From***: TJAPlayer3-Extended \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #LYRIC

***Scope***: branch, non-before, decorative \
***Late effect scope***: all \
***Effect target***: gameplay screen

Display the specified **lyric**.

*Unspecified*: Whether `#LYRIC` commands are ignored if the lyric file specified by [the `LYRICS:` or `LYRICFILE:` header](#lyrics--lyricfile) is used.

* `#LYRIC <str-lyric>`
  * In taiko-web, a `\n` in `<str-lyric>` is displayed as a newline.

***From***: TJAPlayer2 for PC \
***Supported by***: taiko-web ver.20.03.31

#### Compatibility Issues

* In TJAPlayer2 for PC but not TJAPlayer3, the first whitespace in the middle of `<str-lyric>` terminators the loaded lyric.

### #SENOTECHANGE

***Scope***: branch, note one-shot, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes

Override ("**change**") the automatically assigned *<ruby>口<rt>Kuchi</rt> 唱<rt>Shou</rt> 歌<rt>ga</rt></ruby>* "**Note** phoneticization" ("**s**ound **e**ffect of a **note**" or "*<ruby>発<rt>Hatsu</rt> **声**<rt>**se**i</rt></ruby>* vocalization of a **note**" (?)) of the nearest note(s) placed non-before the command.

* `#SENOTECHANGE <enum-int-note-phoneticization>`
  * In `GAME:Taiko`, `<enum-int-note-phoneticization>` can be one of:
    * | | Note phoneticization | Designed for what note symbol
      | --- | --- | ---
      | `1` | *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>* Don | `1`
      | `2` | *<ruby>ド<rt>Do</rt></ruby>* Do | `1`
      | `3` | *<ruby>コ<rt>Ko</rt></ruby>* (Do) | `1`
      | `4` | *<ruby>カッ<rt>Ka'</rt></ruby>* Ka | `2`
      | `5` | *<ruby>カ<rt>Ka</rt></ruby>* (Ka) | `2`
      | `6` | *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）* DON | `3`
      | `7` | *<ruby>カッ<rt>Ka'</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）* KA | `4`
      | `8` | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>* Roll | note head of `5`
      | `9` | *ー* &ndash; | bar body of `5` & `6`
      | `10` | *ーっ!!* &ndash;!! | note end of `5` & `6`
      | `11` | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）* ROLL | note head of `6`
      | `12` | *<ruby>ふ <rt>Fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* Balloon | `7`
  * *Unspecified*: The behavior when an `<enum-int-note-phoneticization>` not designed for the applied note is used.
* *Proposal*: `#SENOTECHANGE <enum-str-note-phoneticization>`
  * `<enum-str-note-phoneticization>` can be one of:
    * `D`, the default, use the automatically assigned note phoneticization.
    * `L`, **l**ong:
      * In Taiko mode, use *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>* Don for note symbol `1` and *<ruby>カッ<rt>Ka'</rt></ruby>* Ka for note symbol `2`
      * In Konga mode, use <ruby>パン<rt>Pan</rt></ruby> for note symbol `1`, <ruby>ポン<rt>Pon</rt></ruby> for `2`, and <ruby>チャン<rt>Chan</rt></ruby> for `4`.
      * For bar drumroll notes, make the ending *ーっ!!* &ndash;!! displayed.
      * Otherwise the same as `D`.
    * `F`, **f**inal:
      * In Konga mode, use <ruby>パッ<rt>Pa'</rt></ruby> for note symbol `1`, <ruby>ポッ<rt>Po'</rt></ruby> for `2`, and <ruby>チャッ<rt>Cha'</rt></ruby> for `4`.
      * Otherwise the same as `L`.
    * `S`, **s**hort:
      * In Taiko mode, use *<ruby>ド<rt>Do</rt></ruby>* Do for note symbol `1` and <ruby>カ<rt>Ka</rt></ruby> (Ka) Ka for note symbol `2`
      * In Konga mode, use <ruby>パ<rt>Pa</rt></ruby> for note symbol `1`, <ruby>ポ<rt>Po</rt></ruby> for `2`, and <ruby>チャ<rt>Cha</rt></ruby> for `4`.
      * For bar drumroll notes, make the ending *ーっ!!* &ndash;!! hidden.
      * Otherwise the same as `D`.
    * `A`, **a**lternate:
      * In Taiko mode, use *<ruby>コ<rt>Ko</rt></ruby>* (Do) for note symbol `1`
      * Otherwise the same as `S`.
* *Proposal*: `#SENOTECHANGE <comma-separated-list-enum-note-phoneticization>`
  * All elements of `<comma-separated-list-enum-note-phoneticization>` are valid `<enum-int-note-phoneticization>` or `<enum-str-note-phoneticization>` and are iterated and applied to multiple notes in their definition order.
* *Proposal*: `#SENOTECHANGE <string-enum-str-note-phoneticization>`
  * All non-whitespace characters in `<string-enum-str-note-phoneticization>` are valid `<enum-str-note-phoneticization>` and are iterated and applied to multiple notes in their definition order.

In the official games, the note phoneticization is assigned per-note and does not follow a definite pattern, especially in earlier games.

The general pattern in recent Taiko games seems to be:

* The visual beat duration between `x` & `y` (`d_<x>_to_<y>` below) is used for determining the note phoneticization and is defined as `scroll` × `beat_duration_<x>_to_<y>` = `scroll_command` × `headscroll` × `beat_duration_<x>_to_<y>`.
* Both the head and end of drumroll-type notes are treated as ordinary notes for determining the note phoneticization.
* A note is "chain-final" when any of the followings are met (the "? / 3" factors are tentatively determined tolerance values):
  * `d_this_to_next_note` > 1/8th, the end of a chain before a pause.
  * `d_this_to_next_note` ≥ 4.0 / 3 × `d_this_to_previous_note`, the end of a chain before a short pause or a sparser chain.
  * `d_next_to_2nd_next_note` ≤ 2.0 / 3 × `d_this_to_next_note`, the end of a chain before a denser chain.
* The long form is avoided for notes in any of the following conditions ("non-long conditions"), to ensure the readability of note phoneticization:
  * `d_this_to_previous_note` \< 1/16th, to avoid the texts from overlapping.
  * `d_this_to_next_note` \< 1/8th, with `scroll` upper-limited to 1.0 for calculation, to avoid the text for a note from being extended below the next note.
* The alternate form is used for every even notes in a chain when all the followings are met for this chain:
  * Each of the previous chain & the next chain is either sparser than this chain or separated from this chain by a pause.
  * The chain contains only odd amount of notes of the same type (*i.e.*, using the same note symbol) and the same drumroll duration (if applicable).
  * The notes are spaced evenly in time duration.
  * The "chain-final" note of this chain does not meet any of the "non-long conditions".
  * The time duration between the first note & the last note ≤ 0.5 seconds.
* The long form is used for "chain-final" hit-type notes which do not meet any of the "non-long conditions".
* There is only one form for drumroll-type notes and applause notes in the official games: The short form had been used in earlier games until the long form was introduced in PS3-generation and has been used onward.
* The short form is used for all other notes and is preferred in other obscure cases.
* For notes near a non-forced branch point, the results of branching from and into each different branch are considered. The long or alternate form is used only if the same form would be used in all branch results, while the short form is used otherwise.

However, in the official Konga games, the general pattern is less consistent and "chain-final" is defined less strictly:

* Both the long and final forms can used for "chain-final" notes which do not meet any of the "non-long conditions".
* There is only one form for drumroll-type notes and applause notes in the official games: Only the short form has been used because all the Konga games were released before the PS3-generation of Taiko games.
* The short form is used otherwise.

***From***: TJAPlayer3 v1.4.0

### *Proposal*: #BALLOON (Command)

***Scope***: branch, note one-shot \
***Late effect scope***: (none) \
***Effect target***: balloon-type notes

Basically the same as the **[`BALLOON:`](#balloon-headers)** header, except that the `#BALLOON` command only applies to non-preceding notes in the note definition.

Override the assigned hit amount specified by the one of the BALLOON headers if applies to an already assigned balloon-type note.

* `#BALLOON <comma-separated-list-non-negative-int-amount-of-hits>`

The semantics are otherwise the same as the [BALLOON](#balloon-headers) headers.

### `#SECTION`

***Scope***: branch, instant one-shot \
***Late effect scope***: all (across branches) \
***Effect target***: (none)

Start a *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart branch"/forked path&ndash;determining **section** by resetting the value of the conditions for determining the next not-yet-determined "branch(es)"/path(s) at the beginning of the section. See the explanation for [the `#BRANCHSTART` command](#branchstart--branchend).

When the `#SECTION` command & a "branch"/path&ndash;determining point occur at the same beat position, the effect of the `#SECTION` command should take place after the "notechart branch"/forked path is determined.

The effects of `#SECTION` applie regardless the current branch and on which branch the command is defined.

An implicit `#SECTION` is placed at the beginning of every notechart definition.

*Unspecified*: Whether the value of the condition for determining the "branch"/path by score (`#BRANCHSTART s, <number-expert-branch-requirement>, <number-master-branch-requirement>`) is reset.

* `#SECTION`
* *Proposal*: `#SECTION <no-punctuation-str-name-section>`
  * Start a named "branch"/path determining section with the initial condition values.

***From***: TaikoJiro v1.63 \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TaikoJiro, the firing order between the `#SECTION` command and a "branch"/path&ndash;determining point is indeterminate when they occur at the same beat position.

### *Proposal*: #SECTIONRESUME / #SECTIONEND

***Scope***: branch, instant one-shot \
***Late effect scope***: all \
***Effect target***: (none)

**Resume**/**end** a *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart branch"/forked path&ndash;determining **section** by resuming/stopping updating the value of the conditions for determining the next not-yet-determined "branch(es)"/path(s) at the beginning of the section. See the explanation for [the `#BRANCHSTART` command](#branchstart--branchend).

This command can apply to only named "branch"/path-determining sections.

* *Proposal*: `#SECTIONRESUME <no-punctuation-str-name-section>`
* *Proposal*: `#SECTIONEND <no-punctuation-str-name-section>`

### `#LEVELHOLD`

***Scope***: branch, measure non-before \
***Late effect scope***: all \
***Effect target***: (none)

Override the result of all *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart **branch**"/forked path ("**level**") determination from the definition of this measure and on with the current branch/path ("**hold**").

*Proposal*: Its effects end at either the next another `#LEVELHOLD` or a [#LEVELREDIR](#proposal-levelredir) command.

* `#LEVELHOLD`
  * Override the determining result as the current "branch"/path.
  * *Proposal*: Equivalent to `#LEVELREDIR <enum-str-branch-current>, <enum-str-branch-current>, <enum-str-branch-current>`, where `<enum-str-branch-current>` represents the current "branch"/path.

***From***: TaikoJiro v1.63 \
***Supported by***: TaikoJiro 2, TJAPlayer2 for PC

### *Proposal*: #LEVELREDIR

***Scope***: branch, measure non-before \
***Late effect scope***: all \
***Effect target***: (none)

Override the result of all *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart **branch**"/forked path ("**level**") determination from the definition of this measure and on with specified branches/paths (**redir**ect).

Its effects end at either the next [`#LEVELHOLD`](#levelhold) or another #LEVELREDIR command.

* *Proposal*: `#LEVELREDIR <enum-str-branch-from-normal>, <enum-str-branch-from-expert>, <enum-str-branch-from-master>`
  * Override the determining result as respectively `<enum-str-branch-from-normal>` / `<enum-str-branch-from-expert>` / `<enum-str-branch-from-master>` when the default "branch"/path is determined to be respectively the ***<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>*** **N**ormal / ***<ruby>玄<rt>Kuro</rt> 人<rt>uto</rt></ruby>*** "Professional"/Advanced ("**E**xpert") / ***<ruby>達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>*** **M**aster "branch"/path. See the explanation of [the `#BRANCHSTART` command](#branchstart--branchend).
  * Example: The "branch"/path behavior of the *<ruby>お<rt>O</rt> に<rt>ni</rt></ruby>* Oni/Extreme difficulty of "<ruby>聖<rt>Shou</rt> 徳<rt>doku</rt> た<rt>Ta</rt> い<rt>i</rt> こ<rt>ko</rt> の<rt>no</rt>「<rt></rt> 日<rt>Hi</rt> い<rt>I</rt> ず<rt>zu</rt> る<rt>ru</rt> ま<rt>ma</rt> で<rt>de</rt> 飛鳥<rt>Asuka</rt>」</ruby>" can be achieved using:

    ```txt
    // Measure 15 - 16

    #BRANCHSTART r, 5, 6
    #N
        #LEVELHOLD
    #M
        #LEVELREDIR N, N, M
    #BRANCHEND
    #SECTION
    // Measure 17 - 18

    #BRANCHSTART r, 7, 8
    #N
        #LEVELHOLD
    #M
        #LEVELREDIR N, N, M
    #BRANCHEND
    #SECTION
    // Measure 19 - 20

    #BRANCHSTART r, 4, 5
    #N
      // Measure 21 - 25
    #E
      // Measure 21 - 25
    #M
      // Measure 21 - 25

    #BRANCHSTART p, 101, 101
    #BRANCHEND
    // Measure 26 -
    ```

    * Reference: <https://wikiwiki.jp/taiko-fumen/収録曲/おに/聖徳たいこの%E3%80%8C日いずるまで飛鳥%E3%80%8D>
* *Proposal*: Initial value: `#LEVELREDIR N, E, M`

### #BRANCHSTART / `#BRANCHEND`

***Scope***: notechart, measure non-before, sequential \
***Late effect scope***: notes, bar lines, & judgment mark(s): non-before, note field(s): non-before the previous measure (`#BRANCHSTART`) or (none) (`#BRANCHEND`) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

Respectively **start** / **end** the definition of a *<ruby>譜<rt>fu</rt> 面<rt>men</rt> 分<rt>bun</rt> 岐<rt>ki</rt></ruby>* "notechart **branch**"/forked path section.

The determining point of this "branch"/path section is defaulted to be placed at the beginning of the previous measure from the `#BRANCHSTART` command.

At the determining point, the "branch"/path&ndash;switching effects are played but the current "branch"/path is not changed until the actual beginning of the "branch"/path section.

* `#BRANCHSTART <enum-str-condition>, <number-expert-branch-requirement>, <number-master-branch-requirement>`
* *Proposal*: `#BRANCHSTART <enum-str-condition>, <number-expert-branch-requirement>, <number-master-branch-requirement>, <no-punctuation-str-name-section>`
  * Use the condition values from the specified named "branch"/path determining section. See [#SECTION](#section).
* *Proposal*: `#BRANCHSTART <enum-str-combination>, <comma-separated-list-requirements>`
  * Use the combined result of determining branch/path by each specified requirements.
  * `<comma-separated-list-requirements>` can be a certain number of argument combinations, each takes a form listed above (including this `<enum-str-combination>` form).
  * `<enum-str-combination>` can be one of:
    * `max`: Requires 2 argument combinations. Use the higher ("**max**imum") determined "branch"/fork.
    * `min`: Requires 2 argument combinations. Use the lower ("**min**imum") determined "branch"/fork.
    * `rev`: Requires 1 argument combination. Flip ("**rev**erse") the determined "branch"/fork. (*i.e.*, the *<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>* Normal and the *<ruby>達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>* Master "branches"/paths are swapped for the result of determining)
* `#BRANCHEND` &mdash; TaikoJiro, TJAPlayer 2 for PC ver.2020031800, TJAPlayer3 v1.5.2, taiko-web

The "branch"/path is determined by a condition value when `<enum-str-condition>` is...

* `r`, accumulated amount of hits on bar drum**r**oll notes during the determining section.
  * If a bar drumroll note is defined as beginning non-after but ending after the default beat position of the determining point, the actual determining point is postponed until the earlier of the definition positions of the ending of that note and an *unspecified* duration before the `#BRANCHSTART` command.
    * TaikoJiro: zero-duration.
    * TJAPlayer2 for PC and TJAPlayer3: 1 measure (i.e., not postponed).
    * *Proposed*: **min**{**min**{4 × 60 / bpm / scroll **at** the first note symbol after the `#BRANCHSTART` command (unit: second)}, 1 measure}.
* *Proposal*: `rt`, accumulated amount of hits on all (**t**otal) drum**r**oll-**t**ype notes during the determining section. The postponed-determining behavior of the `r` condition applies.
* `p`, the percentage (%) of *<ruby>精<rt>sei</rt> 度<rt>do</rt></ruby>* "**p**recision/**p**erfect rate"/accuracy during the determining section.
  * > Formula: (*<ruby>良<rt>Ryou</rt></ruby>* GREAT/Good + 0.5 × *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK) / **max**{*<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD + *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK + *<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, 1} × 100(%) (Unit of variables: Amount of judgment results)
* *Proposal*: `pp`, the **p**ercentage (%) of *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") during the determining section.
* *Proposal*: `ph`, the **p**ercentage (%) of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, **h**it-type note **h**its during the determining section.
* *Proposal*: `pm`, **p**ercentage (%) of *avoided* bomb/**m**ine notes during the determining section.
* *Proposal*: `pa`, **p**ercentage (%) of caught _**A**d libitum_ (**A**D-LIB) notes during the determining section.
* `d`, the percentage (%) of "precision"/accuracy of big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section. (**`d`** can be seen as a rotated `p`) &mdash; TJAPlayer2 for PC
  * Defined but unimplemented in TJAPlayer2 for PC
* *Proposal*: `dp`, the percentage (%) of *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* *Proposal*: `dh`, the percentage (%) of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, **h**it-type note **h**its on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* `b`, the percentage (%) of "precision"/accuracy of *<ruby>特 <rt>Toku</rt></ruby>* "special"/strong judgments on **b**ig (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
  * > Formula: (*<ruby>特 <rt>Toku</rt></ruby>* "special"/strong *<ruby>良<rt>Ryou</rt></ruby>* GREAT/Good + 0.5 × *<ruby>特 <rt>Toku</rt></ruby>* "special"/strong *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK) / **max**{amount of big hit-type notes, 1} × 100(%)
* *Proposal*: `bp`, the percentage (%) of *<ruby>特 <rt>Toku</rt></ruby>* "special"/strong *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* *Proposal*: `bh`, the percentage (%) of *<ruby>特 <rt>Toku</rt></ruby>* "special"/strong judgments on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* *Proposal*: `br`, accumulated amount of *strong* hits on **b**ig bar drum**r**oll notes during the determining section. The postponed-determining behavior of the `r` condition applies.
* *Proposal*: `h`, amount of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, non-blank **h**its during the determining section.
  * > Formula: `h` = `hh` + `rt`
* *Proposal*: `hh`, amount of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, hit-type note **h**its during the determining section.
  * > Formula: `hh` = *<ruby>良<rt>Ryou</rt></ruby>* GREAT/Good + *<ruby>可<rt>Ka</rt></ruby>* GOOD/OK
* *Proposal*: `hp`, amount (**h**its) of *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") during the determining section.
* *Proposal*: `am`, amount of _**a**voided_ bomb/**m**ine notes during the determining section.
* *Proposal*: `ha`, amount of caught ("**h**it") _**A**d libitum_ (**A**D-LIB) notes during the determining section.
* *Proposal*: `hdp`, amount of *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* *Proposal*: `hdh`, amount of non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD, **h**it-type note **h**its on big (<ruby>**大**<rt>**d**ai</rt></ruby>) notes during the determining section.
* *Proposal*: `hb`, amount of *strong* **h**its on all **b**ig notes during the determining section. (**`b`** can be seen as an `h` with rounded bottom)
  * > Formula: `hb` = `hbh` + `br`
* *Proposal*: `hbp`, amount ("hits") of *strong* *<ruby>良<rt>Ryou</rt></ruby>* GREAT/GOOD ("**p**erfect") on **b**ig notes during the determining section.
* *Proposal*: `hbh`, amount ("**h**its") of *strong* non-*<ruby>不<rt>Fu</rt> 可<rt>ka</rt></ruby>* BAD ("**h**it") on **b**ig notes during the determining section.
* `s`, the total **s**core points if (*proposed*) `<no-punctuation-str-name-section>` is not specified or otherwise (*proposed*) accumulated **s**core points during the specified named determining section. &mdash; TaikoJiro v2.66
  * *Unspecified*: The behavior when either unsupported scoring mode or the default value is specified to [the `SCOREMODE:` header](#scoremode) or the *<ruby>真<rt>Shin'</rt> 打<rt>uchi</rt></ruby>* "true performance" option is enabled.
* *Proposal*: `g`, percentage (%) of *<ruby>魂<rt>tamashii</rt> **ゲー**<rt>**g**ee</rt>ジ<rt>ji</rt></ruby>* spirit **g**auge/soul **g**auge change during the determining section, −100 ≤ `g` ≤ 100
* *Proposal*: `c`, the maximum/longest **c**ombo during the determining section (counted from 0).
* *Proposal*: `?`, a uniform distribution random value (float), 0 ≤ `?` \< 100

If the condition value...

* ≥ `<number-master-branch-requirement>`: The *<ruby>達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>* Master "branch"/path will be taken by default.
* Otherwise, ≥ `<number-expert-branch-requirement>`: The *<ruby>玄<rt>Kuro</rt> 人<rt>uto</rt></ruby>* "Professional"/Advanced ("Expert") "branch"/path will be taken by default.
* Otherwise: The *<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>* Normal "branch"/path is taken by default.
* The value of the requirements can be set out-of-bound to force a "branch"/path to be taken by default.
* The [`#LEVELHOLD`](#levelhold) command affects the final determining result.

They are conventionally used as follow:

```txt
#BRANCHSTART r, 1, 2 // Exemplar branch/path condition similar to the opening section of the "画竜点睛 (Garyoutensei)" series
#N
    // 0 hits: "普通 (Futsuu)" Normal branch/path
    // Normal branch/path section

#E
    // 1 hit: "玄人 (Kurouto)"/Advanced branch/path
    // Advanced branch/path section

#M
    // 2+ hits: "達人 (Tatsujin)"/Master branch/path
    // Master branch/path section

#BRANCHEND // Sometimes optional, see below

// Some commands or notechart section

#BRANCHSTART p, 0, 101 // Exemplar condition which forces the "玄人 (Kurouto)"/Advanced branch/path to be chosen
// ...
```

An implicit `#BRANCHEND` is placed before `#BRANCHSTART` and [`#END`](#start--end) commands. If no commands & notechart symbols occur after the explicit defined `#BRANCHEND` and before such commands, the `#BRANCHEND` can be omitted.

*Unspecified*: The behavior when any of the followings are violated:

* No commands should be placed after a branchless measure or `#BRANCHEND` and before the `#BRANCHSTART` command.
* No drumroll-type notes should be defined as starting before and ending non-before the beginning or the end of the "branch"/path section.
  * In TaikoJiro 1, such notes are handled as if the "branches"/paths were independent notecharts. However, the visual appearance of such bar drumroll notes become broken when the note head in the target "branch"/paths is no longer drawn when switching the "branch"/paths.

***From***: TaikoJiro v1.63 \
***Supported by***: (Universally supported)

### `#N` / `#E` / `#M`

***Scope***: notechart, measure non-before \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

Start the definition of respectively the ***<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>*** **N**ormal / ***<ruby>玄<rt>Kuro</rt> 人<rt>uto</rt></ruby>*** "Professional"/Advanced ("**E**xpert") / ***<ruby>達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>*** **M**aster *<ruby>譜<rt>fu</rt> 面<rt>men</rt></ruby> (<ruby>分<rt>bun</rt> 岐<rt>ki</rt></ruby>)* "notechart branch"/forked path section.

The definition of unused "branches"/paths due to forced "branch"/path determination can be omitted.

*Unspecified*: The behavior when any of the followings are violated:

* No ordinary notechart sections should be placed after [the `#BRANCHSTART` command](#branchstart--branchend) and before any of the `#N` / `#E` / `#M` commands.
* All `#N` / `#E` / `#M` commands should be placed within the region enclosed by the `#BRANCHSTART` & (possibly implicit) `#BRANCHEND` commands.
* Definitions should appear in the `#N` / `#E` / `#M` order if defined.
  * In TaikoJiro: Not required.
* At least one definition should exist for any "branch"/path.
  * In TaikoJiro: Not required; an empty "branch"/path section is allowed.
* At most one definition should exist for a particular "branch"/path.
  * In TaikoJiro: The lastly occurring definition is taken.
  * All timing commands should be consistent among all the defined "branches"/paths.
* The amount of measures and their total time duration should be consistent among all of the defined "branches"/paths.
  * In TaikoJiro: The first occurring definition determines the timing settings & amount of measures and all definitions are blank-filled to that amount of measures with that timing settings; any definition with a larger amount of measures or inconsistent timing settings causes unintended behaviors.
* The final effects of non-before&ndash;scoped gimmicky commands should be consistent among all the "branches"/paths, except when the "branch"/path section ends non-before the end of the notechart.
  * In TaikoJiro 1, such cases are handled as if the "branches"/paths were independent notecharts.

***From***: TaikoJiro v1.63 \
***Supported by***: (Universally supported)

### *Proposal*: `#LAYERSTART` / `#LAYEREND`

***Scope***: notechart, non-before, sequential \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

Respectively **start** / **end** the definition of a layer section. All layers in a layer section occur simultaneously and all branch-scoped commands not targeting the gameplay screen are applied separately for each layer.

They can be used as follow:

```txt
#LAYERSTART
#LAYER // Optional
    // Default layer section

#LAYER A
    // Layer A section

#LAYEREND // Sometimes optional, see below
```

An implicit `#LAYEREND` is placed before `#LAYERSTART` & [`#END`](#start--end) commands. If no commands & notechart symbols occur after the explicit defined `#LAYEREND` and before such commands, the `#LAYEREND` can be omitted.

*Unspecified*: The behavior when [the `#BRANCHSTART` commands, `#BRANCHEND`](#branchstart--branchend), [`#N`, `#E`, `#M`](#n--e--m) are placed within the layer section definition.

### *Proposal*: #LAYER

***Scope***: notechart, non-before \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

Start the definition of a layer of the layer section. A layer can span over multiple layer sections.

* `#LAYER <no-punctuation-str-name-layer>`
* `#LAYER` / `#LAYER default`
  * Start the definition of the default layer.

*Unspecified*: The behavior when any of the followings are violated:

* All #LAYER commands should be placed within the region enclosed by the `#LAYERSTART` & (possibly implicit) `#LAYEREND` commands.
* At most one definition should exist for a layer.
* The amount of measures and their total time duration should be consistent among all of the defined layers.

### *Proposal*: #LAYERORDER

***Scope***: branch, non-before \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

Specify the draw **order** of this **layer** relative to other layers in the current layer section for the notes & bar lines non-before the current beat position and the judgment mark(s) & note field(s) (if any) for this layer.

* `#LAYERORDER <int-layer-relative-draw-order>`
  * Specify the draw order relative to other layers in the current layer section (default: 0). Notes from a layer with a more positive number are drawn above the notes from layers with less positive draw orders. Notes outsides the current layer section are not affected.
* Initial value: `#LAYERORDER 0`

### #NEXTSONG

***Scope***: notechart, non-before \
***Late effect scope***: all \
***Effect target***: all

Switch to the **next song** in the *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode".

*<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode" resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games.

Used in conjunction with [`COURSE:Dan`](#course).

See [TJC Header](#tjc-header) for the header version of the `#NEXTSONG` command.

* `#NEXTSONG <string-song-title>,<string-song-subtitle>, <str-genre>,<string-filepath-song-wave>, <non-negative-int-score-init>, <non-negative-int-score-diff>`
  * Basically has the effects of the [`TITLE:`](#title-headers), [`SUBTITLE:`](#subtitle-headers), [`GENRE:`](#genre), [`WAVE:`](#wave), [`SCOREINIT:`](#scoreinit), and [`SCOREDIFF:`](#scorediff) headers combined, except that every comma (`,`) in each `string` values ***MUST*** be escaped as `\,`
* `#NEXTSONG <string-song-title>,<string-song-subtitle>, <str-genre>,<string-filepath-song-wave>, <non-negative-int-score-init>, <non-negative-int-score-diff>,<non-negative-number-level>, <enum-course>, <enum-bool-hide-title>` &mdash; TJAPlayer3-Develop-ReWrite, OpenTaiko (0auBSQ)
  * `<non-negative-number-level>, <enum-course>, <enum-bool-hide-title>` are optional parameters where the last one(s) can be omitted:
    * `<enum-bool-hide-title>` defaults to `False` and specifies whether the title of the song is obscured ("hidden") in the certification challenge selection screen of the *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 認<rt>nin</rt> 定<rt>tei</rt> モー<rt>Moo</rt> ド<rt>do</rt></ruby>* "Rank Certification Mode", which resembles *<ruby>段<rt>Dan'</rt> 位<rt>i</rt> 道<rt>Dou</rt> 場<rt>jou</rt></ruby>* "Rank Dojo"/Dan-i Dojo in the official games. If given, it can be one of:
      * `False`, the default; the title is displayed as-is.
      * `True`, the title is obscured (*e.g.*, displayed as "`???`").
    * `<enum-course>` has the effects and the default value of [the `COURSE:` header](#course).
    * `<non-negative-number-level>` has the effects and the default value of [the `LEVEL:` header](#level).

***From***: TJAPlayer3 v1.5.0

### #GAMETYPE

***Scope***: branch, non-before \
***Late effect scope***: (none) (?) \
***Effect target***: notes, bar lines

Specify the **game** mode ("**type**") for the notes non-before the current beat position. The meaning of the note symbols non-before the current beat position is changed accordingly; see [TJA Notechart Definition](#tja-notechart-definition).

*Unspecified*: The implemented game modes other than Taiko mode and Konga mode.

See [the `GAME:` header](#game) for specifying the initial game mode for the notechart.

* `#GAMETYPE Taiko`
  * A game mode similar to *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> の<rt>no</rt> 達<rt>Tatsu</rt> 人<rt>jin</rt></ruby>*, developed by Namco (now Bandai Namco)
  * See [Note Symbols in Taiko Mode](#note-symbols-in-taiko-mode)
* `#GAMETYPE Konga` / `#GAMETYPE Bongo`
  * A game mode similar to *Donkey Konga*, developed by Namco
  * See [Note Symbols in Konga Mode](#note-symbols-in-konga-mode)
* Initial value: The game mode specified by [the `GAME:` header](#game) (not supported by OpenTaiko (0auBSQ))

***From***: OpenTaiko (0auBSQ) v0.6.0

### NOTE / BARLINE Commands

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines

Manipulate the display properties of **note**s & **bar** **line**s.

The arguments are whitespace-separated.

Resetters:

* `#RESETCOMMAND`
  * **Reset** the effects of gimmicky commands to their default value, including NOTE / BARLINE commands, [the `#JUDGEDELAY` command](#judgedelay), [the `#NOTESPAWN` command](#notespawn), & [the `#GRADATION` command](#gradation).

Setters:

* `#SIZE <unsigned-number-scale>`
  * Specify the scaling ("**size**") of notes.
* `#BARLINESIZE <unsigned-number-pixel-thickness> <unsigned-number-pixel-height>`
  * Specify the **size** of **bar** **line**s.
* `#ANGLE <number-degrees-rotation>`
  * Specify the per-object rotation ("**angle**") of notes & bar lines to be `<number-degrees-rotation>` degrees (°) counterclockwise (↺).
* `#ALPHA <unsigned-number-8bit-a>`
  * Specify the opacity ("**α** channel"/"**alpha** channel") of notes.
* `#COLOR <unsigned-number-8bit-r> <unsigned-number-8bit-g> <unsigned-number-8bit-b> <unsigned-number-8bit-a>`
  * Specify the **color** of bar lines.

***From***: TaikoManyGimmicks

### #GRADATION

***Scope***: branch, non-before, gimmicky, sequential \
***Late effect scope***: non-before \
***Effect target***: notes, bar lines

Control the commands apply to the starting/ending of the per&ndash;note/bar line approaching phase ("**gradation**").

The arguments are whitespace-separated.

* `#GRADATION init`
  * Stop applying effects specified by the `#GRADATION` command to non-preceding notes and bar lines.
* `#GRADATION start <float-seconds-approach-duration> <enum-int-easing-points> <enum-int-easing-function>`
  * Make the following commands apply to the beginning ("**start**") of the approaching phase and specify the time duration and easing property of the approaching phase.
  * `<enum-int-easing-points>` can be one of:
    * `0` &mdash; EaseIn
    * `1` &mdash; EaseOut
    * `2` &mdash; EaseInOut
  * `<enum-int-easing-function>` can be one of:
    * `0` &mdash; Linear
    * `1` &mdash; Sine
    * `2` &mdash; Quadratic
    * `3` &mdash; Cubic
    * `4` &mdash; Quartic
    * `5` &mdash; Quintic
    * `6` &mdash; Exponential
    * `7` &mdash; Circular
    * `8` &mdash; Back
    * `9` &mdash; Elastic
    * `10` &mdash; Bounce
  * See <https://easings.net/> for a visual preview and the actual equation.
* `#GRADATION end`
  * Make the following commands apply to the **end**ing of the approaching phase.
  * Each commands appear after `#GRADATION start <float-seconds-approach-duration> <enum-int-easing-points> <enum-int-easing-function>` are specified again with a possibly different value here.

They are conventionally used as follow:

```tja
#GRADATION start 1 0 0 // Exemplar
#SIZE 1 // Exemplar command with the value before approaching
// More commands with the values before approaching
#GRADATION end
#SIZE 2 // Exemplar command with the value after approaching
// More commands with the values after approaching
// Notechart section
#GRADATION init // Optional sometimes
```

*Unspecified*: Which commands support the `#GRADATION` command.

Commands supporting the `#GRADATION` command in TaikoManyGimmicks:

* [The `#SCROLL` command](#scroll)
* [The `#JUDGEDELAY` command](#judgedelay)
* [The `#SIZE`, `#COLOR`, & `#ANGLE` commands](#note--barline-commands)

***From***: TaikoManyGimmicks

### #INCLUDE

***Scope***: branch (?), (depending on included notechart definition content) \
***Late effect scope***: (depending on included notechart definition content) \
***Effect target***: (depending on included notechart definition content)

Append ("**include**") the notechart definition content defined the included file to the current definition. The included file can have any headers and commands (except for the [`#START` and `#END` commands](#start--end) (?)) in either the TJA (?) or the TMG format.

* `#INCLUDE <string-filepath-notechart-definition>`

***From***: TaikoManyGimmicks

### `#SPLITLANE` / `#MERGELANE`

***Scope***: branch, non-before \
***Late effect scope***: all \
***Effect target***: notes, bar lines, judgment mark(s), note field(s)

**Split**/**merge** the note field ("**lane**") into/from top and bottom note field, with <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> notes on the top note field, <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> notes on the bottom note field, and other notes on the middle of these 2 note fields.

* `#SPLITLANE` / (*Proposed*) `#SPLITLANE 1`
* *Proposal*: `#SPLITLANE <float-split-amount>`
  * Specify the split amount, 1 for `#SPLITLANE` & 0 for `#MERGELANE`. A negative split amount makes <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> notes on the bottom note field and <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> notes on the top note field intead.
* Initial value / `#MERGELANE` / (*Proposed*) `#SPLITLANE 0`

***From***: OpenTaiko (0auBSQ) v0.6.0

### OBJ / CAM Commands

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: all \
***Effect target***: gameplay screen

Manipulate texture **obj**ects & the game screen **cam**ara.

Loader & unloader:

* `#ADDOBJECT <str-name-object>, <number-pixel-x>, <number-pixel-y>,<string-filepath-texture>`
* `#REMOVEOBJECT <str-name-object>`

Display property setters:

* `<number-pixel-x>`
  * `#OBJX <str-name-object>, <number-pixel-x-end>`
  * `#OBJHMOVESTART <str-name-object>, <number-pixel-x-start>, <number-pixel-x-end>, <enum-str-easing-points>, <enum-str-easying-function>`
  * `#OBJHMOVEEND`
* `<number-pixel-y>`
  * `#OBJY <str-name-object>, <number-pixel-y-end>`
  * `#OBJVMOVESTART <str-name-object>, <number-pixel-y-start>, <number-pixel-y-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#OBJVMOVEEND`
* `<float-scale-x>`
  * `#OBJHSCALE <str-name-object>, <float-scale-x-end>`
  * `#OBJHSCALESTART <str-name-object>, <float-scale-x-start>, <float-scale-x-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#OBJHSCALEEND`
* `<float-scale-y>`
  * `#OBJVSCALE <str-name-object>, <float-scale-y-end>`
  * `#OBJVSCALESTART <str-name-object>, <float-scale-y-start>, <float-scale-y-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#OBJVSCALEEND`
* `<number-degrees-rotation>`
  * `#OBJROTATION <str-name-object>, <number-degrees-rotation-end>`
  * `#OBJROTATIONSTART <str-name-object>, <number-degrees-rotation-start>, <number-degrees-rotation-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#OBJROTATIONEND`
* `<unsigned-number-8bit-opacity>`
  * `#OBJOPACITY <str-name-object>, <unsigned-number-8bit-opacity-end>`
  * `#OBJOPACITYSTART <str-name-object>, <unsigned-number-8bit-opacity-start> <unsigned-number-8bit-opacity-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#OBJOPACITYEND`
* `<unsigned-number-8bit-*>`
  * `#OBJCOLOR <str-name-object>, <unsigned-number-8bit-r-end>, <unsigned-number-8bit-g-end>, <unsigned-number-8bit-b-end>`

Frame-based animation:

* `#OBJANIMSTART <str-name-object>, <positive-number-milliseconds-frame-duration>`
* `#OBJANIMSTARTLOOP <str-name-object>, <positive-number-milliseconds-frame-duration>`
* `#OBJANIMEND <str-name-object>`
* `#OBJFRAME <str-name-object>, <unsigned-int-frame-index>`

CAM commands:

* `#CAMRESET`
* `<number-pixel-x>`
  * `#CAMHOFFSET <number-pixel-x-end>`
  * `#CAMHMOVESTART <number-pixel-x-start>, <number-pixel-x-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#CAMHMOVEEND`
* `<number-pixel-y>`
  * `#CAMVOFFSET <number-pixel-y-end>`
  * `#CAMVMOVESTART <number-pixel-y-start>, <number-pixel-y-end>, <enum-str-easing-points>, <enum-str-easying-function>`
  * `#CAMVMOVEEND`
* `<float-zoom-factor>`
  * `#CAMZOOM <float-zoom-factor-end>`
  * `#CAMZOOMSTART <float-zoom-factor-start>, <float-zoom-factor-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#CAMZOOMEND`
* `<float-scale-x>`
  * `#CAMHSCALE <float-scale-x-end>`
  * `#CAMHSCALESTART <float-scale-x-start>, <float-scale-x-end>, <enum-str-easing-type>, <enum-str-easing-function>`
  * `#CAMHSCALEEND`
* `<float-scale-y>`
  * `#CAMVSCALE <float-scale-y-end>`
  * `#CAMVSCALESTART <float-scale-y-start>, <float-scale-y-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#CAMVSCALEEND`
* `<number-degrees-rotation>`
  * `#CAMROTATION <number-degrees-rotation-end>`
  * `#CAMROTATIONSTART <number-degrees-rotation-start>, <number-degrees-rotation-end>, <enum-str-easing-points>, <enum-str-easing-function>`
  * `#CAMROTATIONEND`

The approach phase of a `#<property>START` command starts at its definition position and is ended by the nearest non-preceding corresponding `#<property>END` in notechart definition. *Unspecified*: The behavior when a `#<property>START` command either has no such corresponding `#<property>END` or has such `#<property>END` with an earlier time position than the `#<property>START` command itself.

`<enum-str-easing-points>` can be one of:

* `IN`
* `OUT`
* `IN_OUT`

`<enum-str-easing-function>` can be one of:

* `CUBIC`
* `QUARTIC`
* `QUINTIC`
* `SINUSOIDAL`
* `EXPONENTIAL`
* `CIRCULAR`
* `LINEAR`

***From***: TJAPlayer3-Extended \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #BORDERCOLOR

***Scope***: branch, non-before, decorative \
***Late effect scope***: all \
***Effect target***: gameplay screen

Set the **color** of the displayed region outside the **border** of the gameplay screen (when the gameplay screen camera is manipulated).

* `#BORDERCOLOR <unsigned-number-8bit-r>, <unsigned-number-8bit-g>, <unsigned-number-8bit-b>`

***From***: TJAPlayer3-Extended \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #CHANGETEXTURE / #RESETTEXTURE

***Scope***: branch, non-before, decorative \
***Late effect scope***: all \
***Effect target***: gameplay screen

Respectively **change** / restore ("**reset**") the texture used in the current skin.

* `#CHANGETEXTURE <string-filepath-original>,<string-filepath-replacing>`
* `#RESETTEXTURE <string-filepath-original>`

***From***: TJAPlayer3-Extended \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #SETCONFIG

***Scope***: branch, non-before, gimmicky \
***Late effect scope***: all \
***Effect target***: gameplay screen

Override ("**set**") the **config** value read from the `SkinConfig.ini` of the currently used skin.

*Unspecified*: The exact list of valid configs, allowed values, and the behaviors.

* `#SETCONFIG <str-config-key>=<text-config-value>`

***From***: TJAPlayer3-Extended \
***Supported by***: OpenTaiko (0auBSQ) v0.6.0

### #BGAON / #BGAOFF

***Scope***: branch, non-before, decorative \
***Late effect scope***: all \
***Effect target***: gameplay screen

Start ("**on**")/stop ("**off**") playing the specified **b**ack**g**round video ("**a**nimation") defined by [the `BGA:` header](#bga) on the gameplay screen.

The arguments are whitespace-separated.

* `#BGAON <unsigned-int-video-index> <float-milliseconds-video-offset>`
  * Start playing the specified background video from `<float-milliseconds-video-offset>` milliseconds into the video. The background video specified by [`BGMOVIE:`](#bgmovie) (if any) is hidden but is still playing.
* `#BGAOFF <unsigned-int-video-index>`
  * Stop the specified backgound video. The background video specified by [`BGMOVIE:`](#bgmovie) (if any) is shown and is still playing.

***From***: OpenTaiko (0auBSQ) v0.6.0

#### Compatibility Issues

* In OpenTaiko (0auBSQ) v0.6.0:
  * Only the halfwidth space ("` `") is allowed for separating arguments
  * `<unsigned-int-video-index>` must be exactly 2 decimal digits (with `0` prefixed if necessary).

### *Proposal*: #LUAMOD

***Scope***: branch, timing (intended; depending on usage) \
***Late effect scope***: (none) \
***Effect target***: notes, bar lines (intended; depending on usage)

Execute the given **Lua** code with predefined variables describing the current beat position, the loaded notechart, *etc.*, after the notechart is loaded.

Intended for **mod**ifying the content of loaded notechart, including adjusting the notechart timing, calculating relative note distance, *etc.*

The exact behavior is *unspecified*.

* `#LUAMOD <str-lua-code>`

Inspired by StepMania.

### *Proposal*: #LUAFX

***Scope***: branch, gimmicky (intended; depending on usage) \
***Late effect scope***: (Depending on usage) \
***Effect target***: notes, bar lines, judgment mark(s), note field(s) (intended; depending on usage)

Execute the given **Lua** code with predefined variables describing the current beat position, the loaded notechart, *etc.*, when the beginning of the approach phase of the command is reached during gameplay.

Intended for adding decorative visual/audio **effect**s ("**FX**s"), including changing the moving path of notes, (dis)play extra images and sounds, *etc.*

Intended to be used in conjunction with (**Proposal**) [command modifiers](#proposal-command-modifier).

The exact behavior is *unspecified*.

* `#LUAFX <str-lua-code>`

Inspired by StepMania.

### *Proposal*: Command Modifier

***Scope***: (Part of a command), gimmicky \
***Late effect scope***: (As specified) \
***Effect target***: notes, bar lines, note field(s)

A command modifier can be specified to certain branch-scoped commands using the following form:

* `#COMMAND values; <scope-specifier>; <approach-specifier>`
  * The last semicolon-separated element(s) and trailing semicolon(s) (`;`) can be omitted:
    * `<approach-specifier>` defaults to `0:Linear, 0:Linear`
    * `<scope-specifier>` defaults to (empty).

The whitespace rule of the [comma (`,`)](#comma) also applies to the semicolon (`;`).

The characters after the first semicolon (`;`) are ignored in TaikoJiro 1 but cause crashes in TaikoJiro 2 when loaded.

`<scope-specifier>` specifies the late effect scope of the command.

* Format: `<affected-range-specifier>, <spline-specifier>`
  * The last comma-separated element(s) can be omitted.
* `<affected-range-specifier>` can be one of:
  * (Empty) &mdash; the default.
  * `:` &mdash; (None): Affect no notechart objects.
  * `:<range-affected-non-before>` &mdash; Non-before: Affect notechart objects non-before the point.
  * `<range-affected-before>:` / `<range-affected-before>:0` &mdash; Before, sudden: Suddenly affect notechart objects before the point.
  * `<range-affected-before>:<range-affected-non-before>` &mdash; Both, sudden: Suddenly affect notechart objects near to the point.
* `<range-affected-before>` & `<range-affected-non-before>` can be one of:
  * `*`, the range is unlimited.
  * `<unsigned-int-amount-note>n` specifies the maximum amount of affected notes.
  * `<range-duration-*>` specifies the time/beat range of affected notes (see below).
* *Proposal*: `<spline-specifier>`
  * (Empty), override the effect of the whole scrolling path.
  * `<range-path-deactivate>:<range-path-activate>` &mdash; Override the effect of the part of scrolling path from `<range-path-activate>` (inclusive) before the judgment time to `<range-path-deactivate>` (inclusive) before the judgment time.
    * `<range-path-deactivate>` & `<range-path-activate>` can be one of:
      * `*`, the range is unlimited.
      * `<range-duration-*>` specifies the time/beat duration (inclusive) before the judgment time (see below).

`<approach-specifier>` specifies the time or beat interval and easing method of the approach phase.

* Can be one of:
  * `<approach-before>, <approach-non-before>` &mdash; Start approaching for the specified time duration before the beat position of the command and end approaching at the beat position of the command non-after the specified duration interval.
  * `<approach-both>` &mdash; Both `<approach-before>` & `<approach-non-before>` are `<approach-both>`
  * (Empty) / `0` / `0:Linear` / `0:0` / `0:Linear, 0:Linear`
* `<approach-before>` & `<approach-non-before>` can be one of:
  * `<range-duration-*>` &mdash; (see below).
  * `<range-duration-*>:<enum-str-easing-function>`
    * `<enum-str-easing-function>` specifies the easing functions for the begin or end point of approaching.

`<range-duration-*>` specifies the time/beat duration interval of the approach phase and can be one of:

* `<unsigned-float-seconds-time-duration>` specifies the time duration.
* `<beats-beat-duration>` specifies the beat duration.

## TJA Notechart Definition

The notechart definition is enclosed between `#START` & `#END`.

Most headers are not allowed in notechart definition.

*Unspecified*: The behavior when a header not allowed in notechart definition is placed in a notechart definition.

* In TaikoJiro, such a header is interpreted as note symbols with unrecognized characters ignored and removed.
* In TJAPlayer2 for PC, such a header behavior the same as if the header were placed before `#START` and all commands for the current player-side.

### Whitespaces in Notechart Definition

In non-command lines, all whitespaces are ignored. (TaikoJiro-only?)

* In TJF format, such whitespaces are not ignored as are treated as unknown characters (handled as `0`).

### Notechart Symbols

Including the measure-terminating symbol (comma; `,`) & note symbols (`<enum-str-note>`).

*Unspecified*: Whether unrecognized note symbols are ignored (removed) or treated as `0` (blank).

* In TaikoJiro, unrecognized note symbols are ignored and removed.

### The Measure-terminating Symbol and Timing

The definition of each measure is ended with a comma (`,`). *Unspecified*: The behavior when there are non-whitespaces, non-comment trailing characters after the first comma (`,`) of the line.

Within a measure, there can be any amount of note symbols as long as the *unspecified* maximum allowed amount is not exceeded.

If any note symbols present, each note symbol occupies the same amount of beats within the measure &mdash; a closed-head, open-end beat interval "note symbol beat duration interval". The beat position of the note is at the beginning of this duration interval. The actual time duration of every such beat duration interval can vary and even become negative.

* In TJF format, `,` did not exist and every note symbol occupies the amount of beats of a 1/16th note.

Measures with no note symbols (*i.e.*, `,`-only measures) are equivalent to `0,`

Equation: `beat_duration_of_symbol` (scope: a measure)

* = `measure_beat_duration` / `count_of_symbols`
* = 4 × `measure_upper_numeral` / `measure_lower_numeral` / `count_of_symbols`

Equation: `time_duration_of_symbol` (unit: seconds)

* = 60 × `beat_duration_of_symbol` / `defined_bpm_at_beat_duration`

Compatibility issues:

* In TaikoJiro, the time precision is 1 millisecond, and the time duration of a note symbol is **floor**(**floor**(4 × 60 × 1000 / `defined_bpm_at_beat_duration`) × `beat_duration_of_symbol` / 4) / 1000 (unit: seconds)
  * Reference: <https://twitter.com/barrier15300/status/1619399304250290180> by @barrier15300

Non&ndash;measure-based&ndash;scoped, non-sequential, non&ndash;one-shot commands have their effects fired when the beat duration interval of the nearest preceding note symbol ends. If such commands are placed after the last note symbol of a measure and before the first symbol of the next measure, whether they are placed before or after the `,` symbol has the same effects.

The time duration intervals of different note symbols are possible to overlap by using [`#BPMCHANGE`](#bpmchange) / [`#MEASURE`](#measure) / [`#DELAY`](#delay) commands with non-positive value.

*Unspecified*: The behavior when the time duration intervals of any non-blank note symbols overlap.

* In TaikoJiro, regardless of whether any multiple notechart sections overlap in time, the later defined notes (?) do not accept any inputs until all the earlier defined notes in currently determined branch(es) (?) are judged. This is different from the official games, where a later <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> (or <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby>) hit-type note may be hit before an earlier <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> (or <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>) hit-type note is judged.

(*in construction: explain the behavior of such timing commands with non-positive value*)

* In TaikoJiro, the negative BPM with positive beat duration in [BMS scrolling modes](#bmscroll--hbscroll--nmscroll) can be used for making a warp over an empty section. It works similar to StepMania except that the scrolling behavior of overlapped sections is determined by the last defined section instead of the earliest defined section. See the explanation for StepMania, <https://twitter.com/TaroNuke/status/1250177428783280128> by @TaroNuke

### Note Symbols in Taiko Mode

Effective when [`GAME:Taiko`](#game) or [`#GAMETYPE Taiko`](#gametype) is in effect.

See <https://taiko.namco-ch.net/taiko/en/howto/onpu.php> for the appearance of notes in the official PC-generation arcade games.

| | Note Type | Note Appearance | *<ruby>口<rt>Kuchi</rt> 唱<rt>Shou</rt> 歌<rt>ga</rt></ruby>* <br> "Note phoneticizations" in PC-generation arcade games | Explanations | Notes
--- | --- | --- | --- | --- | ---
`0` | (blank) | (none) | (none) | Nothing needs to be done | ***From***: TJF format
`1` | Regular <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> | Small orange-ish red circle | *<ruby>ド<rt>Do</rt></ruby>* Do / <ruby>コ<rt>Ko</rt></ruby> / *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>* Don | Hit the drum surface | ***From***: TJF format
`2` | Regular <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> | Small sky-blue circle | <ruby>カ<rt>Ka</rt></ruby> / *<ruby>カッ<rt>Ka'</rt></ruby>* Ka | Hit the drum rim | ***From***: TJF format
`3` | Big <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> | Big orange-ish red circle | *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）* DON | Hit the drum surface, score bonus† if with certain force (AC) <br> if on both left and right sides (CS) | ***From***: TJF format
`4` | Big <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> | Big sky-blue circle | *<ruby>カッ<rt>Ka'</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）* KA | Hit the drum rim, score bonus† if with certain force (AC) <br> if on both left and right sides (CS) | ***From***: TJF format
`5` | Head of regular (bar) *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>* drumroll | Small yellow circle with bar attached behind <br> Turns red if hit rapidly in AC games | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>ー* Roll&ndash; | Roll on the drum surface or rim for score bonus | ***From***: TJF format
`I` | (same as `5`) | (see `5`) | (see `5`) | By analogy with Konga mode | ***From***: OpenTaiko (0auBSQ)
`6` | Head of big (bar) *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>* drumroll | Big yellow circle with bar attached behind <br> Turns red if hit rapidly in AC games | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>（<ruby>大<rt>Ookii</rt></ruby>）ー* ROLL&ndash; | Roll on the drum surface or rim for score bonus, more score bonus† if with certain force (AC) <br> if on both left and right sides (CS) | ***From***: TJF format
`H` | (same as `6`) | (see `6`) | (see `6`) | By analogy with Konga mode | ***From***: OpenTaiko (0auBSQ)
`7` | Head of regular *<ruby>激<rt>Geki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>/<ruby>ゲ<rt>Ge</rt> キ<rt>ki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>* "fierce drumroll" burst note / *<ruby>風<rt>Fuu</rt> 船<rt>sen</rt></ruby>/<ruby>ふ <rt>Fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* balloon | Small orange circle (slightly brighter than `1`) with orange-ish red balloon attached behind | *<ruby>ふ <rt>Fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* Balloon | Roll on the drum surface with certain amount of hits for score bonus, extra score bonus† if cleared | ***From***: TJF format
`8` | Explicit end of a drumroll-type note (if any) | (round end of a yellow bar) | (っ!! for ending bar drumroll notes) | Stop rolling the drum non-after the point |
`9` | Head of special burst note/balloon <br> (Differ from game to game) | (Vary) <br> Big yellow circle with potato attached (PS2-generation) <br> Big yellow circle in the shape of a confetti ball 🎊 (PS3- and PC-generation) <br> Has particle decorative visual effects in AC. | *<ruby>く<rt>Ku</rt> す<rt>su</rt> 玉<rt>dama</rt></ruby>* Party Popper <br> (Strictly speaking, *<ruby>薬<rt>Kusu</rt> 玉<rt>dama</rt></ruby>/<ruby>く<rt>Ku</rt> す<rt>su</rt> 玉<rt>dama</rt></ruby>* "Confetti Ball" 🎊 & party popper 🎉 only resemble each other and are not the same thing) | (Vary) <br> In AC, Roll on the drum surface with certain amount of hits (shared among players) for score bonus, extra score bonus† if cleared, more extra score bonus† if done quickly enough <br> In the official games, becomes `7` when not all players encounter `9` with the note head, the full bonus time point, & the note end respectively at the same time position for each player. | From TaikoJiro v2.75
`A` | Hand-holding big <ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby> | Big orange-ish red circle with hands holding with other note(s) for other player(s) | (none) <br> *<ruby>ド<rt>Do</rt> ン<rt>n</rt></ruby>（<ruby>手<rt>Te</rt></ruby>）* "DON (Hand)" (in 4-player mode) | Like `3`, extra score bonus† if all players caught <br> In the official games, becomes `3` when no hit-type notes exist at the same time position for any of the player above or below the current player. | ***From***: TJAPlayer2 for PC ver.2018040100
`B` | Hand-holding big <ruby>カ<rt>Ka</rt> ツ<rt>tsu</rt></ruby> | Big sky-blue circle with hands holding with other note(s) for other player(s) | (none) <br> *<ruby>カッ<rt>Ka'</rt></ruby>（<ruby>手<rt>Te</rt></ruby>）* "KA (Hand)" (in 4-player mode) | Like `4`, extra score bonus† if all players caught <br> In the official games, becomes `4` when no hit-type notes exist at the same time position for any of the player above or below the current player. | ***From***: TJAPlayer2 for PC ver.2018040100
`C` | Bomb/mine | Small dark-blue cherry bomb with ignited fuze 💣 | (none) | Combo-break and *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge penalty if caught | ***From***: OpenTaiko (0auBSQ)
`D` | Fuze/fuse drumroll | ? <br /> (Big circular clock with blue-ish purple edge and with bar attached behind in OpenTaiko (0auBSQ)) | (<ruby>時<rt>Ji</rt> 爆<rt>baku</rt>弾<rt>dan</rt></ruby> "Time bomb"/Fuseroll in OpenTaiko (0auBSQ)) | Roll on the drum surface with certain amount of hits, combo-break (or BAD?) (in OpenTaiko (0auBSQ)) and *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge penalty if failed to do so <br> Not in the official games. | ***From***: OutFox
`F` | *Ad libitum* note (AD-LIB) | (Invisible) | (none) | Hit the drum surface or rim for score bonus or other bonuses. <br> Not in the official games. <br> Inspired by another rhythm game *GROOVE COASTER*, developed by TAITO | ***From***: TJAPlayer2 for PC ver.2016081500
`G` | Swap note | (Vary) <br /> Big green circle in taiko-web (plugin "Green Notes") <br /> Big purple circle in OpenTaiko (0auBSQ) | (*<ruby>グ<rt>Gu</rt> リー<rt>rii</rt> ン<rt>n</rt></ruby>* Green) <br /> (*<ruby>カ<rt>Ka</rt> ド<rt>do</rt> ン<rt>n</rt></ruby>* KADON) | Hit the drum surface on left or right side **&** the drum rim on the other left or right side. <br> Not in the official games. | ***From***: taiko-web (plugin "Green Notes") <br /> ***Supported by***: OpenTaiko (0auBSQ) v0.5.4

†: No score bonuses if the PC-generation scoring rule is followed.

Unknown note symbols & `8` without the corresponding head of drumroll-type notes are treated as `0`.

* In TJAPlayer2 for PC & OpenTaiko (0auBSQ) until v0.6.0, `9` is treated the same as `7`.

#### Hit-type notes

Including `1`, `2`, `3`, `4`, `A`, `B`, *etc.*, but not `F`.

#### Drumroll-type notes

Including `5`, `6`, `7`, `9`, *etc.*

The head and end of drumroll-type notes have no timing window. In the official arcade game, drumroll inputs are allowed non-before/non-after the containing frame of the judgment timing of the head/end of the drumroll-type note.

During the defined duration interval within a drumroll-type note, either `0` or the symbol of the note head may appear. *E.g.*: `5008` / `5558` / `5058` are all equivalent. *Unspecified*: Whether other drumroll-type notes can be used in place of the repeated symbol of the note head.

* In TaikoJiro, all drumroll-type note head symbols can be used in place of the repeated symbol.

*Proposal*: Each symbol of the note head inside a bar drumroll note denote a middle point of the bar which can scroll independently to the head, end, and other middle points of the note.

For special balloons (`9`), the last occurrence of repeated note head symbol (if any) defines the full bonus time point. If the note is cleared, full bonus is awarded only by clearing the note non-after that point and partial bonus is awarded otherwise. The full bonus time point is *unspecified* when no repeated note head symbols ever occur.

* In TaikoJiro, the full bonus time point is implicitly placed at the position 0.6 times of the note duration after the note head.

By default, drumroll-type notes are ended non-after one of:

* The definition position of an `8`.
  * *Proposal*: The ending position can be earlier than the `8` by an *unspecified* duration.
* An *unspecified* duration before a hit-type note symbol.
  * In TaikoJiro, the duration is one of:
    * In notecharts without any "branch"/path sections: 50ms.
    * Otherwise, in the *<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>* Normal "branch"/path state: 8/53 s (≈ 150.94ms) (tentatically determined).
    * Otherwise, in other "branch"/path states: 0ms.
* In TaikoJiro, the definition position of the last note symbol of the notechart, except when the note head is in the definition of a "branch"/path other than the *<ruby>普<rt>Fu</rt> 通<rt>tsuu</rt></ruby>* Normal "branch"/path.

In the official games, drumroll-type notes are usually intentionally made to end earlier than the designed ending beat position by the amount of beats of a 1/48th note.

* Reference: *連打秒数表* ("List of seconds of drumrolls"). 太鼓の達人 譜面とか Wiki\* ("Taiko no Tatsujin - Wiki\* about Notecharts and so on"). <https://wikiwiki.jp/taiko-fumen/収録曲/連打秒数表>

*Unspecified*: Whether other drumroll-type note symbols can appear during a drumroll-type note.

* In TJF format, `8` did not exist and the duration interval is specified by repeat the note head symbol consecutively, where the last repeated symbol corresponds to TJA `8`, *e.g.*, TJF `5555` = TJA `5558`.

*Unspecified*: The behavior when a balloon-type note (including `7`, `9`, `D`, *etc.*) is not ended with an `8` before other non-blank note symbols.

* In TaikoJiro v2.36+, after the non-blank note symbols (must be hit-type), the balloon-type note remains active if not cleared and is only closed by clearing it or by an `8` or another head of this balloon-type note. All other notes become impossible to hit while the balloon-type note is active.
  * This behavior is in reference to *<ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> タ<rt>Ta</rt> ワー<rt>waa</rt> 3<rt>San</rt></ruby>（<ruby>辛<rt>kara</rt> 口<rt>kuchi</rt></ruby>）* ("Taiko Tower 3 (hard)"), where the duration interval of balloon-type notes overlaps with the following hit-type note.
    * See <https://wikiwiki.jp/taiko-fumen/収録曲/その他/太鼓タワー3%28辛口%29>
  * *Proposal*: Restrict this behavior to `COURSE:Tower`.

*Unspecified*: The behavior when a non-positive-duration bar drumroll note is formed, possibly from a drumroll-type note ended by a hit-type note (*e.g.*, `51` / `56` / `65`, where the duration of the drumroll may be shortened as mentioned above) or by using timing settings.

* In Taikosan, zero-duration bar drumroll notes can be created by using an isolated drumroll-type note symbol. However, they are not accepted and an error message is displayed. \
  ![Taikosan's Error Message for Zero-duration Bar Drumroll Note](https://i.imgur.com/MDdNzKX.png)

***From***: TJF format \
***Supported by***: (Universally supported)

#### Compatibility Issues

* In TJAPlayer2 for PC, drumroll-type notes must be ended with `8`.
* In TJAPlayer2 for PC, The head of balloon-type notes has a timing window of the time duration of 1 frame under 60fps.

### Note Symbols in Jube Mode

Effective when [`GAME:Jube`](#game) is in effect.

Unlike `GAME:Taiko`, every 4 hexadecimal digits are grouped together to represent a note combination and occupy the same beat duration interval.

In TJA files, within non-command lines, all whitespaces are ignored by TaikoJiro. In this game mode, every 4 digits are conventionally separated with a space for readability.

#### Example

(This example is adapted from the `README.txt` distributed along with TaikoJiro)

```txt
Note Layout → 0/1 Notation → Note Symbol (Hexadecimal Digit)
■■□■ → 1101 → D
□■■□ → 0110 → 6
□□□■ → 0001 → 1
□□□□ → 0000 → 0
```

* `■` &mdash; Tap note
* `□` &mdash; Blank
* Hold notes were not supported.

The above note combination is written `D610`.

![GAME:Jube Example](https://i.imgur.com/eOqpsO8.gif)

***From***: TaikoJiro v2.13

### Note Symbols in Konga Mode

Effective when [`GAME:Konga`](#game) or [`#GAMETYPE Konga`](#gametype) is in effect.

See the exemplar actual gameplays:

* <https://www.youtube.com/watch?v=G70HoWO1umc> <br /> <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/G70HoWO1umc" title="YouTube video player, playing &quot;Donkey Konga [29] GameCube Longplay&quot;, uploaded by Mutch Games" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
* <https://www.youtube.com/watch?v=myci706YXss> <br /> <iframe width="560" height="315" src="https://www.youtube.com/embed/myci706YXss?si=AKOnV2vJgvUB63gU" title="YouTube video player, playing &quot;Longplay of Donkey Konga 3&quot;, uploaded by LongplayArchive" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| | Note Type | Note Appearance | *<ruby>口<rt>Kuchi</rt> 唱<rt>Shou</rt> 歌<rt>ga</rt></ruby>* <br> "Note phoneticizations" in *Donkey Konga 3* | Explanations | Notes
--- | --- | --- | --- | --- | ---
`0` | (blank) | (none) | (none) | Nothing needs to be done | ***From***: TJF format
`1` | Right drum beat | Red circle with its right half filled | <ruby>パ<rt>Pa</rt></ruby> / <ruby>パッ<rt>Pa'</rt></ruby> / <ruby>パン<rt>Pan</rt></ruby> | Hit the right bongo drum |
`2` | Left drum beat | Yellow circle with its left half filled | <ruby>ポ<rt>Po</rt></ruby> / <ruby>ポッ<rt>Po'</rt></ruby> / <ruby>ポン<rt>Pon</rt></ruby> | Hit the left bongo drum |
`3` | Both drum beats | Pink circle | D | Hit both bongo drums |
`G` | (same as `3`) | (see `3`) | (see `3`) | By analogy with Taiko mode. | ***From***: OpenTaiko (0auBSQ) v0.5.4
`4` | Clap | Sky-blue circle with star-ish edge | <ruby>チャ<rt>Cha</rt></ruby> / <ruby>チャッ<rt>Cha'</rt></ruby> / <ruby>チャン<rt>Chan</rt></ruby> | Clap hands above the bongo drums |
`5` | Head of right bar drumroll | Red circle with its right half filled and with bar attached behind | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>～* "Roll~" | Roll on the right bongo drum for score bonus |
`I` | Head of left bar drumroll | Yellow circle with its left half filled and with bar attached behind | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>～* "Roll~" | Roll on the left bongo drum for score bonus |
`6` | Head of both bar drumroll | Pink circle with bar attached behind | *<ruby>連<rt>Ren</rt> 打<rt>da</rt></ruby>～* "Roll~" | Roll on either bongo drum for score bonus |
`H` | Head of clap bar applause | Sky-blue circle with star-ish edge and with bar attached behind | *<ruby>拍<rt>Haku</rt> 手<rt>shu</rt></ruby>～* "Applaud~" | Applaud above the bongo drums for score bonus |
`7` | Head of regular *<ruby>激<rt>Geki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>/<ruby>ゲ<rt>Ge</rt> キ<rt>ki</rt> 連<rt>ren</rt> 打<rt>da</rt></ruby>* "fierce drumroll" burst note / *<ruby>風<rt>Fuu</rt> 船<rt>sen</rt></ruby>/<ruby>ふ <rt>Fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* balloon | Small orange circle (slightly brighter than `1`) with orange-ish red balloon attached behind | (*<ruby>ふ <rt>Fu</rt> う<rt>u</rt> せ<rt>se</rt> ん<rt>n</rt></ruby>* Balloon) | Roll on either bongo drum with certain amount of hits for score bonus, extra score bonus† if cleared <br /> Not in the official games. <br /> By analogy with Taiko mode. | ***From***: TJF format
`8` | Explicit end of a drumroll-type note (if any) | (round end of a bar) | (none) | Stop rolling the drum or clapping non-after the point |
`9` | Head of special burst note/balloon | (Vary) | (*<ruby>く<rt>Ku</rt> す<rt>su</rt> 玉<rt>dama</rt></ruby>* Party Popper) | (Vary) <br> Roll on either bongo drum with certain amount of hits (shared among players) for score bonus, extra score bonus† if cleared, more extra score bonus† if done quickly enough <br> Might become `7` when not all players encounter `9` with the note head, the full bonus time point, & the note end respectively at the same time position for each player. <br /> Not in the official games. <br /> By analogy with Taiko mode. | From TaikoJiro v2.75
`A` | Hand-holding both drum beats | (Pink circle with hands holding with other note(s) for other player(s)) | ? | Like `3`, extra score bonus† if all players caught <br /> Might becomes `3` when no hit-type notes exist at the same time position for any of the player above or below the current player. <br> Not in the official games. <br> By analogy with `GAME:Taiko`. | ***From***: OpenTaiko (0auBSQ)
`B` | Hand-holding clap beat | (Sky-blue circle with star-ish edge and with hands holding with other note(s) for other player(s)) | ? | Like `4`, extra score bonus† if all players caught <br /> Might becomes `4` when no hit-type notes exist at the same time position for any of the player above or below the current player. <br> Not in the official games. <br> By analogy with Taiko mode. | ***From***: OpenTaiko (0auBSQ)
`C` | Bomb/mine | (Small dark-blue cherry bomb with ignited fuze 💣) | (none) | Combo-break and *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge penalty if caught <br /> Not in the official games. <br /> By analogy with Taiko mode. | ***From***: OpenTaiko (0auBSQ)
`D` | Fuze/fuse drumroll | (Big circular clock with blue-ish purple edge and with bar attached behind in OpenTaiko (0auBSQ)) | (<ruby>時<rt>Ji</rt> 爆<rt>baku</rt>弾<rt>dan</rt></ruby> "Time bomb"/Fuseroll in OpenTaiko (0auBSQ)) | Roll on either bongo drum with certain amount of hits, combo-break (or BAD?) (in OpenTaiko (0auBSQ)) and *<ruby>魂<rt>tamashii</rt> ゲー<rt>gee</rt>ジ<rt>ji</rt></ruby>* spirit gauge/soul gauge penalty if failed to do so <br> Not in the official games. <br /> By analogy with Taiko mode. | ***From***: OutFox
`F` | *Ad libitum* note (AD-LIB) | (Invisible) | (none) | Hit either bongo drum or clap for score bonus or other bonuses. <br> Not in the official games. <br> By analogy with Taiko mode. | ***From***: TJAPlayer2 for PC ver.2016081500

†: No score bonuses if the PC-generation scoring rule is followed.

* Beat-type notes & the clap note correspond to hit-type notes in Taiko mode.
* Drumroll-type notes & the applause note correspond to drumroll-type notes in Taiko mode.

The note handling details of the Taiko mode apply. See the explanation in [Note Symbols in Taiko Mode](#note-symbols-in-taiko-mode).

***From***: OpenTaiko (0auBSQ) v0.5.4 \
***Supported by***: taiko-web (plugin "Donkey Konga Mode"), OutFox

## Terminologies

### Word Usage of this Article

#### General Word

`&` is used only for conjoining independent nouns with similar grammar structure and `and` is used otherwise.

The ***ITALIC BOLD ALL-UPPER-CASE*** keywords ***MUST***, ***MUST NOT***, ***SHOULD***, ***SHOULD NOT***, & ***MAY*** are to be interpreted as described in RFC 2119: <https://www.rfc-editor.org/rfc/rfc2119>

The time relation is denoted as follow:

Word | Before | Non-after | At | Non-before | After
--- | --- | --- | --- | --- | ---
Time relation | \< | ≤ | = | ≥ | >

The fraction (for beat duration, *etc*.) is denoted as follow:

Word | whole | half | 1/3rd | quarter <br /> 1/4th | 1/8th | 1/16th | ...
--- | --- | --- | --- | --- | --- | --- | ---
Fraction | 1/1 | 1/2 | 1/3 | 1/4 | 1/8 | 1/16 | ...
Other <br /> spellings | whole | half | third | quarter <br /> fourth | eighth | sixteenth | ...

#### *Unspecified*

If a usage causes *unspecified* behavior or the behavior itself is *unspecified*, the actual or intended behavior may vary from simulator to simulator and/or dependent on user settings. When portability is concerned, such a usage and the behavior ***SHOULD*** be avoid and the actual behavior ***SHOULD NOT*** be depended upon.

Because this article is still *in construction* and the TJA format is still evolving, this is possible that some usages or behaviors are stated as *unspecified* but the actual or intended behaviors are/have become consistent among most simulators.

### Level of Impact of Headers and Commands

> (normal) > timing > scoring > gimmicky > decorative

The maximum level of impact of the headers and commands are listed in the description of their scope.

Changing the value of a header or command whose impact level ≤ scoring never affects the required timing and types of the gameplay input.

Changing the value of a header or command whose impact level ≤ gimmicky also never affects the sorting order of the song or the gameplay and scoring rules.

A gimmicky header or command may affect the difficulty for reading the notechart during gameplay, while a decorative header or command usually does not.

### Whitespace character

* (Halfwidth) Space (U+0020; "<code> </code>")
* Character Tabulation / Tab (U+0009; `\t`)
* Carriage Return / CR (U+000D; `\r`)
* Line Feed / LF / Newline (U+000A; `\n`)
* ***NOT***: Ideographic Space / Fullwidth Space (U+3000; "<code>　</code>")
* It is *unspecified* (but unlikely) whether other space-like characters are accepted.

### Translations

Japanese terminologies of the game: <https://wikiwiki.jp/taiko-fumen/用語集>

Japanese terminologies are provided with their pronunciation annotated using a <ruby>訓<rt>Kun</rt> 令<rt>rei</rt> 式<rt>Shiki</rt> ロー<rt>Roo</rt> マ<rt>ma</rt> 字<rt>ji</rt></ruby>-like romanization system. If a Japanese terminology can be written in *<ruby>漢<rt>kan</rt> 字<rt>ji</rt></ruby>* "Chinese Character" form, both are listed.

Some of the *<ruby>漢<rt>kan</rt> 字<rt>ji</rt></ruby>* "Chinese Character" form of the Japanese terminologies are literally taken as the Chinese translation.

For some terminologies of the game, there exist multiple English translations. Their are expressed as `"LIT"/TDM/TKT/PC (ALTs)` when necessary in this article:

* `"LIT"` &mdash; A rather literal translation
* `TDM` &mdash; The earlier English translation from the official PS2 console game *Taiko: Drum Master*
* `TKT` &mdash; <https://taikotime.blogspot.com/2010/12/glossary.html>
* `PC` &mdash; The official English translation from the official PC-generation games and the official English website: <https://taiko.namco-ch.net/taiko/en>
* `ALTs` &mdash; Alternative translation(s) usually used in the code & the notechart format

Fields with unknown (not existing or simply not investigated by the maintainer of this article) translation are denoted with `?`.

Translations which are simply romanization transliterations are omitted.

Some corresponding terminologies from other rhythm games are taken as one of the translations instead: See individual entries of <https://github.com/stepmania/stepmania/wiki>

### Mentioned PC-Compatible Simulators with TJA Format Support

Reference: *太鼓シミュレーター一覧* ("List of Taiko Simulators"). (2022, July 26). 太鼓の達人 Wiki ("Taiko no Tatsujin Wiki"). <https://wikiwiki.jp/taiko/太鼓シミュレーター一覧>

Unless stated otherwise, a simulator mentioned in this article also refers to its derivations.

The honorific title is omitted.

* <ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> さ<rt>sa</rt> ん<rt>n</rt> 次<rt>Ji</rt> 郎<rt>rou</rt></ruby> (*TaikoJiro*): By touch.
  * The TJF format was modified and extended into the TJA format for this simulator.
  * Inspired by <ruby>太<rt>Tai</rt> 鼓<rt>ko</rt> さ<rt>sa</rt> ん<rt>n</rt> 太<rt>Ta</rt> 郎<rt>rou</rt></ruby> (*Taikosan*): By VIL.
    * The TJF format was developed and used for this simulator.
* TJAPlayer2 for PC: By J.MIR (kairera0467) <https://github.com/kairera0467/TJAP2fPC>
  * Inspired by TJAPlayer2 (for PSP): (Unknown author)
  * ← Derived from DTXManiaXG (Ver.K): By J.MIR (kairera0467) <https://ja.osdn.net/projects/dtxmaniaxg-verk/>
    * ← Derived from DTXMania: By ＦＲＯＭ (DTXMania), <ruby>や<rt>Ya</rt> ぎ<rt>gi</rt>。</ruby> (yyagi), *et al.* <https://ja.osdn.net/projects/dtxmania/>
      * Reference: <ruby>や<rt>Ya</rt> ぎ<rt>gi</rt>。</ruby> (2020, September 14). *Derivatives of DTXMania*. DTXMania Wiki - DTXMania. OSDN. <https://ja.osdn.net/projects/dtxmania/wiki/derivatives>
  * Derivatives \
    ver.2017072200, non-after 2017, December 15 → TJAPlayer3 (AioiLight): By AioiLight *et al.* <https://github.com/AioiLight/TJAPlayer3>
    * ver-1.6.x, non-after 2019, October 27 → TJAPlayer3 (twopointzero): By Jeremy Gray (twopointzero) <https://github.com/twopointzero/TJAPlayer3>
      * v5.2.4, non-after 2020, May 19, &ndash; v5.2.9 → TJAPlayer3 (KabanFriends): By KabanFriends <https://github.com/KabanFriends/TJAPlayer3>
        * Non-after 2021, May 26 → TJAPlayer3-Extended: By KabanFriends <https://github.com/KabanFriends/TJAPlayer3-Extended>
    * master (v1.5.7). non-after 2020, March 25 → TJAPlayer3-f: By Mr-Ojii <https://github.com/Mr-Ojii/TJAPlayer3-f>
    * master (v1.5.7), non-after 2020, August 28 → TJAPlayer3-Develop: By touhou-renren *et al.* <https://github.com/TJAPlayer3-Develop/TJAPlayer3-Develop>
      * Non-after 2020, Nov 8 → TJAPlayer3-Develop-ReWrite: By touhourenren *et al.* <https://github.com/touhourenren/TJAPlayer3-Develop-ReWrite>
        * Non-after 2021, Sep 21 → OpenTaiko (aka. TJAPlayer3-Develop-BSQ) (0auBSQ): By 0auBSQ *et al.* <https://github.com/0auBSQ/OpenTaiko>
* taiko-web: By Clemaister, later mainly maintained by bui <https://github.com/bui/taiko-web> (no longer unavailable, see <https://github.com/github/dmca/blob/master/2023/02/2023-02-21-bandai.md>)
* Project OutFox: Mainly maintained by Team Rizu <https://projectoutfox.com/>
  * ← Derived from StepMania 5.1: Mainly maintained by The Spinal Shark Collective <https://github.com/stepmania/stepmania>
    * ← Derived from StepMania 3.95: By Chris Danford *et al.*
* TaikoManyGimmicks (aka. taikosimu(NN)): By barrier15300 <https://twitter.com/barrier15300/with_replies>

## References

* *太鼓の達人 譜面とか Wiki\** ("Taiko no Tatsujin - Wiki\* about Notecharts and so on"). <https://wikiwiki.jp/taiko-fumen/>
* tjfフォーマット ("tjf Format"). (2007, July 6). *太鼓さん太郎 nicover* ("Taikosan Nico(nico) ver."). `Readme.txt`
  * This file is distributed along with Taikosan.
* touch (2013, September 12). tjaフォーマット ("tja Format"). *太鼓さん次郎    Ver. 2.92くらい* ("TaikoJiro    Ver. 2.92 or so").
  * This section of the documentation can be retrieved from both the files `readme.txt` & `readme.html` distributed along with TaikoJiro.
  * Some of its paragraphs are cited in other web pages:
    * dispconf (2014, January 1). *４－２．譜面追加　自分で作る* ("4-2 - Add Notecharts: Make You Own"). 太鼓さん次郎解説!! ("TaikoJiro Explanation!!"). <https://taikosanjiro.hatenablog.com/entry/譜面-2>
    * 仕様 ("Specifications"). (2021, August 28). *太鼓さん次郎* ("TaikoJiro"). 太鼓さん次郎交流 Wiki ("TaikoJiro Communication Wiki"). <https://wikiwiki.jp/jiro/太鼓さん次郎#specifications>
* kairera0467 (2021, April 30). *TJAPlayer2 for.PC(仮) by.kairera0467*. kairera0467/TJAP2fPC. GitHub. <https://github.com/kairera0467/TJAP2fPC/blob/work-s/実行時フォルダ/readme.txt>
* *TJAPlayer3/CDTX.cs at ver-1.6.x*. (2019, Mar 2). AioiLight/TJAPlayer3. GitHub. <https://github.com/AioiLight/TJAPlayer3/blob/ver-1.6.x/TJAPlayer3/Songs/CDTX.cs>
* AioiLight (2019, April 17). *.tja フォーマット* (".tja Format"). AioiLight.space. <https://web.archive.org/web/20190914085205/https://aioilight.space/taiko/tjap3/doc/tja/>
  * Browsable archive on GitHub Pages by Iweidieng Iep: [TJAPlayer3-AioiLight-docs/doc/tja](<https://iepiweidieng.github.io/TJAPlayer3/TJAPlayer3-AioiLight-docs/doc/tja.html>)
* KabanFriends (2021, May 29). *New TJA Commands in TJAPlayer3-Extended*. KabanFriends/TJAPlayer3-Extended. GitHub. <https://github.com/KabanFriends/TJAPlayer3-Extended/blob/master/Test/COMMANDS.txt>
* *TJA format*. (2021, September 28). bui/taiko-web Wiki. GitHub. <https://web.archive.org/web/20230103093826/https://github.com/bui/taiko-web/wiki/TJA-format>
  * Archive on GitHub Gist by Katie Frogs: <https://gist.github.com/KatieFrogs/e000f406bbc70a12f3c34a07303eec8b>
* Katie Frogs (2023, Feburary 12). *taiko-web-plugins/README.md at main*. KatieFrogs/taiko-web-plugins. GitHub. <https://github.com/KatieFrogs/taiko-web-plugins/blob/main/README.md>
* Mr-Ojii (2023, Mar 28). *TJAPlayer3-f/AdditionalFeatures.md at v2*. Mr-Ojii/TJAPlayer3-f. GitHub. <https://github.com/Mr-Ojii/TJAPlayer3-f/blob/v2/TJAPlayer3-f/Docs/AdditionalFeatures.md>
* 0auBSQ (2023, September 18). *New Commands*. 0auBSQ/OpenTaiko. GitHub. <https://github.com/0auBSQ/OpenTaiko/blob/main/OpenTaiko/Documentation/Tja/NewCommands.md>
* *OpenTaiko/CDTX.cs at main*. (2024, May 3). 0auBSQ/OpenTaiko. GitHub. <https://github.com/0auBSQ/OpenTaiko/blob/main/OpenTaiko/src/Songs/CDTX.cs>
* *OpenTaiko/NotesManager.cs at main*. (2024, April 15). 0auBSQ/OpenTaiko. GitHub. <https://github.com/0auBSQ/OpenTaiko/blob/main/OpenTaiko/src/Stages/07.Game/Taiko/NotesManager.cs>
* Squirrel (2023, November 4). *TJA Compatibility*. Project OutFox Wiki. <https://outfox.wiki/dev/mode-support/tja-support/>
* nyoro (2023, November 11). *TJA Format Support*. Visual Studio Marketplace. <https://marketplace.visualstudio.com/items?itemName=nyoro.tja-format-support>
  * This vscode extension provides short explanations for TJA headers/commands, including headers/commands introduced by TaikoManyGimmicks.

## TODO

* Reorder headers & commands by their categories & popularity and possibility of being supported: Pending.
* Explain timing commands with non-positive arguments, supplemented with diagrams: In progress. Behaviors to check:
  * Uncertain rules for notes being not judged until a later note in non-trivial cases.
* List & explain known gimmicks, especially the gimmicks which have appeared in multiple charts by different chart creators and received terminologies: Planned. Gimmicks with uncertain mechanics:
  * *<ruby>途<rt>To</rt> 中<rt>chuu</rt> 出<rt>Shutsu</rt> 現<rt>gen</rt></ruby>* "appearing in middle" (including "disappearing in middle").
    * Similar to a warp in definition.
    * Interfering with amount of displayed beats before/after judgment?
    * Utilizing the constant speed past judgment in TaikoJiro?
  * Bar lines that disappears.
    * Unknown threshold to hide bar lines past judgment in TaikoJiro.

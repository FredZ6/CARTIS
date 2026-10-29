<p align="right">
  <a href="README.md"><img src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E5%88%87%E6%8D%A2%E4%B8%AD%E6%96%87-0f766e?style=for-the-badge" alt="切换到简体中文"></a> | <strong>English</strong>
</p>

![CARTIS — A Portal to Every Game Era](docs/images/cartis-cover.png)

# CARTIS 2.27

**A Portal to Every Game Era**

CARTIS is an Android handheld game launcher built on **Socket 0.6**. Browse your library through 3D cartridges and console models, enjoy the feeling of picking a physical cartridge, and launch games through emulators you have installed separately.

## What is CARTIS?

The name **CARTIS** combines **Cartridge** and **TARDIS**. Cartridges carry memories of gaming's golden age; the TARDIS represents travelling through time and exploring different worlds.

CARTIS brings these ideas together: **every cartridge becomes a doorway to another gaming era.** From the monochrome pixels of the Game Boy to the colourful GBA, NDS and PSP libraries, it connects memories across generations.

CARTIS organizes, displays and launches your games. Separate emulators run them. **The APK does not include games, BIOS files, emulators or RetroArch cores.**

[Download 2.27 (tested on KPB)](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.27.apk) · [Release notes](https://github.com/FredZ6/CARTIS/releases/tag/v2.27) · [Getting started](#first-time-start-here)

**Baidu Netdisk mirror:** [CARTIS 2.27 APK](https://pan.baidu.com/s/1CThKm8nin5pcrfILlXYy9Q?pwd=6tfk), extraction code: `6tfk`.

<a href="https://github.com/FredZ6/CARTIS/releases"><img src="https://cartis-readme-counters.vercel.app/downloads.svg" width="340" alt="GBA display showing release asset downloads"></a>
<a href="https://hits.sh/github.com/FredZ6/kpb-socket/"><img src="https://cartis-readme-counters.vercel.app/views.svg" width="340" alt="GBA display showing README views"></a>
<img src="https://hits.sh/github.com/FredZ6/kpb-socket.svg?label=README%20views&amp;color=007ec6" width="1" height="1" alt="">

<sub>The counter images are generated when requested and cached for about 15 minutes; each display shows its latest source-read time in UTC. GitHub's image cache may add delay, so the numbers are not real-time. A temporarily unavailable source shows OFFLINE and its last available value. Downloads include archived records for deleted APK assets (130 downloads) and current GitHub Releases assets, but exclude cloud-drive downloads. Downloads are not installation counts. Views retain the original counter and do not represent unique visitors.</sub>

## Contents

- [What is CARTIS?](#what-is-cartis)
- [Features already delivered in the 2.x series](#features-already-delivered-in-the-2x-series)
- [Performance results and test scope](#performance-results-and-test-scope)
- [KPB on-device gallery](#kpb-on-device-gallery)
- [Before installing or upgrading](#before-installing-or-upgrading)
- [Origins and credits](#origins-and-credits)
- [Roadmap for 3.0](#roadmap-for-30)
- [First-time setup](#first-time-start-here)
- [Step 1: Install CARTIS](#step-1-install-cartis)
- [Step 2: Install the emulators first](#step-2-install-the-emulators-first)
- [Step 3: Organize games and cover art](#step-3-organize-games-and-cover-art)
- [Step 4: Add your platforms to CARTIS](#step-4-add-your-platforms-to-cartis)
- [Everyday controls](#everyday-controls)
- [Troubleshooting](#troubleshooting)
- [Repository rename and old links](#repository-rename-and-old-links)

---

## Latest update: 2.27 cross-platform collections, consistent menus and faster page opening

The latest release is **CARTIS 2.27 (versionCode 27)**, packaged as **`CARTIS-2.27.apk`**. It builds on 2.26, incorporates the 2.25 colour fixes, and has passed KPB feature, interface and input-response regression checks. This complete release has not been retested on KPA or other devices. It keeps the original package name and signing certificate, so you can upgrade in place and retain your configuration. Do not uninstall the previous version or clear its data first.

- **Search every platform and jump to the cartridge:** search covers all added platforms. Tap a result or press A to select that game's platform and cartridge without launching it. You can then favourite it or change its appearance.
- **Local and global collection pages:** Select opens collections for the current platform by default. Use L/R to switch pages. A global collection can contain games from different platforms; global favourites and recently played views also span platforms.
- **Separate collection controls in game details:** press X on a selected game and use the independent Global Collections and This Platform's Collections controls. Collections with the same name remain separate across these scopes.
- **Optional upward swipe to launch:** enable the upward-swipe option under Settings → Performance. The default remains a downward swipe.
- **Consistent top navigation:** the collections page uses L / This Platform / All Platforms / R. The platform chooser shows the full console name in the top L/R bar. Game and collection counts stay in their original area with a larger font; tabs and shoulder controls support touch.
- **Refined dark mode:** switch light/dark mode with the sun/moon control in the settings sidebar. Ordinary bottom buttons share the game-name button's glass colours, while red and green action buttons keep their original colours.
- **Shorter waits after button presses:** fixes remove redundant platform-data rebuilds, repeated footer text layout and slow global game-path deduplication. The footer also follows KPB's existing fast glass-rendering profile.
- **Earlier improvements remain:** custom key bindings and platform shortcuts, font switching, the transparent icon, the About-page illustration, launching without core-folder authorization, model zoom fixes and previously verified performance improvements are retained.

[Download CARTIS-2.27.apk](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.27.apk) · [Full release notes](https://github.com/FredZ6/CARTIS/releases/tag/v2.27) · [SHA-256 checksums](https://github.com/FredZ6/CARTIS/releases/download/v2.27/SHA256SUMS.txt)

### Input-response comparison with 2.23

Both versions were tested on the same KPB, with the same configuration, dark mode and a 504-game GBA library. Each version ran 16 paths × 6 trials; all 192 transitions succeeded. The table shows the median of the last five trials for **input event to the target page's first rendered frame**. These measurements are not emulator startup times or frame-rate results.

| Action | 2.23 | 2.27 | Wait reduction |
| --- | ---: | ---: | ---: |
| Select: open collections | 707.1 ms | 337.5 ms | 52.3% |
| X: open game details | 310.9 ms | 108.9 ms | 65.0% |
| Start: open search | 362.2 ms | 199.9 ms | 44.8% |
| Y: open settings | 398.6 ms | 223.3 ms | 44.0% |
| X: second details layer | 362.3 ms | 179.8 ms | 50.4% |

Median differences on the other 11 paths were below one 60 Hz frame (16.7 ms); this small sample does not establish a consistent change on those paths. First-trial results, observed ranges, test order and limitations are documented in the [complete 16-path report, in Chinese](docs/reports/2026-10-29-key-latency.md). Download the [PDF report](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.23-vs-2.27-latency-report.pdf) or [raw data package](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.23-vs-2.27-latency-data.zip).

Additional checks passed: 126 feature assertions, 36 light/dark footer checks, 8 model/application-page checks, 16 red/green button-colour checks, 60 theme checks and 24 collection-storage checks. Earlier technical records are available in the [key-binding regression report](docs/reports/2026-10-28-keybindings.md) and [platform zoom-fix report](docs/reports/2026-10-27-camera-zoom-fix.md), both in Chinese.

## Features already delivered in the 2.x series

The following features are implemented. CARTIS 2.x continues to receive maintenance and improvements; this is not a list of future plans.

- **Console selection page:** browse 3D console models to change platforms, including additional models and platform options such as GBC.
- **Interactive console models:** consoles such as the GBA SP, NDS and 3DS support display interactions, including automatic lid opening.
- **Cartridge and console inspection:** tap a model to enlarge it, then drag to inspect it from different angles through 360 degrees.
- **Familiar startup and background sounds:** entering certain platforms' cartridge pages plays the corresponding console's startup sound and background audio. Each can be disabled independently.
- **Two model-quality modes:** choose High Detail or High Frame Rate separately for consoles and cartridges to suit the device.
- **Smoother page transitions:** transition animations make navigation less abrupt.
- **Platform-specific and global collections, plus search:** create, rename, delete and reorder collections, including collections that span platforms. Search covers all platforms and selecting a result locates its cartridge.
- **KPA layout adaptation:** layouts, platform names and bottom menus have been adapted for KPA and KPB screen proportions, including a fix for the NDS model shrinking during switching.
- **In-place upgrades:** the original package name and signing certificate are retained so game-folder configuration and personal settings survive upgrades. Do not uninstall or clear app data.
- **Ongoing fixes based on feedback:** model, layout, return-navigation and other reported issues continue to be addressed.
- **CARTIS visual identity and settings:** a transparent pixel-art police-box icon, adaptive pixel loading screen, actual loading progress, consistent key-binding settings and an illustrated About page.
- **Cleaner game details:** pressing X temporarily hides the underlying game-name badge and inactive Select collection hint; B restores them when returning to cartridge selection.
- **Dark mode:** use the settings sidebar's sun/moon control. Ordinary footer buttons match the game-name button, while red and green action colours are preserved.
- **Performance work:** batch-rendered dot backgrounds and cached library traversal reduce repeated work during navigation while retaining transparent cartridges, cover clarity and eight-console model caching. Results are scoped below.

### Performance results and test scope

See the [KPB performance comparison report](docs/reports/2026-10-27-kpb-performance.md), in Chinese.

| Scenario / metric | Before | After | Test scope |
| --- | --- | --- | --- |
| KPB console model enlarged and continuously rotated | 45.66–46.28 FPS | 57.40–57.50 FPS | Alternating A/B runs with the same action; batched dot-background rendering |
| KPB GBA cartridge left/right switching | 36.45–36.61 FPS | 39.07–39.30 FPS | A/B tests through the same actual input-dispatch path |
| P95 frame interval during the GBA switching test | About 82.64 ms | About 49.56 ms | Reduced long-frame interval, not average frame time |
| Draw calls in the enlarged-console scene | About 1,562 | About 111 | Fewer calls per frame after batching the background |
| Mean cold startup across three earlier runs | 17.40 s | 17.03 s | Same-method 2026-10-25 report; about 2.1% improvement |
| Eight-model cache preparation in that earlier test | 21.13 s | 20.24 s | Earlier build; about 4.2% improvement, not first-screen waiting time |

A separate stable build without diagnostic probes measured **41.19 FPS** while stationary on the GBA cartridge page and **39.34 FPS** during left/right switching. A 30-second switching sample recorded no frames above 100 ms. Different pages and actions must be compared separately: a console-model scene approaching 60 FPS does not mean every scene runs at a stable 60 FPS.

**Memory, power use and warm startup:** eight-model caching is retained. There is no complete comparable dataset for memory, power consumption or warm startup in this round, so no reduction percentage is claimed. In particular, the project does not claim a 50% reduction in cold or warm startup. Earlier records: [background memory and resume testing](docs/reports/2026-10-25-background-model-cache.md) and [cold-start testing](docs/reports/2026-10-25-startup-optimization.md), in Chinese.

## KPB on-device gallery

These are screenshots from a KPB. The [complete gallery contains 27 screenshots](docs/SHOWCASE.md), covering loading progress, eight consoles, enlarged models and rotation, collections, creation/editing, search, apps and settings.

| Cartridge browsing | Console selection |
| --- | --- |
| ![Game library](docs/images/showcase/game-library.png) | ![Console chooser](docs/images/showcase/model-gba.png) |

| Collection management | Game search |
| --- | --- |
| ![Collections](docs/images/showcase/collections.png) | ![Search](docs/images/showcase/search.png) |

<details>
<summary>Preview the pixel loading screen and About page</summary>

![Actual loading progress](docs/images/showcase/startup-13.png)

![About page](docs/images/showcase/about.png)

</details>

## Before installing or upgrading

- **Existing Socket BBM / Replay / CARTIS users:** this APK keeps the original package name and signing certificate. Upgrade in place; do not uninstall or clear app data. Back up your configuration and saves before upgrading.
- **KPB 3 GB:** the main tested device. At a previously verified stable checkpoint with the existing quality settings, the stationary GBA cartridge page measured about **41.19 FPS**, and switching measured about **39.34 FPS**. Results vary by scene, device state and library; these are **not stable 60 FPS** claims.
- **KPA:** layout adaptation is implemented and historical releases were checked at 960×640. The complete 2.27 package has been tested on KPB only and has not been retested on KPA. Other displays use adaptive layouts, but adjustments may still be needed.
- **KPB 2 GB:** not tested on a physical device for this release. Caching eight models uses substantial memory; High Frame Rate is not a low-memory mode. Back up first and choose your version carefully.
- **Quality options:** High Detail and High Frame Rate can be selected separately. Emulator compatibility and in-game frame rates depend on the chosen emulator, core and device.

Earlier 2.0 performance experiments have ended. The release retains the verified optimizations and excludes experiments that removed refraction, made cartridge shells opaque, further reduced clarity or switched to OpenGL. See the [2.0 update notes](docs/releases/CARTIS-2.0-20261027.md), in Chinese, for scope and validation details.

## Origins and credits

CARTIS is based on **Socket 0.6**, originally created by **depmots**. Original project: [depmots.com/socket](https://depmots.com/socket).

Independently modified by **Creepynuts**, who uses the same name on Xiaohongshu. Thanks to **HI问风 (bilibili)** for resources and Chinese localization.

CARTIS is an independent modification and does not represent the original author or any platform manufacturer. See [LICENSING.md](LICENSING.md) for the licensing scope of documentation, third-party programs, images and assets.

If you enjoy the project, you can provide voluntary support through **Settings → Support**. International users can also use [PayPal](https://paypal.me/seabird26).

## Roadmap for 3.0

These are plans for the next stage and **have not been released as 3.0 features**. The 2.x features listed above are already implemented.

- **Twelve more console models** to expand platform presentation and selection.
- **Customizable personal pages** for displaying your collections and arranging a personal space.
- **More interface languages**, including English and Traditional Chinese.
- **More fonts, under evaluation**, to find additional options suited to handheld displays.
- **Regional cartridge designs**, such as distinguishing North American NES cartridges from Japanese Famicom cartridges.

### Personal-page design concept

This is a 3.0 personal-page concept. **It is not a screenshot of the current app and does not represent a final implementation.**

![CARTIS 3.0 personal-page concept](docs/images/cartis-3-profile-concept.png)

## Setup guide

- [First-time setup](#first-time-start-here)
- [Step 1: Install CARTIS](#step-1-install-cartis)
- [Step 2: Install the emulators first](#step-2-install-the-emulators-first)
- [Step 3: Organize games and cover art](#step-3-organize-games-and-cover-art)
- [Step 4: Add your platforms to CARTIS](#step-4-add-your-platforms-to-cartis)
- [Everyday controls](#everyday-controls)
- [Troubleshooting](#troubleshooting)

---

## First time? Start here

**Install CARTIS → install emulators → organize games and cover art → add platforms in CARTIS.**

CARTIS is the interface for choosing and launching games. The emulators run them, so installing CARTIS alone is not enough to play.

## Step 1: Install CARTIS

1. [Download the latest APK](https://github.com/FredZ6/CARTIS/releases/download/v2.27/CARTIS-2.27.apk) or open the [latest release page](https://github.com/FredZ6/CARTIS/releases/tag/v2.27).
2. Under **Assets**, choose **`CARTIS-2.27.apk`** (versionCode 27), the package tested on KPB. KPA and other-device users should read the validation scope above; users of 2 GB devices should also read the memory notes. `Source code` is not the installer.
3. Open the APK in the handheld's file manager. If Android asks for permission to install apps, follow its prompts.
4. Existing users should install over the previous version. **Do not uninstall or clear app data first**, or you may lose your configuration.

> **First launch:** the app shows a pixel-art loading screen, progress bar and current stage. Wait for the library to appear instead of repeatedly opening the app.

To return to CARTIS with the Home button, open Android **Settings → Default apps → Home app** and choose **CARTIS**. Names vary by device.

Change fonts under **Settings → Adjust (调整)**. The latest release fixes the black-screen/exit issue when changing fonts; selecting a font refreshes the interface and saves it automatically.

## Step 2: Install the emulators first

**CARTIS does not install emulators or cores for you.** Think of CARTIS as the game shelf, an emulator as a console, and a RetroArch core as the component that emulates a particular system.

### Choose the systems you want to play

The links below point to emulator websites or official project documentation. Select **Android / APK**, not a Windows or macOS build.

| Platform | Emulator / core | Download and notes |
| --- | --- | --- |
| **GBA** | RetroArch + **mGBA** core | [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk) · [mGBA documentation](https://docs.libretro.com/library/mgba/) |
| **GB / GBC** | RetroArch + **Gambatte** core | [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk) · [Gambatte documentation](https://docs.libretro.com/library/gambatte/) |
| **NDS / DS** | RetroArch + **melonDS DS** core | [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk) · [melonDS DS documentation](https://docs.libretro.com/library/melonds_ds/) |
| **PSP** | Standalone **PPSSPP** | [PPSSPP downloads](https://www.ppsspp.org/download/); choose **APK for Android** |
| **PS1 / PSX** | RetroArch + **PCSX ReARMed** core | [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk) · [PCSX ReARMed documentation](https://docs.libretro.com/library/pcsx_rearmed/) |
| **3DS** | Standalone **Azahar** | [Azahar website](https://azahar-emu.org/); follow its download link and choose Android |
| **PS2** | You can try RetroArch + the **Play!** core, or another PS2 launch entry in CARTIS that matches your installed app | [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk) · [Play! documentation](https://docs.libretro.com/library/play/); the core is experimental and is not the first choice for beginners |

**You do not need to install everything.** For GBA alone, start with RetroArch and mGBA. For GBA and PS1, install one copy of RetroArch and add both cores. Standalone emulators such as PPSSPP are separate APKs.

3DS and PS2 require more device performance and have game-specific compatibility limits. Showing a console model does not guarantee that your handheld can run every game for that platform smoothly. Not every listed setup has been individually tested on every device.

### Example: install RetroArch and mGBA for GBA

**A. Install RetroArch itself**

1. Open the [RetroArch Android download](https://buildbot.libretro.com/stable/1.22.2/android/RetroArch.apk).
2. Choose the APK matching your device's Android architecture: **Download (64bit)** for a 64-bit system, **Download (32bit)** for a 32-bit system. If unsure, check the device documentation; do not install several variants at once.
3. Install the APK through the file manager, open RetroArch once and allow access to your game folder when prompted.

The RetroArch website notes that its Google Play build is older and recommends downloading from the website. If the handheld cannot reach the site, download the APK on a computer and copy it to the device.

**B. Download the mGBA core inside RetroArch**

With an internet connection, follow:

```text
Main Menu
  ↓
Load Core
  ↓
Download a Core
  ↓
Nintendo - Game Boy Advance (mGBA)
  ↓
Download and wait for completion
```

Some interfaces also provide **Online Updater → Core Downloader**. Menu wording varies with version and language; see the [official core installation guide](https://docs.libretro.com/guides/download-cores/).

**mGBA here is a RetroArch core, not another Android app to install.** Download other RetroArch cores the same way, choosing the corresponding system/core name.

**C. Test the game directly in RetroArch first**

1. Return to the main menu and choose **Load Core → mGBA**.
2. Choose **Load Content** and open your `.gba` file.
3. Confirm the game works, then return to CARTIS and add the GBA platform.

If the core list does not load, check the network connection and where RetroArch was downloaded. Changing an option in CARTIS cannot install a missing core.

### PSP: install the standalone PPSSPP app

1. Open [PPSSPP downloads](https://www.ppsspp.org/download/) and choose **APK for Android**, then install it.
2. Open PPSSPP, allow access to the PSP game folder and launch a game to confirm it works.
3. Add PSP in CARTIS and select **PPSSPP** as the emulator.

Standalone PPSSPP does not require downloading a PSP core in RetroArch. RetroArch also has a PPSSPP core, but that is a different launch setup; do not mix the two configurations.

### Select the matching emulator and core in CARTIS

Press **Y → Platforms (平台) → Add Platform (添加平台)**, or edit an existing platform. Select the game folder and the emulator you have actually installed.

| Your installed setup | Select in CARTIS |
| --- | --- |
| RetroArch 64-bit with mGBA installed | The matching **RetroArch 64 / mGBA** entry |
| RetroArch 32-bit with mGBA installed | The matching **RetroArch 32 / mGBA** entry |
| Another RetroArch package with mGBA installed | The **RetroArch / mGBA** entry matching that app |
| Standalone PPSSPP | The **PPSSPP** entry, not RetroArch's PPSSPP core |
| Azahar | The **Azahar** entry matching your installed app; do not choose an old Citra / Lime3DS entry just because its name looks similar |

**You do not need to select or authorize a `cores` folder.** CARTIS only checks whether the emulator app is installed. Core names in the list are predefined platform options, not confirmation that the core is installed. Choose the game folder normally; RetroArch loads the selected core itself. Users of customized Tianma emulator packages do not need to replace their emulator just to grant core-folder access.

The exact option names depend on the current CARTIS list. **The installed app, core and launch entry must match.** For example, selecting RetroArch 64 without a 64-bit RetroArch installation can fail, as can selecting a core you have not downloaded.

### BIOS and system files

BIOS files are system files some consoles need to start. **Not every platform or core requires a separate BIOS**; for example, the GBA BIOS is optional for mGBA.

When a BIOS or firmware is required, follow the corresponding core's official documentation and use files you have the right to use. In RetroArch, check **Settings → Directory → System/BIOS** for the actual path instead of copying somebody else's storage path. Standalone emulators have their own settings.

**Test the game in the emulator before launching it from CARTIS.** The CARTIS APK does not include games, BIOS files, emulators or input methods, and will not install those components for you.

## Step 3: Organize games and cover art

Game resources and cover art are linked here: [Quark cloud drive](https://pan.quark.cn/s/8deecaf6406f). Use only resources you have the right to use.

Additional resources: [TianmaG custom configuration pack index (Tencent Docs, in Chinese)](https://docs.qq.com/sheet/DZVBNVmxNZ29GZ2Fn).

Get one GBA game working first, then organize the other platforms.

### Create a game folder

In the handheld's **internal storage**, create a folder such as `天马游戏包`, with a `GBA` folder inside it. Put the GBA game files in that folder.

The file manager may call internal storage “Device storage.” `天马游戏包` is only a suggested folder name; you can choose another name or store your games on an SD card.

### Create a cover-art folder inside the game folder

Inside `GBA`, create **`lmgs`** and place the cover images there. The first character is a **lowercase letter l**, not an uppercase I.

![Game and cover-art folder layout](docs/images/folder-guide.svg)

### Match each cover's filename to the game

For a game named `口袋妖怪 水银.gba`, use a cover named `口袋妖怪 水银.png`: keep the same base filename.

![Matching game and cover filenames](docs/images/cover-name-guide.svg)

PNG and JPG are recommended; JPEG, WebP and BMP are also supported. Renaming an extension does not convert the image format.

Use the same arrangement for other systems:

```text
天马游戏包/
├── GBA/      ← GBA games, with a separate lmgs folder inside
├── NDS/      ← NDS games, with a separate lmgs folder inside
├── PSP/      ← PSP games, with a separate lmgs folder inside
└── PS1/      ← PS1 games, with a separate lmgs folder inside
```

If a download is an archive containing the game files, extract it before organizing it. Supported game formats depend on the emulator and platform scanner. Keep any companion files belonging to disc-based games together.

## Step 4: Add your platforms to CARTIS

1. Press **Y** on the CARTIS main screen, or tap **Settings** at the bottom left.
2. Choose **Platforms → Add Platform → GBA**.
3. Choose the installed emulator and configure the matching core or launch entry.
4. Select your game folder, for example **`天马游戏包/GBA`**, and grant access.
5. Save, wait for scanning to finish and return to the main screen.

**Select the GBA game folder, not `lmgs`.** The `lmgs` folder contains cover images, not games.

![Adding platforms and configuring keys](docs/images/setup-guide.svg)

Add PSP, NDS and other platforms separately. Creating a folder does not add a platform to CARTIS and does not install an emulator.

## Everyday controls

These are the defaults. If you have remapped the buttons, follow the on-screen hints.

| Main-screen input | Action |
| --- | --- |
| D-pad left/right | Select another game |
| A | Launch the selected game |
| B | Open the app list |
| Y | Open settings |
| X | View game details |
| Select | Open collections for the current platform |
| Start | Open game search |
| L or R individually | Switch to the previous / next collection |
| L + R together | Open the console/platform chooser |
| D-pad left + R1 | Go directly to the previous platform's game list |
| D-pad right + R1 | Go directly to the next platform's game list |

In collection and platform pages, use the **D-pad to select, A to enter and B to go back**.

Select opens This Platform's collections by default. In the collection page, press **L/R** or tap the top tabs to switch between **This Platform / All Platforms**. Use **Y to create** and **X to edit**. The editor supports renaming, deletion and moving a collection earlier or later in the order. Global collections can contain games from different systems. Press X on a game and use the two separate collection controls to manage local and global membership.

Search covers every added platform. Type using the touchscreen, select a result with D-pad up/down and press **A to locate its cartridge**, without launching the game. Press A again on the cartridge page to run it. **B first closes the keyboard; press B again to return to the main screen.**

Tap the middle cartridge or console model to enlarge it, drag to rotate it, and tap the model again or press B to exit.

### Adjust visuals and interactions under Performance

Open **Settings → Performance (性能)** to adjust **Console Model Quality** and **Game Model Quality** separately:

- **High Detail:** keeps the full material effects.
- **High Frame Rate:** simplifies some expensive material calculations while retaining covers and transparent cartridge materials. Frame rates still depend on the device, platform and scene.

The same page has independent switches for **console-model interactions, cartridge-page startup sounds and background audio**, plus **upward swipe to launch**. That last option is off by default, so launching uses a downward swipe. Changes save automatically and survive restarts.

A fresh installation defaults to **High Frame Rate**, with the three interaction/audio switches enabled. Upgrading preserves saved settings.

### Customize the buttons

Open **Settings → Key Bindings (按键)**:

1. Select a function, such as Collections.
2. Press the physical button or combination you want to use, for example L + R.
3. Release all buttons, then tap **Save Binding**.

Changes take effect immediately, persist across launches and update the bottom hints. Combinations of up to three buttons are supported. Previous Platform and Next Platform default to D-pad left + R1 / D-pad right + R1 and jump directly between platform libraries.

- **“Button already in use”:** cancel and choose another binding, or replace it. Replacing a conflict leaves the other function unbound.
- To undo your custom bindings, choose **Restore Default Keys**.
- To cancel recording, tap **Cancel Recording** or use Android Back. B itself can be recorded, so it is not a fixed cancel key during recording.
- The D-pad alone still navigates. Left/right can be combined with other buttons; up/down retain their normal role. Android handles Home; set CARTIS as the default Home app if you want that behaviour.

These settings affect CARTIS only. Configure fast-forward, save states and other emulator shortcuts inside the emulator.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| Games do not appear | Did you select the actual game folder? Are files extracted? Was access granted? Is the format supported? |
| Games appear without covers | Are images in that platform's `lmgs` folder? Do the base filenames match? Can the images be opened normally? |
| Newly added games are missing | Rescan from platform settings. Do not delete your existing configuration just because you copied in new files. |
| A changed cover still looks old | Reopen CARTIS; if needed, select the cover manually in the game's customization screen. |
| A game will not launch | Test it directly in the emulator first, then check CARTIS's emulator, core and launch-entry choices. |
| The keyboard opens but typing does not work | Switch the keyboard to English, then back to Chinese. If necessary, install another Chinese input method separately. |
| Home does not return to CARTIS | Check Android's default Home app setting. |

Folder layout, cover naming and permission problems do not require uninstalling CARTIS or clearing all its data.

## Repository rename and old links

The repository was renamed from **`FredZ6/kpb-socket`** to **`FredZ6/CARTIS`**. GitHub redirects old repository pages, file links and release links to the new address, preserving Stars, Issues and commit history. Bookmark [github.com/FredZ6/CARTIS](https://github.com/FredZ6/CARTIS).

README views retain the old counter key so the rename does not reset the count. Downloads cover historical Release assets; caching affects the displayed numbers, and they are not installation counts.

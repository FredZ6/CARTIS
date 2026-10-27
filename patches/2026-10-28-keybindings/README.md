# 按键绑定修复与游戏平台直接切换

对应 `v2.0-keybindings-fix-20261028`，versionCode 20；基准为 `v2.0-core-rollback-20261028`，versionCode 19。

两个补丁分别应用到解密后的 `res://bbm_keys/router.gd` 与 `res://scripts/screens/screen_main_menu_hb.gd`。不包含原 APK、加密密钥、设备配置或游戏文件。

- 统一通过绑定路由器解析平台入口，取消语义上下平台动作形成的隐式组合。
- 增加可改绑的前/后游戏平台动作，默认十字键左/右＋R1，仅在主游戏列表生效。
- 普通方向键继续导航，成功组合才拦截；允许持续持有 R1 连续点方向，防止尾部误触。
- 选择页和快捷切换共用平台进入逻辑，直接进入完整游戏列表。

测试需要自备相应版本授权提取的脚本，放在本目录的 `backup/` 和应用补丁后的 `source/`。`tests/run.py` 提取并实际执行生产状态机及页面输入方法，页面渲染使用测试替身。运行：

```sh
GODOT_BIN=/absolute/path/to/godot python3 tests/run.py --fixed
```

运行时使用的 Godot 应兼容本版本脚本语法；本次桌面运行时为 GDRE 内置 Godot 4.8.dev，目标 KPB 为 APK 原有 Godot 4.7.1 custom。桌面检查与目标设备测试范围见 [完整报告](../../docs/reports/2026-10-28-keybindings.md)。

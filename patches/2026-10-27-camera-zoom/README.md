# 相机缩放修复源码

目标资源：`res://scenes/camera_zoom_3d.gdc`。src中的GDScript应使用与目标项目匹配的字节码编译，并经原资源加密、索引与签名流程打包；本目录不包含完整Socket项目、密钥或签名材料。

运行回归测试（需要Godot）：

```sh
godot --headless --path patches/2026-10-27-camera-zoom --script tests/zoom_test.gd
```

该测试覆盖雾化偏移、重复切换、缩放上下限及多相机环境隔离。完整发行APK另见Releases。

extends SceneTree
func _initialize() -> void:
	call_deferred("run")
func run() -> void:
	var scene := Node3D.new()
	root.add_child(scene)
	var world_env := WorldEnvironment.new()
	var original := Environment.new()
	original.fog_enabled = true
	original.fog_mode = Environment.FOG_MODE_DEPTH
	original.fog_depth_begin = 16.8
	original.fog_depth_end = 19.4
	world_env.environment = original
	scene.add_child(world_env)
	var camera = load("res://src/camera_zoom_3d.gd").new()
	scene.add_child(camera)
	for zoom in [1.0, 0.9, 0.8, 0.5, 0.1, 1.05, 2.0, 3.0, 0.8, 1.0]:
		camera.set_zoom(zoom)
		var env: Environment = camera.environment if camera.environment else original
		var distance: float = -camera.position.z
		var offset: float = maxf(0.0, distance - 15.841)
		if absf(env.fog_depth_begin - (16.8 + offset)) > 0.001 or absf(env.fog_depth_end - (19.4 + offset)) > 0.001:
			printerr("FAIL zoom=", zoom, " fog range=", env.fog_depth_begin, "/", env.fog_depth_end, " camera distance=", distance)
			quit(1)
			return
		if not is_equal_approx(original.fog_depth_begin, 16.8) or not is_equal_approx(original.fog_depth_end, 19.4):
			printerr("FAIL shared world environment mutated")
			quit(1)
			return
	var second = load("res://src/camera_zoom_3d.gd").new()
	scene.add_child(second)
	second.set_zoom(0.8)
	camera.set_zoom(1.0)
	if second.environment == camera.environment or not is_equal_approx(second.environment.fog_depth_begin, 20.76025):
		printerr("FAIL cameras must have independent fog ranges")
		quit(1)
		return
	print("PASS zoom fog regression: 0.5, 0.8, 0.9, 1.0, 1.05, 2.0 and repeated transitions")
	quit(0)

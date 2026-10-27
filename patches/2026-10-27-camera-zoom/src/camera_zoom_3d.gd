extends Camera3D

const _BASE_Z: = -15.841

var _zoom_environment: Environment
var _base_fog_begin: float
var _base_fog_end: float

func set_zoom(zoom: float) -> void :
	position.z = _BASE_Z / clampf(zoom, 0.5, 2.0)
	if not is_inside_tree():
		return
	if _zoom_environment == null:
		var source: Environment = environment
		if source == null:
			source = get_world_3d().environment
		if source == null or not source.fog_enabled or source.fog_mode != Environment.FOG_MODE_DEPTH:
			return
		# Keep other cameras and the shared world environment unchanged.
		_zoom_environment = source.duplicate() as Environment
		_base_fog_begin = source.fog_depth_begin
		_base_fog_end = source.fog_depth_end
		environment = _zoom_environment
	# Zooming out moves the camera back; keep the fog at the same world depth.
	var retreat := maxf(0.0, _BASE_Z - position.z)
	_zoom_environment.fog_depth_begin = _base_fog_begin + retreat
	_zoom_environment.fog_depth_end = _base_fog_end + retreat

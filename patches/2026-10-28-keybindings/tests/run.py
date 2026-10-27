from pathlib import Path
import re,subprocess,sys,os
r=Path(__file__).resolve().parents[1]; fixture=r/'tests/runtime';fixture.mkdir(exist_ok=True)
source=r/('source' if '--fixed' in sys.argv else 'backup')
def method(text,name):
 m=re.search(r'^func '+re.escape(name)+r'\(.*?(?=^func |\Z)',text,re.M|re.S);assert m,name
 return m[0].rstrip()+'\n'
main=(source/'screen_main_menu_hb.gd').read_text();router=(source/'router.gd').read_text()
# Execute the actual production routing/state-machine methods with inert page actions.
core='extends RefCounted\nvar bindings := {}\nvar overrides := {}\nvar held := {}\nvar active := {}\nvar pending := {}\nvar blocked := {}\nvar axes := {}\nvar events := []\nvar page\nvar injecting := false\nvar capture_action := ""\nvar capture_ready := false\nvar focus_overlay: Control\nvar test_scope := "main"\nvar test_viewport := TestViewport.new()\nconst CFG_PATH := "res://test-bindings.cfg"\n'
for line in router.splitlines():
 if line.startswith(('const ACTIONS','const EVENTS','const SCOPES','const TITLES')):core+=line+'\n'
for name in ['defaults','_handle','conflicts','_event_token','_valid_token','_uses_token','_eligible_uses','_runtime_uses','_load_bindings','_save_bindings','commit','restore_defaults','_release_all','_keyboard_alias','_valid_binding','_direction_token','_input','_chord_blocked']:
 core+=method(router,name).replace("ControlIcons.get_style()", "'nintendo'")
core+='''
func _send(action: String, pressed: bool) -> void:
 events.append([action,pressed])
 if page != null:
  var event := InputEventAction.new()
  event.action = EVENTS[action]
  event.pressed = pressed
  page._hb_console_input(event)
class TestViewport:
 extends RefCounted
 var handled := false
 func get_focus_owner(): return null
 func gui_get_focus_owner() -> Control: return null
 func set_input_as_handled(): handled = true
func get_viewport() -> TestViewport: return test_viewport
func context() -> String: return test_scope
func _capture_input(_parsed,_event): pass
func _refresh_axis_bindings(): pass
func _refresh_rows(): pass
func refresh_hints(): pass
func _status(_text): pass
func binding_text(action): return str(bindings[action])
func reset() -> void:
 held.clear()
 active.clear()
 pending.clear()
 blocked.clear()
 axes.clear()
 events.clear()
 bindings = defaults()
 overrides.clear()
'''
(fixture/'router.gd').write_text(core.expandtabs(1))
# Extract up to touch handling; navigation/open/back/confirm behavior stays unchanged.
page=method(main,'_hb_console_input');page=page[:page.index('\telif event is InputEventScreenTouch:')]+'\n\treturn true\n'
(fixture/'page.gd').write_text('''extends Node
var _bbm_keys_router
var is_current := true
var _hb_console_zoomed := false
var _hb_picker
var _hb_find
var _hb_preview
var screen_inspect = {"is_open":false}
var screen_customize = {"is_open":false}
var _hb_console_left := false
var _hb_console_right := false
var _hb_console_pending := 0
var _hb_console_chord := false
var _hb_picker_suppress_apps_release := false
var _hb_console_repeat := 0.0
var opened := false
var toggles := 0
var moves := []
func _hb_console_is_open(): return opened
func _hb_console_open():
 opened = true
 toggles += 1
func _hb_console_close():
 opened = false
 toggles += 1
func _hb_console_move(side): moves.append(side)
func _change_platform(side): moves.append(side)
func _hb_console_choose(): opened = false
func _hb_console_zoom_input(_event): return true
var _hb_scope_key := ''
var platforms := [{'id':'gba'},{'id':'nds'},{'id':'psp'}]
var entered := []
var busy := false
func _hb_console_available() -> Array: return platforms
func _hb_plat_key(platform) -> String: return platform.id
func _hb_page_transition_busy(): return busy
func _stop_move_carousel(): pass
func _hb_console_enter_platform(platform):
 _hb_scope_key = platform.id
 entered.append(platform.id)
'''+method(main,'_hb_console_shoulder')+method(main,'_hb_console_quick_switch')+page.replace("for screen in Screen.screens_open: stack.append(String(screen.id))","pass"))
(fixture/'page.gd').write_text((fixture/'page.gd').read_text().expandtabs(1))
(fixture/'project.godot').write_text('config_version=5\n[application]\nconfig/name="CARTIS key regression"\nconfig/use_custom_user_dir=true\nconfig/custom_user_dir_name="/private/tmp/cartis-key-regression"\n')
engine=Path(os.environ.get('GODOT_BIN',str(r.parent/'Replay-2.0-20261026/tools/gdre/Godot RE Tools.app/Contents/MacOS/Godot RE Tools')))
p=subprocess.run([str(engine),'--headless','--path',str(fixture),'--script',str(r/'tests/suite.gd'),'--log-file',str(r/'diagnostics/runtime-engine.log')],capture_output=True,text=True,timeout=40)
output=p.stdout+p.stderr
(r/'diagnostics'/('green.log' if '--fixed' in sys.argv else 'red.log')).write_text(output)
print(output);sys.exit(0 if p.returncode==0 and 'ALL PASS' in output and 'SCRIPT ERROR' not in output else 1)

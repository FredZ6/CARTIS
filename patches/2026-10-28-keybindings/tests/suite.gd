extends SceneTree
var router
var page
var failures := 0
var checks := 0
func check(ok: bool, label: String):
 checks += 1
 if not ok:
  failures += 1
  print('FAIL ',label)
func tap(token: String, scope := 'main'):
 router._handle(token,true,'joy:0',scope)
 router._handle(token,false,'joy:0',scope)
func chord(tokens: Array, scope := 'main'):
 for token in tokens: router._handle(token,true,'joy:0',scope)
 for token in tokens: router._handle(token,false,'joy:0',scope)
func reset():
 router.reset()
 page.opened = false
 page.toggles = 0
 page.moves.clear()
 page._hb_console_left = false
 page._hb_console_right = false
 page._hb_console_chord = false
 page._hb_console_pending = 0
func _initialize(): call_deferred('run')
func run():
 router = load('res://router.gd').new()
 page = load('res://page.gd').new()
 root.add_child(page)
 page._bbm_keys_router = router
 router.page = page
 for action in router.EVENTS.values():
  if not InputMap.has_action(action): InputMap.add_action(action)
 reset()
 router.bindings.platforms = ['j:4','j:6']
 router._handle('j:9',true,'joy:0','main')
 router._handle('j:10',true,'joy:0','main')
 check(page.toggles == 0,'rebound platforms: L+R cannot open page')
 router._handle('j:9',false,'joy:0','main')
 router._handle('j:10',false,'joy:0','main')
 check(page.moves == [-1,1],'independent previous/next keep working')
 chord(['j:4','j:6'])
 check(page.toggles == 1 and page.opened,'Select+Start opens exactly once')
 check(router.events.filter(func(e): return e[0] in ['search','collections']).is_empty(),'chord does not open search or collections')
 reset()
 chord(['j:9','j:10'])
 check(page.toggles == 1 and page.opened and page.moves.is_empty(),'default L+R opens once without navigation')
 reset()
 router.bindings.previous = ['k:80']
 router.bindings.next = ['k:81']
 router._handle('k:80',true,'keyboard','main')
 router._handle('k:81',true,'keyboard','main')
 check(page.toggles == 0,'new previous+next must not form hidden platforms shortcut')
 for action in router.ACTIONS:
  reset()
  var old: Array = router.bindings[action].duplicate()
  var scope: String = router.SCOPES[action][0]
  var new_token := 'k:4194330'
  router.bindings[action] = [new_token]
  chord(old,scope)
  check(router.events.filter(func(e): return e[0] == action).is_empty(),action+': old binding disabled')
  router.events.clear()
  tap(new_token,scope)
  check(router.events == [[action,true],[action,false]],action+': new binding fires once')
 for action in router.ACTIONS:
  for scope in ['main','gui','picker','search','platforms','preview']:
   reset()
   for other in router.ACTIONS: router.bindings[other] = []
   router.bindings[action] = ['j:7']
   tap('j:7',scope)
   check((not router.events.is_empty()) == (scope in router.SCOPES[action]),action+': scope '+scope)
 reset()
 router.bindings.platforms = ['j:4','j:6']
 tap('j:4');check(router.events == [['collections',true],['collections',false]],'Select alone retains collection action')
 router.events.clear();tap('j:6');check(router.events == [['search',true],['search',false]],'Start alone retains search action')
 router.events.clear()
 router._handle('j:4',true,'joy:0','main');router._handle('j:6',true,'joy:1','main')
 check(router.events.is_empty(),'different controllers cannot form chord')
 reset()
 check(router.conflicts('search',router.bindings.collections) == ['collections'],'shared scope conflict detected')
 check(router.conflicts('apps',router.bindings.back).is_empty(),'apps/back allowed in separate scopes')
 for tokens in [['j:4','j:6'],['j:6','j:4']]:
  reset();router.bindings.platforms = ['j:4','j:6'];chord(tokens)
  check(router.events == [['platforms',true],['platforms',false]],'chord order '+str(tokens))
 reset()
 var e := InputEventJoypadMotion.new();e.axis = JOY_AXIS_TRIGGER_LEFT
 e.axis_value = 0.7;check(router._event_token(e).pressed,'trigger press threshold')
 e.axis_value = 0.5;check(router._event_token(e).is_empty(),'trigger hysteresis prevents repeat')
 e.axis_value = 0.3;check(not router._event_token(e).pressed,'trigger release threshold')

 for action in router.ACTIONS:
  reset()
  var scope: String = router.SCOPES[action][0]
  check(router.commit(action,['j:7','j:8']),'commit two-key '+action)
  router.events.clear()
  chord(['j:8','j:7'],scope)
  check(router.events == [[action,true],[action,false]],'two-key remap '+action)
  router.events.clear()
  chord(['j:7','j:8'],scope)
  check(router.events == [[action,true],[action,false]],'two-key repeat cycle '+action)
  router._load_bindings()
  check(router.bindings[action] == ['j:7','j:8'],'reload saved two-key '+action)
  check(router.commit(action,['j:7','j:8','j:15']),'commit three-key '+action)
  router.events.clear()
  chord(['j:15','j:8','j:7'],scope)
  check(router.events == [[action,true],[action,false]],'three-key remap '+action)
  router.restore_defaults()
  check(router.bindings == router.defaults() and router.overrides.is_empty(),'restore defaults '+action)
 reset()
 check(not router.commit('search',router.bindings.collections),'conflict save rejected')
 check(router.bindings == router.defaults(),'rejected conflict leaves original bindings')
 check(router.commit('search',router.bindings.collections,true),'replace conflict saves')
 check(router.bindings.collections.is_empty(),'replaced action explicitly unbound')
 router._load_bindings()
 check(router.bindings.collections.is_empty() and router.bindings.search == ['j:4'],'replacement survives restart')
 router.restore_defaults()
 reset()
 router._handle('j:9',true,'joy:0','main')
 router._release_all()
 router._handle('j:9',false,'joy:0','main')
 check(router.events.is_empty() and router.held['joy:0'].is_empty(),'focus loss clears delayed prefix')
 reset()
 router._handle('j:1',true,'joy:0','picker')
 router._handle('j:1',false,'joy:0','main')
 check(router.events == [['back',true],['back',false]],'back release does not open apps after context change')
 reset()
 for i in 5: router._handle('j:3',true,'joy:0','main')
 router._handle('j:3',false,'joy:0','main')
 check(router.events == [['settings',true],['settings',false]],'repeated down emits only one press')
 reset()
 router.overrides.platforms = ['j:4','j:6']
 var alias := InputEventKey.new();alias.keycode = KEY_F5;alias.pressed = true
 check(router._keyboard_alias(alias,'main') and router.events.is_empty(),'F5 alias disabled for overridden platforms')
 router.overrides.clear()
 check(router._keyboard_alias(alias,'main') and router.events == [['platforms',true]],'F5 alias available for default platforms')
 router.restore_defaults()

 reset()
 check(router.bindings.get('platform_previous') == ['j:13','j:10'],'default left+R1 previous platform')
 check(router.bindings.get('platform_next') == ['j:14','j:10'],'default right+R1 next platform')
 check(router._valid_token('j:13') and router._valid_token('j:14'),'horizontal dpad accepted for chords')
 if router.bindings.has('platform_previous'):
  for item in [['platform_previous','j:13'],['platform_next','j:14']]:
   for tokens in [[item[1],'j:10'],['j:10',item[1]]]:
    reset();chord(tokens)
    check(router.events == [[item[0],true],[item[0],false]],'platform chord order '+str(tokens))
  reset()
  check(not router.commit('platform_next',['j:14']),'standalone dpad cannot be bound')
  check(not router.commit('platform_next',['j:13','j:14']),'direction-only chord cannot be bound')
  check(not router._valid_token('j:11') and not router._valid_token('j:12'),'vertical dpad remains reserved')

 reset()
 var direction := InputEventJoypadButton.new();direction.button_index = JOY_BUTTON_DPAD_RIGHT;direction.pressed = true
 router.test_scope = 'main';router.test_viewport.handled = false
 router._input(direction)
 check(not router.test_viewport.handled and router.events.is_empty(),'ordinary right dpad passes through native navigation')
 var r1 := InputEventJoypadButton.new();r1.button_index = JOY_BUTTON_RIGHT_SHOULDER;r1.pressed = true
 router._input(r1)
 check(router.events == [['platform_next',true]],'direction first then R1 resolves only platform next')
 direction.pressed = false;router.test_viewport.handled = false;router._input(direction)
 check(router.test_viewport.handled,'claimed chord direction release is consumed')
 r1.pressed = false;router._input(r1)
 check(router.events == [['platform_next',true],['platform_next',false]],'chord suppresses R1 collection step')
 reset()
 r1.pressed = true;router._input(r1)
 direction.pressed = true;router.test_viewport.handled = false;router._input(direction)
 check(router.test_viewport.handled,'R1-first chord consumes dpad press')
 check(router.events == [['platform_next',true]],'R1-first chord fires once')
 reset()
 router.commit('platform_next',['j:7'])
 r1.pressed = true;router._input(r1)
 direction.pressed = true;router.test_viewport.handled = false;router._input(direction)
 check(not router.test_viewport.handled and router.events.is_empty(),'rebound direction+R1 no longer triggers old chord')
 direction.pressed = false;router._input(direction);r1.pressed = false;router._input(r1)
 check(router.events == [['next',true],['next',false]],'R1 navigation restored after platform remap')
 reset()
 router.test_scope = 'gui';direction.pressed = true;router.test_viewport.handled = false;router._input(direction)
 check(not router.test_viewport.handled,'settings dpad navigation passes through')
 router.restore_defaults()

 reset()
 page._hb_scope_key = 'gba';page.entered.clear()
 page._hb_console_quick_switch(1)
 check(page.entered == ['nds'] and not page.opened,'quick next enters adjacent library without chooser')
 page._hb_console_quick_switch(-1)
 check(page._hb_scope_key == 'gba','quick previous returns to previous platform')
 page._hb_console_quick_switch(-1)
 check(page._hb_scope_key == 'psp','previous wraps to last platform')
 page._hb_console_quick_switch(1)
 check(page._hb_scope_key == 'gba','next wraps to first platform')
 page._hb_scope_key = 'removed';page._hb_console_quick_switch(1)
 check(page._hb_scope_key == 'gba','missing scope next selects first visible platform')
 page._hb_scope_key = '';page._hb_console_quick_switch(-1)
 check(page._hb_scope_key == 'psp','unscoped previous selects last platform')
 page.platforms = [];page.entered.clear();page._hb_console_quick_switch(1)
 check(page.entered.is_empty(),'empty platforms handled without navigation')
 page.platforms = [{'id':'gba'}];page._hb_console_quick_switch(1)
 check(page._hb_scope_key == 'gba','single platform safe')
 page.entered.clear();page.is_current = false;page._hb_console_quick_switch(1)
 check(page.entered.is_empty(),'inactive main cannot switch platforms')

 reset()
 router._handle('j:10',true,'joy:0','main')
 for direction_token in ['j:14','j:14','j:13']:
  router._handle(direction_token,true,'joy:0','main')
  router._handle(direction_token,false,'joy:0','main')
 router._handle('j:10',false,'joy:0','main')
 check(router.events == [['platform_next',true],['platform_next',false],['platform_next',true],['platform_next',false],['platform_previous',true],['platform_previous',false]],'hold R1 and tap directions repeatedly without trailing R1 navigation')
 print('CHECKS ',checks,' FAILURES ',failures)
 if failures == 0: print('ALL PASS')
 quit(1 if failures else 0)

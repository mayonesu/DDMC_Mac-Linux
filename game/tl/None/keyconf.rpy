









init 1 python:

















































    if persistent.gamepad:
        if persistent.change_buttons:
            config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            config.pad_bindings["pad_b_press"] = [ "dismiss", "button_select", "bar_activate", "bar_deactivate"]
            config.pad_bindings["pad_x_press"] = [ "hide_windows" ]
            config.pad_bindings["pad_y_press"] = [ "toggle_skip" ]
        else:
            config.pad_bindings["pad_a_press"] = [ "dismiss", "button_select", "bar_activate", "bar_deactivate"]
            config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            config.pad_bindings["pad_x_press"] = [ "toggle_skip" ]
            config.pad_bindings["pad_y_press"] = [ "hide_windows" ]
        config.pad_bindings["pad_leftshoulder_press"] =[ "viewport_up", "viewport_wheelup" ]
        config.pad_bindings["pad_rightshoulder_press"] = [ "viewport_down", "viewport_wheeldown" ]
        config.pad_bindings["pad_lefttrigger_pos"] = [ "skip" ]
        config.pad_bindings["pad_lefttrigger_zero"] = [ "stop_skipping" ]
        config.pad_bindings["pad_righttrigger_pos"] = [ "dismiss" ]
        config.pad_bindings["pad_guide_press"] = [ "screenshot" ]
        config.pad_bindings["pad_start_press"] = [ "quit" ]
        config.pad_bindings["pad_dpleft_press"] = [ "focus_left", "bar_left", "viewport_leftarrow" ]
        config.pad_bindings["pad_leftx_neg"] = [ "focus_left", "bar_left", "viewport_leftarrow" ]
        config.pad_bindings["pad_rightx_neg"] = [ "focus_left", "bar_left", "viewport_leftarrow" ]
        config.pad_bindings["pad_dpright_press"] = [ "focus_right", "bar_right", "viewport_rightarrow" ]
        config.pad_bindings["pad_leftx_pos"] = [ "focus_right", "bar_right", "viewport_rightarrow" ]
        config.pad_bindings["pad_rightx_pos"] = [ "focus_right", "bar_right", "viewport_rightarrow" ]
        config.pad_bindings["pad_dpup_press"] = [ "focus_up", "bar_up", "viewport_uparrow" ]
        config.pad_bindings["pad_pad_lefty_neg"] = [ "focus_up", "bar_up", "viewport_uparrow" ]
        config.pad_bindings["pad_righty_neg"] = [ "viewport_up", "viewport_wheelup" ]
        config.pad_bindings["pad_dpdown_press"] = [ "focus_down", "bar_down", "viewport_downarrow" ]
        config.pad_bindings["pad_lefty_pos"] = [ "focus_down", "bar_down", "viewport_downarrow" ]
        config.pad_bindings["pad_righty_pos"] = [ "viewport_down", "viewport_wheeldown" ]
    else:
        config.pad_bindings["pad_a_press"] = [ ]
        config.pad_bindings["pad_b_press"] = [ ]
        config.pad_bindings["pad_x_press"] = [ ]
        config.pad_bindings["pad_y_press"] = [ ]
        config.pad_bindings["pad_leftshoulder_press"] =[ ]
        config.pad_bindings["pad_rightshoulder_press"] = [ ]
        config.pad_bindings["pad_lefttrigger_pos"] = [ ]
        config.pad_bindings["pad_lefttrigger_zero"] = [ ]
        config.pad_bindings["pad_righttrigger_pos"] = [ ]
        config.pad_bindings["pad_guide_press"] = [ ]
        config.pad_bindings["pad_start_press"] = [ ]
        config.pad_bindings["pad_dpleft_press"] = [ ]
        config.pad_bindings["pad_leftx_neg"] = [ ]
        config.pad_bindings["pad_rightx_neg"] = [ ]
        config.pad_bindings["pad_dpright_press"] = [ ]
        config.pad_bindings["pad_leftx_pos"] = [ ]
        config.pad_bindings["pad_rightx_pos"] = [ ]
        config.pad_bindings["pad_dpup_press"] = [ ]
        config.pad_bindings["pad_lefty_neg"] = [ ]
        config.pad_bindings["pad_righty_neg"] = [ ]
        config.pad_bindings["pad_dpdown_press"] = [ ]
        config.pad_bindings["pad_lefty_pos"] = [ ]
        config.pad_bindings["pad_righty_pos"] = [ ]








init 1 python:



    def _show_history():
        if not renpy.context()._menu:
            renpy.call_in_new_context("_game_menu", _game_menu_screen="history")

    config.underlay.append(renpy.Keymap(history = _show_history))
    config.keymap["history"] = []









    def _toggle_language():
        if _preferences.language=="english":
            renpy.change_language(None)
        else:
            renpy.change_language("english")
        return

    config.underlay.append(renpy.Keymap(toggle_language = _toggle_language))
    config.keymap["toggle_language"] = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

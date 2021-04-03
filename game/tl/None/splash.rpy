translate None python:
    achievement_name_1 = "Bad Sayori"
    achievement_name_2 = "Bad Yuri"
    achievement_name_3 = "Bad Natsuki"
    achievement_name_4 = "Bad Monika"
    achievement_name_5 = "Without Monika"
    achievement_name_6 = "No One"
    achievement_name_7 = "The Truth"
    achievement_name_8 = "Sa...yo...ri...?"
    achievement_name_9 = "Who is laughing?"
    achievement_name_10 = "It's fake!"
    achievement_name_11 = "Natsuki's face data was corrupted"
    achievement_name_12 = "Sayori's eye"
    achievement_name_13 = "Color bar"
    achievement_message_1 = "Complete Sayori's Bad Route"
    achievement_message_2 = "Complete Yuri's Bad Route"
    achievement_message_3 = "Complete Yuri's Bad Route"
    achievement_message_4 = "Complete Monika's Bad Route"
    achievement_message_5 = "Complete Normal End Route"
    achievement_message_6 = "Complete Normal End2 Route"
    achievement_message_7 = "Complete True End Route"
    achievement_message_8 = "You got Sayori's mouse icon"
    achievement_message_9 = "Is this game cursed?"
    achievement_message_10 = "Are you surprised?"
    achievement_message_11 = "What happend...?"
    achievement_message_12 = "She won't come back anymore..."
    achievement_message_13 = "You'll rarely see it on TV until midnight."

translate None image:
    image menu_art_y:
        subpixel True
        "menu_art_y_blink"
        xcenter 600
        ycenter 335
        zoom 0.60
        menu_art_move(0.54, 600, 0.60)

    image menu_art_n:
        subpixel True
        "menu_art_n_blink"
        xcenter 750
        ycenter 385
        zoom 0.58
        menu_art_move(0.58, 750, 0.58)

    image menu_art_s:
        subpixel True
        "menu_art_s_blink"
        xcenter 510
        ycenter 500
        zoom 0.68
        menu_art_move(0.68, 510, 0.68)

    image menu_art_m:
        subpixel True
        "menu_art_m_blink"
        xcenter 1000
        ycenter 640
        zoom 1.00
        menu_art_move(1.00, 1000, 1.00)

    image menu_art_y_eye:
        "mod_assets/y_animation/menu_art_y_eye_1.png"
        choice:
            6.0
        choice:
            3.5
        choice:
            2.5
        "mod_assets/y_animation/menu_art_y_eye_0.png"
        0.1
        repeat
    image menu_art_y_blink = LiveComposite((481,1080),(0,0),"gui/menu_art_y.png",(0,0),"menu_art_y_eye")

    image menu_art_n_eye:
        "mod_assets/n_animation/menu_art_n_eye_1.png"
        choice:
            5.0
        choice:
            3.5
        choice:
            1.5
        "mod_assets/n_animation/menu_art_n_eye_0.png"
        0.1
        repeat
    image menu_art_n_blink = LiveComposite((400,1080),(0,0),"gui/menu_art_n.png",(0,0),"menu_art_n_eye")

    image menu_art_s_eye:
        "mod_assets/s_animation/menu_art_s_eye_1.png"
        choice:
            5.5
        choice:
            3.5
        choice:
            1.0
        "mod_assets/s_animation/menu_art_s_eye_0.png"
        0.1
        repeat
    image menu_art_s_blink = LiveComposite((411,1080),(0,0),"gui/menu_art_s.png",(0,0),"menu_art_s_eye")

    image menu_art_m_eye:
        "mod_assets/m_animation/menu_art_m_eye_1.png"
        choice:
            5.0
        choice:
            4.0
        choice:
            2.0
        "mod_assets/m_animation/menu_art_m_eye_0.png"
        0.1
        repeat
    image menu_art_m_blink = LiveComposite((602,1080),(0,0),"gui/menu_art_m.png",(0,0),"menu_art_m_eye")

translate None python:
    splash_message_fake = "This mod is not suitable for children \nor those who are easily disturbed.\nMoreover,it's better to go home and go to bed for who easily gets mad\nat the modification itself or looks for the happy sweet Literature Club."
    splash_message_fake2 = "This mod is null."
    splash_message_fake3 = "Are you trying to cheat?"
    splash_message_default = "This game is not suitable for children\nor those who are easily disturbed."

translate None image:
    image menu_logo:
        "tl/None/gui/logo.png"
        subpixel True
        xcenter 240
        ycenter 120
        zoom 0.60
        menu_logo_move
translate None label:
    label splashscreen:
        if not renpy.loadable("debug") and config.console:
            call you_are_cheater
            return
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ ]
        python:
            process_list = []
            currentuser = ""
            if renpy.windows:
                try:
                    process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
                except:
                    pass
                try:
                    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                        user = os.environ.get(name)
                        if user:
                            currentuser = user
                except:
                    pass


        python:
            firstrun = ""

            try:
                firstrun = renpy.file("firstrun").read(1)
            except:
                with open(config.basedir + "/game/firstrun", "wb") as f:
                    pass

        if not firstrun:
            if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
                if renpy.loadable("../lang"):
                    $ lang = open(config.basedir + "/lang", "r").read()
                    if lang == "ja":
                        $ renpy.change_language("Japanese")
                    else:
                        $ renpy.change_language(None)
                $ quick_menu = False
                scene black
                menu:
                    "A previous save file has been found. Would you like to delete your save data and start over?"
                    "Yes, delete my existing data.":
                        "Deleting save data...{nw}"
                        python hide:
                            for i in range(0,16):
                                if i == 0:
                                    f = open(renpy.config.gamedir + "/chapter", "w")
                                else:
                                    f = open(renpy.config.gamedir + "/chapter", "a")
                                if persistent.chapter_seen[i]:
                                    f.write("1")
                                else:
                                    f.write("0")
                                f.close()
                        python:
                            delete_all_saves()
                            renpy.loadsave.location.unlink_persistent()
                            renpy.persistent.should_save_persistent = False
                            renpy.utter_restart()
                    "No, continue where I left off.":
                        $ restore_relevant_characters()

            python:
                if not firstrun:
                    try:
                        with open(config.basedir + "/game/firstrun", "w") as f:
                            f.write("1")
                    except:
                        renpy.jump("readonly")

        if renpy.loadable("jp.rpa") and renpy.loadable("none.rpa"):
            $ quick_menu = False
            "DDLC UNOFFICIAL JP PATCH WAS FOUND."
            "You can't play this MOD with DDLC UNOFFICIAL JP PATCH."
            menu:
                "Are you sure to delete DDLC UNOFFICIAL JP PATCH?\nIf you select \"No\",this game will be closed."
                "Yes":
                    "Deleting DDLC UNOFFICIAL JP PATCH...{nw}"
                    $ Uninstall()
                "No":
                    $ renpy.quit()

        if firstrun and (persistent.oncedeleted_ddmcmod == True or persistent.oncedeleted_jppatch == True):
            $ lang = open(config.basedir + "/lang", "r").read()
            if lang == "ja":
                $ renpy.change_language("Japanese")
            else:
                $ renpy.change_language(None)

            $ persistent.oncedeleted_ddmcmod = False
            $ persistent.oncedeleted_jppatch = False
            $ renpy.save_persistent()
            $ renpy.reload_script

        if config.version != persistent.oldversion:
            $ restore_relevant_characters()
            $ persistent.oldversion = config.version
            $ renpy.save_persistent()

        if not persistent.first_run:
            if renpy.loadable("chapter"):
                python:
                    rf = open(renpy.config.gamedir + '/chapter', "rt")
                    count = 0
                    for ch in rf.read():
                        if ch == "1":
                            persistent.chapter_seen[count] = True
                        else:
                            persistent.chapter_seen[count] = False
                        count += 1
                    rf.close()
                    import os
                    try: os.unlink(renpy.config.gamedir + '/chapter')
                    except: pass
            python:
                restore_all_characters()
            $ quick_menu = False
            python:
                try:
                    with open(config.basedir + "/lang", "w") as f:
                        f.write("ja")
                except:
                    pass
            scene white
            pause 0.5
            scene tos
            with Dissolve(1.0)
            pause 1.0
            menu:
                "Which language would you like to play?"
                "English ":
                    $ renpy.change_language(None)
                    python:
                        try:
                            with open(config.basedir + "/lang", "w") as f:
                                f.write("en")
                        except:
                            pass
                "Japanese ":
                    $ renpy.change_language("Japanese")
            pause 1.0
            "This game is not suitable for children or those who are easily disturbed."
            "This game is an unofficial fan work, unaffiliated with Team Salvato."
            "Individuals suffering from anxiety or depression may not have a safe experience playing this game. For content warnings, please visit: {a=http://ddlc.moe/warning.html}http://ddlc.moe/warning.html{/a}"
            menu:
                "By playing Doki Doki Murder Case, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
                "I agree.":
                    pass
            pause 1.0
            "We added 'Chapter mode' from 'ddmc_v1.1.0'."
            "Before using, you must set player's name."
            "Set Chapter mode at 'Settings' in {b}'Main menu'{/b}."
            "You can't set Chapter mode in the story."
            "If you play this mod for the first time, you should play through the story.\nIf possible, you should see at least 1 end(NOT BAD END)."
            "You can't select the chapter that you've never seen in chapter selection from \"v1.2.16\""
            "If you see at once, you will be able to choose it."
            pause 1.0
            if not renpy.loadable("name"):
                "We added 'Save name' from 'ddmc_v1.2.9'."
                "You can save your name as file 'name'."
                "You don't have to enter your name after resetting this game."
                menu:
                    "Do you want to save your name as file?"
                    "Yes":
                        $ persistent.save_name = True
                        "You can change this setting after this."
                    "No":
                        $ persistent.save_name = False
                        "If you change this setting, you must set your name at 'Cahnge player name' from settings."
                pause 1.0
            if renpy.variant("pc"):
                menu:
                    "Are you broadcasting or recording video now?"
                    "Yes":
                        "This mod reads username from your PC."
                        "If you want not to display username, you can hide it."
                        menu:
                            "Do you want to hide username?"
                            "Yes":
                                $ persistent.hideusername = True
                            "No":
                                $ persistent.hideusername = False
                    "No":
                        "This mod reads username from your PC."
                        "If you want not to display username, you can hide it from settings."
            pause 1.0
            menu:
                "Do you want to hide some horror effects?"
                "Yes":
                    $ persistent.horror_effects = False
                "No":
                    $ persistent.horror_effects = True
            "You can change this from settings later."
            pause 1.0
            menu:
                "Choose the settings for some animation effects."
                "Normal":
                    $ persistent.save_graphic = False
                "Light":
                    $ persistent.save_graphic = True
            "You can change this from settings later."
            if ddmm_online:
                pause 1.0
                "Added DDMM achievement settings from 'v1.2.14'."
                menu:
                    "Do you want to use DDMM achievement?"
                    "Yes":
                        $ persistent.ddmm_achievement = True
                        python:
                            ddmm_register_achievement("BAD_SAYORI", achievement_name_1, achievement_message_1)
                            ddmm_register_achievement("BAD_YURI", achievement_name_2, achievement_message_2)
                            ddmm_register_achievement("BAD_NATSUKI", achievement_name_3, achievement_message_3)
                            ddmm_register_achievement("BAD_MONIKA", achievement_name_4, achievement_message_4)
                            ddmm_register_achievement("WITHOUT_MONIKA", achievement_name_5, achievement_message_5)
                            ddmm_register_achievement("NO_ONE", achievement_name_6, achievement_message_6)
                            ddmm_register_achievement("THE_TRUTH", achievement_name_7, achievement_message_7)
                    "No":
                        $ persistent.ddmm_achievement = False
                "You can change this from settings later."
            pause 1.0
            menu:
                "Do you want to use Gamepad?\n(You can use only XInput controler)"
                "Yes":
                    $ persistent.gamepad = True
                    menu:
                        "Are you using Xbox controller?\n(or controller like Xbox layout)"
                        "Yes":
                            $ persistent.change_buttons = False
                        "No":
                            $ persistent.change_buttons = True
                            $ config.pad_bindings["pad_a_press"] = [ ]
                            $ config.pad_bindings["pad_b_press"] = [ "dismiss", "button_select", "bar_activate", "bar_deactivate"]
                            $ config.pad_bindings["pad_x_press"] = [ "hide_windows" ]
                            $ config.pad_bindings["pad_y_press"] = [ "toggle_skip" ]
                    "Button layout was set."
                    "If you know how to use, check this site {a=https://ddmc.ddlc-jp.tokyo/main_page/xbox_en.html}\"https://ddmc.ddlc-jp.tokyo/main_page/xbox_en.html\"{/a}."
                "No":
                    python:
                        persistent.gamepad = False
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
            "You can change this from settings later."
            $ persistent.first_run = True
            scene tos2
            with Dissolve(1.5)
            pause 1.0
            scene white


        python:
            s_kill_early = None



            if not s_kill_early:
                if persistent.playthrough <= 2 and persistent.playthrough != 0:
                    try: renpy.file("../characters/monika.chr")
                    except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
                if persistent.playthrough <= 1 or persistent.playthrough == 4:
                    try: renpy.file("../characters/natsuki.chr")
                    except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                    try: renpy.file("../characters/yuri.chr")
                    except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
                if persistent.playthrough == 4:
                    try: renpy.file("../characters/sayori.chr")
                    except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

        if not persistent.special_poems:
            python hide:
                persistent.special_poems = [0,0,0]
                a = range(1,12)
                for i in range(3):
                    b = renpy.random.choice(a)
                    persistent.special_poems[i] = b
                    a.remove(b)

        $ basedir = config.basedir.replace('\\', '/')



        if persistent.autoload:
            jump autoload



        $ config.allow_skipping = False

        if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
            show black
            $ config.main_menu_music = audio.ghostmenu
            $ persistent.seen_ghost_menu = True
            $ persistent.ghost_menu = True
            $ renpy.music.play(config.main_menu_music)
            $ pause(1.0)
            show end with dissolve_cg
            $ pause(3.0)
            $ config.allow_skipping = True
            return


        if s_kill_early:
            show black
            play music "bgm/s_kill_early.ogg"
            $ pause(1.0)
            show end with dissolve_cg
            $ pause(3.0)
            scene white
            show expression "images/cg/s_kill_early.png":
                yalign -0.05
                xalign 0.25
                dizzy(1.0, 4.0, subpixel=False)
            show white as w2:
                choice:
                    ease 0.25 alpha 0.1
                choice:
                    ease 0.25 alpha 0.125
                choice:
                    ease 0.25 alpha 0.15
                choice:
                    ease 0.25 alpha 0.175
                choice:
                    ease 0.25 alpha 0.2
                choice:
                    ease 0.25 alpha 0.225
                choice:
                    ease 0.25 alpha 0.25
                choice:
                    ease 0.25 alpha 0.275
                choice:
                    ease 0.25 alpha 0.3
                pass
                choice:
                    pass
                choice:
                    0.25
                choice:
                    0.5
                choice:
                    0.75
                repeat
            show noise:
                alpha 0.1
            with Dissolve(1.0)
            show expression Text("Now everyone can be happy.", style="sayori_text"):
                xalign 0.8
                yalign 0.5
                alpha 0.0
                600
                linear 60 alpha 0.5
            pause
            $ renpy.quit()

        if not renpy.loadable("../lang"):
            $ quick_menu = False
            $ renpy.change_language("Japanese")
            menu:
                "\"lang\" file was not found.\nChoose your language."
                "English ":
                    $ renpy.change_language(None)
                    python:
                        try:
                            with open(config.basedir + "/lang", "w") as f:
                                f.write("en")
                        except:
                            pass
                "Japanese ":
                    $ renpy.change_language("Japanese")
                    python:
                        try:
                            with open(config.basedir + "/lang", "w") as f:
                                f.write("jp")
                        except:
                            pass
            "Please be careful not to delete \"lang\" file.{w=3.0}{nw}"
            $ quick_menu = True
        if not renpy.loadable("debug") and renpy.random.randint(0,59) == 0:
            call first_horror
            return
        show white
        $ persistent.ghost_menu = False
        $ splash_message = splash_message_default
        $ config.main_menu_music = audio.t1
        $ renpy.music.play(config.main_menu_music)
        $ starttime = datetime.datetime.now()
        show intro with Dissolve(0.5, alpha=True)
        $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
            $ splash_message = renpy.random.choice(splash_messages)
        show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
        $ config.allow_skipping = True
        if persistent.gamepad:
            if persistent.change_buttons:
                $ config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
            else:
                $ config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
        if renpy.random.randint(0,9) == 0:
            $ chibi_title = True
        else:
            $ chibi_title = False
        return

translate None label:
    label fakesplash:
        $ config.pad_bindings["pad_b_press"] = [ ]
        if not renpy.loadable("../lang"):
            $ quick_menu = False
            menu:
                "\"lang\" file was not found.\nChoose your language."
                "English ":
                    $ renpy.change_language(None)
                    python:
                        try:
                            with open(config.basedir + "/lang", "w") as f:
                                f.write("en")
                        except:
                            pass
                "Japanese ":
                    $ renpy.change_language("Japanese")
                    python:
                        try:
                            with open(config.basedir + "/lang", "w") as f:
                                f.write("jp")
                        except:
                            pass
            "Please be careful not to delete \"lang\" file.{w=3.0}{nw}"
        show white
        $ persistent.ghost_menu = False
        if persistent.normal_end == 1:
            $ splash_message = splash_message_fake
        elif persistent.normal_end == 2:
            $ splash_message = splash_message_fake2
        else:
            $ splash_message = splash_message_fake3
        $ config.main_menu_music = audio.t1
        $ renpy.music.play(config.main_menu_music)
        $ starttime = datetime.datetime.now()
        show intro with Dissolve(0.5, alpha=True)
        $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
            $ splash_message = renpy.random.choice(splash_messages)
        show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
        $ config.allow_skipping = True
        $ main_menu = True

        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

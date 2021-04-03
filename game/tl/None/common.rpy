init python early:
    import os
    try: os.unlink(config.basedir + "/game/saves/persistent")
    except: pass

init -1 python:
    import datetime
    if not (datetime.date.today().year == 2019 and datetime.date.today().month == 9 and datetime.date.today().day == 22):
        persistent.monikabirth = False

init -1 python:
    dialog_message = "UNOFFICIAL JP PATCH WAS DELETED!"
    def Uninstall():
        if _preferences.language == None:
            try:
                with open(config.basedir + "/lang", "w") as f:
                    f.write("en")
            except:
                pass
        else:
            try:
                with open(config.basedir + "/lang", "w") as f:
                    f.write("ja")
            except:
                pass
        renpy.change_language(None)
        persistent.jppatch_uninstall = True
        renpy.save_persistent()
        renpy.utter_restart()
        return

    if persistent.jppatch_uninstall == True:
        import os
        try: os.unlink(config.basedir + "/game/jp.rpa")
        except: pass
        try: os.unlink(config.basedir + "/game/none.rpa")
        except: pass
        persistent.jppatch_uninstall = False
        persistent.oncedeleted_jppatch = True
        renpy.save_persistent()
        try: os.unlink(config.basedir + "/game/saves/persistent")
        except: pass
        renpy.quit()
        pause(2.0)

init -100 python:

    @renpy.pure
    class SetPersistent(Action, FieldEquality):
        identity_fields = ['value']
        equality_fields = ['name']
        
        def __init__(self, name, value):
            self.name = name
            self.value = value
        
        def __call__(self):
            setattr(persistent, self.name, self.value)
            renpy.save_persistent()
            renpy.restart_interaction()
        
        
        def get_selected(self):
            return getattr(persistent, self.name) == self.value
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

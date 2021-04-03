translate Japanese python:
    style.ruby_text.size = 12 
    style.ruby_text.yoffset = -26 

translate Japanese style yuri_text:
    font "gui/font/851tegaki_zatsu_normal.ttf"
    size 28

translate Japanese style yuri_text_2:
    font "gui/font/gatasosyo.ttf"
    size 36

translate Japanese style yuri_text_3:
    font "gui/font/gatasosyo.ttf"
    size 27
    kerning -12
    language "western"

translate Japanese style natsuki_text:
    font "gui/font/SNsanafonP.ttf"
    size 30

translate Japanese style sayori_text:
    font "gui/font/HolidayMDJP.otf"
    size 30

translate Japanese style monika_text:
    font "gui/font/Ruriiro_font.ttf"
    size 30

translate Japanese python:
    mc = DynamicCharacter('player + "{w}"', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_mc')
    s = DynamicCharacter('s_name', image='sayori', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_s', callback=speaker("sayori"))
    m = DynamicCharacter('m_name', image='monika', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_m', callback=speaker("monika"))
    n = DynamicCharacter('n_name', image='natsuki', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_n', callback=speaker("natsuki"))
    y = DynamicCharacter('y_name', image='yuri', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_y', callback=speaker("yuri"))
    q = DynamicCharacter('"？？？"', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_q')
    mcs = DynamicCharacter('mcs_name', image='', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed", window_style='window_mc', callback=speaker("sayori"))
    w = DynamicCharacter('w_name', image='wallace', what_prefix='', what_suffix='', ctc="ctc", ctc_position="fixed")

translate Japanese strings:
    old "Sayori"
    new "サヨリ"

    old "Monika"
    new "モニカ"

    old "Natsuki"
    new "ナツキ"

    old "Yuri"
    new "ユリ"

    old "???"
    new "？？？"

    old "Girl 1"
    new "女子Ａ"

    old "Girl 2"
    new "女子Ｂ"

    old "Girl 3"
    new "女子Ｃ"

    old "[player]&Sayori"
    new "[player]&サヨリ"

    old "Which scene would you like to start?"
    new "どのシーンから始めますか？"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

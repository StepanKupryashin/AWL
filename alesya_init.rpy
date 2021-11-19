init:
    #Начинаем инит блок:
    #Инициализируем мод в списке модов
    $ mods['alesya_mtart'] = u'{font=mods/alesyawhitelist/fonts/glasten.ttf}{color=#2ab6c3}Алеся. Чистый лист{/color}{/font}'

    # Переменные
    $ gamedir = "mods/alesyawhitelist"
    $ imgdir = gamedir + "/img"
    $ spritesdir = imgdir + "/sprites"
    $ gallerydir = imgdir + "/gallery"
    $ musicdir = gamedir + "/music"
    $ soundsdir = gamedir + "/sounds"
    $ fontsdir = gamedir + "/fonts"
    $ videosdir = gamedir + "/vid"

    #Переменные выборов
    $ enter_door = 0

    #Изображения и прочие графические ресурсы
    image bg alesya beach = imgdir + "/alesya_beach.png"
    image bg alesya vlad_road = imgdir + "/lseyamod_d3_untraveled_road.png"
    image bg alesya kiss_epiloge = imgdir + "/lseyamod_epilogue_lseya_kiss.png"
    image bg alesya icecream = imgdir + "/lseyamod_epilogue_icecream.png"
    image bg vlad_roma_kvart = imgdir + "/kvartira.png"
    image bg vlad_alesya karusel = imgdir + "/karusel.png"
    image bg green_park = imgdir + "/greenpark.png"
    image bg ice = imgdir + "/ice_bg.png"
    image cg ice 1 = imgdir + "/ice_cg_1.png"
    image cg ice 2 = imgdir + "/ice_cg_2.png"
    image cg ice 3 = imgdir + "/ice_cg_3.png"
    image cg ice 4 = imgdir + "/ice_cg_4.png"
    image bg hospital_ulica = imgdir + "/ext_hospitall.jpg"
    image bg train = imgdir + "/int_coupe_night_7dl.png"
    image bg lena_room = imgdir + "/int_mt_sam_room_7dl.jpg"
    image bg kitchen_room = imgdir + "/ss_kitchen.jpg"
    image bg room_lena_close = imgdir + "/int_mt_sam_room_close_7dl.jpg"
    image bg hospital_hall = imgdir + "/int_hospital_hall_day_7dl.png"
    image bg train_without = imgdir + "/epilog_without_train.jpg"
    image bg train_its = imgdir + "/epilog_train.jpg"
    image bg hospital_coridor = imgdir + "/int_hospital_corridor_7dl.jpg"
    image bg hospital_palata = imgdir + "/int_refinery_day_7dl.png"
    image bg vlad_kvart = imgdir + "/int_sam_room_7dl.png"
    image bg houses_s = imgdir + "/houses.png"
    image bg park = imgdir + "/park.jpg"
    image bg bad_soon = imgdir + "/d7_un_epilogue_bad_7dl.jpg"
    image bg bad_door = imgdir + "/int_opened_door_7dl.jpg"
    image bg wedding_int = imgdir + "/int_church_7dl.png"
    image bg kl_kabinet_int = imgdir + "/int_chief_office_day_7dl.png"
    image bg karusel_kiss = imgdir + "/karusel_kiss.png"
    image bg karusel_waiter = imgdir + "/karusel_wait.png"
    image bg karusel_sad = im.Scale(imgdir + '/karusel_sad.png', 1920,1080)
    image bg karusel_final = im.Scale(imgdir + '/karusel_final.png', 1920,1080)  
    #Временные фото-арты
    image bg platc = imgdir + "/platc.png"
    image bg mil_base = imgdir + "/military_base.png"
    #Спрайты
    #Спрайты Ромы
    image roma_normal = spritesdir + "/far/rm/roma_normal.png"
    image roma_smile = spritesdir + "/far/rm/roma_smile.png"
    image roma_whats = spritesdir + "/far/rm/roma_what.png"
    image roma_verysmile = spritesdir + "/far/rm/roma_verysmile.png"
    #Спрайты Доктора
    image doc_normal = spritesdir + "/doc/doc.png"
    image doc_left = LiveComposite((800,1800),(0,0), spritesdir + "/doc/doc.png",(0,0), spritesdir + "/doc/left.png")
    image doc_smile = LiveComposite((800,1800),(0,0), spritesdir + "/doc/doc.png",(0,0), spritesdir + "/doc/smile.png")
    image doc_upset = LiveComposite((800,1800),(0,0), spritesdir + "/doc/doc.png",(0,0), spritesdir + "/doc/upset.png")
    #Спрайты мед.сестры
    image medicalsister = spritesdir + "/med/ms.png"
    #Спрайты кардиолога
    image kardio_doc = spritesdir + "/kard/kardiodoc.png" 
    #Спрайты Алеси
    #(Обычная пионерская одежда (( НЕ ИСПОЛЬЗУЕТСЯ БОЛЬШЕ)) )
    image alesya angry_sr = spritesdir + "/normal/al/pio/lseya_angry_pio_norm.png"
    image alesya cry_sr = spritesdir + "/normal/al/pio/lseya_cry_pio_norm.png"
    image alesya fear_sr = spritesdir + "/normal/al/pio/lseya_fear_pio_norm.png"
    image alesya laugh_sr = spritesdir + "/normal/al/pio/lseya_laugh_pio_norm.png"
    image alesya normal_sr = spritesdir + "/normal/al/pio/lseya_normal_pio_norm.png"
    image alesya rage_sr = spritesdir + "/normal/al/pio/lseya_rage_pio_norm.png"
    image alesya sad_sr = spritesdir + "/normal/al/pio/lseya_sad_pio_norm.png"
    image alesya shy_sr = spritesdir + "/normal/al/pio/lseya_shy_pio_norm.png"
    image alesya tender_sr = spritesdir + "/normal/al/pio/lseya_tender_pio_norm.png"
    image alesya upset_sr = spritesdir + "/normal/al/pio/lseya_angry_upset_norm.png"
    #(Спортивная одежда)
    image alesya angry_sp = spritesdir + "/normal/al/sport/lseya_angry_sport_norm.png" 
    image alesya cry_sp = spritesdir + "/normal/al/sport/lseya_cry_sport_norm.png"
    image alesya fear_sp = spritesdir + "/normal/al/sport/lseya_fear_sport_norm.png"
    image alesya laugh_sp = spritesdir + "/normal/al/sport/lseya_laugh_sport_norm.png"
    image alesya normal_sp = spritesdir + "/normal/al/sport/lseya_normal_sport_norm.png"
    image alesya rage_sp = spritesdir + "/normal/al/sport/lseya_rage_sport_norm.png"
    image alesya sad_sp = spritesdir + "/normal/al/sport/lseya_sad_sport_norm.png"
    image alesya shy_sp = spritesdir + "/normal/al/sport/lseya_shy_sport_norm.png"
    image alesya tender_sp = spritesdir + "/normal/al/sport/lseya_tender_sport_norm.png"
    image alesya upset_sp = spritesdir + "/normal/al/sport/lseya_upset_sport_norm.png"
    #(Новая повседневная одежда)
    image alesya angry_pv = spritesdir + "/normal/al/pov/lseya_angry_pov_norm.png"
    image alesya cry_pv = spritesdir + "/normal/al/pov/lseya_cry_pov_norm.png"
    image alesya fear_pv = spritesdir + "/normal/al/pov/lseya_fear_pov_norm.png"
    image alesya laugh_pv = spritesdir + "/normal/al/pov/lseya_laugh_pov_norm.png"
    image alesya normal_pv = spritesdir + "/normal/al/pov/lseya_normal_pov_norm.png"
    image alesya rage_pv = spritesdir + "/normal/al/pov/lseya_rage_pov_norm.png"
    image alesya sad_pv = spritesdir + "/normal/al/pov/lseya_sad_pov_norm.png"
    image alesya shy_pv = spritesdir + "/normal/al/pov/lseya_shy_pov_norm.png"
    image alesya tender_pv = spritesdir + "/normal/al/pov/lseya_tender_pov_norm.png"
    image alesya upset_pv = spritesdir + "/normal/al/pov/lseya_upset_pov_norm.png"

    #Музыка и прочие аудио ресурсы
    $ fox_music = musicdir + "/fox.ogg"
    $ solstice_music = musicdir + "/solstice.ogg"
    $ my_someone_like_music = musicdir + "/my_someone_like.ogg"
    $ reflection_on_water_music = musicdir + "/reflection_on_water.ogg"
    $ jooos = musicdir + '/jooos.ogg'

    $ vlad_frol_lgh_sound = soundsdir + "/vlad_frol_lgh.ogg"
    $ alesya_smile_sound = soundsdir + "/alesya_smile.ogg"
    $ door_crash = soundsdir + "/doorcrash.ogg"
    $ phone_zvon = soundsdir + "/tel_zvon.ogg"
    $ phone_close = soundsdir + "/tel_br.ogg"
    $ flash_back = soundsdir + "/teleport.mp3"
    #Создаём новых персонажей
    $ vlad = Character(u'Влад', color="#008000", what_color="#E2C778",)
    $ alesya = Character(u'Алеся', color="#4169E1", what_color="#E2C778",)
    $ serega = Character(u'Серёга', color="#DAA520", what_color="#E2C778",)
    $ roma = Character(u'Рома', color="#66CDAA", what_color="#E2C778",)
    $ dpl_one = Character(u'Голос в трубке', color="#00aab0", what_color="#E2C778",)
    $ dpl_two = Character(u'Наталья Ивановна', color="#00aab0", what_color="#E2C778",)
    $ doctor_one = Character(u'Хирург', color="#00aab0", what_color="#E2C778",)
    $ med_sister = Character(u'Медсестра', color="#0092B3", what_color="#E2C778",)
    $ doctor_two = Character(u'Кардиолог', color="#008a09", what_color="#E2C778",)

transform menu_animator(xal):
    xalign 1.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0
    on idle:
        zoom 1.0
    on selected_idle:
        easein 0.5 zoom 1.05
        easein 0.5 zoom 0.95
        repeat
    on hover:
        easein 0.5 zoom 1.05
        easein 0.5 zoom 0.95
        repeat
    on selected_hover:
        easein 0.5 zoom 1.05
        easein 0.5 zoom 0.95
        repeat
    on hide:
        xalign xal
        alpha 1.0
        easein 1 xalign 1.1 alpha 0.0


transform leftshowing:
    anchor (0.5, 0.5)
    xpos 0.33
    yalign 1.0

label alesya_mtart: #Катапульта запуска меню
    $ save_name = ('Алеся. Чистый Лист - Меню')
    stop sound
    stop music
    stop ambience
    stop sound_loop
    window hide
    $ day_time()
    play sound_loop fox_music fadein 3
    $ volume (1.0, 'music')
    call screen alesya_whitelits_menu()

label alesya_gamestarter: # Катапульта запуска концовки
    stop sound_loop fadeout 3
    $ renpy.pause(0.8, hard=True)
    jump alesya_opening
   
screen alesya_whitelits_menu: #Главное меню
    tag menu
    modal True
    add imgdir + ("/menu/title_screen_bg.jpg") at menu_animator(0.97)
    imagebutton at menu_animator(0.97):
        auto imgdir + "/menu/lseya_start_%s.png" # Начать игру
        xpos 1380
        ypos 378
        action Jump("alesya_gamestarter")
        
    imagebutton at menu_animator(0.97):
        auto imgdir + "/menu/lseya_settings_%s.png" # Настройки
        xpos 1380
        ypos 482
        action [ShowMenu('preferences')]
        
    imagebutton at menu_animator(0.97):
        auto imgdir + "/menu/lseya_gallery_%s.png" # Галерея
        xpos 1380
        ypos 576
        action [ShowMenu('galleryal')]
        
    imagebutton at menu_animator(0.97):
        auto imgdir + "/menu/quit_button_%s.png" # Выход из игры
        xpos 1380
        ypos 679
        #action return
        action [ShowMenu('quit')]
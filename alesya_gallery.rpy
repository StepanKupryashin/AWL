init python:
    g = Gallery()
    g.transition = dissolve
    mr = MusicRoom(channel=u'music',fadeout=1.0,fadein=1.0)

    #mr.add("mods/alesyawhitelist/music/fox.ogg", always_unlocked=True)
    mr.add("mods/alesyawhitelist/music/solstice.ogg", always_unlocked=True)
    #mr.add(musicdir + "/solstice.ogg", always_unlocked=True)
    #mr.add(musicdir + "/solstice.ogg", always_unlocked=True)

screen galleryal:
    python:
        g.button("im1")
        if persistent.im1=="yes":
            g.image(imgdir + "/alesya_beach.png")
        g.button("im2")
        if persistent.im2=="yes":
            g.image(imgdir + "/lseyamod_d3_untraveled_road.png.png")
        g.button("im3")
        if persistent.im3=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im4")
        if persistent.im4=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im5")
        if persistent.im5=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im5")
        if persistent.im5=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im6")
        if persistent.im6=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im7")
        if persistent.im7=="yes":
            g.image(imgdir + "/karusel.png")
        g.button("im8")
        if persistent.im8=="yes":
            g.image(imgdir + "/karusel.png")

    tag menu
    add gallerydir + "/scena.jpg"

    imagebutton: # Кнопка возврата в главное меню
        auto gallerydir + "/gallery_menu_%s.png"
        xalign 0.50
        yalign 1.0
        action [ShowMenu('alesya_whitelits_menu')]
    imagebutton: # Кнопка музыкальной комнаты
        auto gallerydir + "/music_menu_%s.png"
        xalign 0.25
        yalign 1.0
        action [ShowMenu('music_roomal')]
    imagebutton: # Кнопка галлереи спрайтов 
        auto gallerydir + "/sprites_menu_%s.png"
        xalign 0.75
        yalign 1.0
        action [ShowMenu('music_roomal')]

    imagebutton: # Кнопка >>
        auto gallerydir + "/next_menu_%s.png"
        xalign 1.05
        yalign 0.5
        action [ShowMenu('music_roomal')]

    add g.make_button("im1", imgdir + "/alesya_beach.png", locked = gallerydir + "/locked.png", xalign=0.05, yalign=0.25)
    add g.make_button("im2", imgdir + "/lseyamod_d3_untraveled_road.png.png", locked = gallerydir + "/locked.png", xalign=0.35, yalign=0.25)
    add g.make_button("im3", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.65, yalign=0.25)
    add g.make_button("im4", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.95, yalign=0.25)
    add g.make_button("im5", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.05, yalign=0.70)
    add g.make_button("im6", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.35, yalign=0.70)
    add g.make_button("im7", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.65, yalign=0.70)
    add g.make_button("im8", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.95, yalign=0.70)

    #add g.make_button("im9", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.7, yalign=0.50)
    #add g.make_button("im10", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.9, yalign=0.50)
    #add g.make_button("im11", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.1, yalign=0.75)
    #add g.make_button("im12", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.3, yalign=0.75)
    #add g.make_button("im13", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.5, yalign=0.75)
    #add g.make_button("im14", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.7, yalign=0.75)
    #add g.make_button("im15", imgdir + "/karusel.png", locked = gallerydir + "/locked.png", xalign=0.9, yalign=0.75)

screen music_roomal:

    tag menu

    frame:
        has vbox
        #textbutton "Track 1" action mr.Play(musicdir + "/fox.ogg")
        textbutton "Track 2" action mr.Play("mods/alesyawhitelist/music/solstice.ogg")
        #textbutton "Track 3" action mr.Play(musicdir + "/solstice.ogg")
        null height 20
        textbutton "Next" action mr.Next()
        textbutton "Previous" action mr.Previous()
        null height 20
        textbutton "Main Menu" action [ShowMenu('alesya_whitelits_menu')]
        #on "replace" action mr.Play()
        #on "replaced" action Play("music", musicdir + "/fox.ogg")


"""Contains the code for the user interface of AMG"""

import pygame
from amg import Loop, choose_chord, get_voicing, get_chord_name, notes_sharp, \
    notes_flat, key_sharp_or_flat, set_voicings, chord_sharp_or_flat


class Sound:
    """Represents a sound which has a name and sound file

    @type name: str
    @type sound: pygame.sound
    """

    def __init__(self, name, sound):
        """Constructs a sound which has a name and sound

        @type self: Sound
        @type name: str
        @type sound: pygame.sound
        """

        self.name = name
        self.sound = sound


class Key:
    """Represents a key of the piano

    @type name: str
        A or Bb, e.g.
    @type in_scale: bool
        True if the note is in the scale of the current chord; False if not
    @type color: str
        either 'black' or 'white' (for now it's 'tan' instead of 'white')
    """

    def __init__(self, name, color):
        """Constructs a key object

        @type self: Key
        @type name: str
        @type color: str
        @rtype: None
        """

        self.name = name
        self.color = color
        self.in_scale = False
        self.pressed = False

    def draw_key(self, color):
        """Draws the key self

        @type self: Key
        @type color: str
        @rtype: None"""
        if self == A0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (369, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (387, 402, 25, 128))
        elif self == Bb0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (414, 402, 36, 126))
        elif self == B0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (434, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (452, 402, 45, 128))
        elif self == C0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (44, 402, 43, 128))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (44, 530, 63, 68))

        elif self == C1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (499, 402, 43, 128))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (499, 530, 63, 68))

        elif self == Db0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (89, 402, 36, 126))

        elif self == Db1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (544, 402, 36, 126))

        elif self == D0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (109, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (127, 402, 25, 128))

        elif self == D1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (582, 402, 25, 128))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (564, 530, 63, 68))

        elif self == Eb0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (154, 402, 36, 126))

        elif self == Eb1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (609, 402, 36, 126))

        elif self == E0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (174, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (192, 402, 45, 128))

        elif self == E1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (647, 402, 45, 128))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (629, 530, 63, 68))

        elif self == F0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (239, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (239, 402, 43, 128))

        elif self == F1k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (694, 402, 61, 196))

        elif self == F_0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (284, 402, 36, 126))

        elif self == G0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (304, 530, 63, 68))
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (322, 402, 25, 128))

        elif self == Ab0k:
            pygame.draw.rect(screen, pygame.color.THECOLORS[color],
                             (349, 402, 36, 126))


FONT_FAMILY = 'Arial'
FONT_HEIGHT = 30
WIDTH = 1024
HEIGHT = 768


def render_display(screen):
    """Render stuff to the given screen.

    @type screen: pygame.Surface
    @rtype: None
    """
    # Set the font
    font = pygame.font.SysFont(FONT_FAMILY, 35)

    text_surface = font.render('Welcome to AMADEUS',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (275, 30)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('mellow',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (50, 100)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('dry',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (200, 100)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('shallow',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (50, 250)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('deep',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (200, 250)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('loop length',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (350, 100)
    screen.blit(text_surface, text_pos)

    # dry/mellow ratings
    for x in range(50, 250, 40):
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                         (x, 150, 25, 25))

    for x in range(52, 252, 40):
        if x != 132:
            pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                             (x, 152, 21, 21))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                     (132, 152, 21, 21))

    # depth ratings
    for x in range(50, 250, 40):
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                         (x, 300, 25, 25))

    for x in range(52, 252, 40):
        if x != 132:
            pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                             (x, 302, 21, 21))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                     (132, 302, 21, 21))

    # loop length
    for x in range(340, 500, 40):
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                         (x, 150, 25, 25))

    for x in range(342, 502, 40):
        if x != 382:
            pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                             (x, 152, 21, 21))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                     (382, 152, 21, 21))

    draw_loop_numbers(screen)

    # 'create' button
    pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                     (350, 230, 120, 40))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                     (352, 232, 116, 36))

    text_surface = font.render('CREATE',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (358, 240)
    screen.blit(text_surface, text_pos)

    # 'stop' button
    pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                     (350, 285, 120, 40))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                     (352, 287, 116, 36))

    text_surface = font.render('STOP',
                               1, pygame.color.THECOLORS['black'])
    text_pos = (375, 295)
    screen.blit(text_surface, text_pos)

    # piano
    draw_piano()

    white_keys = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"]

    for key in white_keys:
        text_surface = font.render(key,
                                   1, pygame.color.THECOLORS['black'])
        text_pos = (74+65*white_keys.index(key), 605)
        screen.blit(text_surface, text_pos)

    black_keys = ['W', 'E', '', 'T', 'Y', 'U', '', 'O', 'P']

    for key in black_keys:
        text_surface = font.render(key,
                                   1, pygame.color.THECOLORS['black'])
        text_pos = (100+65*black_keys.index(key), 375)
        screen.blit(text_surface, text_pos)

    # This must be called *after* all other pygame functions have run.
    pygame.display.flip()


def event_loop(screen):
    """Respond to events (mouse clicks, key presses) and update the display.

    Note that the event loop is an *infinite loop*: it continually waits for
    the next event, determines the event's type, and then updates the state
    of the visualisation or the tree itself, updating the display if necessary.
    This loop ends when the user closes the window.

    @type screen: pygame.Surface
    @rtype: None
    """

    selected_mellow = 2
    selected_depth = 2
    selected_loop = 4

    while True:
        # Wait for an event
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return

        elif event.type == pygame.KEYDOWN:
            play_melody(event)

        elif event.type == pygame.KEYUP:
            stop_melody(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            # mellow/dry ratings
            if 50 <= event.pos[0] <= 75 and 150 <= event.pos[1] <= 175:
                # mellow = 0
                erase_previous_rating(selected_mellow, 152)
                selected_mellow = 0
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (52, 152, 21, 21))
                pygame.display.flip()
            elif 90 <= event.pos[0] <= 115 and 150 <= event.pos[1] <= 175:
                # mellow = 1
                erase_previous_rating(selected_mellow, 152)
                selected_mellow = 1
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (92, 152, 21, 21))
                pygame.display.flip()
            elif 130 <= event.pos[0] <= 155 and 150 <= event.pos[1] <= 175:
                # mellow = 2
                erase_previous_rating(selected_mellow, 152)
                selected_mellow = 2
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (132, 152, 21, 21))
                pygame.display.flip()
            elif 170 <= event.pos[0] <= 195 and 150 <= event.pos[1] <= 175:
                # mellow = 3
                erase_previous_rating(selected_mellow, 152)
                selected_mellow = 3
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (172, 152, 21, 21))
                pygame.display.flip()
            elif 210 <= event.pos[0] <= 235 and 150 <= event.pos[1] <= 175:
                # mellow = 4
                erase_previous_rating(selected_mellow, 152)
                selected_mellow = 4
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (212, 152, 21, 21))
                pygame.display.flip()

            # depth ratings
            elif 50 <= event.pos[0] <= 75 and 300 <= event.pos[1] <= 325:
                # depth = 0
                erase_previous_rating(selected_depth, 302)
                selected_depth = 0
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (52, 302, 21, 21))

                pygame.display.flip()
            elif 90 <= event.pos[0] <= 115 and 300 <= event.pos[1] <= 325:
                # depth = 1
                erase_previous_rating(selected_depth, 302)
                selected_depth = 1
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (92, 302, 21, 21))
                pygame.display.flip()
            elif 130 <= event.pos[0] <= 155 and 300 <= event.pos[1] <= 325:
                # depth = 2
                erase_previous_rating(selected_depth, 302)
                selected_depth = 2
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (132, 302, 21, 21))
                pygame.display.flip()
            elif 170 <= event.pos[0] <= 195 and 300 <= event.pos[1] <= 325:
                # depth = 3
                erase_previous_rating(selected_depth, 302)
                selected_depth = 3
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (172, 302, 21, 21))
                pygame.display.flip()
            elif 210 <= event.pos[0] <= 235 and 300 <= event.pos[1] <= 325:
                # depth = 4
                erase_previous_rating(selected_depth, 302)
                selected_depth = 4
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (212, 302, 21, 21))
                pygame.display.flip()

            # loop length
            elif 340 <= event.pos[0] <= 365 and 150 <= event.pos[1] <= 175:
                # loop = 2
                erase_previous_loop(selected_loop)
                selected_loop = 2
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (342, 152, 21, 21))
                draw_loop_numbers(screen)
                pygame.display.flip()
            elif 380 <= event.pos[0] <= 405 and 150 <= event.pos[1] <= 175:
                # loop = 4
                erase_previous_loop(selected_loop)
                selected_loop = 4
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (382, 152, 21, 21))
                draw_loop_numbers(screen)
                pygame.display.flip()
            elif 420 <= event.pos[0] <= 445 and 150 <= event.pos[1] <= 175:
                # loop = 8
                erase_previous_loop(selected_loop)
                selected_loop = 8
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (422, 152, 21, 21))
                draw_loop_numbers(screen)
                pygame.display.flip()
            elif 460 <= event.pos[0] <= 485 and 150 <= event.pos[1] <= 175:
                # loop = 16
                erase_previous_loop(selected_loop)
                selected_loop = 16
                pygame.draw.rect(screen, pygame.color.THECOLORS['tomato'],
                                 (462, 152, 21, 21))
                draw_loop_numbers(screen)
                pygame.display.flip()

            # 'create' button was pressed 350, 230, 120, 40
            elif 350 <= event.pos[0] <= 470 and 230 <= event.pos[1] <= 270:
                # create loop
                pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                                 (590, 30, 100, 330))
                loop = Loop(selected_loop, selected_mellow, selected_depth)

                coordinates = [620, 40]

                loop_chords = []
                bass_keys = []
                loop_chord_objects = []

                for measure_counter in range(loop.measures):
                    if measure_counter == 0:
                        previous = None
                        previous_voice = None

                    chord = choose_chord(loop, measure_counter, previous)
                    previous = chord
                    loop_chord_objects.append(chord)

                    voice = get_voicing(chord, loop, previous_voice)
                    previous_voice = voice

                    font = pygame.font.SysFont(FONT_FAMILY, 25)

                    text_surface = font.render(get_chord_name(chord, loop),
                                               1,
                                               pygame.color.THECOLORS['black'])
                    text_pos = coordinates
                    screen.blit(text_surface, text_pos)

                    pygame.display.flip()

                    coordinates[1] += 20

                    characters = []
                    char1 = ''
                    for char in voice:
                        if char != ' ':
                            char1 += char
                        else:
                            characters.append(char1)
                            char1 = ''

                    sharp_or_flat = key_sharp_or_flat(loop.key)
                    if sharp_or_flat == 's':
                        chosen_notes = notes_sharp
                    else:  # sharp_or_flat == 'f'
                        chosen_notes = notes_flat

                    bass_note = chosen_notes.index(loop.key[0]) + chord.interval
                    if bass_note > 11:
                        bass_note -= 12

                    loop_chords.append(characters)
                    bass_keys.append(chosen_notes[bass_note])

                play_chords(loop_chords, bass_keys, loop_chord_objects, loop)


def play_chords(chords, bass, loop_chord_objects, current_loop):
    """Plays the chords which are indicated by the parameter chords

    @type chords: list[list[str]]
    @type bass: list[str]
    @type loop_chord_objects: list[Chord]
    @type current_loop: Loop
    @rtype: None
    """
    while True:
        count = -1

        for chord_change in chords:
            perc_deep.stop()
            perc_mid.stop()
            perc_high.stop()
            perc_deep.play()
            perc_mid.play()
            perc_high.play()

            notes_played = []
            bass_played = None
            for note in harmony_notes:
                if note.name in chord_change:
                    note.sound.play()
                    notes_played.append(note)

            for key in keys:
                key.in_scale = False

            time1 = pygame.time.get_ticks()
            count += 1  # counter used to keep track of bass note & dashed line

            for bass_note in bass_notes:
                if bass_note.name == bass[count]:
                    bass_note.sound.play()
                    bass_played = bass_note

            if count == 0:
                pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                                 (605, 45, 12, 3))

                pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                                 (605, 45 + 20 * (len(chords) - 1), 12, 3))
                pygame.display.flip()
            else:
                pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                                 (605, 45 + 20 * count, 12, 3))

                pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                                 (605, 45 + 20 * (count - 1), 12, 3))
                pygame.display.flip()

            draw_piano()
            draw_chord_scale(loop_chord_objects[count], current_loop)

            forward = False
            while not forward:
                event = pygame.event.poll()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 350 <= event.pos[0] <= 470 and \
                            285 <= event.pos[1] <= 325:
                        for note in notes_played:
                            note.sound.fadeout(400)
                        bass_played.sound.fadeout(400)
                        perc_deep.fadeout(400)
                        perc_mid.fadeout(400)
                        perc_high.fadeout(400)
                        # draw_piano()
                        for key in keys:
                            key.in_scale = False
                        return

                elif event.type == pygame.KEYDOWN:
                    play_melody(event)

                elif event.type == pygame.KEYUP:
                    stop_melody(event)

                if pygame.time.get_ticks() > time1 + 2970:
                    for note in notes_played:
                        note.sound.fadeout(300)
                    bass_played.sound.fadeout(300)
                    forward = True


def play_melody(event):
    """Plays or stops a melody note

    @type event: pygame.event
    @rtype: None
    """
    if event.key == pygame.K_a:
        C0k.pressed = True
        C0.sound.play()
        C0k.draw_key('red3')
    elif event.key == pygame.K_w:
        Db0k.pressed = True
        Db0.sound.play()
        Db0k.draw_key('red3')
    elif event.key == pygame.K_s:
        D0k.pressed = True
        D0.sound.play()
        D0k.draw_key('red3')
    elif event.key == pygame.K_e:
        Eb0k.pressed = True
        Eb0.sound.play()
        Eb0k.draw_key('red3')
    elif event.key == pygame.K_d:
        E0k.pressed = True
        E0.sound.play()
        E0k.draw_key('red3')
    elif event.key == pygame.K_f:
        F0k.pressed = True
        F0.sound.play()
        F0k.draw_key('red3')
    elif event.key == pygame.K_t:
        F_0k.pressed = True
        F_0.sound.play()
        F_0k.draw_key('red3')
    elif event.key == pygame.K_g:
        G0k.pressed = True
        G0.sound.play()
        G0k.draw_key('red3')
    elif event.key == pygame.K_y:
        Ab0k.pressed = True
        Ab0.sound.play()
        Ab0k.draw_key('red3')
    elif event.key == pygame.K_h:
        A0k.pressed = True
        A0.sound.play()
        A0k.draw_key('red3')
    elif event.key == pygame.K_u:
        Bb0k.pressed = True
        Bb0.sound.play()
        Bb0k.draw_key('red3')
    elif event.key == pygame.K_j:
        B0k.pressed = True
        B0.sound.play()
        B0k.draw_key('red3')
    elif event.key == pygame.K_k:
        C1k.pressed = True
        C1.sound.play()
        C1k.draw_key('red3')
    elif event.key == pygame.K_o:
        Db1k.pressed = True
        Db1.sound.play()
        Db1k.draw_key('red3')
    elif event.key == pygame.K_l:
        D1k.pressed = True
        D1.sound.play()
        D1k.draw_key('red3')
    elif event.key == pygame.K_p:
        Eb1k.pressed = True
        Eb1.sound.play()
        Eb1k.draw_key('red3')
    elif event.key == pygame.K_SEMICOLON:
        E1k.pressed = True
        E1.sound.play()
        E1k.draw_key('red3')
    elif event.key == pygame.K_RETURN:
        F1k.pressed = True
        F1.sound.play()
        F1k.draw_key('red3')
    pygame.display.flip()


def stop_melody(event):
    """Stops a melody note

    @type event: pygame.event
    @rtype: None
    """
    if event.key == pygame.K_a:
        C0.sound.stop()
        C0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(C0k)],
                         (44, 402, 43, 128))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(C0k)],
                         (44, 530, 63, 68))
    elif event.key == pygame.K_w:
        Db0.sound.stop()
        Db0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Db0k)],
                         (89, 402, 36, 126))
    elif event.key == pygame.K_s:
        D0.sound.stop()
        D0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(D0k)],
                         (109, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(D0k)],
                         (127, 402, 25, 128))
    elif event.key == pygame.K_e:
        Eb0.sound.stop()
        Eb0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Eb0k)],
                         (154, 402, 36, 126))
    elif event.key == pygame.K_d:
        E0.sound.stop()
        E0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(E0k)],
                         (174, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(E0k)],
                         (192, 402, 45, 128))
    elif event.key == pygame.K_f:
        F0.sound.stop()
        F0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(F0k)],
                         (239, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(F0k)],
                         (239, 402, 43, 128))
    elif event.key == pygame.K_t:
        F_0.sound.stop()
        F_0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(F_0k)],
                         (284, 402, 36, 126))
    elif event.key == pygame.K_g:
        G0.sound.stop()
        G0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(G0k)],
                         (304, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(G0k)],
                         (322, 402, 25, 128))
    elif event.key == pygame.K_y:
        Ab0.sound.stop()
        Ab0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Ab0k)],
                         (349, 402, 36, 126))
    elif event.key == pygame.K_h:
        A0.sound.stop()
        A0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(A0k)],
                         (369, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(A0k)],
                         (387, 402, 25, 128))
    elif event.key == pygame.K_u:
        Bb0.sound.stop()
        Bb0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Bb0k)],
                         (414, 402, 36, 126))
    elif event.key == pygame.K_j:
        B0.sound.stop()
        B0k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(B0k)],
                         (434, 530, 63, 68))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(B0k)],
                         (452, 402, 45, 128))
    elif event.key == pygame.K_k:
        C1.sound.stop()
        C1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(C1k)],
                         (499, 402, 43, 128))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(C1k)],
                         (499, 530, 63, 68))
    elif event.key == pygame.K_o:
        Db1.sound.stop()
        Db1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Db1k)],
                         (544, 402, 36, 126))
    elif event.key == pygame.K_l:
        D1.sound.stop()
        D1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(D1k)],
                         (582, 402, 25, 128))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(D1k)],
                         (564, 530, 63, 68))
    elif event.key == pygame.K_p:
        Eb1.sound.stop()
        Eb1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(Eb1k)],
                         (609, 402, 36, 126))
    elif event.key == pygame.K_SEMICOLON:
        E1.sound.stop()
        E1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(E1k)],
                         (192+65*7, 402, 45, 128))
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(E1k)],
                         (629, 530, 63, 68))
    elif event.key == pygame.K_RETURN:
        F1.sound.stop()
        F1k.pressed = False
        pygame.draw.rect(screen, pygame.color.THECOLORS[key_to_color(F1k)],
                         (694, 402, 61, 196))
    pygame.display.flip()


def key_to_color(key):
    """Returns the color that the key should return to

    @type key: Key
    @rtype: str
    """
    if key.in_scale:
        return 'tomato'
    else:
        return key.color


def draw_chord_scale(chord, current_loop):
    """Takes a chord and highlights which keys should be played over it

    @type chord: Chord
    @type current_loop: Loop
    @rtype: None
    """

    sharp_or_flat = chord_sharp_or_flat(chord, current_loop)
    if sharp_or_flat == 's':
        chosen_notes = notes_sharp
    else:  # sharp_or_flat == 'f'
        chosen_notes = notes_flat

    scale_notes = []
    root = chosen_notes.index(current_loop.key[0]) + chord.interval

    if root > 11:
        root -= 12

    for scale in chord.chord_scale:
        scale_notes.append(root + scale)

    for scale in scale_notes:
        if scale > 11:
            scale_notes[scale_notes.index(scale)] = scale - 12

    if 0 in scale_notes:
        # A
        A0k.in_scale = True
        if not A0k.pressed:
            A0k.draw_key('tomato')

    if 1 in scale_notes:
        # Bb
        Bb0k.in_scale = True
        if not Bb0k.pressed:
            Bb0k.draw_key('tomato')

    if 2 in scale_notes:
        # B
        B0k.in_scale = True
        if not B0k.pressed:
            B0k.draw_key('tomato')

    if 3 in scale_notes:
        # C
        C0k.in_scale = True
        C1k.in_scale = True
        if not C0k.pressed:
            C0k.draw_key('tomato')

        if not C1k.pressed:
            C1k.draw_key('tomato')

    if 4 in scale_notes:
        # Db
        Db0k.in_scale = True
        Db1k.in_scale = True
        if not Db0k.pressed:
            Db0k.draw_key('tomato')

        if not Db1k.pressed:
            Db1k.draw_key('tomato')

    if 5 in scale_notes:
        # D
        D0k.in_scale = True
        D1k.in_scale = True
        if not D0k.pressed:
            D0k.draw_key('tomato')

        if not D1k.pressed:
            D1k.draw_key('tomato')

    if 6 in scale_notes:
        # Eb
        Eb0k.in_scale = True
        Eb1k.in_scale = True
        if not Eb0k.pressed:
            Eb0k.draw_key('tomato')

        if not Eb1k.pressed:
            Eb1k.draw_key('tomato')

    if 7 in scale_notes:
        # E
        E0k.in_scale = True
        E1k.in_scale = True
        if not E0k.pressed:
            E0k.draw_key('tomato')

        if not E1k.pressed:
            E1k.draw_key('tomato')

    if 8 in scale_notes:
        # F
        F0k.in_scale = True
        F1k.in_scale = True
        if not F0k.pressed:
            F0k.draw_key('tomato')

        if not F1k.pressed:
            F1k.draw_key('tomato')

    if 9 in scale_notes:
        # F#
        F_0k.in_scale = True
        if not F_0k.pressed:
            F_0k.draw_key('tomato')

    if 10 in scale_notes:
        # G
        G0k.in_scale = True
        if not G0k.pressed:
            G0k.draw_key('tomato')

    if 11 in scale_notes:
        # Ab
        Ab0k.in_scale = True
        if not Ab0k.pressed:
            Ab0k.draw_key('tomato')

    pygame.display.flip()


def draw_piano():
    """Draws a piano

    @rtype: None
    """
    pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                     (42, 400, 715, 200))

    pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                     (44, 402, 711, 196))

    for x in range(107, 697, 65):
        pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                         (x, 400, 2, 200))

    for x in range(87, 672, 65):
        if x != 87 + 65 * 2 and x != 87 + 65 * 6:
            pygame.draw.rect(screen, pygame.color.THECOLORS['black'],
                             (x, 400, 40, 130))

    for key in keys:
        if key.pressed:
            key.draw_key('red3')

    pygame.display.flip()


def erase_previous_rating(rating, y):
    """De-selects the previous mellow/dryness rating

    @type rating: int
    @type y: int
    @rtype: None
    """
    if rating == 0:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (52, y, 21, 21))
        pygame.display.flip()
    elif rating == 1:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (92, y, 21, 21))
        pygame.display.flip()
    elif rating == 2:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (132, y, 21, 21))
        pygame.display.flip()
    elif rating == 3:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (172, y, 21, 21))
        pygame.display.flip()
    else:  # rating == 4
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (212, y, 21, 21))
        pygame.display.flip()


def erase_previous_loop(loop):
    """De-selects the previous loop length

    @type loop: int
    @rtype: None
    """
    if loop == 2:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (342, 152, 21, 21))
        pygame.display.flip()
    elif loop == 4:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (382, 152, 21, 21))
        pygame.display.flip()
    elif loop == 8:
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (422, 152, 21, 21))
        pygame.display.flip()
    else:  # loop == 16
        pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                         (462, 152, 21, 21))
        pygame.display.flip()


def draw_loop_numbers(screen):
    """Renders the numbers for the loop lengths

    @type screen: pygame.Surface
    @rtype: None
    """
    font = pygame.font.SysFont(FONT_FAMILY, 25)

    text_surface = font.render('2', 1, pygame.color.THECOLORS['black'])
    text_pos = (348, 155)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('4', 1, pygame.color.THECOLORS['black'])
    text_pos = (388, 155)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('8', 1, pygame.color.THECOLORS['black'])
    text_pos = (428, 155)
    screen.blit(text_surface, text_pos)

    text_surface = font.render('16', 1, pygame.color.THECOLORS['black'])
    text_pos = (463, 155)
    screen.blit(text_surface, text_pos)

    # This must be called *after* all other pygame functions have run.
    pygame.display.flip()


if __name__ == '__main__':

    # Setup pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 650))

    pygame.mixer.init()
    pygame.mixer.set_num_channels(40)

    A = Sound('A', pygame.mixer.Sound('A.wav'))
    Bb = Sound('Bb', pygame.mixer.Sound('Bb.wav'))
    B = Sound('B', pygame.mixer.Sound('B.wav'))
    C = Sound('C', pygame.mixer.Sound('C.wav'))
    Db = Sound('Db', pygame.mixer.Sound('Db.wav'))
    D = Sound('D', pygame.mixer.Sound('D.wav'))
    Eb = Sound('Eb', pygame.mixer.Sound('Eb.wav'))
    E = Sound('E', pygame.mixer.Sound('E.wav'))
    F = Sound('F', pygame.mixer.Sound('F.wav'))
    F_ = Sound('F#', pygame.mixer.Sound('F_.wav'))
    G = Sound('G', pygame.mixer.Sound('G.wav'))
    Ab = Sound('Ab', pygame.mixer.Sound('Ab.wav'))
    harmony_notes = [A, Bb, B, C, Db, D, Eb, E, F, F_, G, Ab]

    for harmony_note in harmony_notes:
        harmony_note.sound.set_volume(0.5)

    bassA = Sound('A', pygame.mixer.Sound('bassA.wav'))
    bassBb = Sound('Bb', pygame.mixer.Sound('bassBb.wav'))
    bassB = Sound('B', pygame.mixer.Sound('bassB.wav'))
    bassC = Sound('C', pygame.mixer.Sound('bassC.wav'))
    bassDb = Sound('Db', pygame.mixer.Sound('bassDb.wav'))
    bassD = Sound('D', pygame.mixer.Sound('bassD.wav'))
    bassEb = Sound('Eb', pygame.mixer.Sound('bassEb.wav'))
    bassE = Sound('E', pygame.mixer.Sound('bassE.wav'))
    bassF = Sound('F', pygame.mixer.Sound('bassF.wav'))
    bassF_ = Sound('F#', pygame.mixer.Sound('bassF_.wav'))
    bassG = Sound('G', pygame.mixer.Sound('bassG.wav'))
    bassAb = Sound('Ab', pygame.mixer.Sound('bassAb.wav'))
    bass_notes = [bassA, bassBb, bassB, bassC, bassDb, bassD, bassEb, bassE,
                  bassF, bassF_, bassG, bassAb]

    for bass_note in bass_notes:
        bass_note.sound.set_volume(0.7)

    C0 = Sound('C', pygame.mixer.Sound('C0.wav'))
    Db0 = Sound('Db', pygame.mixer.Sound('Db0.wav'))
    D0 = Sound('D', pygame.mixer.Sound('D0.wav'))
    Eb0 = Sound('Eb', pygame.mixer.Sound('Eb0.wav'))
    E0 = Sound('E', pygame.mixer.Sound('E0.wav'))
    F0 = Sound('F', pygame.mixer.Sound('F0.wav'))
    F_0 = Sound('F#', pygame.mixer.Sound('F_0.wav'))
    G0 = Sound('G', pygame.mixer.Sound('G0.wav'))
    Ab0 = Sound('Ab', pygame.mixer.Sound('Ab0.wav'))
    A0 = Sound('A', pygame.mixer.Sound('A0.wav'))
    Bb0 = Sound('Bb', pygame.mixer.Sound('Bb0.wav'))
    B0 = Sound('B', pygame.mixer.Sound('B0.wav'))
    C1 = Sound('C', pygame.mixer.Sound('C1.wav'))
    Db1 = Sound('Db', pygame.mixer.Sound('Db1.wav'))
    D1 = Sound('D', pygame.mixer.Sound('D1.wav'))
    Eb1 = Sound('Eb', pygame.mixer.Sound('Eb1.wav'))
    E1 = Sound('E', pygame.mixer.Sound('E1.wav'))
    F1 = Sound('F', pygame.mixer.Sound('F1.wav'))
    melody_notes = [C0, Db0, D0, Eb0, E0, F0, F_0, G0, Ab0, A0, Bb0, B0, C1,
                    Db1, D1, Eb1, E1, F1]

    for melody_note in melody_notes:
        melody_note.sound.set_volume(1.0)

    perc_deep = pygame.mixer.Sound('perc_deep.wav')
    perc_mid = pygame.mixer.Sound('perc_mid.wav')
    perc_high = pygame.mixer.Sound('perc_high.wav')
    perc_deep.set_volume(0.5)
    perc_mid.set_volume(1.0)
    perc_high.set_volume(1.0)

    pygame.draw.rect(screen, pygame.color.THECOLORS['tan'],
                     (0, 0, 800, 650))

    C0k = Key('C', 'tan')
    Db0k = Key('Db', 'black')
    D0k = Key('D', 'tan')
    Eb0k = Key('Eb', 'black')
    E0k = Key('E', 'tan')
    F0k = Key('F', 'tan')
    F_0k = Key('F#', 'black')
    G0k = Key('G', 'tan')
    Ab0k = Key('Ab', 'black')
    A0k = Key('A', 'tan')
    Bb0k = Key('Bb', 'black')
    B0k = Key('B', 'tan')
    C1k = Key('C', 'tan')
    Db1k = Key('Db', 'black')
    D1k = Key('D', 'tan')
    Eb1k = Key('Eb', 'black')
    E1k = Key('E', 'tan')
    F1k = Key('F', 'tan')
    keys = [C0k, Db0k, D0k, Eb0k, E0k, F0k, F_0k, G0k, Ab0k, A0k, Bb0k, B0k,
            C1k, Db1k, D1k, Eb1k, E1k, F1k]

    # Render the display
    render_display(screen)

    # Start an event loop to respond to events.
    event_loop(screen)

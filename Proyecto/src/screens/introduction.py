'''Introduction and 1st Screen of the Application.'''
import math
import time
import tkinter as tk
from typing import Any

import PySimpleGUI as sg

from .. import constants
from ..controllers import observer, theme
from ..assets import animated_intro
from . import _csg


# Fix for frame loading at image animation
# The normal behaviour no takes in count the subsample passed trought initialization at sg.Image instance
# By this reason the element loose the property an displays the frames incorrectly
def update_animation(self: Any, source: str | bytes, time_between_frames: int = 0) -> None:
    '''Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
        NOTE - does NOT perform a sleep call to delay
        :param source:              Filename or Base64 encoded string containing Animated GIF
        :type source:               str | bytes | None
        :param time_between_frames: Number of milliseconds to wait between showing frames
        :type time_between_frames:  (int)'''
    if self.Source != source:
        self.AnimatedFrames = None
        self.Source = source
    if self.AnimatedFrames is None:
        self.TotalAnimatedFrames = 0
        self.AnimatedFrames: list[tk.PhotoImage] = []  # type: ignore

        if type(source) is bytes:
            cfg = {'data': source}
        else:
            cfg = {'file': source}

        for i in range(1000):
            cfg['format'] = 'gif -index %i' % (i)  # type: ignore
            try:
                if self.ImageSubsample:
                    self.AnimatedFrames.append(
                        tk.PhotoImage(**cfg).subsample(self.ImageSubsample)
                    )
                else:
                    self.AnimatedFrames.append(tk.PhotoImage(**cfg))
            except Exception as e:
                break

        self.TotalAnimatedFrames = len(self.AnimatedFrames)
        self.LastFrameTime = time.time()
        self.CurrentFrameNumber = -1

    now = time.time()

    if time_between_frames:
        if (now - self.LastFrameTime) * 1000 > time_between_frames:
            self.LastFrameTime = now
            self.CurrentFrameNumber = (
                self.CurrentFrameNumber + 1) % self.TotalAnimatedFrames
        else:
            return
    else:
        self.CurrentFrameNumber = (
            self.CurrentFrameNumber + 1) % self.TotalAnimatedFrames
    image = self.AnimatedFrames[self.CurrentFrameNumber]
    try:
        self.tktext_label.configure(
            image=image, width=image.width(), height=image.height()
        )
    except Exception as e:
        print('Exception in update_animation', e)


# Fix appliement
sg.Image.update_animation = update_animation


SCREEN_NAME = '-INTRODUCTION-'
SHADOW_FRAMES = 31
FRAMES = animated_intro.frames
FRAME_TIME = 47
BACKGROUND_COLOR = '#000000'
count = FRAMES + SHADOW_FRAMES


image = sg.Image(
    data=animated_intro.source,
    background_color=BACKGROUND_COLOR,
    size=(theme.width, theme.height),
    subsample=math.ceil(animated_intro.size/theme.width)
)


def animation_loop() -> None:
    '''Takes care about the events and frames for displaying the introduction gif.'''
    global count
    count -= 1
    if count == 0:
        observer.unsubscribe(constants.TIMEOUT, animation_loop)
        observer.subscribe(constants.TIMEOUT, disable_screen)
    elif count >= SHADOW_FRAMES:
        image.update_animation(animated_intro.source, FRAME_TIME)


def disable_screen() -> None:
    '''Finalize the animation events and change the view to profile selection screen.'''
    observer.unsubscribe(constants.TIMEOUT, disable_screen)
    observer.post_event(constants.UPDATE_TIMEOUT, None)
    observer.post_event(constants.GOTO_SCREEN, '-SELECT-PROFILE-')


screen_layout = [
    [_csg.centered(image, background_color=BACKGROUND_COLOR)],
]

screen_config = {
    'background_color': BACKGROUND_COLOR,
    'element_justification': 'center',
}


def screen_reset() -> None:
    '''Reset the animation related variables to a starting point and starts the animation.'''
    global count
    count = FRAMES + SHADOW_FRAMES
    observer.subscribe(constants.TIMEOUT, animation_loop)
    observer.post_event(constants.UPDATE_TIMEOUT, FRAME_TIME)

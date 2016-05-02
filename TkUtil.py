import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import tix

import typing as tg


STICK_ALL = frozenset([tix.N, tix.W, tix.S, tix.E])
STICK_HORIZONTAL = frozenset([tix.W, tix.E])
STICK_VERTICAL = frozenset([tix.N, tix.S])
STICK_N = frozenset([tix.N])
STICK_W = frozenset([tix.W])
STICK_S = frozenset([tix.S])
STICK_E = frozenset([tix.E])

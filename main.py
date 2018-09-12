from collections import namedtuple
import os
import pathlib

import jinja2
import matplotlib.pyplot as plt
import numpy as np


BUILD_DIR = 'build'
FIG_DIR = os.path.join(BUILD_DIR, 'figures')

# make dirs if they don't exist
pathlib.Path(BUILD_DIR).mkdir(parents=True, exist_ok=True)
pathlib.Path(FIG_DIR).mkdir(parents=True, exist_ok=True)

# Create the jinja template
renderer = jinja2.Environment(
    block_start_string='%{',
    block_end_string='%}',
    variable_start_string='%{{',
    variable_end_string='%}}',
    loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = renderer.get_template('templates/content.tex')

# Content goes in cells
TextCell = namedtuple('Cell', ['text'])
FigureCell = namedtuple('Cell', ['text', 'figure', 'caption'])

# Write some basic text content
text = TextCell(text='Hello world!')

# Write a figure block
x = np.linspace(0, 1, 1000)
y = np.sin(2 * np.pi * x)
fg, ax = plt.subplots()
ax.plot(x, y)
fg.tight_layout()
figname = 'sine.pdf'
fg.savefig(os.path.join(FIG_DIR, figname))
figure = FigureCell(
    text='Here is a nice plot of a sine wave.',
    figure=figname,
    caption='A sinusoidal wave of 1Hz over one period.'
)

# Save content
cells = [text, figure]
output_filename = os.path.join(BUILD_DIR, 'output.tex')
with open(output_filename, 'w') as f:
    f.write(template.render(cells=cells))

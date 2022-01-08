import random
import subprocess
from pathlib import Path

import drawerFunctions as df
import PySimpleGUI as sg

import paletteImg
from colors import colors

layout2 = [

    [sg.Column([
        [sg.Image(key = "PREVIEW", size=(40, 40))],
        [sg.Button('Start', disabled=True)],
        [sg.Button('Save', disabled=True)],
        [sg.Checkbox('Open at end', key='OPENATEND')]
    ]),

   
    sg.Column([
        [sg.Text("File")],
        [sg.Text("Colors")],
        [sg.Text("Background")]
    ]),

    sg.Column([
        [sg.Input(key = 'FILE', enable_events=True)],
        [
        sg.pin(sg.Input('#000000', key='COLORS', enable_events=True)), 
        sg.pin(sg.Image(filename=None, visible=False, key='PALETTE')),
        sg.pin(sg.Button('New Colors', visible=False, key='NEWCOLORS')),
        sg.pin(sg.Button('Order', visible=False, key='ORDER'))
        ],
        [sg.Input("None", key='BACKGROUND')]
    ]),
    
    sg.Column([
        [sg.FileBrowse('Browse', target = 'FILE', enable_events=True)],
        [sg.Checkbox("Randomize", key='RANDOMWINDOW', enable_events=True)]
    ])],


    [sg.Text("Select a file", size=(70,1), key='OUT')]

]

window = sg.Window('Swap Colors', layout2, auto_size_buttons=True)
lock = True
while True:
    event, values = window.read()


    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'FILE':
        window['PREVIEW'].Update(data=None)
        img_colors = str(Path(values['FILE']).stem).split("_")
        img_name = img_colors[0]
        img_colors = img_colors[1:]
        if len(img_colors) == 0:
            lock = True
            window['OUT'].Update('File should be: name_hexcolor_hexcolor...extension')
            continue
        
        for i in range(len(img_colors)):
            if '#' not in img_colors[i]:
                img_colors[i] = '#' + img_colors[i]

        numOfColors = len(img_colors)
        lock = False


    

    window['OUT'].Update('')

    if event == 'RANDOMWINDOW':
        for each in ['PALETTE', 'NEWCOLORS', 'ORDER']:
            window[each].Update(visible=values['RANDOMWINDOW'])
        
        window['COLORS'].Update(visible= not(values['RANDOMWINDOW']))

    if lock:
        if values['FILE'] == '':
            window['OUT'].Update('Select a file')
        continue


    if event == 'NEWCOLORS':
        colorsAndNames = sum(random.sample(list(colors.items()), numOfColors), ())
        colorCodes = list(colorsAndNames[::2])
        colorNames = " x ".join(colorsAndNames[1::2])
        palette = paletteImg.main(colorCodes, 100, 20)
        window['PALETTE'].update(data = df.image_to_data(palette))
    
    if event == "ORDER":
        try:
            random.shuffle(colorCodes)
            palette = paletteImg.main(colorCodes, 100, 20)
            window['PALETTE'].update(data = df.image_to_data(palette))
        except Exception:
            window['OUT'].Update('Error in shuffling')

    if event == 'NEWCOLORS' or event == 'COLORS':
        [window[each].Update(disabled=False) for each in ['Start', 'Save']]

    if event == 'Start':
        if values['RANDOMWINDOW'] == False:
            colorNames = None
            colorCodes = values['COLORS'].strip('\n')

            if colorCodes[0] == '[' and colorCodes[-1] == ']':
                colorCodes = eval(colorCodes)
            else:
                try:
                    colorCodes = colorCodes.replace(" ", "").strip('\n').split(",")
                except:
                    colorCodes = [colorCodes]

            for i in range(len(colorCodes)):
                if '#' not in colorCodes[i]:
                    colorCodes[i] = '#' + colorCodes[i]

        if values['BACKGROUND'].strip('\n').strip(" ") == 'None':
            values['BACKGROUND'] = None
        elif '#' not in values['BACKGROUND']: 
            values['BACKGROUND'] = '#' + values['BACKGROUND']
        
        img = df.openImage(values['FILE'])[0].convert("RGBA")

        for i in range(len(img_colors)):
            src = df.hexToRgb(img_colors[i])
            dst = df.hexToRgb(colorCodes[i])
            img = df.replaceColor(img, (*src,255), (*dst,255))
           
        bg = df.backgroundPNG(*img.size, values['BACKGROUND'])[0]
        bg = df.pasteItem(bg, img, 0, 0)
        
        window['PREVIEW'].Update(data = df.image_to_data(df.resizeToFit(bg, 100)))


    if event == 'Save':
        fileName = img_name + "_" + "_".join(colorCodes).replace('#', "") + ".png"
        bg.save(fileName, optimize = True)

    if values['OPENATEND']:
        try:
            subprocess.Popen(r'explorer /select,"{}"'.format(fileName))
        except:
            pass


window.close()

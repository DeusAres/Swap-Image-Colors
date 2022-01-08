import drawerFunctions as df

def main(colors, W, H):

    CB, CD = df.backgroundPNG(W, H)
    i=0
    for x in range(0, W//(len(colors))*len(colors), W//(len(colors))):
        CD.rectangle([x,0,x+W//(len(colors)),H], fill = colors[i])
        i+=1

    CB = df.cropToRealSize(CB)
    #CB.show()
    return CB



#main(['#d62839', '#ba324f', '#175676', '#4ba3c3', '#ba324f'], 100, 20)
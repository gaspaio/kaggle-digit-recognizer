import matplotlib.pyplot as plt
import matplotlib.pylab as plb

DDIM = (28,28)

def dshow(data, d=0):
    digit = data[d,:]
    plb.imshow(digit.reshape(DDIM), cmap="Greys")
    plt.show()
    return


def dmosaic(ds=[], cols=10):

    rows = len(ds) / cols + 1 

    for i in range(1,len(ds) + 1):
        plt.subplot(rows,cols,i,frameon=False, xticks=[], yticks=[])
        plt.imshow(ds[i-1].reshape(DDIM), cmap="Greys")
    
    plt.subplots_adjust(hspace=0.001, wspace=0.002) 
    plt.show()

    return



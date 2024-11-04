#todo track signature must be ready before playing  / /
#save file/ 

clock.tempo=175
with open('C:/Users/jo/Krease/30 minu/init.py', 'r') as file:
    code = file.read()
    exec(code) 

Pg * d( r_patterns( V.compagnion8  )   ,orbit=3,amp=0.15,oct=P("6"),snap=10.5,vel=127,p="4",d=2,dur=1)

Pg * d( [sss,": 11   ."]   ,start=0, end=1, amp=.51,oct=P("5"),snap=10.5,vel=127,p="1",d=1,dur=1)

panic()


SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass.fxp");""")

###################################################### preset write #

print( P(' getA  compagnion1'),"<<<",V.compagnion1, V.instrument, V.state ,"<<")

panic()

print(V.scramble, V.compagnion1, V.instrument, V.state ,"<<")

def pat(gate=1, compagnon=None):
    comp = compagnon
    if gate <= 0:
        comp = '.'
    return comp
    
V.gate=[1,1,1,1,1,1,1,1,1,1,1,1,1]

V.compagnion="X K Q X .  X XXX "

V.compagnion1="X . K X .  K XXK"


V.compagnion1="[F2@maj9  ]"


V.compagnion1="k O K X O  KOXHXK"
#V.compagnion1="K H H"

V.compagnion2="[F1 . ]+[[1][12][3][-2][4]]!!34"

#V.compagnion1="KO."

@swim
def fun(p=1,i=0): 
    D(" [vsti1  : D@maj9      ]", oct=("-1"),vel=127 ,dur= 1 , i=i/16) #base32 / 3 \working 1 0!2  -1!4 
    again(fun, p=1/16,i=i+1) 


V.userinput='cmd1_8' #6

V.userinput= '[E1 .!32   ]+[[0][0][0][0][1][3]]!!8'


V.userinput='cmd1_7' #6

V.userinput= '[E0 ]+12+[[0][0][0][0][1][3]]!!64'

V.userinput='cmd1'

V.userinput= '[[F0][E0] ]+12+[[0][0][1][3]]!!8'

V.userinput='dnb'

V.userinput='4'

V.userinput='intro'

############################################

V.userinput='cmd2_6'    #*****

V.userinput='cmd2'

V.userinput= '[E2       ]+12+[[0][0][0][0][1][3]]!!64'  #********

V.userinput= '[F0       ]+[[0][0][0][0][1][3]]!!8'


############################################

V.userinput='cmd1_11' #6

V.userinput= '[E1!4 .!32  F0 FF0 F1!8 G1!16 .!16 ]+[[0][0][0][0][1][3]]!!8'

V.userinput= '[F!16 F1!8 G1!16  F4!2[32]  [F1  ]!64 ]+[[1][1][2][0][1][3]]!!8'

############################################

V.userinput='cmd2'

V.userinput='cmdx'

V.userinput='cmd1'

V.userinput='cmd0'

##################################################
V.userinput='cmd1_5'

V.userinput= '[F1 .!32   ]+[[0][0][0][0][1][3]]!!8'

V.userinput='cmd1'

############################################


V.userinput='cmd3' #*****

V.userinput= '[.!8   F1 .!16   ]+[[0][0][0][0][1][3]]!!8'

##########################################################

V.userinput='.'

V.userinput = "cmd7break"

V.userinput = "V:1" 

V.userinput = "V:6" 

V.userinput = "[V:3]!4 " 
############################################################


V.userinput = "cmd9" 

V.userinput = "B:8 .!9+9 B:8  .!9+9  I:4 .!9+9 " 


V.userinput = "B:8 .!9+9+9  B:7  .!9+9  I:4 .!9+9 " 


V.userinput = "B:6 .!9+9  B:6  .!9+9  I:4 .!9+9 " 


V.userinput = "G:[7:2 ]     " 
############################################################


V.userinput='switch'

V.userinput='transition'

V.userinput='dropb'

V.userinput='dropa'

V.userinput='intro'


V.userinput='cmdx'

############################################################

V.userinput='Q       '

V.userinput='QHHHHH  "


V.userinput = "cmd8break"

V.userinput = "P:3 " 

############################################################

V.userinput='cmd1'

V.userinput= '[F1 .!8  ]+[[0][0][0][0][1][3]]!!8'

############################################################

V.userinput="cmd4_4"


V.userinput="cmd4_e"


V.userinput= '[F5                                    ]+[1 2 3 4 5 -3 ]'

############################################################

V.userinput='cmd5'

V.userinput='cmd5_e'


V.userinput='cmd5_3'

V.userinput= '[C4!2  ]+[1 4 5 1]!!8'

V.userinput='cmd5_4'

V.userinput= '[C4!2 ]+[1 4 5 1]!!8'   #nashvell chords

V.userinput='cmd6'

V.userinput= '[c1 ]+[1 ]!!8'   #nashvell chords



V.userinput='cmd5_6'  #danger 


############################################################


#####

V.userinput = "cmd8break"

V.userinput = "V:3"

V.userinput = "cmd7break"

V.userinput = "P:3" 

V.userinput='cmd1'

V.userinput= '[[F1] [E1]]+[[0]]!!8'

V.userinput='cmdx'

V.userinput='Q       '

V.userinput='Qk k k k'

V.userinput='kkk kkkkkkkkk'

V.userinput='kkkkkkkkkkkkk'

panic()



V.info="drum and ambiant "


clock.tempo = 175

# Initialize global variables
V.current_section = 1
V.bar_count = 0
V.section_lengths = {
    1: 5,  # intro
    2: 10,  # build up
    3: 8,   # pre drop (short)
    4: 32,  # drop
    5: 16,  # extend
    6: 16,  # drop mini
    7: 32,  # breakdown and buildup B
    8: 16,  # switch
    9: 32,  # drop 2
    10: 16, # mixout
    11: 16  # outro
}

@swim
def dnb_track(p=1, i=0):
    # Increment bar count
    V.bar_count = i
    # Check if it's time to switch to the next section
    if V.bar_count == V.section_lengths[V.current_section]:
        V.current_section += 1
        V.bar_count = 0
        if V.current_section > 11:
            V.current_section = 1  # Reset to intro or end the track
    # Set info based on current section
    match V.current_section:
        case 1: 
            V.info = "intro tension ambiant drums low version melody"

            
        case 2: V.info = "build up , Bass"
        case 3: V.info = "pre drop [short]"
        case 4: V.info = "drop   16"
        case 5: V.info = "extend"
        case 6: V.info = "drop mini"
        case 7: V.info = "breakdown and buildup B"
        case 8: V.info = "switch"
        case 9: V.info = "drop 2  16"
        case 10: V.info = "mixout"
        case 11: V.info = "outro"
        case 12: panic()
    write_to_shared_memory(V.info)
    print(f"Section: {V.current_section}, Info: {V.info}",i)
    again(dnb_track, p=4, i=i+1)  # Call again every bar


trackname = "Na2O · CaO · 6SiO2   _     glass"

cmd1_pat_A =  '[E1 .!32   ]+[[0][0][0][0][1][3]]!!8'

cmd1_pat_B =  '[E0 ]+12+[[0][0][0][0][1][3]]!!64'

cmd2_patA   =  '[E2       ]+12+[[0][0][0][0][1][3]]!!64'

cmd1_pat_C = '[E1!4 .!32  F0 FF0 F1!8 G1!16 .!16 ]+[[0][0][0][0][1][3]]!!8'

cmd3_pat_A = '[.!8   F1 .!16   ]+[[0][0][0][0][1][3]]!!8'

cmd9_pat_A =  "B:8 .!9+9 B:8  .!9+9  I:4 .!9+9 " 
 
cmd4_pat_A =  '[F5                                    ]+[1 2 3 4 5 -3 ]'

cmd5_pat_A= '[C4!2  ]+[1 4 5 1]!!8'

cmd6_pat_A='[c1 ]+[1 ]!!8'   #nashvell chords




V.off=0
V.tblk=16  #timeblock
V.ssp=48
@swim
def dnb_track(p=1,i=0):   
    etrack="▽▽▼▼▲▲▷▣▣▣▣▷◎◎◎◎▷▣▣▣▣▷▶▶▶▶▷▣▣▣▣▷▣▣▣▣▷▶▶▶▶▷▼▼▽▽▽▽x"#▼▼▼▼▲▲▲▲▷▣▣▣▣▷▣▣▣▣▣▣▷▣▣▣▣▷▣▣▣▷▼▼▲▷▣▣▣"#▽▽▼▼▼▼▲▲▲▲▷▷▽▣▣▣▣▷▷▽▷▣▣▣▣"# ▣▣▣▣▷▷▣▣▣▣▷▷▣▣▣▣▷▷"#▣▣▷▷▣▣▣▷▣▣▷ ▣▣▷"#▣▣▣▣▣▣▣▣▣▣▶▷◎◎▣▣▣▣_▣▣▣▣▶▷◎◎▣▣▣▣x"
    print(show_part(etrack, 0,1+int(V.off+( (i/16)/V.tblk))%len(etrack)),int(( (i/16)/V.tblk)),V.off)
    #match 101:# 
    match  show_part(etrack, 0,1+int(V.off+( (i/16)/ V.tblk ))%len(etrack))[-1]:             
     case  "▽":
           bass   pad   Fx          impact   Bass2  melo
         4  A B | x     x                      x           #intro
         8  A B | A B   A                      x            #buildup
                                                        silence
            A B         A           A          x        # dropa
                        A           A          A   A    # buildup
                  A B               A              A    # break
                                                        silence
                                    A              A    # dropb
                                                        # transition
                                                   A    # outro              
                           
                           
                           
                           #outro

     case  101: pass
     case  "▲": pass
     case  "▼": pass;
     case  "▣":pass 
     case  "◎":pass   
     case  "▶":pass 
     case  "▷":pass 
     case  " ":pass  
     case  "x":panic()
    again(dnb_track,p=1/16,i=i+1) 


V.cmd10=0

@swim
def fun(p=1,i=0): 
    D(  r_patterns( pat(V.gate[0] ,V.compagnion )  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i) 
    N(f"[ {pat(V.gate[2] ,V.compagnion1) }  ] '", chan=1, vel=120, i=i)
    D(r_patterns(   pat(V.gate[1] ,V.compagnionm1 ) )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    D(f'vsti1  : [ {pat(V.gate[2] ,V.compagnion1) }  ] ',oct=("1"),vel=127 ,dur= 1 , i=i/4) #base32 / 3 \working 1 0!2  -1!4 
    D(f'vsti2  : [ { pat(V.gate[3],V.compagnion2) } ] ',oct=("0"),vel=127 ,dur= 4 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti5  : [ { pat(V.gate[6], V.compagnion5) } ] ',oct=("0"),vel=7,gain=.51,amp=0.2 ,dur= 2 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti5  : [ {pat(V.gate[7] , V.compagnion6) } ] ',oct=("0"),vel=70,gain=1,amp=0.2 ,dur= 1 , i=i/2) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti3  : [ { pat(V.gate[4], V.compagnion3) } ] ',oct=("0"),vel=27 ,dur= 3.2 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    again(fun, p=1/16,i=i+1) 

@swim
def fun1(p=1,i=0):   
    if V.cmd7==1: 
        V.start1 = P(f'[{V.scramble}]!!4',i=i/4)/100  
        V.end1=V.start1
    if V.cmd7==1: 
        V.start2 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ",i=i)/10
        V.end2=V.start2 
    if V.cmd10==1: 
        V.start3 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ",i=i)/10
        V.end3=V.start3    
    def w(n=3, nn=4, nnn='.', nnnn=5):
         return {
        D([ff, f":{n} .  "],d=1, vel=1, speed='1 ',amp=0.2, gain=0.771, rate=1, cutoff=4000, hcutoff=210,orbit=orbdrum , room=0.0, dry=0, snap=0, size=0, i=i/64),
        D([ff, f":{nn} ."],d=1, vel=1, speed='1 ',gain=0.871, rate=1,cutoff=2800, hcutoff=505,orbit=orbdrum , room=0.0, dry=10,snap=0, size=0, i=i/64),
        D([fff, f":{nnn} .!8"],d=1, vel=1, speed='1 ',gain=0.971, rate=2,cutoff=4800, hcutoff=100, orbit=orbdrum ,room=0.0, dry=0,snap=0, size=0, i=i/16),
        D([ffff, f":{nnnn} .!2"],d=1, vel=1, speed='1.25',gain=0.771, rate=1,cutoff=9800, hcutoff=1200, orbit=orbdrum ,room=0.0, dry=0,snap=0.6, size=0, i=i/16)
    } 
    def rise2():D(r_patterns(pat(V.gate[10] , V.compagnion9)  ) ,speed=1,amp=.815,oct=P("4"),vel=127,i=i/4,d=V.ssp,dur=2)
    def impact():D(r_patterns(pat(V.gate[9] , V.compagnion8 )) ,begin=V.start2, end=V.end2+0.012, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def voix():D(r_patterns( pat(V.gate[8] ,V.compagnion7 )) ,legato=8,	oct=5 ,begin=V.start1, end=V.end1+0.012,gain=1, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i/2)     
    def percution():D(r_patterns(pat(V.gate[11] , V.compagnion10 )) ,begin=V.start3, end=V.end3+0.012, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    D(f'vsti4  : [ { pat(V.gate[5] ,V.compagnion4 )} ] ',oct=("0"),vel=7 ,dur= 4 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    rise2(),voix(),impact()
    match V.state :
        case 'a':V.gate=[1,1,1,1,1,1,1,1,1,1,1];  w( '7', '8~2','.', '2');V.orbdrum=1#intro
        #
        case 'b':V.gate=[1,0,0,0,1,1,1,1,1,1,1];  w( '4~13', 16,'.', '6'); V.orbdrum=2 #buildup
        case 'c':V.gate=[1,0,1,1,0,1,1,0,0,1,1];  pass #w( '4~13', 16,'.', '6');#dropa
        case 'd':V.gate=[0,0,0,1,1,1,1,0,0,1,1];  w( '9~19', 17,'.', '6');V.orbdrum=3#dropb
        case 'e':V.gate=[0,0,1,1,1,1,1,1,1,1,1];  V.orbdrum=2#w( '4~13', 16,'.', '6');#outro
        case 'f':V.gate=[1,1,1,0,1,1,1,1,1,1,1];  w( '4~13', 12,'.', '6'); V.orbdrum=1 #switch
        case 'g':V.gate=[0,0,0,1,1,1,1,1,1,1,1];  pass #w( '4~13', 16,'.', '6'); #transition
        case 'h':V.gate=[1,1,0,0,0,1,1,1,1,1,1];  pass
        case 'i':V.gate=[0,0,0,0,0,1,1,0,0,1,1];  pass#w( '4~13', 16,'.', '6');#break                                                                                           
        case "◈":  V.tb=1;   fill(); 
    again(fun1, p=1/16,i=i+1)



print( qualifiers )# r_patterns( V.compagnion  ))

panic()

########################################################################################################################################
stop_flag.clear()

stop_flagw.clear()

console=1

stop_flag.set()

V.compagnion ="X X."

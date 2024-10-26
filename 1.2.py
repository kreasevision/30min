#todo add bass and melody / /
#reduce 12 code évaluation

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

print(V.scramble, V.compagnion, V.instrument, V.state ,"<<")

def pat(gate=1, compagnon=None):
    comp = compagnon
    if gate <= 0:
        comp = '.'
    return comp
    
V.gate=[1,1,0,1,1,1,1,1,1,1,1,1,1]

V.compagnion="X K Q X .  X XXX "

V.compagnion1="X . K X .  K XXK"

V.compagnion1="k O K X O  KOXHXK"
#V.compagnion1="K H H"

V.compagnion2="[F1 . ]+[[1][12][3][-2][4]]!!34"

#V.compagnion1="KO."

@swim
def fun(p=1,i=0): 
    D(  r_patterns( pat(V.gate[0] ,V.compagnion )  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i) 
    D(r_patterns(   pat(V.gate[1] ,V.compagnionm1 ) )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    D(f'vsti1  : [ {pat(V.gate[2] ,V.compagnion1) }  ] ',oct=("1"),vel=127 ,dur= 1 , i=i/4) #base32 / 3 \working 1 0!2  -1!4 
    D(f'vsti2  : [ { pat(V.gate[3],V.compagnion2) } ] ',oct=("0"),vel=127 ,dur= 8 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
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
    def w(n=3, nn=4, nnn='.', nnnn=5):
         return {
        D([ff, f":{n} .  "],d=1, vel=1, speed='1 ',amp=0.2, gain=0.771, rate=1, cutoff=4000, hcutoff=210,orbit=orbdrum , room=0.0, dry=0, snap=0, size=0, i=i/64),
        D([ff, f":{nn} ."],d=1, vel=1, speed='1 ',gain=0.871, rate=1,cutoff=2800, hcutoff=505,orbit=orbdrum , room=0.0, dry=10,snap=0, size=0, i=i/64),
        D([fff, f":{nnn} .!8"],d=1, vel=1, speed='1 ',gain=0.971, rate=2,cutoff=4800, hcutoff=100, orbit=orbdrum ,room=0.0, dry=0,snap=0, size=0, i=i/16),
        D([ffff, f":{nnnn} .!2"],d=1, vel=1, speed='1.25',gain=0.771, rate=1,cutoff=9800, hcutoff=1200, orbit=orbdrum ,room=0.0, dry=0,snap=0.6, size=0, i=i/16)
    } 
    def rise2():D(r_patterns(pat(V.gate[10] , V.compagnion9)  ) ,speed=1,amp=.815,oct=P("4"),vel=127,i=i/4,d=V.ssp,dur=2)
    def impact():D(r_patterns(pat(V.gate[9] , V.compagnion8 )) ,begin=V.start2, end=V.end2+0.012, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def voix():D(r_patterns( pat(V.gate[8] ,V.compagnion7 )) ,legato=8,	oct=5 ,begin=V.start1, end=V.end1+0.012,gain=0.89, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i/2)     
    D(f'vsti4  : [ { pat(V.gate[5] ,V.compagnion4 )} ] ',oct=("0"),vel=7 ,dur= 3.2 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    rise2(),voix(),impact()
    match V.state :
        case 'a':V.gate=[1,1,1,1,1,1,1,1,1,1,1];  w( '7', '8~2','.', '2');V.orbdrum=1#intro
        case 'b':V.gate=[0,0,0,0,0,1,1,1,1,1,1];  w( '4~13', 16,'.', '6'); V.orbdrum=2 #buildup
        case 'c':V.gate=[0,0,0,0,0,1,1,1,1,1,1];  pass #w( '4~13', 16,'.', '6');#dropa
        case 'd':V.gate=[1,0,0,0,0,1,1,1,1,1,1];  w( '9~19', 17,'.', '6');V.orbdrum=3#dropb
        case 'e':V.gate=[0,0,0,1,1,1,1,1,1,1,1];  V.orbdrum=2#w( '4~13', 16,'.', '6');#outro
        case 'f':V.gate=[1,0,0,0,0,1,1,1,1,1,1];  w( '4~13', 12,'.', '6'); V.orbdrum=1 #switch
        case 'g':V.gate=[0,0,1,0,0,1,1,1,1,1,1];  pass #w( '4~13', 16,'.', '6'); #transition
        case 'h':V.gate=[1,0,0,0,0,1,1,1,1,1,1];  pass
        case 'i':V.gate=[0,0,0,0,0,1,1,1,1,1,1];  pass#w( '4~13', 16,'.', '6');#break                                                                                           
        case "◈":  V.tb=1;   fill(); 
    again(fun1, p=1/16,i=i+1)


 

print( r_patterns( V.compagnion  ))

panic()

########################################################################################################################################
stop_flag.clear()

stop_flagw.clear()

console=1

stop_flag.set()

V.compagnion ="X X."

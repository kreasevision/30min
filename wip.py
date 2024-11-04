@swim
def fun1(p=1, i=0):
    if V.cmd7 == 1:
        V.start1 = V.end1 = P(f'[{V.scramble}]!!4', i=i/4)/100
        V.start2 = V.end2 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ", i=i)/10
    if V.cmd10 == 1:
        V.start3 = V.end3 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ", i=i)/10

    def w(n=3, nn=4, nnn='.', nnnn=5):
        return {
            D([ff, f":{n} .  "], d=1, vel=1, speed='1 ', amp=0.2, gain=0.771, rate=1, cutoff=4000, hcutoff=210, orbit=orbdrum, room=0.0, dry=0, snap=0, size=0, i=i/64),
            D([ff, f":{nn} ."], d=1, vel=1, speed='1 ', gain=0.871, rate=1, cutoff=2800, hcutoff=505, orbit=orbdrum, room=0.0, dry=10, snap=0, size=0, i=i/64),
            D([fff, f":{nnn} .!8"], d=1, vel=1, speed='1 ', gain=0.971, rate=2, cutoff=4800, hcutoff=100, orbit=orbdrum, room=0.0, dry=0, snap=0, size=0, i=i/16),
            D([ffff, f":{nnnn} .!2"], d=1, vel=1, speed='1.25', gain=0.771, rate=1, cutoff=9800, hcutoff=1200, orbit=orbdrum, room=0.0, dry=0, snap=0.6, size=0, i=i/16)
        }

    def rise2(): D(r_patterns(pat(V.gate[10], V.compagnion9)), speed=1, amp=.815, oct=P("4"), vel=127, i=i/4, d=V.ssp, dur=2)
    def impact(): D(r_patterns(pat(V.gate[9], V.compagnion8)), begin=V.start2, end=V.end2+0.012, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i)
    def voix(): D(r_patterns(pat(V.gate[8], V.compagnion7)), legato=8, oct=5, begin=V.start1, end=V.end1+0.012, gain=1, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i/2)
    def percution(): D(r_patterns(pat(V.gate[11], V.compagnion10)), begin=V.start3, end=V.end3+0.012, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i)

    D(f'vsti4  : [ {pat(V.gate[5], V.compagnion4)} ]', oct=("0"), vel=7, dur=4, i=i/8)
    rise2()
    voix()
    impact()

    state_actions = {
        'a': lambda: (V.gate[:] = [1,1,1,1,1,1,1,1,1,1,1], w('7', '8~2', '.', '2'), setattr(V, 'orbdrum', 1)),
        'b': lambda: (V.gate[:] = [1,0,0,0,1,1,1,1,1,1,1], w('4~13', 16, '.', '6'), setattr(V, 'orbdrum', 2)),
        'c': lambda: V.gate[:] = [1,0,1,1,0,1,1,0,0,1,1],
        'd': lambda: (V.gate[:] = [0,0,0,1,1,1,1,0,0,1,1], w('9~19', 17, '.', '6'), setattr(V, 'orbdrum', 3)),
        'e': lambda: (V.gate[:] = [0,0,1,1,1,1,1,1,1,1,1], setattr(V, 'orbdrum', 2)),
        'f': lambda: (V.gate[:] = [1,1,1,0,1,1,1,1,1,1,1], w('4~13', 12, '.', '6'), setattr(V, 'orbdrum', 1)),
        'g': lambda: V.gate[:] = [0,0,0,1,1,1,1,1,1,1,1],
        'h': lambda: V.gate[:] = [1,1,0,0,0,1,1,1,1,1,1],
        'i': lambda: V.gate[:] = [0,0,0,0,0,1,1,0,0,1,1],
        '◈': lambda: (setattr(V, 'tb', 1), fill())
    }

    action = state_actions.get(V.state)
    if action:
        action()

    again(fun1, p=1/16, i=i+1)



from functools import lru_cache

@lru_cache(maxsize=128)
def cached_D(*args, **kwargs):
    return D(*args, **kwargs)

def optimized_fun(p=1, i=0):
    gate_companion_pairs = [
        (V.gate[0], V.compagnion),
        (V.gate[1], V.compagnionm1),
        (V.gate[2], V.compagnion1),
        (V.gate[3], V.compagnion2),
        (V.gate[6], V.compagnion5),
        (V.gate[7], V.compagnion6),
        (V.gate[4], V.compagnion3)
    ]

    for idx, (gate, companion) in enumerate(gate_companion_pairs):
        if idx < 2:
            cached_D(r_patterns(pat(gate, companion)), orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i)
        else:
            oct = "1" if idx == 2 else "0"
            vel = 127 if idx < 4 else (7 if idx == 4 else (70 if idx == 5 else 27))
            dur = 1 if idx in (2, 5) else (4 if idx == 3 else (2 if idx == 4 else 3.2))
            i_div = 4 if idx in (2, 3, 6) else (8 if idx == 4 else 2)
            gain = 0.51 if idx == 4 else 1
            amp = 0.2 if idx in (4, 5) else 1
            cached_D(f'vsti{idx+1 if idx < 5 else idx}  : [ {pat(gate, companion)} ]', oct=(oct), vel=vel, dur=dur, i=i/i_div, gain=gain, amp=amp)

    again(optimized_fun, p=1/16, i=i+1)

def optimized_fun1(p=1, i=0):
    if V.cmd7 == 1:
        V.start1 = V.end1 = P(f'[{V.scramble}]!!4', i=i/4)/100
        V.start2 = V.end2 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ", i=i)/10
    
    if V.cmd10 == 1:
        V.start3 = V.end3 = P("  [4 4 4 4 ][5 5 5 5 6  7 7 7 3 3 3 3 2 2 2 ] [2 6 6 3 15 4 ]!3 [2  2 2 2 2 3  4]!3  ", i=i)/10

    @lru_cache(maxsize=32)
    def w(n=3, nn=4, nnn='.', nnnn=5):
        return {
            cached_D([ff, f":{n} .  "], d=1, vel=1, speed='1 ', amp=0.2, gain=0.771, rate=1, cutoff=4000, hcutoff=210, orbit=orbdrum, room=0.0, dry=0, snap=0, size=0, i=i/64),
            cached_D([ff, f":{nn} ."], d=1, vel=1, speed='1 ', gain=0.871, rate=1, cutoff=2800, hcutoff=505, orbit=orbdrum, room=0.0, dry=10, snap=0, size=0, i=i/64),
            cached_D([fff, f":{nnn} .!8"], d=1, vel=1, speed='1 ', gain=0.971, rate=2, cutoff=4800, hcutoff=100, orbit=orbdrum, room=0.0, dry=0, snap=0, size=0, i=i/16),
            cached_D([ffff, f":{nnnn} .!2"], d=1, vel=1, speed='1.25', gain=0.771, rate=1, cutoff=9800, hcutoff=1200, orbit=orbdrum, room=0.0, dry=0, snap=0.6, size=0, i=i/16)
        }

    def rise2(): cached_D(r_patterns(pat(V.gate[10], V.compagnion9)), speed=1, amp=.815, oct=P("4"), vel=127, i=i/4, d=V.ssp, dur=2)
    def impact(): cached_D(r_patterns(pat(V.gate[9], V.compagnion8)), begin=V.start2, end=V.end2+0.012, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i)
    def voix(): cached_D(r_patterns(pat(V.gate[8], V.compagnion7)), legato=8, oct=5, begin=V.start1, end=V.end1+0.012, gain=1, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i/2)
    def percution(): cached_D(r_patterns(pat(V.gate[11], V.compagnion10)), begin=V.start3, end=V.end3+0.012, orbit=orbdrum, d=V.ssp, speed=1, room=0.01, dry=1, i=i)

    cached_D(f'vsti4  : [ {pat(V.gate[5], V.compagnion4)} ]', oct=("0"), vel=7, dur=4, i=i/8)
    rise2(), voix(), impact()

    state_actions = {
        'a': lambda: (setattr(V, 'gate', [1,1,1,1,1,1,1,1,1,1,1]), w('7', '8~2', '.', '2'), setattr(V, 'orbdrum', 1)),
        'b': lambda: (setattr(V, 'gate', [1,0,0,0,1,1,1,1,1,1,1]), w('4~13', 16, '.', '6'), setattr(V, 'orbdrum', 2)),
        'c': lambda: setattr(V, 'gate', [1,0,1,1,0,1,1,0,0,1,1]),
        'd': lambda: (setattr(V, 'gate', [0,0,0,1,1,1,1,0,0,1,1]), w('9~19', 17, '.', '6'), setattr(V, 'orbdrum', 3)),
        'e': lambda: (setattr(V, 'gate', [0,0,1,1,1,1,1,1,1,1,1]), setattr(V, 'orbdrum', 2)),
        'f': lambda: (setattr(V, 'gate', [1,1,1,0,1,1,1,1,1,1,1]), w('4~13', 12, '.', '6'), setattr(V, 'orbdrum', 1)),
        'g': lambda: setattr(V, 'gate', [0,0,0,1,1,1,1,1,1,1,1]),
        'h': lambda: setattr(V, 'gate', [1,1,0,0,0,1,1,1,1,1,1]),
        'i': lambda: setattr(V, 'gate', [0,0,0,0,0,1,1,0,0,1,1]),
        '◈': lambda: (setattr(V, 'tb', 1), fill())
    }

    state_actions.get(V.state, lambda: None)()

    again(optimized_fun1, p=1/16, i=i+1)

# Replace the original functions with the optimized versions
fun = swim(optimized_fun)
fun1 = swim(optimized_fun1)    


   section  duration  bass   pad   Fx impact   Bass2 melo
    Intro     32.0   A B   A B    x      x  #intro    x
 Build-up     64.0 A B C A B C  A B      A       x    x
  Silence      8.0                                     
   Drop A     64.0 A B C   B C  B x      B     A B  B C
 Build-up     48.0   A B   A B  A B      A     A B  A B
    Break     32.0 A B C A B C  A B      A       A    A
  Silence      8.0                                     
   Drop B     64.0 A B C   A B  B C    B C     A B  A B
Transition    16.0                                     
    Outro     32.0     A   A C             A          A




    def handle_case(case=""):
    match case:
        case "intro_S":
            PisteA[0] = V.compagnion
            PisteB[0] = V.compagnion
        case "buildup_S":
            PisteA[1] = V.compagnion
            PisteB[1] = V.compagnion
        case "dropa_S":
            PisteA[2] = V.compagnion
            PisteB[2] = V.compagnion
        case "dropb_S":
            PisteA[3] = V.compagnion
            PisteB[3] = V.compagnion
        case "outro_S":
            PisteA[4] = V.compagnion
            PisteB[4] = V.compagnion
        case "switch_S":
            PisteA[5] = V.compagnion
            PisteB[5] = V.compagnion
        case "transition_S":
            PisteA[6] = V.compagnion
            PisteB[6] = V.compagnion
        case "break_S":
            PisteA[7] = V.compagnion
            PisteB[7] = V.compagnion
        case "full_S":
            PisteA[8] = V.compagnion
            PisteB[8] = V.compagnion
        case _:
            print(f"Unrecognized case: {case}")


handle_case("outro_S")

V.compagnion[0]=' . '
V.compagnion[1]=' . . '


for i in range(1, 10):
    PisteA[i] = V.compagnion
    PisteB[i] = V.compagnion

    pres(V.face,3,"cmd4_2");

V.presets_SA[V.state  ][0]="dxdddcc"

print("step variables 2")  

print(V.state) 

print(V.presets_SA) 

print("step variables 2")  
time.sleep(5)

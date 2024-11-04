from window_terminal import WindowTerminal
import threading
import subprocess
import sys
import os
import time
from multiprocessing import shared_memory
from copy import deepcopy

time.sleep(10)

SC.info()
trackname= "dnb"
clock.tempo=175


SHARED_MEMORY_SIZE = 1024 
SHARED_MEMORY_NAME1 = "my_memory4"
shm1 = shared_memory.SharedMemory(name=SHARED_MEMORY_NAME1, create=True, size=SHARED_MEMORY_SIZE)
 

time.sleep(.1)
compagnion_path = os.path.join("C:/Users/jo/Krease/30 minu/", "UI.py")
cmd = f'start cmd /k "{sys.executable} "{compagnion_path}""'


def write_to_shared_memory(text):
     # Encode the string to bytes
    encoded_text = text.encode('utf-8')
     # Ensure the encoded text fits within the shared memory size
    if len(encoded_text) > SHARED_MEMORY_SIZE - 1:
        raise ValueError("Text is too long for the shared memory buffer")
     # Write the encoded text to the shared memory buffer
    shm1.buf[:len(encoded_text)] = encoded_text
    # Null terminate the buffer
    shm1.buf[len(encoded_text)] = 0  # Null terminator
    shm1.buf[len(encoded_text)+1:] = b'\0' * (SHARED_MEMORY_SIZE - len(encoded_text) - 1)


# # Example usage
text_to_write = "Hello, World!1"
write_to_shared_memory(text_to_write)


subprocess.Popen(cmd, shell=True)

V.info="step1 buss |||||10%"
write_to_shared_memory(V.info)
# Making a new OSC-In Handler
listener = OSCInHandler(
    ip="127.0.0.1",
    port=44447,
    name="Listener",
    loop=osc_loop
)
output_one = OSCHandler(
    ip="127.0.0.1", port=41234,
    name="A first test connexion",
    ahead_amount=0.0, loop=osc_loop, # The default OSC loop, don't ask why!
)
bowl.add_handler(output_one)
one = output_one.send
bowl.add_handler(listener)
time.sleep(3)

V.info="loaded1|||"
write_to_shared_memory(V.info)


print("loaded")
time.sleep(1)

#We open bus and direct orbit where we want. On this exemple  one orbit go to one effect and is output on the main output
#Bus and vst effect is powerfull to mix and regulate every sound/ also a good way to build ear candy but it can be cpu intensive.

SC("""(
~effectBus1 = Bus.audio(s, 2);   
~effectBus2 = Bus.audio(s, 2); 
~effectBus3 = Bus.audio(s, 2); 
~vitalBus = Bus.audio(s, 2); 
~vsti1_Bus = Bus.audio(s, 2); 
~vsti2_Bus = Bus.audio(s, 2); 
~vsti3_Bus = Bus.audio(s, 2); 
~vsti4_Bus = Bus.audio(s, 2); 
~vsti5_Bus = Bus.audio(s, 2); 
~ottBus = Bus.audio(s, 2);  
~sardine = Bus.audio(s, 2); 
~effectBus1kick = Bus.audio(s, 2);   
~effectBus2kick = Bus.audio(s, 2); 
~effectBus1break = Bus.audio(s, 2); 
~mainOutBus = 0;
~dirt.orbits[1].outBus =~vitalBus  ;
~dirt.orbits[2].outBus =~ottBus  ;
~dirt.orbits[3].outBus =~effectBus1break  ;
)""")

time.sleep(2)
print("step1 buss ")  

V.info="step1 buss |||||30%"
write_to_shared_memory(V.info)

 
V.compagnion = [None] * 10
#all sample variable 
V.ssp=4   #variable change d on some some patern 
V.progress=1 #timeblock chan help to pose and and play etc
orbdrum=2     #orbit variable can be helpfull to trigger effect
aa=" stjakick:16 " 
bb=" stjasnares:13"
cc=" hats: 1"
cc2="hihats"  
dd=" ..    "
ddd=" . . .  "
dddd=" .... "
d1=" . "
d2=".. "
d3=" ... "
d4=" .... "
d5=" ....."
d6=" ...... " 
d7=" ......."
d8= " ........ "
d10= " .......... "
ee=" percusion"
ff="akasl"
fff="drumloops"
ffff="radbreak"
ffb="vbreak"
ffv="vfill"
gg="glitchs"
hh="impact"
ii="chant"
jj="vocal"
kk="stab"
ll="tonal:11"
mm="devastatorrises"
nn="hloop"   # voix#
oo="akasos"
pp="akapad"
qq="hloop"
rr="antamelo"
ss="voc"
sss="voc2"
ssss="voc3"
tt="piano"
uu="clap"
vv="kick"
V.compagnion[0] = "x.0."
def show_part(s, start, length):
    char_array = list(s)
   # Ensure start index is within bounds
    start = max(0, min(start, len(char_array) - 1))
    #  Ensure length doesn't exceed string length
    length = min(length, len(char_array) - start)
    #  Extract the desired part
    part = char_array[start:start+length]
    # Convert back to string and return
    return ''.join(part)

    
def pg(n=1):
    if(n==0) :return 1
    if(n>0): return (((1/16)/4)/4)/n 

time.sleep(2)
print("step1 variables")  
     
     #interesting  fx  fx:4~10
#we start with loading all the sample using dirt and supercolider language inside sardine directly
SC("""~dirt.loadSoundFileFolder("E:/music pack/STRANJAH-FREE-SAMPLE-PACK-VOL-1/kicks","stjakick")""")
SC( """~dirt.loadSoundFileFolder("Epack/STRANJAH-FREE-SAMPLE-PACK-VOL-1/hihats")""")
SC("""~dirt.loadSoundFileFolder("E:/music pack/STRANJAH-FREE-SAMPLE-PACK-VOL-1/snares","stjasnares")""")
SC( """~dirt.loadSoundFiles("E:/music pack/AKAS DNB ESSENTIALS/drumhits/*"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/AKAS DNB ESSENTIALS/drumloops","akasl")""")
SC("""~dirt.loadSoundFileFolder("E:/music pack/musicradar-drumnbass-170bpm/Beats/Samples","drumloops"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/musicradar-breakbeat-140bpm/Breaks/Loops","radbreak"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/seb/# Sons/Vengeance/VENGEANCE ESSENTIAL CLUB SOUNDS vol-1/VENGEANCE ESSENTIAL CLUB SOUNDS vol-1/VENGEANCE ESSENTIAL CLUB SOUNDS vol-1/VEC1 BreakBeats","vbreak"); """ )
SC("""~dirt.loadSoundFileFolder("E:/music pack/Tonal Ambience/","tonal"); """ )
SC( """~dirt.loadSoundFileFolder("E:/music pack/Tonal Impacts","impact"); """ )  
SC("""~dirt.loadSoundFileFolder("E:/music pack/AKAS DNB ESSENTIALS/BASS ONE SHOTS","akasos")""")
SC("""~dirt.loadSoundFileFolder("E:/music pack/50 Best Free Vocal Samples","voc"); """ ) 
SC( """~dirt.loadSoundFileFolder("E:/music pack/musicradar-stab-samples/Misc Stabs","stab"); """ )  
SC( """~dirt.loadSoundFileFolder("E:/music pack/10-Glitch-Sound-Effects/10 Glitch Sound Effects","glitchs");""")
SC( """~dirt.loadSoundFileFolder("E:/Everyday_music/Evolution+-+Devastator+Warzone+-+Free+Edition+(WAV)/Evolution - Devastator Warzone - Free Edition (WAV)/03. ONESHOTS/04.TONAL FX/Rises","devastatorrises");""")
SC( """~dirt.loadSoundFileFolder("E:/music pack/Distortion Glitch SFX Courtesy of PremiumBeat","prglitch");""")
SC("""~dirt.loadSoundFileFolder("E:/music pack/Horizons-Gospel Melody Collection/Horizons - Gospel Melody Collection","piano"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/CymaticsEuphoriaVocalSamplePack-V4-h7y/Cymatics - Infinity Vocal Pack/Vocal Chops","voc3"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/General Guyble - Free Frenchcore Shots Vol.1/GGFF1_Clap","clap"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/STRANJAH-FREE-SAMPLE-PACK-VOL-1/kicks","kick"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/Cymatics - Infinity Vocal Pack/Vocal Loops","voc2"); """ ) 
SC("""~dirt.loadSoundFileFolder("E:/music pack/WAProd_Free_Vocal_Loops_Chops/WAV Loops & Cuts/House Loops","hloop"); """ )

V.info="step1 samples |||||||"
write_to_shared_memory(V.info)
print("step samples ")  
time.sleep(10)

#2 function to load the vst and vsti
SC("""(
~loadVST = { |synthDefName, vstFilePath, vstID, outBus = 0|
    var synth, controller;
    SynthDef(synthDefName, { |out, vstID|
        var effect;
        effect = VSTPlugin.ar(nil, 2, id: vstID); 
        Out.ar(out, effect); 
    }).add;
    synth = Synth(synthDefName, [\\out, outBus, \\vstID, vstID]);
    controller = VSTPluginController(synth);
    controller.open(vstFilePath, editor: true, multiThreading: true);
    Routine {
        while { controller.isOpen.not } { 0.1.wait; };
        "Loaded VSTi %".format(synthDefName).postln;
    }.play;
    controller;
};
~loadVSTeffect = { |synthDefName, vstFilePath, vstID, inBus = 0, outBus = 0|
    var synth, controller;
    SynthDef(synthDefName, { |in, out, vstID|
        var effect;
        effect = VSTPlugin.ar(In.ar(in, 2), 2, id: vstID);
        Out.ar(out, effect);
    }).add;  
    synth = Synth.after(~dirt.group,synthDefName, [\\in, inBus, \\out, outBus, \\vstID, vstID]);
    controller = VSTPluginController(synth);
    controller.open(vstFilePath, editor: true, multiThreading: true);
    Routine {
        while { controller.isOpen.not } { 0.1.wait; };
        "Loaded VSTi %".format(synthDefName).postln;
    }.play;
    controller;
};
)""")

print("step4")  
time.sleep(3)

V.info="r patern |||||||50%"
write_to_shared_memory(V.info)




def r_patterns(pattern_string):
    mappings = {'K':vv,'X': aa, 'O': bb ,'Q': uu,'H': cc, '|': ee,'V': ss, 'W': sss, 'U': ssss ,'I': hh,'T': nn,'R': mm, 'B': oo,'P': tt, 'S': kk ,'C': ii ,'G': gg }
    result = [mappings.get(char, char) for char in pattern_string]
    return result

def save_pattern(pattern_array, filename):
    with open(filename, 'w') as file:
        for line in pattern_array:
            file.write(line + '\n') 


def record(user_input):
    with open('C:/Users/jo/Krease/30 minu/test.pat', 'a') as file:
        file.write(user_input + '\n')



print("step patern ")  
time.sleep(7)

#loading the vst effect  weirdly i need to run them 2 time to be sure
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\130, ~ottBus , 0 );)""") #ott
SC("""(~vstEffectbreak= ~loadVSTeffect.value(\\shaperbox, "E:/vst/ShaperBox 3.vst3", \\136,  ~effectBus1break   ,~vitalBus  );)""") #ott

SC("""(~vstEffect1 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\13, ~vsti1_Bus   , 0 );)""") #ott
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\14, ~vsti2_Bus   , 0 );)""") #ott
SC("""(~vstEffect3 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\15, ~vsti3_Bus   , 0 );)""") #ott
SC("""(~vstEffect4 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\16, ~vsti4_Bus   , 0 );)""") #ott
SC("""(~vstEffect5 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\17, ~vsti5_Bus   , 0 );)""") #ott





#loading the vsti effect  weirdly i need to run them 2 time to be su
SC("""(
~vst1 = ~loadVST.value(\\vsti1, "E:/vst/Vital.vst3", \\200,  ~vsti1_Bus);
~vst2 = ~loadVST.value(\\vsti2, "E:/vst/Vital.vst3", \\300, ~vsti2_Bus);
~vst3 = ~loadVST.value(\\vsti3, "E:/vst/Vital.vst3", \\400, ~vsti3_Bus);
~vst4 = ~loadVST.value(\\vsti4, "E:/vst/Vital.vst3", \\500,  ~vsti4_Bus);
~vst5 = ~loadVST.value(\\vsti5, "E:/vst/Vital.vst3", \\600,  ~vsti5_Bus);
)""")

V.info=" vst |||||||||| 70%"
write_to_shared_memory(V.info)

print("step4 vst s")  
time.sleep(7)


#loading the vst effect  weirdly i need to run them 2 time to be sure
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\130, ~ottBus , 0 );)""") #ott
SC("""(~vstEffectbreak= ~loadVSTeffect.value(\\shaperbox, "E:/vst/ShaperBox 3.vst3", \\136,  ~effectBus1break   ,~vitalBus  );)""") #ott

SC("""(~vstEffect1 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\13, ~vsti1_Bus   , 0 );)""") #ott
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\14, ~vsti2_Bus   , 0 );)""") #ott
SC("""(~vstEffect3 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\15, ~vsti3_Bus   , 0 );)""") #ott
SC("""(~vstEffect4 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\16, ~vsti4_Bus   , 0 );)""") #ott
SC("""(~vstEffect5 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\17, ~vsti5_Bus   , 0 );)""") #ott


 

#loading the vsti effect  weirdly i need to run them 2 time to be su
SC("""(
~vst1 = ~loadVST.value(\\vsti1, "E:/vst/Vital.vst3", \\200,  ~vsti1_Bus);
~vst2 = ~loadVST.value(\\vsti2, "E:/vst/Vital.vst3", \\300, ~vsti2_Bus);
~vst3 = ~loadVST.value(\\vsti3, "E:/vst/Vital.vst3", \\400, ~vsti3_Bus);
~vst4 = ~loadVST.value(\\vsti4, "E:/vst/Vital.vst3", \\500,  ~vsti4_Bus);
~vst5 = ~loadVST.value(\\vsti5, "E:/vst/Vital.vst3", \\600,  ~vsti5_Bus);
)""")


SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\130, ~ottBus , 0 );)""") #ott
SC("""(~vstEffectbreak= ~loadVSTeffect.value(\\shaperbox, "E:/vst/ShaperBox 3.vst3", \\136,  ~effectBus1break   ,~vitalBus  );)""") #ott

SC("""(~vstEffect1 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\13, ~vsti1_Bus   , 0 );)""") #ott
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\14, ~vsti2_Bus   , 0 );)""") #ott
SC("""(~vstEffect3 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\15, ~vsti3_Bus   , 0 );)""") #ott
SC("""(~vstEffect4 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\16, ~vsti4_Bus   , 0 );)""") #ott
SC("""(~vstEffect5 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\17, ~vsti5_Bus   , 0 );)""") #ott

 
#loading the vsti effect  weirdly i need to run them 2 time to be su
# SC("""(
#   Routine({
#     loop {
#         ~vst1.set(462, rrand(0.0, 1.0)); 
#         0.1.wait; 
#     }
# }).play;
# )""")

#SC("""(~vst1.info.printParameters; )""")

#loading the vsti effect  weirdly i need to run them 2 time to be su
SC("""(
~vst1 = ~loadVST.value(\\vsti1, "E:/vst/Vital.vst3", \\200,  ~vsti1_Bus);
~vst2 = ~loadVST.value(\\vsti2, "E:/vst/Vital.vst3", \\300, ~vsti2_Bus);
~vst3 = ~loadVST.value(\\vsti3, "E:/vst/Vital.vst3", \\400, ~vsti3_Bus);
~vst4 = ~loadVST.value(\\vsti4, "E:/vst/Vital.vst3", \\500,  ~vsti4_Bus);
~vst5 = ~loadVST.value(\\vsti5, "E:/vst/Vital.vst3", \\600,  ~vsti5_Bus);
)""")


print("step4 presets s")  

time.sleep(12)
 

V.info=" presets |||||||||| 75%"
write_to_shared_memory(V.info)


V.compagnion = [None] * 13
V.presets=[None]*5
#compagnion is a commandeline that open on the side and can launch custome commande that lauchn sample and command like intro switch etc      
V.start1=0
V.end1=1
V.start2=0
V.end2=1
V.cmd8=0
V.cmd7=0
V.cmd10=0
V.compagnion[10] = ' .  ' 
V.compagnion[9] =' .  ' 
V.compagnion[8] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion[7] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion[5] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion[6] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion[4] = ' .' # fx ?  
V.compagnion[3] = ' .' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
V.compagnion[2] = ' . ' #[F#1!2 F0 ]  .!7      [F#1!2 . F0 . ] . F0!8 .  . .!17 . [F#!4 . F2] . .!8  2
V.compagnion[1] = ' . ' #[C0]!2    .!16 
V.compagnion[0] = " X... O... .. X. O..."
V.compagnion[11] = "." 
techno=[" X.O. X..O X. X. X.O."," X..X X..X X. X. X..X"," X . O X .  X XXX "," X...O..X .. X. O..."," X...O..O .X X. O .X."," X...O... ..O. X.O."," X...O... .X X. O .X."," X.X.X.X. XX X. X .X."," X . X . O . XX ","X . X . O .  .  .  . XXHO .  .  ."] 
dnb=[" X... O... .. X. O..."," X... O..O .. X. O..."," X... O..O .. X. OO.."," X...O..X .. X. O..."," X...O..O .X X. O .X."," X...O... ..O. X.O."," X...O... .X X. O .X."," X.X.X.X. XX X. X .X."," X . X . O . XX ","X . X . O .  .  .  . XXHO .  .  ."] 
dnb2=["..H. ..H.  H.H. ..H.","..    H . . .  H ."," H..H..... H. .. .H.."," ........ .. .. . .H."," H.H.H.H. H. H. H .H."]
dnb3=["..|. ..|. ..|. ..|. "," H..H..... H. .. .H.."," ........ .. .. . .H."," H.H.H.H. H. H. H .H."]
scramblepat=["[12 12 16 70 70 80 10 10 50!!8]"]
saveb = [None] * 12  # Creates a list with 12 None elements
saveb[0]= V.compagnion[10]  
saveb[1]=V.compagnion[9] 
saveb[2]= V.compagnion[8]  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
saveb[3]=  V.compagnion[7]  # melodyfx ?   F0 . .! 14 .  .  .  
saveb[4]= V.compagnion[5]  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
saveb[5]= V.compagnion[6]  # melodyfx ?   F0 . .! 14 .  .  .  
saveb[6]= V.compagnion[4]  # fx ?  
saveb[7]= V.compagnion[3]  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
saveb[8]= V.compagnion[2] 
saveb[9]= V.compagnion[1]  #'[C0]!2    .!16' 
saveb[10]= V.compagnion[0]   
saveb[11]= V.compagnion[11]
savea = [None] * 12  # Creates a list with 12 None elements
savea[0]= V.compagnion[10]  
savea[1]=V.compagnion[9] 
savea[2]= V.compagnion[8]  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
savea[3]=  V.compagnion[7]  # melodyfx ?   F0 . .! 14 .  .  .  
savea[4]= V.compagnion[5]  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
savea[5]= V.compagnion[6]  # melodyfx ?   F0 . .! 14 .  .  .  
savea[6]= V.compagnion[4]  # fx ?  
savea[7]= V.compagnion[3]  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
savea[8]= V.compagnion[2] 
savea[9]= V.compagnion[1]  #'[C0]!2    .!16' 
savea[10]= V.compagnion[0]   
savea[11]= V.compagnion[11]
pattern_array = [
    "X... O... .. X. O...",
    "O... X... .. O. X...",
    "X... O... .. X. O..."
]
V.scramble="[16 10 70 20 40 30 35!7 ]"

V.D=[1,1,1,8,1,1,1,1,1,1,1,1,1] #durée des notes
V.S=[1,4,4,8,1,1,1,1,1,1,1,1,1]
V.userinput="" 

PisteA=[None]*13
PisteB=[None]*13
V.face='A'

V.presets_SA = {
    "a": ["", "", "", "", ""],
    "b": ["", "", "", "", ""],
    "c": ["", "", "", "", ""],
    "d": ["", "", "", "", ""],
    "e": ["", "", "", "", ""],
    "f": ["", "", "", "", ""],
    "g": ["", "", "", "", ""],
    "h": ["", "", "", "", ""],
    "i": ["", "", "", "", ""]
}

V.presets_SB = {
    "a": ["", "", "", "", ""],
    "b": ["", "", "", "", ""],
    "c": ["", "", "", "", ""],
    "d": ["", "", "", "", ""],
    "e": ["", "", "", "", ""],
    "f": ["", "", "", "", ""],
    "g": ["", "", "", "", ""],
    "h": ["", "", "", "", ""],
    "i": ["", "", "", "", ""]
}
V.state='x'

def pres(face='A',p=0,t=""):
    if V.face=='A':  V.presets_SA[V.state ][p]=t
    if V.face=='B':  V.presets_SB[V.state ][p]=t
    print(V.presets_SB,V.presets_SA)

print("step variables 2")  
time.sleep(5)

print(V.state) 
 
V.instrument=0

stop_flag = threading.Event()
def input_thread( ):
    while not stop_flag.is_set():
        time.sleep(.5)  
        user_input=V.userinput
        compagnion =deepcopy(V.compagnion)
        if user_input=="" :
            continue
            return
        match user_input :
         case "FaceA": V.face='A'
         case "FaceB": V.face='B'     
         case "pause":
            V.instrument= 2222 ;
         case "kit":
            aa=" stjakick:10 " 
            bb=" stjasnares:10"
            cc=" hats: 4"   
         case "clear":
             aa=" stjakick:16 " 
             bb=" stjasnares:13"
             cc=" hats: 1"
             V.scramble="[16 10 70 20 40 30 35!7 ]"
             V.compagnion[10] = ' .  ' 
             V.compagnion[9] = ' . '
             V.compagnion[8] = '  . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion[7] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion[5] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion[6] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion[4] = ' . ' # fx ?  
             V.compagnion[3] = ' . ' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
             V.compagnion[2] = ' . '
             V.compagnion[1] = ' . '#'[C0]!2    .!16' 
             V.compagnion[0] = " . "  
             V.compagnion[11] = ". "      
             V.start1=0
             V.end1=1
             V.start2=0   
             V.end2=1
         case "start":
             V.compagnion[8] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion[7] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion[5] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion[6] = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion[4] = ' . ' # fx ?  
             V.compagnion[3] = ' . ' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
             V.compagnion[2] = '[F#1!2 F0 ]  .!7       [F#1!2 . F0 . ] . F0!8 .  . .!17 . [F#!4 . F2] . .!8  '
             V.compagnion[1] = '. '#'[C0]!2    .!16' 
             V.compagnion[0] = " . "  
             V.compagnion[11] = " . "    
         case "melo":
            V.compagnion[8] =  " F0 . .!14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  " 
            V.compagnion[7] =  " F0 . .!14 .  .  . "   
         case "cmdx":  V.instrument=-1; #drum                  
         case "cmd0":  V.instrument=0  ; #drum
         case "cmd1":  V.instrument=1  ; #bass
         case "cmd2":  V.instrument=2  ; #pad"
         case "cmd3":  V.instrument=3  ; #lead
         case "cmd4":  V.instrument=4  ; #sythn
         case "cmd5":  V.instrument=5  ; #sythn melody
         case "cmd6":  V.instrument=6  ; #sythn melody
         case "cmd7": 
            V.instrument=7  ; 
            V.cmd7=0 #voix
            V.start1=0
            V.end1=1
         case "cmd8":
            V.instrument=8  ; 
            V.cmd8=0 #voix
            V.start=0
            V.end2=1  
         case "cmd9":  V.instrument=9  ; #rise R 
         case "cmd10":  V.instrument=10  ; #bass 
         case "scramble":V.instrument=400
         #
         case "cmd7break":  
                V.cmd7=1 
                print( "cmd7break",V.cmd7)
                V.instrument=7  ; #voix
         case "cmd8break":
                V.cmd8=1  
                V.instrument=8  ; #impact
                V.start2=V.end2
         #
         case "cmd1_1":pres(V.face,0,"cmd1_1"); V.instrument=1 ;SC("""~vst1.readProgram("preset/vital_bass_1.fxp");""")  ; #sythn
         case "cmd1_2":pres(V.face,0,"cmd1_2"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass1.fxp");""")  ; #sythn
         case "cmd1_3":pres(V.face,0,"cmd1_3"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass2.fxp");""")  ; #sythn
         case "cmd1_4":pres(V.face,0,"cmd1_4"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass3.fxp");""")  ; #sythn
         case "cmd1_5":pres(V.face,0,"cmd1_5"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass4.fxp");""")  ; #sythn
         case "cmd1_6":pres(V.face,0,"cmd1_6"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass5.fxp");""")  ; #sythn
         case "cmd1_7":pres(V.face,0,"cmd1_7"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass6.fxp");""")  ; #sythn
         case "cmd1_8":pres(V.face,0,"cmd1_8"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass7.fxp");""")  ; #sythn
         case "cmd1_9":pres(V.face,0,"cmd1_9"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass8.fxp");""")  ; #sythn
         case "cmd1_10":pres(V.face,0,"cmd1_10"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass9.fxp");""")  ; #sythn
         case "cmd1_11":pres(V.face,0,"cmd1_11"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass10.fxp");""")  ; #sythn
         case "cmd1_12":pres(V.face,0,"cmd1_12"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass11.fxp");""")  ; #sythn
         case "cmd1_13":pres(V.face,0,"cmd1_13"); V.instrument=1 ;SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vst1_bass12.fxp");""")  ; #sythn
#
         case "cmd2_1":pres(V.face,1,"cmd2_1"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vital2_reese_track1.fxp");""") #interesting track1
         case "cmd2_2":pres(V.face,1,"cmd2_2"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead.fxp");""")  ; #sythn
         case "cmd2_3":pres(V.face,1,"cmd2_3"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead3.fxp");""")  ; #sythn
         case "cmd2_4":pres(V.face,1,"cmd2_4"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead4.fxp");""")  ; #sythn
         case "cmd2_5":pres(V.face,1,"cmd2_5"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead5.fxp");""")  ; #sythn
         case "cmd2_6":pres(V.face,1,"cmd2_6"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead6.fxp");""")  ; #sythn
         case "cmd2_7":pres(V.face,1,"cmd2_7"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_lead7.fxp");""")  ; #sythn
         case "cmd2_8":pres(V.face,1,"cmd2_8"); V.instrument=2 ;SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vst2_padbest.fxp");""")  ; 
#
         case "cmd3_0":pres(V.face,2,"cmd3_0");  SC("""~vst3.readProgram("C:/Users/jo/Documents/Vital/vital3_roller_track1.fxp");""") #interesting track1
         case "cmd3_1":pres(V.face,2,"cmd3_1");  SC("""~vst3.readProgram("C:/Users/jo/Documents/Vital/vst3_fx.fxp");""")  ; 
         case "cmd3_2":pres(V.face,2,"cmd3_2");  SC("""~vst3.readProgram("C:/Users/jo/Documents/Vital/vst3_fx1.fxp");""")  ; 
#
         case "cmd4":  V.instrument=4  ; #sythn key
         case "cmd4_1":pres(V.face,3,"cmd4_1"); V.instrument=4  ;SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead.fxp");""")  ; #sythn
         case "cmd4_2":pres(V.face,3,"cmd4_2"); V.instrument=4  ;SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead2.fxp");""")  ; #sythn
         case "cmd4_3":pres(V.face,3,"cmd4_3"); V.instrument=4  ;SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead3.fxp");""")  ; #sythn
         case "cmd4_4":pres(V.face,3,"cmd4_4"); V.instrument=4  ;SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead4.fxp");""")  ; #sythn star unicorn
         case "cmd4_5":pres(V.face,3,"cmd4_5"); V.instrument=4  ; SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead5.fxp");""")  ; #sythn
         case "cmd4_6":pres(V.face,3,"cmd4_6"); V.instrument=4  ;SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vst4_lead6.fxp");""")  ; #sythn
#
         case "cmd5_2":pres(V.face,4,"cmd5_2"); V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo3.fxp");""")  ; #sythn
         case "cmd5_3":pres(V.face,4,"cmd5_3");V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo2.fxp");""")  ; #sythn ****   
         case "cmd5_4":pres(V.face,4,"cmd5_4"); V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo1.fxp");""")  ; #sythn **
         case "cmd5_5":pres(V.face,4,"cmd5_5"); V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo4.fxp");""")  ; #sythn
         case "cmd5_6":pres(V.face,4,"cmd5_6"); V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo5.fxp");""")  ; #sythn
         case "cmd5_7":pres(V.face,4,"cmd5_7"); V.instrument=5  ;SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vst2_melo6.fxp");""")  ; #sythn
         case "cmd6": V.instrument=6  ; #sythn melody
         #
         case "cmd1_e":  SC('~vst1.editor')
         case "cmd2_e":  SC('~vst2.editor') ; #sythn"
         case "cmd3_e":  SC('~vst3.editor') ; #sythn
         case "cmd4_e":  SC('~vst4.editor'); #sythn
         case "cmd5_e":  SC('~vst5.editor'); #sythn melody
         case "cmd6_e":  SC('~vst5.editor'); #sythn melody 
#   
         case "cmd1_i":  SC("""(~vst1.info.printParameters; )""")
         case "cmd2_i":  SC("""(~vst2.info.printParameters; )""")
         case "cmd3_i":  SC("""(~vst3.info.printParameters; )""")
         case "cmd4_i":  SC("""(~vst4.info.printParameters; )""")
         case "cmd5_i":  SC("""(~vst5.info.printParameters; )""")
         case "cmd6_i":  SC("""(~vst5.info.printParameters; )""")
         #case "cmdb":   SC('~vst2.editor'); #bass 
         #
         case "intro":  V.state='a'   ;
         case "buildup":  V.state='b'  ;
         case "dropa":  V.state='c'  ;
         case "dropb":  V.state='d'  ;
         case "outro":  V.state='e'  ;
         case "switch":  V.state='f'  ;
         case "transition":  V.state='g'  ;
         case "break":  V.state='i'  ;
         case "full":  V.state='h'  ;
         #
         case "intro_S": 
            if V.face=='A': PisteA[0] = compagnion
            if V.face=='B': PisteB[0] = compagnion
         case "buildup_S":
            if V.face=='A':    PisteA[1] = compagnion
            if V.face=='B':    PisteB[1] = compagnion
         case "dropa_S":
            if V.face=='A':        PisteA[2] = compagnion
            if V.face=='B':    PisteB[2] = compagnion
         case "dropb_S":
            if V.face=='A':    PisteA[3] = compagnion
            if V.face=='B':    PisteB[3] = compagnion
         case "outro_S":
            if V.face=='A':   PisteA[4] = compagnion
            if V.face=='B':    PisteB[4] = compagnion
         case "switch_S":  
            if V.face=='A':    PisteA[5] = compagnion
            if V.face=='B':    PisteB[5] = compagnion
         case "transition_S":
            if V.face=='A':    PisteA[6] = compagnion
            if V.face=='B':    PisteB[6] = compagnion
         case "break_S":
            if V.face=='A':    PisteA[7] = compagnion
            if V.face=='B':    PisteB[7] = compagnion
         case "full_S":  
            if V.face=='A':    PisteA[8] = compagnion
            if V.face=='B':    PisteB[8] = compagnion
         #
         case "intro_L":  
            if V.face=='A':        V.compagnion = PisteA[0];V.state='a'   ;
            if V.face=='B':        V.compagnion = PisteB[0]; V.state='a'   ;
         case "buildup_L":
            if V.face=='A':        V.compagnion = PisteA[1]; V.state='b'   ;
            if V.face=='B':        V.compagnion = PisteB[1]; V.state='b'   ;
         case "dropa_L":
            if V.face=='A':        V.compagnion = PisteA[2]; V.state='c'   ;
            if V.face=='B':        V.compagnion = PisteB[2]; V.state='c'   ;
         case "dropb_L":
            if V.face=='A':        V.compagnion = PisteA[3]; V.state='d'   ;
            if V.face=='B':        V.compagnion = PisteB[3]; V.state='d'   ;
         case "outro_L":
            if V.face=='A':        V.compagnion = PisteA[4]; V.state='e'   ;
            if V.face=='B':        V.compagnion = PisteB[4]; V.state='e'   ;
         case "switch_L":  
            if V.face=='A':        V.compagnion = PisteA[5]; V.state='f'   ;
            if V.face=='B':        V.compagnion = PisteB[5]; V.state='f'   ;
         case "transition_L":
            if V.face=='A':        V.compagnion = PisteA[6]; V.state='g'   ;
            if V.face=='B':        V.compagnion = PisteB[6]; V.state='g'   ;
         case "break_L":
            if V.face=='A':        V.compagnion = PisteA[7]; V.state='h'   ;
            if V.face=='B':        V.compagnion = PisteB[7]; V.state='h'   ;
         case "full_L":  
            if V.face=='A':        V.compagnion = PisteA[8]; V.state='i'   ;
            if V.face=='A':        V.compagnion = PisteB[8]; V.state='i'   ;
         case "dnb":  V.instrument=100  ;
         case "techno":  V.instrument=200  ;
         case'help':  window.print(open('C:/Users/jo/Krease/30 minu/help_rdm', 'r').read())
         case "scope":SC.freqscope()
         case "1sav":
            print("save")  

         case  "savec":  V.instrument=300  ;
         case "loada":
            V.compagnion[10]   = savea[0]
            V.compagnion[9]  = savea[0]
            V.compagnion[8]   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            V.compagnion[7]   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  
            V.compagnion[5]   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            V.compagnion[6]   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  
            V.compagnion[4]   = savea[0]# fx ?  
            V.compagnion[3] = savea[0]  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
            V.compagnion[2]  = savea[0]
            V.compagnion[1]   = savea[0]#'[C0]!2    .!16' 
            V.compagnion[0]   = savea[0] 
            V.compagnion[11] = savea[0]                           
         case "loadb":  V.instrument=300  ;
         case "save":  
            track1= [ PisteA , PisteB ]
            save_pattern(PisteA, f"my_patternx.pat")
            print("saved")
         case "panic": eval(panic())    
         case "spreset":   V.instrument =500
         case "lpreset":   V.instrument =600
         case "hpreset":  print(os.listdir("preset/"))
         case "lenNote":   V.instrument =700
        if V.instrument == 100:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " 1234567890 ~" for char in user_input):
                        V.compagnion[0] = dnb[P(user_input)]
                    print( "dnb xxxz ", V.compagnion, V.instrument )
        if V.instrument == 200:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " 1234567890 ~" for char in user_input):
                        V.compagnion[0] = techno[P(user_input)]
                    print( "techno xxxz ", V.compagnion, V.instrument )   
        if V.instrument == 300:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " 1234567890 ~" for char in user_input):
                        V.scramble = scramblepat[P(user_input)]
                    print( "scramble >>> ", V.scramble, V.instrument )                              
        if V.instrument == 0:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """ G Q X.OoxhH K  dnb techno  | + - * / : [] V VV I 1234567890""" for char in user_input):
                        V.compagnion[0] = " "+f""+user_input+" "
                    print( "drums xxxz ", V.compagnion, V.instrument )
        if V.instrument == -1:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """K Q g H X.OoxhH { } dnb techno | + - * / : [] V V II 1234567890""" for char in user_input):
                        V.compagnion[11] = " "+f""+user_input+" "
                    print( "drums xxxz ", V.compagnion[11], V.instrument )            
        if V.instrument == 1:
            match user_input:
                case _:
                    #user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in "augMaj7 maj7^ mM9 dim seven  six min7 sus4 + -  / * iv IV CDEFGA @ 0123456789 []! . }{" for char in user_input):
                        V.compagnion[1] = f" "+user_input+" "
                    print( "bass xx ", V.compagnion[1] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 2:
            match user_input:
                case _:
                    #user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - /   *augMaj7 maj7^ mM9 dim seven  six min7 sus4   dnb CDEFGAB @ 0123456789 []! . }{""" for char in user_input):
                        V.compagnion[2] = " "+user_input+" "
                    print( "reese x ", V.compagnion[2] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 3:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[3] = " "+user_input+" "
                    print( "FX ", V.compagnion[3] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 4:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[4] = " "+user_input+" "
                    print( "Bass2 ", V.compagnion[4] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 5:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[5] = " "+user_input+" "
                    print( "x melo", V.compagnion[5] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 6:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[6] = " "+user_input+" "
                    print( "x melo", V.compagnion[6] , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 7:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB P : w T V W U I 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[7] = " "+user_input+" "
                    print( "voix ", V.compagnion[7] , V.instrument , all(char in " + - / * # CDEFGAB P : w V U I 0123456789 []! . {}" for char in user_input))
        if V.instrument == 8:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # QCDEFGAB P p u  w T v W U : V I X O 0123456789 []! . {}""" for char in user_input):
                        V.compagnion[8] = " "+user_input+" "
                    print( "yy ", V.compagnion[8] , V.instrument , all(char in "+ - / * # CDEFGAB P : w V U I 0123456789 []! . {}" for char in user_input))
        if V.instrument == 9:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots  stab rise  
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * #Q CDEFGAB R Y W X C S KBPS  U G Y T  P S : V I X O 0123456789 []! . {}""" for char in user_input):
                       V.compagnion[9] = " "+user_input+" "
                    print( "impact ",V.compagnion[9] , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))
        if V.instrument == 10:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots  stab rise  
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * #Q CDEFGAB R Y W X  , C S KBPS  U G Y T  P S : V I X O 0123456789 [] ! . {}""" for char in user_input):
                        V.compagnionb = " "+user_input+" "
                    print( "drum percution ", V.compagnion[10] , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))
        if V.instrument == 400:
            match user_input:
                case _:
                    #   user_input = user_input.upper()
                    # Replace spaces with dots  stab rise  
                    if all(char in """+ - / * #Q CDEFGAB R Y W X  , C S KBPS  U G Y T  P S : V I X O 0123456789 [] ! . {}""" for char in user_input):
                        V.scramble = f"{user_input}"
                    print( "scramble ", V.scramble , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))         
        if V.instrument == 500:
            match user_input:
                case _:
                    if ',' in user_input:
                        vst = user_input.split(',')
                    #   user_input = user_input.upper()
                        SC(f"""~{vst[0]}.writeProgram("preset/{vst[1]}.fxp");""")  ; #sythn
                    print( "savepreset ", V.scramble , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))         
        if V.instrument == 600:
            match user_input:
                case _:
                    if ',' in user_input:
                        vst = user_input.split(',')
                    #   user_input = user_input.upper()
                        SC(f"""~{vst[0]}.readProgram("preset/{vst[1]}.fxp");""")  ; #sythn
                    print( "loadpreset ", V.scramble , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))         
        if V.instrument == 700:
            match user_input:
                case _:
                    if ',' in user_input:
                        vl=["2","8","16"]
                        vl = user_input.split(',')
                        print(">>>",vl)
                    #   note length
                        V.D[int(vl[0])]= int(vl[1])
                        V.S[int(vl[0])]=int(vl[2])
                    print( "vst note length "  , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))         
        V.userinput=""
        time.sleep(2.5)     
          

print( V.compagnion, V.instrument, V.state ,"<<")

V.info="step companion init vst |||||||||| 80%"
write_to_shared_memory(V.info)
print("step companion init ")  
time.sleep(5)



#connecting the sardine midi  to the vsti 
SC("""(~dirt.soundLibrary.addMIDI(\\vsti1, ~vst1.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti2, ~vst2.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti4, ~vst4.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti3, ~vst3.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti5, ~vst5.midi);)""") #wait

print("vst preset")

SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vital2_reese_track1.fxp");""") #interesting track1
SC("""~vst3.readProgram("C:/Users/jo/Documents/Vital/vital3_roller_track1.fxp");""") #interesting track1
SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vital1_bassnoise_track1.fxp");""") #interesting track1
SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vital3_fx_track1.fxp");""") #interesting track1
SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vital3_melo_track1.fxp");""") #interesting track1
SC("""~vstEffect1.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffectbreak.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_shapper.fxp");""")
SC("""~vstEffect2.readProgram("C:/Users/jo/Documents/Vital/ott2.fxp");""")

SC("""~vstEffect1.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffect2.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffect3.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffect4.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffect5.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")


V.info=" loaded 100% "
write_to_shared_memory(V.info)

print("loaded")  
time.sleep(5)

stop_flagw = threading.Event()
def windows_thread():
    SHARED_MEMORY_SIZE = 1024  
    oldata=""
    while True:
        shm = shared_memory.SharedMemory(name="my_memory")    
        data = bytearray(shm.buf).split(b'\0')[0].decode('utf-8')
        if  data!=oldata:
            print(f"Read from shared memory: {data}", V.compagnion[0], V.compagnion[1])
            V.userinput = data
            time.sleep(0.21)
            #V.userinput =""
        oldata=data


threading.Thread(target=windows_thread, daemon=True).start()
threading.Thread(target=input_thread, daemon=True).start()

V.presets=[None]*5


 
 
print("PisteA:", PisteA,"///",PisteB) #ok


V.gate=[1,1,1,1,1,1,1,1,1,1,1,1,1]

V.D=[1,1,1,8,1,1,1,1,1,1,1,1,1]

V.S=[1,4,4,8,1,1,1,1,1,1,1,1,1]

def pat(gate=1, compagnion=None):
    comp = compagnion
    if gate <= 0:
        comp = '.'
    return comp



pres(V.face,3,"cmd4_2");

    
# Print the results to verify
print("PisteA:", PisteA[0][0])

print("PisteB:", PisteB[0])



V.compagnion = PisteA[0]



compagnion = PisteB[0]; 



V.state='a'   ;

print(V.compagnion )

V.compagnion[10] =[ ' .  ' ]

V.compagnion[9] =' .  ' 
V.compagnion[8] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion[7] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion[5] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion[6] = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion[4] = ' .' # fx ?  
V.compagnion[3] = ' .' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
V.compagnion[2] = ' . ' #[F#1!2 F0 ]  .!7      [F#1!2 . F0 . ] . F0!8 .  . .!17 . [F#!4 . F2] . .!8  2
V.compagnion[1] = ' . ' #[C0]!2    .!16 
V.compagnion[0] = " X... O... .. X. O..."
V.compagnion[11] = "." 


@swim
def fun(p=1,i=0): 
    D(  r_patterns( pat(V.gate[0] ,V.compagnion[0] )  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i) 
    D(r_patterns(   pat(V.gate[1] ,V.compagnion[11] ) )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    D(f'vsti1  : [ {pat(V.gate[2] ,V.compagnion[1]) }  ] ',oct=("1"),vel=127 ,dur= V.D[2] , i=i/V.S[2]) #base32 / 3 \working 1 0!2  -1!4 
    D(f'vsti2  : [ { pat(V.gate[3],V.compagnion[2]) } ] ',oct=("0"),vel=127 ,dur= V.D[3] , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti5  : [ { pat(V.gate[6], V.compagnion[5]) } ] ',oct=("0"),vel=7,gain=.51,amp=0.2 ,dur= 2 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti5  : [ {pat(V.gate[7] , V.compagnion[6]) } ] ',oct=("0"),vel=70,gain=1,amp=0.2 ,dur= V.D[7], i=i/2) #base32 / 3 \working 1 0!2  -1!4
    D(f'vsti3  : [ { pat(V.gate[4], V.compagnion[3]) } ] ',oct=("0"),vel=27 ,dur= 3.2 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
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
    def rise2():D(r_patterns(pat(V.gate[10] ,V.compagnion[9])  ) ,speed=1,amp=.815,oct=P("4"),vel=127,i=i/4,d=V.ssp,dur=2)
    def impact():D(r_patterns(pat(V.gate[9] , V.compagnion[8] )) ,begin=V.start2, end=V.end2+0.012, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def voix():D(r_patterns( pat(V.gate[8] ,V.compagnion[7] )),legato=8,	oct=5 ,begin=V.start1, end=V.end1+0.012,gain=1, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i/2)    
    def percution():D(r_patterns(pat(V.gate[11] , V.compagnion[10] )) ,begin=V.start3, end=V.end3+0.012, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    D(f'vsti4  : [ { pat(V.gate[5] ,V.compagnion[4] )} ] ',oct=("0"),vel=7 ,dur= 4 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    rise2(),voix(),impact()
    match V.state :
        case 'a':V.gate=[0,0,1,1,1,0,0,0,0,0,0];  w( '7', '8~2','.', '2');V.orbdrum=1#intro
        case 'b':V.gate=[1,1,1,1,1,0,0,0,0,0,0];  w( '4~13', 16,'.', '6'); V.orbdrum=2 #buildup
        case 'c':V.gate=[1,0,1,1,0,1,1,0,0,1,1];  pass #w( '4~13', 16,'.', '6');#dropa
        case 'd':V.gate=[1,0,0,0,0,1,1,0,0,1,1];  w( '9~19', 17,'.', '6');V.orbdrum=3#dropb
        case 'e':V.gate=[0,0,1,1,1,1,1,1,1,1,1]; # V.orbdrum=2w( '4~13', 16,'.', '6');#outro
        case 'f':V.gate=[1,1,1,0,0,1,1,1,1,1,1];  w( '4~13', 12,'.', '6'); V.orbdrum=1 #switch
        case 'g':V.gate=[0,0,0,1,1,1,1,1,1,1,1];  w( '16~19', 17,'.', '6'); #transition
        case 'h':V.gate=[1,1,1,1,1,1,1,1,1,1,1];  w( '8~20', 1,'8', '6'); V.orbdrum=1 #switc #full
        case 'i':V.gate=[0,0,0,0,0,1,1,0,1,1,1];  pass#w( '4~13', 16,'.', '6');#break                                                                                           
        case "◈":  V.tb=1;   fill(); 
    again(fun1, p=1/16,i=i+1)



@swim(snap=0.5)
def dnb_track(p=1,i=0,):
    one('dirt/play1',values="ee")
    again(dnb_track,p=1/16,i=i+1)
    
panic()
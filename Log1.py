#todo add bass and melody
#reduce 12 code évaluation
from window_terminal import WindowTerminal
import threading
SC.info()
trackname= "dnb"
clock.tempo=175
#We open bus and direct orbit where we want. On this exemple  one orbit go to one effect and is output on the main output
#Bus and vst effect is powerfull to mix and regulate every sound/ also a good way to build ear candy but it can be cpu intensive.
SC("""(
~effectBus1 = Bus.audio(s, 2);   
~effectBus2 = Bus.audio(s, 2); 
~effectBus3 = Bus.audio(s, 2); 
~vitalBus = Bus.audio(s, 2); 
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
ee=" percusion:8 "
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
nn="cimpact"
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
V.compagnion = "x.0."
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

Pg * d( r_patterns( V.compagnion8  )   ,orbit=3,amp=0.15,oct=P("6"),snap=10.5,vel=127,p="4",d=2,dur=1)

Pg * d( [aa,": 2 "]   ,amp=0.15,oct=P("0"),snap=10.5,vel=127,p="4",d=2,dur=1)

panic()
  


def pg(n=1):
    if(n==0) :return 1
    if(n>0): return (((1/16)/4)/4)/n 
     



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
)""")
SC("""(
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


#loading the vst effect  weirdly i need to run them 2 time to be sure
SC("""(~vstEffect2 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\130, ~ottBus , 0 );)""") #ott
SC("""(~vstEffectbreak= ~loadVSTeffect.value(\\shaperbox, "E:/vst/ShaperBox 3.vst3", \\136,  ~effectBus1break   ,~vitalBus  );)""") #ott
SC("""(~vstEffect1 = ~loadVSTeffect.value(\\ott, "E:/vst/OTT_x64.dll", \\13, ~vitalBus , 0 );)""") #ott

SC('~vstEffect2.editor')

SC('~vstEffectbreak.editor')

#loading the vsti effect  weirdly i need to run them 2 time to be su
SC("""(
~vst1 = ~loadVST.value(\\vsti1, "E:/vst/Vital.vst3", \\200,  ~vitalBus);
~vst2 = ~loadVST.value(\\vsti2, "E:/vst/Vital.vst3", \\300, ~vitalBus);
~vst3 = ~loadVST.value(\\vsti3, "E:/vst/Vital.vst3", \\400, ~vitalBus);
~vst4 = ~loadVST.value(\\vsti4, "E:/vst/Vital.vst3", \\500,  ~vitalBus);
~vst5 = ~loadVST.value(\\vsti5, "E:/vst/Vital.vst3", \\600,  ~vitalBus);
)""")

SC('~vst1.editor')

SC('~vst3.free')


#connecting the sardine midi  to the vsti 
SC("""(~dirt.soundLibrary.addMIDI(\\vsti1, ~vst1.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti2, ~vst2.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti4, ~vst4.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti3, ~vst3.midi);)""") #wait
SC("""(~dirt.soundLibrary.addMIDI(\\vsti5, ~vst5.midi);)""") #wait
##preset for vsti
SC("""~vst2.readProgram("C:/Users/jo/Documents/Vital/vital2_reese_track1.fxp");""") #interesting track1
SC("""~vst3.readProgram("C:/Users/jo/Documents/Vital/vital3_roller_track1.fxp");""") #interesting track1
SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vital1_bassnoise_track1.fxp");""") #interesting track1
SC("""~vst4.readProgram("C:/Users/jo/Documents/Vital/vital3_fx_track1.fxp");""") #interesting track1
SC("""~vst5.readProgram("C:/Users/jo/Documents/Vital/vital3_melo_track1.fxp");""") #interesting track1
SC("""~vstEffect1.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_ott.fxp");""")
SC("""~vstEffectbreak.readProgram("C:/Users/jo/Documents/Vital/vstEffect1_shapper.fxp");""")
SC("""~vst1.readProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass.fxp");""")
SC("""~vstEffect2.readProgram("C:/Users/jo/Documents/Vital/ott2.fxp");""")


SC("""~vst1.writeProgram("C:/Users/jo/Documents/Vital/vstEffect6_bass.fxp");""")

SC('~vst5.editor')




def r_patterns(pattern_string):
    mappings = {'K':vv,'X': aa, 'O': bb ,'Q': uu,'H': cc, '|': ee,'V': ss, 'W': sss, 'U': ssss ,'I': hh,'T': nn,'R': mm, 'B': oo,'P': tt, 'S': kk ,'C': ii ,'G': gg }
    result = [mappings.get(char, char) for char in pattern_string]
    return result

def save_pattern(pattern_array, filename):
    with open(filename, 'w') as file:
        for line in pattern_array:
            file.write(line + '\n')



#compagnon is a commandeline that open on the side and can launch custome commande that lauchn sample and command like intro switch etc      
V.compagnion = [' .  ']
V.compagnion10 = ' .  ' 
V.compagnion9 = ' .  ' 
V.compagnion8 = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion7 = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion5 = ' .' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
V.compagnion6 = ' .' # melodyfx ?   F0 . .! 14 .  .  .  
V.compagnion4 = ' .' # fx ?  
V.compagnion3 = ' .' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
V.compagnion2 = ' . ' #[F#1!2 F0 ]  .!7      [F#1!2 . F0 . ] . F0!8 .  . .!17 . [F#!4 . F2] . .!8  2
V.compagnion1 = ' . ' #[C0]!2    .!16 
V.compagnion = " X... O... .. X. O..." 
V.compagnionm1 = "." 
techno=[" X.O. X..O X. X. X.O."," X... O..O .. X. O..."," X... O..O .. X. OO.."," X...O..X .. X. O..."," X...O..O .X X. O .X."," X...O... ..O. X.O."," X...O... .X X. O .X."," X.X.X.X. XX X. X .X."," X . X . O . XX ","X . X . O .  .  .  . XXHO .  .  ."] 
dnb=[" X... O... .. X. O..."," X... O..O .. X. O..."," X... O..O .. X. OO.."," X...O..X .. X. O..."," X...O..O .X X. O .X."," X...O... ..O. X.O."," X...O... .X X. O .X."," X.X.X.X. XX X. X .X."," X . X . O . XX ","X . X . O .  .  .  . XXHO .  .  ."] 
dnb2=["..H. ..H.  H.H. ..H.","..    H . . .  H ."," H..H..... H. .. .H.."," ........ .. .. . .H."," H.H.H.H. H. H. H .H."]
dnb3=["..|. ..|. ..|. ..|. "," H..H..... H. .. .H.."," ........ .. .. . .H."," H.H.H.H. H. H. H .H."]
saveb[0]= V.compagnion10  
saveb[1]= V.compagnion9 
saveb[2]= V.compagnion8  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
saveb[3]=  V.compagnion7  # melodyfx ?   F0 . .! 14 .  .  .  
saveb[4]= V.compagnion5  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
saveb[5]= V.compagnion6  # melodyfx ?   F0 . .! 14 .  .  .  
saveb[6]= V.compagnion4  # fx ?  
saveb[7]= V.compagnion3  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
saveb[8]= V.compagnion2 
saveb[9]= V.compagnion1  #'[C0]!2    .!16' 
saveb[10]= V.compagnion   
saveb[11]= V.compagnionm1
pattern_array = [
    "X... O... .. X. O...",
    "O... X... .. O. X...",
    "X... O... .. X. O..."
]
V.instrument=0
V.state='x'
def input_thread():
    savea = [None] * 12  # Creates a list with 12 None elements
    savea[0]= V.compagnion10  
    savea[1]= V.compagnion9 
    savea[2]= V.compagnion8  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
    savea[3]=  V.compagnion7  # melodyfx ?   F0 . .! 14 .  .  .  
    savea[4]= V.compagnion5  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
    savea[5]= V.compagnion6  # melodyfx ?   F0 . .! 14 .  .  .  
    savea[6]= V.compagnion4  # fx ?  
    savea[7]= V.compagnion3  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
    savea[8]= V.compagnion2 
    savea[9]= V.compagnion1  #'[C0]!2    .!16' 
    savea[10]= V.compagnion   
    savea[11]= V.compagnionm1
    window = WindowTerminal.create_window()
    window.open()
    while True:
        window.print("template  : X... O... .. X. O...")
        user_input = window.input("Enter text: ")
        match user_input :
         case "clear":
             V.compagnion10 = ' .  ' 
             V.compagnion9 = ' . '
             V.compagnion8 = '  . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion7 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion5 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion6 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion4 = ' . ' # fx ?  
             V.compagnion3 = ' . ' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
             V.compagnion2 = ' . '
             V.compagnion1 = ' . '#'[C0]!2    .!16' 
             V.compagnion = " . "  
             V.compagnionm1 = ". "      
         case "start":
             V.compagnion8 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion7 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion5 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
             V.compagnion6 = ' . ' # melodyfx ?   F0 . .! 14 .  .  .  
             V.compagnion4 = ' . ' # fx ?  
             V.compagnion3 = ' . ' # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
             V.compagnion2 = '[F#1!2 F0 ]  .!7       [F#1!2 . F0 . ] . F0!8 .  . .!17 . [F#!4 . F2] . .!8  '
             V.compagnion1 = '. '#'[C0]!2    .!16' 
             V.compagnion = " . "  
             V.compagnionm1 = " . "    
         case "melo":
            V.compagnion8 =  " F0 . .!14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  " 
            V.compagnion7 =  " F0 . .!14 .  .  . "   
         case "cmdx":  V.instrument=-1; #drum                  
         case "cmd0":  V.instrument=0  ; #drum
         case "cmd1":  V.instrument=1  ; #sythn
         case "cmd2":  V.instrument=2  ; #sythn"
         case "cmd3":  V.instrument=3  ; #sythn
         case "cmd4":  V.instrument=4  ; #sythn
         case "cmd5":  V.instrument=5  ; #sythn melody
         case "cmd6":  V.instrument=6  ; #sythn melody
         case "cmd7":  V.instrument=7  ; #voix
         case "cmd8":  V.instrument=8  ; #impact
         case "cmd9":  V.instrument=9  ; #rise R 
         case "cmdb":  V.instrument=10  ; #bass 
         case "intro":  V.state='a'  ;
         case "buildup":  V.state='b'  ;
         case "dropa":  V.state='c'  ;
         case "dropb":  V.state='d'  ;
         case "outro":  V.state='e'  ;
         case "switch":  V.state='f'  ;
         case "transition":  V.state='g'  ;
         case "silence":  V.state='i'  ;
         case "dnb":  V.instrument=100  ;
         case "1sav":
            print("save")  
            savea[0]= V.compagnion10  
            savea[1]= V.compagnion9 
            # savea[2]= V.compagnion8  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            # savea[3]=  V.compagnion7  # melodyfx ?   F0 . .! 14 .  .  .  
            # savea[4]= V.compagnion5  # melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            # savea[5]= V.compagnion6  # melodyfx ?   F0 . .! 14 .  .  .  
            # savea[6]= V.compagnion4  # fx ?  
            # savea[7]= V.compagnion3  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
            # savea[8]= V.compagnion2 
            # savea[9]= V.compagnion1  #'[C0]!2    .!16' 
            # savea[10]= V.compagnion   
            # savea[11]= V.compagnionm1
         case  "saveb":  V.instrument=200  ;
         case "loada":
            V.compagnion10   = savea[0]
            V.compagnion9  = savea[0]
            V.compagnion8   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            V.compagnion7   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  
            V.compagnion5   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  . C1 .  .  . .!8  .  .  . C3 . F1 . F2 . A3 . .! .  . A4 . A4 . G4  5 
            V.compagnion6   = savea[0]# melodyfx ?   F0 . .! 14 .  .  .  
            V.compagnion4   = savea[0]# fx ?  
            V.compagnion3 = savea[0]  # Enter text: [C2 .!7][C2 .!7] .!32       #[C1 . .!8] . [C1 . .!8]+3 . [C1 . .!8]+3 . [F2 . .!4] 
            V.compagnion2  = savea[0]
            V.compagnion1   = savea[0]#'[C0]!2    .!16' 
            V.compagnion   = savea[0] 
            V.compagnionm1 = savea[0]                           
         case "loadb":  V.instrument=200  ;
         case "save":  
            save_pattern(savea, "my_pattern.pat")
            print("saved")
         case "panic": eval(panic())    
        if V.instrument == 100:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " 1234567890 ~" for char in user_input):
                        V.compagnion = dnb[P(user_input)]
                    print( "dnb xxxz ", V.compagnion, V.instrument )
        if V.instrument == 200:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " 1234567890 ~" for char in user_input):
                        V.compagnion = techno[P(user_input)]
                    print( "techno xxxz ", V.compagnion, V.instrument )                   
        if V.instrument == 0:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in " G Q X.OoxhH K{{}} dnb | + - * / : [] V VV I 1234567890" for char in user_input):
                        V.compagnion = " "+f""+user_input+" "
                    print( "drums xxxz ", V.compagnion, V.instrument )
        if V.instrument == -1:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in "K Q g H X.OoxhH {{}} dnb | + - * / : [] V V II 1234567890" for char in user_input):
                        V.compagnionm1 = " "+f""+user_input+" "
                    print( "drums xxxz ", V.compagnionm1, V.instrument )            
        if V.instrument == 1:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in f"""+ - # / * CDEFGA 0123456789 []! . {{}} """ for char in user_input):
                        V.compagnion1 = f" "+user_input+" "
                    print( "bass xx ", V.compagnion1 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 2:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / #* dnb CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion2 = " "+user_input+" "
                    print( "reese x ", V.compagnion2 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 3:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion3 = " "+user_input+" "
                    print( "rollx ", V.compagnion3 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 4:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion4 = " "+user_input+" "
                    print( "x ", V.compagnion4 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 5:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion5 = " "+user_input+" "
                    print( "x melo", V.compagnion5 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 6:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB 0123456789 []! . {}""" for char in user_input):
                        V.compagnion6 = " "+user_input+" "
                    print( "x melo", V.compagnion6 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 7:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # CDEFGAB : V U I 0123456789 []! . {}""" for char in user_input):
                        V.compagnion7 = " "+user_input+" "
                    print( "y ", V.compagnion7 , V.instrument , all(char in " . CDEFGA 1234560789 []!" for char in user_input))
        if V.instrument == 8:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * # QCDEFGAB : V I X O 0123456789 []! . {}""" for char in user_input):
                        V.compagnion8 = " "+user_input+" "
                    print( "yy ", V.compagnion8 , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))
        if V.instrument == 9:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots  stab rise  
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * #Q CDEFGAB R Y W X C S KBPS  U G Y T  P S : V I X O 0123456789 []! . {}""" for char in user_input):
                        V.compagnion9 = " "+user_input+" "
                    print( "yy ", V.compagnion9 , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))
        if V.instrument == 10:
            match user_input:
                case _:
                    user_input = user_input.upper()
                    # Replace spaces with dots  stab rise  
                    user_input= user_input.replace(" ", " . ")
                    if all(char in """+ - / * #Q CDEFGAB R Y W X  , C S KBPS  U G Y T  P S : V I X O 0123456789 [] ! . {}""" for char in user_input):
                        V.compagnion10 = " "+user_input+" "
                    print( "bass ", V.compagnion10 , V.instrument , all(char in " . CDEFGA : V I X O 1234560789 []!" for char in user_input))
    
    print(  V.instrument, V.state ,"<<")

threading.Thread(target=input_thread, daemon=True).start()

V.orbdrum=0
V.tb=4
V.ssp=4
@swim(snap=0.5)
def Thecompagnion(p=1,i=0,):
    orbdrum=V.orbdrum
    def x():D(r_patterns( V.compagnion  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i) 
    def xx():D(r_patterns( V.compagnionm1  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def bassb(n = V.instrument) :  D(f'vsti6  :  [{ V.compagnion10 } ]',oct=("0"),vel=107 ,dur= 2 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    #def x():D(r_patterns( V.compagnion  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i) 
    def bass(n = V.instrument) : 
        if (n==1) :
            D(f'vsti1  : [ { V.compagnion1 } ] ',oct=("0"),vel=127 ,dur= 8 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    def reese(n = V.instrument) : 
        if (n==1) :
            D(f'vsti2  : [ { V.compagnion2 } ] ',oct=("0"),vel=127 ,dur= 8 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    def roller(n = V.instrument) : 
        if (n==1) :
            D(f'vsti3  : [ { V.compagnion3 } ] ',oct=("0"),vel=27 ,dur= 3.2 , i=i/7) #base32 / 3 \working 1 0!2  -1!4
    def fx(n = V.instrument) : 
        if (n==1) :
            D(f'vsti4  : [ { V.compagnion4 } ] ',oct=("0"),vel=27 ,dur= 3.2 , i=i/4) #base32 / 3 \working 1 0!2  -1!4
    def melo(n = V.instrument) : 
        if (n==1) :
            D(f'vsti5  : [ { V.compagnion5 } ] ',oct=("0"),vel=7,gain=.51,amp=0.2 ,dur= 2 , i=i/8) #base32 / 3 \working 1 0!2  -1!4
    def melo1(n = V.instrument) : 
        if (n==1) :
            D(f'vsti5  : [ { V.compagnion6 } ] ',oct=("0"),vel=70,gain=1,amp=0.2 ,dur= 1 , i=i/2) #base32 / 3 \working 1 0!2  -1!4
    def rise2():D(r_patterns( V.compagnion9  ) ,   speed=1,amp=.815,oct=P("4"),vel=127,i=i/4,d=V.ssp,dur=2)
    def impact():D(r_patterns( V.compagnion7  )  , orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def voix():D(r_patterns( V.compagnion8  )  , oct=4 ,gain=0.82, orbit=orbdrum,d=V.ssp, speed=1, room=0.01, dry=1, i=i)     
    def w(n=3, nn=4, nnn='.', nnnn=5):
         return {
        D([ff, f":{n} .  "], d=1, vel=1, speed='1  ',amp=0.2, gain=0.771, rate=1, cutoff=4000, hcutoff=210,orbit=orbdrum , room=0.0, dry=0, snap=0, size=0, i=i/64),
        D([ff, f":{nn} ."], d=1, vel=1, speed='1  ', gain=0.871, rate=1,cutoff=2800, hcutoff=505,orbit=orbdrum , room=0.0, dry=10,snap=0, size=0, i=i/64),
        D([fff, f":{nnn} .!8"],d=1, vel=1, speed='1  ', gain=0.971, rate=2,cutoff=4800, hcutoff=100, orbit=orbdrum ,room=0.0, dry=0,snap=0, size=0, i=i/16),
        D([ffff, f":{nnnn} .!2"],   d=1, vel=1, speed='1.25', gain=0.771, rate=1,cutoff=9800, hcutoff=1200, orbit=orbdrum ,room=0.0, dry=0,snap=0.6, size=0, i=i/16)
    }
    def fill():D( r_patterns(dnb2[4]),d=V.ssp, speed='1  ', orbit=orbdrum ,room=0.3,gain=0.85, dry=0.2, size=0.5, i=i) 
    def fill2():{
        D( r_patterns(dnb2[0]),d=V.ssp, speed='1  ', room=0.3,gain=0.85, dry=0.2, size=0.5, i=i),
        D( r_patterns(dnb[7]),d=V.ssp, speed='1  ', room=0.3,gain=0.85, dry=0.2, size=0.5, i=i)
         }
   # x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1), 
    rise2()
    #V.state='d'                                                                                          
    match V.state :
        case 'a': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);voix();impact();bassb(); w( '7', '8~2','.', '2');V.orbdrum=2#intro
        case 'b': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);voix();w( '4~13', 16,'.', '6');bassb(); V.orbdrum=2 #buildup
        case 'c': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);voix();impact();bassb();#w( '4~13', 16,'.', '6');#dropa
        case 'd': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);impact(),w( '9~19', 17,'.', '6');V.orbdrum=3#dropb
        case 'e': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);voix();bassb();V.orbdrum=2#w( '4~13', 16,'.', '6');#outro
        case 'f': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);impact();w( '4~13', 12,'.', '6');bassb();V.orbdrum=1 #switch
        case 'g': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);bassb();#w( '4~13', 16,'.', '6');
        case 'h': x();xx();bass(1);reese(1),roller(1),fx(1);melo1(1),melo(1);voix()#w( '4~13', 16,'.', '6');#outro                                                                                          
        case 'i': pass
        case "◈": rise2 (1); V.tb=1;   fill();
    def bassintro(n=0,nn=3) :D([oo,f":{n} .!{nn}"],note="12 24",amp=.51,oct=P("4"),vel=127,i=i/16,d=2,dur=2)        
    def ww(n=3):D([ffv, f":{n} .!3"],   d=1, vel=1, speed='1.15', gain=.51, rate=1, orbit=orbdrum,room=0.0, dry=0,snap=0.6, dure=2, size=0, i=i/16)
    def voc(n=5) :D([ss,f":{n}"],speed=1,amp=1.21,oct=P("5"),cutoff=4800,hcutoff=1050,vel=127,i=i/160,d=1,dur=1)
    etrack="++++++++++++"# ◈>>>|▲▷▷/▲▣▣▣◎▷◎◎◎▣◈DDDD|▲▷▷▲▲▲▲"#▽▣▣◎◈>>>|▲▷▷▲" #▽▽▲▲▷▲▲▷▣▣"#▣▣◎/▷+"  #◈>>>|▲▷▷▲ drop 1      ◈DDDD|▲▷▷▲ drop2
   ## print("\n"*50,show_part(etrack, 0,1+int(V.progress)%len(etrack)),V.tb,P("4 3 2 1",i=i/64) )
    match show_part(etrack, 0,1+int(V.progress)%len(etrack))[-1]:             
     case 101: pass
     case  "▽": V.ssp=8 ; V.tb=1;tonal(18)
     case  "▣": V.ssp=4 ; V.tb=2;y
     case  "◎": V.ssp=4 ; V.tb=2;
     case  "▷": V.ssp=4 ; V.tb=1; ww("17") ;  
     case  "▲": V.ssp=4 ; V.tb=1 ; bassintro(2); w( 7, 16,'.', '.')  ;# ambiant()
     case  "▼": V.ssp=8 ; V.tb=2 ;kontakt() ;tonal(18);  x();V.orbdrum=2 ; # bassintro(), x();w( 7, 16,'.', '.')  ; ambiant()
     case  " ": pass;
     case  "/":  V.progress=1 #timeblock  
     case "◈": rise2 (1); V.tb=1;   fill();
     case ">": V.ssp=P("4 3 2 1 1 1 1 1",i=i/128) ; V.tb=1 ; fill()
     case "D": V.ssp=P("4 3 2 1 1 1 1 1",i=i/128) ; V.tb=1 ; fill2()
     case  "|":V.tb=1;voc(n=3); 
     case  "-":V.tb=1;
     case  "+":V.tb=0;
     case  "_":V.tb=1;
     case  "x":panic()
    V.progress+= pg(V.tb) ; 
    again(Thecompagnion,p=1/16,i=i+1)  

panic()

orbdrum=2

V.progress-=2

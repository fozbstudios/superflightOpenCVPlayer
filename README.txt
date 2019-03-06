the intent of this project is to create a supeflight auto player which runs (at least) in arch linux NOTE I AM NOT INVOLVED WITH SUPERFLIGHT IN ANY WAY

wine requirements
------------------
tbd
audio requirements
-------------------
install jack2-dbus and cadence
The ALSA audio bridge should be set to ALSA -> PulseAudio -> JACK, and the PulseAudio bridge should be enabled. Make sure in pavucontrol that all output devices besides Jack sink are muted, and all input devices besides Jack input are muted. Start JACK using the Force Restart button, and if it starts successfully PulseAudio programs should begin outputting to JACK. 
    -from https://wiki.archlinux.org/index.php/PulseAudio/Examples#Monitor_specific_output

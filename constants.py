# The eye aspect ratio (EAR) threshold that the EAR needs
# to be below to be considered closed.
EYE_AR_THRESH = 0.23
# The consecutive frames that the eyes need to be closed to 
# indicate a blink: dot
EYE_AR_CONSEC_FRAMES = 5
# Consec frames the EAR must be below the threshold: dash
EYE_AR_CONSEC_FRAMES_CLOSED = 15
# Consec frames the eye 
# must be open the threshold: /
PAUSE_CONSEC_FRAMES = 55
# Consec frames the eye must be open the threshold to indicated a pause
# between words. This is added with PAUSE_CONSEC_FRAMES to detect pause
WORD_PAUSE_CONSEC_FRAMES = 100
# Consec frames eyes must be closed to exit the program
BREAK_LOOP_FRAMES = 240
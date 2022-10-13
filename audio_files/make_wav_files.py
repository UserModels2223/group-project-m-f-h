from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()



with open("portugese_vocab.txt") as file:
    for line in file:
        pt_word = line.rstrip().partition('=')[0]
        eng_word = line.rstrip().partition('=')[2]
        # print(word[1:] + ".wav")
        pt_word = pt_word[:-1]
        eng_word = eng_word[1:]
        # print(pt_word)
        # print(eng_word)
        tts = gTTS(pt_word, lang='pt')
        tts.write_to_fp(mp3_fp)
        tts.save(eng_word + ".wav")
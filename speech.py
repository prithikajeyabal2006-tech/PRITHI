import os
import wave
from vosk import Model, KaldiRecognizer
import json
import speech_recognition as sr

VOSK_MODEL_PATH = os.getenv('VOSK_MODEL_PATH', 'models/vosk-small')

def transcribe_audio(path: str) -> str:
    # Try Vosk first
    try:
        wf = wave.open(path, "rb")
        if wf.getnchannels() != 1:
            from pydub import AudioSegment
            sound = AudioSegment.from_file(path)
            sound = sound.set_channels(1).set_frame_rate(16000)
            tmp = path + ".conv.wav"
            sound.export(tmp, format="wav")
            wf = wave.open(tmp, "rb")
            path = tmp

        model = Model(VOSK_MODEL_PATH)
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                results.append(res.get('text', ''))
        res = json.loads(rec.FinalResult())
        results.append(res.get('text', ''))
        return ' '.join([r for r in results if r])
    except Exception as e:
        r = sr.Recognizer()
        with sr.AudioFile(path) as source:
            audio = r.record(source)
        try:
            return r.recognize_google(audio)
        except Exception:
            return ""

from __future__ import division

import re
import sys

from google.cloud import speech

import pyaudio
from six.moves import queue

from playsound import playsound

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self.status = 0 
        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        if self.status ==0:
            self._buff.put(in_data)
            return None, pyaudio.paContinue
        elif self.status == 1:
            self._buff.put(b'')
            return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses, stream):
    num_chars_printed = 0
    voice_path = "./pompeii_voice/"
    p_state = 0
    disasters = ["지진", "홍수"]
    quiz_state = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            v_cmd = transcript + overwrite_chars
            if(p_state == 0):
                if("하이 폼페이" in v_cmd):
                    stream.status = 1
                    playsound(voice_path+'start.mp3')
                    stream.status = 0
                    p_state = 1
                else:
                    stream.status = 1
                    playsound(voice_path+'unknown_cmd.mp3')
                    stream.status = 0
            if(p_state == 1):
                if("퀴즈" in v_cmd):
                    stream.status = 1
                    playsound(voice_path+'selectDisaster.mp3')
                    stream.status = 0
                    p_state = 2
                elif("다른거" in v_cmd):
                    stream.statue = 1
                    stream.statue = 0
                else:
                    stream.status = 1
                    playsound(voice_path+'unknown_cmd.mp3')
                    stream.status = 0
            if(p_state == 2):
                # Quiz Start
                if(v_cmd.strip() in disasters):
                    stream.status = 1
                    playsound(voice_path + 'quizStart.mp3')
                    stream.status = 0
                    p_state = 3
                    quiz_state = 0
                    answer_cnt = 0
            if(p_state ==3):
                if(quiz_state == 3):
                    # Quiz End
                    if(answer_cnt == 0):
                        stream.status = 1
                        playsound(voice_path + 'zeroAnswer.mp3')
                        stream.status = 0
                    elif(answer_cnt == 1):
                        stream.status = 1
                        playsound(voice_path + 'oneAnswer.mp3')
                        stream.status = 0
                    elif(answer_cnt == 2):
                        stream.staus = 1
                        playsound(voice_path + 'twoAnswer.mp3')
                        stream.statue = 0
                    else:
                        stream.status = 1
                        playsound(voice_path + 'allAnswer.mp3')
                        stream.status = 0
                    p_state = 0
                    quiz_state = 0
                else:
                    quiz_state +=1
                    # QUIZ


                
            
                

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            num_chars_printed = 0


def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = "ko-KR"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses, stream)


if __name__ == "__main__":
    main()
# [END speech_transcribe_streaming_mic]

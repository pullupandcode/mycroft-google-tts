from mycroft import MycroftSkill, intent_handler
from google.cloud import texttospeech


class TextToSpeechSkill(MycroftSkill):
    def __init__(self):
        super(TextToSpeechSkill, self).__init__()
        self.tts = texttospeech.TextToSpeechClient()

    @intent_handler('playback.response.intent')
    def playback_response(self):
        content = "Sir, this is a Wendy's"
        systhesis_input = texttospeech.SysthesisInput(text=content)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = self.tts.systhesize_speech(
            input=systhesis_input, voice=voice, audio_config=audio_config
        )

        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)
            print("audio write out succeeded")



def create_skill():
    return TextToSpeechSkill()
import openai
import json

openai.organization = # add
openai.api_key = # add

# voice to text
def voice_to_text(audio_file):
    '''Takes in an .mp3 file and returns a string of the audio file's transcript
    
    Parameters:
        audio_file (str): path to .mp3 file

    Returns:
        str: transcript of audio file
    '''
    voice = open(audio_file, "rb")
    text = openai.Audio.transcribe("whisper-1", voice)
    return text # returns a string

text = voice_to_text("g_test.mp3")

# text to g-code
def text_to_g(text):
    '''Takes in a string and returns a string of the text's g-code
    
    Parameters:
        text (str): text to be converted to g-code

    Returns:
        str: g-code of text
    '''
    text = 'make the folling in g-code: ' + text['text']
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system", "content":"You program a 3D printer using G-Code. You just return the code, you must not include any disclaimers or explainations outside of comments in the code."},
            {"role":"user", "content":text}
        ],
        temperature=0,
        max_tokens=8000)
    return response

# output = text_to_g(text)
# g_code = output['choices'][0]['message']['content']

def vtg(audio_file):
    '''Takes in an .mp3 file and returns a string of the audio file's g-code
    
    Parameters:
        audio_file (str): path to .mp3 file

    Returns:
        str: g-code of audio file
    '''
    text = voice_to_text(audio_file)
    output = text_to_g(text)
    g_code = output['choices'][0]['message']['content']
    return print(g_code)

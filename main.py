# This is a sample Python script.
from gtts import gTTS

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tts = gTTS('한경호 교수님 종합 설계는 4월 20일에 중간 발표가 있습니다.', lang='ko')
    tts.save('example.mp3')


import sys
from mashup_logic import run_mashup

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102303723.py <Singer> <Videos> <Duration> <OutputFile>")
        return

    singer = sys.argv[1]
    videos = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]

    if videos <= 10:
        print("Number of videos must be greater than 10.")
        return

    if duration <= 20:
        print("Duration must be greater than 20 seconds.")
        return

    run_mashup(singer, videos, duration, output)

if __name__ == "__main__":
    main()

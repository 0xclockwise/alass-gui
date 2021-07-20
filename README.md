# ALASS GUI

A shitty tkinter wrapper around the very awesome [Automatic Language-Agnostic Subtitle Synchronization (Command Line Tool)](https://github.com/kaegi/alass)

![Screenshot](./screenshot.png)

Have you ever tried watching a movie with subtitles only to realize that the subtitle was not properly aligned with the movie? ALASS is a program that can align misaligned subtitles to a reference file which can either be a video file (in any format) or a correctly aligned subtitle file. If a video file is specified, alass will use voice activity detection on the choosen audio track of the video to align the subtitles. This takes longer than aligning to an other subtitle file. 
## Download

### Windows

Download the .zip from [here](https://github.com/0xclockwise/alass-gui/releases). It should work out of the box on regular installations of Windows. No need to install Python separately.

## TODO

- [ ] Tidy up the list of encodings. Right now it is just a copy-paste of what is present
      [here](https://encoding.spec.whatwg.org/), so it is filled with duplicates.
- [ ] Add the possibility of batch aligning series.

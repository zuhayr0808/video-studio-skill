# Long-form video guide

Read this for YouTube videos and anything longer than a couple of minutes.

## Format

- 16:9, 1920x1080 (or 3840x2160 if the user's footage is 4K), 24, 30 or 60 fps to match the footage. Never change the frame rate of footage without a reason.
- Export H.264 with AAC audio at a good bitrate. Name the output clearly and never overwrite the original.

## Editing real footage, in order

1. Make a working copy and an audio-only copy. The originals stay untouched.
2. Transcribe with Whisper so every word has a timestamp.
3. Find the dead air: long pauses, false starts, repeated takes and filler words. Propose the cuts to the user as a list with timestamps before cutting.
4. Cut with FFmpeg. Cut on word boundaries and leave a few frames of breathing room so speech does not feel chopped.
5. Fix the sound: even out the loudness, and keep music under the voice.
6. Add animated captions, lower thirds and titles with Remotion on top of the footage.
7. Export, then run the audio and picture checks.

## Keeping people watching

- Open with the payoff or the question, then explain. Do not start with a long intro.
- Change something every 5 to 10 seconds: a cut, a zoom, a graphic, a caption or a sound. Do not change things only for the sake of it, since each change should help the viewer.
- Put chapter titles and on-screen labels where the topic changes.
- End with one clear next step, not three.

## Sound

- Speech comes first. Music sits well below it and ducks under talking.
- Same research rule as short-form: no guessed sounds, every source and license logged, unconfirmed things marked unverified.
- Run the audio check on the whole file and report loudness, long silences, and any section where the music is louder than the voice.

## Checklist before delivering

- [ ] Original footage untouched
- [ ] Cut list approved by the user
- [ ] Speech clear throughout, music under it
- [ ] Captions match the transcript
- [ ] Contact sheet checked for bad frames, black frames and cut-off text
- [ ] Sources and licenses listed
- [ ] Anything unconfirmed marked unverified

# Code-made video guide

Read this when making a video from scratch with Remotion: animations, explainers, kinetic text, promos, intros, animated captions and graphics over real footage.

## Why code

Everything is drawn by code, so text, colors and timing are exact and the video can be re-rendered or changed at any time. This is not an AI video model. It does not make realistic people or places. It makes sharp motion graphics, typography, charts and edits of real clips.

## Set up a project

1. Run the setup check first.
2. Create the project in its own folder with `npx create-video@latest`.
3. Put every setting in one config file: colors, fonts, sizes, frame rate, and the timeline of scenes with start and end times. Scenes read from it, so a change in one place updates everything.
4. Keep assets (footage, images, audio) in a separate folder and never edit the originals.

## Plan before you code

Write the timeline in numbers first: total length, frame rate, and each scene with its start time, end time, on-screen text and sound. Show the user and get a yes. Check that scenes do not overlap by accident and add up to the total length.

## Build rules

- Animate with frames and Remotion's built-in timing and spring helpers, never with real-world timers, so every render is identical.
- One scene, one component. Small and reusable.
- Text must be readable on a phone. Use large type, strong contrast, and keep it inside the safe zones from the short-form guide when the video is vertical.
- Put the hook or the main message on screen within the first 3 seconds.
- Do not put a label on a number that is still counting up.
- Use a limited palette of two or three colors and one or two fonts.
- For captions over real footage, take the word timestamps from the Whisper transcript and highlight each word as it is spoken.

## Render

1. Do a quick low-resolution preview render first and check it.
2. Render the final video with Remotion at the target resolution and frame rate.
3. Use FFmpeg for the last step if needed: joining pieces, mixing in audio, or exporting for a platform.

## Check your work

You cannot watch the video, so measure it. Export a contact sheet of frames and look for black frames, cut-off text, overlaps and unreadable text. Run the audio check. For loops, compare the last frame with the first. Fix what fails and check again before delivering.

## Checklist before delivering

- [ ] Timeline approved by the user
- [ ] All settings in one config file
- [ ] Preview rendered and checked before the final render
- [ ] Hook or main message on screen by 3 s
- [ ] Text readable at phone size
- [ ] Contact sheet and audio checked
- [ ] Sources and licenses listed for any sound or asset
- [ ] Anything unconfirmed marked unverified

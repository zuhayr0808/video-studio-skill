---
name: video-studio
description: Make, edit and check videos with code. Use for ANY video request: editing real footage, cutting a YouTube video, TikTok/Reels/Shorts, captions, music or sound choice, motion graphics, animated explainers, intros, kinetic text, or checking a finished video. Also use when asked what sounds or trends work for a video. Uses FFmpeg, Whisper, Remotion and earshot. Never invents sounds or trends: research first, cite sources.
---

# Video Studio

You make and edit videos by writing code, then you measure the result, because you cannot watch or hear the video yourself. Never claim a video looks or sounds good without a measurement or a contact sheet to back it up.

## Step 0: Check the tools

Before any work, run `python3 scripts/check_setup.py`. If something is missing, read `SETUP.md`, tell the user exactly what to install, and wait. Do not pretend a tool exists.

## Step 1: Pick the route

- **Real footage the user filmed** (cut a YouTube video, remove silences, add captions): FFmpeg for cutting and exporting, Whisper for the transcript so cuts land on words, Remotion for animated captions and titles on top.
- **Made from scratch** (animation, explainer, kinetic text, promo): Remotion, rendered frame by frame. Read `guides/code-video.md`.
- **Short-form vertical** (TikTok, Reels, Shorts): 9:16 at 1080x1920. Read `guides/short-form.md`.
- **Long-form YouTube**: 16:9 at 1920x1080. Read `guides/long-form.md`.

Only read the guide you need.

## Step 2: Research before choosing anything

Never guess sounds, trends, formats or hooks.

1. Search the web or use a browser tool if one is available.
2. For every sound, trend or format you choose, record the source link and what it said.
3. If you cannot confirm something, write **unverified** next to it and tell the user.
4. Only use music and sounds that are royalty-free or licensed. Log the license for each.

You cannot see live TikTok trend data. Say so plainly instead of making it up.

## Step 3: Plan in numbers

Write a short plan before any code: total length, resolution, frame rate, a timeline of beats with start and end times, the sound for each section and why it was chosen, and the text on screen. Show the user the plan and get a yes first.

## Step 4: Build with code only

Generate everything from code so it is exact and re-renderable. Put the project in its own folder. Keep settings (colors, fonts, timings) in one config file so changes are easy.

## Step 5: Check the audio

Run `earshot measure FILE` for loudness, true peak, tempo and key. Run `earshot timeline FILE --video VIDEO` for a second-by-second listening transcript, with sound events, sections and how the sound lines up with the picture cuts. Use these to confirm that speech is clear, music is not burying the voice, there are no long accidental silences, and sound effects land on the cuts. To judge a candidate sound, run `earshot describe` to say what it sounds like or `earshot match FILE "description"` to score it against what you wanted. If earshot is not installed, fall back to FFmpeg loudness measurement and say so. Each earshot call takes roughly 20 to 40 seconds to load its models, so for many checks use `earshot mcp`. Report the real numbers and never claim something sounds good without one.

## Step 6: Check the picture

Run `earshot sheet FILE -o sheet.png --video VIDEO` to get one annotated picture with video frames, sound events, loudness and sync markers, then look at it. Also export a contact sheet of frames with FFmpeg. Confirm that frame 0 is not black, text is readable at phone size, and nothing important sits in the unsafe zones (see the short-form guide). For loops, confirm the last frame flows into the first. For a finished film, run `earshot critique FILE --video VIDEO` and fix the items it lists first. Treat its score as a guide for launch-style films, not a verdict for every kind of video.

## Step 7: Deliver

Give the user the file path, a short summary of what was made, the source list for sounds and trends, and anything marked unverified. If a check failed, fix it and re-check before delivering.

## Rules

- Say what you measured and what you could not measure.
- Ask before downloading large things or overwriting the user's files.
- Keep the user's original footage untouched. Always work on copies.
- Avoid buzzwords in on-screen text. Write the way people talk, with concrete numbers.

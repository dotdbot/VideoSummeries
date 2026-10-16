# Whisper Fallback Transcription

Use when youtube-transcript-api fails or for Hebrew videos.

## Download Audio

```bash
python3.11 -m yt_dlp -x --audio-format mp3 -o '/tmp/ytaudio.%(ext)s' 'URL'
```

If 403:
```bash
uv run --with yt-dlp yt-dlp -x --audio-format mp3 -o '/tmp/ytaudio.%(ext)s' 'URL'
```

If still 403, try m4a format:
```bash
python3.11 -m yt_dlp -f 140 -o '/tmp/ytaudio.%(ext)s' 'URL'
```

## Transcribe with faster-whisper

```bash
KMP_DUPLICATE_LIB_OK=TRUE uv run --with "faster-whisper" --with "numpy<2" python3.11 -c "
from faster_whisper import WhisperModel
model = WhisperModel('small', device='cpu', compute_type='int8')
segments, _ = model.transcribe('/tmp/ytaudio.mp3', beam_size=5)
with open('/tmp/transcript.txt', 'w') as f:
    for seg in segments:
        line = f'[{int(seg.start)}s] {seg.text.strip()}'
        print(line, flush=True); f.write(line + '\n')
"
```

### Hebrew

Add `language='he'` to `.transcribe()`:
```python
segments, _ = model.transcribe('/tmp/ytaudio.mp3', beam_size=5, language='he')
```

### Long audio

Use `terminal(background=True, notify=True)` to avoid timeouts.

### Timeout recovery

If whisper times out mid-run:
1. Check partial output: `tail -5 /tmp/transcript.txt`
2. Get last timestamp
3. Cut audio from that point: `ffmpeg -i /tmp/ytaudio.mp3 -ss LAST_TIMESTAMP -c copy /tmp/ytaudio_rest.mp3`
4. Transcribe the remainder and append

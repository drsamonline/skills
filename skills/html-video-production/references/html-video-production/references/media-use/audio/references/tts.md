# [MANUS OVERRIDE] Voice in Manus

Use `generate_speech` for all new voiceover. Save the generated WAV at the workflow's expected voice path, transcribe it with the permitted local fallback when word timestamps are required, and write the resulting `voices[]` record in `audio_meta.json` by hand. Do not choose a cloud voice provider, authenticate to an upstream provider, or configure a credential.

import asyncio
import edge_tts


async def generate_audio(
    text,
    profile,
    output_file,
):
    

    communicate = edge_tts.Communicate(
        text=text,
        voice=profile["voice"],
        rate=profile["rate"],
        volume=profile["volume"],
        pitch=profile["pitch"],
    )

    await communicate.save(output_file)
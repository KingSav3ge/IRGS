"""AI layer: multi-provider narration, TTS, STT, image generation, and the Jev
fast-decision layer (action-intent classification + content moderation).

Everything runs through the Emergent Universal LLM key. The AI narrates only;
it never mutates authoritative world state (that is the engine's job).
"""
import os
import io
import json
import base64
import logging

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("irgs.ai")

EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY")

# Provider/model options exposed in the UI. Default is GPT-5.6 Terra.
PROVIDERS = [
    {"id": "openai", "label": "ChatGPT", "model": "gpt-5.6-terra", "model_label": "GPT-5.6 Terra"},
    {"id": "gemini", "label": "Gemini", "model": "gemini-3.1-pro-preview", "model_label": "Gemini 3.1 Pro"},
    {"id": "anthropic", "label": "Claude", "model": "claude-sonnet-5-5", "model_label": "Claude Sonnet 5.5"},
]
DEFAULT_PROVIDER = "openai"
DEFAULT_MODEL = "gpt-5.6-terra"

TTS_VOICES = ["fable", "onyx", "nova", "sage", "shimmer", "echo"]
ELEVEN_VOICES = [
    {"id": "el-chronicler", "label": "The Chronicler", "style": "Deep, measured elder", "fallback": "onyx"},
    {"id": "el-bard", "label": "The Bard", "style": "Warm, theatrical storyteller", "fallback": "fable"},
    {"id": "el-seer", "label": "The Seer", "style": "Hushed, mystical", "fallback": "shimmer"},
    {"id": "el-herald", "label": "The Herald", "style": "Bright, commanding", "fallback": "nova"},
]


def _model_for(provider: str, model: str):
    for p in PROVIDERS:
        if p["id"] == provider:
            return provider, (model or p["model"])
    return DEFAULT_PROVIDER, DEFAULT_MODEL


async def narrate(scene_context: str, declaration: str, intent: str, provider: str, model: str) -> str:
    """Generate player-facing narration for a committed action. Presentation only."""
    from emergentintegrations.llm.chat import LlmChat, UserMessage

    provider, model = _model_for(provider, model)
    system = (
        "You are the Narrator of a persistent roleplaying simulation (historical, fantasy or science-fiction settings). "
        "The game engine is the sole authority over world state; you ONLY describe what the "
        "player perceives as a result of their declared action. Rules you must obey: "
        "do NOT change the player's inventory, inflict unrecorded injuries, award ranks, titles, "
        "wealth or qualifications, advance the calendar, create binding obligations, reveal hidden "
        "information, or rewrite history. Narrate in immersive second-person prose, 2-4 short "
        "paragraphs, grounded strictly in the provided scene context. End on an open beat that "
        "invites the player's next decision. Never resolve the outcome as guaranteed success."
    )
    chat = LlmChat(api_key=EMERGENT_LLM_KEY, session_id="narrate", system_message=system).with_model(provider, model)
    prompt = (
        f"SCENE CONTEXT:\n{scene_context}\n\n"
        f"The player (intent classified as '{intent}') declares:\n\"{declaration}\"\n\n"
        "Write the narration of what unfolds."
    )
    try:
        reply = await chat.send_message(UserMessage(text=prompt))
        return reply if isinstance(reply, str) else str(reply)
    except Exception as e:
        logger.error(f"narration failed: {e}")
        return (
            "The world holds its breath. Your words are recorded exactly as spoken, but the threads of "
            "consequence have not yet been drawn — the Narrator's voice falters for a moment. (AI narration "
            "is temporarily unavailable; your action is saved.)"
        )


async def jev_decide(declaration: str) -> dict:
    """Jev fast-decision layer: classify action-intent and moderate content.

    Returns {'intent': <category>, 'allowed': bool, 'reason': str}. Implemented as a
    compact, structured LLM classification (fast, cheap model).
    """
    from emergentintegrations.llm.chat import LlmChat, UserMessage

    system = (
        "You are a fast routing + safety classifier for a roleplaying engine. "
        "Given a player's action declaration, respond with STRICT JSON only, no prose: "
        '{"intent": one of ["move","speak","observe","interact","combat","rest","other"], '
        '"allowed": true|false, "reason": short string}. '
        "Set allowed=false only for content that is sexual content involving minors, real-world "
        "hate/harassment targeting protected groups, or instructions for real-world violence/weapons. "
        "In-fiction combat and conflict (any era or setting) is allowed."
    )
    chat = LlmChat(api_key=EMERGENT_LLM_KEY, session_id="jev", system_message=system).with_model("openai", "gpt-5.4-mini")
    try:
        reply = await chat.send_message(UserMessage(text=declaration[:1500]))
        text = reply if isinstance(reply, str) else str(reply)
        text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        data = json.loads(text)
        intent = data.get("intent", "other")
        if intent not in ("move", "speak", "observe", "interact", "combat", "rest", "other"):
            intent = "other"
        return {"intent": intent, "allowed": bool(data.get("allowed", True)), "reason": str(data.get("reason", ""))}
    except Exception as e:
        logger.error(f"jev decide failed: {e}")
        return {"intent": "other", "allowed": True, "reason": "classifier-unavailable"}


async def generate_image(prompt: str) -> bytes:
    """Generate a scene / portrait image (gpt-image-1). Returns PNG bytes."""
    from emergentintegrations.llm.openai.image_generation import OpenAIImageGeneration

    gen = OpenAIImageGeneration(api_key=EMERGENT_LLM_KEY)
    images = await gen.generate_images(prompt=prompt, model="gpt-image-1", number_of_images=1)
    if not images:
        raise RuntimeError("No image generated")
    return images[0]


async def tts_speak(text: str, voice: str = "fable") -> str:
    """OpenAI TTS. Returns base64 mp3 for inline playback."""
    from emergentintegrations.llm.openai import OpenAITextToSpeech

    tts = OpenAITextToSpeech(api_key=EMERGENT_LLM_KEY)
    if voice not in TTS_VOICES:
        voice = "fable"
    audio_b64 = await tts.generate_speech_base64(text=text[:4000], model="tts-1", voice=voice)
    return audio_b64


async def stt_transcribe(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    """OpenAI Whisper transcription of a spoken action."""
    from emergentintegrations.llm.openai import OpenAISpeechToText

    stt = OpenAISpeechToText(api_key=EMERGENT_LLM_KEY)
    buf = io.BytesIO(audio_bytes)
    buf.name = filename
    resp = await stt.transcribe(file=buf, model="whisper-1", response_format="json")
    return resp.text if hasattr(resp, "text") else str(resp)

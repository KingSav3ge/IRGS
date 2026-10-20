import { useRef, useState } from "react";
import { toast } from "sonner";
import { api, errMsg, fileUrl } from "@/lib/api";

export const useNarrator = () => {
  const audioRef = useRef(null);
  const [playingId, setPlayingId] = useState(null);
  const [loadingId, setLoadingId] = useState(null);

  const stop = () => {
    audioRef.current?.pause();
    audioRef.current = null;
    setPlayingId(null);
  };

  const speak = async (id, text, { engine, voice, castPid }) => {
    if (playingId === id) return stop();
    stop();
    setLoadingId(id);
    try {
      let src;
      if (castPid) {
        const { data } = await api.post(`/playthroughs/${castPid}/events/${id}/voice`, {}, { timeout: 120000 });
        src = fileUrl(data.audio_url);
      } else {
        const { data } = await api.post("/voice/tts", { text, engine, voice });
        if (data.downgraded) toast("Your ElevenLabs subscription has ended, so the standard voice is narrating.");
        src = `data:audio/mp3;base64,${data.audio_base64}`;
      }
      const audio = new Audio(src);
      audioRef.current = audio;
      audio.onended = () => setPlayingId(null);
      await audio.play();
      setPlayingId(id);
    } catch (e) {
      toast.error(errMsg(e, "Narration voice unavailable"));
    } finally {
      setLoadingId(null);
    }
  };

  return { speak, stop, playingId, loadingId };
};

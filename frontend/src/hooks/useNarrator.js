import { useRef, useState } from "react";
import { toast } from "sonner";
import { api, errMsg } from "@/lib/api";

export const useNarrator = () => {
  const audioRef = useRef(null);
  const [playingId, setPlayingId] = useState(null);
  const [loadingId, setLoadingId] = useState(null);

  const stop = () => {
    audioRef.current?.pause();
    audioRef.current = null;
    setPlayingId(null);
  };

  const speak = async (id, text, { engine, voice }) => {
    if (playingId === id) return stop();
    stop();
    setLoadingId(id);
    try {
      const { data } = await api.post("/voice/tts", { text, engine, voice });
      const audio = new Audio(`data:audio/mp3;base64,${data.audio_base64}`);
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

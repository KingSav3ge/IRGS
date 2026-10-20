import { useRef, useState } from "react";
import { toast } from "sonner";
import { api, errMsg } from "@/lib/api";

export const useRecorder = (onText) => {
  const recRef = useRef(null);
  const [state, setState] = useState("idle");

  const start = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const rec = new MediaRecorder(stream);
      const chunks = [];
      rec.ondataavailable = (e) => chunks.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach((t) => t.stop());
        setState("transcribing");
        const fd = new FormData();
        fd.append("file", new Blob(chunks, { type: "audio/webm" }), "action.webm");
        try {
          const { data } = await api.post("/voice/stt", fd);
          onText(data.text);
        } catch (e) {
          toast.error(errMsg(e, "Could not transcribe"));
        } finally {
          setState("idle");
        }
      };
      rec.start();
      recRef.current = rec;
      setState("recording");
    } catch {
      toast.error("Microphone access was denied");
    }
  };

  const toggle = () => (state === "recording" ? recRef.current?.stop() : state === "idle" && start());
  return { state, toggle };
};

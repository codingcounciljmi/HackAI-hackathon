
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np
import io
import wave
from core.rich_ui import console, print_error

class SoundBox:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.last_input_was_voice = False
        self.sample_rate = 16000  # Standard for speech recognition
        self.channels = 1
        try:
            self.engine = pyttsx3.init()
            # Set properties - make it sound decent
            self.engine.setProperty('rate', 170) 
            self.available = True
        except Exception as e:
            console.print(f"[yellow]⚠️ SoundBox (TTS) initialized with errors: {e}[/yellow]")
            self.engine = None
            self.available = False

    def get_input(self, prompt_text: str = "", input_style: str = "bold white") -> str:
        """
        Get input from user, supporting voice via 'v'.
        """
        self.last_input_was_voice = False
        if prompt_text:
            console.print(f"\n{prompt_text}", style="bold cyan")
        console.print("[dim](⌨️ Type or 🎤 Press 'v' + Enter for Voice)[/dim]")
        
        user_in = console.input(f"[{input_style}]   👉 [/{input_style}]").strip()
        
        if user_in.lower() == 'v':
            voice_text = self.listen()
            if voice_text:
                self.last_input_was_voice = True
                return voice_text
            else:
                return "" # Failed input
        
        return user_in

    def speak(self, text):
        """Convert text to speech."""
        if self.engine:
            try:
                # Clean text of markdown or emojis if simple tts struggles? 
                # pyttsx3 usually handles basic text fine.
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                console.print(f"[red]SoundBox Error: {e}[/red]")

    def stop(self):
        """Stop any ongoing speech immediately."""
        if self.engine:
            try:
                self.engine.stop()
            except Exception:
                pass  # Silently ignore errors when stopping

    def _record_audio(self, duration: float = 8.0) -> np.ndarray:
        """Record audio using sounddevice."""
        console.print("\n[bold red blink]🎤 Listening... (Speak now)[/bold red blink]")
        
        # Record audio
        recording = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype=np.int16
        )
        sd.wait()  # Wait until recording is finished
        
        return recording

    def _numpy_to_audio_data(self, audio_np: np.ndarray) -> sr.AudioData:
        """Convert numpy array to SpeechRecognition AudioData."""
        # Create a WAV file in memory
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)  # 2 bytes for int16
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_np.tobytes())
        
        buffer.seek(0)
        
        # Read it back as AudioData
        with sr.AudioFile(buffer) as source:
            audio_data = self.recognizer.record(source)
        
        return audio_data

    def listen(self):
        """Listen to microphone input and return text."""
        try:
            # Record audio using sounddevice
            audio_np = self._record_audio(duration=8.0)
            
            console.print("[dim cyan]Thinking...[/dim cyan]")
            
            # Convert to AudioData for speech_recognition
            audio_data = self._numpy_to_audio_data(audio_np)
            
            # Use Google Speech Recognition
            text = self.recognizer.recognize_google(audio_data)
            console.print(f"[bold green]🗣️ Detected:[/bold green] \"{text}\"\n")
            return text
                
        except sr.UnknownValueError:
            console.print("[yellow]🤔 Could not distinguish words.[/yellow]")
            return None
        except sr.RequestError as e:
            console.print(f"[red]Request Error: {e}[/red]")
            return None
        except Exception as e:
            console.print(f"[red]Microphone Error (is it connected?): {e}[/red]")
            return None

# Global instance
soundbox = SoundBox()

from faster_whisper import WhisperModel


print("INICIO")


model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


print("MODELO CARGADO")
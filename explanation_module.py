import os

# Optional local explanation model.
# If TRANSFORMERS_ENABLED=false, EduGenie uses Gemini as a fallback.
USE_TRANSFORMERS = os.getenv("TRANSFORMERS_ENABLED", "false").lower() == "true"

_tokenizer = None
_model = None


def _load_local_model():
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        model_name = os.getenv(
            "EXPLANATION_MODEL",
            "MBZUAI/LaMini-Flan-T5-783M"
        )
        _tokenizer = AutoTokenizer.from_pretrained(model_name)
        _model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return _tokenizer, _model


def explain_topic(topic: str) -> str:
    if not USE_TRANSFORMERS:
        from gemini_module import _generate
        return _generate(
            f"Explain '{topic}' in simple, clear language for a college student. "
            "Use a short explanation and one example."
        )

    tokenizer, model = _load_local_model()
    import torch

    prompt = (
        f"Explain the concept of '{topic}' in a simple and clear way "
        "for a college student. Give one example."
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=180,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

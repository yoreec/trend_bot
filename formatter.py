import random

def make_hype_post(headline):
    templates = [
        f"🔥 БОМБА! {headline.upper()} — ты не поверишь, что происходит!",
        f"⚠️ ВСЕ говорят об этом: {headline}",
        f"💥 Разрыв! {headline} — обсуждают в каждом чате!",
        f"🤯 {headline} — вот где настоящий хайп!"
    ]
    return random.choice(templates)

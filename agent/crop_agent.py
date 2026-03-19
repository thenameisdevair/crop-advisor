import os
from openai import OpenAI
from config.settings import MODEL, MAX_TOKENS, TEMPERATURE
from utils.image_utils import compress_and_encode

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(farmer_note="", location=""):
    context_parts = []
    if location:
        context_parts.append(f"Location: {location}")
    if farmer_note:
        context_parts.append(f"Farmer says: {farmer_note}")
    context = "\n".join(context_parts) if context_parts else "No additional context provided."
    return (
        "You are a friendly farm advisor helping smallholder farmers. "
        "Speak directly to the farmer in plain, simple English like a trusted friend who knows farming.\n\n"
        f"Context:\n{context}\n\n"
        "Look at this crop photo carefully and respond in this exact conversational format:\n\n"
        "This is a picture of a [plant name] plant, damaged by [problem name].\n"
        "This type of damage is mainly caused by [main cause], though [other factors] may also contribute.\n"
        "For cure, try [2-3 simple, cheap, local remedies].\n"
        "Next time you can prevent this by [1-2 prevention tips].\n\n"
        "If the plant looks healthy, say so clearly and give one tip to keep it that way.\n"
        "Keep language simple. No bullet points. Speak like you are talking to the farmer face to face."
    )

def analyze_crop(image_bytes, farmer_note="", location="", crop_type=""):
    try:
        base64_image = compress_and_encode(image_bytes)
        prompt = build_prompt(farmer_note, location)
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Analysis failed: {str(e)}"
import random

def analyze_wardrobe(img):
    fabrics = ["Polyester", "Cotton", "Silk", "Hemp", "Denim"]
    detected = random.sample(fabrics, k=2)
    sustainable = {"Cotton": True, "Hemp": True, "Polyester": False, "Silk": True, "Denim": False}

    result = "**🧵 Detected Fabrics:** " + ", ".join(detected) + "\n\n"
    result += "**🌱 Sustainability Tips:**\n"
    for f in detected:
        if sustainable[f]:
            result += f"- ✅ {f} is eco-friendly and biodegradable.\n"
        else:
            result += f"- ⚠️ {f} is not eco-optimal. Try switching to organic cotton or hemp.\n"
    return result

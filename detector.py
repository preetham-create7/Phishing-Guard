from urllib.parse import urlparse
import ipaddress


def detect_phishing(url):

    score = 0
    reasons = []

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    if not hostname:
        return {
            "score": 100,
            "status": "Invalid URL",
            "reasons": ["Invalid domain name"]
        }

    # Check HTTPS
    if parsed.scheme != "https":
        score += 15
        reasons.append("Website does not use HTTPS")

    # Check IP address
    try:
        ipaddress.ip_address(hostname)
        score += 25
        reasons.append("Uses an IP address instead of a domain")
    except ValueError:
        pass

    # Check suspicious keywords
    keywords = [
        "login", "verify", "update",
        "secure", "password", "banking"
    ]

    found = [word for word in keywords if word in url.lower()]

    if found:
        score += min(len(found) * 8, 24)
        reasons.append("Suspicious keywords detected")

    # Check URL length
    if len(url) > 75:
        score += 10
        reasons.append("Unusually long URL")

    # Check @ symbol
    if "@" in url:
        score += 20
        reasons.append("Contains @ symbol")

    score = min(score, 100)

    if score >= 50:
        status = "High Risk"
    elif score >= 25:
        status = "Suspicious"
    else:
        status = "Low Risk"

    if not reasons:
        reasons.append("No suspicious URL patterns detected")

    return {
        "score": score,
        "status": status,
        "reasons": reasons
    }
# alerts/detox_rotation.py
import os, smtplib, hashlib, datetime as dt
from email.mime.text import MIMEText

# ---- USER CONFIG ----
ITEMS = [
    "Haldi water (warm)",
    "Saunf (fennel) water",
    "Kesar water",
    "Methi (fenugreek) water",
    "Elaichi water",
    "AloeGelJaiphal water",   # aapne jo likha tha usko safely ek naam de diya
    "Ginger water",
    "Jeera water",
    "Lemon water"
]
TIMEZONE_NOTE = "Asia/Kolkata (IST)"
NUM_PER_DAY = 2   # aaj ke din kitne reminder slots (2 = 2 emails)

# Secrets (GitHub Actions → Settings → Secrets → Actions)
SENDER = os.environ["SMTP_USER"]
APP_PASS = os.environ["SMTP_PASS"]
TO = os.environ.get("TO_EMAIL", SENDER)

# SLOT decides kaunsa item bhejna (1st or 2nd of the day)
SLOT = int(os.environ.get("SLOT", "1"))  # 1 ya 2

# ---- PICK ITEM FOR TODAY ----
# stable rotation: date-based seed
today = dt.date.today()
seed = int(hashlib.sha256(str(today).encode()).hexdigest(), 16)
start_idx = seed % len(ITEMS)

# slot -> index mapping (distinct items per day)
# e.g., SLOT=1 -> start_idx, SLOT=2 -> start_idx+1, wrap around
idx = (start_idx + (SLOT - 1)) % len(ITEMS)
item = ITEMS[idx]

# ---- EMAIL ----
subject = f"💧 Morning Detox Reminder ({item})"
body = (
    f"Good morning! Hare Krishna🌅\n\n"
    f"Aaj ka detox: {item}\n"
    f"(Daily rotation • Timezone: {TIMEZONE_NOTE})\n\n"
    f"Stay hydrated ✨"
)

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = subject
msg["From"] = SENDER
msg["To"] = TO

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER, APP_PASS)
    smtp.send_message(msg)

print(f"✅ Sent detox reminder for {today}: [{SLOT}/{NUM_PER_DAY}] -> {item}")

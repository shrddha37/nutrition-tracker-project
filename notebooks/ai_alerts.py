{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ce629b6-4067-43ba-9148-c47f60eee82e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⚠️ Hydration Alert: Drink more water (below 2L)\n"
     ]
    }
   ],
   "source": [
    "# ai_alerts.py\n",
    "# Rule-based intelligence for Nutrition-DE-Pipeline\n",
    "\n",
    "def generate_alerts(water_ml, total_kcal, target_kcal):\n",
    "    alerts = []\n",
    "\n",
    "    if water_ml < 2000:\n",
    "        alerts.append(\"⚠️ Hydration Alert: Drink more water (below 2L)\")\n",
    "\n",
    "    if total_kcal > target_kcal + 200:\n",
    "        alerts.append(\"⚠️ Calorie Alert: Intake exceeded daily target\")\n",
    "\n",
    "    if total_kcal < target_kcal - 300:\n",
    "        alerts.append(\"⚠️ Low Energy Alert: Calories too low today\")\n",
    "\n",
    "    if not alerts:\n",
    "        alerts.append(\"✅ Good job! Nutrition is on track\")\n",
    "\n",
    "    return alerts\n",
    "\n",
    "\n",
    "# ---- Example run (can later be replaced by PySpark output) ----\n",
    "if __name__ == \"__main__\":\n",
    "    water_ml = 1500\n",
    "    total_kcal = 2200\n",
    "    target_kcal = 2000\n",
    "\n",
    "    results = generate_alerts(water_ml, total_kcal, target_kcal)\n",
    "\n",
    "    for r in results:\n",
    "        print(r)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

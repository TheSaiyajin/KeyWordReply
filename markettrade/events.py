import random


def format_event_line(event_data):
    change_percent = round(float(event_data.get("change_per_tick", 0.0)) * 100, 2)
    remaining_ticks = max(0, int(event_data.get("remaining_ticks", 0)))
    direction = "+" if change_percent >= 0 else ""
    return f"⚡ {direction}{change_percent}% x {remaining_ticks} tick(s)"


def roll_random_event(active_events, assets, chance_percent: float):
    chance = min(100.0, max(0.0, float(chance_percent))) / 100.0
    if random.random() >= chance:
        return active_events, None

    available_symbols = [symbol for symbol in assets.keys() if symbol not in active_events]
    if not available_symbols:
        return active_events, None

    selected_symbol = random.choice(available_symbols)
    random_percent = round(random.uniform(1.0, 3.0), 2)
    signed_percent = random_percent if random.random() < 0.5 else random_percent * -1
    active_events[selected_symbol] = {
        "change_per_tick": round(signed_percent / 100.0, 4),
        "remaining_ticks": random.randint(1, 4),
        "source": "random",
    }
    return active_events, (selected_symbol, dict(active_events[selected_symbol]))

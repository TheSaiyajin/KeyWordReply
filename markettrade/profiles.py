import random


PROFILE_NAMES = (
    "stable",
    "wild",
    "uptrend",
    "downtrend",
    "swing",
    "bullrun",
    "crash",
    "recovery",
    "flat",
)


PROFILE_DATA = {
    "stable": {
        "volatility": 0.006,
        "risk": 0.9,
        "momentum": 0.50,
        "reversal_accel": 0.14,
        "drift": 0.00003,
        "bull_bias": 0.002,
    },
    "wild": {
        "volatility": 0.016,
        "risk": 1.2,
        "momentum": 0.54,
        "reversal_accel": 0.12,
        "drift": 0.00002,
        "bull_bias": 0.002,
    },
    "uptrend": {
        "volatility": 0.008,
        "risk": 1.0,
        "momentum": 0.53,
        "reversal_accel": 0.12,
        "drift": 0.00008,
        "bull_bias": 0.008,
    },
    "downtrend": {
        "volatility": 0.008,
        "risk": 1.0,
        "momentum": 0.53,
        "reversal_accel": 0.12,
        "drift": -0.00008,
        "bull_bias": -0.008,
    },
    "swing": {
        "volatility": 0.012,
        "risk": 1.1,
        "momentum": 0.48,
        "reversal_accel": 0.18,
        "drift": 0.0,
        "bull_bias": 0.0,
    },
    "bullrun": {
        "volatility": 0.014,
        "risk": 1.15,
        "momentum": 0.70,
        "reversal_accel": 0.07,
        "drift": 0.00018,
        "bull_bias": 0.020,
    },
    "crash": {
        "volatility": 0.020,
        "risk": 1.35,
        "momentum": 0.72,
        "reversal_accel": 0.05,
        "drift": -0.00028,
        "bull_bias": -0.030,
    },
    "recovery": {
        "volatility": 0.009,
        "risk": 1.0,
        "momentum": 0.58,
        "reversal_accel": 0.10,
        "drift": 0.00011,
        "bull_bias": 0.012,
    },
    "flat": {
        "volatility": 0.003,
        "risk": 0.75,
        "momentum": 0.45,
        "reversal_accel": 0.20,
        "drift": 0.0,
        "bull_bias": 0.0,
    },
}


PROFILE_TRANSITIONS = {
    "stable": [("stable", 55), ("uptrend", 18), ("downtrend", 16), ("swing", 7), ("flat", 2), ("bullrun", 1), ("crash", 1)],
    "uptrend": [("uptrend", 45), ("stable", 30), ("swing", 10), ("downtrend", 8), ("bullrun", 5), ("flat", 2)],
    "downtrend": [("downtrend", 45), ("stable", 30), ("swing", 10), ("uptrend", 8), ("crash", 5), ("flat", 2)],
    "swing": [("swing", 45), ("stable", 25), ("uptrend", 12), ("downtrend", 12), ("wild", 4), ("flat", 2)],
    "wild": [("wild", 40), ("swing", 25), ("stable", 15), ("uptrend", 8), ("downtrend", 8), ("bullrun", 2), ("crash", 2)],
    "bullrun": [("uptrend", 70), ("stable", 20), ("swing", 8), ("wild", 2)],
    "crash": [("recovery", 70), ("stable", 20), ("downtrend", 8), ("flat", 2)],
    "recovery": [("stable", 55), ("uptrend", 30), ("swing", 10), ("flat", 5)],
    "flat": [("stable", 60), ("uptrend", 15), ("downtrend", 15), ("swing", 8), ("wild", 2)],
}


def behavior_profile(profile: str):
    return PROFILE_DATA.get(profile)


def profile_transition_window_seconds():
    return random.randint(2 * 3600, 8 * 3600)


def next_profile(current_profile: str):
    options = PROFILE_TRANSITIONS.get(current_profile, PROFILE_TRANSITIONS["stable"])
    roll = random.uniform(0.0, sum(weight for _, weight in options))
    running = 0.0
    for name, weight in options:
        running += weight
        if roll <= running:
            return name
    return options[-1][0]


def detect_asset_profile(asset: dict) -> str:
    explicit_profile = str(asset.get("profile", "")).strip().lower()
    if explicit_profile in set(PROFILE_NAMES) | {"custom"}:
        return explicit_profile

    asset_volatility = round(float(asset.get("volatility", 0.0)), 4)
    asset_risk = round(float(asset.get("risk", 1.0)), 2)
    asset_momentum = round(float(asset.get("momentum", 0.6)), 4)
    asset_reversal_accel = round(float(asset.get("reversal_accel", 0.08)), 4)
    asset_drift = round(float(asset.get("drift", 0.0)), 5)
    asset_bull_bias = round(float(asset.get("bull_bias", 0.05)), 4)

    for profile_name in PROFILE_NAMES:
        profile_data = behavior_profile(profile_name)
        if profile_data is None:
            continue
        if (
            asset_volatility == round(float(profile_data.get("volatility", 0.0)), 4)
            and asset_risk == round(float(profile_data.get("risk", 1.0)), 2)
            and asset_momentum == round(float(profile_data.get("momentum", 0.6)), 4)
            and asset_reversal_accel == round(float(profile_data.get("reversal_accel", 0.08)), 4)
            and asset_drift == round(float(profile_data.get("drift", 0.0)), 5)
            and asset_bull_bias == round(float(profile_data.get("bull_bias", 0.05)), 4)
        ):
            return profile_name

    return "custom"

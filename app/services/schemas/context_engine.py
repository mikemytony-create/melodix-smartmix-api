from datetime import datetime


class ContextEngine:

    def get_context(self):

        now = datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            period = "morning"

        elif 12 <= hour < 18:
            period = "afternoon"

        elif 18 <= hour < 22:
            period = "evening"

        else:
            period = "night"

        return {
            "hour": hour,
            "period": period,
            "weekday": now.strftime("%A"),
            "month": now.strftime("%B")
        }

    def suggest_mood(self):

        context = self.get_context()

        if context["period"] == "morning":
            return "motivation"

        elif context["period"] == "afternoon":
            return "focus"

        elif context["period"] == "evening":
            return "chill"

        return "relax"


context_engine = ContextEngine()
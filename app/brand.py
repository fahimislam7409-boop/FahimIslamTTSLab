"""The name and the credit line. Every screen, banner and page takes them from here."""

NAME = "Fahim TTS Lab"
VERSION = "2.0.0"
CREDIT = "Developer Fahim Islam"
CHANNEL_NAME = "Freelancer Fahim Islam"
CHANNEL_URL = "https://www.youtube.com/@FreelancerFahimIslam/videos"
REPO_URL = "https://github.com/fahimislam7409-boop/FahimIslamTTSLab"


def banner() -> str:
    line = "=" * 62
    return f"{line}\n  {NAME}  v{VERSION}\n  {CREDIT}\n  {CHANNEL_URL}\n{line}"


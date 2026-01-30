import os
from typing import Optional


class StoryGenerator:
    """Generates stories. If `OPENAI_API_KEY` is set and the `openai` package
    is available, it will use the OpenAI ChatCompletion API. Otherwise it
    falls back to a deterministic local generator."""

    def __init__(self, model: Optional[str] = None):
        self.model = model or "gpt-3.5-turbo"
        self.api_key = os.getenv("OPENAI_API_KEY")

    def _ai_generate(self, prompt: str, genre: str, length: str, tone: str) -> Optional[str]:
        if not self.api_key:
            return None

        try:
            import openai
        except Exception:
            return None

        openai.api_key = self.api_key
        system = (
            "You are a creative writing assistant."
            " Produce a story based on the user's prompt. Keep it coherent and in the requested tone and genre."
        )
        user_msg = f"Write a {length.lower()} {genre} story in a {tone.lower()} tone. Prompt: {prompt}"

        try:
            resp = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user_msg}],
                max_tokens=800,
            )
            return resp.choices[0].message.content.strip()
        except Exception:
            return None

    def generate_story(self, prompt: str, genre: str, length: str, tone: str) -> str:
        # Try AI backend first (if configured)
        ai_result = self._ai_generate(prompt, genre, length, tone)
        if ai_result:
            return ai_result

        # Improved deterministic fallback with varied narrative content
        return self._generate_fallback_story(prompt, genre, length, tone)

    def _generate_fallback_story(self, prompt: str, genre: str, length: str, tone: str) -> str:
        """Generate a varied fallback story using different narrative structures."""
        paragraphs = []
        
        # Opening
        opening = self._get_opening(prompt, genre, tone)
        paragraphs.append(opening)
        
        # Determine number of body paragraphs
        if length.lower() == "short":
            num_body = 2
        elif length.lower() == "long":
            num_body = 5
        else:
            num_body = 3
        
        # Body paragraphs with varied content
        for i in range(num_body):
            body = self._get_body_paragraph(prompt, genre, tone, i + 1, num_body)
            paragraphs.append(body)
        
        # Closing
        closing = self._get_closing(prompt, genre, tone)
        paragraphs.append(closing)
        
        return "\n\n".join(paragraphs)

    def _get_opening(self, prompt: str, genre: str, tone: str) -> str:
        """Generate an opening paragraph based on genre and tone."""
        openings = {
            "Fantasy": [
                "In a realm where {prompt}, magic flowed through the land like unseen rivers. The prophecy had spoken of this moment for centuries.",
                "The ancient scroll foretold: '{prompt}'. On the darkest night, the heroes assembled, knowing their fate was sealed.",
                "A whispered rumor spread through the kingdom: {prompt}. None dared speak it aloud.",
            ],
            "Sci-Fi": [
                "The star charts aligned with an impossible pattern. Scientists confirmed it: {prompt}. Humanity would never be the same.",
                "Dr. Chen's scanner beeped three times. The reading was impossible: {prompt}. She stared at the data in disbelief.",
                "Year 2287: {prompt}. The transmission crackled across the void, changing everything they thought they knew.",
            ],
            "Mystery": [
                "The case arrived on Detective Morgan's desk with no explanation: {prompt}. Her hands trembled as she opened the file.",
                "No one wanted to talk about it, but everyone knew: {prompt}. The truth was buried somewhere in the shadows.",
                "Three clues. One victim. One question: {prompt}. The investigation had only just begun.",
            ],
            "Horror": [
                "The first sign was subtle: {prompt}. By the time anyone noticed, it was already too late.",
                "They say that {prompt} was just the beginning. The nightmare had only just woken.",
                "In the dead of night, whispers told of {prompt}. No one dared investigate—not after what happened to the last person who did.",
            ],
            "Romance": [
                "Two souls crossed paths because of {prompt}. Neither expected to find what they were truly seeking.",
                "It started with {prompt}. Neither of them believed in fate, but the universe had other plans.",
                "Against all odds, {prompt} brought them together. What happened next neither could have predicted.",
            ],
            "Historical": [
                "In the annals of history, {prompt} marked a turning point. Few knew the truth behind the legend.",
                "The year was darker than most, and {prompt} echoed through the chronicles of time.",
                "Historians would later argue about {prompt}, but those who lived it knew the real story.",
            ],
        }
        
        genre_openings = openings.get(genre, openings["Fantasy"])
        template = genre_openings[hash(prompt) % len(genre_openings)]
        return template.format(prompt=prompt)

    def _get_body_paragraph(self, prompt: str, genre: str, tone: str, para_num: int, total_paras: int) -> str:
        """Generate a body paragraph with varied content based on narrative position."""
        midpoint = total_paras / 2
        
        if para_num <= midpoint:
            # Early body: setup and complications
            templates = [
                "As the events unfolded, it became clear that {prompt} was only the beginning. Deeper layers of complexity emerged.",
                "The implications of {prompt} spread like ripples across a still pond. Unexpected consequences followed.",
                "Few understood the significance of {prompt}. Fewer still could have predicted what came next.",
                "Time seemed to move differently after {prompt}. The world had shifted in subtle but profound ways.",
            ]
        else:
            # Late body: climax and revelation
            templates = [
                "The truth about {prompt} was finally coming into focus. Pieces fell into place like a puzzle long unsolved.",
                "What seemed impossible became reality. {prompt} wasn't just an event—it was a revelation.",
                "In that moment, when {prompt} became undeniable, everything changed. There was no going back.",
                "The culmination of {prompt} brought clarity. All the doubt, all the fear—it crystallized into truth.",
            ]
        
        selected = templates[hash(prompt + str(para_num)) % len(templates)]
        return selected.format(prompt=prompt)

    def _get_closing(self, prompt: str, genre: str, tone: str) -> str:
        """Generate a closing paragraph that resolves or reflects on the story."""
        closings = {
            "Serious": [
                "The weight of {prompt} settled upon them like an eternal burden. Some lessons, once learned, could never be unlearned.",
                "And so {prompt} became part of the tapestry of their lives—indelible and unchangeable.",
                "When the dust settled, {prompt} had left its mark. The world would remember.",
            ],
            "Humorous": [
                "In the end, {prompt} turned out to be far more absurd than anyone had imagined. Nobody saw the punchline coming.",
                "If someone had told them that {prompt} would lead here, they would have laughed. Well, here they were.",
                "The moral of the story was simple: {prompt} was funnier in hindsight than it was in the moment.",
            ],
            "Dark": [
                "The shadows around {prompt} never fully lifted. Some truths were too dark to fully illuminate.",
                "In the darkness after {prompt}, they found only silence and the echo of what might have been.",
                "{prompt} had changed them. Whether for better or worse, no one could say.",
            ],
            "Inspirational": [
                "{prompt} had shown them what they were truly capable of. The journey had only just begun.",
                "From {prompt}, hope emerged. And with hope came possibility.",
                "The lesson of {prompt} would stay with them forever: triumph comes to those brave enough to face the unknown.",
            ],
        }
        
        tone_key = tone if tone in closings else "Serious"
        closing_list = closings[tone_key]
        template = closing_list[hash(prompt) % len(closing_list)]
        return template.format(prompt=prompt)

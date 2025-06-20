from transformers import pipeline

# Load the summarization model
summarizer = pipeline("text2text-generation", model="sshleifer/distilbart-cnn-12-6")

def summarize_segment(transcript, web_context=""):
    prompt = f"""
You are a senior documentation and technical writing expert. Your task is to convert a raw transcript segment into a highly accurate, formal implementation guide for the subject matter discussed.

Use the formatting, detail level, and clarity expected of professional documentation intended for training, onboarding, and knowledge retention.

---

OBJECTIVE:
Produce a **step-by-step implementation or process guide** that is comprehensive enough to support the creation of over 100 technical or comprehension questions in a separate process. Your guide must reflect real-world tools, terminology, and workflows relevant to the subject — not abstract or generic instructions.

---

DOCUMENT FORMAT & STRUCTURE RULES:

1. STRUCTURE
- Use numbered sections and sub-sections (e.g., 1, 1.1, 1.2.1)
- No markdown, emojis, or decorative formatting
- Use plain, formal, enterprise-grade language

2. EACH SECTION MUST INCLUDE:
- A **clear title** and **brief purpose statement**
- **Step-by-step technical or procedural instructions**, including:
  - Tools or interfaces mentioned (if any)
  - Paths, commands, actions, or steps
  - Required inputs, parameters, or values
  - Logical and complete sequence of operations

3. VALIDATION
- Describe how to confirm success (e.g., outputs, indicators, system checks, verifications)

4. TROUBLESHOOTING (if applicable)
- Include common errors, causes, and solutions
- Mention where logs, reports, or error outputs can be reviewed

5. BEST PRACTICES
- Conclude each major section with expert tips, efficiency recommendations, or standard guidelines

6. CONCLUSION
- Summarize what was implemented or discussed
- Confirm expected outcomes and readiness indicators

---

WEB CONTEXT USAGE:

If web content is provided, **use it only to clarify or enhance** information in the transcript. Do **not** quote or copy it directly. Use it to fill in gaps or support the logical flow of the guide.

--- BEGIN WEB CONTEXT ---
{web_context}
--- END WEB CONTEXT ---

---

TRANSCRIPT SEGMENT:
\"\"\"{transcript}\"\"\"

---

FINAL INSTRUCTION:
Return only the fully formatted implementation or process guide.  
Do **not** generate any questions in this step.  
Ensure the output is detailed and structured enough for a separate team to extract **100+ questions** later.

End the document with:  
**Suggested next steps: No specific next steps mentioned in this segment.**
"""
    return prompt.strip()


def chunk_text(text, max_tokens=800):
    words = text.split()
    return [' '.join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]

def generate_summary(text: str, web_context: str = "") -> str:
    if not text.strip():
        return "Summary not generated: empty text."

    chunks = chunk_text(text)
    final_summary = []

    for chunk in chunks:
        try:
            prompt = summarize_segment(chunk, web_context)
            result = summarizer(prompt, max_length=1024, min_length=100, do_sample=False)
            final_summary.append(result[0]['generated_text'])
        except Exception as e:
            final_summary.append("[Error summarizing this chunk]")

    return '\n\n'.join(final_summary)

# AI Story Generator

Simple Streamlit app that generates short stories. It uses a local deterministic
fallback generator and can optionally call OpenAI if you set `OPENAI_API_KEY`.

Setup

1. (Optional) Create a virtual environment and activate it.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=sk-...
```

Running

Start the Streamlit app:

```bash
streamlit run app.py
```

PowerShell note

If you see a PowerShell profile/script execution warning, it's about your
profile script being blocked by Windows execution policy and is informational.
You can run the app even if that message appears. To temporarily allow scripts
in the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Security

- Use `RemoteSigned` or another restricted policy for daily use rather than
  leaving unrestricted execution enabled permanently.
- Keep your `OPENAI_API_KEY` secret and do not commit it to source control.

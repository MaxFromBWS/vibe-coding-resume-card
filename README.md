# AI Resume Business Card

Interactive portfolio-style resume website with modern UI, theme switching, project links, and downloadable PDF resume.

## Live Demo

- Website: [https://maxfrombws.github.io/vibe-coding-resume-card/](https://maxfrombws.github.io/vibe-coding-resume-card/)

## Features

- Hero section with profile photo and animated typing text
- Dark and light theme toggle
- Sections: About in Numbers, Services, Skills, Contacts
- Clickable project cards
- Download resume as PDF (theme-based files)
- Python script for PDF generation (`build_resume_pdf.py`)

## Tech Stack

- HTML5
- CSS3 (theme variables, animation, responsive layout)
- JavaScript (interactions and effects)
- Python + ReportLab (PDF generation)

## Project Structure

```text
.
|-- index.html
|-- build_resume_pdf.py
|-- resume-print.html
`-- assets/
    |-- profile-maxim-new.png
    |-- Resume_Maxim_Vibecoding_RU.pdf
    |-- Resume_Maxim_Vibecoding_RU_dark.pdf
    |-- Resume_Maxim_Vibecoding_RU_light.pdf
    |-- html2canvas.min.js
    `-- jspdf.umd.min.js
```

## Run Locally

1. Clone the repository.
2. Open `index.html` in a browser, or run a local server.

Example:

```bash
python -m http.server 5500
```

Then open:

- `http://localhost:5500`

## Generate PDF

Install dependency:

```bash
pip install reportlab
```

Generate files:

```bash
python build_resume_pdf.py
```

## Contact

- Telegram: [@ONYX_lab](https://t.me/ONYX_lab)
- Email: onyx.lab.chat@gmail.com
- Phone: 8-900-318-15-73

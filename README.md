# Veterinary CE Webinar Landing Page

A modern landing page for a veterinary continuing education webinar platform built with Flask and Bootstrap. The platform features a countdown timer, speaker profiles, testimonials, FAQ section, and registration functionality.

## Features

- Countdown Timer to Event Date
- Speaker Profile Section
- Testimonials
- FAQ Accordion
- Registration CTA
- 'Why Attend?' Section with Six Key Benefits
- Responsive Design
- Brand Color System Integration

## Tech Stack

- Backend: Flask
- Frontend: Bootstrap 5
- JavaScript: Vanilla JS
- CSS: Custom styling with Bootstrap integration
- Typography: Poppins font family
- Brand Colors: Navy (#1B365D), Lime (#9DC543)

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Visit `http://localhost:5000` in your browser

## Deployment

The static assets of this project are automatically deployed to GitHub Pages when changes are pushed to the main branch. You can view the live site at:
`https://margotbot.github.io/veterinary-ce-webinar/`

## Project Structure

```
├── .github/
│   └── workflows/
│       └── pages.yml
├── static/
│   ├── css/
│   │   └── custom.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       └── speaker-headshot.png
├── templates/
│   ├── base.html
│   └── index.html
├── app.py
└── main.py
```

## License

Copyright © 2024 Vet On It, LLC. All rights reserved.

# Portfolio Website - Streamlit

A modern, interactive personal portfolio website built with Python and Streamlit. Showcase your projects, skills, and experience in a beautiful, responsive web application.

## Features

✨ **Modern Design** - Clean and professional interface
🎨 **Customizable** - Easy to personalize with your information
📱 **Responsive** - Works perfectly on desktop and mobile
⚡ **Fast** - Built with Streamlit for instant rendering
🎯 **Multi-page** - Home, About, Projects, Skills, and Contact sections
✉️ **Contact Form** - Built-in contact functionality

## Pages

- **Home** - Welcome section with key statistics
- **About** - Your background and expertise
- **Projects** - Showcase your best work
- **Skills** - Display technical skills by category
- **Contact** - Contact information and message form

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Styling**: Custom CSS
- **Deployment**: Streamlit Cloud / Heroku

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio-streamlit.git
cd portfolio-streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Requirements

- Python 3.8+
- streamlit
- streamlit-lottie
- requests
- Pillow
- pandas
- plotly

## Customization

Edit `app.py` to customize:
- Your name and title
- About section content
- Projects list
- Skills categories
- Contact information

## Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repository
4. Configure and deploy

### Deploy to Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

## File Structure

```
portfolio-streamlit/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## Features Explained

### Navigation
- Sidebar navigation to switch between pages
- Smooth transitions between sections

### Styling
- Custom CSS for professional appearance
- Responsive design
- Custom skill tags

### Components
- Metrics cards for statistics
- Project cards with technology tags
- Contact form with submission handling

## Future Enhancements

- [ ] Dark mode toggle
- [ ] Blog section
- [ ] Project filtering
- [ ] Email notifications
- [ ] Analytics integration
- [ ] Resume download

## Contributing

Feel free to fork, modify, and use this template for your portfolio!

## License

MIT License - feel free to use this for your projects

## Author

Created with ❤️ using Streamlit

---

**Ready to build your portfolio?** Star this repo and get started! 🚀

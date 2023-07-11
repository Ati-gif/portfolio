from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    # About Me section
    about_me = {
        'name': 'Atianna DeAngelo',
        'bio': 'Hi! a web developer based in Utah. I have been learning new languages and creating projects since 2020. I am passionate about building software, problem-solving, and building relationships. I am a loyal and determined individual who is always willing to go above and beyond in order to make any goal or project a success.',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Ruby',],
    }

    # Project section
    projects = [
        {
            'title': 'My Portfolio',
            'description': 'Python- My portfolio website.',
            'github_url': 'https://github.com/Ati-gif?tab=repositories',
        },
        {
            'title': 'L&P Bakery',
            'description': 'Java- My end of cohort project to help build a fully functioning website for a local bakery.',
            'github_url': 'https://github.com/landonHickman/L-and-P-Bakery',
        },
        {
            'title': 'Ruby Food Court',
            'description': 'Ruby - A food court menu based on Stranger Things StarCourt mall.',
            'github_url': 'https://github.com/Ati-gif/RubyFoodCourt',
        },
    ]

    # Contact section
    contact_info = {
        'github': 'https://github.com/Ati-gif',
        'email': 'atianna.deangelo@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/atiannadeangelo/',
    }

    return render_template('portfolio.html', about_me=about_me, projects=projects, contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True)
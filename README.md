# Production Engineering - Week 1 - Portfolio Site

Welcome to the MLH Fellowship! During Week 1, you'll be using Flask to build a portfolio site. This site will be the foundation for activities we do in future weeks so spend time this week making it your own and reflect your personality!

## Tasks

Once you've got your portfolio downloaded and running using the instructions below, you should attempt to complete the following tasks.

For each of these tasks, you should create an [Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and work on them in a new [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches). When the task has been completed, you should open a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and get another fellow in your pod to give you feedback before merging it in.

*Note: Make sure to include a link to the Issue you're progressing on inside of your Pull Request so your reviewer knows what you're progressing on!*

### GitHub Tasks
- [ ] Create Issues for each task below
- [ ] Progress on each task in a new branch
- [ ] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [ ] Add a photo of yourself to the website
- [ ] Add an "About yourself" section to the website
- [ ] Add your previous work experiences
- [ ] Add your hobbies (including images)
- [ ] Add your current/previous education
- [ ] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [ ] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [ ] Create a new page to display hobbies
- [ ] Add a menu bar that dynamically displays other pages in the app


## Installation

This project has been tested with Python 3.10.

From the repository root, create and activate a project-local virtual
environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

If `python3.10` is not available as a command, use the path to your local
Python 3.10 installation.

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Create your local environment file from the committed example:

```bash
cp example.env .env
```

The `.env` file and `.venv` directory are intentionally ignored by Git. Do not
commit either one.

Start the Flask development server:

```bash
export FLASK_ENV=development
flask run --port 5001
```

You should see output similar to:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
```

Open [http://127.0.0.1:5001](http://127.0.0.1:5001) in your browser. Stop the
server with `Ctrl+C`, and leave the virtual environment with `deactivate`.

### Port 5000 on macOS

Recent versions of macOS may use port 5000 for AirPlay Receiver. If visiting
`127.0.0.1:5000` shows an HTTP 403 error, use port 5001 as shown above or
disable AirPlay Receiver in **System Settings → General → AirDrop & Handoff**.

The portfolio is only available locally while the Flask server is running.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

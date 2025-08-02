# View Recent Tweets from an X (Twitter) User

This is a simple Streamlit web application that allows users to view the **5 most recent tweets** from any public Twitter (X) account using the Twitter API v2 via **Tweepy**.

---

## Requirements

- Python 3.8+
- Twitter (X) API **bearer token**
- Public internet access

---

## Tech Stack

- [Streamlit](https://streamlit.io/) – For building the UI
- [Tweepy](https://docs.tweepy.org/en/stable/) – For interacting with the Twitter API v2
- [dotenv](https://pypi.org/project/python-dotenv/) – To manage environment variables

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install:

```bash
pip install streamlit tweepy python-dotenv
```

### 3. Add your Twitter Bearer Token

Create a `.env` file in the root of your project and add:

```env
bearer_token=your_twitter_api_bearer_token
```

---

##Running the App

```bash
streamlit run your_script_name.py
```

Then open the app in your browser at `http://localhost:8501`

---

## How It Works

- User inputs a Twitter username (without `@`)
- The app fetches the user's Twitter ID using the Tweepy Client
- It retrieves and displays the **5 most recent tweets**
- Error handling is included for:
  - Invalid usernames
  - No tweets
  - Rate limits
  - General API errors

---

## Example

**Input:**

```
elonmusk
```

**Output:**

```
Latest Tweets from @elonmusk:
2025-07-29 16:30:10: Starship is getting ready for its next launch!
2025-07-28 10:05:03: Tesla’s latest autopilot update is rolling out.
...
```

---

## Notes

- This app only works for **public Twitter accounts**
- Uses `tweet_fields=["created_at"]` to show timestamp
- Uses `max_results=5` for simplicity and rate limit awareness

---

##  License

This project is open-source and available under the [MIT License](LICENSE).

---

**Built by [Sidney](https://github.com/your-mathncode-sid)** 🚀

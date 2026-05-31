# 🔮 Space Oracle

A tiny cosmic Magic 8-Ball for your terminal, living in the **sv-test**
repository (used to exercise Spring Voyage OSS functionality). Ask a yes/no
question and the cosmos answers. No dependencies — just Python 3.10+ and a
sense of wonder.

## About this repository

<p align="center">
  <img src="docs/test-voyage.png" alt="A cherry-blossom sailboat in dry dock with a 'Test Voyage in progress' sign" width="360">
</p>

This is a **test repository** used to exercise the functionality of
[**Spring Voyage**](https://spring.voyage) — the open-source human–AI agent
collaboration platform from [CVOYA](https://cvoya.com). The little Space Oracle
project below gives the platform something real to work on: commits, pull
requests, issues, and agent/human collaboration through Spring Voyage's GitHub
connector.

- 🌐 Website: <https://spring.voyage>
- 💻 Source: <https://github.com/cvoya-com/spring-voyage>

## Usage

```bash
# Ask inline
python3 oracle.py "Will my code compile on the first try?"

# Or run it and let the Oracle prompt you
python3 oracle.py
```

Example:

```
You asked: Will my code compile on the first try?
The Oracle says: Not in this galaxy. 🌑
```

## Running the tests

```bash
python3 -m pytest        # if you have pytest
# or, no install required:
python3 -m unittest discover -p "test_*.py"
```

## License

For demo/testing purposes. Have fun out there, spacefarer. 🚀

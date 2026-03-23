# keeprule

> 100 curated investment principles from Buffett, Munger, Graham, Lynch & more — ready to use in your Python code.

[![PyPI version](https://img.shields.io/pypi/v/keeprule.svg)](https://pypi.org/project/keeprule/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Curated by [KeepRule.com](https://keeprule.com) — the investment principles encyclopedia.

## Install

```bash
pip install keeprule
```

## Quick Start

```python
import keeprule

# Get a random principle
p = keeprule.random()
print(f'"{p["text"]}" — {p["author"]}')

# Get all principles by Warren Buffett
buffett = keeprule.by_author("Buffett")
print(f"{len(buffett)} principles from Buffett")

# Search for "margin of safety"
results = keeprule.search("margin of safety")
for r in results:
    print(r["text"])
```

## API Reference

### `keeprule.random()`

Returns a random investment principle.

```python
p = keeprule.random()
# {
#   "id": 3,
#   "text": "Price is what you pay. Value is what you get.",
#   "author": "Warren Buffett",
#   "category": "Value Investing",
#   "source": "Berkshire Hathaway Shareholder Letter, 2008"
# }
```

### `keeprule.random_multiple(count)`

Returns multiple random non-repeating principles.

```python
principles = keeprule.random_multiple(5)
```

### `keeprule.by_author(name)`

Filter by author name (case-insensitive partial match).

```python
keeprule.by_author("Munger")     # All Charlie Munger principles
keeprule.by_author("Graham")     # All Benjamin Graham principles
keeprule.by_author("Lynch")      # All Peter Lynch principles
```

### `keeprule.by_category(category)`

Filter by category (case-insensitive partial match).

```python
keeprule.by_category("Risk Management")
keeprule.by_category("Value Investing")
keeprule.by_category("Mental Models")
```

### `keeprule.search(keyword)`

Full-text search across text, author, category, and source.

```python
keeprule.search("compound")      # Principles about compound interest
keeprule.search("fear")          # Principles about fear/greed
keeprule.search("intelligent")   # The Intelligent Investor references
```

### `keeprule.all()`

Returns all 100 principles.

```python
all_principles = keeprule.all()
print(f"Total: {len(all_principles)} principles")
```

### `keeprule.authors()`

Returns a sorted list of all unique author names.

```python
keeprule.authors()
# ["Albert Einstein", "Alexander Elder", "Benjamin Graham", "Charlie Munger", ...]
```

### `keeprule.categories()`

Returns a sorted list of all unique categories.

```python
keeprule.categories()
# ["Behavioral Finance", "Business Quality", "Circle of Competence", ...]
```

### `keeprule.get_by_id(id)`

Get a specific principle by its ID (1-100).

```python
p = keeprule.get_by_id(1)
# Rule No. 1: Never lose money...
```

### `keeprule.count()`

Returns the total number of principles.

```python
keeprule.count()  # 100
```

## Data Structure

Each principle is a dict with:

| Key | Type | Description |
|-----|------|-------------|
| `id` | int | Unique identifier (1-100) |
| `text` | str | The investment principle or quote |
| `author` | str | Author name |
| `category` | str | Category classification |
| `source` | str | Source reference |

## Categories

- **Value Investing** — Core value investing principles
- **Risk Management** — Managing and understanding risk
- **Market Psychology** — Understanding market behavior
- **Long-term Investing** — Patience and compound growth
- **Mental Models** — Thinking frameworks
- **Behavioral Finance** — Psychology of investing
- **Circle of Competence** — Knowing your limits
- **Decision Making** — Better investment decisions
- **Business Quality** — Evaluating businesses
- **Financial Discipline** — Spending, saving, discipline
- **Portfolio Management** — Diversification and allocation
- **Research** — Due diligence and analysis

## Featured Authors

- **Warren Buffett** — The Oracle of Omaha
- **Charlie Munger** — Berkshire Hathaway Vice Chairman
- **Benjamin Graham** — Father of Value Investing
- **Peter Lynch** — Legendary Fidelity fund manager
- **John Templeton** — Global investing pioneer
- **John Bogle** — Vanguard founder, index fund advocate
- **Jesse Livermore** — Legendary stock trader
- **Philip Fisher** — Growth investing pioneer
- **George Soros** — Quantum Fund founder

## Use Cases

- **Daily principle bot** — Display a random principle every day
- **Financial apps** — Enrich your app with curated wisdom
- **CLI tools** — Show investing tips in terminal
- **Education** — Teach investment principles programmatically
- **Data analysis** — Analyze investing wisdom patterns

## Explore More

Visit [KeepRule.com](https://keeprule.com) for:
- Interactive investment principle scenarios
- Deep-dive explanations with real-world examples
- AI-powered investment principle analysis
- Community discussions and notes

## License

MIT - see [LICENSE](LICENSE)

## Contributing

Issues and PRs welcome at [GitHub](https://github.com/henu-wang/keeprule-pypi).

## 🔗 More KeepRule Resources

### Free Tools
- [Investor Personality Quiz](https://henu-wang.github.io/investor-personality-quiz/) - Which legendary investor are you?
- [Investment Scorecard](https://henu-wang.github.io/keeprule-investment-scorecard/) - Rate any stock like Buffett
- [Portfolio Health Check](https://henu-wang.github.io/keeprule-tools/portfolio-check.html) - Grade your portfolio
- [Fear & Greed Calculator](https://henu-wang.github.io/keeprule-tools/fear-greed.html) - Market sentiment tool
- [Decision Tree](https://henu-wang.github.io/keeprule-tools/decision-tree.html) - Buy/Hold/Sell guidance
- [30-Day Challenge](https://henu-wang.github.io/keeprule-challenge/) - Transform your investing

### For Developers
- [Free API](https://henu-wang.github.io/keeprule-api/) - 100 principles, 20 authors
- [NPM Package](https://github.com/henu-wang/keeprule-npm) - `npm install keeprule`
- [PyPI Package](https://github.com/henu-wang/keeprule-pypi) - `pip install keeprule`
- [Chrome Extension](https://github.com/henu-wang/keeprule-chrome-extension)
- [Discord Bot](https://github.com/henu-wang/keeprule-discord-bot)
- [Embeddable Widget](https://github.com/henu-wang/keeprule-widget)

### Learning
- [Master Guides](https://henu-wang.github.io/keeprule-masters/) - Buffett, Munger, Graham & more
- [Free Ebook](https://henu-wang.github.io/keeprule-ebook/download.html) - 100 Investment Principles
- [Email Course](https://henu-wang.github.io/keeprule-email-course/) - 7-day Buffett course
- [Infographics](https://henu-wang.github.io/keeprule-infographics/) - Visual investing guides

---
Built by [William Wang](https://keeprule.com) | [All Tools](https://henu-wang.github.io/keeprule-hub/)

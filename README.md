# The World in One Day — Thursday 19 November 2026

A one-page newspaper front page summing up 19 November 2026, made for the
[news-image-20261119](https://make.fun/bounty/news-image-20261119) bounty
on make.fun.

## The page

Masthead date first, then one hero story and seven briefs — eight stories
across geopolitics, culture, business, US politics, the Middle East, Europe
and science, each as reported on 19 November 2026:

- **Hero:** Trump, Xi and Putin meet in Shenzhen (APEC summit)
- **Culture:** GTA VI launches worldwide
- **Middle East:** US and Iran trade fire across the Gulf
- **Business:** Anthropic's $81.3bn IPO, the largest ever
- **United States:** Jeffries set to be first Black House Speaker
- **Middle East:** Israel launches ground operation in Gaza
- **Europe:** Ukraine strikes Crimean bridge again
- **Science:** Voyager 1 reaches one light-day from Earth

The design is deliberately sparse: eight stories, not forty, so every
headline stays legible when the page is viewed at phone size.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the front page
(`entry.png`, 1024x1024, 139 KB) to `/output/entry.png`. Run it twice and
the output bytes are identical.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

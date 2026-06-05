# Lubbock Content Engine

Generate a daily batch of 3 branded, reviewed-ready Facebook posts for the "Lubbock Rent to Own Homes Available" group — complete with Higgsfield images and Canva text overlays.

---

## Spreadsheet
**ID:** `1OeOfwfTrmkiIEYEri2ON8d2TRMj3Is1F8IT2aifgUYc`

Tabs used:
- `Post History Log` — freshness check (exact: 1-year lockout, similar: 14-day lockout)
- `Knowledge Base` — RTO education facts, talking points
- `Entertainment Library` — Lubbock nostalgia, local life, pop culture topics
- `Brand Intelligence` — brand voice rules
- `Daily Queue` — write approved posts here at end

---

## Brand Voice
- Audience: "Maria" — mom, 25–45, Lubbock TX, credit-challenged, wants stability for her kids
- Tone: casual, warm, direct — like a knowledgeable friend, zero corporate language
- Never: hidden fees talk, pressure tactics, too-good-to-be-true promises
- Always: real Lubbock specifics, empathy, social proof signals
- Brand: Rent 2 Own Cribs (R2OC)

---

## Content Mix (one of each per batch)
| Type | Purpose | Example hooks |
|---|---|---|
| **Educate** | Build trust, break down RTO/homeownership concepts | "Here's the math on renting in Lubbock for 5 years..." |
| **Entertain** | Warm up the algorithm, get comments | "If you could bring back one Lubbock restaurant..." |
| **Pitch** | Drive leads, show available homes | "Available now: 3-bed brick in Frenship ISD..." |

---

## Step 1 — Read Context from Sheet

Use `google_sheets_get_many_spreadsheet_rows_advanced` (or `get_data_range`) to pull:

1. **Post History Log** — all rows; extract Topic, Content Type, Date Posted, Next Allowed Date (Similar), Next Allowed Date (Exact)
2. **Knowledge Base** — all rows with Status = Verified; extract Category, Topic, Content
3. **Entertainment Library** — all rows with Status = Active; extract Category, Topic, Content/Detail, Target Audience Fit, Freshness Rule

---

## Step 2 — Generate 3 Post Concepts

Apply the scoring matrix before writing full copy. For each of the 3 content types, generate **5 concepts** (15 total), then score each:

| Factor | Weight | Rule |
|---|---|---|
| Freshness (Exact) | 30% | 0 pts if posted within 365 days; 10 pts otherwise |
| Freshness (Similar) | 25% | 0 pts if similar posted within 14 days; 5 pts if 15–30 days; 10 pts if 30+ days |
| Audience Match | 20% | 10 pts = direct Maria match; 5 pts = broad appeal; 0 pts = mismatch |
| Engagement Potential | 15% | 10 pts = strong hook + question; 5 pts = statement; 0 pts = broadcast |
| Brand Voice | 10% | 10 pts = casual/empathetic; 0 pts = corporate/stiff |

Select the **top-scoring concept** from each type. Discard any concept that conflicts with a Post History Log lockout date.

---

## Step 3 — Write Full Post Copy

For each of the 3 winning concepts, write the complete post:

```
HOOK: [1-2 punchy lines — this is also the Canva overlay text]
BODY: [2-4 sentences max — warm, direct, no jargon]
CTA: [One clear action — prefer "Comment [KEYWORD] below" over "Click link"]
HASHTAGS: [4-6 relevant tags — always include #RentToOwn #Lubbock #Rent2OwnCribs]
```

---

## Step 4 — Generate Higgsfield Image

For each post, call `mcp__2a946e7c-eba9-4b6f-bfd0-c43ecaeb1620__generate_image` with a prompt tailored to the content type:

- **Educate**: Clean, modern infographic-style scene. Warm tones. Lubbock neighborhood feel. No text in image.
- **Entertain**: Warm, nostalgic, relatable lifestyle photo matching the topic (restaurant, local spot, family moment). No text in image.
- **Pitch**: Bright, inviting exterior or interior of a home. Suburban Lubbock feel. No text in image.

Keep all image prompts photo-realistic, warm, aspirational. Target audience is a mom who wants a safe, stable home for her kids. Always end the prompt with: `no text, no watermarks, photorealistic, warm lighting, aspirational`

Wait for each image job to complete before moving to Step 5.

---

## Step 5 — Canva Text Overlay

For each Higgsfield image:

1. Upload the image to Canva using `mcp__b96d0f74-7168-4eb8-a60b-3cb573b89588__upload-asset-from-url`
2. Create a Facebook post design (1200×630px) using `generate-design-structured` with:
   - Background: the uploaded Higgsfield image
   - Primary text: the **HOOK** from Step 3 (bold, high contrast, readable on mobile)
   - Brand tag: "Rent 2 Own Cribs" in smaller text, bottom corner
   - Keep text minimal — the image does the work, the hook seals it
3. Export the design using `export-design` (PNG format)

---

## Step 6 — Present for Review

Show all 3 posts in the conversation in this format:

---
### Post 1 — [ENTERTAIN / EDUCATE / PITCH]
**Score:** [X/100]
**Hook:** [hook text]
**Body:** [full post copy]
**CTA:** [call to action]
**Hashtags:** [tags]
**Image:** [Canva export link or thumbnail]

---

Ask: "Approve all 3, or any tweaks before I write to the sheet?"

---

## Step 7 — Write Approved Posts to Sheet

For each approved post, append a row to the **Daily Queue** tab with:
- Post ID: `DQ-[next number]`
- Date: today's date
- Content Type: Educate / Entertain / Pitch
- Platform: Facebook
- Status: **Approved**
- Post Copy: full text (hook + body + CTA + hashtags)
- Hook: hook line only
- CTA: CTA line only
- Hashtags: hashtag string
- Image Notes: Canva export URL
- Notes: "Generated by lubbock-content-engine skill"

Then append a row to the **Post History Log** tab for each post:
- Date Posted: today
- Content Type
- Topic / Theme
- Exact Hook Used
- Engagement Score: (leave blank — to be filled after posting)
- Next Allowed Date (Similar): today + 14 days
- Next Allowed Date (Exact): today + 365 days

---

## Step 8 — Confirm

Report back: "3 posts written to Daily Queue. [list the 3 hooks]. Ready to post."

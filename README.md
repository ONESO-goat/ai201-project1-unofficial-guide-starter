# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain


"Hackthons for students", this can include free - paid - beginner - AI produced - etc.

---

## Document Sources

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | reddit/hackthons |place to find hackthons | |
| 2 | reddit/tech  | place to find tech related events| |
| 3 | reddit/cs | place to find cs related events| |
| 4 | reddit/networking | place to find networking related events| |
| 5 | google/hackathons | place to find hackthons | |
| 6 | your-univerity/college-website/tech | place to find tech related events | |
| 7 | your-univerity/clubs | place to find clubs inside your school| |
| 8 | your-city/local event | place to find local events | |
| 9 | Devpost/Hackathons| web application with hackathons
| 10 | MLH.io | place filled with hackathons| |

---

## Chunking Strategy


**Chunk size:** 300

**Overlap:** 60

**Why these choices fit your documents:** Simple queries

**Final chunk count:** 3-5

---

## Embedding Model



**Model used:** "llama-3.3-70b-versatile"

**Production tradeoff reflection:**
Some responses are intentionally concise because the bot prioritizes information from its hackathon focused training data. Given the scope of this project, I focused on core functionality and retrieval quality. For a production or public facing deployment, I would invest additional effort in response refinement, broader knowledge coverage, and user experience improvements.

---

## Grounded Generation

**System prompt grounding instruction:** Extract and prioritize the user's key constraints and intent from the query. For example:

User query:
"What are **free**, **long-term** hackathons that are coming this **year** in **my area**?"

Key information to retain:

* Event type: Hackathons
* Cost constraint: Free
* Duration constraint: Long-term
* Time constraint: This year / upcoming
* Location constraint: User's area
* Intent: Discover and recommend relevant events matching all specified criteria

The assistant should use these constraints to guide retrieval, ranking, and response generation.

**How source attribution is surfaced in the response:** Include a source citation or event link for every recommended hackathon. Clearly associate each recommendation with its source so users can verify event details, dates, eligibility requirements, and registration information.


---

## Evaluation Report

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | "What are some upcoming hackathons near me?" |  "list of hackathons near me" |
| 2 | "What are some free hackathons near me?" | "list of free hackthons" |

| 3 | "Who are the winners from the '<hackathon name>' hackathon?" | "Name or Names of winners" |
| 4 | "I want to focus on <field>, which tech event is best to gain the knowledge?"| "List of events that related to that spific field" |
| 5 | "What hackathons will be taking place in <state>? | "List of hackathons inside that state" |

**Retrieval quality:** **Relevant** / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:** What are some hackathons that are happening in massachusetts?

**What the system returned:** Doesn't know based on provided results

**Root cause (tied to a specific pipeline stage):** There weren't any hackthons available for massachusetts


**What you would change to fix it:** Add/find hackathons that are occuring in massachusetts



---

## Spec Reflection

I had to figure where I was going to grab data for hackathons that wasn't going to be a hurdle. I decided to use MLH and got this response from my AI:

     Here are some free hackathons:

     1. **GDG Solution Hacks** - June 27-29, Toronto, Canada
     2. **SpurHacks** - June 20-22, Waterloo, Ontario, Canada
     3. **Hack4Bengal 4.0** - June 20-22, Newtown, West Bengal, India
     4. **Hack 4 Her** - June 14-15, Monterrey, Nuevo León, Mexico
     5. **Global Hack Week: GenAI** - June 13-19, Everywhere, Worldwide
     6. **MasseyHacks** - May 17-18, Windsor, Ontario, Canada
     7. **JAMHacks 9** - May 16-18, Waterloo, Ontario, Canada
     8. **NMIT HACKS 2025** - May 16-18, Bengaluru, Karnataka, India
     9. **DesignVerse at UCR** - May 10-11, Riverside, California, US
     10. **HACKMESA** - May 9-10, Los Angeles, CA, US
     11. **Global Hack Week: Open Source Week** - May 9-15, Everywhere, Worldwide
     12. **GDSCHACKS** - May 2-4, Guelph, Ontario, Canada
     13. **HackUPC** - May 2-4, Barcelona, Catalunya, Spain
     14. **HackDartmouth X** - April 26-27, Hanover, New Hampshire, US
     15. **DragonHacks 11** - April 26-27, Philadelphia, PA, US
     16. **JacHacks** - April 26-27, Quebec, Sainte-Anne-de-Bellevue, Canada
     17. **MorganHacks** - April 26-27, Baltimore, Maryland, US
     18. **Hacktech by Caltech** - April 25-27, Pasadena, CA, US
     19. **LA Hacks** - April 25-27, Los Angeles, California, US
     20. **HackDavis 2025** - April 19-20, Davis, California, US
     21. **UTA Datathon** - April 12-13, Arlington, Texas, US
     22. **Hackabull** - April 12-13, Tampa, Florida, US
     23. **Bit Hacks** - April 11-13, Irvine, California, US
     24. **Bitcamp 2025** - April 11-13, College Park, Maryland, US

     All of these hackathons are free to attend.

This response shows strong understanding, quick explaining, and successful implemation and formatting.

**One way the spec helped you during implementation:**

The specification helped define which parts of the user's query were most important to extract and preserve (e.g., location, cost, timeframe, and event type). This made it easier to design the retrieval and ranking logic because the bot could consistently prioritize hackathons that matched the user's stated constraints.


**One way your implementation diverged from the spec, and why:**
The implementation did not always enforce every constraint perfectly when relevant data was limited. For example, if there were few or no free long-term hackathons available in the user's area, the bot could return partially matching results instead of no results at all. This tradeoff was made to improve usefulness and provide users with potentially relevant alternatives rather than an empty response.
---

## AI Usage


**Instance 1** Debugging

- *What I gave the AI:* Buggy code and terminal tracebacks
- *What it produced:*  Possible fixes
- *What I changed or overrode:* Kept prompting until confusing bugs disappeared

**Instance 2** finding sources for hackathons 

- *What I gave the AI:* Sites with free APIS for hackathons
- *What it produced:* Sites to use with free APIs for the "request" package
- *What I changed or overrode:* Changed the info into readable code or inside classes

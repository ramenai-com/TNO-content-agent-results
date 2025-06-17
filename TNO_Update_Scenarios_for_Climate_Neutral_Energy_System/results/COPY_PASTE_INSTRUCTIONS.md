# Copy & Paste Instructions for TNO CMS

## Task Summary
**Task**: Update climate scenarios page with improved storytelling using accordion blocks
**Pages to update**:
- English: https://www.tno.nl/en/sustainable/system-solutions-environment/transition-pathways/scenarios-climate-neutral-energy-system/
- Dutch: https://www.tno.nl/nl/duurzaam/systeemoplossingen-omgeving-milieu/transitiepaden/scenario-klimaatneutraal-energiesysteem/

## Quick Copy/Paste Guide

### Step 1: Open Your CMS
1. Log into the TNO CMS
2. Navigate to the English climate scenarios page
3. Switch to edit mode

### Step 2: Copy English Content
1. Open file: `./results/english_climate_scenarios_improved.md`
2. Copy everything EXCEPT the first section (CMS Implementation Instructions)
3. Start copying from: "## Your Journey to Climate Neutrality Starts Here"

### Step 3: Paste into CMS
1. Replace the existing page content
2. For each section marked with "🔽 ACCORDION":
   - Create a new accordion block in your CMS
   - Use the section title (without the emoji and "ACCORDION:" text)
   - Paste the content into the accordion body

### Step 4: Configure Accordions
Set these properties for each accordion:
- **Default state**: Collapsed
- **Allow multiple open**: Yes
- **Animation**: Slide (300ms)

### Step 5: Repeat for Dutch
1. Open file: `./results/dutch_climate_scenarios_improved.md`
2. Navigate to the Dutch page in CMS
3. Repeat steps 2-4 with Dutch content

## Accordion Structure Overview

You need to create 6 accordion blocks:

1. **Understanding the Challenge** / **De uitdaging begrijpen**
2. **Two Futures, Two Choices** / **Twee toekomsten, twee keuzes**
3. **Your Sector's Transformation Path** / **Het transformatiepad voor uw sector**
4. **Critical Success Factors** / **Kritieke succesfactoren**
5. **Making It Real - Implementation Roadmap** / **Het werkelijkheid maken**
6. **Your Next Steps** / **Uw volgende stappen**

## Content That Stays Visible
Keep these sections always visible (not in accordions):
- Main title
- Opening paragraphs about the journey to climate neutrality
- "Choose Your Path" section

## Final Checklist
- [ ] All 6 accordions created on English page
- [ ] All 6 accordions created on Dutch page
- [ ] Cross-language links updated at bottom of each page
- [ ] Preview both pages to ensure accordions work
- [ ] Test on mobile device
- [ ] Publish both pages

## Files Location
All improved content is in the `./results/` directory:
- English content: `english_climate_scenarios_improved.md`
- Dutch content: `dutch_climate_scenarios_improved.md`
- Detailed guide: `CMS_implementation_guide.md`

## Support
If you need the detailed implementation guide with styling recommendations and technical specifications, refer to `./results/CMS_implementation_guide.md`
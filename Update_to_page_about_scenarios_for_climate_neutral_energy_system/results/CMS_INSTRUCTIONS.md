# CMS Update Instructions for TNO Scenarios Pages

## Overview
This document contains improved content for the TNO "Scenarios for a climate-neutral energy system" pages in both English and Dutch. The content has been restructured with better storytelling flow and organized using accordion blocks for improved user experience.

## Pages to Update

### 1. English Page
**URL:** https://www.tno.nl/en/sustainable/system-solutions-environment/transition-pathways/scenarios-climate-neutral-energy-system/

### 2. Dutch Page  
**URL:** https://www.tno.nl/nl/duurzaam/systeemoplossingen-omgeving-milieu/transitiepaden/scenario-klimaatneutraal-energiesysteem/

## Implementation Instructions

### Step 1: Backup Current Content
Before making any changes, please backup the current page content in your CMS.

### Step 2: Page Structure Update

The new content structure consists of:
1. **Page Title** (remains the same)
2. **Introduction Section** (2-3 paragraphs setting up the challenge)
3. **Main Content Title** ("Two Pathways to Climate Neutrality" / "Twee Routes naar Klimaatneutraliteit")
4. **8 Accordion Blocks** containing the main content
5. **Conclusion Section**
6. **Contact Information**

### Step 3: Accordion Block Implementation

Each accordion block should be implemented with:
- **Collapsed by default** (users click to expand)
- **Clear, descriptive titles** that encourage clicking
- **Smooth expand/collapse animation**
- **Plus/minus or arrow indicators** for open/closed state

The accordion blocks are marked in the content as:
```
### [Accordion Block X: Title]
```

### Step 4: Content Migration

#### For English Version:
1. Open file: `./results/tno_scenarios_english_improved.md`
2. Copy the entire content
3. In CMS, navigate to the English page
4. Replace existing content with the new structured content
5. Configure each section marked as "Accordion Block" as an actual accordion element

#### For Dutch Version:
1. Open file: `./results/tno_scenarios_dutch_improved.md`
2. Copy the entire content
3. In CMS, navigate to the Dutch page
4. Replace existing content with the new structured content
5. Configure each section marked as "Accordeon Blok" as an actual accordion element

### Step 5: Formatting Guidelines

- **Headers:** Use the header levels as indicated (# = H1, ## = H2, ### = H3)
- **Bold text:** Apply to key phrases and section introductions
- **Bullet points:** Maintain formatting for lists
- **Links:** Ensure all existing links (PDF downloads, contact info) remain functional

### Step 6: Visual Elements

Consider adding:
- **Hero image** at the top showcasing renewable energy
- **Icons** for each accordion block to improve visual appeal
- **Infographics** showing the difference between ADAPT and TRANSFORM scenarios
- **Call-to-action buttons** for downloading the full report

### Step 7: SEO Considerations

- Maintain existing URL structure
- Update meta descriptions to reflect the improved content structure
- Ensure accordion content is crawlable by search engines

### Step 8: Quality Check

After implementation:
1. Test all accordion blocks open/close properly
2. Verify all links work correctly
3. Check mobile responsiveness
4. Ensure content hierarchy is clear
5. Test page load speed (accordions should improve this)

## Key Improvements Made

1. **Narrative Flow:** Content now tells a story from challenge → solutions → implementation → action
2. **Clarity:** ADAPT and TRANSFORM scenarios are introduced early and explained clearly
3. **Organization:** Related information is grouped together in themed accordion blocks
4. **Engagement:** Accordion structure allows users to explore topics of interest
5. **Action-Oriented:** Clear next steps for different stakeholder groups
6. **Accessibility:** Cleaner structure improves content scanning and navigation

## Technical Notes

- If your CMS doesn't support accordion blocks natively, consider using:
  - Built-in accordion widgets/modules
  - Custom HTML/CSS/JavaScript implementation
  - Third-party accordion plugins compatible with your CMS

## Contact for Questions

If you have any questions about implementing these changes, please refer to the original Smartsheet task (Row ID: 7398723649671044) or contact the content team.

---

**Files Provided:**
- `/results/tno_scenarios_english_improved.md` - Complete English content
- `/results/tno_scenarios_dutch_improved.md` - Complete Dutch content
- `/results/CMS_INSTRUCTIONS.md` - This instruction file